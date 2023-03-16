import hashlib
import pickle
import pandas as pd

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

