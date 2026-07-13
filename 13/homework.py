import random
import subprocess
import threading
import time
import webbrowser
from win10toast import ToastNotifier

toaster=ToastNotifier()


subprocess.Popen(["D:/Program Files/NetBeans-14/netbeans/bin/netbeans64.exe"])

messages=["Take a break",
    "You've studied enough"
          ]

(webbrowser.get("C:/Program Files/Google/Chrome/Application/chrome.exe %s")
 .open("https://itskola.net/"))

def message():
    while True:
        toaster.show_toast("Reminder", random.choice(messages), duration=2)
        time.sleep(60)

thread_message=threading.Thread(target=message())
thread_message.start()