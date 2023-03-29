#pip install yt-dlp
#pip install AudioSegment    
#pip install pydub
#pip install pyqt5
import os
import subprocess
import shutil
import glob
import ffmpeg
import yt_dlp
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QComboBox, QFileDialog
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
class YoutubeDownloader(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Youtube Downloader')
        self.setGeometry(100, 100, 700, 400)

        self.link_label = QLabel(self)
        self.link_label.setText('Enter video link:')        
        self.link_label.move(50, 50)
        
        self.link_input = QLineEdit(self)
        self.link_input.move(250, 50)
        self.link_input.resize(300, 30)
        self.link_input.text()

        self.name_label = QLabel(self)
        self.name_label.setText('Enter the name of the file:')
        self.name_label.move(50, 100)

        self.name_input = QLineEdit(self)
        self.name_input.move(250, 100)
        self.name_input.resize(300, 30)
        self.name_input.text()

        self.destination_label = QLabel(self)
        self.destination_label.setText('Enter destination folder:')
        self.destination_label.move(50, 300)

        self.destination_input = QLineEdit(self)
        self.destination_input.move(250, 300)
        self.destination_input.resize(300, 30)
        self.destination_input.text()

        self.choose_destination_button = QPushButton('Choose Folder', self)
        self.choose_destination_button.move(550, 300)
        self.choose_destination_button.clicked.connect(self.choose_folder)

        self.download_label = QLabel(self)
        self.download_label.setText('Choose download option:')
        self.download_label.move(50, 150)

        self.download_choice = QComboBox(self)
        self.download_choice.addItem('Video Only')
        self.download_choice.addItem('Video + Subtitles')
        self.download_choice.addItem('Audio Only')
        self.download_choice.addItem('Subtitles Only')
        self.download_choice.move(250, 200)
        self.download_choice.resize(200, 30)
        self.download_choice.currentIndexChanged.connect(self.setDownloadOption)

        self.download_button = QPushButton('Download', self)
        self.download_button.move(300, 350)
        self.download_button.clicked.connect(self.download_video)

    def choose_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self, 'Select Folder')
        self.destination_input.setText(folder_path)

    def setDownloadOption(self, index):
        self.download_option = self.download_choice.itemText(index)

    def download_video(self):
        if self.download_option == 'Video Only':
                        ydl_opts = {
                            'format': 'bv+ba',
                            'addmetadata': True,
                            'outtmpl': self.name_input.text()
                        }
                        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                            ydl.download([self.link_input.text()])
                        for extension in ["*.mp4", "*.mkv", "*.webm", "*.flv"]:
                            for filename in glob.glob(extension):
                                shutil.move(filename, self.destination_input.text())
        if self.download_option == 'Video + Subtitles':
                        ydl_opts = {
                            'format': 'bv+ba',
                            'addmetadata': True,
                            'outtmpl': self.destination_input.text() + '/%(title)s.%(ext)s',
                            'allsubtitles': True,
                            'writeautomaticsub': True
                        }
                        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                            ydl.download([self.link_input.text()])                        
                        for extension in ["*.mp4", "*.mkv", "*.webm", "*.flv", "*.srt", "*.ass", "*.vtt", "*.lrc"]:
                            for filename in glob.glob(extension):
                                shutil.move(filename, self.destination_input.text())
        if self.download_option == 'Audio Only':
                        ydl_opts = {
                            'format': 'bestaudio',
                            'addmetadata': True,
                            'postprocessors': [{
                            'key': 'FFmpegExtractAudio',
                            'preferredcodec': 'mp3',
                            'preferredquality': '320',
                            }],
                            'outtmpl': self.name_input.text()
                        }                       
                        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                            ydl.download([self.link_input.text()])
                        for extension in ["*.mp3", "*.aac", "*.flac", "*.m4a", "*.ogg", "*.wav", "*.opus", "*.vorbis"]:
                            for filename in glob.glob(extension):
                                shutil.move(filename, self.destination_input.text())
        if self.download_option == 'Subtitles Only':
                        ydl_opts = {
                            'skip_download': True,
                            'addmetadata': True,
                            'outtmpl': self.destination_input.text() + '/%(title)s.%(ext)s',
                            'allsubtitles': True,
                            'writeautomaticsub': True
                        }          
                        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                            info_dict = ydl.extract_info(self.link_input.text(), download=False)
                            filename = ydl.prepare_filename(info_dict)
                            ydl.process_info(info_dict)
                        for extension in ["*.srt", "*.ass", "*.vtt", "*.lrc"]:
                            for filename in glob.glob(extension):
                                shutil.move(filename, self.destination_input.text())
        else:
                        print("Please enter a number between 1 and 4")


# def convertisso_subtitle():

#     while True:
#         if i==1:
#             print("hello world")

class convertissso_video_GUI(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Convertisso video')
        self.setGeometry(100, 100, 700, 400)

        self.path_label = QLabel(self)
        self.path_label.setText('Chose directory (its store your(s) file(s) to convert):')
        self.path_label.move(50, 50)

        self.path_input = QLineEdit(self)
        self.path_input.move(250, 300)
        self.path_input.resize(300, 30)
        self.path_input.text()

        self.choose_path_button = QPushButton('Select one directory (not recursive)', self)
        self.choose_path_button.move(550, 300)
        self.choose_path_button.clicked.connect(self.choose_folder)

        self.convertvideo_label = QLabel(self)
        self.convertvideo_label.setText('Choose convert option:')
        self.convertvideo_label.move(50, 150)

        self.convertvideo_choice = QComboBox(self)
        self.convertvideo_choice.addItem('Video Only')
        self.convertvideo_choice.addItem('Video + Subtitles')
        self.convertvideo_choice.addItem('Audio Only')
        self.convertvideo_choice.addItem('Subtitles Only')
        self.convertvideo_choice.move(250, 200)
        self.convertvideo_choice.resize(200, 30)
        self.convertvideo_choice.currentIndexChanged.connect(self.setconvertvideoOption)

        self.convertvideo_button = QPushButton('Convert', self)
        self.convertvideo_button.move(300, 350)
        self.convertvideo_button.clicked.connect(self.convertvideo_video)

    def choose_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self, 'Select one directory (not recursive)')
        self.destination_input.setText(folder_path)

    def setDownloadOption(self, index):
        self.download_option = self.download_choice.itemText(index)

video=7
while True:
    if self.convertsubtitle_option == 1:  # mkv en avi ----------------------------------------------------------------------------------------Problème convertion impossible a revoir
        file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
        if file:
            mkv_files = glob.glob(f"{file}/**/*.mkv", recursive=True)
            if mkv_files:
                print("Conversion in progress ...")
                for t in mkv_files:
                    out_filename = os.path.splitext(t)[0] + '.avi'
                    stream = ffmpeg.input(t)
                    stream = ffmpeg.output(stream, out_filename, vcodec='copy', acodec='copy',  map_metadata=0)
                    ffmpeg.run(stream, quiet=True)
                encov = "avi"
                break
            else:
                QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                continue
        else:
            QMessageBox.critical(None, "Error", "No files selected")
            continue
    elif self.convertsubtitle_option == 2:  # mkv en mov
        file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
        if file:
            mkv_files = glob.glob(f"{file}/**/*.mkv", recursive=True)
            if mkv_files:
                print("Conversion in progress ...")
                for t in mkv_files:
                    out_filename = os.path.splitext(t)[0] + '.mov'
                    stream = ffmpeg.input(t)
                    stream = ffmpeg.output(stream, out_filename, vcodec='copy', acodec='copy', map_metadata=0)
                    ffmpeg.run(stream, quiet=True)
                encov = "mov"
                break
            else:
                QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                continue
        else:
            QMessageBox.critical(None, "Error", "No files selected")
            continue
    if self.convertsubtitle_option == 3:  # mkv en mp4
        file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
        if file:
            mkv_files = glob.glob(f"{file}/**/*.mkv", recursive=True)
            if mkv_files:
                print("Conversion in progress ...")
                for t in mkv_files:
                    out_filename = os.path.splitext(t)[0] + '.mp4'
                    stream = ffmpeg.input(t)
                    stream = ffmpeg.output(stream, out_filename, vcodec='copy', acodec='copy', map_metadata=0)
                    ffmpeg.run(stream, quiet=True)
                encov = "mp4"
                break
            else:
                QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                continue
        else:
            QMessageBox.critical(None, "Error", "No files selected")
            continue
    elif self.convertsubtitle_option == 4:  # mkv en webm
        file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
        if file:
            mkv_files = glob.glob(f"{file}/**/*.mkv", recursive=True)
            if mkv_files:
                print("Conversion in progress ...")
                for t in mkv_files:
                    out_filename = os.path.splitext(t)[0] + '.webm'
                    stream = ffmpeg.input(t)
                    stream = ffmpeg.output(stream, out_filename, vcodec='copy', acodec='copy', map_metadata=0)
                    ffmpeg.run(stream, quiet=True)
                encov = "webm"
                break
            else:
                QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                continue
        else:
            QMessageBox.critical(None, "Error", "No files selected")
            continue
    elif self.convertsubtitle_option == 5:  # mkv en flv
        file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
        if file:
            mkv_files = glob.glob(f"{file}/**/*.mkv", recursive=True)
            if mkv_files:
                print("Conversion in progress ...")
                for t in mkv_files:
                    out_filename = os.path.splitext(t)[0] + '.flv'
                    stream = ffmpeg.input(t)
                    stream = ffmpeg.output(stream, out_filename, vcodec='copy', acodec='copy', map_metadata=0)
                    ffmpeg.run(stream, quiet=True)
                encov = "flv"
                break
            else:
                QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                continue
        else:
            QMessageBox.critical(None, "Error", "No files selected")
            continue
    elif self.convertsubtitle_option == 6:  # mkv en hevc
        file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
        if file:
            mkv_files = glob.glob(f"{file}/**/*.mkv", recursive=True)
            if mkv_files:
                print("Conversion in progress ...")
                for t in mkv_files:
                    out_filename = os.path.splitext(t)[0] + '.hevc'
                    stream = ffmpeg.input(t)
                    stream = ffmpeg.output(stream, out_filename,  vcodec='copy', acodec='copy', map_metadata=0)
                    ffmpeg.run(stream, quiet=True)
                encov = "hevc"
                break
            else:
                QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                continue
        else:
            QMessageBox.critical(None, "Error", "No files selected")
            continue        
    elif self.convertsubtitle_option == 7:    #mp4 en mkv 
        file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
        if file:
            mp4_files = glob.glob(f"{file}/**/*.mp4", recursive=True)
            if mp4_files:
                print("Conversion in progress ...")
                for t in mp4_files:
                    out_filename = os.path.splitext(t)[0] + '.mkv'
                    stream = ffmpeg.input(t)
                    stream = ffmpeg.output(stream, out_filename, vcodec='copy', acodec='copy', map_metadata=0)
                    ffmpeg.run(stream, quiet=True)
                encov = "mkv"
                break
            else:
                QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                continue
        else:
            QMessageBox.critical(None, "Error", "No files selected")
            continue
    elif self.convertsubtitle_option == 8:    #mp4 en mov 
        file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
        if file:
            mp4_files = glob.glob(f"{file}/**/*.mp4", recursive=True)
            if mp4_files:
                print("Conversion in progress ...")
                for t in mp4_files:
                    out_filename = os.path.splitext(t)[0] + '.mov'
                    stream = ffmpeg.input(t)
                    stream = ffmpeg.output(stream, out_filename,  vcodec='copy', acodec='copy', map_metadata=0)
                    ffmpeg.run(stream, quiet=True)
                encov = "mov"
                break
            else:
                QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                continue
        else:
            QMessageBox.critical(None, "Error", "No files selected")
            continue
    elif self.convertsubtitle_option == 9:    #mp4 en avi 
        file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
        if file:
            mp4_files = glob.glob(f"{file}/**/*.mp4", recursive=True)
            if mp4_files:
                print("Conversion in progress ...")
                for t in mp4_files:
                    out_filename = os.path.splitext(t)[0] + '.avi'
                    stream = ffmpeg.input(t)
                    stream = ffmpeg.output(stream, out_filename,  vcodec='copy', acodec='copy', map_metadata=0)
                    ffmpeg.run(stream, quiet=True)
                encov = "avi"
                break
            else:
                QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                continue
        else:
            QMessageBox.critical(None, "Error", "No files selected")
            continue
    elif self.convertsubtitle_option == 10:    #mp4 en webm 
        file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
        if file:
            mp4_files = glob.glob(f"{file}/**/*.mp4", recursive=True)
            if mp4_files:
                print("Conversion in progress ...")
                for t in mp4_files:
                    out_filename = os.path.splitext(t)[0] + '.webm'
                    stream = ffmpeg.input(t)
                    stream = ffmpeg.output(stream, out_filename,  vcodec='copy', acodec='copy', map_metadata=0)
                    ffmpeg.run(stream, quiet=True)
                encov = "webm"
                break
            else:
                QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                continue
        else:
            QMessageBox.critical(None, "Error", "No files selected")
            continue        
    elif self.convertsubtitle_option == 11:    #mp4 en flv 
        file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
        if file:
            mp4_files = glob.glob(f"{file}/**/*.mp4", recursive=True)
            if mp4_files:
                print("Conversion in progress ...")
                for t in mp4_files:
                    out_filename = os.path.splitext(t)[0] + '.flv'
                    stream = ffmpeg.input(t)
                    stream = ffmpeg.output(stream, out_filename,  vcodec='copy', acodec='copy', map_metadata=0)
                    ffmpeg.run(stream, quiet=True)
                encov = "flv"
                break
            else:
                QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                continue
        else:
            QMessageBox.critical(None, "Error", "No files selected")
            continue         
    elif self.convertsubtitle_option == 12:    #mp4 en hevc 
        file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
        if file:
            mp4_files = glob.glob(f"{file}/**/*.mp4", recursive=True)
            if mp4_files:
                print("Conversion in progress ...")
                for t in mp4_files:
                    out_filename = os.path.splitext(t)[0] + '.hevc'
                    stream = ffmpeg.input(t)
                    stream = ffmpeg.output(stream, out_filename,  vcodec='copy', acodec='copy', map_metadata=0)
                    ffmpeg.run(stream, quiet=True)
                encov = "hevc"
                break
            else:
                QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                continue
        else:
            QMessageBox.critical(None, "Error", "No files selected")
            continue         
    elif self.convertsubtitle_option == 13:    #mov en mkv 
        file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
        if file:
            mov_files = glob.glob(f"{file}/**/*.mov", recursive=True)
            if mov_files:
                print("Conversion in progress ...")
                for t in mov_files:
                    out_filename = os.path.splitext(t)[0] + '.mkv'
                    stream = ffmpeg.input(t)
                    stream = ffmpeg.output(stream, out_filename,  vcodec='copy', acodec='copy', map_metadata=0)
                    ffmpeg.run(stream, quiet=True)
                encov = "mkv"
                break
            else:
                QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                continue
        else:
            QMessageBox.critical(None, "Error", "No files selected")
            continue
    elif self.convertsubtitle_option == 14:    #mov en mp4 
        file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
        if file:
            mov_files = glob.glob(f"{file}/**/*.mov", recursive=True)
            if mov_files:
                print("Conversion in progress ...")
                for t in mov_files:
                    out_filename = os.path.splitext(t)[0] + '.mp4'
                    stream = ffmpeg.input(t)
                    stream = ffmpeg.output(stream, out_filename,  vcodec='copy', acodec='copy', map_metadata=0)
                    ffmpeg.run(stream, quiet=True)
                encov = "mp4"
                break
            else:
                QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                continue
        else:
            QMessageBox.critical(None, "Error", "No files selected")
            continue
    elif self.convertsubtitle_option == 15:    #mov en avi 
        file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
        if file:
            mov_files = glob.glob(f"{file}/**/*.mov", recursive=True)
            if mov_files:
                print("Conversion in progress ...")
                for t in mov_files:
                    out_filename = os.path.splitext(t)[0] + '.avi'
                    stream = ffmpeg.input(t)
                    stream = ffmpeg.output(stream, out_filename,  vcodec='copy', acodec='copy', map_metadata=0)
                    ffmpeg.run(stream, quiet=True)
                encov = "avi"
                break
            else:
                QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                continue
        else:
            QMessageBox.critical(None, "Error", "No files selected")
            continue
    elif self.convertsubtitle_option == 16:    #mov en webm 
        file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
        if file:
            mov_files = glob.glob(f"{file}/**/*.mov", recursive=True)
            if mov_files:
                print("Conversion in progress ...")
                for t in mov_files:
                    out_filename = os.path.splitext(t)[0] + '.webm'
                    stream = ffmpeg.input(t)
                    stream = ffmpeg.output(stream, out_filename,  vcodec='copy', acodec='copy', map_metadata=0)
                    ffmpeg.run(stream, quiet=True)
                encov = "webm"
                break
            else:
                QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                continue
        else:
            QMessageBox.critical(None, "Error", "No files selected")
            continue        
    elif self.convertsubtitle_option == 17:    #mov en flv 
        file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
        if file:
            mov_files = glob.glob(f"{file}/**/*.mov", recursive=True)
            if mov_files:
                print("Conversion in progress ...")
                for t in mov_files:
                    out_filename = os.path.splitext(t)[0] + '.flv'
                    stream = ffmpeg.input(t)
                    stream = ffmpeg.output(stream, out_filename,  vcodec='copy', acodec='copy', map_metadata=0)
                    ffmpeg.run(stream, quiet=True)
                encov = "flv"
                break
            else:
                QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                continue
        else:
            QMessageBox.critical(None, "Error", "No files selected")
            continue         
    elif self.convertsubtitle_option == 18:    #mov en hevc 
        file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
        if file:
            mov_files = glob.glob(f"{file}/**/*.mov", recursive=True)
            if mov_files:
                print("Conversion in progress ...")
                for t in mov_files:
                    out_filename = os.path.splitext(t)[0] + '.hevc'
                    stream = ffmpeg.input(t)
                    stream = ffmpeg.output(stream, out_filename,  vcodec='copy', acodec='copy', map_metadata=0)
                    ffmpeg.run(stream, quiet=True)
                encov = "hevc"
                break
            else:
                QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                continue
        else:
            QMessageBox.critical(None, "Error", "No files selected")
            continue
    elif self.convertsubtitle_option == 19:    #avi en mkv 
        file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
        if file:
            avi_files = glob.glob(f"{file}/**/*.avi", recursive=True)
            if avi_files:
                print("Conversion in progress ...")
                for t in avi_files:
                    out_filename = os.path.splitext(t)[0] + '.mkv'
                    stream = ffmpeg.input(t)
                    stream = ffmpeg.output(stream, out_filename,  vcodec='copy', acodec='copy', map_metadata=0)
                    ffmpeg.run(stream, quiet=True)
                encov = "mkv"
                break
            else:
                QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                continue
        else:
            QMessageBox.critical(None, "Error", "No files selected")
            continue
    elif self.convertsubtitle_option == 20:    #avi en mp4 
        file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
        if file:
            avi_files = glob.glob(f"{file}/**/*.avi", recursive=True)
            if avi_files:
                print("Conversion in progress ...")
                for t in avi_files:
                    out_filename = os.path.splitext(t)[0] + '.mp4'
                    stream = ffmpeg.input(t)
                    stream = ffmpeg.output(stream, out_filename,  vcodec='copy', acodec='copy', map_metadata=0)
                    ffmpeg.run(stream, quiet=True)
                encov = "avi"
                break
            else:
                QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                continue
        else:
            QMessageBox.critical(None, "Error", "No files selected")
            continue
    elif self.convertsubtitle_option == 21:    #avi en mov 
        file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
        if file:
            avi_files = glob.glob(f"{file}/**/*.avi", recursive=True)
            if avi_files:
                print("Conversion in progress ...")
                for t in avi_files:
                    out_filename = os.path.splitext(t)[0] + '.mov'
                    stream = ffmpeg.input(t)
                    stream = ffmpeg.output(stream, out_filename,  vcodec='copy', acodec='copy', map_metadata=0)
                    ffmpeg.run(stream, quiet=True)
                encov = "mov"
                break
            else:
                QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                continue
        else:
            QMessageBox.critical(None, "Error", "No files selected")
            continue
    elif self.convertsubtitle_option == 22:    #avi en webm 
        file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
        if file:
            avi_files = glob.glob(f"{file}/**/*.avi", recursive=True)
            if avi_files:
                print("Conversion in progress ...")
                for t in avi_files:
                    out_filename = os.path.splitext(t)[0] + '.webm'
                    stream = ffmpeg.input(t)
                    stream = ffmpeg.output(stream, out_filename,  vcodec='copy', acodec='copy', map_metadata=0)
                    ffmpeg.run(stream, quiet=True)
                encov = "webm"
                break
            else:
                QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                continue
        else:
            QMessageBox.critical(None, "Error", "No files selected")
            continue        
    elif self.convertsubtitle_option == 23:    #avi en flv 
        file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
        if file:
            avi_files = glob.glob(f"{file}/**/*.avi", recursive=True)
            if avi_files:
                print("Conversion in progress ...")
                for t in avi_files:
                    out_filename = os.path.splitext(t)[0] + '.flv'
                    stream = ffmpeg.input(t)
                    stream = ffmpeg.output(stream, out_filename,  vcodec='copy', acodec='copy', map_metadata=0)
                    ffmpeg.run(stream, quiet=True)
                encov = "flv"
                break
            else:
                QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                continue
        else:
            QMessageBox.critical(None, "Error", "No files selected")
            continue         
    elif self.convertsubtitle_option == 24:    #avi en hevc 
        file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
        if file:
            avi_files = glob.glob(f"{file}/**/*.avi", recursive=True)
            if avi_files:
                print("Conversion in progress ...")
                for t in avi_files:
                    out_filename = os.path.splitext(t)[0] + '.hevc'
                    stream = ffmpeg.input(t)
                    stream = ffmpeg.output(stream, out_filename, vcodec='libx265', acodec='aac', map_metadata=0)
                    ffmpeg.run(stream, quiet=True)
                encov = "hevc"
                break
            else:
                QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                continue
        else:
            QMessageBox.critical(None, "Error", "No files selected")
            continue
    elif self.convertsubtitle_option == 25:    #webm en avi 
        file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
        if file:
            webm_files = glob.glob(f"{file}/**/*.webm", recursive=True)
            if webm_files:
                print("Conversion in progress ...")
                for t in webm_files:
                    out_filename = os.path.splitext(t)[0] + '.avi'
                    stream = ffmpeg.input(t)
                    stream = ffmpeg.output(stream, out_filename,  vcodec='copy', acodec='copy', map_metadata=0)
                    ffmpeg.run(stream, quiet=True)
                encov = "avi"
                break
            else:
                QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                continue
        else:
            QMessageBox.critical(None, "Error", "No files selected")
            continue
    elif self.convertsubtitle_option == 26:    #webm en mkv 
        file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
        if file:
            webm_files = glob.glob(f"{file}/**/*.webm", recursive=True)
            if webm_files:
                print("Conversion in progress ...")
                for t in webm_files:
                    out_filename = os.path.splitext(t)[0] + '.mkv'
                    stream = ffmpeg.input(t)
                    stream = ffmpeg.output(stream, out_filename,  vcodec='copy', acodec='copy', map_metadata=0)
                    ffmpeg.run(stream, quiet=True)
                encov = "mkv"
                break
            else:
                QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                continue
        else:
            QMessageBox.critical(None, "Error", "No files selected")
            continue
    elif self.convertsubtitle_option == 27:    #webm en mov 
        file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
        if file:
            webm_files = glob.glob(f"{file}/**/*.webm", recursive=True)
            if webm_files:
                print("Conversion in progress ...")
                for t in webm_files:
                    out_filename = os.path.splitext(t)[0] + '.mov'
                    stream = ffmpeg.input(t)
                    stream = ffmpeg.output(stream, out_filename,  vcodec='copy', acodec='copy', map_metadata=0)
                    ffmpeg.run(stream, quiet=True)
                encov = "mov"
                break
            else:
                QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                continue
        else:
            QMessageBox.critical(None, "Error", "No files selected")
            continue
    elif self.convertsubtitle_option == 28:    #webm en mp4 
        file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
        if file:
            webm_files = glob.glob(f"{file}/**/*.webm", recursive=True)
            if webm_files:
                print("Conversion in progress ...")
                for t in webm_files:
                    out_filename = os.path.splitext(t)[0] + '.mp4'
                    stream = ffmpeg.input(t)
                    stream = ffmpeg.output(stream, out_filename,  vcodec='copy', acodec='copy', map_metadata=0)
                    ffmpeg.run(stream, quiet=True)
                encov = "mp4"
                break
            else:
                QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                continue
        else:
            QMessageBox.critical(None, "Error", "No files selected")
            continue        
    elif self.convertsubtitle_option == 29:    #webm en flv 
        file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
        if file:
            webm_files = glob.glob(f"{file}/**/*.webm", recursive=True)
            if webm_files:
                print("Conversion in progress ...")
                for t in webm_files:
                    out_filename = os.path.splitext(t)[0] + '.flv'
                    stream = ffmpeg.input(t)
                    stream = ffmpeg.output(stream, out_filename,  vcodec='copy', acodec='copy', map_metadata=0)
                    ffmpeg.run(stream, quiet=True)
                encov = "flv"
                break
            else:
                QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                continue
        else:
            QMessageBox.critical(None, "Error", "No files selected")
            continue         
    elif self.convertsubtitle_option == 30:    #webm en hevc 
        file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
        if file:
            webm_files = glob.glob(f"{file}/**/*.webm", recursive=True)
            if webm_files:
                print("Conversion in progress ...")
                for t in webm_files:
                    out_filename = os.path.splitext(t)[0] + '.hevc'
                    stream = ffmpeg.input(t)
                    stream = ffmpeg.output(stream, out_filename,  vcodec='copy', acodec='copy', map_metadata=0)
                    ffmpeg.run(stream, quiet=True)
                encov = "hevc"
                break
            else:
                QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                continue
        else:
            QMessageBox.critical(None, "Error", "No files selected")
            continue
    elif self.convertsubtitle_option == 31:    #hevc en avi 
        file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
        if file:
            hevc_files = glob.glob(f"{file}/**/*.hevc", recursive=True)
            if hevc_files:
                print("Conversion in progress ...")
                for t in hevc_files:
                    out_filename = os.path.splitext(t)[0] + '.avi'
                    stream = ffmpeg.input(t)
                    stream = ffmpeg.output(stream, out_filename,  vcodec='copy', acodec='copy', map_metadata=0)
                    ffmpeg.run(stream, quiet=True)
                encov = "avi"
                break
            else:
                QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                continue
        else:
            QMessageBox.critical(None, "Error", "No files selected")
            continue
    elif self.convertsubtitle_option == 32:    #hevc en mkv 
        file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
        if file:
            hevc_files = glob.glob(f"{file}/**/*.hevc", recursive=True)
            if hevc_files:
                print("Conversion in progress ...")
                for t in hevc_files:
                    out_filename = os.path.splitext(t)[0] + '.mkv'
                    stream = ffmpeg.input(t)
                    stream = ffmpeg.output(stream, out_filename,  vcodec='copy', acodec='copy', map_metadata=0)
                    ffmpeg.run(stream, quiet=True)
                encov = "mkv"
                break
            else:
                QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                continue
        else:
            QMessageBox.critical(None, "Error", "No files selected")
            continue
    elif self.convertsubtitle_option == 33:    #hevc en mov 
        file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
        if file:
            hevc_files = glob.glob(f"{file}/**/*.hevc", recursive=True)
            if hevc_files:
                print("Conversion in progress ...")
                for t in hevc_files:
                    out_filename = os.path.splitext(t)[0] + '.mov'
                    stream = ffmpeg.input(t)
                    stream = ffmpeg.output(stream, out_filename,  vcodec='copy', acodec='copy', map_metadata=0)
                    ffmpeg.run(stream, quiet=True)
                encov = "mov"
                break
            else:
                QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                continue
        else:
            QMessageBox.critical(None, "Error", "No files selected")
            continue
    elif self.convertsubtitle_option == 34:    #hevc en mp4 
        file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
        if file:
            hevc_files = glob.glob(f"{file}/**/*.hevc", recursive=True)
            if hevc_files:
                print("Conversion in progress ...")
                for t in hevc_files:
                    out_filename = os.path.splitext(t)[0] + '.mp4'
                    stream = ffmpeg.input(t)
                    stream = ffmpeg.output(stream, out_filename,  vcodec='copy', acodec='copy', map_metadata=0)
                    ffmpeg.run(stream, quiet=True)
                encov = "mp4"
                break
            else:
                QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                continue
        else:
            QMessageBox.critical(None, "Error", "No files selected")
            continue        
    elif self.convertsubtitle_option == 35:    #hevc en flv 
        file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
        if file:
            hevc_files = glob.glob(f"{file}/**/*.hevc", recursive=True)
            if hevc_files:
                print("Conversion in progress ...")
                for t in hevc_files:
                    out_filename = os.path.splitext(t)[0] + '.flv'
                    stream = ffmpeg.input(t)
                    stream = ffmpeg.output(stream, out_filename,  vcodec='copy', acodec='copy', map_metadata=0)
                    ffmpeg.run(stream, quiet=True)
                encov = "flv"
                break
            else:
                QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                continue
        else:
            QMessageBox.critical(None, "Error", "No files selected")
            continue         
    elif self.convertsubtitle_option == 36:    #hevc en webm 
        file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
        if file:
            hevc_files = glob.glob(f"{file}/**/*.hevc", recursive=True)
            if hevc_files:
                print("Conversion in progress ...")
                for t in hevc_files:
                    out_filename = os.path.splitext(t)[0] + '.webm'
                    stream = ffmpeg.input(t)
                    stream = ffmpeg.output(stream, out_filename,  vcodec='copy', acodec='copy', map_metadata=0)
                    ffmpeg.run(stream, quiet=True)
                encov = "webm"
                break
            else:
                QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                continue
        else:
            QMessageBox.critical(None, "Error", "No files selected")
            continue
    elif self.convertsubtitle_option == 37:    #flv en avi 
        file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
        if file:
            flv_files = glob.glob(f"{file}/**/*.flv", recursive=True)
            if flv_files:
                print("Conversion in progress ...")
                for t in flv_files:
                    out_filename = os.path.splitext(t)[0] + '.avi'
                    stream = ffmpeg.input(t)
                    stream = ffmpeg.output(stream, out_filename,  vcodec='copy', acodec='copy', map_metadata=0)
                    ffmpeg.run(stream, quiet=True)
                encov = "avi"
                break
            else:
                QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                continue
        else:
            QMessageBox.critical(None, "Error", "No files selected")
            continue
    elif self.convertsubtitle_option == 38:    #flv en mkv 
        file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
        if file:
            flv_files = glob.glob(f"{file}/**/*.flv", recursive=True)
            if flv_files:
                print("Conversion in progress ...")
                for t in flv_files:
                    out_filename = os.path.splitext(t)[0] + '.mkv'
                    stream = ffmpeg.input(t)
                    stream = ffmpeg.output(stream, out_filename,  vcodec='copy', acodec='copy', map_metadata=0)
                    ffmpeg.run(stream, quiet=True)
                encov = "mkv"
                break
            else:
                QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                continue
        else:
            QMessageBox.critical(None, "Error", "No files selected")
            continue
    elif self.convertsubtitle_option == 39:    #flv en mov 
        file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
        if file:
            flv_files = glob.glob(f"{file}/**/*.flv", recursive=True)
            if flv_files:
                print("Conversion in progress ...")
                for t in flv_files:
                    out_filename = os.path.splitext(t)[0] + '.mov'
                    stream = ffmpeg.input(t)
                    stream = ffmpeg.output(stream, out_filename,  vcodec='copy', acodec='copy', map_metadata=0)
                    ffmpeg.run(stream, quiet=True)
                encov = "mov"
                break
            else:
                QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                continue
        else:
            QMessageBox.critical(None, "Error", "No files selected")
            continue
    elif self.convertsubtitle_option == 40:    #flv en mp4 
        file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
        if file:
            flv_files = glob.glob(f"{file}/**/*.flv", recursive=True)
            if flv_files:
                print("Conversion in progress ...")
                for t in flv_files:
                    out_filename = os.path.splitext(t)[0] + '.mp4'
                    stream = ffmpeg.input(t)
                    stream = ffmpeg.output(stream, out_filename,  vcodec='copy', acodec='copy', map_metadata=0)
                    ffmpeg.run(stream, quiet=True)
                encov = "mp4"
                break
            else:
                QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                continue
        else:
            QMessageBox.critical(None, "Error", "No files selected")
            continue        
    elif self.convertsubtitle_option == 41:    #flv en hevc 
        file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
        if file:
            flv_files = glob.glob(f"{file}/**/*.flv", recursive=True)
            if flv_files:
                print("Conversion in progress ...")
                for t in flv_files:
                    out_filename = os.path.splitext(t)[0] + '.hevc'
                    stream = ffmpeg.input(t)
                    stream = ffmpeg.output(stream, out_filename,  vcodec='copy', acodec='copy', map_metadata=0)
                    ffmpeg.run(stream, quiet=True)
                encov = "hevc"
                break
            else:
                QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                continue
        else:
            QMessageBox.critical(None, "Error", "No files selected")
            continue         
    elif self.convertsubtitle_option == 42:    #flv en webm 
        file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
        if file:
            flv_files = glob.glob(f"{file}/**/*.flv", recursive=True)
            if flv_files:
                print("Conversion in progress ...")
                for t in flv_files:
                    out_filename = os.path.splitext(t)[0] + '.webm'
                    stream = ffmpeg.input(t)
                    stream = ffmpeg.output(stream, out_filename,  vcodec='copy', acodec='copy', map_metadata=0)
                    ffmpeg.run(stream, quiet=True)
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
        
class Convertissosubtitle(QWidget):
    app = QApplication(sys.argv)
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Convertisso subtitle')
        self.setGeometry(100, 100, 700, 400)

        self.path_label = QLabel(self)
        self.path_label.setText('Chose directory (its store your(s) file(s) to convert):')
        self.path_label.move(50, 50)

        self.path_input = QLineEdit(self)
        self.path_input.move(250, 300)
        self.path_input.resize(300, 30)
        self.path_input.text()

        self.choose_path_button = QPushButton('Select a directory', self)
        self.choose_path_button.move(550, 300)
        self.choose_path_button.clicked.connect(self.choose_folder)

        self.convertsubtitle_label = QLabel(self)
        self.convertsubtitle_label.setText('Choose a convert option:')
        self.convertsubtitle_label.move(50, 150)

        self.convertsubtitle_choice = QComboBox(self)
        self.convertsubtitle_choice.addItem('vtt to srt')
        self.convertsubtitle_choice.addItem('vtt to ass')
        self.convertsubtitle_choice.addItem('vtt to lrc')
        self.convertsubtitle_choice.addItem('srt to vtt')
        self.convertsubtitle_choice.addItem('srt to ass')
        self.convertsubtitle_choice.addItem('srt to lrc')
        self.convertsubtitle_choice.addItem('ass to srt')
        self.convertsubtitle_choice.addItem('ass to lrc')
        self.convertsubtitle_choice.addItem('ass to vtt')
        self.convertsubtitle_choice.addItem('lrc to srt')
        self.convertsubtitle_choice.addItem('lrc to ass')
        self.convertsubtitle_choice.addItem('lrc to vtt')
        self.convertsubtitle_choice.move(250, 200)
        self.convertsubtitle_choice.resize(200, 30)
        self.convertsubtitle_choice.currentIndexChanged.connect(self.setconvertsubtitleOption)

        self.convertsubtitle_button = QPushButton('Convert', self)
        self.convertsubtitle_button.move(300, 350)
        self.convertsubtitle_button.clicked.connect(self.convertisso_subtitle)

    def choose_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self, 'Select a directory')
        self.path_input.setText(folder_path)

    def setconvertsubtitleOption(self, index):
        self.convertsubtitle_option = self.convertsubtitle_choice.itemText(index)
    def convertisso_subtitle(self):
        while True:
            if self.convertsubtitle_option == 'vtt to srt':  #vtt en srt 
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
            elif self.convertsubtitle_option == 'vtt to ass':  #vtt en ass
                file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
                if file:
                    vtt_files = glob.glob(f"{file}/**/*.vtt", recursive=True)
                    if vtt_files:
                        print("Conversion in progress ...")
                        for t in vtt_files:
                            out_filename = os.path.splitext(t)[0] + '.ass'
                            stream = ffmpeg.input(t)
                            stream = ffmpeg.output(stream, out_filename, map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                        encov = "ass"
                        break
                    else:
                        QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                        continue
                else:
                    QMessageBox.critical(None, "Error", "No files selected")
                    continue
            if self.convertsubtitle_option == 'vtt en lrc':  # vtt en lrc
                file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
                if file:
                    vtt_files = glob.glob(f"{file}/**/*.vtt", recursive=True)
                    if vtt_files:
                        print("Conversion in progress ...")
                        for t in vtt_files:
                            out_filename = os.path.splitext(t)[0] + '.lrc'
                            stream = ffmpeg.input(t)
                            stream = ffmpeg.output(stream, out_filename, map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                        encov = "lrc"
                        break
                    else:
                        QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                        continue
                else:
                    QMessageBox.critical(None, "Error", "No files selected")
                    continue
            elif self.convertsubtitle_option == 4:  # srt en vtt
                file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
                if file:
                    srt_files = glob.glob(f"{file}/**/*.srt", recursive=True)
                    if srt_files:
                        print("Conversion in progress ...")
                        for t in srt_files:
                            out_filename = os.path.splitext(t)[0] + '.vtt'
                            stream = ffmpeg.input(t)
                            stream = ffmpeg.output(stream, out_filename, map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                        encov = "vtt"
                        break
                    else:
                        QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                        continue
                else:
                    QMessageBox.critical(None, "Error", "No files selected")
                    continue
            elif self.convertsubtitle_option == 5:  # srt en ass
                file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
                if file:
                    srt_files = glob.glob(f"{file}/**/*.srt", recursive=True)
                    if srt_files:
                        print("Conversion in progress ...")
                        for t in srt_files:
                            out_filename = os.path.splitext(t)[0] + '.ass'
                            stream = ffmpeg.input(t)
                            stream = ffmpeg.output(stream, out_filename, map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                        encov = "ass"
                        break
                    else:
                        QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                        continue
                else:
                    QMessageBox.critical(None, "Error", "No files selected")
                    continue
            elif self.convertsubtitle_option == 6:  # srt en lrc
                file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
                if file:
                    srt_files = glob.glob(f"{file}/**/*.srt", recursive=True)
                    if srt_files:
                        print("Conversion in progress ...")
                        for t in srt_files:
                            out_filename = os.path.splitext(t)[0] + '.lrc'
                            stream = ffmpeg.input(t)
                            stream = ffmpeg.output(stream, out_filename, map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                        encov = "lrc"
                        break
                    else:
                        QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                        continue
                else:
                    QMessageBox.critical(None, "Error", "No files selected")
                    continue        
            elif self.convertsubtitle_option == 7:    #ass en srt 
                file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
                if file:
                    ass_files = glob.glob(f"{file}/**/*.ass", recursive=True)
                    if ass_files:
                        print("Conversion in progress ...")
                        for t in ass_files:
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
            elif self.convertsubtitle_option == 8:    #ass en lrc 
                file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
                if file:
                    ass_files = glob.glob(f"{file}/**/*.ass", recursive=True)
                    if ass_files:
                        print("Conversion in progress ...")
                        for t in ass_files:
                            out_filename = os.path.splitext(t)[0] + '.lrc'
                            stream = ffmpeg.input(t)
                            stream = ffmpeg.output(stream, out_filename, map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                        encov = "lrc"
                        break
                    else:
                        QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                        continue
                else:
                    QMessageBox.critical(None, "Error", "No files selected")
                    continue
            elif self.convertsubtitle_option == 9:    #ass en vtt 
                file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
                if file:
                    ass_files = glob.glob(f"{file}/**/*.ass", recursive=True)
                    if ass_files:
                        print("Conversion in progress ...")
                        for t in ass_files:
                            out_filename = os.path.splitext(t)[0] + '.vtt'
                            stream = ffmpeg.input(t)
                            stream = ffmpeg.output(stream, out_filename, map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                        encov = "vtt"
                        break
                    else:
                        QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                        continue
                else:
                    QMessageBox.critical(None, "Error", "No files selected")
                    continue
            elif self.convertsubtitle_option == 10:    #lrc en srt 
                file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
                if file:
                    lrc_files = glob.glob(f"{file}/**/*.lrc", recursive=True)
                    if lrc_files:
                        print("Conversion in progress ...")
                        for t in lrc_files:
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
            elif self.convertsubtitle_option == 11:    #lrc en ass 
                file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
                if file:
                    lrc_files = glob.glob(f"{file}/**/*.lrc", recursive=True)
                    if lrc_files:
                        print("Conversion in progress ...")
                        for t in lrc_files:
                            out_filename = os.path.splitext(t)[0] + '.ass'
                            stream = ffmpeg.input(t)
                            stream = ffmpeg.output(stream, out_filename, map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                        encov = "ass"
                        break
                    else:
                        QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                        continue
                else:
                    QMessageBox.critical(None, "Error", "No files selected")
                    continue         
            elif self.convertsubtitle_option == 12:    #lrc en vtt 
                file = QFileDialog.getExistingDirectory(None, "Select one directory (not recursive)")
                if file:
                    lrc_files = glob.glob(f"{file}/**/*.lrc", recursive=True)
                    if lrc_files:
                        print("Conversion in progress ...")
                        for t in lrc_files:
                            out_filename = os.path.splitext(t)[0] + '.vtt'
                            stream = ffmpeg.input(t)
                            stream = ffmpeg.output(stream, out_filename, map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
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
window = Convertissosubtitle()
window.show()
app.exec_()
        
def convertissso_audio():
    audio=1
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

asd=int(input("Entrer le bon numero: 1=download, 2=video, 3=audio, 4=subtitle. ->  "))

if asd == 1:
    YoutubeDownloader()
    window = YoutubeDownloader()
    window.show()()
elif asd == 2:
    convertissso_video()
elif asd == 3:
    convertissso_audio()
elif asd == 4:
    convertissso_subtitle()
else:
    print("erreur")
