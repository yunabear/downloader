from instaloader.structures import Post
from pytube import YouTube
import instaloader
import os
pilihan = { 
    1 : "1. Video Youtube",
    2 : "2. Video Youtube To Mp3",
    3 : "3. Instagram Post"
}

print("Program Downloader")
print(pilihan[1])
print(pilihan[2])
print(pilihan[3])
print()
data = int(input("Pilih Sesuai Angka : "))
os.system('cls')
if data == 1:
    reso = input("Resolusi [360/480/720/1080] :")
    if reso == "360":
        a = YouTube(input("Masukkan Link : "))
        yt = a.streams.get_by_itag(134).download()
    elif reso == "480":
        a = YouTube(input("Masukkan Link : "))
        yt = a.streams.get_by_itag(135).download()
    elif reso == "720":
        a = YouTube(input("Masukkan Link : "))
        yt = a.streams.get_by_itag(136).download()
    elif reso == "1080":
        a = YouTube(input("Masukkan Link : "))
        yt = a.streams.get_by_itag(137).download()
    else:
        print("Resolusi Salah! Coba Input Kembali")
    print(yt)
    if os.path.exists(yt):
        os.remove(yt)
    else:
        print("The file does not exist")
elif data == 2:
    a = YouTube(input("Masukkan Link: "))
    b = input("Masukan Nama File : ")
    yt = a.streams.filter(only_audio=True).first()
    h = yt.download(filename= b+'.mp3')
elif data == 3:
    ins = instaloader.Instaloader()
    code = input("Masukkan Link : ")
    namafolder = input("Nama Folder : ")
    os.system('cls')
    if code[-1] != "/":
        post = Post.from_shortcode(ins.context, code[28:])
        ins.download_post(post, namafolder)
    elif code[-1] == "/":
        post = Post.from_shortcode(ins.context, code[28:-1])
        ins.download_post(post, namafolder)
