import json
import pdb

import re
import sys
import time
import os

from pytube import YouTube

def download_Video_Audio(path, vid_url, file_no):
    try:
        yt = YouTube(vid_url)
    except Exception as e:
        print("Error:", str(e), "- Skipping Video with url '"+vid_url+"'.")
        return

    try:  # Tries to find the video in 720p
        video = yt.get('video/mp4', '720p')
    except Exception:  # Sorts videos by resolution and picks the highest quality video if a 720p video doesn't exist
        video = yt.streams.filter(mime_type ="video/mp4").all()[0]

    print("downloading", yt.title+" Video and Audio...")
    try:
        video.download(path,filename = str(file_no))
        print("successfully downloaded", yt.title, "!")
    except OSError:
        print(yt.title, "already exists in this directory! Skipping video...")



with open("./activity_net.v1-3.min.json",'r') as load_f:
    load_dict = json.load(load_f)
    count = 0
    for key,value in load_dict["database"].iteritems():
        # pdb.set_trace()
        path = "./"+value["subset"]+"/"
        if not os.path.isdir(path):
            os.mkdir(path)

        vid_url = value["url"]
        file_no = count
        count = count + 1
        download_Video_Audio(path, vid_url, file_no)
        # pdb.set_trace()

