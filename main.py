# -*- coding:utf-8 -*-
# author:木子川
# Data: 2022/7/9

import socket
import time
import struct
import os
import numpy as np
from tensorflow.keras.preprocessing import image
from keras.models import load_model
import matplotlib.pyplot as plt

def socket_service_image():
    host = "192.168.43.111"
    port = 6666
    tcpserver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcpserver.bind((host, port))
    tcpserver.listen(5)
    print("Wait for Connection.....................")

    sock, addr = tcpserver.accept()  # addr是一个元组(ip,port)
    #path = \
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


if __name__ == '__main__':
    print("hello1")
    cmd = 'sudo ./api'
    print("hello2")
    os.system(cmd)
    print("hello3")
    os.system(cmd)
    print("hello4")
    # model_dir = 'rps.h5'
    # model = load_model(model_dir)
    # model.summary()
    # #path =
    # path = socket_service_image()
    # print(path)
    # img = image.load_img(path, target_size=(150, 150))
    # x = image.img_to_array(img)
    # x = np.expand_dims(x, axis=0)
    # images = np.vstack([x])
    # classes = model.predict(images, batch_size=10)
    # #paper-rock-scissors
    # #print(classes)
    # if classes[0][0] == 1.0:
    #     print('You gave paper!')
    # elif classes[0][1] == 1.0:
    #     print('You gave rock!')
    # else:
    #     print('You gave scissors!')
