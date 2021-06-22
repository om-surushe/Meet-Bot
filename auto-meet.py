import webbrowser
import pyautogui
import time
import datetime
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
webbrowser.register("chrome",None,webbrowser.BackgroundBrowser(chrome_path))
def join(url):
    webbrowser.get("chrome").open_new_tab(url)
    time.sleep(10) 
    pyautogui.click(610, 810)
    time.sleep(5)
    pyautogui.click(720, 810) 
    time.sleep(2)
    pyautogui.click(1360, 640) 
    time.sleep(2)
    
timej = int(input("Please enter the time: "))
meetlink = input("Please enter the link: ")
m=0
while True:
    strtime= datetime.datetime.now().strftime('%H:%M:%S')
    hour = int(strtime[:2])
    minute = int(strtime[3:5])
    seconds = int(strtime[6:])
    print(hour)


    if hour == timej and m==0 :
        m=m+1
        join(meetlink)
