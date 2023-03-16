import hashlib
import pickle
import pandas as pd
import requests
#hash function
def md5hash(filepath):
    with open(filepath, 'rb') as f:
        data = f.read()
        return hashlib.md5(data).hexdigest()

# Example usage

# enter filename here
hash = md5hash('hello.txt')

#opening trained model
with open('malware_detection_model.pkl', 'rb') as file:
    rf = pickle.load(file)

# reading data file
data= pd.read_csv('top_1000_pe_imports.csv')


test_hash = hash


test_data = data[data['hash'] == test_hash]

test_X = test_data[['OpenProcess', 'LoadLibraryA', 'GetProcessHeap', 'ShellExecuteW', 'VirtualFree', 'GetDC', 'IsDebuggerPresent', 'malloc', 'FindNextFileA', 'free', 'GetAsyncKeyState', 'GetTickCount', 'exit', '_cexit', 'VirtualAlloc', 'VirtualProtect', 'GetModuleHandleA', 'ExitProcess', 'RegCloseKey','GetCurrentProcessId']]
try:
    prediction = rf.predict(test_X)
    if prediction[0] == 1:
        print('The file is malicious')
    else:
        print('The file is not malicious')
except ValueError:
    print('file is not malicious ')


print('VirusTotal Verification')

def lookup_hash(hash_value, api_key):
    url = f"https://www.virustotal.com/vtapi/v2/file/report?apikey={api_key}&resource={hash_value}"
    response = requests.get(url)
    if response.status_code == 200:
        result = response.json()
        if result["response_code"] == 0:
            print(f"file not found in VirusTotal database.")
        elif result["positives"] == 0:
            print(f"file is not malicious according to VirusTotal.")
        else:
            print(f"file is malicious according to VirusTotal.")
    else:
        print("Error fetching data from VirusTotal.")

lookup_hash(test_hash,'0ce5cb0b16c6be24b31ce39653359444dd3a3a761ba0d7f29ad3bc67e226f69a')
