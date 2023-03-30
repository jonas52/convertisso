import glob
import shutil
import sys
import os
import yt_dlp
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QComboBox, QFileDialog
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
        elif self.download_option == 'Video + Subtitles':
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
        elif self.download_option == 'Subtitles Only':
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
window = YoutubeDownloader()
window.show()
app.exec_()
