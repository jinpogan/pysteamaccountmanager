def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)
def login(name):
    cmd('''taskkill /f /im steam.exe''')
    time.sleep(2)
    cmd('''reg add "HKCU\Software\Valve\Steam" /v AutoLoginUser /t REG_SZ /d '''+name+" /f")
    cmd('''reg add "HKCU\Software\Valve\Steam" /v RememberPassword /t REG_DWORD /d 1 /f''')
    import subprocess
    subprocess.Popen(r"C:\Program Files (x86)\Steam\Steam.exe ")
def editaccs():
    cmd("notepad %appdata%\steamaccman.txt ")
    quit()
import tkinter as tk
import json
import subprocess
import codecs
import time
import os
from PIL import ImageTk, Image
from os import system as cmd
root = tk.Tk()
root.minsize(300, 0)
button_list = []
root.iconbitmap(resource_path('image.ico'))
root.title("Steam账号登录")
root.resizable(False, False)
img=ImageTk.PhotoImage(Image.open(resource_path("small.png")))
tk.Label(root, image = img ).place(x=150,y=0)
if os.path.exists(os.getenv('APPDATA')+"\steamaccman.txt"):
    while (1):
        try:
            with codecs.open(os.getenv('APPDATA')+"\steamaccman.txt",encoding='utf-8') as f:
                accounts=json.loads(f.read())
        except Exception as e:
            try:
                with codecs.open(os.getenv('APPDATA')+"\steamaccman.txt",encoding='utf-8') as f:
                    accounts=json.loads(f.read().encode().decode('utf-8-sig'))
            except Exception as e:
                with codecs.open(os.getenv('APPDATA')+"\steamaccman.txt","w",encoding='utf-8') as f:
                    f.write('''{"<把这个删掉改成用户名>":"<把这个删掉改备注>","<把这个删掉改成用户名>":"<把这个删掉改备注>","<把这个删掉改成用户名>":"<把这个删掉改备注>"}''')
                cmd("notepad %appdata%\steamaccman.txt")
        if accounts=={} or accounts=={"<把这个删掉改成用户名>":"<把这个删掉改备注>","<把这个删掉改成用户名>":"<把这个删掉改备注>","<把这个删掉改成用户名>":"<把这个删掉改备注>"}:
            with codecs.open(os.getenv('APPDATA')+"\steamaccman.txt","w",encoding='utf-8') as f:
                f.write('''{"<把这个删掉改成用户名>":"<把这个删掉改备注>","<把这个删掉改成用户名>":"<把这个删掉改备注>","<把这个删掉改成用户名>":"<把这个删掉改备注>"}''')
            cmd("notepad %appdata%\steamaccman.txt")
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
    with codecs.open(os.getenv('APPDATA')+"\steamaccman.txt","w",encoding='utf-8') as f:
        f.write('''{"<把这个删掉改成用户名>":"<把这个删掉改备注>","<把这个删掉改成用户名>":"<把这个删掉改备注>","<把这个删掉改成用户名>":"<把这个删掉改备注>"}''')
    cmd("notepad %appdata%\steamaccman.txt")
