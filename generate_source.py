"""
script to generate source images from test videos
"""
import cv2
import os
import sys
from tqdm import tqdm

def main():
    video_path = "./data/fashion/test/"
    source_path = "./data/fashion/source/"
    for vid in tqdm(os.listdir(video_path)):
        video_file = os.path.join(video_path, vid)
        source_file = vid.split('.')[0]+'.png'
        source_file = os.path.join(source_path, source_file)
        video = cv2.VideoCapture(video_file)
        frame, ok = video.read()
        cv2.imwrite(source_file, frame)
        video.release()

if __name__ == "__main__":
    main()
