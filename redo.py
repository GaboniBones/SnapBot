import schedule
import time
import pickle
import pyautogui as pg
from pyclick import HumanClicker
hc = HumanClicker()


anchors = []


with (open("redo.txt", "rb")) as openfile:
    while True:
        try:
            anchors.append(pickle.load(openfile))
        except EOFError:
            break
anc1 = []
with open('redo.txt', 'rb') as openfile:
    try:
        anc1.append(pickle.load(openfile))
    except:
        print('File read error')
t1, t2, t3, t4, t5, t6 = anc1[0]

def send():
    hc.move(t2, 1)
    pg.click(t2)
    hc.move(t3, 1)
    pg.click(t3)
    hc.move(t4, 1)
    pg.click(t4)
    hc.move(t5, 1)
    pg.click(t5)
    hc.move(t6, 1)
    pg.click(t6)
    hc.move(t1, 1)
    pg.click(t1)
    print(":: Streak Sent! ::")
    print(":: Bot Running Again At 1 Pm ::")


print(":: Bot Running At 1 Pm ::")
schedule.every().day.at("13:00").do(send)

while True:
    schedule.run_pending()
    time.sleep(1)



























