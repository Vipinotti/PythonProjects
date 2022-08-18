import pyautogui, time
time.sleep(5)
f = open("", 'r') #put your file name or repository(.txt) inside the "".
for word in f:
    pyautogui,typewrite(word)
    pyautogui.press("enter")