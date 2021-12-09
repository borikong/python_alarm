from playsound import playsound
import winsound
import time

def loop():
    winsound.Beep(5000, 500)
    time.sleep(0.3)
while True:
    for i in range(7):
        loop()

    time.sleep(300)
    print("5분 경과")
    time.sleep(300)
    print("10분 경과")
    time.sleep(600)
    print("20분 경과")
    time.sleep(600)
    print("30분 경과")

    # time.sleep(2100)
