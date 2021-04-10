import pyautogui as pg
import pickle
import time
import keyboard
anchors = []
import os
from os import system, name
import schedule

print("  :: Press enter when Over Camera Button ::")
if keyboard.read_key() == "enter":
    pos1 = pg.position()
    anchors.append(pos1)
    print(":: Coords Captured! ::")
time.sleep(0.5)
print("  :: Press Enter When Over Picture Button :: ")
if keyboard.read_key() == "enter":
    pos2 = pg.position()
    anchors.append(pos2)
    print(":: Coords Captured! ::")
time.sleep(0.5)
print("  :: Press Enter When Over Pick Button")
if keyboard.read_key() == "enter":
    pos3 = pg.position()
    anchors.append(pos3)
    print(":: Coords Captured! ::")
time.sleep(0.5)
print("  :: Press Enter When Over Group Button ::")
if keyboard.read_key() == "enter":
    pos4 = pg.position()
    anchors.append(pos4)
    print(":: Coords Captured! ::")
time.sleep(0.5)
print("   :: Click Enter When Over Person Button ::")
if keyboard.read_key() == "enter":
    pos5 = pg.position()
    anchors.append(pos5)
    print(":: Coords Captured! ::")
time.sleep(0.5)
print("    :: Press Enter When Over Send Button ::")
if keyboard.read_key() == "enter":
    pos6 = pg.position()
    anchors.append(pos6)
    print(":: Coords Captured! ::")


with open('redo.txt', 'wb') as fp:
    pickle.dump(anchors, fp)

print('anchors = ', anchors)

anc1 = []
# append the anchors list to the list anc1, which results in a list of lists
with open('redo.txt', 'rb') as openfile:
    try:
        anc1.append(pickle.load(openfile))
    except:
        print('File read error')
print("anc1 = ", anc1)  # anc1 is a list whose first and only element is the original anchors list
t1, t2, t3, t4, t5, t6 = anc1[0]  # note that we use anc1[0] instead of anc1
print('t1 =', t1)
print('t2 =', t2)
print('t3 =', t3)
print('t4 =', t4)
print('t5 =', t5)
print('t6 =', t6)

def clear():
    if name == 'nt':
        _ = system('cls')

def send():
    pg.moveTo(t2, duration=1)
    pg.click(t2)
    pg.moveTo(t3, duration=2)
    pg.click(t3)
    pg.moveTo(t4, duration=1)
    pg.click(t4)
    pg.moveTo(t5, duration=1)
    pg.click(t5)
    pg.moveTo(t6, duration=1)
    pg.click(t6)
    pg.moveTo(t1, duration=1)
    pg.click(t1)


time.sleep(2)
print(":: Go Back To Picture Page And Press Enter ::")
if keyboard.read_key() == "enter":
    send()
clear()
with open("redo.py") as infile:
    exec(infile.read())











































