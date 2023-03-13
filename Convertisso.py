#pip install youtube-dl
import os
import subprocess
import shutil
import glob
import ffmpeg
from PyQt5.QtWidgets import QApplication, QFileDialog, QMessageBox
import sys
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
    response = subprocess.call(['ping', '-c', '1', '1.1.1.1'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if response == 0:
            while True:
                    userchoice = int(input("Choose how your video will be downloaded.   : "))
                    userchoicelink = input("Copy the link(URL) of the video and paste it here.  ->  ")
                    destination = input("Enter the destination folder where you want to download the video. ->  ")
                    if userchoice == 1:
                        subprocess.run(['youtube-dl', '-f', 'best', '--add-metadata', userchoicelink])
                        for extension in ["*.mp4", "*.mkv", "*.webm", "*.flv"]:
                            for filename in glob.glob(extension):
                                shutil.move(filename, destination)
                        break
                    elif userchoice == 2:
                        subprocess.run(['youtube-dl', '--write-srt', '--all-subs', '--add-metadata', userchoicelink])
                        for extension in ["*.mp4", "*.mkv", "*.webm", "*.flv", "*.srt", "*.ass", "*.vtt", "*.lrc"]:
                            for filename in glob.glob(extension):
                                shutil.move(filename, destination)
                        break
                    elif userchoice == 3:
                        subprocess.run(['youtube-dl', '-x', '--audio-format', 'best','--add-metadata', userchoicelink])
                        for extension in ["*.mp3", "*.aac", "*.flac", "*.m4a", "*.ogg", "*.wav", "*.opus", "*.vorbis"]:
                            for filename in glob.glob(extension):
                                shutil.move(filename, destination)
                        break
                    elif userchoice == 4:
                        subprocess.run(['youtube-dl', '--all-subs', '--skip-download','--add-metadata', userchoicelink])
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
            filetoconvers = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                mkv_files = glob.glob(f"{filetoconvers}/**/*.mkv", recursive=True)
                if mkv_files:
                    print("Conversion in progress ...")
                    for t in mkv_files:
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
            filetoconvers = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                mkv_files = glob.glob(f"{filetoconvers}/**/*.mkv", recursive=True)
                if mkv_files:
                    print("Conversion in progress ...")
                    for t in mkv_files:
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
            filetoconvers = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                mkv_files = glob.glob(f"{filetoconvers}/**/*.mkv", recursive=True)
                if mkv_files:
                    print("Conversion in progress ...")
                    for t in mkv_files:
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
            filetoconvers = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                mkv_files = glob.glob(f"{filetoconvers}/**/*.mkv", recursive=True)
                if mkv_files:
                    print("Conversion in progress ...")
                    for t in mkv_files:
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
            filetoconvers = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                mp4_files = glob.glob(f"{filetoconvers}/**/*.mp4", recursive=True)
                if mp4_files:
                    print("Conversion in progress ...")
                    for t in mp4_files:
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
            filetoconvers = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                mp4_files = glob.glob(f"{filetoconvers}/**/*.mp4", recursive=True)
                if mp4_files:
                    print("Conversion in progress ...")
                    for t in mp4_files:
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
            filetoconvers = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                mp4_files = glob.glob(f"{filetoconvers}/**/*.mp4", recursive=True)
                if mp4_files:
                    print("Conversion in progress ...")
                    for t in mp4_files:
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
            filetoconvers = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                mp4_files = glob.glob(f"{filetoconvers}/**/*.mp4", recursive=True)
                if mp4_files:
                    print("Conversion in progress ...")
                    for t in mp4_files:
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
            filetoconvers = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                mp4_files = glob.glob(f"{filetoconvers}/**/*.mp4", recursive=True)
                if mp4_files:
                    print("Conversion in progress ...")
                    for t in mp4_files:
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
            filetoconvers = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                mp4_files = glob.glob(f"{filetoconvers}/**/*.mp4", recursive=True)
                if mp4_files:
                    print("Conversion in progress ...")
                    for t in mp4_files:
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
            filetoconvers = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                mov_files = glob.glob(f"{filetoconvers}/**/*.mov", recursive=True)
                if mov_files:
                    print("Conversion in progress ...")
                    for t in mov_files:
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
            filetoconvers = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                mov_files = glob.glob(f"{filetoconvers}/**/*.mov", recursive=True)
                if mov_files:
                    print("Conversion in progress ...")
                    for t in mov_files:
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
            filetoconvers = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                mov_files = glob.glob(f"{filetoconvers}/**/*.mov", recursive=True)
                if mov_files:
                    print("Conversion in progress ...")
                    for t in mov_files:
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
            filetoconvers = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                mov_files = glob.glob(f"{filetoconvers}/**/*.mov", recursive=True)
                if mov_files:
                    print("Conversion in progress ...")
                    for t in mov_files:
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
            filetoconvers = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                mov_files = glob.glob(f"{filetoconvers}/**/*.mov", recursive=True)
                if mov_files:
                    print("Conversion in progress ...")
                    for t in mov_files:
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
            filetoconvers = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                mov_files = glob.glob(f"{filetoconvers}/**/*.mov", recursive=True)
                if mov_files:
                    print("Conversion in progress ...")
                    for t in mov_files:
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
            filetoconvers = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                avi_files = glob.glob(f"{filetoconvers}/**/*.avi", recursive=True)
                if avi_files:
                    print("Conversion in progress ...")
                    for t in avi_files:
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
            filetoconvers = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                avi_files = glob.glob(f"{filetoconvers}/**/*.avi", recursive=True)
                if avi_files:
                    print("Conversion in progress ...")
                    for t in avi_files:
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
            filetoconvers = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                avi_files = glob.glob(f"{filetoconvers}/**/*.avi", recursive=True)
                if avi_files:
                    print("Conversion in progress ...")
                    for t in avi_files:
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
            filetoconvers = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                avi_files = glob.glob(f"{filetoconvers}/**/*.avi", recursive=True)
                if avi_files:
                    print("Conversion in progress ...")
                    for t in avi_files:
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
            filetoconvers = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                avi_files = glob.glob(f"{filetoconvers}/**/*.avi", recursive=True)
                if avi_files:
                    print("Conversion in progress ...")
                    for t in avi_files:
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
            filetoconvers = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                avi_files = glob.glob(f"{filetoconvers}/**/*.avi", recursive=True)
                if avi_files:
                    print("Conversion in progress ...")
                    for t in avi_files:
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
            filetoconvers = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                webm_files = glob.glob(f"{filetoconvers}/**/*.webm", recursive=True)
                if webm_files:
                    print("Conversion in progress ...")
                    for t in webm_files:
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
            filetoconvers = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                webm_files = glob.glob(f"{filetoconvers}/**/*.webm", recursive=True)
                if webm_files:
                    print("Conversion in progress ...")
                    for t in webm_files:
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
            filetoconvers = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                webm_files = glob.glob(f"{filetoconvers}/**/*.webm", recursive=True)
                if webm_files:
                    print("Conversion in progress ...")
                    for t in webm_files:
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
            filetoconvers = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                webm_files = glob.glob(f"{filetoconvers}/**/*.webm", recursive=True)
                if webm_files:
                    print("Conversion in progress ...")
                    for t in webm_files:
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
            filetoconvers = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                webm_files = glob.glob(f"{filetoconvers}/**/*.webm", recursive=True)
                if webm_files:
                    print("Conversion in progress ...")
                    for t in webm_files:
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
            filetoconvers = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                webm_files = glob.glob(f"{filetoconvers}/**/*.webm", recursive=True)
                if webm_files:
                    print("Conversion in progress ...")
                    for t in webm_files:
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
            filetoconvers = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                hevc_files = glob.glob(f"{filetoconvers}/**/*.hevc", recursive=True)
                if hevc_files:
                    print("Conversion in progress ...")
                    for t in hevc_files:
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
            filetoconvers = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                hevc_files = glob.glob(f"{filetoconvers}/**/*.hevc", recursive=True)
                if hevc_files:
                    print("Conversion in progress ...")
                    for t in hevc_files:
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
            filetoconvers = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                hevc_files = glob.glob(f"{filetoconvers}/**/*.hevc", recursive=True)
                if hevc_files:
                    print("Conversion in progress ...")
                    for t in hevc_files:
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
            filetoconvers = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                hevc_files = glob.glob(f"{filetoconvers}/**/*.hevc", recursive=True)
                if hevc_files:
                    print("Conversion in progress ...")
                    for t in hevc_files:
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
            filetoconvers = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                hevc_files = glob.glob(f"{filetoconvers}/**/*.hevc", recursive=True)
                if hevc_files:
                    print("Conversion in progress ...")
                    for t in hevc_files:
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
            filetoconvers = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                hevc_files = glob.glob(f"{filetoconvers}/**/*.hevc", recursive=True)
                if hevc_files:
                    print("Conversion in progress ...")
                    for t in hevc_files:
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
            filetoconvers = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                flv_files = glob.glob(f"{filetoconvers}/**/*.flv", recursive=True)
                if flv_files:
                    print("Conversion in progress ...")
                    for t in flv_files:
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
            filetoconvers = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                flv_files = glob.glob(f"{filetoconvers}/**/*.flv", recursive=True)
                if flv_files:
                    print("Conversion in progress ...")
                    for t in flv_files:
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
            filetoconvers = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                flv_files = glob.glob(f"{filetoconvers}/**/*.flv", recursive=True)
                if flv_files:
                    print("Conversion in progress ...")
                    for t in flv_files:
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
            filetoconvers = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                flv_files = glob.glob(f"{filetoconvers}/**/*.flv", recursive=True)
                if flv_files:
                    print("Conversion in progress ...")
                    for t in flv_files:
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
            filetoconvers = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                flv_files = glob.glob(f"{filetoconvers}/**/*.flv", recursive=True)
                if flv_files:
                    print("Conversion in progress ...")
                    for t in flv_files:
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
            filetoconvers = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                flv_files = glob.glob(f"{filetoconvers}/**/*.flv", recursive=True)
                if flv_files:
                    print("Conversion in progress ...")
                    for t in flv_files:
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
    video=1
    while True:
        if video == 1:  #vtt en srt 
            file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                vtt_files = glob.glob(f"{file}/**/*.vtt", recursive=True)
                if vtt_files:
                    print("Conversion in progress ...")
                    for t in vtt_files:
                        subprocess.run(f"ffmpeg -i {t} -codec copy {t[:-4]}.srt", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
                    encov = "srt"
                    break
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    continue
            else:
                QMessageBox.critical(None, "Error", "No files selected")
                continue
        elif video == 2:  #vtt en ass
            filetoconvers = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                vtt_files = glob.glob(f"{filetoconvers}/**/*.vtt", recursive=True)
                if vtt_files:
                    print("Conversion in progress ...")
                    for t in vtt_files:
                        subprocess.run(f"ffmpeg -i {t} -codec copy {t[:-4]}.ass", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
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
                        subprocess.run(f"ffmpeg -i {t} -codec copy {t[:-4]}.lrc", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
                    encov = "lrc"
                    break
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    continue
            else:
                QMessageBox.critical(None, "Error", "No files selected")
                continue
        elif video == 4:  # srt en vtt
            filetoconvers = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                srt_files = glob.glob(f"{filetoconvers}/**/*.srt", recursive=True)
                if srt_files:
                    print("Conversion in progress ...")
                    for t in mkv_files:
                        subprocess.run(f"ffmpeg -i {t} -c:v libvpx -c:a libvorbis {t[:-4]}.vtt", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
                    encov = "vtt"
                    break
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    continue
            else:
                QMessageBox.critical(None, "Error", "No files selected")
                continue
        elif video == 5:  # srt en ass
            filetoconvers = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                srt_files = glob.glob(f"{filetoconvers}/**/*.srt", recursive=True)
                if srt_files:
                    print("Conversion in progress ...")
                    for t in srt_files:
                        subprocess.run(f"ffmpeg -i {t} -c:v flv -c:a mp3 {t[:-4]}.ass", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
                    encov = "ass"
                    break
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    continue
            else:
                QMessageBox.critical(None, "Error", "No files selected")
                continue
        elif video == 6:  # srt en lrc
            filetoconvers = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                srt_files = glob.glob(f"{filetoconvers}/**/*.srt", recursive=True)
                if srt_files:
                    print("Conversion in progress ...")
                    for t in srt_files:
                        subprocess.run(f"ffmpeg -i {t} -c:v libx265 -c:a aac {t[:-4]}.lrc", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
                    encov = "lrc"
                    break
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    continue
            else:
                QMessageBox.critical(None, "Error", "No files selected")
                continue        
        elif video == 7:    #ass en srt 
            filetoconvers = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                ass_files = glob.glob(f"{filetoconvers}/**/*.ass", recursive=True)
                if ass_files:
                    print("Conversion in progress ...")
                    for t in ass_files:
                        subprocess.run(f"ffmpeg -i {t} -codec copy {t[:-4]}.srt", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
                    encov = "srt"
                    break
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    continue
            else:
                QMessageBox.critical(None, "Error", "No files selected")
                continue
        elif video == 8:    #ass en lrc 
            filetoconvers = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                ass_files = glob.glob(f"{filetoconvers}/**/*.ass", recursive=True)
                if ass_files:
                    print("Conversion in progress ...")
                    for t in ass_files:
                        subprocess.run(f"ffmpeg -i {t} -codec copy {t[:-4]}.lrc", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
                    encov = "lrc"
                    break
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    continue
            else:
                QMessageBox.critical(None, "Error", "No files selected")
                continue
        elif video == 9:    #ass en vtt 
            filetoconvers = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                ass_files = glob.glob(f"{filetoconvers}/**/*.ass", recursive=True)
                if ass_files:
                    print("Conversion in progress ...")
                    for t in ass_files:
                        subprocess.run(f"ffmpeg -i {t} -codec copy {t[:-4]}.vtt", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
                    encov = "vtt"
                    break
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    continue
            else:
                QMessageBox.critical(None, "Error", "No files selected")
                continue
        elif video == 10:    #lrc en srt 
            filetoconvers = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                lrc_files = glob.glob(f"{filetoconvers}/**/*.lrc", recursive=True)
                if lrc_files:
                    print("Conversion in progress ...")
                    for t in lrc_files:
                        subprocess.run(f"ffmpeg -i {t} zz-c:v libvpx -c:a libvorbis {t[:-4]}.srt", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
                    encov = "srt"
                    break
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    continue
            else:
                QMessageBox.critical(None, "Error", "No files selected")
                continue        
        elif video == 11:    #lrc en ass 
            filetoconvers = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                lrc_files = glob.glob(f"{filetoconvers}/**/*.lrc", recursive=True)
                if lrc_files:
                    print("Conversion in progress ...")
                    for t in lrc_files:
                        subprocess.run(f"ffmpeg -i {t} -c:v libvpx -c:a libvorbis {t[:-4]}.ass", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
                    encov = "ass"
                    break
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    continue
            else:
                QMessageBox.critical(None, "Error", "No files selected")
                continue         
        elif video == 12:    #lrc en vtt 
            filetoconvers = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
            if file:
                lrc_files = glob.glob(f"{filetoconvers}/**/*.lrc", recursive=True)
                if lrc_files:
                    print("Conversion in progress ...")
                    for t in lrc_files:
                        subprocess.run(f"ffmpeg -i {t} -c:v libx265 -c:a aac {t[:-4]}.vtt", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
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
app.exit()

asd=int(input("Entrer le bon numero: 1=download, 2=video"))

if asd == 1:
    convertisso_download_video()
elif asd == 2:
    convertissso_video()
else:
    print("erreur")
