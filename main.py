# -*- coding:utf-8 -*-
# author:金昕澳
# Data: 2022/9/4

# paper 1 rock 2 scissors 3


import random
from interval import Interval
import socket
import time
import struct
import os
import copy
import datetime
import numpy as np
from tensorflow.keras.preprocessing import image
from keras.models import load_model
import shlex, subprocess
import matplotlib.pyplot as plt



from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True


def wait(target_time:str):
    #target_time 是目标日期，str
    realnow = datetime.datetime.now()
    realnow_localtime = realnow.strftime('%H:%M:%S')
    realnow_time = Interval(realnow_localtime, realnow_localtime)
    time_interval = Interval(target_time, target_time)
    if realnow_time in time_interval:
        return False
    else:
        return True

def make_targettime(nowtime:datetime.datetime , bias:int) -> datetime.datetime :
    # nowtime是 datetime.datetime.now()的实例，bias是向后推移的时间，单位为s
    # bias 至多为60， 如果bias>60 应当反复执行make_targettime
    if nowtime.second + bias > 59:
        nowtime = nowtime.replace(second=nowtime.second + bias - 60)
        if nowtime.minute == 59:# 表示现在是59分xx秒 + bias 秒后， 分钟进位，且小时也要进位
            nowtime = nowtime.replace(minute=0)
            nowtime = nowtime.replace(hour=nowtime.hour + 1)
        else:
            nowtime = nowtime.replace(minute=nowtime.minute + 1)
    else:
        nowtime = nowtime.replace(second = nowtime.second + bias)

    return nowtime



def socket_service_image():
    #以下在初始化中已经完成
    # host = "192.168.43.111"
    # port = 6666
    # tcpserver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # tcpserver.bind((host, port))
    tcpserver.listen(5)
    print("Wait for Connection.....................")

    sock, addr = tcpserver.accept()  # addr是一个元组(ip,port)
    path = deal_image(sock, addr)
    # 这里表示可以多首
    # sock, addr = tcpserver.accept()
    # deal_image(sock, addr)
    # sock, addr = tcpserver.accept()
    # deal_image(sock, addr)
    # sock, addr = tcpserver.accept()
    # deal_image(sock, addr)
    return path


def deal_image(sock: object, addr: object) -> object:
    #print("Accept connection from {0}".format(addr))  # 查看发送端的ip和端口
    print("-" * 5 + "开始接收" + "-" * 5)

    while True:
        fileinfo_size = struct.calcsize('128sq')
        buf = sock.recv(fileinfo_size)  # 接收图片名
        if buf:
            filename, filesize = struct.unpack('128sq', buf)
            fn = filename.decode().strip('\x00')
            recvd_size = 0

            now_time = time.strftime("%Y%m%d-%H%M%S")
            # print(f"保存为：./{ now_time} {fn}")
            fp = open(r"./" + now_time + " " + fn, 'wb')

            while not recvd_size == filesize:
                if filesize - recvd_size > 1024:
                    data = sock.recv(1024)
                    recvd_size += len(data)
                else:
                    data = sock.recv(1024)
                    recvd_size = filesize
                fp.write(data)  # 写入图片数据
            fp.close()
        print("-"*5 + "接收完成" + "-"*5)
        sock.close()
        path = "./" + now_time + " " + fn
        #print(path)
        #print(type(path))
        break
    return path

def judge(people:int, robot:int) -> int:
    # 返回 1 表示people wins, 返回 -1 表示robot wins，返回 0 表示平局
    # paper 1 rock 2 scissors 3

    if people == 1:
        if robot == 1:
            command_lin = 'python3 ptop.py'
            arg = shlex.split(command_lin)
            q = subprocess.Popen(arg)
            return 0
        elif robot == 2:
            command_lin = 'python3 ptor.py'
            arg = shlex.split(command_lin)
            q = subprocess.Popen(arg)
            return 1
        else:
            command_lin = 'python3 ptos.py'
            arg = shlex.split(command_lin)
            q = subprocess.Popen(arg)
            return -1
    elif people == 2:
        if robot == 1:
            command_lin = 'python3 rtop.py'
            arg = shlex.split(command_lin)
            q = subprocess.Popen(arg)
            return -1
        elif robot == 2:
            command_lin = 'python3 rtor.py'
            arg = shlex.split(command_lin)
            q = subprocess.Popen(arg)
            return 0
        else:
            command_lin = 'python3 rtos.py'
            arg = shlex.split(command_lin)
            q = subprocess.Popen(arg)
            return 1
    else:
        if robot == 1:
            command_lin = 'python3 stop.py'
            arg = shlex.split(command_lin)
            q = subprocess.Popen(arg)
            return 1
        elif robot == 2:
            command_lin = 'python3 stor.py'
            arg = shlex.split(command_lin)
            q = subprocess.Popen(arg)
            return -1
        else:
            command_lin = 'python3 stos.py'
            arg = shlex.split(command_lin)
            q = subprocess.Popen(arg)
            return 0


def classification(path) -> int :
    # 对读到的图片进行处理
    img = image.load_img(path, target_size=(150, 150))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    images = np.vstack([x])
    classes = model.predict(images, batch_size=10)
    if classes[0][0] == 1.0:
        print('You gave paper!')
        return 1
    elif classes[0][1] == 1.0:
        print('You gave rock!')
        return 2
    else:
        print('You gave scissors!')
        return 3

#程序开始运行啦
#确定石头剪刀布开始时间为按下2min内

#确定主程序开始运行时间
now_ori = datetime.datetime.now()
nextmin = copy.deepcopy(now_ori)
# 防止分钟数越界
if now_ori.minute + 2 > 59:
    nextmin = nextmin.replace(minute=now_ori.minute + 2 -60)
    nextmin = nextmin.replace(hour = nextmin.hour + 1)
else:
    nextmin = nextmin.replace(minute=now_ori.minute+2)
nextmin = nextmin.replace(second=0)
nextmin = nextmin.replace(microsecond=0)
next_localtime = nextmin.strftime('%H:%M:%S')
#确定主程序开始运行时间

audio_starttime = copy.deepcopy(now_ori)
if now_ori.minute + 1 > 59:
    audio_starttime = audio_starttime.replace(minute=now_ori.minute + 1 - 60)
    audio_starttime = audio_starttime.replace(minute=now_ori.hour + 1)
else:
    audio_starttime = audio_starttime.replace(minute=now_ori.minute + 1)
audio_starttime = audio_starttime.replace(second=56)
audio_starttime = audio_starttime.replace(microsecond=0)
audio_localstarttime = audio_starttime.strftime('%H:%M:%S')

#确定tcp通信的ip socket
host = "192.168.43.111"
port = 6666
tcpserver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpserver.bind((host, port))
#确定tcp通信的ip socket
# 导入训练好的模型
model_dir = 'rps.h5'
model = load_model(model_dir)
model.summary()
# 导入训练好的模型
# 初始化比赛结果
wins = 0
loses = 0
even = 0
# 初始化比赛结果

#以上过程应当在1min内完成。这样，程序会在按下运行键后最接近



start_time = copy.deepcopy(nextmin)
strstart_time = start_time.strftime('%H:%M:%S')
print(strstart_time)
i = 0

flag = True
while flag:
    flag = wait(audio_localstarttime)

command_line = 'python3 gamestart.py'
args = shlex.split(command_line)
print(args)
p = subprocess.Popen(args)

while (abs(wins - loses) < 2) and (i<=20) :
    i = i + 1
    flag = True
    while flag:
        flag = wait(strstart_time)

    rand_robot = random.randint(1,3)

    command_line2 = 'python3 psr.py'
    ar = shlex.split(command_line2)
    t = subprocess.Popen(ar)

    #控制灵巧手运动过程
    # paper 1 rock 2 scissors 3
    if rand_robot == 1:
        command_line = 'sudo ./paper'
    elif rand_robot == 2:
        command_line = 'sudo ./rock'
    else:
        command_line = 'sudo ./scissors'
    args = shlex.split(command_line)
    print(args)
    p = subprocess.Popen(args)
    #Popen.kill() #杀死进程，先不杀
    #控制灵巧手运动过程

    if rand_robot == 1:
        print("Rotot gave paper.")
    elif rand_robot == 2:
        print("Rotot gave rock.")
    else:
        print("Rotot gave scissors.")

    #读取图片并返回图片路径
    target_time = make_targettime(start_time, 7)
    target_localtime = target_time.strftime('%H:%M:%S')
    flag = True
    while flag:
        flag = wait(target_localtime)
    path = socket_service_image()
    #读取图片并返回图片路径

    #判断胜负
    recognize_result = classification(path)
    term_result = judge(recognize_result,rand_robot)
    if term_result == 1:
        wins = wins + 1
        print("In this term, you win!")
    elif term_result == 0:
        even = even + 1
        print("In this term, you got even.")
    else:
        loses = loses + 1
        print("Oh, in this term, you lose.")
    start_time = make_targettime(start_time, 10)
    strstart_time = start_time.strftime('%H:%M:%S')

if abs(wins -loses) >= 2:
    if wins > loses:
        command_line = 'python3 win.py'
        args = shlex.split(command_line)
        print(args)
        p = subprocess.Popen(args)
        print("Congratulations, you win!")
    else:
        command_line = 'python3 lose.py'
        args = shlex.split(command_line)
        print(args)
        p = subprocess.Popen(args)
        print("It's a pity that you lost.")
else:
    command_line = 'python3 timetoolong.py'
    args = shlex.split(command_line)
    print(args)
    p = subprocess.Popen(args)
    print("The game has lasted for too long.EXIT!")


print("The final result is you won {} time(s), got even {} times and lost {} times".format(wins, even, loses))