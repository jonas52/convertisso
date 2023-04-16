import os
from urllib import request
import subprocess
script_path = "python3 convertisso-GUI.py"
Arch = '/etc/pacman.conf'
Debian = '/etc/apt/sources.list'
# Fedora = '/etc/dnf/dnf.conf'

def internet_check(host='https://google.com'):
    '''
    Check if the user have an Internet connection by connecting to google.com over https
    '''
    try:
        request.urlopen(host, timeout=4)
        return True
    except:
        return False

if internet_check() == True:
    if os.path.isfile(Debian):
        print("Installing upgrade")
        os.system('sudo apt-get update -y && sudo apt upgrade -y > /dev/null 2>&1')
        print("Installing pip")
        os.system('sudo apt-get install python3-pip > /dev/null 2>&1')
        print("Installing ffmpeg and ffprobe")
        os.system("sudo apt-get install ffmpeg > /dev/null 2>&1")
        os.system("sudo apt-get install ffprobe > /dev/null 2>&1")
        os.system("pip install ffmpeg > /dev/null 2>&1")
        print("Installing yt_dlp")
        os.system("pip install yt_dlp > /dev/null 2>&1")
        print("Installing PyQt5")
        os.system("pip install PyQt5 > /dev/null 2>&1")
        subprocess.run([script_path], shell=True)
    elif os.path.isfile(Arch):
        print("Installing upgrade")
        os.system('sudo pacman -Syu --noconfirm > /dev/null 2>&1')
        print("Installing pip")
        os.system('sudo pacman -S python3-pip > /dev/null 2>&1')
        print("Installing ffmpeg and ffprobe")
        os.system("sudo pacman -S ffmpeg > /dev/null 2>&1")
        os.system("sudo pacman -S ffprobe > /dev/null 2>&1")
        os.system("pip install ffmpeg > /dev/null 2>&1")
        print("Installing yt_dlp")
        os.system("pip install yt_dlp > /dev/null 2>&1")
        print("Installing PyQt5")
        os.system("pip install PyQt5 > /dev/null 2>&1")
        subprocess.run([script_path], shell=True)
    else:
        print("Error", "Your device is not compatible with this programme")
else:
    print("Error", "No internet connextion please check your connection")

