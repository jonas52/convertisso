#pip install yt-dlp
#pip install AudioSegment    
#pip install pydub 
import os
import subprocess
import shutil
import glob
import ffmpeg
import yt_dlp
from PyQt5.QtWidgets import QApplication, QFileDialog, QMessageBox
import sys
from pydub import AudioSegment
from urllib import request
#https://www.youtube.com/watch?v=Mx_OexsUI2M&ab_channel=RihannaVEVO
#subprocess.run(["ping", "arg1", "arg2", ...], capture_output=True)
subprocess.run(["echo", "-n", "-e", "\033]0;Convertisso\007"])

def convertisso(): 
    print("\n")
    print("\033[33m   ██████╗ ██████╗ ███╗   ██╗██╗   ██╗███████╗██████╗ ████████╗██╗███████╗███████╗ ██████╗  \033[0m")
    print("\033[33m  ██╔════╝██╔═══██╗████╗  ██║██║   ██║██╔════╝██╔══██╗╚══██╔══╝██║██╔════╝██╔════╝██╔═══██╗ \033[0m")
    print("\033[33m  ██║     ██║   ██║██╔██╗ ██║██║   ██║█████╗  ██████╔╝   ██║   ██║███████╗███████╗██║   ██║ \033[0m")
    print("\033[33m  ██║     ██║   ██║██║╚██╗██║╚██╗ ██╔╝██╔══╝  ██╔══██╗   ██║   ██║╚════██║╚════██║██║   ██║ \033[0m")
    print("\033[33m  ╚██████╗╚██████╔╝██║ ╚████║ ╚████╔╝ ███████╗██║  ██║   ██║   ██║███████║███████║╚██████╔╝ \033[0m")
    print("\033[33m   ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝╚══════╝╚══════╝ ╚═════╝  \033[0m")
    print("\033[33m                                                       +-+ +-+ +-+ +-+ +-+ +-+ +-+ +-+ +-+  \033[0m")
    print("\033[33m                                                       |b| |y| |J| |o| |n| |a| |s| |5| |2|  \033[0m")
    print("\033[33m                                                       +-+ +-+ +-+ +-+ +-+ +-+ +-+ +-+ +-+  \033[0m")
    print("\n")
        
convertisso()

# i=0

# def convertisso_subtitle():
    
#     while True:
#         if i==1:
#             print("hello world")
     
app = QApplication(sys.argv)
def convertisso_download_video():
    response = request.urlopen('https://google.com', timeout=4)
    if response == 0:
            while True:
                    userchoice = int(input("Choose how your video will be downloaded.   : "))
                    userchoicelink = input("Copy the link(URL) of the video and paste it here.  ->  ")
                    name=input("enter the name that the file will have once uploaded. ->  ")
                    destination = input("Enter the destination folder where you want to download the video. ->  ")
                    if userchoice == 1:
                        ydl_opts = {
                            'format': 'bv*+ba',
                            'addmetadata': True,
                            'outtmpl': "name"
                        }
                        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                            ydl.download([userchoicelink])
                        for extension in ["*.mp4", "*.mkv", "*.webm", "*.flv"]:
                            for filename in glob.glob(extension):
                                shutil.move(filename, destination)
                        break
                    elif userchoice == 2:
                        ydl_opts = {
                            'format': 'bv*+ba',
                            'addmetadata': True,
                            'outtmpl': destination + '/%(title)s.%(ext)s',
                            'allsubtitles': True,
                            'writeautomaticsub': True
                        }
                        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                            ydl.download([userchoicelink])                        
                        for extension in ["*.mp4", "*.mkv", "*.webm", "*.flv", "*.srt", "*.ass", "*.vtt", "*.lrc"]:
                            for filename in glob.glob(extension):
                                shutil.move(filename, destination)
                        break
                    elif userchoice == 3:
                        ydl_opts = {
                            'x': True,
                            'audio-format': 'best',
                            'audio-quality': 'best',
                            'addmetadata': True,
                            'outtmpl': name
                        }                       
                        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                            ydl.download([userchoicelink])
                        for extension in ["*.mp3", "*.aac", "*.flac", "*.m4a", "*.ogg", "*.wav", "*.opus", "*.vorbis"]:
                            for filename in glob.glob(extension):
                                shutil.move(filename, destination)
                        break
                    elif userchoice == 4:
                        ydl_opts = {
                            'skip_download': True,
                            'addmetadata': True,
                            'outtmpl': destination + '/%(title)s.%(ext)s',
                            'allsubtitles': True,
                            'writeautomaticsub': True
                        }          
                        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                            info_dict = ydl.extract_info(userchoicelink, download=False)
                            filename = ydl.prepare_filename(info_dict)
                            ydl.process_info(info_dict)
                        for extension in ["*.srt", "*.ass", "*.vtt", "*.lrc"]:
                            for filename in glob.glob(extension):
                                shutil.move(filename, destination)
                        break
                    else:
                        print("Please enter a number between 1 and 4")
                        break
    else:
        print("Your device is not connected to the Internet, connect your device to the Internet and try again.")

# def convertisso_subtitle():

#     while True:
#         if i==1:
#             print("hello world")


def convertissso_video():
    video=1
    while True:
        if video == 1:  # mkv en avi
            file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                mkv_files = glob.glob(f"{file}/**/*.mkv", recursive=True)
                if mkv_files:
                    print("Conversion in progress ...")
                    for t in mkv_files:
                        out_filename = os.path.splitext(t)[0] + '.ogg'
                        stream = ffmpeg.input(t)
                        stream = ffmpeg.output(stream, out_filename, acodec='libvorbis', map_metadata=0)
                        ffmpeg.run(stream, quiet=True)
                        subprocess.run(f"ffmpeg -i {t} -codec copy {t[:-4]}.avi", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
                    encov = "avi"
                    break
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    continue
            else:
                QMessageBox.critical(None, "Error", "No files selected")
                continue
        elif video == 2:  # mkv en mov
            file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                mkv_files = glob.glob(f"{file}/**/*.mkv", recursive=True)
                if mkv_files:
                    print("Conversion in progress ...")
                    for t in mkv_files:
                        out_filename = os.path.splitext(t)[0] + '.ogg'
                        stream = ffmpeg.input(t)
                        stream = ffmpeg.output(stream, out_filename, acodec='libvorbis', map_metadata=0)
                        ffmpeg.run(stream, quiet=True)
                        subprocess.run(f"ffmpeg -i {t} -codec copy {t[:-4]}.mov", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
                    encov = "mov"
                    break
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    continue
            else:
                QMessageBox.critical(None, "Error", "No files selected")
                continue
        if video == 3:  # mkv en mp4
            file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                mkv_files = glob.glob(f"{file}/**/*.mkv", recursive=True)
                if mkv_files:
                    print("Conversion in progress ...")
                    for t in mkv_files:
                        out_filename = os.path.splitext(t)[0] + '.ogg'
                        stream = ffmpeg.input(t)
                        stream = ffmpeg.output(stream, out_filename, acodec='libvorbis', map_metadata=0)
                        ffmpeg.run(stream, quiet=True)
                        subprocess.run(f"ffmpeg -i {t} -codec copy {t[:-4]}.mp4", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
                    encov = "mp4"
                    break
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    continue
            else:
                QMessageBox.critical(None, "Error", "No files selected")
                continue
        elif video == 4:  # mkv en webm
            file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                mkv_files = glob.glob(f"{file}/**/*.mkv", recursive=True)
                if mkv_files:
                    print("Conversion in progress ...")
                    for t in mkv_files:
                        out_filename = os.path.splitext(t)[0] + '.ogg'
                        stream = ffmpeg.input(t)
                        stream = ffmpeg.output(stream, out_filename, acodec='libvorbis', map_metadata=0)
                        ffmpeg.run(stream, quiet=True)
                        subprocess.run(f"ffmpeg -i {t} -c:v libvpx -c:a libvorbis {t[:-4]}.webm", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
                    encov = "webm"
                    break
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    continue
            else:
                QMessageBox.critical(None, "Error", "No files selected")
                continue
        elif video == 5:  # mkv en flv
            file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                mkv_files = glob.glob(f"{file}/**/*.mkv", recursive=True)
                if mkv_files:
                    print("Conversion in progress ...")
                    for t in mkv_files:
                        out_filename = os.path.splitext(t)[0] + '.ogg'
                        stream = ffmpeg.input(t)
                        stream = ffmpeg.output(stream, out_filename, acodec='libvorbis', map_metadata=0)
                        ffmpeg.run(stream, quiet=True)
                        subprocess.run(f"ffmpeg -i {t} -c:v flv -c:a mp3 {t[:-4]}.flv", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
                    encov = "flv"
                    break
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    continue
            else:
                QMessageBox.critical(None, "Error", "No files selected")
                continue
        elif video == 6:  # mkv en hevc
            file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                mkv_files = glob.glob(f"{file}/**/*.mkv", recursive=True)
                if mkv_files:
                    print("Conversion in progress ...")
                    for t in mkv_files:
                        out_filename = os.path.splitext(t)[0] + '.ogg'
                        stream = ffmpeg.input(t)
                        stream = ffmpeg.output(stream, out_filename, acodec='libvorbis', map_metadata=0)
                        ffmpeg.run(stream, quiet=True)
                        subprocess.run(f"ffmpeg -i {t} -c:v libx265 -c:a aac {t[:-4]}.hevc", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
                    encov = "hevc"
                    break
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    continue
            else:
                QMessageBox.critical(None, "Error", "No files selected")
                continue        
        elif video == 7:    #mp4 en mkv 
            file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                mp4_files = glob.glob(f"{file}/**/*.mp4", recursive=True)
                if mp4_files:
                    print("Conversion in progress ...")
                    for t in mp4_files:
                        out_filename = os.path.splitext(t)[0] + '.ogg'
                        stream = ffmpeg.input(t)
                        stream = ffmpeg.output(stream, out_filename, acodec='libvorbis', map_metadata=0)
                        ffmpeg.run(stream, quiet=True)
                        subprocess.run(f"ffmpeg -i {t} -codec copy {t[:-4]}.mkv", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
                    encov = "mkv"
                    break
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    continue
            else:
                QMessageBox.critical(None, "Error", "No files selected")
                continue
        elif video == 8:    #mp4 en mov 
            file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                mp4_files = glob.glob(f"{file}/**/*.mp4", recursive=True)
                if mp4_files:
                    print("Conversion in progress ...")
                    for t in mp4_files:
                        out_filename = os.path.splitext(t)[0] + '.ogg'
                        stream = ffmpeg.input(t)
                        stream = ffmpeg.output(stream, out_filename, acodec='libvorbis', map_metadata=0)
                        ffmpeg.run(stream, quiet=True)
                        subprocess.run(f"ffmpeg -i {t} -codec copy {t[:-4]}.mov", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
                    encov = "mov"
                    break
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    continue
            else:
                QMessageBox.critical(None, "Error", "No files selected")
                continue
        elif video == 9:    #mp4 en avi 
            file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                mp4_files = glob.glob(f"{file}/**/*.mp4", recursive=True)
                if mp4_files:
                    print("Conversion in progress ...")
                    for t in mp4_files:
                        out_filename = os.path.splitext(t)[0] + '.ogg'
                        stream = ffmpeg.input(t)
                        stream = ffmpeg.output(stream, out_filename, acodec='libvorbis', map_metadata=0)
                        ffmpeg.run(stream, quiet=True)
                        subprocess.run(f"ffmpeg -i {t} -codec copy {t[:-4]}.avi", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
                    encov = "avi"
                    break
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    continue
            else:
                QMessageBox.critical(None, "Error", "No files selected")
                continue
        elif video == 10:    #mp4 en webm 
            file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                mp4_files = glob.glob(f"{file}/**/*.mp4", recursive=True)
                if mp4_files:
                    print("Conversion in progress ...")
                    for t in mp4_files:
                        out_filename = os.path.splitext(t)[0] + '.ogg'
                        stream = ffmpeg.input(t)
                        stream = ffmpeg.output(stream, out_filename, acodec='libvorbis', map_metadata=0)
                        ffmpeg.run(stream, quiet=True)
                        subprocess.run(f"ffmpeg -i {t} zz-c:v libvpx -c:a libvorbis {t[:-4]}.webm", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
                    encov = "webm"
                    break
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    continue
            else:
                QMessageBox.critical(None, "Error", "No files selected")
                continue        
        elif video == 11:    #mp4 en flv 
            file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                mp4_files = glob.glob(f"{file}/**/*.mp4", recursive=True)
                if mp4_files:
                    print("Conversion in progress ...")
                    for t in mp4_files:
                        out_filename = os.path.splitext(t)[0] + '.ogg'
                        stream = ffmpeg.input(t)
                        stream = ffmpeg.output(stream, out_filename, acodec='libvorbis', map_metadata=0)
                        ffmpeg.run(stream, quiet=True)
                        subprocess.run(f"ffmpeg -i {t} -c:v libvpx -c:a libvorbis {t[:-4]}.flv", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
                    encov = "flv"
                    break
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    continue
            else:
                QMessageBox.critical(None, "Error", "No files selected")
                continue         
        elif video == 12:    #mp4 en hevc 
            file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                mp4_files = glob.glob(f"{file}/**/*.mp4", recursive=True)
                if mp4_files:
                    print("Conversion in progress ...")
                    for t in mp4_files:
                        out_filename = os.path.splitext(t)[0] + '.ogg'
                        stream = ffmpeg.input(t)
                        stream = ffmpeg.output(stream, out_filename, acodec='libvorbis', map_metadata=0)
                        ffmpeg.run(stream, quiet=True)
                        subprocess.run(f"ffmpeg -i {t} -c:v libx265 -c:a aac {t[:-4]}.hevc", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
                    encov = "hevc"
                    break
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    continue
            else:
                QMessageBox.critical(None, "Error", "No files selected")
                continue         
        elif video == 13:    #mov en mkv 
            file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                mov_files = glob.glob(f"{file}/**/*.mov", recursive=True)
                if mov_files:
                    print("Conversion in progress ...")
                    for t in mov_files:
                        out_filename = os.path.splitext(t)[0] + '.ogg'
                        stream = ffmpeg.input(t)
                        stream = ffmpeg.output(stream, out_filename, acodec='libvorbis', map_metadata=0)
                        ffmpeg.run(stream, quiet=True)
                        subprocess.run(f"ffmpeg -i {t} -codec copy {t[:-4]}.mkv", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
                    encov = "mkv"
                    break
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    continue
            else:
                QMessageBox.critical(None, "Error", "No files selected")
                continue
        elif video == 14:    #mov en mp4 
            file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                mov_files = glob.glob(f"{file}/**/*.mov", recursive=True)
                if mov_files:
                    print("Conversion in progress ...")
                    for t in mov_files:
                        out_filename = os.path.splitext(t)[0] + '.ogg'
                        stream = ffmpeg.input(t)
                        stream = ffmpeg.output(stream, out_filename, acodec='libvorbis', map_metadata=0)
                        ffmpeg.run(stream, quiet=True)
                        subprocess.run(f"ffmpeg -i {t} -codec copy {t[:-4]}.mp4", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
                    encov = "mp4"
                    break
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    continue
            else:
                QMessageBox.critical(None, "Error", "No files selected")
                continue
        elif video == 15:    #mov en avi 
            file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                mov_files = glob.glob(f"{file}/**/*.mov", recursive=True)
                if mov_files:
                    print("Conversion in progress ...")
                    for t in mov_files:
                        out_filename = os.path.splitext(t)[0] + '.ogg'
                        stream = ffmpeg.input(t)
                        stream = ffmpeg.output(stream, out_filename, acodec='libvorbis', map_metadata=0)
                        ffmpeg.run(stream, quiet=True)
                        subprocess.run(f"ffmpeg -i {t} -codec copy {t[:-4]}.avi", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
                    encov = "avi"
                    break
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    continue
            else:
                QMessageBox.critical(None, "Error", "No files selected")
                continue
        elif video == 16:    #mov en webm 
            file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                mov_files = glob.glob(f"{file}/**/*.mov", recursive=True)
                if mov_files:
                    print("Conversion in progress ...")
                    for t in mov_files:
                        out_filename = os.path.splitext(t)[0] + '.ogg'
                        stream = ffmpeg.input(t)
                        stream = ffmpeg.output(stream, out_filename, acodec='libvorbis', map_metadata=0)
                        ffmpeg.run(stream, quiet=True)
                        subprocess.run(f"ffmpeg -i {t} -c:v libvpx -c:a libvorbis {t[:-4]}.webm", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
                    encov = "webm"
                    break
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    continue
            else:
                QMessageBox.critical(None, "Error", "No files selected")
                continue        
        elif video == 17:    #mov en flv 
            file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                mov_files = glob.glob(f"{file}/**/*.mov", recursive=True)
                if mov_files:
                    print("Conversion in progress ...")
                    for t in mov_files:
                        out_filename = os.path.splitext(t)[0] + '.ogg'
                        stream = ffmpeg.input(t)
                        stream = ffmpeg.output(stream, out_filename, acodec='libvorbis', map_metadata=0)
                        ffmpeg.run(stream, quiet=True)
                        subprocess.run(f"ffmpeg -i {t} -c:v flv -c:a mp3 {t[:-4]}.flv", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
                    encov = "flv"
                    break
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    continue
            else:
                QMessageBox.critical(None, "Error", "No files selected")
                continue         
        elif video == 18:    #mov en hevc 
            file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                mov_files = glob.glob(f"{file}/**/*.mov", recursive=True)
                if mov_files:
                    print("Conversion in progress ...")
                    for t in mov_files:
                        out_filename = os.path.splitext(t)[0] + '.ogg'
                        stream = ffmpeg.input(t)
                        stream = ffmpeg.output(stream, out_filename, acodec='libvorbis', map_metadata=0)
                        ffmpeg.run(stream, quiet=True)
                        subprocess.run(f"ffmpeg -i {t} -c:v libx265 -c:a aac {t[:-4]}.hevc", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
                    encov = "hevc"
                    break
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    continue
            else:
                QMessageBox.critical(None, "Error", "No files selected")
                continue
        elif video == 19:    #avi en mkv 
            file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                avi_files = glob.glob(f"{file}/**/*.avi", recursive=True)
                if avi_files:
                    print("Conversion in progress ...")
                    for t in avi_files:
                        out_filename = os.path.splitext(t)[0] + '.ogg'
                        stream = ffmpeg.input(t)
                        stream = ffmpeg.output(stream, out_filename, acodec='libvorbis', map_metadata=0)
                        ffmpeg.run(stream, quiet=True)
                        subprocess.run(f"ffmpeg -i {t} -codec copy {t[:-4]}.mkv", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
                    encov = "mkv"
                    break
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    continue
            else:
                QMessageBox.critical(None, "Error", "No files selected")
                continue
        elif video == 20:    #avi en mp4 
            file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                avi_files = glob.glob(f"{file}/**/*.avi", recursive=True)
                if avi_files:
                    print("Conversion in progress ...")
                    for t in avi_files:
                        out_filename = os.path.splitext(t)[0] + '.ogg'
                        stream = ffmpeg.input(t)
                        stream = ffmpeg.output(stream, out_filename, acodec='libvorbis', map_metadata=0)
                        ffmpeg.run(stream, quiet=True)
                        subprocess.run(f"ffmpeg -i {t} -codec copy {t[:-4]}.avi", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
                    encov = "avi"
                    break
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    continue
            else:
                QMessageBox.critical(None, "Error", "No files selected")
                continue
        elif video == 21:    #avi en mov 
            file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                avi_files = glob.glob(f"{file}/**/*.avi", recursive=True)
                if avi_files:
                    print("Conversion in progress ...")
                    for t in avi_files:
                        out_filename = os.path.splitext(t)[0] + '.ogg'
                        stream = ffmpeg.input(t)
                        stream = ffmpeg.output(stream, out_filename, acodec='libvorbis', map_metadata=0)
                        ffmpeg.run(stream, quiet=True)
                        subprocess.run(f"ffmpeg -i {t} -codec copy {t[:-4]}.mov", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
                    encov = "mov"
                    break
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    continue
            else:
                QMessageBox.critical(None, "Error", "No files selected")
                continue
        elif video == 22:    #avi en webm 
            file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                avi_files = glob.glob(f"{file}/**/*.avi", recursive=True)
                if avi_files:
                    print("Conversion in progress ...")
                    for t in avi_files:
                        out_filename = os.path.splitext(t)[0] + '.ogg'
                        stream = ffmpeg.input(t)
                        stream = ffmpeg.output(stream, out_filename, acodec='libvorbis', map_metadata=0)
                        ffmpeg.run(stream, quiet=True)
                        subprocess.run(f"ffmpeg -i {t} -c:v libvpx -c:a libvorbis {t[:-4]}.webm", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
                    encov = "webm"
                    break
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    continue
            else:
                QMessageBox.critical(None, "Error", "No files selected")
                continue        
        elif video == 23:    #avi en flv 
            file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                avi_files = glob.glob(f"{file}/**/*.avi", recursive=True)
                if avi_files:
                    print("Conversion in progress ...")
                    for t in avi_files:
                        out_filename = os.path.splitext(t)[0] + '.ogg'
                        stream = ffmpeg.input(t)
                        stream = ffmpeg.output(stream, out_filename, acodec='libvorbis', map_metadata=0)
                        ffmpeg.run(stream, quiet=True)
                        subprocess.run(f"ffmpeg -i {t} -c:v flv -c:a mp3 {t[:-4]}.flv", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
                    encov = "flv"
                    break
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    continue
            else:
                QMessageBox.critical(None, "Error", "No files selected")
                continue         
        elif video == 24:    #avi en hevc 
            file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                avi_files = glob.glob(f"{file}/**/*.avi", recursive=True)
                if avi_files:
                    print("Conversion in progress ...")
                    for t in avi_files:
                        out_filename = os.path.splitext(t)[0] + '.ogg'
                        stream = ffmpeg.input(t)
                        stream = ffmpeg.output(stream, out_filename, acodec='libvorbis', map_metadata=0)
                        ffmpeg.run(stream, quiet=True)
                        subprocess.run(f"ffmpeg -i {t} -c:v libx265 -c:a aac {t[:-4]}.hevc", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
                    encov = "hevc"
                    break
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    continue
            else:
                QMessageBox.critical(None, "Error", "No files selected")
                continue
        elif video == 25:    #webm en avi 
            file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                webm_files = glob.glob(f"{file}/**/*.webm", recursive=True)
                if webm_files:
                    print("Conversion in progress ...")
                    for t in webm_files:
                        out_filename = os.path.splitext(t)[0] + '.ogg'
                        stream = ffmpeg.input(t)
                        stream = ffmpeg.output(stream, out_filename, acodec='libvorbis', map_metadata=0)
                        ffmpeg.run(stream, quiet=True)
                        subprocess.run(f"ffmpeg -i {t} -codec copy {t[:-5]}.avi", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
                    encov = "avi"
                    break
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    continue
            else:
                QMessageBox.critical(None, "Error", "No files selected")
                continue
        elif video == 26:    #webm en mkv 
            file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                webm_files = glob.glob(f"{file}/**/*.webm", recursive=True)
                if webm_files:
                    print("Conversion in progress ...")
                    for t in webm_files:
                        out_filename = os.path.splitext(t)[0] + '.ogg'
                        stream = ffmpeg.input(t)
                        stream = ffmpeg.output(stream, out_filename, acodec='libvorbis', map_metadata=0)
                        ffmpeg.run(stream, quiet=True)
                        subprocess.run(f"ffmpeg -i {t} -codec copy {t[:-5]}.mkv", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
                    encov = "mkv"
                    break
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    continue
            else:
                QMessageBox.critical(None, "Error", "No files selected")
                continue
        elif video == 27:    #webm en mov 
            file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                webm_files = glob.glob(f"{file}/**/*.webm", recursive=True)
                if webm_files:
                    print("Conversion in progress ...")
                    for t in webm_files:
                        out_filename = os.path.splitext(t)[0] + '.ogg'
                        stream = ffmpeg.input(t)
                        stream = ffmpeg.output(stream, out_filename, acodec='libvorbis', map_metadata=0)
                        ffmpeg.run(stream, quiet=True)
                        subprocess.run(f"ffmpeg -i {t} -codec copy {t[:-5]}.mov", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
                    encov = "mov"
                    break
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    continue
            else:
                QMessageBox.critical(None, "Error", "No files selected")
                continue
        elif video == 28:    #webm en mp4 
            file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                webm_files = glob.glob(f"{file}/**/*.webm", recursive=True)
                if webm_files:
                    print("Conversion in progress ...")
                    for t in webm_files:
                        out_filename = os.path.splitext(t)[0] + '.ogg'
                        stream = ffmpeg.input(t)
                        stream = ffmpeg.output(stream, out_filename, acodec='libvorbis', map_metadata=0)
                        ffmpeg.run(stream, quiet=True)
                        subprocess.run(f"ffmpeg -i {t} -codec copy {t[:-5]}.mp4", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
                    encov = "mp4"
                    break
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    continue
            else:
                QMessageBox.critical(None, "Error", "No files selected")
                continue        
        elif video == 29:    #webm en flv 
            file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                webm_files = glob.glob(f"{file}/**/*.webm", recursive=True)
                if webm_files:
                    print("Conversion in progress ...")
                    for t in webm_files:
                        out_filename = os.path.splitext(t)[0] + '.ogg'
                        stream = ffmpeg.input(t)
                        stream = ffmpeg.output(stream, out_filename, acodec='libvorbis', map_metadata=0)
                        ffmpeg.run(stream, quiet=True)
                        subprocess.run(f"ffmpeg -i {t} -c:v flv -c:a mp3 {t[:-5]}.flv", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
                    encov = "flv"
                    break
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    continue
            else:
                QMessageBox.critical(None, "Error", "No files selected")
                continue         
        elif video == 30:    #webm en hevc 
            file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                webm_files = glob.glob(f"{file}/**/*.webm", recursive=True)
                if webm_files:
                    print("Conversion in progress ...")
                    for t in webm_files:
                        out_filename = os.path.splitext(t)[0] + '.ogg'
                        stream = ffmpeg.input(t)
                        stream = ffmpeg.output(stream, out_filename, acodec='libvorbis', map_metadata=0)
                        ffmpeg.run(stream, quiet=True)
                        subprocess.run(f"ffmpeg -i {t} -c:v libx265 -c:a aac {t[:-5]}.hevc", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
                    encov = "hevc"
                    break
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    continue
            else:
                QMessageBox.critical(None, "Error", "No files selected")
                continue
        elif video == 31:    #hevc en avi 
            file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                hevc_files = glob.glob(f"{file}/**/*.hevc", recursive=True)
                if hevc_files:
                    print("Conversion in progress ...")
                    for t in hevc_files:
                        out_filename = os.path.splitext(t)[0] + '.ogg'
                        stream = ffmpeg.input(t)
                        stream = ffmpeg.output(stream, out_filename, acodec='libvorbis', map_metadata=0)
                        ffmpeg.run(stream, quiet=True)
                        subprocess.run(f"ffmpeg -i {t} -codec copy {t[:-5]}.avi", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
                    encov = "avi"
                    break
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    continue
            else:
                QMessageBox.critical(None, "Error", "No files selected")
                continue
        elif video == 32:    #hevc en mkv 
            file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                hevc_files = glob.glob(f"{file}/**/*.hevc", recursive=True)
                if hevc_files:
                    print("Conversion in progress ...")
                    for t in hevc_files:
                        out_filename = os.path.splitext(t)[0] + '.ogg'
                        stream = ffmpeg.input(t)
                        stream = ffmpeg.output(stream, out_filename, acodec='libvorbis', map_metadata=0)
                        ffmpeg.run(stream, quiet=True)
                        subprocess.run(f"ffmpeg -i {t} -codec copy {t[:-5]}.mkv", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
                    encov = "mkv"
                    break
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    continue
            else:
                QMessageBox.critical(None, "Error", "No files selected")
                continue
        elif video == 33:    #hevc en mov 
            file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                hevc_files = glob.glob(f"{file}/**/*.hevc", recursive=True)
                if hevc_files:
                    print("Conversion in progress ...")
                    for t in hevc_files:
                        out_filename = os.path.splitext(t)[0] + '.ogg'
                        stream = ffmpeg.input(t)
                        stream = ffmpeg.output(stream, out_filename, acodec='libvorbis', map_metadata=0)
                        ffmpeg.run(stream, quiet=True)
                        subprocess.run(f"ffmpeg -i {t} -codec copy {t[:-5]}.mov", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
                    encov = "mov"
                    break
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    continue
            else:
                QMessageBox.critical(None, "Error", "No files selected")
                continue
        elif video == 34:    #hevc en mp4 
            file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                hevc_files = glob.glob(f"{file}/**/*.hevc", recursive=True)
                if hevc_files:
                    print("Conversion in progress ...")
                    for t in hevc_files:
                        out_filename = os.path.splitext(t)[0] + '.ogg'
                        stream = ffmpeg.input(t)
                        stream = ffmpeg.output(stream, out_filename, acodec='libvorbis', map_metadata=0)
                        ffmpeg.run(stream, quiet=True)
                        subprocess.run(f"ffmpeg -i {t} -codec copy {t[:-5]}.mp4", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
                    encov = "mp4"
                    break
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    continue
            else:
                QMessageBox.critical(None, "Error", "No files selected")
                continue        
        elif video == 35:    #hevc en flv 
            file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                hevc_files = glob.glob(f"{file}/**/*.hevc", recursive=True)
                if hevc_files:
                    print("Conversion in progress ...")
                    for t in hevc_files:
                        out_filename = os.path.splitext(t)[0] + '.ogg'
                        stream = ffmpeg.input(t)
                        stream = ffmpeg.output(stream, out_filename, acodec='libvorbis', map_metadata=0)
                        ffmpeg.run(stream, quiet=True)
                        subprocess.run(f"ffmpeg -i {t} -c:v flv -c:a mp3 {t[:-5]}.flv", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
                    encov = "flv"
                    break
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    continue
            else:
                QMessageBox.critical(None, "Error", "No files selected")
                continue         
        elif video == 36:    #hevc en webm 
            file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                hevc_files = glob.glob(f"{file}/**/*.hevc", recursive=True)
                if hevc_files:
                    print("Conversion in progress ...")
                    for t in hevc_files:
                        out_filename = os.path.splitext(t)[0] + '.ogg'
                        stream = ffmpeg.input(t)
                        stream = ffmpeg.output(stream, out_filename, acodec='libvorbis', map_metadata=0)
                        ffmpeg.run(stream, quiet=True)
                        subprocess.run(f"ffmpeg -i {t} -c:v libvpx -c:a libvorbis {t[:-5]}.webm", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
                    encov = "webm"
                    break
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    continue
            else:
                QMessageBox.critical(None, "Error", "No files selected")
                continue
        elif video == 37:    #flv en avi 
            file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                flv_files = glob.glob(f"{file}/**/*.flv", recursive=True)
                if flv_files:
                    print("Conversion in progress ...")
                    for t in flv_files:
                        out_filename = os.path.splitext(t)[0] + '.ogg'
                        stream = ffmpeg.input(t)
                        stream = ffmpeg.output(stream, out_filename, acodec='libvorbis', map_metadata=0)
                        ffmpeg.run(stream, quiet=True)
                        subprocess.run(f"ffmpeg -i {t} -codec copy {t[:-4]}.avi", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
                    encov = "avi"
                    break
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    continue
            else:
                QMessageBox.critical(None, "Error", "No files selected")
                continue
        elif video == 38:    #flv en mkv 
            file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                flv_files = glob.glob(f"{file}/**/*.flv", recursive=True)
                if flv_files:
                    print("Conversion in progress ...")
                    for t in flv_files:
                        out_filename = os.path.splitext(t)[0] + '.ogg'
                        stream = ffmpeg.input(t)
                        stream = ffmpeg.output(stream, out_filename, acodec='libvorbis', map_metadata=0)
                        ffmpeg.run(stream, quiet=True)
                        subprocess.run(f"ffmpeg -i {t} -codec copy {t[:-4]}.mkv", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
                    encov = "mkv"
                    break
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    continue
            else:
                QMessageBox.critical(None, "Error", "No files selected")
                continue
        elif video == 39:    #flv en mov 
            file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                flv_files = glob.glob(f"{file}/**/*.flv", recursive=True)
                if flv_files:
                    print("Conversion in progress ...")
                    for t in flv_files:
                        out_filename = os.path.splitext(t)[0] + '.ogg'
                        stream = ffmpeg.input(t)
                        stream = ffmpeg.output(stream, out_filename, acodec='libvorbis', map_metadata=0)
                        ffmpeg.run(stream, quiet=True)
                        subprocess.run(f"ffmpeg -i {t} -codec copy {t[:-4]}.mov", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
                    encov = "mov"
                    break
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    continue
            else:
                QMessageBox.critical(None, "Error", "No files selected")
                continue
        elif video == 40:    #flv en mp4 
            file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                flv_files = glob.glob(f"{file}/**/*.flv", recursive=True)
                if flv_files:
                    print("Conversion in progress ...")
                    for t in flv_files:
                        out_filename = os.path.splitext(t)[0] + '.ogg'
                        stream = ffmpeg.input(t)
                        stream = ffmpeg.output(stream, out_filename, acodec='libvorbis', map_metadata=0)
                        ffmpeg.run(stream, quiet=True)
                        subprocess.run(f"ffmpeg -i {t} -codec copy {t[:-4]}.mp4", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
                    encov = "mp4"
                    break
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    continue
            else:
                QMessageBox.critical(None, "Error", "No files selected")
                continue        
        elif video == 41:    #flv en hevc 
            file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                flv_files = glob.glob(f"{file}/**/*.flv", recursive=True)
                if flv_files:
                    print("Conversion in progress ...")
                    for t in flv_files:
                        out_filename = os.path.splitext(t)[0] + '.ogg'
                        stream = ffmpeg.input(t)
                        stream = ffmpeg.output(stream, out_filename, acodec='libvorbis', map_metadata=0)
                        ffmpeg.run(stream, quiet=True)
                        subprocess.run(f"ffmpeg -i {t} -c:v libx265 -c:a aac {t[:-4]}.hevc", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
                    encov = "hevc"
                    break
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    continue
            else:
                QMessageBox.critical(None, "Error", "No files selected")
                continue         
        elif video == 42:    #flv en webm 
            file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                flv_files = glob.glob(f"{file}/**/*.flv", recursive=True)
                if flv_files:
                    print("Conversion in progress ...")
                    for t in flv_files:
                        out_filename = os.path.splitext(t)[0] + '.ogg'
                        stream = ffmpeg.input(t)
                        stream = ffmpeg.output(stream, out_filename, acodec='libvorbis', map_metadata=0)
                        ffmpeg.run(stream, quiet=True)
                        subprocess.run(f"ffmpeg -i {t} -c:v libvpx -c:a libvorbis {t[:-4]}.webm", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
                    encov = "webm"
                    break
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    continue
            else:
                QMessageBox.critical(None, "Error", "No files selected")
                continue
        else:
            QMessageBox.critical(None, "Error", "An unexpected error has occurred")
            continue
        
def convertissso_subtitle():
    video=40
    while True:
        if video == 1:  #vtt en srt 
            file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                vtt_files = glob.glob(f"{file}/**/*.vtt", recursive=True)
                if vtt_files:
                    print("Conversion in progress ...")
                    for t in vtt_files:
                        out_filename = os.path.splitext(t)[0] + '.srt'
                        stream = ffmpeg.input(t)
                        stream = ffmpeg.output(stream, out_filename, map_metadata=0)
                        ffmpeg.run(stream, quiet=True)
                    encov = "srt"
                    break
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    continue
            else:
                QMessageBox.critical(None, "Error", "No files selected")
                continue
        elif video == 2:  #vtt en ass
            file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                vtt_files = glob.glob(f"{file}/**/*.vtt", recursive=True)
                if vtt_files:
                    print("Conversion in progress ...")
                    for t in vtt_files:
                        out_filename = os.path.splitext(t)[0] + '.ogg'
                        stream = ffmpeg.input(t)
                        stream = ffmpeg.output(stream, out_filename, acodec='libvorbis', map_metadata=0)
                        ffmpeg.run(stream, quiet=True)
                        subprocess.run(f"ffmpeg -i {t} {t[:-4]}.ass", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
                    encov = "ass"
                    break
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    continue
            else:
                QMessageBox.critical(None, "Error", "No files selected")
                continue
        if video == 3:  # vtt en lrc
            file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                vtt_files = glob.glob(f"{file}/**/*.vtt", recursive=True)
                if vtt_files:
                    print("Conversion in progress ...")
                    for t in vtt_files:
                        out_filename = os.path.splitext(t)[0] + '.ogg'
                        stream = ffmpeg.input(t)
                        stream = ffmpeg.output(stream, out_filename, acodec='libvorbis', map_metadata=0)
                        ffmpeg.run(stream, quiet=True)
                        subprocess.run(f"ffmpeg -i {t} {t[:-4]}.lrc", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
                    encov = "lrc"
                    break
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    continue
            else:
                QMessageBox.critical(None, "Error", "No files selected")
                continue
        elif video == 4:  # srt en vtt
            file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                srt_files = glob.glob(f"{file}/**/*.srt", recursive=True)
                if srt_files:
                    print("Conversion in progress ...")
                    for t in srt_files:
                        out_filename = os.path.splitext(t)[0] + '.ogg'
                        stream = ffmpeg.input(t)
                        stream = ffmpeg.output(stream, out_filename, acodec='libvorbis', map_metadata=0)
                        ffmpeg.run(stream, quiet=True)
                        subprocess.run(f"ffmpeg -i {t} {t[:-4]}.vtt", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
                    encov = "vtt"
                    break
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    continue
            else:
                QMessageBox.critical(None, "Error", "No files selected")
                continue
        elif video == 5:  # srt en ass
            file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                srt_files = glob.glob(f"{file}/**/*.srt", recursive=True)
                if srt_files:
                    print("Conversion in progress ...")
                    for t in srt_files:
                        out_filename = os.path.splitext(t)[0] + '.ogg'
                        stream = ffmpeg.input(t)
                        stream = ffmpeg.output(stream, out_filename, acodec='libvorbis', map_metadata=0)
                        ffmpeg.run(stream, quiet=True)
                        subprocess.run(f"ffmpeg -i {t} {t[:-4]}.ass", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
                    encov = "ass"
                    break
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    continue
            else:
                QMessageBox.critical(None, "Error", "No files selected")
                continue
        elif video == 6:  # srt en lrc
            file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                srt_files = glob.glob(f"{file}/**/*.srt", recursive=True)
                if srt_files:
                    print("Conversion in progress ...")
                    for t in srt_files:
                        out_filename = os.path.splitext(t)[0] + '.ogg'
                        stream = ffmpeg.input(t)
                        stream = ffmpeg.output(stream, out_filename, acodec='libvorbis', map_metadata=0)
                        ffmpeg.run(stream, quiet=True)
                        subprocess.run(f"ffmpeg -i {t} {t[:-4]}.lrc", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
                    encov = "lrc"
                    break
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    continue
            else:
                QMessageBox.critical(None, "Error", "No files selected")
                continue        
        elif video == 7:    #ass en srt 
            file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                ass_files = glob.glob(f"{file}/**/*.ass", recursive=True)
                if ass_files:
                    print("Conversion in progress ...")
                    for t in ass_files:
                        out_filename = os.path.splitext(t)[0] + '.ogg'
                        stream = ffmpeg.input(t)
                        stream = ffmpeg.output(stream, out_filename, acodec='libvorbis', map_metadata=0)
                        ffmpeg.run(stream, quiet=True)
                        subprocess.run(f"ffmpeg -i {t} {t[:-4]}.srt", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
                    encov = "srt"
                    break
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    continue
            else:
                QMessageBox.critical(None, "Error", "No files selected")
                continue
        elif video == 8:    #ass en lrc 
            file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                ass_files = glob.glob(f"{file}/**/*.ass", recursive=True)
                if ass_files:
                    print("Conversion in progress ...")
                    for t in ass_files:
                        out_filename = os.path.splitext(t)[0] + '.ogg'
                        stream = ffmpeg.input(t)
                        stream = ffmpeg.output(stream, out_filename, acodec='libvorbis', map_metadata=0)
                        ffmpeg.run(stream, quiet=True)
                        subprocess.run(f"ffmpeg -i {t} {t[:-4]}.lrc", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
                    encov = "lrc"
                    break
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    continue
            else:
                QMessageBox.critical(None, "Error", "No files selected")
                continue
        elif video == 9:    #ass en vtt 
            file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                ass_files = glob.glob(f"{file}/**/*.ass", recursive=True)
                if ass_files:
                    print("Conversion in progress ...")
                    for t in ass_files:
                        out_filename = os.path.splitext(t)[0] + '.ogg'
                        stream = ffmpeg.input(t)
                        stream = ffmpeg.output(stream, out_filename, acodec='libvorbis', map_metadata=0)
                        ffmpeg.run(stream, quiet=True)
                        subprocess.run(f"ffmpeg -i {t} {t[:-4]}.vtt", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
                    encov = "vtt"
                    break
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    continue
            else:
                QMessageBox.critical(None, "Error", "No files selected")
                continue
        elif video == 10:    #lrc en srt 
            file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                lrc_files = glob.glob(f"{file}/**/*.lrc", recursive=True)
                if lrc_files:
                    print("Conversion in progress ...")
                    for t in lrc_files:
                        out_filename = os.path.splitext(t)[0] + '.ogg'
                        stream = ffmpeg.input(t)
                        stream = ffmpeg.output(stream, out_filename, acodec='libvorbis', map_metadata=0)
                        ffmpeg.run(stream, quiet=True)
                        subprocess.run(f"ffmpeg -i {t} {t[:-4]}.srt", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
                    encov = "srt"
                    break
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    continue
            else:
                QMessageBox.critical(None, "Error", "No files selected")
                continue        
        elif video == 11:    #lrc en ass 
            file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                lrc_files = glob.glob(f"{file}/**/*.lrc", recursive=True)
                if lrc_files:
                    print("Conversion in progress ...")
                    for t in lrc_files:
                        out_filename = os.path.splitext(t)[0] + '.ogg'
                        stream = ffmpeg.input(t)
                        stream = ffmpeg.output(stream, out_filename, acodec='libvorbis', map_metadata=0)
                        ffmpeg.run(stream, quiet=True)
                        subprocess.run(f"ffmpeg -i {t} {t[:-4]}.ass", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
                    encov = "ass"
                    break
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    continue
            else:
                QMessageBox.critical(None, "Error", "No files selected")
                continue         
        elif video == 12:    #lrc en vtt 
            file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                lrc_files = glob.glob(f"{file}/**/*.lrc", recursive=True)
                if lrc_files:
                    print("Conversion in progress ...")
                    for t in lrc_files:
                        out_filename = os.path.splitext(t)[0] + '.ogg'
                        stream = ffmpeg.input(t)
                        stream = ffmpeg.output(stream, out_filename, acodec='libvorbis', map_metadata=0)
                        ffmpeg.run(stream, quiet=True)
                        subprocess.run(f"ffmpeg -i {t} {t[:-4]}.vtt", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
                    encov = "vtt"
                    break
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    continue
            else:
                QMessageBox.critical(None, "Error", "No files selected")
                continue         
        else:
            QMessageBox.critical(None, "Error", "An unexpected error has occurred")
            continue
        
def convertissso_audio():

    while True:
        if audio == 1:  # mp3 en ogg
            file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                mp3_files = glob.glob(f"{file}/**/*.mp3", recursive=True)
                if mp3_files:
                    print("Conversion in progress ...")
                    for t in mp3_files:
                        out_filename = os.path.splitext(t)[0] + '.ogg'
                        stream = ffmpeg.input(t)
                        stream = ffmpeg.output(stream, out_filename, acodec='libvorbis', map_metadata=0)
                        ffmpeg.run(stream, quiet=True)
                    encov = "ogg"
                    break
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    continue
            else:
                QMessageBox.critical(None, "Error", "No files selected")
                continue
        elif audio == 2:  # mp3 en aac
            file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                mp3_files = glob.glob(f"{file}/**/*.mp3", recursive=True)
                if mp3_files:
                    print("Conversion in progress ...")
                    for t in mp3_files:
                        out_filename = os.path.splitext(t)[0] + '.aac'
                        stream = ffmpeg.input(t)
                        stream = ffmpeg.output(stream, out_filename, acodec='aac', map_metadata=0)
                        ffmpeg.run(stream, quiet=True)
                    encov = "aac"
                    break
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    continue
            else:
                QMessageBox.critical(None, "Error", "No files selected")
                continue
        if audio == 3:  # mp3 en wav
            file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                mp3_files = glob.glob(f"{file}/**/*.mp3", recursive=True)
                if mp3_files:
                    print("Conversion in progress ...")
                    for t in mp3_files:
                        out_filename = os.path.splitext(t)[0] + '.wav'
                        stream = ffmpeg.input(t)
                        stream = ffmpeg.output(stream, out_filename, map_metadata=0)
                        ffmpeg.run(stream, quiet=True)
                    encov = "wav"
                    break
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    continue
            else:
                QMessageBox.critical(None, "Error", "No files selected")
                continue
        elif audio == 4:  # mp3 en ac3
            file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                mp3_files = glob.glob(f"{file}/**/*.mp3", recursive=True)
                if mp3_files:
                    print("Conversion in progress ...")
                    for t in mp3_files:
                        out_filename = os.path.splitext(t)[0] + '.ac3'
                        stream = ffmpeg.input(t)
                        stream = ffmpeg.output(stream, out_filename, acodec='ac3', map_metadata=0)
                        ffmpeg.run(stream, quiet=True)
                    encov = "ac3"
                    break
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    continue
            else:
                QMessageBox.critical(None, "Error", "No files selected")
                continue
        elif audio == 5:  # mp3 en opus
            file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                mp3_files = glob.glob(f"{file}/**/*.mp3", recursive=True)
                if mp3_files:
                    print("Conversion in progress ...")
                    for t in mp3_files:
                        out_filename = os.path.splitext(t)[0] + '.opus'
                        stream = ffmpeg.input(t)
                        stream = ffmpeg.output(stream, out_filename, acodec='libopus', map_metadata=0)
                        ffmpeg.run(stream, quiet=True)
                    encov = "opus"
                    break
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    continue
            else:
                QMessageBox.critical(None, "Error", "No files selected")
                continue                
        elif audio == 6:  # wav en mp3
            file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                wav_files = glob.glob(f"{file}/**/*.wav", recursive=True)
                if wav_files:
                    print("Conversion in progress ...")
                    for t in wav_files:
                        out_filename = os.path.splitext(t)[0] + '.mp3'
                        stream = ffmpeg.input(t)
                        stream = ffmpeg.output(stream, out_filename, acodec='libmp3lame', map_metadata=0)
                        ffmpeg.run(stream, quiet=True)
                    encov = "mp3"
                    break
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    continue
            else:
                QMessageBox.critical(None, "Error", "No files selected")
                continue 
        elif audio == 7:  # wav en ogg
            file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                wav_files = glob.glob(f"{file}/**/*.wav", recursive=True)
                if wav_files:
                    print("Conversion in progress ...")
                    for t in wav_files:
                        out_filename = os.path.splitext(t)[0] + '.ogg'
                        stream = ffmpeg.input(t)
                        stream = ffmpeg.output(stream, out_filename, acodec='libvorbis', map_metadata=0)
                        ffmpeg.run(stream, quiet=True)
                    encov = "ogg"
                    break
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    continue
            else:
                QMessageBox.critical(None, "Error", "No files selected")
                continue
        if audio == 8:  # wav en aac
            file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                wav_files = glob.glob(f"{file}/**/*.wav", recursive=True)
                if wav_files:
                    print("Conversion in progress ...")
                    for t in wav_files:
                        out_filename = os.path.splitext(t)[0] + '.aac'
                        stream = ffmpeg.input(t)
                        stream = ffmpeg.output(stream, out_filename, acodec='aac', map_metadata=0)
                        ffmpeg.run(stream, quiet=True)
                    encov = "aac"
                    break
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    continue
            else:
                QMessageBox.critical(None, "Error", "No files selected")
                continue
        elif audio == 9:  # wav en ac3
            file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                wav_files = glob.glob(f"{file}/**/*.wav", recursive=True)
                if wav_files:
                    print("Conversion in progress ...")
                    for t in wav_files:
                        out_filename = os.path.splitext(t)[0] + '.ac3'
                        stream = ffmpeg.input(t)
                        stream = ffmpeg.output(stream, out_filename, acodec='ac3', map_metadata=0)
                        ffmpeg.run(stream, quiet=True)
                    encov = "ac3"
                    break
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    continue
            else:
                QMessageBox.critical(None, "Error", "No files selected")
                continue
        elif audio == 10:  # wav en opus
            file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                wav_files = glob.glob(f"{file}/**/*.wav", recursive=True)
                if wav_files:
                    print("Conversion in progress ...")
                    for t in wav_files:
                        out_filename = os.path.splitext(t)[0] + '.opus'
                        stream = ffmpeg.input(t)
                        stream = ffmpeg.output(stream, out_filename, acodec='libopus', map_metadata=0)
                        ffmpeg.run(stream, quiet=True)
                    encov = "opus"
                    break
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    continue
            else:
                QMessageBox.critical(None, "Error", "No files selected")
                continue
        elif audio == 11:  # ogg en mp3
            file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                ogg_files = glob.glob(f"{file}/**/*.ogg", recursive=True)
                if ogg_files:
                    print("Conversion in progress ...")
                    for t in ogg_files:
                        out_filename = os.path.splitext(t)[0] + '.mp3'
                        stream = ffmpeg.input(t)
                        stream = ffmpeg.output(stream, out_filename, acodec='libmp3lame', map_metadata=0)
                        ffmpeg.run(stream, quiet=True)
                    encov = "mp3"
                    break
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    continue
            else:
                QMessageBox.critical(None, "Error", "No files selected")
                continue 
        elif audio == 12:  # ogg en wav
            file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                ogg_files = glob.glob(f"{file}/**/*.ogg", recursive=True)
                if ogg_files:
                    print("Conversion in progress ...")
                    for t in ogg_files:
                        out_filename = os.path.splitext(t)[0] + '.wav'
                        stream = ffmpeg.input(t)
                        stream = ffmpeg.output(stream, out_filename, map_metadata=0)
                        ffmpeg.run(stream, quiet=True)
                    encov = "ogg"
                    break
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    continue
            else:
                QMessageBox.critical(None, "Error", "No files selected")
                continue
        if audio == 13:  # ogg en aac
            file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                ogg_files = glob.glob(f"{file}/**/*.ogg", recursive=True)
                if ogg_files:
                    print("Conversion in progress ...")
                    for t in ogg_files:
                        out_filename = os.path.splitext(t)[0] + '.aac'
                        stream = ffmpeg.input(t)
                        stream = ffmpeg.output(stream, out_filename, acodec='aac', map_metadata=0)
                        ffmpeg.run(stream, quiet=True)
                    encov = "aac"
                    break
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    continue
            else:
                QMessageBox.critical(None, "Error", "No files selected")
                continue
        elif audio == 14:  # ogg en ac3
            file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                ogg_files = glob.glob(f"{file}/**/*.ogg", recursive=True)
                if ogg_files:
                    print("Conversion in progress ...")
                    for t in ogg_files:
                        out_filename = os.path.splitext(t)[0] + '.ac3'
                        stream = ffmpeg.input(t)
                        stream = ffmpeg.output(stream, out_filename, acodec='ac3', map_metadata=0)
                        ffmpeg.run(stream, quiet=True)
                    encov = "ac3"
                    break
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    continue
            else:
                QMessageBox.critical(None, "Error", "No files selected")
                continue
        elif audio == 15:  # ogg en opus
            file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                ogg_files = glob.glob(f"{file}/**/*.ogg", recursive=True)
                if ogg_files:
                    print("Conversion in progress ...")
                    for t in ogg_files:
                        out_filename = os.path.splitext(t)[0] + '.opus'
                        stream = ffmpeg.input(t)
                        stream = ffmpeg.output(stream, out_filename, acodec='libopus', map_metadata=0)
                        ffmpeg.run(stream, quiet=True)
                    encov = "opus"
                    break
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    continue
            else:
                QMessageBox.critical(None, "Error", "No files selected")
                continue
        elif audio == 16:  # ac3 en mp3
            file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                ac3_files = glob.glob(f"{file}/**/*.ac3", recursive=True)
                if ac3_files:
                    print("Conversion in progress ...")
                    for t in ac3_files:
                        out_filename = os.path.splitext(t)[0] + '.mp3'
                        stream = ffmpeg.input(t)
                        stream = ffmpeg.output(stream, out_filename, acodec='libmp3lame', map_metadata=0)
                        ffmpeg.run(stream, quiet=True)
                    encov = "mp3"
                    break
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    continue
            else:
                QMessageBox.critical(None, "Error", "No files selected")
                continue 
        elif audio == 17:  # ac3 en wav
            file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                ac3_files = glob.glob(f"{file}/**/*.ac3", recursive=True)
                if ac3_files:
                    print("Conversion in progress ...")
                    for t in ac3_files:
                        out_filename = os.path.splitext(t)[0] + '.wav'
                        stream = ffmpeg.input(t)
                        stream = ffmpeg.output(stream, out_filename, map_metadata=0)
                        ffmpeg.run(stream, quiet=True)
                    encov = "wav"
                    break
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    continue
            else:
                QMessageBox.critical(None, "Error", "No files selected")
                continue
        if audio == 18:  # ac3 en aac
            file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                ac3_files = glob.glob(f"{file}/**/*.ac3", recursive=True)
                if ac3_files:
                    print("Conversion in progress ...")
                    for t in ac3_files:
                        out_filename = os.path.splitext(t)[0] + '.aac'
                        stream = ffmpeg.input(t)
                        stream = ffmpeg.output(stream, out_filename, acodec='aac', map_metadata=0)
                        ffmpeg.run(stream, quiet=True)
                    encov = "aac"
                    break
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    continue
            else:
                QMessageBox.critical(None, "Error", "No files selected")
                continue
        elif audio == 19:  # ac3 en ogg
            file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                ac3_files = glob.glob(f"{file}/**/*.ac3", recursive=True)
                if ac3_files:
                    print("Conversion in progress ...")
                    for t in ac3_files:
                        out_filename = os.path.splitext(t)[0] + '.ogg'
                        stream = ffmpeg.input(t)
                        stream = ffmpeg.output(stream, out_filename, acodec='libvorbis', map_metadata=0)
                        ffmpeg.run(stream, quiet=True)
                    encov = "ogg"
                    break
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    continue
            else:
                QMessageBox.critical(None, "Error", "No files selected")
                continue
        elif audio == 20:  # ac3 en opus
            file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                ac3_files = glob.glob(f"{file}/**/*.ac3", recursive=True)
                if ac3_files:
                    print("Conversion in progress ...")
                    for t in ac3_files:
                        out_filename = os.path.splitext(t)[0] + '.opus'
                        stream = ffmpeg.input(t)
                        stream = ffmpeg.output(stream, out_filename, acodec='libopus', map_metadata=0)
                        ffmpeg.run(stream, quiet=True)
                    encov = "opus"
                    break
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    continue
            else:
                QMessageBox.critical(None, "Error", "No files selected")
                continue           
        elif audio == 21:  # aac en wav
            file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                aac_files = glob.glob(f"{file}/**/*.aac", recursive=True)
                if aac_files:
                    print("Conversion in progress ...")
                    for t in aac_files:
                        out_filename = os.path.splitext(t)[0] + '.wav'
                        stream = ffmpeg.input(t)
                        stream = ffmpeg.output(stream, out_filename, map_metadata=0)
                        ffmpeg.run(stream, quiet=True)
                    encov = "wav"
                    break
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    continue
            else:
                QMessageBox.critical(None, "Error", "No files selected")
                continue 
        elif audio == 22:  # aac en ac3
            file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                aac_files = glob.glob(f"{file}/**/*.aac", recursive=True)
                if aac_files:
                    print("Conversion in progress ...")
                    for t in aac_files:
                        out_filename = os.path.splitext(t)[0] + '.ac3'
                        stream = ffmpeg.input(t)
                        stream = ffmpeg.output(stream, out_filename, acodec='ac3', map_metadata=0)
                        ffmpeg.run(stream, quiet=True)
                    encov = "ac3"
                    break
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    continue
            else:
                QMessageBox.critical(None, "Error", "No files selected")
                continue
        if audio == 23:  # aac en ogg
            file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                aac_files = glob.glob(f"{file}/**/*.aac", recursive=True)
                if aac_files:
                    print("Conversion in progress ...")
                    for t in aac_files:
                        out_filename = os.path.splitext(t)[0] + '.ogg'
                        stream = ffmpeg.input(t)
                        stream = ffmpeg.output(stream, out_filename, acodec='libvorbis', map_metadata=0)
                        ffmpeg.run(stream, quiet=True)
                    encov = "ogg"
                    break
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    continue
            else:
                QMessageBox.critical(None, "Error", "No files selected")
                continue
        elif audio == 24:  # aac en mp3
            file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                aac_files = glob.glob(f"{file}/**/*.aac", recursive=True)
                if aac_files:
                    print("Conversion in progress ...")
                    for t in aac_files:
                        out_filename = os.path.splitext(t)[0] + '.mp3'
                        stream = ffmpeg.input(t)
                        stream = ffmpeg.output(stream, out_filename, acodec='libmp3lame', map_metadata=0)
                        ffmpeg.run(stream, quiet=True)
                    encov = "mp3"
                    break
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    continue
            else:
                QMessageBox.critical(None, "Error", "No files selected")
                continue
        elif audio == 25:  # aac en opus
            file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                aac_files = glob.glob(f"{file}/**/*.aac", recursive=True)
                if aac_files:
                    print("Conversion in progress ...")
                    for t in aac_files:
                        out_filename = os.path.splitext(t)[0] + 'opus'
                        stream = ffmpeg.input(t)
                        stream = ffmpeg.output(stream, out_filename, acodec='libopus', map_metadata=0)
                        ffmpeg.run(stream, quiet=True)
                    encov = "opus"
                    break
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    continue
            else:
                QMessageBox.critical(None, "Error", "No files selected")
                continue
        elif audio == 26:  # flac en mp3
            file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                flac_files = glob.glob(f"{file}/**/*.flac", recursive=True)
                if flac_files:
                    print("Conversion in progress ...")
                    for t in flac_files:
                        out_filename = os.path.splitext(t)[0] + '.mp3'
                        stream = ffmpeg.input(t)
                        stream = ffmpeg.output(stream, out_filename, acodec='libmp3lame', map_metadata=0)
                        ffmpeg.run(stream, quiet=True)
                    encov = "mp3"
                    break
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    continue
            else:
                QMessageBox.critical(None, "Error", "No files selected")
                continue 
        elif audio == 27:  # flac en wav
            file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                flac_files = glob.glob(f"{file}/**/*.flac", recursive=True)
                if flac_files:
                    print("Conversion in progress ...")
                    for t in flac_files:
                        out_filename = os.path.splitext(t)[0] + '.wav'
                        stream = ffmpeg.input(t)
                        stream = ffmpeg.output(stream, out_filename, map_metadata=0)
                        ffmpeg.run(stream, quiet=True)
                    encov = "wav"
                    break
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    continue
            else:
                QMessageBox.critical(None, "Error", "No files selected")
                continue
        if audio == 28:  # flac en ogg
            file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                flac_files = glob.glob(f"{file}/**/*.flac", recursive=True)
                if flac_files:
                    print("Conversion in progress ...")
                    for t in flac_files:
                        out_filename = os.path.splitext(t)[0] + '.ogg'
                        stream = ffmpeg.input(t)
                        stream = ffmpeg.output(stream, out_filename, acodec='libvorbis', map_metadata=0)
                        ffmpeg.run(stream, quiet=True)
                    encov = "ogg"
                    break
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    continue
            else:
                QMessageBox.critical(None, "Error", "No files selected")
                continue
        elif audio == 29:  # flac en ac3
            file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                flac_files = glob.glob(f"{file}/**/*.flac", recursive=True)
                if flac_files:
                    print("Conversion in progress ...")
                    for t in flac_files:
                        out_filename = os.path.splitext(t)[0] + '.ac3'
                        stream = ffmpeg.input(t)
                        stream = ffmpeg.output(stream, out_filename, acodec='ac3', map_metadata=0)
                        ffmpeg.run(stream, quiet=True)
                    encov = "ac3"
                    break
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    continue
            else:
                QMessageBox.critical(None, "Error", "No files selected")
                continue
        elif audio == 30:  # flac en opus
            file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                flac_files = glob.glob(f"{file}/**/*.flac", recursive=True)
                if flac_files:
                    print("Conversion in progress ...")
                    for t in flac_files:
                        out_filename = os.path.splitext(t)[0] + '.opus'
                        stream = ffmpeg.input(t)
                        stream = ffmpeg.output(stream, out_filename, acodec='libopus', map_metadata=0)
                        ffmpeg.run(stream, quiet=True)
                    encov = "opus"
                    break
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    continue
            else:
                QMessageBox.critical(None, "Error", "No files selected")
                continue
        elif audio == 31:  # opus en mp3
            file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                opus_files = glob.glob(f"{file}/**/*.opus", recursive=True)
                if opus_files:
                    print("Conversion in progress ...")
                    for t in opus_files:
                        out_filename = os.path.splitext(t)[0] + '.mp3'
                        stream = ffmpeg.input(t)
                        stream = ffmpeg.output(stream, out_filename, ab='320k', acodec='libmp3lame', map_metadata=0)
                        ffmpeg.run(stream, quiet=True)
                    encov = "mp3"
                    break
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    continue
            else:
                QMessageBox.critical(None, "Error", "No files selected")
                continue 
        if audio == 32:  # opus en ac3
            file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                opus_files = glob.glob(f"{file}/**/*.opus", recursive=True)
                if opus_files:
                    print("Conversion in progress ...")
                    for t in opus_files:
                        out_filename = os.path.splitext(t)[0] + '.ac3'
                        stream = ffmpeg.input(t)
                        stream = ffmpeg.output(stream, out_filename, ab='320k', acodec='ac3', map_metadata=0)
                        ffmpeg.run(stream, quiet=True)
                    encov = "ac3"
                    break
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    continue
            else:
                QMessageBox.critical(None, "Error", "No files selected")
                continue
        elif audio == 33:  # opus en aac
            file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                opus_files = glob.glob(f"{file}/**/*.opus", recursive=True)
                if opus_files:
                    print("Conversion in progress ...")
                    for t in opus_files:
                        out_filename = os.path.splitext(t)[0] + '.aac'
                        stream = ffmpeg.input(t)
                        stream = ffmpeg.output(stream, out_filename, ab='320k', acodec='aac', map_metadata=0)
                        ffmpeg.run(stream, quiet=True)
                    encov = "aac"
                    break
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    continue
            else:
                QMessageBox.critical(None, "Error", "No files selected")
                continue
        elif audio == 34:  # opus en flac
                file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
                if file:
                    opus_files = glob.glob(f"{file}/**/*.opus", recursive=True)
                    if opus_files:
                        print("Conversion in progress ...")
                        for t in opus_files:
                            out_filename = os.path.splitext(t)[0] + '.flac'
                            stream = ffmpeg.input(t)
                            stream = ffmpeg.output(stream, out_filename, acodec='flac', map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                        encov = "flac"
                        break
                    else:
                        QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                        continue
                else:
                    QMessageBox.critical(None, "Error", "No files selected")
                    continue
        elif audio == 35:  # opus en wav
                file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
                if file:
                    opus_files = glob.glob(f"{file}/**/*.opus", recursive=True)
                    if opus_files:
                        print("Conversion in progress ...")
                        for t in opus_files:
                            out_filename = os.path.splitext(t)[0] + '.wav'
                            stream = ffmpeg.input(t)
                            stream = ffmpeg.output(stream, out_filename, map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                        encov = "wav"
                        break
                    else:
                        QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                        continue
                else:
                    QMessageBox.critical(None, "Error", "No files selected")
                    continue      
        elif audio == 36:  # opus en ogg
            file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                opus_files = glob.glob(f"{file}/**/*.opus", recursive=True)
                if opus_files:
                    print("Conversion in progress ...")
                    for t in opus_files:
                        out_filename = os.path.splitext(t)[0].replace("'", "-'").replace(" ", "_") + '.ogg'
                        stream = ffmpeg.input(t)
                        stream = ffmpeg.output(stream, out_filename, ab='320k', map_metadata=0, acodec='libvorbis')
                        ffmpeg.run(stream, quiet=True)
                    encov = "ogg"
                    break
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    continue
            else:
                QMessageBox.critical(None, "Error", "No files selected")
                continue
        else:
            QMessageBox.critical(None, "Error", "An unexpected error has occurred")
            continue    
app.exit()

asd=int(input("Entrer le bon numero: 1=download, 2=video, 3=audio. ->  "))

if asd == 1:
    convertisso_download_video()
elif asd == 2:
    convertissso_video()
elif asd == 3:
    convertissso_audio()
else:
    print("erreur")
