def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)
def login(name):
    cmd('''C:\Program Files (x86)\Steam\steam.exe -shutdown''')
    time.sleep(2)
    cmd('''reg add "HKCU\Software\Valve\Steam" /v AutoLoginUser /t REG_SZ /d '''+name+" /f")
    cmd('''reg add "HKCU\Software\Valve\Steam" /v RememberPassword /t REG_DWORD /d 1 /f''')
    cmd('''C:\Program Files (x86)\Steam\steam.exe''')
def editaccs():
    cmd("notepad %appdata%\steam账号管家无毒绿色版.txt ")
    os.execl("steam账号管家无毒绿色版.exe")
    quit()
import tkinter as tk
import json
import codecs
import sys
import time
import os
from os import system as cmd
root = tk.Tk()
button_list = []
root.iconbitmap(resource_path('image.ico'))
root.title("steam账号管家无毒绿色版")
root.resizable(False, False)
if os.path.exists(os.getenv('APPDATA')+"\steam账号管家无毒绿色版.txt"):
    while (1):
        try:
            with codecs.open(os.getenv('APPDATA')+"\steam账号管家无毒绿色版.txt",encoding='utf-8') as f:
                accounts=json.loads(f.read())
        except:
            with codecs.open(os.getenv('APPDATA')+"\steam账号管家无毒绿色版.txt",encoding='utf-8') as f:
                accounts=json.loads(f.read().encode().decode('utf-8-sig'))
        if accounts=={} or accounts=={"<把这个删掉改成用户名>":"<把这个删掉改备注>","<把这个删掉改成用户名>":"<把这个删掉改备注>","<把这个删掉改成用户名>":"<把这个删掉改备注>"}:
            cmd("copy  accounts.txt %appdata%\steam账号管家无毒绿色版.txt  ")
            cmd("notepad %appdata%\steam账号管家无毒绿色版.txt")
        else:
            break
    counter=0
    for account in accounts.keys():
        button_list.append(tk.Button(root, text=accounts[account], command=lambda account=account: login(account)))
        button_list[-1].grid(row=counter, column=0)
        counter=counter+1
    tk.Button(root, text="添加/删除账号", command=editaccs).grid(row=counter+2, column=0,pady= 20,)
    root.mainloop()
else:
    print(e)
    print("2")
    cmd("copy accounts.txt %appdata%\steam账号管家无毒绿色版.txt  ")
    cmd("notepad %appdata%\steam账号管家无毒绿色版.txt")
