import cv2
import os

def get_photo():
    cap = cv2.VideoCapture(0)
    # i = 10
    # while i != 0 :
    #     i = i-1
    #     ret, frame = cap.read()
    #     cv2.imwrite('yumei.jpg', frame)
    # cap.release()
    ret, frame = cap.read()
    cv2.imwrite('yumei.jpg', frame)
    cap.release()

if __name__=='__main__':
    get_photo()