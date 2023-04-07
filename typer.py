import pyautogui
import time

def write(s):
    if s=="<":
        pyautogui.hotkey("shift",",")
    else:
        pyautogui.write(s,interval=0.001)

f=open("text.txt")
txt = f.read()

print("Starting typer")
python = True

if "printf" in txt or "System.out.println" in txt:
    python = False
    print("Detected language Python")

if not python:
    if "printf" in txt:
        print("Detected language C")
    else:
        print("Detected language Java")

s = txt.split("\n")
time.sleep(3)

if not python:
    #remove tab space
    for i in s:

        if "<" in i:
            flag=0
            for j in i:
                if flag == 0 and j!=" ": 
                    flag=1 
                    write(j) 
                elif flag ==1: 
                    write(j) 
        else:
            idx=0
            for j in i:
                if j==" ":
                    idx+=1
                else:
                    break
            write(i[idx:])
        write("\n")
else:
    space=0
    prev_space = 0
    for i in s:
        for j in i:
            if j==" ":
                space+=1
            else:
                break
        if(space == prev_space):
            write(i[space:])
        elif space > prev_space:
            write(i[space:])
        else:
            c = int((prev_space - space)/4)
            write("\n")
            for k in range(c):
                pyautogui.hotkey("backspace")
            write(i[space:])
        prev_space = space
        space = 0
        write("\n")

#clear extra curly braces and stuff
if not python:
    pyautogui.keyDown("Delete")
    time.sleep(3)
    pyautogui.keyUp("Delete")

