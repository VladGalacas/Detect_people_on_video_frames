# import yadisk
# from config import token
#
# y = yadisk.YaDisk(token=token)
#
# if y.is_file('camera_office.mp4'):
#     y.download('camera_office.mp4', 'camera_office.mp4')


import cv2
import sys
import time

xmin, ymin = 115, 210
xmax, ymax = 350, 445
dim = 116

video = cv2.VideoCapture('camera_office.mp4')
if not video.isOpened():
    print("Could not open video")
    sys.exit()

total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
start = time.time()
count_frames = 0
while True:
    ok, frame = video.read()
    if not ok:
        print("Frame is bad")
        break
    count_frames += 1
    if count_frames % 15 == 0:
        crop_frame = frame[ymin:ymin + (ymax - ymin), xmin:xmin + (xmax - xmin)]
        crop_frame_with_dim_116 = cv2.resize(crop_frame, (dim, dim))
        cv2.imwrite(f'photos/{int(count_frames / 15)}.jpeg', crop_frame_with_dim_116)
    if count_frames % 5000 == 0:
        print(f'Обработано {count_frames} кадров из {total_frames} за {"%.2f" % float((time.time() - start) / 60)} минут')