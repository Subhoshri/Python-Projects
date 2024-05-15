from pytube import YouTube, Playlist
import os

def video(url):
    vid = YouTube(url)
    print("Downloading:",vid.title)
    video=vid.streams.filter(progressive=True,file_extension='mp4').order_by(
            'resolution').desc().first()
    v=''
    for i in vid.title:
        if i.isalpha() or i.isdigit():
            v+=i
    out_path = video.download(output_path=v)
    new_name = os.path.splitext(out_path)
    os.rename(out_path,new_name[0] + ".mp4")
    print("Download Complete!")
    
def playlist(url):
    pl = Playlist(url)
    print("Downloading:",pl.title)
    print('Number of videos in playlist: %s' % len(pl.video_urls))
    v=''
    for i in pl.title:
        if i.isalpha() or i.isdigit():
            v+=i

    for vid in pl.videos:
        video=vid.streams.filter(progressive=True,file_extension='mp4').order_by(
            'resolution').desc().first()
        out_path = video.download(output_path=v)
    new_name = os.path.splitext(out_path)
    os.rename(out_path,new_name[0] + ".mp4")
    print("Download Complete!")

def voice(url):
    aud = YouTube(url)
    print("Downloading:",aud.title)
    audio = aud.streams.filter(only_audio=True).first()
    v=''
    for i in aud.title:
        if i.isalpha() or i.isdigit():
            v+=i
    out_path = audio.download(output_path=v)
    new_name = os.path.splitext(out_path)
    os.rename(out_path,new_name[0] + ".mp3")
    print("Download Complete!")

def picture_only(url):
    vid = YouTube(url)
    print("Downloading:",vid.title)
    video = vid.streams.filter(only_video=True).first()
    v=''
    for i in vid.title:
        if i.isalpha() or i.isdigit():
            v+=i
    out_path = video.download(output_path=v)
    new_name = os.path.splitext(out_path)
    os.rename(out_path,new_name[0] + ".mp4")
    print("Download Complete!")

op = input("Do you want to download:\n1.Video \n2.Playlist \n3.Audio Only \n4.Picture Only\n")
if op=="playlist":
    url = input("Enter the URL for the whole playlist\n")
    playlist(url)
elif op=="video":
    url = input("Enter the URL of the video\n")
    video(url)
elif op == "voice":
    url = input("Enter the URL of the video\n")
    voice(url)
elif op == "picture":
    url = input("Enter the URL of the video\n")
    picture_only(url)    
else:
    print("The URL you have entered is invalid!")
