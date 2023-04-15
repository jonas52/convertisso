#!/usr/bin/env python3
# a ajouter pop-up pour la convertion reussi --bon
# installer -- a faire
# enlever le sub process -- bon 
# option pour sans ffmpeg avec yt_dlp --a faire
import os
from urllib import request
import subprocess
import shutil
import glob
import yt_dlp
import ffmpeg
from PyQt5.QtCore import Qt, QTimer
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QTabWidget, QWidget, QLabel, QPushButton, QLineEdit, QComboBox, QFileDialog, QMessageBox, QMainWindow, QDesktopWidget, QVBoxLayout, QScrollBar, QProgressBar
from PyQt5.QtGui import QColor
import requests
import sys
from pydub import AudioSegment
from urllib import request

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

def show_success_message():
    message_box = QMessageBox()
    message_box.setWindowTitle("Successful conversion")
    message_box.setText("The conversion was successful")
    message_box.setIcon(QMessageBox.Information)
    message_box.setStandardButtons(QMessageBox.Ok)
    message_box.exec_()

def show_download_success_message():
    message_box = QMessageBox()
    message_box.setWindowTitle("Successful download")
    message_box.setText("The download was successful.")
    message_box.setIcon(QMessageBox.Information)
    message_box.addButton(QMessageBox.Ok)
    message_box.exec_()

def internet_check(host='https://google.com'):
    '''
    Check if the user have an Internet connection by connecting to google.com over https
    '''
    try:
        request.urlopen(host, timeout=4)
        return True
    except:
        return False

class DownloaderTab(QWidget):
    def __init__(self):
        super().__init__()

        label = QLabel("Downloader", self)
        label.move(20, 20)

        self.initUI()

    def initUI(self):

        self.link_label = QLabel(self)
        self.link_label.setText('Enter video link:')        
        self.link_label.move(50, 100)
        
        self.link_input = QLineEdit(self)
        self.link_input.move(250, 100)
        self.link_input.resize(300, 30)
        self.link_input.text()

        self.name_label = QLabel(self)
        self.name_label.setText('Enter the name of the file:')
        self.name_label.move(50, 150)

        self.name_input = QLineEdit(self)
        self.name_input.move(250, 150)
        self.name_input.resize(300, 30)
        self.name_input.text()

        self.destination_label = QLabel(self)
        self.destination_label.setText('Enter destination folder:')
        self.destination_label.move(50, 350)

        self.destination_input = QLineEdit(self)
        self.destination_input.move(250, 350)
        self.destination_input.resize(300, 30)
        self.destination_input.text()

        self.choose_destination_button = QPushButton('Choose Folder', self)
        self.choose_destination_button.move(550, 350)
        self.choose_destination_button.clicked.connect(self.choose_folder)

        self.download_label = QLabel(self)
        self.download_label.setText('Choose download option:')
        self.download_label.move(50, 200)

        self.download_choice = QComboBox(self)
        self.download_choice.addItem('Please choice')
        self.download_choice.addItem('Video Only')
        self.download_choice.addItem('Video + Subtitles')
        self.download_choice.addItem('Audio Only')
        self.download_choice.addItem('Subtitles Only')
        self.download_choice.move(250, 200)
        self.download_choice.setEditable(True)        
        self.download_choice.resize(200, 30)
        self.download_choice.currentIndexChanged.connect(self.setDownloadOption)
    
        self.internet_txt_label = QLabel(self)
        self.internet_txt_label.setText('Internet check : ')
        self.internet_txt_label.move(475, 20)

        self.internet_label = QLabel(self)
        self.internet_label.setFixedSize(20, 20)
        self.internet_label.move(600, 20)
        self.internet_label.setStyleSheet("background-color: red; border-radius: 10px;")
        self.timer = QTimer()
        self.timer.timeout.connect(self.check_internet_connection)
        self.timer.start(1000)

        self.download_button = QPushButton('Download', self)
        self.download_button.move(350, 400)
        self.download_button.clicked.connect(self.download_video)


    def choose_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self, 'Choose Folder')
        self.destination_input.setText(folder_path)

    def setDownloadOption(self, index):
        self.download_option_user = self.download_choice.itemText(index)
    
    def check_internet_connection(self):
        try:
            response = requests.get('http://www.google.com', timeout=5)
            if response.status_code == 200:
                self.internet_label.setStyleSheet("background-color: green; border-radius: 10px;")
            else:
                self.internet_label.setStyleSheet("background-color: red; border-radius: 10px;")
        except:
            self.internet_label.setStyleSheet("background-color: red; border-radius: 10px;")
    


    def download_video(self):
        try:
            if internet_check() == True:
                if self.download_option_user == 'Video Only':
                    ydl_opts = {
                        'format': 'best',
                        'addmetadata': True,
                        'outtmpl': self.name_input.text()
                    }
                    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                        ydl.download([self.link_input.text()])
                    for extension in ["*.mp4", "*.mkv", "*.webm", "*.flv"]:
                        for filename in glob.glob(extension):
                            shutil.move(filename, self.destination_input.text())
                    show_download_success_message()
                elif self.download_option_user == 'Video + Subtitles':
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
                    show_download_success_message()
                if self.download_option_user == 'Audio Only':
                    ydl_opts = {
                        'format': 'bestaudio/best',
                        'postprocessors': [{
                            'key': 'FFmpegExtractAudio',
                            'preferredcodec': 'flac',
                            'preferredquality': 'lossless',
                        }],
                        'addmetadata': True,
                        'outtmpl': self.name_input.text() + '.%(ext)s'
                    }
                    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                        ydl.download([self.link_input.text()])
                    for extension in ["*.mp3", "*.aac", "*.flac", "*.m4a", "*.ogg", "*.wav", "*.opus", "*.vorbis"]:
                        for filename in glob.glob(extension):
                            shutil.move(filename, self.destination_input.text())
                    show_download_success_message()
                elif self.download_option_user == 'Subtitles Only':
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
                    show_download_success_message()
                else:
                    QMessageBox.critical(None, "Error", "An unexpected error has occurred")
            else:
                QMessageBox.critical(None, "Error", "No internet connextion please check your connection")
        except Exception as e:
            error_message = "Une erreur s'est produite lors du téléchargement : {}".format(str(e))
            message_box = QMessageBox()
            message_box.setWindowTitle("Erreur de téléchargement")
            message_box.setText(error_message)
            message_box.setIcon(QMessageBox.Warning)
            message_box.addButton(QMessageBox.Ok)
            message_box.exec_()

class AudioTab(QWidget):

    def __init__(self):
        super().__init__()

        label = QLabel("Audio content", self)
        label.move(20, 20)
        self.initUI()
    def initUI(self):
        
        self.path_label = QLabel(self)
        self.path_label.setText('Chose directory (its store your(s) file(s) to convert):')
        self.path_label.move(50, 50)

        self.path_input = QLineEdit(self)
        self.path_input.move(430, 50)
        self.path_input.resize(300, 30)
        self.path_input.text()

        self.choose_path_button = QPushButton('Choose Folder', self)
        self.choose_path_button.move(730, 50)
        self.choose_path_button.clicked.connect(self.choose_folder)
        self.convertaudio_choice = QComboBox(self)
        self.convertaudio_choice.addItem('Please choose')
        self.convertaudio_choice.addItems(['mp3 to ogg', 'mp3 to aac', 'mp3 to wav', 'mp3 to ac3', 'mp3 to opus', 'mp3 to m4a',
                                        'wav to ogg', 'wav to aac', 'wav to mp3', 'wav to ac3', 'wav to opus', 'wav to m4a',
                                        'ogg to wav', 'ogg to aac', 'ogg to mp3', 'ogg to ac3', 'ogg to opus', 'ogg to m4a',
                                        'ac3 to wav', 'ac3 to aac', 'ac3 to mp3', 'ac3 to ogg', 'ac3 to opus', 'ac3 to m4a',
                                        'aac to wav', 'aac to ac3', 'aac to mp3', 'aac to ogg', 'aac to opus', 'aac to m4a',
                                        'flac to wav', 'flac to ac3', 'flac to mp3', 'flac to ogg', 'flac to opus', 'flac to m4a', 'flac to aac',
                                        'opus to wav', 'opus to ac3', 'opus to mp3', 'opus to ogg', 'opus to m4a', 'opus to aac',
                                        'm4a to wav', 'm4a to ac3', 'm4a to mp3', 'm4a to ogg', 'm4a to opus', 'm4a to aac'])
        self.convertaudio_choice.move(250, 200)
        self.convertaudio_choice.resize(200, 30)
        self.convertaudio_choice.setMaxVisibleItems(5)
        self.convertaudio_choice.setEditable(True)
        self.convertaudio_choice.view().setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.convertaudio_choice.currentIndexChanged.connect(self.setaudioOption)
        
        self.convertaudio_button = QPushButton('Convert', self)
        self.convertaudio_button.move(300, 350)
        self.convertaudio_button.clicked.connect(self.convertaudio)

    def choose_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self, 'Choose Folder')
        self.path_input.setText(folder_path)

    def setaudioOption(self, index):
        self.convert_audio_choice = self.convertaudio_choice.itemText(index)

    def convertaudio(self):

        if self.convert_audio_choice == 'mp3 to ogg':
            mp3_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.mp3"), recursive=True)
            if mp3_files:
                print("Conversion in progress ...")
                for mp3_file in mp3_files:
                    ogg_file = os.path.splitext(mp3_file)[0] + '.ogg'
                    try:
                        stream = ffmpeg.input(mp3_file)
                        stream = ffmpeg.output(stream, ogg_file, acodec='libvorbis', map_metadata=0)
                        ffmpeg.run(stream, quiet=True)
                        print("Conversion OK")
                    except ffmpeg.Error as e:
                        QMessageBox.critical(None, "Error", f"Failed to convert {mp3_file}: {e.stderr}")
                        return
                    encov = "ogg"
            else:
                QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                return
            show_success_message()
        elif self.convert_audio_choice == 'mp3 to aac':
                mp3_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.mp3"), recursive=True)
                if mp3_files:
                    print("Conversion in progress ...")
                    for mp3_file in mp3_files:
                        aac_file = os.path.splitext(mp3_file)[0] + '.aac'
                        try:
                            stream = ffmpeg.input(mp3_file)
                            stream = ffmpeg.output(stream, aac_file, acodec='aac', map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                            print("Conversion OK")
                            show_success_message()
                        except ffmpeg.Error as e:
                            QMessageBox.critical(None, "Error", f"Failed to convert {mp3_file}: {e.stderr}")
                            return
                        encov = "aac"
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
        elif self.convert_audio_choice == 'mp3 to wav':
                mp3_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.mp3"), recursive=True)
                if mp3_files:
                    print("Conversion in progress ...")
                    for mp3_file in mp3_files:
                        wav_file = os.path.splitext(mp3_file)[0] + '.wav'
                        try:
                            stream = ffmpeg.input(mp3_file)
                            stream = ffmpeg.output(stream, wav_file, map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                            print("Conversion OK")
                            show_success_message()
                        except ffmpeg.Error as e:
                            QMessageBox.critical(None, "Error", f"Failed to convert {mp3_file}: {e.stderr}")
                            return
                        encov = "aac"
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
        elif self.convert_audio_choice == 'mp3 to ac3':
                mp3_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.mp3"), recursive=True)
                if mp3_files:
                    print("Conversion in progress ...")
                    for mp3_file in mp3_files:
                        ac3_file = os.path.splitext(mp3_file)[0] + '.ac3'
                        try:
                            stream = ffmpeg.input(mp3_file)
                            stream = ffmpeg.output(stream, ac3_file, acodec='ac3', map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                            print("Conversion OK")
                            show_success_message()
                        except ffmpeg.Error as e:
                            QMessageBox.critical(None, "Error", f"Failed to convert {mp3_file}: {e.stderr}")
                            return
                        encov = "ac3"
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
        elif self.convert_audio_choice == 'mp3 to opus':
                mp3_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.mp3"), recursive=True)
                if mp3_files:
                    print("Conversion in progress ...")
                    for mp3_file in mp3_files:
                        opus_file = os.path.splitext(mp3_file)[0] + '.opus'
                        try:
                            stream = ffmpeg.input(mp3_file)
                            stream = ffmpeg.output(stream, opus_file, acodec='libopus', map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                            print("Conversion OK")
                            show_success_message()
                        except ffmpeg.Error as e:
                            QMessageBox.critical(None, "Error", f"Failed to convert {mp3_file}: {e.stderr}")
                            return
                        encov = "opus"
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
        elif self.convert_audio_choice == 'mp3 to m4a':
                mp3_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.mp3"), recursive=True)
                if mp3_files:
                    print("Conversion in progress ...")
                    for mp3_file in mp3_files:
                        m4a_file = os.path.splitext(mp3_file)[0] + '.m4a'
                        try:
                            stream = ffmpeg.input(mp3_file)
                            stream = ffmpeg.output(stream, m4a_file, acodec='alac', map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                            print("Conversion OK")
                            show_success_message()
                        except ffmpeg.Error as e:
                            QMessageBox.critical(None, "Error", f"Failed to convert {mp3_file}: {e.stderr}")
                            return
                        encov = "m4a"
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
        elif self.convert_audio_choice == 'wav to ogg':
                wav_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.wav"), recursive=True)
                if wav_files:
                    print("Conversion in progress ...")
                    for wav_file in wav_files:
                        ogg_file = os.path.splitext(wav_file)[0] + '.ogg'
                        try:
                            stream = ffmpeg.input(wav_file)
                            stream = ffmpeg.output(stream, ogg_file, acodec='libvorbis', map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                            print("Conversion OK")
                            show_success_message()
                        except ffmpeg.Error as e:
                            QMessageBox.critical(None, "Error", f"Failed to convert {wav_file}: {e.stderr}")
                            return
                        encov = "ogg"
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
        elif self.convert_audio_choice == 'wav to aac':
                wav_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.wav"), recursive=True)
                if wav_files:
                    print("Conversion in progress ...")
                    for wav_file in wav_files:
                        aac_file = os.path.splitext(wav_file)[0] + '.aac'
                        try:
                            stream = ffmpeg.input(wav_file)
                            stream = ffmpeg.output(stream, aac_file, acodec='aac', map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                            print("Conversion OK")
                            show_success_message()
                        except ffmpeg.Error as e:
                            QMessageBox.critical(None, "Error", f"Failed to convert {wav_file}: {e.stderr}")
                            return
                        encov = "aac"
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
        elif self.convert_audio_choice == 'wav to mp3':
                wav_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.wav"), recursive=True)
                if wav_files:
                    print("Conversion in progress ...")
                    for wav_file in wav_files:
                        mp3_file = os.path.splitext(wav_file)[0] + '.mp3'
                        try:
                            stream = ffmpeg.input(wav_file)
                            stream = ffmpeg.output(stream, mp3_file, acodec='libmp3lame', map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                            print("Conversion OK")
                            show_success_message()
                        except ffmpeg.Error as e:
                            QMessageBox.critical(None, "Error", f"Failed to convert {wav_file}: {e.stderr}")
                            return
                        encov = "aac"
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
        elif self.convert_audio_choice == 'wav to ac3':
                wav_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.wav"), recursive=True)
                if wav_files:
                    print("Conversion in progress ...")
                    for wav_file in wav_files:
                        ac3_file = os.path.splitext(wav_file)[0] + '.ac3'
                        try:
                            stream = ffmpeg.input(wav_file)
                            stream = ffmpeg.output(stream, ac3_file, acodec='ac3', map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                            print("Conversion OK")
                            show_success_message()
                        except ffmpeg.Error as e:
                            QMessageBox.critical(None, "Error", f"Failed to convert {wav_file}: {e.stderr}")
                            return
                        encov = "ac3"
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
        elif self.convert_audio_choice == 'wav to opus':
                wav_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.wav"), recursive=True)
                if wav_files:
                    print("Conversion in progress ...")
                    for wav_file in wav_files:
                        opus_file = os.path.splitext(wav_file)[0] + '.opus'
                        try:
                            stream = ffmpeg.input(wav_file)
                            stream = ffmpeg.output(stream, opus_file, acodec='libopus', map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                            print("Conversion OK")
                            show_success_message()
                        except ffmpeg.Error as e:
                            QMessageBox.critical(None, "Error", f"Failed to convert {wav_file}: {e.stderr}")
                            return
                        encov = "opus"
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
        elif self.convert_audio_choice == 'wav to m4a':
                wav_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.wav"), recursive=True)
                if wav_files:
                    print("Conversion in progress ...")
                    for wav_file in wav_files:
                        m4a_file = os.path.splitext(wav_file)[0] + '.m4a'
                        try:
                            stream = ffmpeg.input(wav_file)
                            stream = ffmpeg.output(stream, m4a_file, acodec='alac', map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                            print("Conversion OK")
                            show_success_message()
                        except ffmpeg.Error as e:
                            QMessageBox.critical(None, "Error", f"Failed to convert {wav_file}: {e.stderr}")
                            return
                        encov = "m4a"
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
        elif self.convert_audio_choice == 'ogg to wav':
                ogg_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.ogg"), recursive=True)
                if ogg_files:
                    print("Conversion in progress ...")
                    for ogg_file in ogg_files:
                        wav_file = os.path.splitext(ogg_file)[0] + '.wav'
                        try:
                            stream = ffmpeg.input(ogg_file)
                            stream = ffmpeg.output(stream, wav_file, map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                            print("Conversion OK")
                            show_success_message()
                        except ffmpeg.Error as e:
                            QMessageBox.critical(None, "Error", f"Failed to convert {ogg_file}: {e.stderr}")
                            return
                        encov = "ogg"
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
        elif self.convert_audio_choice == 'ogg to aac':
                ogg_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.ogg"), recursive=True)
                if ogg_files:
                    print("Conversion in progress ...")
                    for ogg_file in ogg_files:
                        aac_file = os.path.splitext(ogg_file)[0] + '.aac'
                        try:
                            stream = ffmpeg.input(ogg_file)
                            stream = ffmpeg.output(stream, aac_file, acodec='aac', map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                            print("Conversion OK")
                            show_success_message()
                        except ffmpeg.Error as e:
                            QMessageBox.critical(None, "Error", f"Failed to convert {ogg_file}: {e.stderr}")
                            return
                        encov = "aac"
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
        elif self.convert_audio_choice == 'ogg to mp3':
                ogg_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.ogg"), recursive=True)
                if ogg_files:
                    print("Conversion in progress ...")
                    for ogg_file in ogg_files:
                        mp3_file = os.path.splitext(ogg_file)[0] + '.mp3'
                        try:
                            stream = ffmpeg.input(ogg_file)
                            stream = ffmpeg.output(stream, mp3_file, acodec='libmp3lame', map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                            print("Conversion OK")
                            show_success_message()
                        except ffmpeg.Error as e:
                            QMessageBox.critical(None, "Error", f"Failed to convert {ogg_file}: {e.stderr}")
                            return
                        encov = "aac"
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
        elif self.convert_audio_choice == 'ogg to ac3':
                ogg_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.ogg"), recursive=True)
                if ogg_files:
                    print("Conversion in progress ...")
                    for ogg_file in ogg_files:
                        ac3_file = os.path.splitext(ogg_file)[0] + '.ac3'
                        try:
                            stream = ffmpeg.input(ogg_file)
                            stream = ffmpeg.output(stream, ac3_file, acodec='ac3', map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                            print("Conversion OK")
                            show_success_message()
                        except ffmpeg.Error as e:
                            QMessageBox.critical(None, "Error", f"Failed to convert {ogg_file}: {e.stderr}")
                            return
                        encov = "ac3"
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
        elif self.convert_audio_choice == 'ogg to opus':
                ogg_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.ogg"), recursive=True)
                if ogg_files:
                    print("Conversion in progress ...")
                    for ogg_file in ogg_files:
                        opus_file = os.path.splitext(ogg_file)[0] + '.opus'
                        try:
                            stream = ffmpeg.input(ogg_file)
                            stream = ffmpeg.output(stream, opus_file, acodec='libopus', map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                            print("Conversion OK")
                            show_success_message()
                        except ffmpeg.Error as e:
                            QMessageBox.critical(None, "Error", f"Failed to convert {ogg_file}: {e.stderr}")
                            return
                        encov = "opus"
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
        elif self.convert_audio_choice == 'ogg to m4a':
                ogg_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.ogg"), recursive=True)
                if ogg_files:
                    print("Conversion in progress ...")
                    for ogg_file in ogg_files:
                        m4a_file = os.path.splitext(ogg_file)[0] + '.m4a'
                        try:
                            stream = ffmpeg.input(ogg_file)
                            stream = ffmpeg.output(stream, m4a_file, acodec='alac', map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                            print("Conversion OK")
                            show_success_message()
                        except ffmpeg.Error as e:
                            QMessageBox.critical(None, "Error", f"Failed to convert {ogg_file}: {e.stderr}")
                            return
                        encov = "m4a"
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
        elif self.convert_audio_choice == 'ac3 to wav':
                ac3_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.ac3"), recursive=True)
                if ac3_files:
                    print("Conversion in progress ...")
                    for ac3_file in ac3_files:
                        wav_file = os.path.splitext(ac3_file)[0] + '.wav'
                        try:
                            stream = ffmpeg.input(ac3_file)
                            stream = ffmpeg.output(stream, wav_file, map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                            print("Conversion OK")
                            show_success_message()
                        except ffmpeg.Error as e:
                            QMessageBox.critical(None, "Error", f"Failed to convert {ac3_file}: {e.stderr}")
                            return
                        encov = "ac3"
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
        elif self.convert_audio_choice == 'ac3 to aac':
                ac3_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.ac3"), recursive=True)
                if ac3_files:
                    print("Conversion in progress ...")
                    for ac3_file in ac3_files:
                        aac_file = os.path.splitext(ac3_file)[0] + '.aac'
                        try:
                            stream = ffmpeg.input(ac3_file)
                            stream = ffmpeg.output(stream, aac_file, acodec='aac', map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                            print("Conversion OK")
                            show_success_message()
                        except ffmpeg.Error as e:
                            QMessageBox.critical(None, "Error", f"Failed to convert {ac3_file}: {e.stderr}")
                            return
                        encov = "aac"
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
        elif self.convert_audio_choice == 'ac3 to mp3':
                ac3_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.ac3"), recursive=True)
                if ac3_files:
                    print("Conversion in progress ...")
                    for ac3_file in ac3_files:
                        mp3_file = os.path.splitext(ac3_file)[0] + '.mp3'
                        try:
                            stream = ffmpeg.input(ac3_file)
                            stream = ffmpeg.output(stream, mp3_file, acodec='libmp3lame', map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                            print("Conversion OK")
                            show_success_message()
                        except ffmpeg.Error as e:
                            QMessageBox.critical(None, "Error", f"Failed to convert {ac3_file}: {e.stderr}")
                            return
                        encov = "aac"
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
        elif self.convert_audio_choice == 'ac3 to ogg':
                ac3_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.ac3"), recursive=True)
                if ac3_files:
                    print("Conversion in progress ...")
                    for ac3_file in ac3_files:
                        ogg_file = os.path.splitext(ac3_file)[0] + '.ogg'
                        try:
                            stream = ffmpeg.input(ac3_file)
                            stream = ffmpeg.output(stream, ogg_file, acodec='libvorbis', map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                            print("Conversion OK")
                            show_success_message()
                        except ffmpeg.Error as e:
                            QMessageBox.critical(None, "Error", f"Failed to convert {ac3_file}: {e.stderr}")
                            return
                        encov = "ogg"
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
        elif self.convert_audio_choice == 'ac3 to opus':
                ac3_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.ac3"), recursive=True)
                if ac3_files:
                    print("Conversion in progress ...")
                    for ac3_file in ac3_files:
                        opus_file = os.path.splitext(ac3_file)[0] + '.opus'
                        try:
                            stream = ffmpeg.input(ac3_file)
                            stream = ffmpeg.output(stream, opus_file, acodec='libopus', map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                            print("Conversion OK")
                            show_success_message()
                        except ffmpeg.Error as e:
                            QMessageBox.critical(None, "Error", f"Failed to convert {ac3_file}: {e.stderr}")
                            return
                        encov = "opus"
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
        elif self.convert_audio_choice == 'ac3 to m4a':
                ac3_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.ac3"), recursive=True)
                if ac3_files:
                    print("Conversion in progress ...")
                    for ac3_file in ac3_files:
                        m4a_file = os.path.splitext(ac3_file)[0] + '.m4a'
                        try:
                            stream = ffmpeg.input(ac3_file)
                            stream = ffmpeg.output(stream, m4a_file, acodec='alac', map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                            print("Conversion OK")
                            show_success_message()
                        except ffmpeg.Error as e:
                            QMessageBox.critical(None, "Error", f"Failed to convert {ac3_file}: {e.stderr}")
                            return
                        encov = "m4a"
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
        elif self.convert_audio_choice == 'aac to wav':
                aac_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.aac"), recursive=True)
                if aac_files:
                    print("Conversion in progress ...")
                    for aac_file in aac_files:
                        wav_file = os.path.splitext(aac_file)[0] + '.wav'
                        try:
                            stream = ffmpeg.input(aac_file)
                            stream = ffmpeg.output(stream, wav_file, map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                            print("Conversion OK")
                            show_success_message()
                        except ffmpeg.Error as e:
                            QMessageBox.critical(None, "Error", f"Failed to convert {aac_file}: {e.stderr}")
                            return
                        encov = "aac"
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
        elif self.convert_audio_choice == 'aac to ac3':
                aac_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.aac"), recursive=True)
                if aac_files:
                    print("Conversion in progress ...")
                    for aac_file in aac_files:
                        ac3_file = os.path.splitext(aac_file)[0] + '.ac3'
                        try:
                            stream = ffmpeg.input(aac_file)
                            stream = ffmpeg.output(stream, ac3_file, acodec='ac3', map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                            print("Conversion OK")
                            show_success_message()
                        except ffmpeg.Error as e:
                            QMessageBox.critical(None, "Error", f"Failed to convert {aac_file}: {e.stderr}")
                            return
                        encov = "ac3"
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
        elif self.convert_audio_choice == 'aac to mp3':
                aac_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.aac"), recursive=True)
                if aac_files:
                    print("Conversion in progress ...")
                    for aac_file in aac_files:
                        mp3_file = os.path.splitext(aac_file)[0] + '.mp3'
                        try:
                            stream = ffmpeg.input(aac_file)
                            stream = ffmpeg.output(stream, mp3_file, acodec='libmp3lame', map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                            print("Conversion OK")
                            show_success_message()
                        except ffmpeg.Error as e:
                            QMessageBox.critical(None, "Error", f"Failed to convert {aac_file}: {e.stderr}")
                            return
                        encov = "aac"
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
        elif self.convert_audio_choice == 'aac to ogg':
                aac_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.aac"), recursive=True)
                if aac_files:
                    print("Conversion in progress ...")
                    for aac_file in aac_files:
                        ogg_file = os.path.splitext(aac_file)[0] + '.ogg'
                        try:
                            stream = ffmpeg.input(aac_file)
                            stream = ffmpeg.output(stream, ogg_file, acodec='libvorbis', map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                            print("Conversion OK")
                            show_success_message()
                        except ffmpeg.Error as e:
                            QMessageBox.critical(None, "Error", f"Failed to convert {aac_file}: {e.stderr}")
                            return
                        encov = "ogg"
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
        elif self.convert_audio_choice == 'aac to opus':
                aac_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.aac"), recursive=True)
                if aac_files:
                    print("Conversion in progress ...")
                    for aac_file in aac_files:
                        opus_file = os.path.splitext(aac_file)[0] + '.opus'
                        try:
                            stream = ffmpeg.input(aac_file)
                            stream = ffmpeg.output(stream, opus_file, acodec='libopus', map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                            print("Conversion OK")
                            show_success_message()
                        except ffmpeg.Error as e:
                            QMessageBox.critical(None, "Error", f"Failed to convert {aac_file}: {e.stderr}")
                            return
                        encov = "opus"
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
        elif self.convert_audio_choice == 'aac to m4a':
                aac_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.aac"), recursive=True)
                if aac_files:
                    print("Conversion in progress ...")
                    for aac_file in aac_files:
                        m4a_file = os.path.splitext(aac_file)[0] + '.m4a'
                        try:
                            stream = ffmpeg.input(aac_file)
                            stream = ffmpeg.output(stream, m4a_file, acodec='alac', map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                            print("Conversion OK")
                            show_success_message()
                        except ffmpeg.Error as e:
                            QMessageBox.critical(None, "Error", f"Failed to convert {aac_file}: {e.stderr}")
                            return
                        encov = "m4a"
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
        elif self.convert_audio_choice == 'flac to wav':
                flac_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.flac"), recursive=True)
                if flac_files:
                    print("Conversion in progress ...")
                    for flac_file in flac_files:
                        wav_file = os.path.splitext(flac_file)[0] + '.wav'
                        try:
                            stream = ffmpeg.input(flac_file)
                            stream = ffmpeg.output(stream, wav_file, map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                            print("Conversion OK")
                            show_success_message()
                        except ffmpeg.Error as e:
                            QMessageBox.critical(None, "Error", f"Failed to convert {flac_file}: {e.stderr}")
                            return
                        encov = "flac"
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
        elif self.convert_audio_choice == 'flac to ac3':
                flac_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.flac"), recursive=True)
                if flac_files:
                    print("Conversion in progress ...")
                    for flac_file in flac_files:
                        ac3_file = os.path.splitext(flac_file)[0] + '.ac3'
                        try:
                            stream = ffmpeg.input(flac_file)
                            stream = ffmpeg.output(stream, ac3_file, acodec='ac3', map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                            print("Conversion OK")
                            show_success_message()
                        except ffmpeg.Error as e:
                            QMessageBox.critical(None, "Error", f"Failed to convert {flac_file}: {e.stderr}")
                            return
                        encov = "ac3"
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
        elif self.convert_audio_choice == 'flac to mp3':
                flac_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.flac"), recursive=True)
                if flac_files:
                    print("Conversion in progress ...")
                    for flac_file in flac_files:
                        mp3_file = os.path.splitext(flac_file)[0] + '.mp3'
                        try:
                            stream = ffmpeg.input(flac_file)
                            stream = ffmpeg.output(stream, mp3_file, acodec='libmp3lame', map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                            print("Conversion OK")
                            show_success_message()
                        except ffmpeg.Error as e:
                            QMessageBox.critical(None, "Error", f"Failed to convert {flac_file}: {e.stderr}")
                            return
                        encov = "mp3"
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
        elif self.convert_audio_choice == 'flac to ogg':
                flac_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.flac"), recursive=True)
                if flac_files:
                    print("Conversion in progress ...")
                    for flac_file in flac_files:
                        ogg_file = os.path.splitext(flac_file)[0] + '.ogg'
                        try:
                            stream = ffmpeg.input(flac_file)
                            stream = ffmpeg.output(stream, ogg_file, acodec='libvorbis', map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                            print("Conversion OK")
                            show_success_message()
                        except ffmpeg.Error as e:
                            QMessageBox.critical(None, "Error", f"Failed to convert {flac_file}: {e.stderr}")
                            return
                        encov = "ogg"
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
        elif self.convert_audio_choice == 'flac to opus':
                flac_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.flac"), recursive=True)
                if flac_files:
                    print("Conversion in progress ...")
                    for flac_file in flac_files:
                        opus_file = os.path.splitext(flac_file)[0] + '.opus'
                        try:
                            stream = ffmpeg.input(flac_file)
                            stream = ffmpeg.output(stream, opus_file, acodec='libopus', map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                            print("Conversion OK")
                            show_success_message()
                        except ffmpeg.Error as e:
                            QMessageBox.critical(None, "Error", f"Failed to convert {flac_file}: {e.stderr}")
                            return
                        encov = "opus"
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
        elif self.convert_audio_choice == 'flac to m4a':
                flac_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.flac"), recursive=True)
                if flac_files:
                    print("Conversion in progress ...")
                    for flac_file in flac_files:
                        m4a_file = os.path.splitext(flac_file)[0] + '.m4a'
                        try:
                            stream = ffmpeg.input(flac_file)
                            stream = ffmpeg.output(stream, m4a_file, acodec='alac', map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                            print("Conversion OK")
                            show_success_message()
                        except ffmpeg.Error as e:
                            QMessageBox.critical(None, "Error", f"Failed to convert {flac_file}: {e.stderr}")
                            return
                        encov = "m4a"
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
        elif self.convert_audio_choice == 'flac to aac':
                flac_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.flac"), recursive=True)
                if flac_files:
                    print("Conversion in progress ...")
                    for flac_file in flac_files:
                        aac_file = os.path.splitext(flac_file)[0] + '.aac'
                        try:
                            stream = ffmpeg.input(flac_file)
                            stream = ffmpeg.output(stream, aac_file, acodec='aac', map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                            print("Conversion OK")
                            show_success_message()
                        except ffmpeg.Error as e:
                            QMessageBox.critical(None, "Error", f"Failed to convert {flac_file}: {e.stderr}")
                            return
                        encov = "aac"
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
        elif self.convert_audio_choice == 'opus to wav':
                opus_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.opus"), recursive=True)
                if opus_files:
                    print("Conversion in progress ...")
                    for opus_file in opus_files:
                        wav_file = os.path.splitext(opus_file)[0] + '.wav'
                        try:
                            stream = ffmpeg.input(opus_file)
                            stream = ffmpeg.output(stream, wav_file, map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                            print("Conversion OK")
                            show_success_message()
                        except ffmpeg.Error as e:
                            QMessageBox.critical(None, "Error", f"Failed to convert {opus_file}: {e.stderr}")
                            return
                        encov = "opus"
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
        elif self.convert_audio_choice == 'opus to ac3':
                opus_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.opus"), recursive=True)
                if opus_files:
                    print("Conversion in progress ...")
                    for opus_file in opus_files:
                        ac3_file = os.path.splitext(opus_file)[0] + '.ac3'
                        try:
                            stream = ffmpeg.input(opus_file)
                            stream = ffmpeg.output(stream, ac3_file, acodec='ac3', map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                            print("Conversion OK")
                            show_success_message()
                        except ffmpeg.Error as e:
                            QMessageBox.critical(None, "Error", f"Failed to convert {opus_file}: {e.stderr}")
                            return
                        encov = "ac3"
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
        elif self.convert_audio_choice == 'opus to mp3':
                opus_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.opus"), recursive=True)
                if opus_files:
                    print("Conversion in progress ...")
                    for opus_file in opus_files:
                        mp3_file = os.path.splitext(opus_file)[0] + '.mp3'
                        try:
                            stream = ffmpeg.input(opus_file)
                            stream = ffmpeg.output(stream, mp3_file, acodec='libmp3lame', map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                            print("Conversion OK")
                            show_success_message()
                        except ffmpeg.Error as e:
                            QMessageBox.critical(None, "Error", f"Failed to convert {opus_file}: {e.stderr}")
                            return
                        encov = "opus"
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
        elif self.convert_audio_choice == 'opus to ogg':
                opus_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.opus"), recursive=True)
                if opus_files:
                    print("Conversion in progress ...")
                    for opus_file in opus_files:
                        ogg_file = os.path.splitext(opus_file)[0] + '.ogg'
                        try:
                            stream = ffmpeg.input(opus_file)
                            stream = ffmpeg.output(stream, ogg_file, acodec='libvorbis', map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                            print("Conversion OK")
                            show_success_message()
                        except ffmpeg.Error as e:
                            QMessageBox.critical(None, "Error", f"Failed to convert {opus_file}: {e.stderr}")
                            return
                        encov = "ogg"
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
        elif self.convert_audio_choice == 'opus to m4a':
                opus_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.opus"), recursive=True)
                if opus_files:
                    print("Conversion in progress ...")
                    for opus_file in opus_files:
                        m4a_file = os.path.splitext(opus_file)[0] + '.m4a'
                        try:
                            stream = ffmpeg.input(opus_file)
                            stream = ffmpeg.output(stream, m4a_file, acodec='alac', map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                            print("Conversion OK")
                            show_success_message()
                        except ffmpeg.Error as e:
                            QMessageBox.critical(None, "Error", f"Failed to convert {opus_file}: {e.stderr}")
                            return
                        encov = "m4a"
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
        elif self.convert_audio_choice == 'opus to aac':
                opus_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.opus"), recursive=True)
                if opus_files:
                    print("Conversion in progress ...")
                    for opus_file in opus_files:
                        aac_file = os.path.splitext(opus_file)[0] + '.aac'
                        try:
                            stream = ffmpeg.input(opus_file)
                            stream = ffmpeg.output(stream, aac_file, acodec='aac', map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                            print("Conversion OK")
                            show_success_message()
                        except ffmpeg.Error as e:
                            QMessageBox.critical(None, "Error", f"Failed to convert {opus_file}: {e.stderr}")
                            return
                        encov = "aac"
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
        elif self.convert_audio_choice == 'm4a to wav':
                m4a_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.m4a"), recursive=True)
                if m4a_files:
                    print("Conversion in progress ...")
                    for m4a_file in m4a_files:
                        wav_file = os.path.splitext(m4a_file)[0] + '.wav'
                        try:
                            stream = ffmpeg.input(m4a_file)
                            stream = ffmpeg.output(stream, wav_file, map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                            print("Conversion OK")
                            show_success_message()
                        except ffmpeg.Error as e:
                            QMessageBox.critical(None, "Error", f"Failed to convert {m4a_file}: {e.stderr}")
                            return
                        encov = "m4a"
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
        elif self.convert_audio_choice == 'm4a to ac3':
                m4a_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.m4a"), recursive=True)
                if m4a_files:
                    print("Conversion in progress ...")
                    for m4a_file in m4a_files:
                        ac3_file = os.path.splitext(m4a_file)[0] + '.ac3'
                        try:
                            stream = ffmpeg.input(m4a_file)
                            stream = ffmpeg.output(stream, ac3_file, acodec='ac3', map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                            print("Conversion OK")
                            show_success_message()
                        except ffmpeg.Error as e:
                            QMessageBox.critical(None, "Error", f"Failed to convert {m4a_file}: {e.stderr}")
                            return
                        encov = "ac3"
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
        elif self.convert_audio_choice == 'm4a to mp3':
                m4a_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.m4a"), recursive=True)
                if m4a_files:
                    print("Conversion in progress ...")
                    for m4a_file in m4a_files:
                        mp3_file = os.path.splitext(m4a_file)[0] + '.mp3'
                        try:
                            stream = ffmpeg.input(m4a_file)
                            stream = ffmpeg.output(stream, mp3_file, acodec='libmp3lame', map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                            print("Conversion OK")
                            show_success_message()
                        except ffmpeg.Error as e:
                            QMessageBox.critical(None, "Error", f"Failed to convert {m4a_file}: {e.stderr}")
                            return
                        encov = "m4a"
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
        elif self.convert_audio_choice == 'm4a to ogg':
                m4a_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.m4a"), recursive=True)
                if m4a_files:
                    print("Conversion in progress ...")
                    for m4a_file in m4a_files:
                        ogg_file = os.path.splitext(m4a_file)[0] + '.ogg'
                        try:
                            stream = ffmpeg.input(m4a_file)
                            stream = ffmpeg.output(stream, ogg_file, acodec='libvorbis', map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                            print("Conversion OK")
                            show_success_message()
                        except ffmpeg.Error as e:
                            QMessageBox.critical(None, "Error", f"Failed to convert {m4a_file}: {e.stderr}")
                            return
                        encov = "ogg"
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
        elif self.convert_audio_choice == 'm4a to opus':
                m4a_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.m4a"), recursive=True)
                if m4a_files:
                    print("Conversion in progress ...")
                    for m4a_file in m4a_files:
                        opus_file = os.path.splitext(m4a_file)[0] + '.opus'
                        try:
                            stream = ffmpeg.input(m4a_file)
                            stream = ffmpeg.output(stream, opus_file, acodec='libopus', map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                            print("Conversion OK")
                            show_success_message()
                        except ffmpeg.Error as e:
                            QMessageBox.critical(None, "Error", f"Failed to convert {m4a_file}: {e.stderr}")
                            return
                        encov = "opus"
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
        elif self.convert_audio_choice == 'm4a to aac':
                m4a_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.m4a"), recursive=True)
                if m4a_files:
                    print("Conversion in progress ...")
                    for m4a_file in m4a_files:
                        aac_file = os.path.splitext(m4a_file)[0] + '.aac'
                        try:
                            stream = ffmpeg.input(m4a_file)
                            stream = ffmpeg.output(stream, aac_file, acodec='aac', map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                            print("Conversion OK")
                            show_success_message()
                        except ffmpeg.Error as e:
                            QMessageBox.critical(None, "Error", f"Failed to convert {m4a_file}: {e.stderr}")
                            return
                        encov = "aac"
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
        else:
            QMessageBox.critical(None, "Error", "An unexpected error has occurred") 

class VideoTab(QWidget):
    def __init__(self):
        super().__init__()

        label = QLabel("Video content", self)
        label.move(20, 20)

        self.initUI()

    def initUI(self):
        self.path_label = QLabel(self)
        self.path_label.setText('Chose directory (its store your(s) file(s) to convert):')
        self.path_label.move(50, 50)

        self.path_input = QLineEdit(self)
        self.path_input.move(430, 50)
        self.path_input.resize(300, 30)
        self.path_input.text()

        self.choose_path_button = QPushButton('Choose Folder', self)
        self.choose_path_button.move(730, 50)
        self.choose_path_button.clicked.connect(self.choose_folder)
        self.convertvideo_choice = QComboBox(self)
        self.convertvideo_choice.addItem('Please choose')
        self.convertvideo_choice.addItems(['mkv to avi', 'mkv to mov', 'mkv to mp4', 'mkv to webm', 'mkv to flv', 'mkv to hevc',
                                   'mp4 to mkv', 'mp4 to mov', 'mp4 to avi', 'mp4 to webm', 'mp4 to flv', 'mp4 to hevc',
                                   'mov to mkv', 'mov to mp4', 'mov to avi', 'mov to webm', 'mov to flv', 'mov to hevc',
                                   'avi to mkv', 'avi to mp4', 'avi to mov', 'avi to webm', 'avi to flv', 'avi to hevc',
                                   'webm to avi', 'webm to mkv', 'webm to mov', 'webm to mp4', 'webm to flv', 'webm to hevc',
                                   'hevc to avi', 'hevc to mkv', 'hevc to mov', 'hevc to mp4', 'hevc to flv', 'hevc to webm',
                                   'flv to avi', 'flv to mkv', 'flv to mov', 'flv to mp4', 'flv to hevc', 'flv to webm'])
        self.convertvideo_choice.move(250, 200)
        self.convertvideo_choice.resize(200, 30)
        self.convertvideo_choice.setMaxVisibleItems(5)
        self.convertvideo_choice.setEditable(True)
        self.convertvideo_choice.view().setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.convertvideo_choice.currentIndexChanged.connect(self.setVideoOption)
        
        self.convertvideo_button = QPushButton('Convert', self)
        self.convertvideo_button.move(300, 350)
        self.convertvideo_button.clicked.connect(self.convertvideo)

    def choose_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self, 'Choose Folder')
        self.path_input.setText(folder_path)

    def setVideoOption(self, index):
        self.convertuniquementvideo_choice = self.convertvideo_choice.itemText(index)

    def convertvideo(self):
            if self.convertuniquementvideo_choice == 'mkv to avi':
                mkv_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.mkv"), recursive=True)
                if mkv_files:
                    print("Conversion in progress ...")
                    for mkv_file in mkv_files:
                        avi_file = os.path.splitext(mkv_file)[0] + '.avi'
                        try:
                            stream = ffmpeg.input(mkv_file)
                            stream = ffmpeg.output(stream, avi_file, vcodec='libx264', acodec='aac', map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                            print("Conversion OK")
                            show_success_message()
                        except ffmpeg.Error as e:
                            QMessageBox.critical(None, "Error", f"Failed to convert {mkv_file}: {e.stderr}")
                            return
                        encov = "avi"
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
            elif self.convertuniquementvideo_choice == 'mkv to mov':  # mkv to mov
                mkv_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.mkv"), recursive=True)
                if mkv_files:
                    print("Conversion in progress ...")
                    for mkv_file in mkv_files:
                        mov_file = os.path.splitext(mkv_file)[0] + '.mov'
                        try:
                            stream = ffmpeg.input(mkv_file)
                            stream = ffmpeg.output(stream, mov_file, vcodec='libx264', acodec='aac', map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                            print("Conversion OK")
                            show_success_message()
                        except ffmpeg.Error as e:
                            QMessageBox.critical(None, "Error", f"Failed to convert {mkv_file}: {e.stderr}")
                            return
                        encov = "mov"
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
            elif self.convertuniquementvideo_choice == 'mkv to mp4':  # mkv to mp4
                mkv_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.mkv"), recursive=True)
                if mkv_files:
                    print("Conversion in progress ...")
                    for mkv_file in mkv_files:
                        mp4_file = os.path.splitext(mkv_file)[0] + '.mp4'
                        try:
                            stream = ffmpeg.input(mkv_file)
                            stream = ffmpeg.output(stream, mp4_file, vcodec='libx264', acodec='aac', map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                            print("Conversion OK")
                            show_success_message()
                        except ffmpeg.Error as e:
                            QMessageBox.critical(None, "Error", f"Failed to convert {mkv_file}: {e.stderr}")
                            return
                        encov = "mp4"
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
            elif self.convertuniquementvideo_choice == 'mkv to webm':  # mkv to webm
                mkv_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.mkv"), recursive=True)
                if mkv_files:
                    print("Conversion in progress ...")
                    for mkv_file in mkv_files:
                        webm_file = os.path.splitext(mkv_file)[0] + '.webm'
                        try:
                            stream = ffmpeg.input(mkv_file)
                            stream = ffmpeg.output(stream, webm_file, vcodec='libvpx', acodec='libvorbis', map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                            print("Conversion OK")
                            show_success_message()
                        except ffmpeg.Error as e:
                            QMessageBox.critical(None, "Error", f"Failed to convert {mkv_file}: {e.stderr}")
                            return
                        encov = "webm"
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
            elif self.convertuniquementvideo_choice == 'mkv to flv':  # mkv to flv
                mkv_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.mkv"), recursive=True)
                if mkv_files:
                    print("Conversion in progress ...")
                    for mkv_file in mkv_files:
                        flv_file = os.path.splitext(mkv_file)[0] + '.flv'
                        try:
                            stream = ffmpeg.input(mkv_file)
                            stream = ffmpeg.output(stream, flv_file, vcodec='flv', acodec='libmp3lame', map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                            print("Conversion OK")
                            show_success_message()
                        except ffmpeg.Error as e:
                            QMessageBox.critical(None, "Error", f"Failed to convert {mkv_file}: {e.stderr}")
                            return
                        encov = "flv"
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
            elif self.convertuniquementvideo_choice == 'mkv to hevc':  # mkv to hevc
                mkv_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.mkv"), recursive=True)
                if mkv_files:
                    print("Conversion in progress ...")
                    for mkv_file in mkv_files:
                        hevc_file = os.path.splitext(mkv_file)[0] + '.hevc'
                        try:
                            stream = ffmpeg.input(mkv_file)
                            stream = ffmpeg.output(stream, hevc_file, vcodec='libx265', acodec='copy', map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                            print("Conversion OK")
                            show_success_message()
                        except ffmpeg.Error as e:
                            QMessageBox.critical(None, "Error", f"Failed to convert {mkv_file}: {e.stderr}")
                            return
                        encov = "hevc"
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return       
            elif self.convertuniquementvideo_choice == 'mp4 to mkv ':    #mp4 to mkv 
                mp4_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.mp4"), recursive=True)
                if mp4_files:
                    print("Conversion in progress ...")
                    for mp4_file in mp4_files:
                        mkv_file = os.path.splitext(mp4_file)[0] + '.mkv'
                        try:
                            stream = ffmpeg.input(mp4_file)
                            stream = ffmpeg.output(stream, mkv_file, vcodec='copy', acodec='copy', map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                            print("Conversion OK")
                            show_success_message()
                        except ffmpeg.Error as e:
                            QMessageBox.critical(None, "Error", f"Failed to convert {mp4_file}: {e.stderr}")
                            return
                        encov = "mkv"
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
            elif self.convertuniquementvideo_choice == 'mp4 to mov':    #mp4 to mov 
                mp4_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.mkv"), recursive=True)
                if mp4_files:
                    print("Conversion in progress ...")
                    for mp4_file in mp4_files:
                        mov_file = os.path.splitext(mp4_file)[0] + '.mov'
                        try:
                            stream = ffmpeg.input(mp4_file)
                            stream = ffmpeg.output(stream, mov_file, vcodec='libx264', acodec='aac', map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                            print("Conversion OK")
                            show_success_message()
                        except ffmpeg.Error as e:
                            QMessageBox.critical(None, "Error", f"Failed to convert {mp4_file}: {e.stderr}")
                            return
                        encov = "mov"
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
            elif self.convertuniquementvideo_choice == 'mp4 to avi':    #mp4 to avi 
                mp4_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.mkv"), recursive=True)
                if mp4_files:
                    print("Conversion in progress ...")
                    for mp4_file in mp4_files:
                        avi_file = os.path.splitext(mp4_file)[0] + '.avi'
                        try:
                            stream = ffmpeg.input(mp4_file)
                            stream = ffmpeg.output(stream, avi_file, vcodec='libx264', acodec='aac', map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                            print("Conversion OK")
                            show_success_message()
                        except ffmpeg.Error as e:
                            QMessageBox.critical(None, "Error", f"Failed to convert {mp4_file}: {e.stderr}")
                            return
                        encov = "avi"
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
            elif self.convertuniquementvideo_choice == 'mp4 to webm':    #mp4 to webm 
                mp4_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.mp4"), recursive=True)
                if mp4_files:
                    print("Conversion in progress ...")
                    for mp4_file in mp4_files:
                        webm_file = os.path.splitext(mp4_file)[0] + '.webm'
                        try:
                            stream = ffmpeg.input(mp4_file)
                            stream = ffmpeg.output(stream, webm_file, vcodec='libvpx', acodec='libvorbis', map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                            print("Conversion OK")
                            show_success_message()
                        except ffmpeg.Error as e:
                            QMessageBox.critical(None, "Error", f"Failed to convert {mp4_file}: {e.stderr}")
                            return
                        encov = "webm"
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return       
            elif self.convertuniquementvideo_choice == 'mp4 to flv':    #mp4 to flv 
                mp4_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.mp4"), recursive=True)
                if mp4_files:
                    print("Conversion in progress ...")
                    for mp4_file in mp4_files:
                        flv_file = os.path.splitext(mp4_file)[0] + '.flv'
                        try:
                            stream = ffmpeg.input(mp4_file)
                            stream = ffmpeg.output(stream, flv_file, vcodec='flv', acodec='libmp3lame', map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                            print("Conversion OK")
                            show_success_message()
                            exit
                        except ffmpeg.Error as e:
                            QMessageBox.critical(None, "Error", f"Failed to convert {mp4_file}: {e.stderr}")
                            return
                        encov = "flv"
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return         
            elif self.convertuniquementvideo_choice == 'mp4 to hevc':    #mp4 to hevc 
                mp4_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.mp4"), recursive=True)
                if mp4_files:
                    print("Conversion in progress ...")
                    for mp4_file in mp4_files:
                        hevc_file = os.path.splitext(mp4_file)[0] + '.hevc'
                        try:
                            stream = ffmpeg.input(mp4_file)
                            stream = ffmpeg.output(stream, hevc_file, vcodec='libx265', acodec='copy', map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                            print("Conversion OK")
                            show_success_message()
                        except ffmpeg.Error as e:
                            QMessageBox.critical(None, "Error", f"Failed to convert {mp4_file}: {e.stderr}")
                            return
                        encov = "hevc"
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
            elif self.convertuniquementvideo_choice == 'mov to mkv':    #mov to mkv 
                mov_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.mov"), recursive=True)
                if mov_files:
                    print("Conversion in progress ...")
                    for mov_file in mov_files:
                        mkv_file = os.path.splitext(mov_file)[0] + '.mkv'
                        try:
                            stream = ffmpeg.input(mov_file)
                            stream = ffmpeg.output(stream, mkv_file, vcodec='copy', acodec='copy', map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                            print("Conversion OK")
                            show_success_message()
                        except ffmpeg.Error as e:
                            QMessageBox.critical(None, "Error", f"Failed to convert {mov_file}: {e.stderr}")
                            return
                        encov = "mkv"
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
            elif self.convertuniquementvideo_choice == 'mov to mp4':    #mov to mp4 
                mov_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.mp4"), recursive=True)
                if mov_files:
                    print("Conversion in progress ...")
                    for mov_file in mov_files:
                        mp4_file = os.path.splitext(mov_file)[0] + '.mp4'
                        try:
                            stream = ffmpeg.input(mov_file)
                            stream = ffmpeg.output(stream, mp4_file, vcodec='libx264', acodec='aac', map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                            print("Conversion OK")
                            show_success_message()
                        except ffmpeg.Error as e:
                            QMessageBox.critical(None, "Error", f"Failed to convert {mov_file}: {e.stderr}")
                            return
                        encov = "mp4"
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
            elif self.convertuniquementvideo_choice == 'mov to avi':    #mov to avi 
                mov_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.mkv"), recursive=True)
                if mov_files:
                    print("Conversion in progress ...")
                    for mov_file in mov_files:
                        avi_file = os.path.splitext(mov_file)[0] + '.avi'
                        try:
                            stream = ffmpeg.input(mov_file)
                            stream = ffmpeg.output(stream, avi_file, vcodec='libx264', acodec='aac', map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                            print("Conversion OK")
                            show_success_message()
                        except ffmpeg.Error as e:
                            QMessageBox.critical(None, "Error", f"Failed to convert {mov_file}: {e.stderr}")
                            return
                        encov = "avi"
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
            elif self.convertuniquementvideo_choice == 'mov to webm':    #mov to webm 
                mov_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.mov"), recursive=True)
                if mov_files:
                    print("Conversion in progress ...")
                    for mov_file in mov_files:
                        webm_file = os.path.splitext(mov_file)[0] + '.webm'
                        try:
                            stream = ffmpeg.input(mov_file)
                            stream = ffmpeg.output(stream, webm_file, vcodec='libvpx', acodec='libvorbis', map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                            print("Conversion OK")
                            show_success_message()
                        except ffmpeg.Error as e:
                            QMessageBox.critical(None, "Error", f"Failed to convert {mov_file}: {e.stderr}")
                            return
                        encov = "webm"
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return          
            elif self.convertuniquementvideo_choice == 'mov to flv':    #mov to flv 
                mov_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.mov"), recursive=True)
                if mov_files:
                    print("Conversion in progress ...")
                    for mov_file in mov_files:
                        flv_file = os.path.splitext(mov_file)[0] + '.flv'
                        try:
                            stream = ffmpeg.input(mov_file)
                            stream = ffmpeg.output(stream, flv_file, vcodec='flv', acodec='libmp3lame', map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                            print("Conversion OK")
                            show_success_message()
                        except ffmpeg.Error as e:
                            QMessageBox.critical(None, "Error", f"Failed to convert {mov_file}: {e.stderr}")
                            return
                        encov = "flv"
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return          
            elif self.convertuniquementvideo_choice == 'mov to hevc':    #mov to hevc 
                mov_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.mov"), recursive=True)
                if mov_files:
                    print("Conversion in progress ...")
                    for mov_file in mov_files:
                        hevc_file = os.path.splitext(mov_file)[0] + '.hevc'
                        try:
                            stream = ffmpeg.input(mov_file)
                            stream = ffmpeg.output(stream, hevc_file, vcodec='libx265', acodec='copy', map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                            print("Conversion OK")
                            show_success_message()
                        except ffmpeg.Error as e:
                            QMessageBox.critical(None, "Error", f"Failed to convert {mov_file}: {e.stderr}")
                            return
                        encov = "hevc"
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
            elif self.convertuniquementvideo_choice == 'avi to mkv':    #avi to mkv 
                avi_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.avi"), recursive=True)
                if avi_files:
                    print("Conversion in progress ...")
                    for avi_file in avi_files:
                        mkv_file = os.path.splitext(avi_file)[0] + '.mkv'
                        try:
                            stream = ffmpeg.input(avi_file)
                            stream = ffmpeg.output(stream, mkv_file, vcodec='copy', acodec='copy', map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                            print("Conversion OK")
                            show_success_message()
                        except ffmpeg.Error as e:
                            QMessageBox.critical(None, "Error", f"Failed to convert {avi_file}: {e.stderr}")
                            return
                        encov = "mkv"
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
            elif self.convertuniquementvideo_choice == 'avi to mp4':    #avi to mp4 
                avi_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.mp4"), recursive=True)
                if avi_files:
                    print("Conversion in progress ...")
                    for avi_file in avi_files:
                        mp4_file = os.path.splitext(avi_file)[0] + '.mp4'
                        try:
                            stream = ffmpeg.input(avi_file)
                            stream = ffmpeg.output(stream, mp4_file, vcodec='libx264', acodec='aac', map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                            print("Conversion OK")
                            show_success_message()
                        except ffmpeg.Error as e:
                            QMessageBox.critical(None, "Error", f"Failed to convert {avi_file}: {e.stderr}")
                            return
                        encov = "mp4"
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
            elif self.convertuniquementvideo_choice == 'avi to mov':    #avi to mov 
                avi_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.mkv"), recursive=True)
                if avi_files:
                    print("Conversion in progress ...")
                    for avi_file in avi_files:
                        mov_file = os.path.splitext(avi_file)[0] + '.mov'
                        try:
                            stream = ffmpeg.input(avi_file)
                            stream = ffmpeg.output(stream, mov_file, vcodec='libx264', acodec='aac', map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                            print("Conversion OK")
                            show_success_message()
                        except ffmpeg.Error as e:
                            QMessageBox.critical(None, "Error", f"Failed to convert {avi_file}: {e.stderr}")
                            return
                        encov = "mov"
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
            elif self.convertuniquementvideo_choice == 'avi to webm':    #avi to webm 
                avi_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.avi"), recursive=True)
                if avi_files:
                    print("Conversion in progress ...")
                    for avi_file in avi_files:
                        webm_file = os.path.splitext(avi_file)[0] + '.webm'
                        try:
                            stream = ffmpeg.input(avi_file)
                            stream = ffmpeg.output(stream, webm_file, vcodec='libvpx', acodec='libvorbis', map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                            print("Conversion OK")
                            show_success_message()
                        except ffmpeg.Error as e:
                            QMessageBox.critical(None, "Error", f"Failed to convert {avi_file}: {e.stderr}")
                            return
                        encov = "webm"
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return         
            elif self.convertuniquementvideo_choice == 'avi to flv':    #avi to flv 
                avi_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.avi"), recursive=True)
                if avi_files:
                    print("Conversion in progress ...")
                    for avi_file in avi_files:
                        flv_file = os.path.splitext(avi_file)[0] + '.flv'
                        try:
                            stream = ffmpeg.input(avi_file)
                            stream = ffmpeg.output(stream, flv_file, vcodec='flv', acodec='libmp3lame', map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                            print("Conversion OK")
                            show_success_message()
                        except ffmpeg.Error as e:
                            QMessageBox.critical(None, "Error", f"Failed to convert {avi_file}: {e.stderr}")
                            return
                        encov = "flv"
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return         
            elif self.convertuniquementvideo_choice == 'avi to hevc':    #avi to hevc 
                avi_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.avi"), recursive=True)
                if avi_files:
                    print("Conversion in progress ...")
                    for avi_file in avi_files:
                        hevc_file = os.path.splitext(avi_file)[0] + '.hevc'
                        try:
                            stream = ffmpeg.input(avi_file)
                            stream = ffmpeg.output(stream, hevc_file, vcodec='libx265', acodec='copy', map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                            print("Conversion OK")
                            show_success_message()
                        except ffmpeg.Error as e:
                            QMessageBox.critical(None, "Error", f"Failed to convert {avi_file}: {e.stderr}")
                            return
                        encov = "hevc"
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
            elif self.convertuniquementvideo_choice == 'webm to avi':    #webm to avi 
                webm_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.mkv"), recursive=True)
                if webm_files:
                    print("Conversion in progress ...")
                    for webm_file in webm_files:
                        avi_file = os.path.splitext(webm_file)[0] + '.avi'
                        try:
                            stream = ffmpeg.input(webm_file)
                            stream = ffmpeg.output(stream, avi_file, vcodec='libx264', acodec='aac', map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                            print("Conversion OK")
                            show_success_message()
                        except ffmpeg.Error as e:
                            QMessageBox.critical(None, "Error", f"Failed to convert {webm_file}: {e.stderr}")
                            return
                        encov = "avi"
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
            elif self.convertuniquementvideo_choice == 'webm to mkv':    #webm to mkv 
                webm_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.webm"), recursive=True)
                if webm_files:
                    print("Conversion in progress ...")
                    for webm_file in webm_files:
                        mkv_file = os.path.splitext(webm_file)[0] + '.mkv'
                        try:
                            stream = ffmpeg.input(webm_file)
                            stream = ffmpeg.output(stream, mkv_file, vcodec='copy', acodec='copy', map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                            print("Conversion OK")
                            show_success_message()
                        except ffmpeg.Error as e:
                            QMessageBox.critical(None, "Error", f"Failed to convert {webm_file}: {e.stderr}")
                            return
                        encov = "hevc"
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
            elif self.convertuniquementvideo_choice == 'webm to mov':    #webm to mov 
                webm_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.mkv"), recursive=True)
                if webm_files:
                    print("Conversion in progress ...")
                    for webm_file in webm_files:
                        mov_file = os.path.splitext(webm_file)[0] + '.mov'
                        try:
                            stream = ffmpeg.input(webm_file)
                            stream = ffmpeg.output(stream, mov_file, vcodec='libx264', acodec='aac', map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                            print("Conversion OK")
                            show_success_message()
                        except ffmpeg.Error as e:
                            QMessageBox.critical(None, "Error", f"Failed to convert {webm_file}: {e.stderr}")
                            return
                        encov = "mov"
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
            elif self.convertuniquementvideo_choice == 'webm to mp4':    #webm to mp4 
                webm_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.mp4"), recursive=True)
                if webm_files:
                    print("Conversion in progress ...")
                    for webm_file in webm_files:
                        mp4_file = os.path.splitext(webm_file)[0] + '.mp4'
                        try:
                            stream = ffmpeg.input(webm_file)
                            stream = ffmpeg.output(stream, mp4_file, vcodec='libx264', acodec='aac', map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                            print("Conversion OK")
                            show_success_message()
                        except ffmpeg.Error as e:
                            QMessageBox.critical(None, "Error", f"Failed to convert {webm_file}: {e.stderr}")
                            return
                        encov = "mp4"
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return     
            elif self.convertuniquementvideo_choice == 'webm to flv':    #webm to flv 
                webm_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.webm"), recursive=True)
                if webm_files:
                    print("Conversion in progress ...")
                    for webm_file in webm_files:
                        flv_file = os.path.splitext(webm_file)[0] + '.flv'
                        try:
                            stream = ffmpeg.input(webm_file)
                            stream = ffmpeg.output(stream, flv_file, vcodec='flv', acodec='libmp3lame', map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                            print("Conversion OK")
                            show_success_message()
                        except ffmpeg.Error as e:
                            QMessageBox.critical(None, "Error", f"Failed to convert {webm_file}: {e.stderr}")
                            return
                        encov = "flv"
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return           
            elif self.convertuniquementvideo_choice == 'webm to hevc':    #webm to hevc 
                webm_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.webm"), recursive=True)
                if webm_files:
                    print("Conversion in progress ...")
                    for webm_file in webm_files:
                        hevc_file = os.path.splitext(webm_file)[0] + '.hevc'
                        try:
                            stream = ffmpeg.input(webm_file)
                            stream = ffmpeg.output(stream, hevc_file, vcodec='libx265', acodec='copy', map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                            print("Conversion OK")
                            show_success_message()
                        except ffmpeg.Error as e:
                            QMessageBox.critical(None, "Error", f"Failed to convert {webm_file}: {e.stderr}")
                            return
                        encov = "hevc"
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
            elif self.convertuniquementvideo_choice == 'hevc to avi':    #hevc to avi 
                hevc_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.mkv"), recursive=True)
                if hevc_files:
                    print("Conversion in progress ...")
                    for hevc_file in hevc_files:
                        avi_file = os.path.splitext(hevc_file)[0] + '.avi'
                        try:
                            stream = ffmpeg.input(hevc_file)
                            stream = ffmpeg.output(stream, avi_file, vcodec='libx264', acodec='aac', map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                            print("Conversion OK")
                            show_success_message()
                        except ffmpeg.Error as e:
                            QMessageBox.critical(None, "Error", f"Failed to convert {hevc_file}: {e.stderr}")
                            return
                        encov = "avi"
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
            elif self.convertuniquementvideo_choice == 'hevc to mkv':    #hevc to mkv 
                hevc_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.hevc"), recursive=True)
                if hevc_files:
                    print("Conversion in progress ...")
                    for hevc_file in hevc_files:
                        mkv_file = os.path.splitext(hevc_file)[0] + '.mkv'
                        try:
                            stream = ffmpeg.input(hevc_file)
                            stream = ffmpeg.output(stream, mkv_file, vcodec='copy', acodec='copy', map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                            print("Conversion OK")
                            show_success_message()
                        except ffmpeg.Error as e:
                            QMessageBox.critical(None, "Error", f"Failed to convert {hevc_file}: {e.stderr}")
                            return
                        encov = "hevc"
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
            elif self.convertuniquementvideo_choice == 'hevc to mov':    #hevc to mov 
                hevc_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.mkv"), recursive=True)
                if hevc_files:
                    print("Conversion in progress ...")
                    for hevc_file in hevc_files:
                        mov_file = os.path.splitext(hevc_file)[0] + '.mov'
                        try:
                            stream = ffmpeg.input(hevc_file)
                            stream = ffmpeg.output(stream, mov_file, vcodec='libx264', acodec='aac', map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                            print("Conversion OK")
                            show_success_message()
                        except ffmpeg.Error as e:
                            QMessageBox.critical(None, "Error", f"Failed to convert {hevc_file}: {e.stderr}")
                            return
                        encov = "mov"
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
            elif self.convertuniquementvideo_choice == 'hevc to mp4':    #hevc to mp4 
                hevc_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.mp4"), recursive=True)
                if hevc_files:
                    print("Conversion in progress ...")
                    for hevc_file in hevc_files:
                        mp4_file = os.path.splitext(hevc_file)[0] + '.mp4'
                        try:
                            stream = ffmpeg.input(hevc_file)
                            stream = ffmpeg.output(stream, mp4_file, vcodec='libx264', acodec='aac', map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                            print("Conversion OK")
                            show_success_message()
                        except ffmpeg.Error as e:
                            QMessageBox.critical(None, "Error", f"Failed to convert {hevc_file}: {e.stderr}")
                            return
                        encov = "mp4"
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return        
            elif self.convertuniquementvideo_choice == 'hevc to flv':    #hevc to flv 
                hevc_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.hevc"), recursive=True)
                if hevc_files:
                    print("Conversion in progress ...")
                    for hevc_file in hevc_files:
                        flv_file = os.path.splitext(hevc_file)[0] + '.flv'
                        try:
                            stream = ffmpeg.input(hevc_file)
                            stream = ffmpeg.output(stream, flv_file, vcodec='flv', acodec='libmp3lame', map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                            print("Conversion OK")
                            show_success_message()
                        except ffmpeg.Error as e:
                            QMessageBox.critical(None, "Error", f"Failed to convert {hevc_file}: {e.stderr}")
                            return
                        encov = "flv"
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return          
            elif self.convertuniquementvideo_choice == 'hevc to webm':    #hevc to webm 
                hevc_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.hevc"), recursive=True)
                if hevc_files:
                    print("Conversion in progress ...")
                    for hevc_file in hevc_files:
                        webm_file = os.path.splitext(hevc_file)[0] + '.webm'
                        try:
                            stream = ffmpeg.input(hevc_file)
                            stream = ffmpeg.output(stream, webm_file, vcodec='libvpx', acodec='libvorbis', map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                            print("Conversion OK")
                            show_success_message()
                        except ffmpeg.Error as e:
                            QMessageBox.critical(None, "Error", f"Failed to convert {hevc_file}: {e.stderr}")
                            return
                        encov = "webm"
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return 
            elif self.convertuniquementvideo_choice == 'flv to avi':    #flv to avi 
                flv_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.mkv"), recursive=True)
                if flv_files:
                    print("Conversion in progress ...")
                    for flv_file in flv_files:
                        avi_file = os.path.splitext(flv_file)[0] + '.avi'
                        try:
                            stream = ffmpeg.input(flv_file)
                            stream = ffmpeg.output(stream, avi_file, vcodec='libx264', acodec='aac', map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                            print("Conversion OK")
                            show_success_message()
                        except ffmpeg.Error as e:
                            QMessageBox.critical(None, "Error", f"Failed to convert {flv_file}: {e.stderr}")
                            return
                        encov = "avi"
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
            elif self.convertuniquementvideo_choice == 'flv to mkv':    #flv to mkv 
                flv_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.flv"), recursive=True)
                if flv_files:
                    print("Conversion in progress ...")
                    for flv_file in flv_files:
                        mkv_file = os.path.splitext(flv_file)[0] + '.mkv'
                        try:
                            stream = ffmpeg.input(flv_file)
                            stream = ffmpeg.output(stream, mkv_file, vcodec='copy', acodec='copy', map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                            print("Conversion OK")
                            show_success_message()
                        except ffmpeg.Error as e:
                            QMessageBox.critical(None, "Error", f"Failed to convert {flv_file}: {e.stderr}")
                            return
                        encov = "flv"
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
            elif self.convertuniquementvideo_choice == 'flv to mov':    #flv to mov 
                flv_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.mkv"), recursive=True)
                if flv_files:
                    print("Conversion in progress ...")
                    for flv_file in flv_files:
                        mov_file = os.path.splitext(flv_file)[0] + '.mov'
                        try:
                            stream = ffmpeg.input(flv_file)
                            stream = ffmpeg.output(stream, mov_file, vcodec='libx264', acodec='aac', map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                            print("Conversion OK")
                            show_success_message()
                        except ffmpeg.Error as e:
                            QMessageBox.critical(None, "Error", f"Failed to convert {flv_file}: {e.stderr}")
                            return
                        encov = "mov"
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
            elif self.convertuniquementvideo_choice == 'flv to mp4':    #flv to mp4 
                flv_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.mp4"), recursive=True)
                if flv_files:
                    print("Conversion in progress ...")
                    for flv_file in flv_files:
                        mp4_file = os.path.splitext(flv_file)[0] + '.mp4'
                        try:
                            stream = ffmpeg.input(flv_file)
                            stream = ffmpeg.output(stream, mp4_file, vcodec='libx264', acodec='aac', map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                            print("Conversion OK")
                            show_success_message()
                        except ffmpeg.Error as e:
                            QMessageBox.critical(None, "Error", f"Failed to convert {flv_file}: {e.stderr}")
                            return
                        encov = "mp4"
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return          
            elif self.convertuniquementvideo_choice == 'flv to hevc':    #flv to hevc 
                flv_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.flv"), recursive=True)
                if flv_files:
                    print("Conversion in progress ...")
                    for flv_file in flv_files:
                        hevc_file = os.path.splitext(flv_file)[0] + '.hevc'
                        try:
                            stream = ffmpeg.input(flv_file)
                            stream = ffmpeg.output(stream, hevc_file, vcodec='libx265', acodec='copy', map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                            print("Conversion OK")
                            show_success_message()
                        except ffmpeg.Error as e:
                            QMessageBox.critical(None, "Error", f"Failed to convert {flv_file}: {e.stderr}")
                            return
                        encov = "hevc"
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return         
            elif self.convertuniquementvideo_choice == 'flv to webm':    #flv to webm 
                flv_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.flv"), recursive=True)
                if flv_files:
                    print("Conversion in progress ...")
                    for flv_file in flv_files:
                        webm_file = os.path.splitext(flv_file)[0] + '.webm'
                        try:
                            stream = ffmpeg.input(flv_file)
                            stream = ffmpeg.output(stream, webm_file, vcodec='libvpx', acodec='libvorbis', map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                            print("Conversion OK")
                            show_success_message()
                        except ffmpeg.Error as e:
                            QMessageBox.critical(None, "Error", f"Failed to convert {flv_file}: {e.stderr}")
                            return
                        encov = "webm"
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return 
            else:
                QMessageBox.critical(None, "Error", "An unexpected error has occurred")
class Subtitle(QWidget):
    def __init__(self):
        super().__init__()

        label = QLabel("Subtitle", self)
        label.move(20, 20)

        self.initUI()

    def initUI(self):
        self.path_label = QLabel(self)
        self.path_label.setText('Chose directory (its store your(s) file(s) to convert):')
        self.path_label.move(50, 50)

        self.path_input = QLineEdit(self)
        self.path_input.move(430, 50)
        self.path_input.resize(300, 30)
        self.path_input.text()

        self.choose_path_button = QPushButton('Choose Folder', self)
        self.choose_path_button.move(730, 50)
        self.choose_path_button.clicked.connect(self.choose_folder)
        self.convertsubtitle_choice = QComboBox(self)
        self.convertsubtitle_choice.addItem('Please choose')
        self.convertsubtitle_choice.addItems(['vtt to srt', 'vtt to ass', 'vtt to lrc', 'srt to vtt', 'srt to ass', 'srt to lrc', 
                                            'ass to srt', 'ass to lrc', 'ass to vtt', 'lrc to srt', 'lrc to ass', 'lrc to vtt'])
        self.convertsubtitle_choice.move(250, 200)
        self.convertsubtitle_choice.resize(200, 30)
        self.convertsubtitle_choice.setMaxVisibleItems(5)
        self.convertsubtitle_choice.setEditable(True)
        self.convertsubtitle_choice.view().setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.convertsubtitle_choice.currentIndexChanged.connect(self.setsubtitleOption)
        
        self.convertsubtitle_button = QPushButton('Convert', self)
        self.convertsubtitle_button.move(300, 350)
        self.convertsubtitle_button.clicked.connect(self.convertsubtitle)

    def choose_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self, 'Choose Folder')
        self.path_input.setText(folder_path)

    def setsubtitleOption(self, index):
        self.convert_subtitle_choice = self.convertsubtitle_choice.itemText(index)

    def convertsubtitle(self):
        if self.convert_subtitle_choice == 'vtt to srt':
                vtt_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.vtt"), recursive=True)
                if vtt_files:
                    print("Conversion in progress ...")
                    for vtt_file in vtt_files:
                        srt_file = os.path.splitext(vtt_file)[0] + '.srt'
                        try:
                            stream = ffmpeg.input(vtt_file)
                            stream = ffmpeg.output(stream, srt_file, map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                            print("Conversion OK")
                            show_success_message()
                        except ffmpeg.Error as e:
                            QMessageBox.critical(None, "Error", f"Failed to convert {vtt_file}: {e.stderr}")
                            return
                        encov = "srt"
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return 
        elif self.convert_subtitle_choice == 'vtt to ass':
                vtt_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.vtt"), recursive=True)
                if vtt_files:
                    print("Conversion in progress ...")
                    for vtt_file in vtt_files:
                        ass_file = os.path.splitext(vtt_file)[0] + '.ass'
                        try:
                            stream = ffmpeg.input(vtt_file)
                            stream = ffmpeg.output(stream, ass_file, map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                            print("Conversion OK")
                            show_success_message()
                        except ffmpeg.Error as e:
                            QMessageBox.critical(None, "Error", f"Failed to convert {vtt_file}: {e.stderr}")
                            return
                        encov = "ass"
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
        elif self.convert_subtitle_choice == 'vtt to lrc':
                vtt_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.vtt"), recursive=True)
                if vtt_files:
                    print("Conversion in progress ...")
                    for vtt_file in vtt_files:
                        lrc_file = os.path.splitext(vtt_file)[0] + '.lrc'
                        try:
                            stream = ffmpeg.input(vtt_file)
                            stream = ffmpeg.output(stream, lrc_file, map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                            print("Conversion OK")
                            show_success_message()
                        except ffmpeg.Error as e:
                            QMessageBox.critical(None, "Error", f"Failed to convert {vtt_file}: {e.stderr}")
                            return
                        encov = "lrc"
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return 
        elif self.convert_subtitle_choice == 'srt to vtt':
                srt_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.srt"), recursive=True)
                if srt_files:
                    print("Conversion in progress ...")
                    for srt_file in srt_files:
                        vtt_file = os.path.splitext(srt_file)[0] + '.vtt'
                        try:
                            stream = ffmpeg.input(srt_file)
                            stream = ffmpeg.output(stream, vtt_file, map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                            print("Conversion OK")
                            show_success_message()
                        except ffmpeg.Error as e:
                            QMessageBox.critical(None, "Error", f"Failed to convert {srt_file}: {e.stderr}")
                            return
                        encov = "vtt"
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
        elif self.convert_subtitle_choice == 'srt to ass':
                srt_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.srt"), recursive=True)
                if srt_files:
                    print("Conversion in progress ...")
                    for srt_file in srt_files:
                        ass_file = os.path.splitext(srt_file)[0] + '.ass'
                        try:
                            stream = ffmpeg.input(srt_file)
                            stream = ffmpeg.output(stream, ass_file, map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                            print("Conversion OK")
                            show_success_message()
                        except ffmpeg.Error as e:
                            QMessageBox.critical(None, "Error", f"Failed to convert {srt_file}: {e.stderr}")
                            return
                        encov = "ass"
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return 
        elif self.convert_subtitle_choice == 'srt to lrc':
                srt_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.srt"), recursive=True)
                if srt_files:
                    print("Conversion in progress ...")
                    for srt_file in srt_files:
                        lrc_file = os.path.splitext(srt_file)[0] + '.lrc'
                        try:
                            stream = ffmpeg.input(srt_file)
                            stream = ffmpeg.output(stream, lrc_file, map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                            print("Conversion OK")
                            show_success_message()
                        except ffmpeg.Error as e:
                            QMessageBox.critical(None, "Error", f"Failed to convert {srt_file}: {e.stderr}")
                            return
                        encov = "lrc"
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return 
        elif self.convert_subtitle_choice == 'ass to srt':
                ass_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.ass"), recursive=True)
                if ass_files:
                    print("Conversion in progress ...")
                    for ass_file in ass_files:
                        srt_file = os.path.splitext(ass_file)[0] + '.srt'
                        try:
                            stream = ffmpeg.input(ass_file)
                            stream = ffmpeg.output(stream, srt_file, map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                            print("Conversion OK")
                            show_success_message()
                        except ffmpeg.Error as e:
                            QMessageBox.critical(None, "Error", f"Failed to convert {ass_file}: {e.stderr}")
                            return
                        encov = "srt"
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
        elif self.convert_subtitle_choice == 'ass to lrc':
                ass_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.ass"), recursive=True)
                if ass_files:
                    print("Conversion in progress ...")
                    for ass_file in ass_files:
                        lrc_file = os.path.splitext(ass_file)[0] + '.lrc'
                        try:
                            stream = ffmpeg.input(ass_file)
                            stream = ffmpeg.output(stream, lrc_file, map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                            print("Conversion OK")
                            show_success_message()
                        except ffmpeg.Error as e:
                            QMessageBox.critical(None, "Error", f"Failed to convert {ass_file}: {e.stderr}")
                            return
                        encov = "lrc"
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
        elif self.convert_subtitle_choice == 'ass to vtt':
                ass_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.ass"), recursive=True)
                if ass_files:
                    print("Conversion in progress ...")
                    for ass_file in ass_files:
                        vtt_file = os.path.splitext(ass_file)[0] + '.vtt'
                        try:
                            stream = ffmpeg.input(ass_file)
                            stream = ffmpeg.output(stream, vtt_file, map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                            print("Conversion OK")
                            show_success_message()
                        except ffmpeg.Error as e:
                            QMessageBox.critical(None, "Error", f"Failed to convert {ass_file}: {e.stderr}")
                            return
                        encov = "vtt"
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return         
        elif self.convert_subtitle_choice == 'lrc to srt':
                lrc_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.lrc"), recursive=True)
                if lrc_files:
                    print("Conversion in progress ...")
                    for lrc_file in lrc_files:
                        srt_file = os.path.splitext(lrc_file)[0] + '.srt'
                        try:
                            stream = ffmpeg.input(lrc_file)
                            stream = ffmpeg.output(stream, srt_file, map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                            print("Conversion OK")
                            show_success_message()
                        except ffmpeg.Error as e:
                            QMessageBox.critical(None, "Error", f"Failed to convert {lrc_file}: {e.stderr}")
                            return
                        encov = "srt"
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return 
        if self.convert_subtitle_choice == 'lrc to ass':
                lrc_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.lrc"), recursive=True)
                if lrc_files:
                    print("Conversion in progress ...")
                    for lrc_file in lrc_files:
                        ass_file = os.path.splitext(lrc_file)[0] + '.ass'
                        try:
                            stream = ffmpeg.input(lrc_file)
                            stream = ffmpeg.output(stream, ass_file, map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                            print("Conversion OK")
                            show_success_message()
                        except ffmpeg.Error as e:
                            QMessageBox.critical(None, "Error", f"Failed to convert {lrc_file}: {e.stderr}")
                            return
                        encov = "ass"
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
        if self.convert_subtitle_choice == 'lrc to vtt':
                lrc_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.lrc"), recursive=True)
                if lrc_files:
                    print("Conversion in progress ...")
                    for lrc_file in lrc_files:
                        vtt_file = os.path.splitext(lrc_file)[0] + '.vtt'
                        try:
                            stream = ffmpeg.input(lrc_file)
                            stream = ffmpeg.output(stream, vtt_file, map_metadata=0)
                            ffmpeg.run(stream, quiet=True)
                            print("Conversion OK")
                            show_success_message()
                        except ffmpeg.Error as e:
                            QMessageBox.critical(None, "Error", f"Failed to convert {lrc_file}: {e.stderr}")
                            return
                        encov = "vtt"
                else:
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
        else:
            QMessageBox.critical(None, "Error", "An unexpected error has occurred")










class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Convertisso')

        screen_resolution = QDesktopWidget().screenGeometry()

        # Définir la taille et la position de la fenêtre en fonction de la résolution de l'écran
        self.setGeometry(0, 0, screen_resolution.width(), screen_resolution.height())

        layout = QVBoxLayout()

        self.tabs = QTabWidget(self)
        # Premier onglet
        self.downloader_tab = DownloaderTab()
        self.tabs.addTab(self.downloader_tab, "Downloader")
        # Deuxième onglet
        self.audio_tab = AudioTab()
        self.tabs.addTab(self.audio_tab, "Audio")
        # Troisième onglet
        self.video_tab = VideoTab()
        self.tabs.addTab(self.video_tab, "Video")
        self.video_tab = Subtitle()
        self.tabs.addTab(self.video_tab, "Subtitle")
        # Ajout du QTabWidget au layout
        layout.addWidget(self.tabs)
        # Création d'un widget principal pour contenir le layout
        main_widget = QWidget()
        main_widget.setLayout(layout)
        self.setCentralWidget(main_widget)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())
