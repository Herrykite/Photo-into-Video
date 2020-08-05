# encoding=UTF-8
import os
import cv2
import time


def pic_video(path, size):
    file_list = os.listdir(path)
    fps = 60
    file_path = 'C:/Users/admin/Desktop/' + str(int(time.time())) + '.avi'
    character_code = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
    video = cv2.VideoWriter(file_path, character_code, fps, size)
    for item in file_list:
        if item.endswith('.jpg'):
            item = path + '/' + item
            img = cv2.imread(item)
            video.write(img)
    video.release()


if __name__ == "__main__":
    pic_video('D:/output photo', (960, 1280))             # 一定要注意输入路径不能有汉字
