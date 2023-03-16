# Using RandomForestClassifier
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# importing dataset
data= pd.read_csv('top_1000_pe_imports.csv')

#
df= data[['OpenProcess', 'LoadLibraryA', 'GetProcessHeap', 'ShellExecuteW', 'VirtualFree', 'GetDC', 'IsDebuggerPresent', 'malloc', 'FindNextFileA', 'free', 'GetAsyncKeyState', 'GetTickCount', 'exit', '_cexit', 'VirtualAlloc', 'VirtualProtect', 'GetModuleHandleA', 'ExitProcess', 'RegCloseKey','GetCurrentProcessId', 'malware']]
y= df['malware']
X= df.drop(['malware'], axis=1)

print(X.shape, y.shape)

X_train, X_test, y_train, y_test= train_test_split(X, y, test_size=0.2, random_state=2)

# training
rf = RandomForestClassifier(n_estimators=1600,
                            random_state=3,
                            bootstrap= True,
                            max_depth= 110,
                            max_features= 3,
                            min_samples_leaf= 2,
                            min_samples_split= 10)
rf.fit(X_train,y_train)


print("Train Accuracy:",rf.score(X_train, y_train) )#accuracy
import pickle
with open('malware_detection_model.pkl', 'wb') as f:
    model = pickle.dump(rf,f)






