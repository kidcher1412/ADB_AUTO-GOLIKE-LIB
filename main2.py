import time
import cv2
import numpy as np
import subprocess
import os
def click_pos(X,Y):
    comd="adb -s RWLJYXYD8TOZGYEM shell input tap "+str(X)+" "+str(Y)
    print(comd)
    os.system(comd)
def find_image(picture1,picture2):
    img_rgb = cv2.imread(picture1)
    template = cv2.imread(picture2)
    h = template.shape[0]
    w = template.shape[1]

    res = cv2.matchTemplate(img_rgb, template, cv2.TM_CCOEFF_NORMED)
    threshold = .8
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):  # Switch collumns and rows
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
    
    posX=(2*pt[0] + w)/2
    posY=(2*pt[1] + h)/2
    print("x= ",posX)
    print("y= ",posY)
    click_pos(posX,posY)
def do_job():
    click_pos(426,936)
    click_pos(975,1238)
    time.sleep(5)

# def check_job(picture1,picture2):
#     posX=0
#     posY=0
#     img_rgb = cv2.imread(picture1)
#     template = cv2.imread(picture2)
#     h = template.shape[0]
#     w = template.shape[1]

#     res = cv2.matchTemplate(img_rgb, template, cv2.TM_CCOEFF_NORMED)
#     threshold = .8
#     loc = np.where(res >= threshold)
#     for pt in zip(*loc[::-1]):  # Switch collumns and rows
#         cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
#     posX=(2*pt[0] + w)/2
#     posY=(2*pt[1] + h)/2
#     if (posX!=0):
#         print("x= ",posX)
#         print("y= ",posY)
#         click_pos(posX,posY)
#     else:
#         click_pos(989,1008)
def recheck_checkpoint(picture1,picture2):
    img_rgb = cv2.imread(picture1)
    template = cv2.imread(picture2)
    h = template.shape[0]
    w = template.shape[1]
    check=False
    res = cv2.matchTemplate(img_rgb, template, cv2.TM_CCOEFF_NORMED)
    threshold = .8
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):  # Switch collumns and rows
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
        if( pt[1]!=0 and pt[0]!=0 ):
            check=True
    if(check!=True):
        print("khong tim ra check")
    else:
        print("tim ra check")
        click_pos(991, 349)
        time.sleep(2)
        os.system("adb -s RWLJYXYD8TOZGYEM shell screencap -p '/sdcard/temp.png'")
        os.system("adb -s RWLJYXYD8TOZGYEM pull /sdcard/temp.png D:\\temppc2.png")
        pic1="D:\\temppc2.png"
        pic2="D:\\data\\FINISHbutton.png"
        find_image(pic1,pic2)
        time.sleep(10)
def baoloi():
    os.system("adb -s RWLJYXYD8TOZGYEM shell screencap -p '/sdcard/temp.png'")
    os.system("adb -s RWLJYXYD8TOZGYEM pull /sdcard/temp.png D:\\temppc2.png")
    pic1a="D:\\temppc2.png"
    pic2a="D:\\data\\baoloi.png"
    find_image(pic1a,pic2a)
    time.sleep(2)
    os.system("adb -s RWLJYXYD8TOZGYEM shell input swipe 520 1682 520 650  ")
    time.sleep(2)
    os.system("adb -s RWLJYXYD8TOZGYEM shell screencap -p '/sdcard/temp.png'")
    os.system("adb -s RWLJYXYD8TOZGYEM pull /sdcard/temp.png D:\\temppc2.png")
    pic2a="D:\\data\\guibaocao.png"
    find_image(pic1a,pic2a)
    time.sleep(2)
    os.system("adb -s RWLJYXYD8TOZGYEM shell screencap -p '/sdcard/temp.png'")
    os.system("adb -s RWLJYXYD8TOZGYEM pull /sdcard/temp.png D:\\temppc2.png")
    pic2a="D:\\data\\OKbutton.png"
    find_image(pic1a,pic2a)
    time.sleep(2)
    

def recheck_checkpoint02(picture1,picture2):
    img_rgb = cv2.imread(picture1)
    template = cv2.imread(picture2)
    h = template.shape[0]
    w = template.shape[1]
    check=False
    res = cv2.matchTemplate(img_rgb, template, cv2.TM_CCOEFF_NORMED)
    threshold = .8
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):  # Switch collumns and rows
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
        if( pt[1]!=0 and pt[0]!=0 ):
            check=True
    if(check!=True):
        print("khong tim ra check")
    else:
        print("tim ra check")
        baoloi()
def rework():
    os.system("adb -s RWLJYXYD8TOZGYEM shell input swipe 520 1682 520 840  ")
    os.system("adb -s RWLJYXYD8TOZGYEM shell screencap -p '/sdcard/temp.png'")
    os.system("adb -s RWLJYXYD8TOZGYEM pull /sdcard/temp.png D:\\temppc2.png")
    pic1="D:\\temppc2.png"
    pic2="D:\\data\\getjob.png"
    find_image(pic1,pic2)
    time.sleep(4)
    os.system("adb -s RWLJYXYD8TOZGYEM shell screencap -p '/sdcard/temp.png'")
    os.system("adb -s RWLJYXYD8TOZGYEM pull /sdcard/temp.png D:\\temppc2.png")
    pic2="D:\\data\\TIKTOKbutton.png"
    find_image(pic1,pic2)
    time.sleep(6)
    do_job()
    click_pos(293, 2338)
    time.sleep(1.5)
    click_pos(105, 1212)
    time.sleep(2)
    os.system("adb -s RWLJYXYD8TOZGYEM shell screencap -p '/sdcard/temp.png'")
    os.system("adb -s RWLJYXYD8TOZGYEM pull /sdcard/temp.png D:\\temppc2.png")
    pic2="D:\\data\\FINISHbutton.png"
    find_image(pic1,pic2)
    time.sleep(5)
    os.system("adb -s RWLJYXYD8TOZGYEM shell screencap -p '/sdcard/temp.png'")
    os.system("adb -s RWLJYXYD8TOZGYEM pull /sdcard/temp.png D:\\temppc2.png")
    pic2="D:\\data\\CHECKPOINT.png"
    recheck_checkpoint(pic1,pic2)
    time.sleep(2)

    os.system("adb -s RWLJYXYD8TOZGYEM shell screencap -p '/sdcard/temp.png'")
    os.system("adb -s RWLJYXYD8TOZGYEM pull /sdcard/temp.png D:\\temppc2.png")
    pic2="D:\\data\\OKbutton.png"
    find_image(pic1,pic2)
    time.sleep(2)
    os.system("adb -s RWLJYXYD8TOZGYEM shell screencap -p '/sdcard/temp.png'")
    os.system("adb -s RWLJYXYD8TOZGYEM pull /sdcard/temp.png D:\\temppc2.png")
    pic2="D:\\data\\baoloi.png"
    recheck_checkpoint02(pic1,pic2)
i=0
while(i<100):
    rework()
