#pip install youtube-dl
import os
import subprocess
import shutil
import glob
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

convertisso_download_video()