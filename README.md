<pre>    
     ██████╗ ██████╗ ███╗   ██╗██╗   ██╗███████╗██████╗ ████████╗██╗███████╗███████╗ ██████╗ 
    ██╔════╝██╔═══██╗████╗  ██║██║   ██║██╔════╝██╔══██╗╚══██╔══╝██║██╔════╝██╔════╝██╔═══██╗
    ██║     ██║   ██║██╔██╗ ██║██║   ██║█████╗  ██████╔╝   ██║   ██║███████╗███████╗██║   ██║
    ██║     ██║   ██║██║╚██╗██║╚██╗ ██╔╝██╔══╝  ██╔══██╗   ██║   ██║╚════██║╚════██║██║   ██║
    ╚██████╗╚██████╔╝██║ ╚████║ ╚████╔╝ ███████╗██║  ██║   ██║   ██║███████║███████║╚██████╔╝
     ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝╚══════╝╚══════╝ ╚═════╝    
                                      Script to convert files
</pre>

<!--  [ Authors ] -->
<p align="center">
    <a href="https://github.com/jonas52">
        <img src="https://img.shields.io/badge/Made%20by-Jonas%20Petitpierre%20(jonas52)-important?style=for-the-badge" alt="Made by">
    </a>
    <a href="https://github.com/PentestSociety">
        <img src="https://img.shields.io/badge/Owner-©%20PSociety™%20(jonas52)-important?style=for-the-badge" alt="Owner">
    </a>
</p>

<!--  [ Informations about this repositorie ] -->
<p align="center">
    <a href="https://github.com/jonas52/convertisso/stargazers">
        <img src="https://img.shields.io/github/stars/jonas52/convertisso?style=for-the-badge&color=success" alt="Stars">
    </a>
    <a href="https://github.com/jonas52/convertisso/watchers">
        <img src="https://img.shields.io/github/watchers/jonas52/convertisso?color=cyan&style=for-the-badge&color=success" alt="Watchers">
    </a>
    <a href="https://github.com/jonas52/convertisso/issues">
        <img src="https://img.shields.io/github/last-commit/jonas52/convertisso?color=cyan&style=for-the-badge&color=success" alt="Last commit">
    </a>

</p>

<!--  [ More informations ] -->
<p align="center">
    <img src="https://img.shields.io/badge/Release%20status-In%20Development-informational?style=for-the-badge" alt="Release status">
    <img src="https://img.shields.io/badge/Supported%20OS-Linux-informational?style=for-the-badge" alt="Supported OS">
    <img src="https://img.shields.io/badge/Supported%20OS-Windows-informational?style=for-the-badge" alt="Supported OS">
    <img src="https://img.shields.io/badge/Supported%20OS-MacOs-informational?style=for-the-badge" alt="Supported OS">
    <img src="https://img.shields.io/github/repo-size/jonas52/convertisso?color=informational&style=for-the-badge" alt="Repo size">
    <a href="https://github.com/jonas52/convertisso/blob/test_v1/LICENSE">
        <img src="https://img.shields.io/github/license/jonas52/convertisso?color=informational&style=for-the-badge" alt="Repo License" >
    </a>
</p>

---

# **Summary**

- [**About Convertisso**](#about-convertisso)
- [**Main GUI of Convertisso**](#main-gui-of-convertisso)
- [**Installation**](#installation-of-convertisso-guipyqt)
- [**Help**](#help)
   - [**Convertisso downloader**](#convertisso-downloader)
   - [**Convertisso convert**](#convertisso-convert)
- [**Credit & Copyrights**](credit-&-copyrights)
- [**Licence**](#licence)
- [**Other**](#other)

--- 


# **About Convertisso**
### The script is currently in Python and is available for all systeme.
### This script can:
- Download your favorite video from any website, with or without title, download only the audio or only the subtitles. (attention only works if you have python3 3.7 and higher)
- Convert your subtitle files (vtt, srt, ass, lrc). 
- Convert your video files (mkv, mp4, mov, avi, webm, hevc, flv). 
- Convert your audio files (mp3, wav, ogg, ac3, aac, flac, opus, m4a).
- Convert your photo files (png, jpg, tiff, pdf, svg, pdf, gif, heic). -> coming soon
# **Main GUI of Convertisso**
| Main-Downloader-Convertisso | Main-Audio-Convertisso |
|---------|---------|
| ![Main-Downloader-Convertisso](https://user-images.githubusercontent.com/83141023/232312519-001d4c3e-92d3-45e6-949b-aecc5ef8a18c.png) | ![Main-audio-Convertisso](https://user-images.githubusercontent.com/83141023/232312518-384f1293-1879-4d16-a17e-810261286b6a.png) 

| Main-Video-Convertisso | Main-Subtitle-Convertisso |
|---------|---------|
| ![Main-Video-Convertisso](https://user-images.githubusercontent.com/83141023/232312685-b643b8bc-4e2a-4b3b-9530-eaebcee60ae6.png) | ![Main-Subtitle-Convertisso](https://user-images.githubusercontent.com/83141023/232312739-60f9acdc-27c9-4657-9feb-e33b3ba6ce6c.png)

# **Installation of Convertisso GUI(PyQt)**
## Install all dependencies:
### Install Python on your device please check: _[Python website](https://www.python.org/downloads/)_
## Open terminal and type this
>     pip install yt_dlp ffmpeg-python requests PyQt5
#### And install FFmpeg in your systeme:
```
sudo apt install ffmpeg
```
```
sudo pacman -S ffmpeg
```
##### If your are on Windows, MacOs or others distribution please check: _[FFmpeg download website](https://ffmpeg.org/download.html)_
## Open terminal and type this
### Download and lauch whit :
>     git clone https://github.com/jonas52/convertisso.git && cd convertisso && python3 convertisso-GUI.py
- And it's all good conversions and/or video downloads
- To exit the program alt F4 or the cross of the right top.

# **Help**
### Convertisso downloader
1. Please copy and paste the URL of your video.
2. Enter the name that the file will have once uploaded.
3. Choose by clicking on an option in the drop-down menu.
4. Enter where your file will be saved once uploaded.
5. Press download to start the download, once the bonton press you will see the green led of download in progress.
### Convertisso convert
1. Choose by clicking on an option in the drop-down menu.
2. Enter where your file will be saved once converted.
3. Press convert to start the convert, once the bonton press you will see the green led of convert in progress.
#### If you need more help please contact me : petitpierre@duck.com
# **Other**
> #### For problems or ideas for additions related to my code do not hesitate to contact me: petitpierre@duck.com
> #### The Convertisso is a product of © PSociety by jonas52! Copyright (C) 2022-2023 © PSociety. All rights reserved.
## **Credit & Copyrights**

```
             The Convertisso is a product of PSociety by Jonas Petitpierre (jonas52).
                   Copyright (C) 2021-2023 © PSociety. All rights reserved.

           This programme has been created and designed from scratch by Jonas Petitpierre.
```
# **Licence**
- This program uses the license _[General Public License v3.0](https://github.com/jonas52/convertisso/blob/main/LICENSE)_.
