import os
import keyboard 
import subprocess
import time

while(True):
    try:
        time.sleep(0.05)
        if keyboard.is_pressed('alt+5'):   
            si = subprocess.STARTUPINFO()
            si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
            subprocess.Popen('taskkill /F /IM cmd.exe', startupinfo=si)
            os.system("SndVol.exe")
            time.sleep(0.05)
            continue
    except:
        continue

