# Python 3.9
# Created 20210928 10:45
# autoMouse.py is to automatically move the mouse to keep teams online

# Use pyautogui package
import math
import sys

import pyautogui as pg
# import time
import datetime
# import keyboard
# import sys

def moyufun():
    # starttime = datetime.datetime.now()
    # Set radius
    R = 400
    # Measure screen size
    (x, y) = pg.size()
    # Locating center of the screen
    (X, Y) = pg.position(x / 2, y / 2)
    # Offsetting by radius
    pg.moveTo(X + R, Y)
    dif = 0
    while True:
        i = 0
        while i < 360:
            pg.moveTo(X + R * math.cos(math.radians(i)), Y + R * math.sin(math.radians(i)))
            # print(int(X + R * math.cos(math.radians(i))), int(Y + R * math.sin(math.radians(i))))
            (Xnow, Ynow) = pg.position()
            # print(Xnow, Ynow)
            if (Xnow != int(X + R * math.cos(math.radians(i)))) | (Ynow != int(Y + R * math.sin(math.radians(i)))):
                print("You stop Moyu!!!!!!")
                sys.exit(0)
            i = i + 15
        # time.sleep(120)
        # endtime = datetime.datetime.now()
        # dif = (endtime - starttime).seconds

# Moyutime = input("Input your Moyu time in minute:")
moyufun()

# def moyufun(MoyuTime):
#     starttime = datetime.datetime.now()
#     # Set radius
#     R = 400
#     # Measure screen size
#     (x, y) = pg.size()
#     # Locating center of the screen
#     (X, Y) = pg.position(x / 2, y / 2)
#     # Offsetting by radius
#     pg.moveTo(X + R, Y)
#     dif = 0
#     while dif < int(MoyuTime) * 60:
#         i = 0
#         while i < 360:
#             pg.moveTo(X + R * math.cos(math.radians(i)), Y + R * math.sin(math.radians(i)))
#             # print(int(X + R * math.cos(math.radians(i))), int(Y + R * math.sin(math.radians(i))))
#             (Xnow, Ynow) = pg.position()
#             # print(Xnow, Ynow)
#             if (Xnow != int(X + R * math.cos(math.radians(i)))) | (Ynow != int(Y + R * math.sin(math.radians(i)))):
#                 print("You stop Moyu!!!!!!")
#                 sys.exit(0)
#             i = i + 15
#         # time.sleep(120)
#         endtime = datetime.datetime.now()
#         dif = (endtime - starttime).seconds
#
# Moyutime = input("Input your Moyu time in minute:")
# moyufun(Moyutime)

# def moveMouse():
#     # Set radius
#     R = 400
#     # Measure screen size
#     (x, y) = pg.size()
#     # Locating center of the screen
#     (X, Y) = pg.position(x / 2, y / 2)
#     # Offsetting by radius
#     pg.moveTo(X + R, Y)
#     # Setting pace with a mouduls
#     i = 0
#     while i < 360:
#         pg.moveTo(X + R * math.cos(math.radians(i)), Y + R * math.sin(math.radians(i)))
#         # print(int(X + R * math.cos(math.radians(i))), int(Y + R * math.sin(math.radians(i))))
#         # (Xnow, Ynow) = pg.position()
#         # # print(Xnow, Ynow)
#         # if (Xnow != int(X + R * math.cos(math.radians(i)))) | (Ynow != int(Y + R * math.sin(math.radians(i)))):
#         #     print("You stop Moyu!!!!!!")
#         #     return False
#         #     break
#         i = i + 15
#
# # def tasklist(MoyuTime):
# #     schedule.clear()
# #     schedule.every(2).seconds.do(moveMouse())
# #     for i in range(MoyuTime):
# #         schedule.run_pending()
# #         time.sleep(2)
#
# def loopMoyu(MoyuTime):
#     starttime = datetime.datetime.now()
#     dif = 0
#     while dif < int(MoyuTime) * 10:
#         moveMouse()
#         # time.sleep(120)
#         endtime = datetime.datetime.now()
#         dif = (endtime - starttime).seconds





