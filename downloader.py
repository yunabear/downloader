from instaloader.structures import Post
from pytube import YouTube
import instaloader
from moviepy.editor import *
import os

pilihan1 = input("Youtube/Instagram : ")
if pilihan1 == "youtube" or pilihan1 == "YOUTUBE":
    pilihan = input("Download [Mp3/Mp4]: ")
    if pilihan == "mp4" or pilihan == "MP4":
        reso = input("Resolusi [360/480/720/1080] :")
        if reso == "720":
            a = YouTube(input("Masukkan Link : "))
            yt = a.streams.get_by_itag(136).download()
        elif reso == "360":
            a = YouTube(input("Masukkan Link : "))
            yt = a.streams.get_by_itag(134).download()
        elif reso == "1080":
            a = YouTube(input("Masukkan Link : "))
            yt = a.streams.get_by_itag(137).download()
        elif reso == "480":
            a = YouTube(input("Masukkan Link : "))
            yt = a.streams.get_by_itag(135).download()
        print(yt)
        if os.path.exists(yt):
            os.remove(yt)
        else:
            print("The file does not exist")
    elif pilihan == "mp3" or pilihan == "MP3":
        a = YouTube(input("Masukkan Link: "))
        yt = a.streams.filter(only_audio=False, subtype='mp4', abr='128kbps').first().download()
        v = VideoFileClip(yt)
        ac = v.audio 
        ac.write_audiofile()
elif pilihan1 == "instagram" or pilihan1 == "Instagram" :
    ins = instaloader.Instaloader()
    pilihan = input("Masukkan Short Code Post : ") # https://www.instagram.com/p/CXVqQ-Hv1tI/ shortcode = CXVqQ-Hv1tI
    namafolder = input("Nama Folder : ")
    post = Post.from_shortcode(ins.context, pilihan)
    ins.download_post(post, namafolder)