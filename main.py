# -*- coding:utf-8 -*-
# author:金昕澳
# Data: 2022/9/4
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
import matplotlib.pyplot as plt

def wait(target_time = ''):
    #target_time 是目标日期，str
    realnow = datetime.datetime.now()
    realnow_localtime = realnow.strftime('%H:%M:%S')
    realnow_time = Interval(realnow_localtime, realnow_localtime)
    time_interval = Interval(target_time, target_time)
    if realnow_time in time_interval:
        return True
    else:
        return False

def make_targettime(nowtime , bias):
    # nowtime是 datetime.datetime.now()的实例，bias是向后推移的时间，单位为s
    # bias 至多为60， 如果bias>60 应当反复执行make_targettime
    if nowtime.second + bias > 59:
        nowtime = nowtime.replace(second =  nowtime.second + bias - 60)
        if nowtime.minute == 59:# 表示现在是59分xx秒 + bias 秒后， 分钟进位，且小时也要进位
            nowtime = nowtime.replace(minute = 0)
            nowtime = nowtime.replace(hour = nowtime.hour + 1)
        else:
            nowtime.minute = nowtime.minute + 1
    else:
        nowtime = nowtime.replace(second = nowtime.second + 1)

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
    print("Accept connection from {0}".format(addr))  # 查看发送端的ip和端口
    print("-" * 5 + "开始接收" + "-" * 5)

    while True:
        fileinfo_size = struct.calcsize('128sq')
        buf = sock.recv(fileinfo_size)  # 接收图片名
        if buf:
            filename, filesize = struct.unpack('128sq', buf)
            fn = filename.decode().strip('\x00')
            recvd_size = 0

            now_time = time.strftime("%Y%m%d-%H%M%S")
            print(f"保存为：./{ now_time} {fn}")
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
        print(path)
        print(type(path))
        break
    return path


#程序开始运行啦
#确定石头剪刀布开始时间为按下2min内
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
now_localtime = nextmin.strftime('%H:%M:%S')

#确定tcp通信的ip socket
host = "192.168.43.111"
port = 6666
tcpserver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpserver.bind((host, port))
# 导入训练好的模型
model_dir = 'rps.h5'
model = load_model(model_dir)
model.summary()
#以上过程应当在1min内完成。这样，程序会在按下运行键后最接近

flag = True

while flag:
        flag = wait(next_localtime)

#控制灵巧手运动过程
cmd = 'sudo ./api'
os.system(cmd)
#读取图片并返回图片路径
path = socket_service_image()
# print("path of the picture is")
# print(path)
#对读到的图片进行处理
img = image.load_img(path, target_size=(150, 150))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
images = np.vstack([x])
classes = model.predict(images, batch_size=10)
#paper-rock-scissors
#print(classes)
if classes[0][0] == 1.0:
    print('You gave paper!')
elif classes[0][1] == 1.0:
    print('You gave rock!')
else:
    print('You gave scissors!')