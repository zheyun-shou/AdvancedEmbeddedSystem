from ast import If
from lib2to3.pgen2.pgen import DFAState
import cv2
import os
import socket
import sys
import struct
import datetime
import copy
from interval import Interval

def sock_client_image(num):
    while True:
        try:
            host = "192.168.43.111"
            port = 6666
            tcpclient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            tcpclient.connect((host, port))
        except socket.error as msg:
            print(msg)
            print(sys.exit(1))

        #filepath = r"/home/peterking/Downloads/filetrans/image.png"  # 输入当前目录下的图片名
        filepath = "image" + str(num) + ".jpg"
        fhead = struct.pack(b'128sq', bytes(os.path.basename(filepath), encoding='utf-8'),
                            os.stat(filepath).st_size)  # 将图片以128sq的格式打包
        tcpclient.send(fhead)

        fp = open(filepath, 'rb')  # 打开要传输的图片
        while True:
            data = fp.read(1024)  # 读入图片数据
            if not data:
                print('{0} send over...'.format(filepath))
                break
            tcpclient.send(data)  # 以二进制格式发送图片数据
        tcpclient.close()
        break    # 注释则循环发送

def get_photo1(num):
    a=os.system("fswebcam --no-banner -r 150x150 image" + str(num) + ".jpg")
    return a

def get_photo2(num):
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cv2.imwrite("image" + str(num) + ".jpg", frame)
    cap.release()

def wait(target_time:str):
    realnow = datetime.datetime.now()
    realow_localtime = realnow.strftime('%H:%M:%S')
    realnow_time = Interval(realow_localtime, realow_localtime)
    time_interval = Interval(target_time, target_time)
    if realnow_time in time_interval:
        return False
    else:
        return True

def make_targettime(now:datetime.datetime, bias:int) -> datetime.datetime :
    nowtime = copy.deepcopy(now)
    if nowtime.second + bias > 59:
        print("1")
        nowtime = nowtime.replace(second= nowtime.second + bias - 60)
        if nowtime.minute == 59:
            print("2")
            nowtime.replace(minute = 0)
            nowtime.replace(hour = nowtime.hour + 1)
        else:
            print("3")
            nowtime.replace(minute = nowtime.minute + 1)
    else:
        print("4")
        nowtime.replace(second = nowtime.second + bias)
    
    print(nowtime.second)
    print(nowtime.strftime('%H:%M:%S'))

    return nowtime

now_ori = datetime.datetime.now()
nextmin = copy.deepcopy(now_ori)

if now_ori.minute + 2 > 59:
    nextmin = nextmin.replace(minute = now_ori.minute + 2 - 60)
    nextmin = nextmin.replace(hour = nextmin.hour + 1)
else:
    nextmin = nextmin.replace(minute = now_ori.minute + 2)
nextmin = nextmin.replace(second = 0)
nextmin = nextmin.replace(microsecond = 0)
next_localtime = nextmin.strftime('%H:%M:%S')

start_time = copy.deepcopy(nextmin)
strstart_time = start_time.strftime('%H:%M:%S')

print(strstart_time)

i = 0

if True:
    i = i + 1
    targettime = make_targettime(start_time, 8)
    target_localtime = targettime.strftime('%H:%M:%S')
    print(target_localtime)
    flag = True
    while flag:
        flag = wait(target_localtime)
    a = get_photo2(i)
    #sock_client_image(i)
    start_time = make_targettime(start_time, 10)
    strstart_time = start_time.strftime('%H:%M:%S')
    print(i)
    print(flag)


    


# if __name__=='__main__':
#     # function2 run faster seemingly
#     a = get_photo1(1)
#     sock_client_image(1)
#     # b = get_photo2(2)
#     # sock_client_image(2)
#     # c = get_photo1(3)
#     # sock_client_image(3)
#     # d = get_photo2(4)
#     # sock_client_image(4)