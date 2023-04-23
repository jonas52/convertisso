#!/usr/bin/env python3
# option pour sans ffmpeg avec yt_dlp --a faire
# ---------------- Import section ----------------
import os
import sys
import shutil
import glob
import yt_dlp
import ffmpeg
from PyQt5.QtCore import Qt, QTimer
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QTabWidget, QWidget, QLabel, QPushButton, QLineEdit, QComboBox, QFileDialog, QMessageBox, QMainWindow, QDesktopWidget, QVBoxLayout, QScrollBar, QProgressBar
from PyQt5.QtGui import QColor, QFont
import requests
from urllib import request
# ---------------- Print convertisso ----------------
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
        
convertisso() #print convertisso

# ---------------- Make pop-up for conversion succesful ----------------
def show_success_message():
    message_box = QMessageBox()
    message_box.setWindowTitle("Successful conversion")
    message_box.setText("The conversion was successful")
    message_box.setIcon(QMessageBox.Information)
    message_box.setStandardButtons(QMessageBox.Ok)
    message_box.exec_()
# ---------------- Make pop-up for download succesful ----------------
def show_download_success_message():
    message_box = QMessageBox()
    message_box.setWindowTitle("Successful download")
    message_box.setText("The download was successful.")
    message_box.setIcon(QMessageBox.Information)
    message_box.addButton(QMessageBox.Ok)
    message_box.exec_()
# ---------------- internet checker for convertisso downloader ----------------
def internet_check(host='https://google.com'):
    try:
        request.urlopen(host, timeout=4)
        return True
    except:
        return False
# ---------------- Convertisso downloader ----------------
class DownloaderTab(QWidget):
    def __init__(self):
        super().__init__()
        # Crée un QLabel avec le texte "Convertisso downloader" et le positionne à (20,20)
        label = QLabel("Convertisso downloader", self)
        label.move(20, 20)
        # Appelle la méthode initUI()
        self.initUI()

    def initUI(self):
        # Crée un QLabel avec le texte "Enter video link:" et le positionne à (50,100)
        self.link_label = QLabel(self)
        self.link_label.setText('Enter video link:')        
        self.link_label.move(50, 100)
        # Crée un QLineEdit et le positionne à (250,100) avec une largeur de 300 et une hauteur de 30
        self.link_input = QLineEdit(self)
        self.link_input.move(250, 100)
        self.link_input.resize(300, 30)
        self.link_input.text()
        # Crée un QLabel avec le texte "Enter the name of the file:" et le positionne à (50,150)
        self.name_label = QLabel(self)
        self.name_label.setText('Enter the name of the file:')
        self.name_label.move(50, 150)
        # Crée un QLineEdit et le positionne à (250,150) avec une largeur de 300 et une hauteur de 30
        self.name_input = QLineEdit(self)
        self.name_input.move(250, 150)
        self.name_input.resize(300, 30)
        self.name_input.text()
        # Crée un QLabel avec le texte "Enter destination folder:" et le positionne à (50,350)
        self.destination_label = QLabel(self)
        self.destination_label.setText('Enter destination folder:')
        self.destination_label.move(50, 350)
        # Crée un QLineEdit et le positionne à (250,350) avec une largeur de 300 et une hauteur de 30
        self.destination_input = QLineEdit(self)
        self.destination_input.move(250, 350)
        self.destination_input.resize(300, 30)
        self.destination_input.text()
        # Crée un QPushButton avec le texte "Choose Folder" et le positionne à (550,350). Connecte le bouton à la méthode "choose_folder".
        self.choose_destination_button = QPushButton('Choose Folder', self)
        self.choose_destination_button.move(550, 350)
        self.choose_destination_button.clicked.connect(self.choose_folder)
        # Crée un QLabel avec le texte "Choose download option:" et le positionne à (50,200)
        self.download_label = QLabel(self)
        self.download_label.setText('Choose download option:')
        self.download_label.move(50, 200)
         # Crée un QComboBox avec les options "Please choice", "Video Only", "Video + Subtitles", "Audio Only" et "Subtitles Only". Connecte le QComboBox à la méthode "setDownloadOption".
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
        # Crée un QLabel avec le texte "Download in progress : " et le positionne à (418, 50)
        self.Downloadcheck_txt_label = QLabel(self)
        self.Downloadcheck_txt_label.setText('Download in progress : ')
        self.Downloadcheck_txt_label.move(418, 50)
        # Création d'un QLabel pour afficher le statut de vérification de téléchargement avec une led, deffition de la led rouge pas defaut
        self.Downloadcheck_label = QLabel(self)
        self.Downloadcheck_label.setFixedSize(20, 20)
        self.Downloadcheck_label.move(600, 50)
        self.Downloadcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
        # Création d'un QLabel pour afficher le texte "Internet check : "
        self.internet_txt_label = QLabel(self)
        self.internet_txt_label.setText('Internet check : ')
        self.internet_txt_label.move(475, 20)
        # Création d'un QLabel pour afficher le statut de vérification d'Internet
        self.internet_label = QLabel(self)
        self.internet_label.setFixedSize(20, 20)
        self.internet_label.move(600, 20)
        self.internet_label.setStyleSheet("background-color: red; border-radius: 10px;")
        # Création d'un QTimer pour vérifier la connexion Internet tous les 1000 millisecondes
        self.timer = QTimer()
        self.timer.timeout.connect(self.check_internet_connection)
        self.timer.start(1000)
        # Création d'un QPushButton pour démarrer le téléchargement
        self.download_button = QPushButton('Download', self)
        self.download_button.move(350, 400)
        self.download_button.clicked.connect(self.download_video)


    # Fonction pour choisir le dossier de destination du téléchargement
    def choose_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self, 'Choose Folder')
        self.destination_input.setText(folder_path)
    # Fonction pour définir l'option de téléchargement sélectionnée par l'utilisateur
    def setDownloadOption(self, index):
        self.download_option_user = self.download_choice.itemText(index)
    # Fonction pour vérifier la connexion Internet
    def check_internet_connection(self):
        try:
            response = requests.get('http://www.google.com', timeout=5) # envoie d'une requete avec un timeout de 5
            if response.status_code == 200:
                self.internet_label.setStyleSheet("background-color: green; border-radius: 10px;")
            else:
                self.internet_label.setStyleSheet("background-color: red; border-radius: 10px;")
        except:
            self.internet_label.setStyleSheet("background-color: red; border-radius: 10px;")
    # Cette fonction permet de télécharger une vidéo à partir du lien donné par l'utilisateur
    def download_video(self):
        try:
            # Vérifier si l'utilisateur a une connexion internet active
            if internet_check() == True:
                if self.download_option_user == 'Video Only':  # Vérifier si l'utilisateur a choisi l'option "Video Only"
                    # Définir les options de téléchargement de la vidéo
                    ydl_opts = {
                        'format': 'bestvideo+bestaudio', 
                        'addmetadata': True, 
                        'outtmpl': self.name_input.text() 
                    }
                    # Afficher un indicateur de réussite du téléchargement en changeant la couleur d'un label en vert
                    self.Downloadcheck_label.setStyleSheet("background-color: green; border-radius: 10px;")
                    self.repaint()
                    # Télécharger la vidéo à partir du lien donné par l'utilisateur
                    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                        ydl.download([self.link_input.text()])
                    # Déplacer la vidéo téléchargée vers le dossier de destination choisi par l'utilisateur
                    for extension in ["*.mp4", "*.mkv", "*.webm", "*.flv"]:
                        for filename in glob.glob(extension):
                            shutil.move(filename, self.destination_input.text())
                    # Afficher un message de succès de téléchargement
                    show_download_success_message()
                    # Effacer les champs de saisie de l'utilisateur
                    self.link_input.clear()
                    self.name_input.clear()
                    self.destination_input.clear()
                    self.download_choice.setCurrentText('Please choose')
                    # Réinitialiser l'indicateur de réussite du téléchargement
                    self.Downloadcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                    self.repaint()
                elif self.download_option_user == 'Video + Subtitles':  # Vérifier si l'utilisateur a choisi l'option "Video + Subtitles"
                    # Définir les options de téléchargement de la vidéo
                    ydl_opts = {
                        'format': 'bv+ba', 
                        'addmetadata': True, 
                        'outtmpl': self.destination_input.text() + '/%(title)s.%(ext)s', 
                        'allsubtitles':  True,
                        'writeautomaticsub': True
                    }
                    # Afficher un indicateur de réussite du téléchargement en changeant la couleur d'un label en vert
                    self.Downloadcheck_label.setStyleSheet("background-color: green; border-radius: 10px;")
                    self.repaint()
                    # Télécharger la vidéo à partir du lien donné par l'utilisateur
                    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                        ydl.download([self.link_input.text()])
                    #Déplacer la vidéo téléchargée vers le dossier de destination choisi par l'utilisateur                        
                    for extension in ["*.mp4", "*.mkv", "*.webm", "*.flv", "*.srt", "*.ass", "*.vtt", "*.lrc"]:
                        for filename in glob.glob(extension):
                            shutil.move(filename, self.destination_input.text())
                    # Afficher un message de succès de téléchargement
                    show_download_success_message()
                    # Effacer les champs de saisie de l'utilisateur
                    self.link_input.clear()
                    self.name_input.clear()
                    self.destination_input.clear()
                    self.download_choice.setCurrentText('Please choose')
                    # Réinitialiser l'indicateur de réussite du téléchargement
                    self.Downloadcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                    self.repaint()
                elif self.download_option_user == 'Audio Only':  # Vérifier si l'utilisateur a choisi l'option "Audio Only"
                    # Définir les options de téléchargement de la vidéo
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
                    # Afficher un indicateur de réussite du téléchargement en changeant la couleur d'un label en vert
                    self.Downloadcheck_label.setStyleSheet("background-color: green; border-radius: 10px;")
                    self.repaint()
                    # Télécharger la vidéo à partir du lien donné par l'utilisateur
                    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                        ydl.download([self.link_input.text()])
                    #Déplacer la vidéo téléchargée vers le dossier de destination choisi par l'utilisateur                        
                    for extension in ["*.mp3", "*.aac", "*.flac", "*.m4a", "*.ogg", "*.wav", "*.opus", "*.vorbis"]:
                        for filename in glob.glob(extension):
                            shutil.move(filename, self.destination_input.text())
                    # Afficher un message de succès de téléchargement
                    show_download_success_message()
                    # Effacer les champs de saisie de l'utilisateur
                    self.link_input.clear()
                    self.name_input.clear()
                    self.destination_input.clear()
                    self.download_choice.setCurrentText('Please choose')
                    # Réinitialiser l'indicateur de réussite du téléchargement
                    self.Downloadcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                    self.repaint()
                elif self.download_option_user == 'Subtitles Only': # Vérifier si l'utilisateur a choisi l'option "Subtitles Only"
                    # Définir les options de téléchargement de la vidéo
                    ydl_opts = {
                        'skip_download': True,
                        'addmetadata':  True,
                        'outtmpl':  self.destination_input.text() + '.%(ext)s',
                        'allsubtitles':  True,
                        'writeautomaticsub':  True
                    }
                    # Afficher un indicateur de réussite du téléchargement en changeant la couleur d'un label en vert
                    self.Downloadcheck_label.setStyleSheet("background-color: green; border-radius: 10px;")
                    self.repaint()     
                    # Télécharger la vidéo à partir du lien donné par l'utilisateur     
                    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                        info_dict = ydl.extract_info(self.link_input.text(), download=False)
                        filename = ydl.prepare_filename(info_dict)
                        ydl.process_info(info_dict)
                    #Déplacer la vidéo téléchargée vers le dossier de destination choisi par l'utilisateur                        
                    for extension in ["*.srt", "*.ass", "*.vtt", "*.lrc"]:
                        for filename in glob.glob(extension):
                            shutil.move(filename, self.destination_input.text())
                    # Afficher un message de succès de téléchargement
                    show_download_success_message()
                    # Effacer les champs de saisie de l'utilisateur
                    self.link_input.clear()
                    self.name_input.clear()
                    self.destination_input.clear()
                    self.download_choice.setCurrentText('Please choose')
                    # Réinitialiser l'indicateur de réussite du téléchargement
                    self.Downloadcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                    self.repaint()
                else: 
                    # Si la vérification de la connexion internet a échoué, le label d'affichage de la connexion
                    self.internet_label.setStyleSheet("background-color: red; border-radius: 10px;")
                    # Si une erreur inattendue se produit, un message d'erreur"An unexpected error has occurred" sera affichez.
                    QMessageBox.critical(None, "Error", "An unexpected error has occurred")
                    # Le label d'affichage de la réussite du téléchargement devient rouge.
                    self.Downloadcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
            else:
                # Si la vérification de la connexion internet a échoué, le label d'affichage de la connexion
                self.internet_label.setStyleSheet("background-color: red; border-radius: 10px;")
                # Un message d'erreur est affiché pour indiquer à l'utilisateur que la connexion internet est indisponible.
                QMessageBox.critical(None, "Error", "No internet connextion please check your connection")
                # Le label d'affichage de la réussite du téléchargement devient rouge.
                self.Downloadcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
        except Exception as e:
            self.internet_label.setStyleSheet("background-color: red; border-radius: 10px;")
            # Un message d'erreur est affiché avec des informations sur l'erreur qui s'est produite pendant le téléchargement.
            error_message = "An error occurred during the download: {}".format(str(e))
            message_box = QMessageBox()
            message_box.setWindowTitle("Download error")
            message_box.setText(error_message) # Un message d'erreur est ensuite créé en utilisant la variable "e", qui contient l'exception levée, puis affiché dans une boîte de dialogue
            message_box.setIcon(QMessageBox.Warning)
            message_box.addButton(QMessageBox.Ok) # La boîte de dialogue affichera un bouton "OK" qui permettra à l'utilisateur de fermer la boîte de dialogue et de revenir à l'interface principale
            message_box.exec_()
# ---------------- Convertisso Audio ----------------
class AudioTab(QWidget):

    def __init__(self):
        super().__init__() 
        # Crée un QLabel avec le texte "Convertisso Audio" et le positionne à (20,20)   
        label = QLabel("Convertisso audio", self)
        label.move(20, 20)
        # Appelle la méthode initUI()
        self.initUI()
    def initUI(self):
                # Crée un QLabel avec le texte "Chose directory (its store your(s) file(s) to convert):" et le positionne à (50,200)
        self.path_label = QLabel(self)
        self.path_label.setText('Chose directory (where are stored your(s) file(s) to convert):')
        self.path_label.move(50, 200)
        # Crée un QLineEdit et le positionne à (470, 200) avec une largeur de 300 et une hauteur de 30
        self.path_input = QLineEdit(self)
        self.path_input.move(470, 200)
        self.path_input.resize(300, 30)
        self.path_input.text()
        # Crée un QPushButton avec le texte "Choose Folder" et le positionne à (770, 200). Connecte le bouton à la méthode "choose_folder".
        self.choose_path_button = QPushButton('Choose Folder', self)
        self.choose_path_button.move(770, 200)
        self.choose_path_button.clicked.connect(self.choose_folder)
        # Crée un QComboBox avec les options ci-dessous. Connecte le QComboBox à la méthode "setaudioOption".
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
        self.convertaudio_choice.move(250, 100)
        self.convertaudio_choice.resize(200, 30)
        self.convertaudio_choice.setMaxVisibleItems(5)
        self.convertaudio_choice.setEditable(True)
        self.convertaudio_choice.view().setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.convertaudio_choice.currentIndexChanged.connect(self.setaudioOption)
        # Crée un QLabel avec le texte "Conversion in progress: " et le positionne à (400, 20)
        self.convertcheck_txt_label = QLabel(self)
        self.convertcheck_txt_label.setText('Conversion in progress: ')
        self.convertcheck_txt_label.move(400, 20)
        # Création d'un QLabel pour afficher le statut de vérification de la convertion avec une led, deffition de la led rouge pas defaut
        self.convertcheck_label = QLabel(self)
        self.convertcheck_label.setFixedSize(20, 20)
        self.convertcheck_label.move(600, 20)
        self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
        # Création d'un QPushButton pour démarrer la convertion
        self.convertaudio_button = QPushButton('Convert', self)
        self.convertaudio_button.move(300, 350)
        self.convertaudio_button.clicked.connect(self.convertaudio)
    # Fonction pour choisir le dossier de destination de la convertion
    def choose_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self, 'Choose Folder')
        self.path_input.setText(folder_path)
    # Fonction pour définir l'option de convertion sélectionnée par l'utilisateur
    def setaudioOption(self, index):
        self.convert_audio_choice = self.convertaudio_choice.itemText(index)

    def convertaudio(self): #cette partie permet de convertir des fichiers audio
        try:
            if self.convert_audio_choice == 'mp3 to ogg': # Vérifie l'entré utilisteur de la QComboBox   # Vérifie l'entré utilisteur de la QComboBox
                # Recherche des fichiers d'entrées dans le répertoire sélectionné et ses sous-répertoires
                mp3_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.mp3"), recursive=True)
                # Vérifier si les fichiers d'entré ont été trouvés dans le répertoire
                # Vérifier si des fichiers MP3 ont été trouvés dans le répertoire
                if mp3_files:
                    # Afficher un message indiquant que la conversion est en cours
                    print("Conversion en cours...")
                    # Parcourir tous les fichiers d'entrées trouvés
                    for mp3_file in mp3_files:
                        # Définir le nom de fichier sortant en remplaçant l'extension du fichier intrant par celui du sortant                     
                        ogg_file = os.path.splitext(mp3_file)[0] + '.ogg'
                        try:
                            # Mise à jour de l'étiquette en vert, d'état pour indiquer que la conversion est en cours
                            self.convertcheck_label.setStyleSheet("background-color: green; border-radius: 10px;")
                            # Mettre à jour l'interface graphique
                            self.repaint()
                            # Création de la sortie de flux FFmpeg pour le fichier MP3 d'entrée
                            stream = ffmpeg.input(mp3_file)
                            # Définition des options de sortie pour la conversion en AAC
                            stream = ffmpeg.output(stream, ogg_file, acodec='libvorbis', map_metadata=0)
                            # Lancer la conversion à l'aide de FFmpeg en mode silencieux
                            ffmpeg.run(stream, quiet=True)
                            # Afficher un message indiquant que la conversion est réussie
                            print("Conversion réussie")
                        except ffmpeg.Error as e:
                            # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                            self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                            # Afficher un message d'erreur avec la raison de l'échec de la conversion
                            QMessageBox.critical(None, "Error", f"Échec de la conversion de {mp3_file}: {e.stderr}")
                            return
                        # Définir l'extension de fichier en sortie
                        encov = "ogg"
                else:
                    # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                    self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                    # Afficher un message d'erreur si aucun fichier compatible n'a été trouvé dans le répertoire
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
                # Afficher un message de succès de la conversion
                show_success_message()
                # Effacer le champ de saisie pour le chemin d'entrée
                self.path_input.clear()
                # Réinitialiser le choix de conversion
                self.convertaudio_choice.setCurrentText('Veuillez choisir')
                # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                # Mettre à jour l'interface graphique
                self.repaint()
            elif self.convert_audio_choice == 'mp3 to aac': # Vérifie l'entré utilisteur de la QComboBox   
            # Recherche des fichiers d'entrées dans le répertoire sélectionné et ses sous-répertoires
                mp3_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.mp3"), recursive=True)
                # Vérifier si les fichiers d'entré ont été trouvés dans le répertoire
                if mp3_files:
                    # Afficher un message indiquant que la conversion est en cours
                    print("Conversion en cours...")
                    # Parcourir tous les fichiers d'entrées trouvés
                    for mp3_file in mp3_files:
                        # Définir le nom de fichier sortant en remplaçant l'extension du fichier intrant par celui du sortant
                        aac_file = os.path.splitext(mp3_file)[0] + '.aac'
                        try:
                            # Mise à jour de l'étiquette d'état en vert, pour indiquer que la conversion est en cours
                            self.convertcheck_label.setStyleSheet("background-color: green; border-radius: 10px;")
                            # Mettre à jour l'interface graphique
                            self.repaint() 
                            # Création de la sortie de flux FFmpeg pour le fichier d'entrée
                            stream = ffmpeg.input(mp3_file)
                            # Définition des options de sortie pour la conversion
                            stream = ffmpeg.output(stream, aac_file, acodec='aac', map_metadata=0)
                            # Lancer la conversion à l'aide de FFmpeg en mode silencieux
                            ffmpeg.run(stream, quiet=True)
                            # Afficher un message indiquant que la conversion est réussie
                            print("Conversion OK")
                        except ffmpeg.Error as e:
                            # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                            self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                            # Afficher un message d'erreur avec la raison de l'échec de la conversion
                            QMessageBox.critical(None, "Erreur", f"Impossible de convertir {mp3_file} : {e.stderr}")
                            return
                        encov = "aac"
                else:
                    # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec                  
                    self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                    # Afficher un message d'erreur si aucun fichier compatible n'a été trouvé dans le répertoire
                    QMessageBox.critical(None, "Erreur", "No compatible files found in the selected directory")
                    return
                # Afficher un message de succès de la conversion
                show_success_message()
                # Effacer le champ de saisie pour le chemin d'entrée
                self.path_input.clear()
                # Réinitialiser le choix de conversion
                self.convertaudio_choice.setCurrentText('Veuillez choisir')
                # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                # Mettre à jour l'interface graphique
                self.repaint()
            elif self.convert_audio_choice == 'mp3 to wav': # Vérifie l'entré utilisteur de la QComboBox 
                     # Recherche des fichiers d'entrées dans le répertoire sélectionné et ses sous-répertoires
                    mp3_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.mp3"), recursive=True)
                    # Vérifier si les fichiers d'entré ont été trouvés dans le répertoire
                    if mp3_files:
                        # Afficher un message indiquant que la conversion est en cours
                        print("Conversion in progress ...")
                        for mp3_file in mp3_files:
                            # Définir le nom de fichier sortant en remplaçant l'extension du fichier intrant par celui du sortant
                            wav_file = os.path.splitext(mp3_file)[0] + '.wav'
                            try:
                                # Mise à jour de l'étiquette d'état en vert, pour indiquer que la conversion est en cours
                                self.convertcheck_label.setStyleSheet("background-color: green; border-radius: 10px;")
                                # Mettre à jour l'interface graphique
                                self.repaint() 
                                # Création de la sortie de flux FFmpeg pour le fichier d'entrée
                                stream = ffmpeg.input(mp3_file)
                                # Définition des options de sortie pour la conversion
                                stream = ffmpeg.output(stream, wav_file, map_metadata=0)
                                # Lancer la conversion à l'aide de FFmpeg en mode silencieux
                                ffmpeg.run(stream, quiet=True)
                                # Afficher un message indiquant que la conversion est réussie
                                print("Conversion OK")
                            except ffmpeg.Error as e:
                                # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                                self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                                # Afficher un message d'erreur avec la raison de l'échec de la conversion
                                QMessageBox.critical(None, "Error", f"Failed to convert {mp3_file}: {e.stderr}")
                                return
                            encov = "aac"
                    else: 
                        # Définir le style pour l'étiquette(en rouge) de vérification de la conversion en échec                  
                        self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                        # Afficher un message d'erreur si aucun fichier compatible n'a été trouvé dans le répertoire
                        QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                        return
                    # Afficher un message de succès de la conversion
                    show_success_message()
                    # Effacer le champ de saisie pour le chemin d'entrée
                    self.path_input.clear()
                    # Réinitialiser le choix de conversion
                    self.convertaudio_choice.setCurrentText('Veuillez choisir')
                    # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                    self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                    # Mettre à jour l'interface graphique
                    self.repaint()
            elif self.convert_audio_choice == 'mp3 to ac3': # Vérifie l'entré utilisteur de la QComboBox 
                     # Recherche des fichiers d'entrées dans le répertoire sélectionné et ses sous-répertoires
                    mp3_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.mp3"), recursive=True)
                    # Vérifier si les fichiers d'entré ont été trouvés dans le répertoire
                    if mp3_files:
                        # Afficher un message indiquant que la conversion est en cours
                        print("Conversion in progress ...")
                        for mp3_file in mp3_files:
                            # Définir le nom de fichier sortant en remplaçant l'extension du fichier intrant par celui du sortant
                            ac3_file = os.path.splitext(mp3_file)[0] + '.ac3'
                            try:
                                # Mise à jour de l'étiquette d'état en vert, pour indiquer que la conversion est en cours
                                self.convertcheck_label.setStyleSheet("background-color: green; border-radius: 10px;")
                                # Mettre à jour l'interface graphique
                                self.repaint() 
                                # Création de la sortie de flux FFmpeg pour le fichier d'entrée
                                stream = ffmpeg.input(mp3_file)
                                # Définition des options de sortie pour la conversion
                                stream = ffmpeg.output(stream, ac3_file, acodec='ac3', map_metadata=0)
                                # Lancer la conversion à l'aide de FFmpeg en mode silencieux
                                ffmpeg.run(stream, quiet=True)
                                # Afficher un message indiquant que la conversion est réussie
                                print("Conversion OK")
                            except ffmpeg.Error as e:
                                # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                                self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                                # Afficher un message d'erreur avec la raison de l'échec de la conversion
                                QMessageBox.critical(None, "Error", f"Failed to convert {mp3_file}: {e.stderr}")
                                return
                            encov = "ac3"
                    else: 
                        # Définir le style pour l'étiquette(en rouge) de vérification de la conversion en échec                  
                        self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                        # Afficher un message d'erreur si aucun fichier compatible n'a été trouvé dans le répertoire
                        QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                        return
                    # Afficher un message de succès de la conversion
                    show_success_message()
                    # Effacer le champ de saisie pour le chemin d'entrée
                    self.path_input.clear()
                    # Réinitialiser le choix de conversion
                    self.convertaudio_choice.setCurrentText('Veuillez choisir')
                    # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                    self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                    # Mettre à jour l'interface graphique
                    self.repaint()
            elif self.convert_audio_choice == 'mp3 to opus' : # Vérifie l'entré utilisteur de la QComboBox 
                    # Recherche des fichiers d'entrées dans le répertoire sélectionné et ses sous-répertoires
                    mp3_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.mp3"), recursive=True)
                    # Vérifier si les fichiers d'entré ont été trouvés dans le répertoire
                    if mp3_files:
                        # Afficher un message indiquant que la conversion est en cours
                        print("Conversion in progress ...")
                        for mp3_file in mp3_files:
                            # Définir le nom de fichier sortant en remplaçant l'extension du fichier intrant par celui du sortant 
                            opus_file = os.path.splitext(mp3_file)[0] + '.opus'
                            try:
                                # Mise à jour de l'étiquette d'état en vert, pour indiquer que la conversion est en cours
                                self.convertcheck_label.setStyleSheet("background-color: green; border-radius: 10px;")
                                # Mettre à jour l'interface graphique
                                self.repaint() 
                                # Création de la sortie de flux FFmpeg pour le fichier d'entrée
                                stream = ffmpeg.input(mp3_file)
                                # Définition des options de sortie pour la conversion
                                stream = ffmpeg.output(stream, opus_file, acodec='libopus', map_metadata=0)
                                # Lancer la conversion à l'aide de FFmpeg en mode silencieux
                                ffmpeg.run(stream, quiet=True)
                                # Afficher un message indiquant que la conversion est réussie
                                print("Conversion OK")
                            except ffmpeg.Error as e:
                                # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                                self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                                # Afficher un message d'erreur avec la raison de l'échec de la conversion
                                QMessageBox.critical(None, "Error", f"Failed to convert {mp3_file}: {e.stderr}")
                                return
                            encov = "opus"
                    else: 
                        # Définir le style pour l'étiquette(en rouge) de vérification de la conversion en échec                  
                        self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                        # Afficher un message d'erreur si aucun fichier compatible n'a été trouvé dans le répertoire
                        QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                        return
                    # Afficher un message de succès de la conversion
                    show_success_message()
                    # Effacer le champ de saisie pour le chemin d'entrée
                    self.path_input.clear()
                    # Réinitialiser le choix de conversion
                    self.convertaudio_choice.setCurrentText('Veuillez choisir')
                    # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                    self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                    # Mettre à jour l'interface graphique
                    self.repaint()
            elif self.convert_audio_choice == 'mp3 to m4a': # Vérifie l'entré utilisteur de la QComboBox 
                     # Recherche des fichiers d'entrées dans le répertoire sélectionné et ses sous-répertoires
                    mp3_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.mp3"), recursive=True)
                    # Vérifier si les fichiers d'entré ont été trouvés dans le répertoire
                    if mp3_files:
                        # Afficher un message indiquant que la conversion est en cours
                        print("Conversion in progress ...")
                        for mp3_file in mp3_files:
                            # Définir le nom de fichier sortant en remplaçant l'extension du fichier intrant par celui du sortant
                            m4a_file = os.path.splitext(mp3_file)[0] + '.m4a'
                            try:
                                # Mise à jour de l'étiquette d'état en vert, pour indiquer que la conversion est en cours
                                self.convertcheck_label.setStyleSheet("background-color: green; border-radius: 10px;")
                                # Mettre à jour l'interface graphique
                                self.repaint() 
                                # Création de la sortie de flux FFmpeg pour le fichier d'entrée
                                stream = ffmpeg.input(mp3_file)
                                # Définition des options de sortie pour la conversion
                                stream = ffmpeg.output(stream, m4a_file, acodec='alac', map_metadata=0)
                                # Lancer la conversion à l'aide de FFmpeg en mode silencieux
                                ffmpeg.run(stream, quiet=True)
                                # Afficher un message indiquant que la conversion est réussie
                                print("Conversion OK")
                            except ffmpeg.Error as e:
                                # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                                self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                                # Afficher un message d'erreur avec la raison de l'échec de la conversion
                                QMessageBox.critical(None, "Error", f"Failed to convert {mp3_file}: {e.stderr}")
                                return
                            encov = "m4a"
                    else: 
                        # Définir le style pour l'étiquette(en rouge) de vérification de la conversion en échec                  
                        self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                        # Afficher un message d'erreur si aucun fichier compatible n'a été trouvé dans le répertoire
                        QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                        return
                    # Afficher un message de succès de la conversion
                    show_success_message()
                    # Effacer le champ de saisie pour le chemin d'entrée
                    self.path_input.clear()
                    # Réinitialiser le choix de conversion
                    self.convertaudio_choice.setCurrentText('Veuillez choisir')
                    # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                    self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                    # Mettre à jour l'interface graphique
                    self.repaint()
            elif self.convert_audio_choice == 'wav to ogg': # Vérifie l'entré utilisteur de la QComboBox 
                     # Recherche des fichiers d'entrées dans le répertoire sélectionné et ses sous-répertoires
                    wav_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.wav"), recursive=True)
                    # Vérifier si les fichiers d'entré ont été trouvés dans le répertoire
                    if wav_files:
                        # Afficher un message indiquant que la conversion est en cours
                        print("Conversion in progress ...")
                        for wav_file in wav_files:
                            # Définir le nom de fichier sortant en remplaçant l'extension du fichier intrant par celui du sortant
                            ogg_file = os.path.splitext(wav_file)[0] + '.ogg'
                            try:
                                # Mise à jour de l'étiquette d'état en vert, pour indiquer que la conversion est en cours
                                self.convertcheck_label.setStyleSheet("background-color: green; border-radius: 10px;")
                                # Mettre à jour l'interface graphique
                                self.repaint() 
                                # Création de la sortie de flux FFmpeg pour le fichier d'entrée
                                stream = ffmpeg.input(wav_file)
                                # Définition des options de sortie pour la conversion
                                stream = ffmpeg.output(stream, ogg_file, acodec='libvorbis', map_metadata=0)
                                # Lancer la conversion à l'aide de FFmpeg en mode silencieux
                                ffmpeg.run(stream, quiet=True)
                                # Afficher un message indiquant que la conversion est réussie
                                print("Conversion OK")
                            except ffmpeg.Error as e:
                                # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                                self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                                # Afficher un message d'erreur avec la raison de l'échec de la conversion
                                QMessageBox.critical(None, "Error", f"Failed to convert {wav_file}: {e.stderr}")
                                return
                            encov = "ogg"
                    else: 
                        # Définir le style pour l'étiquette(en rouge) de vérification de la conversion en échec                  
                        self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                        # Afficher un message d'erreur si aucun fichier compatible n'a été trouvé dans le répertoire
                        QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                        return
                    # Afficher un message de succès de la conversion
                    show_success_message()
                    # Effacer le champ de saisie pour le chemin d'entrée
                    self.path_input.clear()
                    # Réinitialiser le choix de conversion
                    self.convertaudio_choice.setCurrentText('Veuillez choisir')
                    # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                    self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                    # Mettre à jour l'interface graphique
                    self.repaint()
            elif self.convert_audio_choice == 'wav to aac': # Vérifie l'entré utilisteur de la QComboBox 
                     # Recherche des fichiers d'entrées dans le répertoire sélectionné et ses sous-répertoires
                    wav_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.wav"), recursive=True)
                    # Vérifier si les fichiers d'entré ont été trouvés dans le répertoire
                    if wav_files:
                        # Afficher un message indiquant que la conversion est en cours
                        print("Conversion in progress ...")
                        for wav_file in wav_files:
                            # Définir le nom de fichier sortant en remplaçant l'extension du fichier intrant par celui du sortant
                            aac_file = os.path.splitext(wav_file)[0] + '.aac'
                            try:
                                # Mise à jour de l'étiquette d'état en vert, pour indiquer que la conversion est en cours
                                self.convertcheck_label.setStyleSheet("background-color: green; border-radius: 10px;")
                                # Mettre à jour l'interface graphique
                                self.repaint() 
                                # Création de la sortie de flux FFmpeg pour le fichier d'entrée
                                stream = ffmpeg.input(wav_file)
                                # Définition des options de sortie pour la conversion
                                stream = ffmpeg.output(stream, aac_file, acodec='aac', map_metadata=0)
                                # Lancer la conversion à l'aide de FFmpeg en mode silencieux
                                ffmpeg.run(stream, quiet=True)
                                # Afficher un message indiquant que la conversion est réussie
                                print("Conversion OK")
                            except ffmpeg.Error as e:
                                # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                                self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                                # Afficher un message d'erreur avec la raison de l'échec de la conversion
                                QMessageBox.critical(None, "Error", f"Failed to convert {wav_file}: {e.stderr}")
                                return
                            encov = "aac"
                    else: 
                        # Définir le style pour l'étiquette(en rouge) de vérification de la conversion en échec                  
                        self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                        # Afficher un message d'erreur si aucun fichier compatible n'a été trouvé dans le répertoire
                        QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                        return
                    # Afficher un message de succès de la conversion
                    show_success_message()
                    # Effacer le champ de saisie pour le chemin d'entrée
                    self.path_input.clear()
                    # Réinitialiser le choix de conversion
                    self.convertaudio_choice.setCurrentText('Veuillez choisir')
                    # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                    self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                    # Mettre à jour l'interface graphique
                    self.repaint()
            elif self.convert_audio_choice == 'wav to mp3': # Vérifie l'entré utilisteur de la QComboBox 
                     # Recherche des fichiers d'entrées dans le répertoire sélectionné et ses sous-répertoires
                    wav_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.wav"), recursive=True)
                    # Vérifier si les fichiers d'entré ont été trouvés dans le répertoire
                    if wav_files:
                        # Afficher un message indiquant que la conversion est en cours
                        print("Conversion in progress ...")
                        for wav_file in wav_files:
                            # Définir le nom de fichier sortant en remplaçant l'extension du fichier intrant par celui du sortant
                            mp3_file = os.path.splitext(wav_file)[0] + '.mp3'
                            try:
                                # Mise à jour de l'étiquette d'état en vert, pour indiquer que la conversion est en cours
                                self.convertcheck_label.setStyleSheet("background-color: green; border-radius: 10px;")
                                # Mettre à jour l'interface graphique
                                self.repaint() 
                                # Création de la sortie de flux FFmpeg pour le fichier d'entrée
                                stream = ffmpeg.input(wav_file)
                                # Définition des options de sortie pour la conversion
                                stream = ffmpeg.output(stream, mp3_file, acodec='libmp3lame', map_metadata=0)
                                # Lancer la conversion à l'aide de FFmpeg en mode silencieux
                                ffmpeg.run(stream, quiet=True)
                                # Afficher un message indiquant que la conversion est réussie
                                print("Conversion OK")
                            except ffmpeg.Error as e:
                                # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                                self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                                # Afficher un message d'erreur avec la raison de l'échec de la conversion
                                QMessageBox.critical(None, "Error", f"Failed to convert {wav_file}: {e.stderr}")
                                return
                            encov = "aac"
                    else: 
                        # Définir le style pour l'étiquette(en rouge) de vérification de la conversion en échec                  
                        self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                        # Afficher un message d'erreur si aucun fichier compatible n'a été trouvé dans le répertoire
                        QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                        return
                    # Afficher un message de succès de la conversion
                    show_success_message()
                    # Effacer le champ de saisie pour le chemin d'entrée
                    self.path_input.clear()
                    # Réinitialiser le choix de conversion
                    self.convertaudio_choice.setCurrentText('Veuillez choisir')
                    # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                    self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                    # Mettre à jour l'interface graphique
                    self.repaint()
            elif self.convert_audio_choice == 'wav to ac3': # Vérifie l'entré utilisteur de la QComboBox 
                     # Recherche des fichiers d'entrées dans le répertoire sélectionné et ses sous-répertoires
                    wav_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.wav"), recursive=True)
                    # Vérifier si les fichiers d'entré ont été trouvés dans le répertoire
                    if wav_files:
                        # Afficher un message indiquant que la conversion est en cours
                        print("Conversion in progress ...")
                        for wav_file in wav_files:
                            # Définir le nom de fichier sortant en remplaçant l'extension du fichier intrant par celui du sortant
                            ac3_file = os.path.splitext(wav_file)[0] + '.ac3'
                            try:
                                # Mise à jour de l'étiquette d'état en vert, pour indiquer que la conversion est en cours
                                self.convertcheck_label.setStyleSheet("background-color: green; border-radius: 10px;")
                                # Mettre à jour l'interface graphique
                                self.repaint() 
                                # Création de la sortie de flux FFmpeg pour le fichier d'entrée
                                stream = ffmpeg.input(wav_file)
                                # Définition des options de sortie pour la conversion
                                stream = ffmpeg.output(stream, ac3_file, acodec='ac3', map_metadata=0)
                                # Lancer la conversion à l'aide de FFmpeg en mode silencieux
                                ffmpeg.run(stream, quiet=True)
                                # Afficher un message indiquant que la conversion est réussie
                                print("Conversion OK")
                            except ffmpeg.Error as e:
                                # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                                self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                                # Afficher un message d'erreur avec la raison de l'échec de la conversion
                                QMessageBox.critical(None, "Error", f"Failed to convert {wav_file}: {e.stderr}")
                                return
                            encov = "ac3"
                    else: 
                        # Définir le style pour l'étiquette(en rouge) de vérification de la conversion en échec                  
                        self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                        # Afficher un message d'erreur si aucun fichier compatible n'a été trouvé dans le répertoire
                        QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                        return
                    # Afficher un message de succès de la conversion
                    show_success_message()
                    # Effacer le champ de saisie pour le chemin d'entrée
                    self.path_input.clear()
                    # Réinitialiser le choix de conversion
                    self.convertaudio_choice.setCurrentText('Veuillez choisir')
                    # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                    self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                    # Mettre à jour l'interface graphique
                    self.repaint()
            elif self.convert_audio_choice == 'wav to opus' : # Vérifie l'entré utilisteur de la QComboBox 
                    # Recherche des fichiers d'entrées dans le répertoire sélectionné et ses sous-répertoires
                    wav_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.wav"), recursive=True)
                    # Vérifier si les fichiers d'entré ont été trouvés dans le répertoire
                    if wav_files:
                        # Afficher un message indiquant que la conversion est en cours
                        print("Conversion in progress ...")
                        for wav_file in wav_files:
                            # Définir le nom de fichier sortant en remplaçant l'extension du fichier intrant par celui du sortant 
                            opus_file = os.path.splitext(wav_file)[0] + '.opus'
                            try:
                                # Mise à jour de l'étiquette d'état en vert, pour indiquer que la conversion est en cours
                                self.convertcheck_label.setStyleSheet("background-color: green; border-radius: 10px;")
                                # Mettre à jour l'interface graphique
                                self.repaint() 
                                # Création de la sortie de flux FFmpeg pour le fichier d'entrée
                                stream = ffmpeg.input(wav_file)
                                # Définition des options de sortie pour la conversion
                                stream = ffmpeg.output(stream, opus_file, acodec='libopus', map_metadata=0)
                                # Lancer la conversion à l'aide de FFmpeg en mode silencieux
                                ffmpeg.run(stream, quiet=True)
                                # Afficher un message indiquant que la conversion est réussie
                                print("Conversion OK")
                            except ffmpeg.Error as e:
                                # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                                self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                                # Afficher un message d'erreur avec la raison de l'échec de la conversion
                                QMessageBox.critical(None, "Error", f"Failed to convert {wav_file}: {e.stderr}")
                                return
                            encov = "opus"
                    else: 
                        # Définir le style pour l'étiquette(en rouge) de vérification de la conversion en échec                  
                        self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                        # Afficher un message d'erreur si aucun fichier compatible n'a été trouvé dans le répertoire
                        QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                        return
                    # Afficher un message de succès de la conversion
                    show_success_message()
                    # Effacer le champ de saisie pour le chemin d'entrée
                    self.path_input.clear()
                    # Réinitialiser le choix de conversion
                    self.convertaudio_choice.setCurrentText('Veuillez choisir')
                    # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                    self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                    # Mettre à jour l'interface graphique
                    self.repaint()
            elif self.convert_audio_choice == 'wav to m4a': # Vérifie l'entré utilisteur de la QComboBox 
                     # Recherche des fichiers d'entrées dans le répertoire sélectionné et ses sous-répertoires
                    wav_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.wav"), recursive=True)
                    # Vérifier si les fichiers d'entré ont été trouvés dans le répertoire
                    if wav_files:
                        # Afficher un message indiquant que la conversion est en cours
                        print("Conversion in progress ...")
                        for wav_file in wav_files:
                            # Définir le nom de fichier sortant en remplaçant l'extension du fichier intrant par celui du sortant
                            m4a_file = os.path.splitext(wav_file)[0] + '.m4a'
                            try:
                                # Mise à jour de l'étiquette d'état en vert, pour indiquer que la conversion est en cours
                                self.convertcheck_label.setStyleSheet("background-color: green; border-radius: 10px;")
                                # Mettre à jour l'interface graphique
                                self.repaint() 
                                # Création de la sortie de flux FFmpeg pour le fichier d'entrée
                                stream = ffmpeg.input(wav_file)
                                # Définition des options de sortie pour la conversion
                                stream = ffmpeg.output(stream, m4a_file, acodec='alac', map_metadata=0)
                                # Lancer la conversion à l'aide de FFmpeg en mode silencieux
                                ffmpeg.run(stream, quiet=True)
                                # Afficher un message indiquant que la conversion est réussie
                                print("Conversion OK")
                            except ffmpeg.Error as e:
                                # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                                self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                                # Afficher un message d'erreur avec la raison de l'échec de la conversion
                                QMessageBox.critical(None, "Error", f"Failed to convert {wav_file}: {e.stderr}")
                                return
                            encov = "m4a"
                    else: 
                        # Définir le style pour l'étiquette(en rouge) de vérification de la conversion en échec                  
                        self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                        # Afficher un message d'erreur si aucun fichier compatible n'a été trouvé dans le répertoire
                        QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                        return
                    # Afficher un message de succès de la conversion
                    show_success_message()
                    # Effacer le champ de saisie pour le chemin d'entrée
                    self.path_input.clear()
                    # Réinitialiser le choix de conversion
                    self.convertaudio_choice.setCurrentText('Veuillez choisir')
                    # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                    self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                    # Mettre à jour l'interface graphique
                    self.repaint()
            elif self.convert_audio_choice == 'ogg to wav': # Vérifie l'entré utilisteur de la QComboBox 
                     # Recherche des fichiers d'entrées dans le répertoire sélectionné et ses sous-répertoires
                    ogg_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.ogg"), recursive=True)
                    # Vérifier si les fichiers d'entré ont été trouvés dans le répertoire
                    if ogg_files:
                        # Afficher un message indiquant que la conversion est en cours
                        print("Conversion in progress ...")
                        for ogg_file in ogg_files:
                            # Définir le nom de fichier sortant en remplaçant l'extension du fichier intrant par celui du sortant
                            wav_file = os.path.splitext(ogg_file)[0] + '.wav'
                            try:
                                # Mise à jour de l'étiquette d'état en vert, pour indiquer que la conversion est en cours
                                self.convertcheck_label.setStyleSheet("background-color: green; border-radius: 10px;")
                                # Mettre à jour l'interface graphique
                                self.repaint() 
                                # Création de la sortie de flux FFmpeg pour le fichier d'entrée
                                stream = ffmpeg.input(ogg_file)
                                # Définition des options de sortie pour la conversion
                                stream = ffmpeg.output(stream, wav_file, map_metadata=0)
                                # Lancer la conversion à l'aide de FFmpeg en mode silencieux
                                ffmpeg.run(stream, quiet=True)
                                # Afficher un message indiquant que la conversion est réussie
                                print("Conversion OK")
                            except ffmpeg.Error as e:
                                # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                                self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                                # Afficher un message d'erreur avec la raison de l'échec de la conversion
                                QMessageBox.critical(None, "Error", f"Failed to convert {ogg_file}: {e.stderr}")
                                return
                            encov = "ogg"
                    else: 
                        # Définir le style pour l'étiquette(en rouge) de vérification de la conversion en échec                  
                        self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                        # Afficher un message d'erreur si aucun fichier compatible n'a été trouvé dans le répertoire
                        QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                        return
                    # Afficher un message de succès de la conversion
                    show_success_message()
                    # Effacer le champ de saisie pour le chemin d'entrée
                    self.path_input.clear()
                    # Réinitialiser le choix de conversion
                    self.convertaudio_choice.setCurrentText('Veuillez choisir')
                    # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                    self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                    # Mettre à jour l'interface graphique
                    self.repaint()
            elif self.convert_audio_choice == 'ogg to aac': # Vérifie l'entré utilisteur de la QComboBox 
                     # Recherche des fichiers d'entrées dans le répertoire sélectionné et ses sous-répertoires
                    ogg_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.ogg"), recursive=True)
                    # Vérifier si les fichiers d'entré ont été trouvés dans le répertoire
                    if ogg_files:
                        # Afficher un message indiquant que la conversion est en cours
                        print("Conversion in progress ...")
                        for ogg_file in ogg_files:
                            # Définir le nom de fichier sortant en remplaçant l'extension du fichier intrant par celui du sortant
                            aac_file = os.path.splitext(ogg_file)[0] + '.aac'
                            try:
                                # Mise à jour de l'étiquette d'état en vert, pour indiquer que la conversion est en cours
                                self.convertcheck_label.setStyleSheet("background-color: green; border-radius: 10px;")
                                # Mettre à jour l'interface graphique
                                self.repaint() 
                                # Création de la sortie de flux FFmpeg pour le fichier d'entrée
                                stream = ffmpeg.input(ogg_file)
                                # Définition des options de sortie pour la conversion
                                stream = ffmpeg.output(stream, aac_file, acodec='aac', map_metadata=0)
                                # Lancer la conversion à l'aide de FFmpeg en mode silencieux
                                ffmpeg.run(stream, quiet=True)
                                # Afficher un message indiquant que la conversion est réussie
                                print("Conversion OK")
                            except ffmpeg.Error as e:
                                # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                                self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                                # Afficher un message d'erreur avec la raison de l'échec de la conversion
                                QMessageBox.critical(None, "Error", f"Failed to convert {ogg_file}: {e.stderr}")
                                return
                            encov = "aac"
                    else: 
                        # Définir le style pour l'étiquette(en rouge) de vérification de la conversion en échec                  
                        self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                        # Afficher un message d'erreur si aucun fichier compatible n'a été trouvé dans le répertoire
                        QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                        return
                    # Afficher un message de succès de la conversion
                    show_success_message()
                    # Effacer le champ de saisie pour le chemin d'entrée
                    self.path_input.clear()
                    # Réinitialiser le choix de conversion
                    self.convertaudio_choice.setCurrentText('Veuillez choisir')
                    # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                    self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                    # Mettre à jour l'interface graphique
                    self.repaint()
            elif self.convert_audio_choice == 'ogg to mp3': # Vérifie l'entré utilisteur de la QComboBox 
                     # Recherche des fichiers d'entrées dans le répertoire sélectionné et ses sous-répertoires
                    ogg_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.ogg"), recursive=True)
                    # Vérifier si les fichiers d'entré ont été trouvés dans le répertoire
                    if ogg_files:
                        # Afficher un message indiquant que la conversion est en cours
                        print("Conversion in progress ...")
                        for ogg_file in ogg_files:
                            # Définir le nom de fichier sortant en remplaçant l'extension du fichier intrant par celui du sortant
                            mp3_file = os.path.splitext(ogg_file)[0] + '.mp3'
                            try:
                                # Mise à jour de l'étiquette d'état en vert, pour indiquer que la conversion est en cours
                                self.convertcheck_label.setStyleSheet("background-color: green; border-radius: 10px;")
                                # Mettre à jour l'interface graphique
                                self.repaint() 
                                # Création de la sortie de flux FFmpeg pour le fichier d'entrée
                                stream = ffmpeg.input(ogg_file)
                                # Définition des options de sortie pour la conversion
                                stream = ffmpeg.output(stream, mp3_file, acodec='libmp3lame', map_metadata=0)
                                # Lancer la conversion à l'aide de FFmpeg en mode silencieux
                                ffmpeg.run(stream, quiet=True)
                                # Afficher un message indiquant que la conversion est réussie
                                print("Conversion OK")
                            except ffmpeg.Error as e:
                                # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                                self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                                # Afficher un message d'erreur avec la raison de l'échec de la conversion
                                QMessageBox.critical(None, "Error", f"Failed to convert {ogg_file}: {e.stderr}")
                                return
                            encov = "aac"
                    else: 
                        # Définir le style pour l'étiquette(en rouge) de vérification de la conversion en échec                  
                        self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                        # Afficher un message d'erreur si aucun fichier compatible n'a été trouvé dans le répertoire
                        QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                        return
                    # Afficher un message de succès de la conversion
                    show_success_message()
                    # Effacer le champ de saisie pour le chemin d'entrée
                    self.path_input.clear()
                    # Réinitialiser le choix de conversion
                    self.convertaudio_choice.setCurrentText('Veuillez choisir')
                    # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                    self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                    # Mettre à jour l'interface graphique
                    self.repaint()
            elif self.convert_audio_choice == 'ogg to ac3': # Vérifie l'entré utilisteur de la QComboBox 
                     # Recherche des fichiers d'entrées dans le répertoire sélectionné et ses sous-répertoires
                    ogg_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.ogg"), recursive=True)
                    # Vérifier si les fichiers d'entré ont été trouvés dans le répertoire
                    if ogg_files:
                        # Afficher un message indiquant que la conversion est en cours
                        print("Conversion in progress ...")
                        for ogg_file in ogg_files:
                            # Définir le nom de fichier sortant en remplaçant l'extension du fichier intrant par celui du sortant
                            ac3_file = os.path.splitext(ogg_file)[0] + '.ac3'
                            try:
                                # Mise à jour de l'étiquette d'état en vert, pour indiquer que la conversion est en cours
                                self.convertcheck_label.setStyleSheet("background-color: green; border-radius: 10px;")
                                # Mettre à jour l'interface graphique
                                self.repaint() 
                                # Création de la sortie de flux FFmpeg pour le fichier d'entrée
                                stream = ffmpeg.input(ogg_file)
                                # Définition des options de sortie pour la conversion
                                stream = ffmpeg.output(stream, ac3_file, acodec='ac3', map_metadata=0)
                                # Lancer la conversion à l'aide de FFmpeg en mode silencieux
                                ffmpeg.run(stream, quiet=True)
                                # Afficher un message indiquant que la conversion est réussie
                                print("Conversion OK")
                            except ffmpeg.Error as e:
                                # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                                self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                                # Afficher un message d'erreur avec la raison de l'échec de la conversion
                                QMessageBox.critical(None, "Error", f"Failed to convert {ogg_file}: {e.stderr}")
                                return
                            encov = "ac3"
                    else: 
                        # Définir le style pour l'étiquette(en rouge) de vérification de la conversion en échec                  
                        self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                        # Afficher un message d'erreur si aucun fichier compatible n'a été trouvé dans le répertoire
                        QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                        return
                    # Afficher un message de succès de la conversion
                    show_success_message()
                    # Effacer le champ de saisie pour le chemin d'entrée
                    self.path_input.clear()
                    # Réinitialiser le choix de conversion
                    self.convertaudio_choice.setCurrentText('Veuillez choisir')
                    # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                    self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                    # Mettre à jour l'interface graphique
                    self.repaint()
            elif self.convert_audio_choice == 'ogg to opus' : # Vérifie l'entré utilisteur de la QComboBox 
                    # Recherche des fichiers d'entrées dans le répertoire sélectionné et ses sous-répertoires
                    ogg_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.ogg"), recursive=True)
                    # Vérifier si les fichiers d'entré ont été trouvés dans le répertoire
                    if ogg_files:
                        # Afficher un message indiquant que la conversion est en cours
                        print("Conversion in progress ...")
                        for ogg_file in ogg_files:
                            # Définir le nom de fichier sortant en remplaçant l'extension du fichier intrant par celui du sortant 
                            opus_file = os.path.splitext(ogg_file)[0] + '.opus'
                            try:
                                # Mise à jour de l'étiquette d'état en vert, pour indiquer que la conversion est en cours
                                self.convertcheck_label.setStyleSheet("background-color: green; border-radius: 10px;")
                                # Mettre à jour l'interface graphique
                                self.repaint() 
                                # Création de la sortie de flux FFmpeg pour le fichier d'entrée
                                stream = ffmpeg.input(ogg_file)
                                # Définition des options de sortie pour la conversion
                                stream = ffmpeg.output(stream, opus_file, acodec='libopus', map_metadata=0)
                                # Lancer la conversion à l'aide de FFmpeg en mode silencieux
                                ffmpeg.run(stream, quiet=True)
                                # Afficher un message indiquant que la conversion est réussie
                                print("Conversion OK")
                            except ffmpeg.Error as e:
                                # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                                self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                                # Afficher un message d'erreur avec la raison de l'échec de la conversion
                                QMessageBox.critical(None, "Error", f"Failed to convert {ogg_file}: {e.stderr}")
                                return
                            encov = "opus"
                    else: 
                        # Définir le style pour l'étiquette(en rouge) de vérification de la conversion en échec                  
                        self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                        # Afficher un message d'erreur si aucun fichier compatible n'a été trouvé dans le répertoire
                        QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                        return
                    # Afficher un message de succès de la conversion
                    show_success_message()
                    # Effacer le champ de saisie pour le chemin d'entrée
                    self.path_input.clear()
                    # Réinitialiser le choix de conversion
                    self.convertaudio_choice.setCurrentText('Veuillez choisir')
                    # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                    self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                    # Mettre à jour l'interface graphique
                    self.repaint()
            elif self.convert_audio_choice == 'ogg to m4a': # Vérifie l'entré utilisteur de la QComboBox 
                     # Recherche des fichiers d'entrées dans le répertoire sélectionné et ses sous-répertoires
                    ogg_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.ogg"), recursive=True)
                    # Vérifier si les fichiers d'entré ont été trouvés dans le répertoire
                    if ogg_files:
                        # Afficher un message indiquant que la conversion est en cours
                        print("Conversion in progress ...")
                        for ogg_file in ogg_files:
                            # Définir le nom de fichier sortant en remplaçant l'extension du fichier intrant par celui du sortant
                            m4a_file = os.path.splitext(ogg_file)[0] + '.m4a'
                            try:
                                # Mise à jour de l'étiquette d'état en vert, pour indiquer que la conversion est en cours
                                self.convertcheck_label.setStyleSheet("background-color: green; border-radius: 10px;")
                                # Mettre à jour l'interface graphique
                                self.repaint() 
                                # Création de la sortie de flux FFmpeg pour le fichier d'entrée
                                stream = ffmpeg.input(ogg_file)
                                # Définition des options de sortie pour la conversion
                                stream = ffmpeg.output(stream, m4a_file, acodec='alac', map_metadata=0)
                                # Lancer la conversion à l'aide de FFmpeg en mode silencieux
                                ffmpeg.run(stream, quiet=True)
                                # Afficher un message indiquant que la conversion est réussie
                                print("Conversion OK")
                            except ffmpeg.Error as e:
                                # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                                self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                                # Afficher un message d'erreur avec la raison de l'échec de la conversion
                                QMessageBox.critical(None, "Error", f"Failed to convert {ogg_file}: {e.stderr}")
                                return
                            encov = "m4a"
                    else: 
                        # Définir le style pour l'étiquette(en rouge) de vérification de la conversion en échec                  
                        self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                        # Afficher un message d'erreur si aucun fichier compatible n'a été trouvé dans le répertoire
                        QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                        return
                    # Afficher un message de succès de la conversion
                    show_success_message()
                    # Effacer le champ de saisie pour le chemin d'entrée
                    self.path_input.clear()
                    # Réinitialiser le choix de conversion
                    self.convertaudio_choice.setCurrentText('Veuillez choisir')
                    # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                    self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                    # Mettre à jour l'interface graphique
                    self.repaint()
            elif self.convert_audio_choice == 'ac3 to wav': # Vérifie l'entré utilisteur de la QComboBox 
                     # Recherche des fichiers d'entrées dans le répertoire sélectionné et ses sous-répertoires
                    ac3_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.ac3"), recursive=True)
                    # Vérifier si les fichiers d'entré ont été trouvés dans le répertoire
                    if ac3_files:
                        # Afficher un message indiquant que la conversion est en cours
                        print("Conversion in progress ...")
                        for ac3_file in ac3_files:
                            # Définir le nom de fichier sortant en remplaçant l'extension du fichier intrant par celui du sortant
                            wav_file = os.path.splitext(ac3_file)[0] + '.wav'
                            try:
                                # Mise à jour de l'étiquette d'état en vert, pour indiquer que la conversion est en cours
                                self.convertcheck_label.setStyleSheet("background-color: green; border-radius: 10px;")
                                # Mettre à jour l'interface graphique
                                self.repaint() 
                                # Création de la sortie de flux FFmpeg pour le fichier d'entrée
                                stream = ffmpeg.input(ac3_file)
                                # Définition des options de sortie pour la conversion
                                stream = ffmpeg.output(stream, wav_file, map_metadata=0)
                                # Lancer la conversion à l'aide de FFmpeg en mode silencieux
                                ffmpeg.run(stream, quiet=True)
                                # Afficher un message indiquant que la conversion est réussie
                                print("Conversion OK")
                            except ffmpeg.Error as e:
                                # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                                self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                                # Afficher un message d'erreur avec la raison de l'échec de la conversion
                                QMessageBox.critical(None, "Error", f"Failed to convert {ac3_file}: {e.stderr}")
                                return
                            encov = "ac3"
                    else: 
                        # Définir le style pour l'étiquette(en rouge) de vérification de la conversion en échec                  
                        self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                        # Afficher un message d'erreur si aucun fichier compatible n'a été trouvé dans le répertoire
                        QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                        return
                    # Afficher un message de succès de la conversion
                    show_success_message()
                    # Effacer le champ de saisie pour le chemin d'entrée
                    self.path_input.clear()
                    # Réinitialiser le choix de conversion
                    self.convertaudio_choice.setCurrentText('Veuillez choisir')
                    # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                    self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                    # Mettre à jour l'interface graphique
                    self.repaint()
            elif self.convert_audio_choice == 'ac3 to aac': # Vérifie l'entré utilisteur de la QComboBox 
                     # Recherche des fichiers d'entrées dans le répertoire sélectionné et ses sous-répertoires
                    ac3_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.ac3"), recursive=True)
                    # Vérifier si les fichiers d'entré ont été trouvés dans le répertoire
                    if ac3_files:
                        # Afficher un message indiquant que la conversion est en cours
                        print("Conversion in progress ...")
                        for ac3_file in ac3_files:
                            # Définir le nom de fichier sortant en remplaçant l'extension du fichier intrant par celui du sortant
                            aac_file = os.path.splitext(ac3_file)[0] + '.aac'
                            try:
                                # Mise à jour de l'étiquette d'état en vert, pour indiquer que la conversion est en cours
                                self.convertcheck_label.setStyleSheet("background-color: green; border-radius: 10px;")
                                # Mettre à jour l'interface graphique
                                self.repaint() 
                                # Création de la sortie de flux FFmpeg pour le fichier d'entrée
                                stream = ffmpeg.input(ac3_file)
                                # Définition des options de sortie pour la conversion
                                stream = ffmpeg.output(stream, aac_file, acodec='aac', map_metadata=0)
                                # Lancer la conversion à l'aide de FFmpeg en mode silencieux
                                ffmpeg.run(stream, quiet=True)
                                # Afficher un message indiquant que la conversion est réussie
                                print("Conversion OK")
                            except ffmpeg.Error as e:
                                # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                                self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                                # Afficher un message d'erreur avec la raison de l'échec de la conversion
                                QMessageBox.critical(None, "Error", f"Failed to convert {ac3_file}: {e.stderr}")
                                return
                            encov = "aac"
                    else: 
                        # Définir le style pour l'étiquette(en rouge) de vérification de la conversion en échec                  
                        self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                        # Afficher un message d'erreur si aucun fichier compatible n'a été trouvé dans le répertoire
                        QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                        return
                    # Afficher un message de succès de la conversion
                    show_success_message()
                    # Effacer le champ de saisie pour le chemin d'entrée
                    self.path_input.clear()
                    # Réinitialiser le choix de conversion
                    self.convertaudio_choice.setCurrentText('Veuillez choisir')
                    # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                    self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                    # Mettre à jour l'interface graphique
                    self.repaint()
            elif self.convert_audio_choice == 'ac3 to mp3': # Vérifie l'entré utilisteur de la QComboBox 
                     # Recherche des fichiers d'entrées dans le répertoire sélectionné et ses sous-répertoires
                    ac3_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.ac3"), recursive=True)
                    # Vérifier si les fichiers d'entré ont été trouvés dans le répertoire
                    if ac3_files:
                        # Afficher un message indiquant que la conversion est en cours
                        print("Conversion in progress ...")
                        for ac3_file in ac3_files:
                            # Définir le nom de fichier sortant en remplaçant l'extension du fichier intrant par celui du sortant
                            mp3_file = os.path.splitext(ac3_file)[0] + '.mp3'
                            try:
                                # Mise à jour de l'étiquette d'état en vert, pour indiquer que la conversion est en cours
                                self.convertcheck_label.setStyleSheet("background-color: green; border-radius: 10px;")
                                # Mettre à jour l'interface graphique
                                self.repaint() 
                                # Création de la sortie de flux FFmpeg pour le fichier d'entrée
                                stream = ffmpeg.input(ac3_file)
                                # Définition des options de sortie pour la conversion
                                stream = ffmpeg.output(stream, mp3_file, acodec='libmp3lame', map_metadata=0)
                                # Lancer la conversion à l'aide de FFmpeg en mode silencieux
                                ffmpeg.run(stream, quiet=True)
                                # Afficher un message indiquant que la conversion est réussie
                                print("Conversion OK")
                            except ffmpeg.Error as e:
                                # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                                self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                                # Afficher un message d'erreur avec la raison de l'échec de la conversion
                                QMessageBox.critical(None, "Error", f"Failed to convert {ac3_file}: {e.stderr}")
                                return
                            encov = "aac"
                    else: 
                        # Définir le style pour l'étiquette(en rouge) de vérification de la conversion en échec                  
                        self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                        # Afficher un message d'erreur si aucun fichier compatible n'a été trouvé dans le répertoire
                        QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                        return
                    # Afficher un message de succès de la conversion
                    show_success_message()
                    # Effacer le champ de saisie pour le chemin d'entrée
                    self.path_input.clear()
                    # Réinitialiser le choix de conversion
                    self.convertaudio_choice.setCurrentText('Veuillez choisir')
                    # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                    self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                    # Mettre à jour l'interface graphique
                    self.repaint()
            elif self.convert_audio_choice == 'ac3 to ogg': # Vérifie l'entré utilisteur de la QComboBox 
                     # Recherche des fichiers d'entrées dans le répertoire sélectionné et ses sous-répertoires
                    ac3_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.ac3"), recursive=True)
                    # Vérifier si les fichiers d'entré ont été trouvés dans le répertoire
                    if ac3_files:
                        # Afficher un message indiquant que la conversion est en cours
                        print("Conversion in progress ...")
                        for ac3_file in ac3_files:
                            # Définir le nom de fichier sortant en remplaçant l'extension du fichier intrant par celui du sortant
                            ogg_file = os.path.splitext(ac3_file)[0] + '.ogg'
                            try:
                                # Mise à jour de l'étiquette d'état en vert, pour indiquer que la conversion est en cours
                                self.convertcheck_label.setStyleSheet("background-color: green; border-radius: 10px;")
                                # Mettre à jour l'interface graphique
                                self.repaint() 
                                # Création de la sortie de flux FFmpeg pour le fichier d'entrée
                                stream = ffmpeg.input(ac3_file)
                                # Définition des options de sortie pour la conversion
                                stream = ffmpeg.output(stream, ogg_file, acodec='libvorbis', map_metadata=0)
                                # Lancer la conversion à l'aide de FFmpeg en mode silencieux
                                ffmpeg.run(stream, quiet=True)
                                # Afficher un message indiquant que la conversion est réussie
                                print("Conversion OK")
                            except ffmpeg.Error as e:
                                # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                                self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                                # Afficher un message d'erreur avec la raison de l'échec de la conversion
                                QMessageBox.critical(None, "Error", f"Failed to convert {ac3_file}: {e.stderr}")
                                return
                            encov = "ogg"
                    else: 
                        # Définir le style pour l'étiquette(en rouge) de vérification de la conversion en échec                  
                        self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                        # Afficher un message d'erreur si aucun fichier compatible n'a été trouvé dans le répertoire
                        QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                        return
                    # Afficher un message de succès de la conversion
                    show_success_message()
                    # Effacer le champ de saisie pour le chemin d'entrée
                    self.path_input.clear()
                    # Réinitialiser le choix de conversion
                    self.convertaudio_choice.setCurrentText('Veuillez choisir')
                    # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                    self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                    # Mettre à jour l'interface graphique
                    self.repaint()
            elif self.convert_audio_choice == 'ac3 to opus' : # Vérifie l'entré utilisteur de la QComboBox 
                    # Recherche des fichiers d'entrées dans le répertoire sélectionné et ses sous-répertoires
                    ac3_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.ac3"), recursive=True)
                    # Vérifier si les fichiers d'entré ont été trouvés dans le répertoire
                    if ac3_files:
                        # Afficher un message indiquant que la conversion est en cours
                        print("Conversion in progress ...")
                        for ac3_file in ac3_files:
                            # Définir le nom de fichier sortant en remplaçant l'extension du fichier intrant par celui du sortant 
                            opus_file = os.path.splitext(ac3_file)[0] + '.opus'
                            try:
                                # Mise à jour de l'étiquette d'état en vert, pour indiquer que la conversion est en cours
                                self.convertcheck_label.setStyleSheet("background-color: green; border-radius: 10px;")
                                # Mettre à jour l'interface graphique
                                self.repaint() 
                                # Création de la sortie de flux FFmpeg pour le fichier d'entrée
                                stream = ffmpeg.input(ac3_file)
                                # Définition des options de sortie pour la conversion
                                stream = ffmpeg.output(stream, opus_file, acodec='libopus', map_metadata=0)
                                # Lancer la conversion à l'aide de FFmpeg en mode silencieux
                                ffmpeg.run(stream, quiet=True)
                                # Afficher un message indiquant que la conversion est réussie
                                print("Conversion OK")
                            except ffmpeg.Error as e:
                                # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                                self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                                # Afficher un message d'erreur avec la raison de l'échec de la conversion
                                QMessageBox.critical(None, "Error", f"Failed to convert {ac3_file}: {e.stderr}")
                                return
                            encov = "opus"
                    else: 
                        # Définir le style pour l'étiquette(en rouge) de vérification de la conversion en échec                  
                        self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                        # Afficher un message d'erreur si aucun fichier compatible n'a été trouvé dans le répertoire
                        QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                        return
                    # Afficher un message de succès de la conversion
                    show_success_message()
                    # Effacer le champ de saisie pour le chemin d'entrée
                    self.path_input.clear()
                    # Réinitialiser le choix de conversion
                    self.convertaudio_choice.setCurrentText('Veuillez choisir')
                    # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                    self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                    # Mettre à jour l'interface graphique
                    self.repaint()
            elif self.convert_audio_choice == 'ac3 to m4a': # Vérifie l'entré utilisteur de la QComboBox 
                     # Recherche des fichiers d'entrées dans le répertoire sélectionné et ses sous-répertoires
                    ac3_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.ac3"), recursive=True)
                    # Vérifier si les fichiers d'entré ont été trouvés dans le répertoire
                    if ac3_files:
                        # Afficher un message indiquant que la conversion est en cours
                        print("Conversion in progress ...")
                        for ac3_file in ac3_files:
                            # Définir le nom de fichier sortant en remplaçant l'extension du fichier intrant par celui du sortant
                            m4a_file = os.path.splitext(ac3_file)[0] + '.m4a'
                            try:
                                # Mise à jour de l'étiquette d'état en vert, pour indiquer que la conversion est en cours
                                self.convertcheck_label.setStyleSheet("background-color: green; border-radius: 10px;")
                                # Mettre à jour l'interface graphique
                                self.repaint() 
                                # Création de la sortie de flux FFmpeg pour le fichier d'entrée
                                stream = ffmpeg.input(ac3_file)
                                # Définition des options de sortie pour la conversion
                                stream = ffmpeg.output(stream, m4a_file, acodec='alac', map_metadata=0)
                                # Lancer la conversion à l'aide de FFmpeg en mode silencieux
                                ffmpeg.run(stream, quiet=True)
                                # Afficher un message indiquant que la conversion est réussie
                                print("Conversion OK")
                            except ffmpeg.Error as e:
                                # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                                self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                                # Afficher un message d'erreur avec la raison de l'échec de la conversion
                                QMessageBox.critical(None, "Error", f"Failed to convert {ac3_file}: {e.stderr}")
                                return
                            encov = "m4a"
                    else: 
                        # Définir le style pour l'étiquette(en rouge) de vérification de la conversion en échec                  
                        self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                        # Afficher un message d'erreur si aucun fichier compatible n'a été trouvé dans le répertoire
                        QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                        return
                    # Afficher un message de succès de la conversion
                    show_success_message()
                    # Effacer le champ de saisie pour le chemin d'entrée
                    self.path_input.clear()
                    # Réinitialiser le choix de conversion
                    self.convertaudio_choice.setCurrentText('Veuillez choisir')
                    # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                    self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                    # Mettre à jour l'interface graphique
                    self.repaint()
            elif self.convert_audio_choice == 'aac to wav': # Vérifie l'entré utilisteur de la QComboBox 
                     # Recherche des fichiers d'entrées dans le répertoire sélectionné et ses sous-répertoires
                    aac_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.aac"), recursive=True)
                    # Vérifier si les fichiers d'entré ont été trouvés dans le répertoire
                    if aac_files:
                        # Afficher un message indiquant que la conversion est en cours
                        print("Conversion in progress ...")
                        for aac_file in aac_files:
                            # Définir le nom de fichier sortant en remplaçant l'extension du fichier intrant par celui du sortant
                            wav_file = os.path.splitext(aac_file)[0] + '.wav'
                            try:
                                # Mise à jour de l'étiquette d'état en vert, pour indiquer que la conversion est en cours
                                self.convertcheck_label.setStyleSheet("background-color: green; border-radius: 10px;")
                                # Mettre à jour l'interface graphique
                                self.repaint() 
                                # Création de la sortie de flux FFmpeg pour le fichier d'entrée
                                stream = ffmpeg.input(aac_file)
                                # Définition des options de sortie pour la conversion
                                stream = ffmpeg.output(stream, wav_file, map_metadata=0)
                                # Lancer la conversion à l'aide de FFmpeg en mode silencieux
                                ffmpeg.run(stream, quiet=True)
                                # Afficher un message indiquant que la conversion est réussie
                                print("Conversion OK")
                            except ffmpeg.Error as e:
                                # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                                self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                                # Afficher un message d'erreur avec la raison de l'échec de la conversion
                                QMessageBox.critical(None, "Error", f"Failed to convert {aac_file}: {e.stderr}")
                                return
                            encov = "aac"
                    else: 
                        # Définir le style pour l'étiquette(en rouge) de vérification de la conversion en échec                  
                        self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                        # Afficher un message d'erreur si aucun fichier compatible n'a été trouvé dans le répertoire
                        QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                        return
                    # Afficher un message de succès de la conversion
                    show_success_message()
                    # Effacer le champ de saisie pour le chemin d'entrée
                    self.path_input.clear()
                    # Réinitialiser le choix de conversion
                    self.convertaudio_choice.setCurrentText('Veuillez choisir')
                    # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                    self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                    # Mettre à jour l'interface graphique
                    self.repaint()
            elif self.convert_audio_choice == 'aac to ac3': # Vérifie l'entré utilisteur de la QComboBox 
                     # Recherche des fichiers d'entrées dans le répertoire sélectionné et ses sous-répertoires
                    aac_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.aac"), recursive=True)
                    # Vérifier si les fichiers d'entré ont été trouvés dans le répertoire
                    if aac_files:
                        # Afficher un message indiquant que la conversion est en cours
                        print("Conversion in progress ...")
                        for aac_file in aac_files:
                            # Définir le nom de fichier sortant en remplaçant l'extension du fichier intrant par celui du sortant
                            ac3_file = os.path.splitext(aac_file)[0] + '.ac3'
                            try:
                                # Mise à jour de l'étiquette d'état en vert, pour indiquer que la conversion est en cours
                                self.convertcheck_label.setStyleSheet("background-color: green; border-radius: 10px;")
                                # Mettre à jour l'interface graphique
                                self.repaint() 
                                # Création de la sortie de flux FFmpeg pour le fichier d'entrée
                                stream = ffmpeg.input(aac_file)
                                # Définition des options de sortie pour la conversion
                                stream = ffmpeg.output(stream, ac3_file, acodec='ac3', map_metadata=0)
                                # Lancer la conversion à l'aide de FFmpeg en mode silencieux
                                ffmpeg.run(stream, quiet=True)
                                # Afficher un message indiquant que la conversion est réussie
                                print("Conversion OK")
                            except ffmpeg.Error as e:
                                # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                                self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                                # Afficher un message d'erreur avec la raison de l'échec de la conversion
                                QMessageBox.critical(None, "Error", f"Failed to convert {aac_file}: {e.stderr}")
                                return
                            encov = "ac3"
                    else: 
                        # Définir le style pour l'étiquette(en rouge) de vérification de la conversion en échec                  
                        self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                        # Afficher un message d'erreur si aucun fichier compatible n'a été trouvé dans le répertoire
                        QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                        return
                    # Afficher un message de succès de la conversion
                    show_success_message()
                    # Effacer le champ de saisie pour le chemin d'entrée
                    self.path_input.clear()
                    # Réinitialiser le choix de conversion
                    self.convertaudio_choice.setCurrentText('Veuillez choisir')
                    # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                    self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                    # Mettre à jour l'interface graphique
                    self.repaint()
            elif self.convert_audio_choice == 'aac to mp3': # Vérifie l'entré utilisteur de la QComboBox 
                     # Recherche des fichiers d'entrées dans le répertoire sélectionné et ses sous-répertoires
                    aac_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.aac"), recursive=True)
                    # Vérifier si les fichiers d'entré ont été trouvés dans le répertoire
                    if aac_files:
                        # Afficher un message indiquant que la conversion est en cours
                        print("Conversion in progress ...")
                        for aac_file in aac_files:
                            # Définir le nom de fichier sortant en remplaçant l'extension du fichier intrant par celui du sortant
                            mp3_file = os.path.splitext(aac_file)[0] + '.mp3'
                            try:
                                # Mise à jour de l'étiquette d'état en vert, pour indiquer que la conversion est en cours
                                self.convertcheck_label.setStyleSheet("background-color: green; border-radius: 10px;")
                                # Mettre à jour l'interface graphique
                                self.repaint() 
                                # Création de la sortie de flux FFmpeg pour le fichier d'entrée
                                stream = ffmpeg.input(aac_file)
                                # Définition des options de sortie pour la conversion
                                stream = ffmpeg.output(stream, mp3_file, acodec='libmp3lame', map_metadata=0)
                                # Lancer la conversion à l'aide de FFmpeg en mode silencieux
                                ffmpeg.run(stream, quiet=True)
                                # Afficher un message indiquant que la conversion est réussie
                                print("Conversion OK")
                            except ffmpeg.Error as e:
                                # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                                self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                                # Afficher un message d'erreur avec la raison de l'échec de la conversion
                                QMessageBox.critical(None, "Error", f"Failed to convert {aac_file}: {e.stderr}")
                                return
                            encov = "aac"
                    else: 
                        # Définir le style pour l'étiquette(en rouge) de vérification de la conversion en échec                  
                        self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                        # Afficher un message d'erreur si aucun fichier compatible n'a été trouvé dans le répertoire
                        QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                        return
                    # Afficher un message de succès de la conversion
                    show_success_message()
                    # Effacer le champ de saisie pour le chemin d'entrée
                    self.path_input.clear()
                    # Réinitialiser le choix de conversion
                    self.convertaudio_choice.setCurrentText('Veuillez choisir')
                    # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                    self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                    # Mettre à jour l'interface graphique
                    self.repaint()
            elif self.convert_audio_choice == 'aac to ogg': # Vérifie l'entré utilisteur de la QComboBox 
                     # Recherche des fichiers d'entrées dans le répertoire sélectionné et ses sous-répertoires
                    aac_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.aac"), recursive=True)
                    # Vérifier si les fichiers d'entré ont été trouvés dans le répertoire
                    if aac_files:
                        # Afficher un message indiquant que la conversion est en cours
                        print("Conversion in progress ...")
                        for aac_file in aac_files:
                            # Définir le nom de fichier sortant en remplaçant l'extension du fichier intrant par celui du sortant
                            ogg_file = os.path.splitext(aac_file)[0] + '.ogg'
                            try:
                                # Mise à jour de l'étiquette d'état en vert, pour indiquer que la conversion est en cours
                                self.convertcheck_label.setStyleSheet("background-color: green; border-radius: 10px;")
                                # Mettre à jour l'interface graphique
                                self.repaint() 
                                # Création de la sortie de flux FFmpeg pour le fichier d'entrée
                                stream = ffmpeg.input(aac_file)
                                # Définition des options de sortie pour la conversion
                                stream = ffmpeg.output(stream, ogg_file, acodec='libvorbis', map_metadata=0)
                                # Lancer la conversion à l'aide de FFmpeg en mode silencieux
                                ffmpeg.run(stream, quiet=True)
                                # Afficher un message indiquant que la conversion est réussie
                                print("Conversion OK")
                            except ffmpeg.Error as e:
                                # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                                self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                                # Afficher un message d'erreur avec la raison de l'échec de la conversion
                                QMessageBox.critical(None, "Error", f"Failed to convert {aac_file}: {e.stderr}")
                                return
                            encov = "ogg"
                    else: 
                        # Définir le style pour l'étiquette(en rouge) de vérification de la conversion en échec                  
                        self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                        # Afficher un message d'erreur si aucun fichier compatible n'a été trouvé dans le répertoire
                        QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                        return
                    # Afficher un message de succès de la conversion
                    show_success_message()
                    # Effacer le champ de saisie pour le chemin d'entrée
                    self.path_input.clear()
                    # Réinitialiser le choix de conversion
                    self.convertaudio_choice.setCurrentText('Veuillez choisir')
                    # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                    self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                    # Mettre à jour l'interface graphique
                    self.repaint()
            elif self.convert_audio_choice == 'aac to opus' : # Vérifie l'entré utilisteur de la QComboBox 
                    # Recherche des fichiers d'entrées dans le répertoire sélectionné et ses sous-répertoires
                    aac_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.aac"), recursive=True)
                    # Vérifier si les fichiers d'entré ont été trouvés dans le répertoire
                    if aac_files:
                        # Afficher un message indiquant que la conversion est en cours
                        print("Conversion in progress ...")
                        for aac_file in aac_files:
                            # Définir le nom de fichier sortant en remplaçant l'extension du fichier intrant par celui du sortant 
                            opus_file = os.path.splitext(aac_file)[0] + '.opus'
                            try:
                                # Mise à jour de l'étiquette d'état en vert, pour indiquer que la conversion est en cours
                                self.convertcheck_label.setStyleSheet("background-color: green; border-radius: 10px;")
                                # Mettre à jour l'interface graphique
                                self.repaint() 
                                # Création de la sortie de flux FFmpeg pour le fichier d'entrée
                                stream = ffmpeg.input(aac_file)
                                # Définition des options de sortie pour la conversion
                                stream = ffmpeg.output(stream, opus_file, acodec='libopus', map_metadata=0)
                                # Lancer la conversion à l'aide de FFmpeg en mode silencieux
                                ffmpeg.run(stream, quiet=True)
                                # Afficher un message indiquant que la conversion est réussie
                                print("Conversion OK")
                            except ffmpeg.Error as e:
                                # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                                self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                                # Afficher un message d'erreur avec la raison de l'échec de la conversion
                                QMessageBox.critical(None, "Error", f"Failed to convert {aac_file}: {e.stderr}")
                                return
                            encov = "opus"
                    else: 
                        # Définir le style pour l'étiquette(en rouge) de vérification de la conversion en échec                  
                        self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                        # Afficher un message d'erreur si aucun fichier compatible n'a été trouvé dans le répertoire
                        QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                        return
                    # Afficher un message de succès de la conversion
                    show_success_message()
                    # Effacer le champ de saisie pour le chemin d'entrée
                    self.path_input.clear()
                    # Réinitialiser le choix de conversion
                    self.convertaudio_choice.setCurrentText('Veuillez choisir')
                    # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                    self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                    # Mettre à jour l'interface graphique
                    self.repaint()
            elif self.convert_audio_choice == 'aac to m4a' : # Vérifie l'entré utilisteur de la QComboBox 
                     # Recherche des fichiers d'entrées dans le répertoire sélectionné et ses sous-répertoires
                    aac_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.aac"), recursive=True)
                    # Vérifier si les fichiers d'entré ont été trouvés dans le répertoire
                    if aac_files:
                        # Afficher un message indiquant que la conversion est en cours
                        print("Conversion in progress ...")
                        for aac_file in aac_files:
                            # Définir le nom de fichier sortant en remplaçant l'extension du fichier intrant par celui du sortant
                            m4a_file = os.path.splitext(aac_file)[0] + '.m4a'
                            try:
                                # Mise à jour de l'étiquette d'état en vert, pour indiquer que la conversion est en cours
                                self.convertcheck_label.setStyleSheet("background-color: green; border-radius: 10px;")
                                # Mettre à jour l'interface graphique
                                self.repaint() 
                                # Création de la sortie de flux FFmpeg pour le fichier d'entrée
                                stream = ffmpeg.input(aac_file)
                                # Définition des options de sortie pour la conversion
                                stream = ffmpeg.output(stream, m4a_file, acodec='alac', map_metadata=0)
                                # Lancer la conversion à l'aide de FFmpeg en mode silencieux
                                ffmpeg.run(stream, quiet=True)
                                # Afficher un message indiquant que la conversion est réussie
                                print("Conversion OK")
                            except ffmpeg.Error as e:
                                # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                                self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                                # Afficher un message d'erreur avec la raison de l'échec de la conversion
                                QMessageBox.critical(None, "Error", f"Failed to convert {aac_file}: {e.stderr}")
                                return
                            encov = "m4a"
                    else: 
                        # Définir le style pour l'étiquette(en rouge) de vérification de la conversion en échec                  
                        self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                        # Afficher un message d'erreur si aucun fichier compatible n'a été trouvé dans le répertoire
                        QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                        return
                    # Afficher un message de succès de la conversion
                    show_success_message()
                    # Effacer le champ de saisie pour le chemin d'entrée
                    self.path_input.clear()
                    # Réinitialiser le choix de conversion
                    self.convertaudio_choice.setCurrentText('Veuillez choisir')
                    # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                    self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                    # Mettre à jour l'interface graphique
                    self.repaint()
            elif self.convert_audio_choice == 'flac to wav' : # Vérifie l'entré utilisteur de la QComboBox 
                    # Recherche des fichiers d'entrées dans le répertoire sélectionné et ses sous-répertoires
                    flac_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.flac"), recursive=True)
                    # Vérifier si les fichiers d'entré ont été trouvés dans le répertoire
                    if flac_files:
                        # Afficher un message indiquant que la conversion est en cours
                        print("Conversion in progress ...")
                        for flac_file in flac_files:
                            # Définir le nom de fichier sortant en remplaçant l'extension du fichier intrant par celui du sortant
                            wav_file = os.path.splitext(flac_file)[0] + '.wav'
                            try:
                                # Mise à jour de l'étiquette d'état en vert, pour indiquer que la conversion est en cours
                                self.convertcheck_label.setStyleSheet("background-color: green; border-radius: 10px;")
                                # Mettre à jour l'interface graphique
                                self.repaint() 
                                # Création de la sortie de flux FFmpeg pour le fichier d'entrée
                                stream = ffmpeg.input(flac_file)
                                # Définition des options de sortie pour la conversion
                                stream = ffmpeg.output(stream, wav_file, map_metadata=0)
                                # Lancer la conversion à l'aide de FFmpeg en mode silencieux
                                ffmpeg.run(stream, quiet=True)
                                # Afficher un message indiquant que la conversion est réussie
                                print("Conversion OK")
                            except ffmpeg.Error as e:
                                # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                                self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                                # Afficher un message d'erreur avec la raison de l'échec de la conversion
                                QMessageBox.critical(None, "Error", f"Failed to convert {flac_file}: {e.stderr}")
                                return
                            encov = "flac"
                    else: 
                        # Définir le style pour l'étiquette(en rouge) de vérification de la conversion en échec                  
                        self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                        # Afficher un message d'erreur si aucun fichier compatible n'a été trouvé dans le répertoire
                        QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                        return
                    # Afficher un message de succès de la conversion
                    show_success_message()
                    # Effacer le champ de saisie pour le chemin d'entrée
                    self.path_input.clear()
                    # Réinitialiser le choix de conversion
                    self.convertaudio_choice.setCurrentText('Veuillez choisir')
                    # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                    self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                    # Mettre à jour l'interface graphique
                    self.repaint()
            elif self.convert_audio_choice == 'flac to ac3' : # Vérifie l'entré utilisteur de la QComboBox 
                    # Recherche des fichiers d'entrées dans le répertoire sélectionné et ses sous-répertoires
                    flac_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.flac"), recursive=True)
                    # Vérifier si les fichiers d'entré ont été trouvés dans le répertoire
                    if flac_files:
                        # Afficher un message indiquant que la conversion est en cours
                        print("Conversion in progress ...")
                        for flac_file in flac_files:
                            # Définir le nom de fichier sortant en remplaçant l'extension du fichier intrant par celui du sortant
                            ac3_file = os.path.splitext(flac_file)[0] + '.ac3'
                            try:
                                # Mise à jour de l'étiquette d'état en vert, pour indiquer que la conversion est en cours
                                self.convertcheck_label.setStyleSheet("background-color: green; border-radius: 10px;")
                                # Mettre à jour l'interface graphique
                                self.repaint() 
                                # Création de la sortie de flux FFmpeg pour le fichier d'entrée
                                stream = ffmpeg.input(flac_file)
                                # Définition des options de sortie pour la conversion
                                stream = ffmpeg.output(stream, ac3_file, acodec='ac3', map_metadata=0)
                                # Lancer la conversion à l'aide de FFmpeg en mode silencieux
                                ffmpeg.run(stream, quiet=True)
                                # Afficher un message indiquant que la conversion est réussie
                                print("Conversion OK")
                            except ffmpeg.Error as e:
                                # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                                self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                                # Afficher un message d'erreur avec la raison de l'échec de la conversion
                                QMessageBox.critical(None, "Error", f"Failed to convert {flac_file}: {e.stderr}")
                                return
                            encov = "ac3"
                    else: 
                        # Définir le style pour l'étiquette(en rouge) de vérification de la conversion en échec                  
                        self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                        # Afficher un message d'erreur si aucun fichier compatible n'a été trouvé dans le répertoire
                        QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                        return
                    # Afficher un message de succès de la conversion
                    show_success_message()
                    # Effacer le champ de saisie pour le chemin d'entrée
                    self.path_input.clear()
                    # Réinitialiser le choix de conversion
                    self.convertaudio_choice.setCurrentText('Veuillez choisir')
                    # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                    self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                    # Mettre à jour l'interface graphique
                    self.repaint()
            elif self.convert_audio_choice == 'flac to mp3' : # Vérifie l'entré utilisteur de la QComboBox 
                    # Recherche des fichiers d'entrées dans le répertoire sélectionné et ses sous-répertoires
                    flac_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.flac"), recursive=True)
                    # Vérifier si les fichiers d'entré ont été trouvés dans le répertoire
                    if flac_files:
                        # Afficher un message indiquant que la conversion est en cours
                        print("Conversion in progress ...")
                        for flac_file in flac_files:
                            # Définir le nom de fichier sortant en remplaçant l'extension du fichier intrant par celui du sortant
                            mp3_file = os.path.splitext(flac_file)[0] + '.mp3'
                            try:
                                # Mise à jour de l'étiquette d'état en vert, pour indiquer que la conversion est en cours
                                self.convertcheck_label.setStyleSheet("background-color: green; border-radius: 10px;")
                                # Mettre à jour l'interface graphique
                                self.repaint() 
                                # Création de la sortie de flux FFmpeg pour le fichier d'entrée
                                stream = ffmpeg.input(flac_file)
                                # Définition des options de sortie pour la conversion
                                stream = ffmpeg.output(stream, mp3_file, acodec='libmp3lame', map_metadata=0)
                                # Lancer la conversion à l'aide de FFmpeg en mode silencieux
                                ffmpeg.run(stream, quiet=True)
                                # Afficher un message indiquant que la conversion est réussie
                                print("Conversion OK")
                            except ffmpeg.Error as e:
                                # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                                self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                                # Afficher un message d'erreur avec la raison de l'échec de la conversion
                                QMessageBox.critical(None, "Error", f"Failed to convert {flac_file}: {e.stderr}")
                                return
                            encov = "mp3"
                    else: 
                        # Définir le style pour l'étiquette(en rouge) de vérification de la conversion en échec                  
                        self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                        # Afficher un message d'erreur si aucun fichier compatible n'a été trouvé dans le répertoire
                        QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                        return
                    # Afficher un message de succès de la conversion
                    show_success_message()
                    # Effacer le champ de saisie pour le chemin d'entrée
                    self.path_input.clear()
                    # Réinitialiser le choix de conversion
                    self.convertaudio_choice.setCurrentText('Veuillez choisir')
                    # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                    self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                    # Mettre à jour l'interface graphique
                    self.repaint()
            elif self.convert_audio_choice == 'flac to ogg' : # Vérifie l'entré utilisteur de la QComboBox 
                    # Recherche des fichiers d'entrées dans le répertoire sélectionné et ses sous-répertoires
                    flac_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.flac"), recursive=True)
                    # Vérifier si les fichiers d'entré ont été trouvés dans le répertoire
                    if flac_files:
                        # Afficher un message indiquant que la conversion est en cours
                        print("Conversion in progress ...")
                        for flac_file in flac_files:
                            # Définir le nom de fichier sortant en remplaçant l'extension du fichier intrant par celui du sortant
                            ogg_file = os.path.splitext(flac_file)[0] + '.ogg'
                            try:
                                # Mise à jour de l'étiquette d'état en vert, pour indiquer que la conversion est en cours
                                self.convertcheck_label.setStyleSheet("background-color: green; border-radius: 10px;")
                                # Mettre à jour l'interface graphique
                                self.repaint() 
                                # Création de la sortie de flux FFmpeg pour le fichier d'entrée
                                stream = ffmpeg.input(flac_file)
                                # Définition des options de sortie pour la conversion
                                stream = ffmpeg.output(stream, ogg_file, acodec='libvorbis', map_metadata=0)
                                # Lancer la conversion à l'aide de FFmpeg en mode silencieux
                                ffmpeg.run(stream, quiet=True)
                                # Afficher un message indiquant que la conversion est réussie
                                print("Conversion OK")
                            except ffmpeg.Error as e:
                                # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                                self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                                # Afficher un message d'erreur avec la raison de l'échec de la conversion
                                QMessageBox.critical(None, "Error", f"Failed to convert {flac_file}: {e.stderr}")
                                return
                            encov = "ogg"
                    else: 
                        # Définir le style pour l'étiquette(en rouge) de vérification de la conversion en échec                  
                        self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                        # Afficher un message d'erreur si aucun fichier compatible n'a été trouvé dans le répertoire
                        QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                        return
                    # Afficher un message de succès de la conversion
                    show_success_message()
                    # Effacer le champ de saisie pour le chemin d'entrée
                    self.path_input.clear()
                    # Réinitialiser le choix de conversion
                    self.convertaudio_choice.setCurrentText('Veuillez choisir')
                    # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                    self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                    # Mettre à jour l'interface graphique
                    self.repaint()
            elif self.convert_audio_choice == 'flac to opus ' : # Vérifie l'entré utilisteur de la QComboBox
                    # Recherche des fichiers d'entrées dans le répertoire sélectionné et ses sous-répertoires
                    flac_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.flac"), recursive=True)
                    # Vérifier si les fichiers d'entré ont été trouvés dans le répertoire
                    if flac_files:
                        # Afficher un message indiquant que la conversion est en cours
                        print("Conversion in progress ...")
                        for flac_file in flac_files:
                            # Définir le nom de fichier sortant en remplaçant l'extension du fichier intrant par celui du sortant 
                            opus_file = os.path.splitext(flac_file)[0] + '.opus'
                            try:
                                # Mise à jour de l'étiquette d'état en vert, pour indiquer que la conversion est en cours
                                self.convertcheck_label.setStyleSheet("background-color: green; border-radius: 10px;")
                                # Mettre à jour l'interface graphique
                                self.repaint() 
                                # Création de la sortie de flux FFmpeg pour le fichier d'entrée
                                stream = ffmpeg.input(flac_file)
                                # Définition des options de sortie pour la conversion
                                stream = ffmpeg.output(stream, opus_file, acodec='libopus', map_metadata=0)
                                # Lancer la conversion à l'aide de FFmpeg en mode silencieux
                                ffmpeg.run(stream, quiet=True)
                                # Afficher un message indiquant que la conversion est réussie
                                print("Conversion OK")
                            except ffmpeg.Error as e:
                                # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                                self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                                # Afficher un message d'erreur avec la raison de l'échec de la conversion
                                QMessageBox.critical(None, "Error", f"Failed to convert {flac_file}: {e.stderr}")
                                return
                            encov = "opus"
                    else: 
                        # Définir le style pour l'étiquette(en rouge) de vérification de la conversion en échec                  
                        self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                        # Afficher un message d'erreur si aucun fichier compatible n'a été trouvé dans le répertoire
                        QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                        return
                    # Afficher un message de succès de la conversion
                    show_success_message()
                    # Effacer le champ de saisie pour le chemin d'entrée
                    self.path_input.clear()
                    # Réinitialiser le choix de conversion
                    self.convertaudio_choice.setCurrentText('Veuillez choisir')
                    # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                    self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                    # Mettre à jour l'interface graphique
                    self.repaint()
            elif self.convert_audio_choice == 'flac to m4a' : # Vérifie l'entré utilisteur de la QComboBox 
                    # Recherche des fichiers d'entrées dans le répertoire sélectionné et ses sous-répertoires
                    flac_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.flac"), recursive=True)
                    # Vérifier si les fichiers d'entré ont été trouvés dans le répertoire
                    if flac_files:
                        # Afficher un message indiquant que la conversion est en cours
                        print("Conversion in progress ...")
                        for flac_file in flac_files:
                            # Définir le nom de fichier sortant en remplaçant l'extension du fichier intrant par celui du sortant
                            m4a_file = os.path.splitext(flac_file)[0] + '.m4a'
                            try:
                                # Mise à jour de l'étiquette d'état en vert, pour indiquer que la conversion est en cours
                                self.convertcheck_label.setStyleSheet("background-color: green; border-radius: 10px;")
                                # Mettre à jour l'interface graphique
                                self.repaint() 
                                # Création de la sortie de flux FFmpeg pour le fichier d'entrée
                                stream = ffmpeg.input(flac_file)
                                # Définition des options de sortie pour la conversion
                                stream = ffmpeg.output(stream, m4a_file, acodec='alac', map_metadata=0)
                                # Lancer la conversion à l'aide de FFmpeg en mode silencieux
                                ffmpeg.run(stream, quiet=True)
                                # Afficher un message indiquant que la conversion est réussie
                                print("Conversion OK")
                            except ffmpeg.Error as e:
                                # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                                self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                                # Afficher un message d'erreur avec la raison de l'échec de la conversion
                                QMessageBox.critical(None, "Error", f"Failed to convert {flac_file}: {e.stderr}")
                                return
                            encov = "m4a"
                    else: 
                        # Définir le style pour l'étiquette(en rouge) de vérification de la conversion en échec                  
                        self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                        # Afficher un message d'erreur si aucun fichier compatible n'a été trouvé dans le répertoire
                        QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                        return
                    # Afficher un message de succès de la conversion
                    show_success_message()
                    # Effacer le champ de saisie pour le chemin d'entrée
                    self.path_input.clear()
                    # Réinitialiser le choix de conversion
                    self.convertaudio_choice.setCurrentText('Veuillez choisir')
                    # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                    self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                    # Mettre à jour l'interface graphique
                    self.repaint()
            elif self.convert_audio_choice == 'flac to aac' : # Vérifie l'entré utilisteur de la QComboBox 
                    # Recherche des fichiers d'entrées dans le répertoire sélectionné et ses sous-répertoires
                    flac_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.flac"), recursive=True)
                    # Vérifier si les fichiers d'entré ont été trouvés dans le répertoire
                    if flac_files:
                        # Afficher un message indiquant que la conversion est en cours
                        print("Conversion in progress ...")
                        for flac_file in flac_files:
                            # Définir le nom de fichier sortant en remplaçant l'extension du fichier intrant par celui du sortant
                            aac_file = os.path.splitext(flac_file)[0] + '.aac'
                            try:
                                # Mise à jour de l'étiquette d'état en vert, pour indiquer que la conversion est en cours
                                self.convertcheck_label.setStyleSheet("background-color: green; border-radius: 10px;")
                                # Mettre à jour l'interface graphique
                                self.repaint() 
                                # Création de la sortie de flux FFmpeg pour le fichier d'entrée
                                stream = ffmpeg.input(flac_file)
                                # Définition des options de sortie pour la conversion
                                stream = ffmpeg.output(stream, aac_file, acodec='aac', map_metadata=0)
                                # Lancer la conversion à l'aide de FFmpeg en mode silencieux
                                ffmpeg.run(stream, quiet=True)
                                # Afficher un message indiquant que la conversion est réussie
                                print("Conversion OK")
                            except ffmpeg.Error as e:
                                # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                                self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                                # Afficher un message d'erreur avec la raison de l'échec de la conversion
                                QMessageBox.critical(None, "Error", f"Failed to convert {flac_file}: {e.stderr}")
                                return
                            encov = "aac"
                    else: 
                        # Définir le style pour l'étiquette(en rouge) de vérification de la conversion en échec                  
                        self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                        # Afficher un message d'erreur si aucun fichier compatible n'a été trouvé dans le répertoire
                        QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                        return
                    # Afficher un message de succès de la conversion
                    show_success_message()
                    # Effacer le champ de saisie pour le chemin d'entrée
                    self.path_input.clear()
                    # Réinitialiser le choix de conversion
                    self.convertaudio_choice.setCurrentText('Veuillez choisir')
                    # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                    self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                    # Mettre à jour l'interface graphique
                    self.repaint()
            elif self.convert_audio_choice == 'opus to wav' : # Vérifie l'entré utilisteur de la QComboBox 
                    # Recherche des fichiers d'entrées dans le répertoire sélectionné et ses sous-répertoires
                    opus_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.opus"), recursive=True)
                    # Vérifier si les fichiers d'entré ont été trouvés dans le répertoire
                    if opus_files:
                        # Afficher un message indiquant que la conversion est en cours
                        print("Conversion in progress ...")
                        for opus_file in opus_files:
                            # Définir le nom de fichier sortant en remplaçant l'extension du fichier intrant par celui du sortant
                            wav_file = os.path.splitext(opus_file)[0] + '.wav'
                            try:
                                # Mise à jour de l'étiquette d'état en vert, pour indiquer que la conversion est en cours
                                self.convertcheck_label.setStyleSheet("background-color: green; border-radius: 10px;")
                                # Mettre à jour l'interface graphique
                                self.repaint() 
                                # Création de la sortie de flux FFmpeg pour le fichier d'entrée
                                stream = ffmpeg.input(opus_file)
                                # Définition des options de sortie pour la conversion
                                stream = ffmpeg.output(stream, wav_file, map_metadata=0)
                                # Lancer la conversion à l'aide de FFmpeg en mode silencieux
                                ffmpeg.run(stream, quiet=True)
                                # Afficher un message indiquant que la conversion est réussie
                                print("Conversion OK")
                            except ffmpeg.Error as e:
                                # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                                self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                                # Afficher un message d'erreur avec la raison de l'échec de la conversion
                                QMessageBox.critical(None, "Error", f"Failed to convert {opus_file}: {e.stderr}")
                                return
                            encov = "opus"
                    else: 
                        # Définir le style pour l'étiquette(en rouge) de vérification de la conversion en échec                  
                        self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                        # Afficher un message d'erreur si aucun fichier compatible n'a été trouvé dans le répertoire
                        QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                        return
                    # Afficher un message de succès de la conversion
                    show_success_message()
                    # Effacer le champ de saisie pour le chemin d'entrée
                    self.path_input.clear()
                    # Réinitialiser le choix de conversion
                    self.convertaudio_choice.setCurrentText('Veuillez choisir')
                    # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                    self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                    # Mettre à jour l'interface graphique
                    self.repaint()
            elif self.convert_audio_choice == 'opus to ac3' : # Vérifie l'entré utilisteur de la QComboBox 
                    # Recherche des fichiers d'entrées dans le répertoire sélectionné et ses sous-répertoires
                    opus_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.opus"), recursive=True)
                    # Vérifier si les fichiers d'entré ont été trouvés dans le répertoire
                    if opus_files:
                        # Afficher un message indiquant que la conversion est en cours
                        print("Conversion in progress ...")
                        for opus_file in opus_files:
                            # Définir le nom de fichier sortant en remplaçant l'extension du fichier intrant par celui du sortant
                            ac3_file = os.path.splitext(opus_file)[0] + '.ac3'
                            try:
                                # Mise à jour de l'étiquette d'état en vert, pour indiquer que la conversion est en cours
                                self.convertcheck_label.setStyleSheet("background-color: green; border-radius: 10px;")
                                # Mettre à jour l'interface graphique
                                self.repaint() 
                                # Création de la sortie de flux FFmpeg pour le fichier d'entrée
                                stream = ffmpeg.input(opus_file)
                                # Définition des options de sortie pour la conversion
                                stream = ffmpeg.output(stream, ac3_file, acodec='ac3', map_metadata=0)
                                # Lancer la conversion à l'aide de FFmpeg en mode silencieux
                                ffmpeg.run(stream, quiet=True)
                                # Afficher un message indiquant que la conversion est réussie
                                print("Conversion OK")
                            except ffmpeg.Error as e:
                                # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                                self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                                # Afficher un message d'erreur avec la raison de l'échec de la conversion
                                QMessageBox.critical(None, "Error", f"Failed to convert {opus_file}: {e.stderr}")
                                return
                            encov = "ac3"
                    else: 
                        # Définir le style pour l'étiquette(en rouge) de vérification de la conversion en échec                  
                        self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                        # Afficher un message d'erreur si aucun fichier compatible n'a été trouvé dans le répertoire
                        QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                        return
                    # Afficher un message de succès de la conversion
                    show_success_message()
                    # Effacer le champ de saisie pour le chemin d'entrée
                    self.path_input.clear()
                    # Réinitialiser le choix de conversion
                    self.convertaudio_choice.setCurrentText('Veuillez choisir')
                    # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                    self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                    # Mettre à jour l'interface graphique
                    self.repaint()
            elif self.convert_audio_choice == 'opus to mp3' : # Vérifie l'entré utilisteur de la QComboBox 
                    # Recherche des fichiers d'entrées dans le répertoire sélectionné et ses sous-répertoires
                    opus_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.opus"), recursive=True)
                    # Vérifier si les fichiers d'entré ont été trouvés dans le répertoire
                    if opus_files:
                        # Afficher un message indiquant que la conversion est en cours
                        print("Conversion in progress ...")
                        for opus_file in opus_files:
                            # Définir le nom de fichier sortant en remplaçant l'extension du fichier intrant par celui du sortant
                            mp3_file = os.path.splitext(opus_file)[0] + '.mp3'
                            try:
                                # Mise à jour de l'étiquette d'état en vert, pour indiquer que la conversion est en cours
                                self.convertcheck_label.setStyleSheet("background-color: green; border-radius: 10px;")
                                # Mettre à jour l'interface graphique
                                self.repaint() 
                                # Création de la sortie de flux FFmpeg pour le fichier d'entrée
                                stream = ffmpeg.input(opus_file)
                                # Définition des options de sortie pour la conversion
                                stream = ffmpeg.output(stream, mp3_file, acodec='libmp3lame', map_metadata=0)
                                # Lancer la conversion à l'aide de FFmpeg en mode silencieux
                                ffmpeg.run(stream, quiet=True)
                                # Afficher un message indiquant que la conversion est réussie
                                print("Conversion OK")
                            except ffmpeg.Error as e:
                                # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                                self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                                # Afficher un message d'erreur avec la raison de l'échec de la conversion
                                QMessageBox.critical(None, "Error", f"Failed to convert {opus_file}: {e.stderr}")
                                return
                            encov = "opus"
                    else: 
                        # Définir le style pour l'étiquette(en rouge) de vérification de la conversion en échec                  
                        self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                        # Afficher un message d'erreur si aucun fichier compatible n'a été trouvé dans le répertoire
                        QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                        return
                    # Afficher un message de succès de la conversion
                    show_success_message()
                    # Effacer le champ de saisie pour le chemin d'entrée
                    self.path_input.clear()
                    # Réinitialiser le choix de conversion
                    self.convertaudio_choice.setCurrentText('Veuillez choisir')
                    # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                    self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                    # Mettre à jour l'interface graphique
                    self.repaint()
            elif self.convert_audio_choice == 'opus to ogg' : # Vérifie l'entré utilisteur de la QComboBox 
                    # Recherche des fichiers d'entrées dans le répertoire sélectionné et ses sous-répertoires
                    opus_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.opus"), recursive=True)
                    # Vérifier si les fichiers d'entré ont été trouvés dans le répertoire
                    if opus_files:
                        # Afficher un message indiquant que la conversion est en cours
                        print("Conversion in progress ...")
                        for opus_file in opus_files:
                            # Définir le nom de fichier sortant en remplaçant l'extension du fichier intrant par celui du sortant
                            ogg_file = os.path.splitext(opus_file)[0] + '.ogg'
                            try:
                                # Mise à jour de l'étiquette d'état en vert, pour indiquer que la conversion est en cours
                                self.convertcheck_label.setStyleSheet("background-color: green; border-radius: 10px;")
                                # Mettre à jour l'interface graphique
                                self.repaint() 
                                # Création de la sortie de flux FFmpeg pour le fichier d'entrée
                                stream = ffmpeg.input(opus_file)
                                # Définition des options de sortie pour la conversion
                                stream = ffmpeg.output(stream, ogg_file, acodec='libvorbis', map_metadata=0)
                                # Lancer la conversion à l'aide de FFmpeg en mode silencieux
                                ffmpeg.run(stream, quiet=True)
                                # Afficher un message indiquant que la conversion est réussie
                                print("Conversion OK")
                            except ffmpeg.Error as e:
                                # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                                self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                                # Afficher un message d'erreur avec la raison de l'échec de la conversion
                                QMessageBox.critical(None, "Error", f"Failed to convert {opus_file}: {e.stderr}")
                                return
                            encov = "ogg"
                    else: 
                        # Définir le style pour l'étiquette(en rouge) de vérification de la conversion en échec                  
                        self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                        # Afficher un message d'erreur si aucun fichier compatible n'a été trouvé dans le répertoire
                        QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                        return
                    # Afficher un message de succès de la conversion
                    show_success_message()
                    # Effacer le champ de saisie pour le chemin d'entrée
                    self.path_input.clear()
                    # Réinitialiser le choix de conversion
                    self.convertaudio_choice.setCurrentText('Veuillez choisir')
                    # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                    self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                    # Mettre à jour l'interface graphique
                    self.repaint()
            elif self.convert_audio_choice == 'opus to m4a' : # Vérifie l'entré utilisteur de la QComboBox 
                    # Recherche des fichiers d'entrées dans le répertoire sélectionné et ses sous-répertoires
                    opus_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.opus"), recursive=True)
                    # Vérifier si les fichiers d'entré ont été trouvés dans le répertoire
                    if opus_files:
                        # Afficher un message indiquant que la conversion est en cours
                        print("Conversion in progress ...")
                        for opus_file in opus_files:
                            # Définir le nom de fichier sortant en remplaçant l'extension du fichier intrant par celui du sortant
                            m4a_file = os.path.splitext(opus_file)[0] + '.m4a'
                            try:
                                # Mise à jour de l'étiquette d'état en vert, pour indiquer que la conversion est en cours
                                self.convertcheck_label.setStyleSheet("background-color: green; border-radius: 10px;")
                                # Mettre à jour l'interface graphique
                                self.repaint() 
                                # Création de la sortie de flux FFmpeg pour le fichier d'entrée
                                stream = ffmpeg.input(opus_file)
                                # Définition des options de sortie pour la conversion
                                stream = ffmpeg.output(stream, m4a_file, acodec='alac', map_metadata=0)
                                # Lancer la conversion à l'aide de FFmpeg en mode silencieux
                                ffmpeg.run(stream, quiet=True)
                                # Afficher un message indiquant que la conversion est réussie
                                print("Conversion OK")
                            except ffmpeg.Error as e:
                                # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                                self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                                # Afficher un message d'erreur avec la raison de l'échec de la conversion
                                QMessageBox.critical(None, "Error", f"Failed to convert {opus_file}: {e.stderr}")
                                return
                            encov = "m4a"
                    else: 
                        # Définir le style pour l'étiquette(en rouge) de vérification de la conversion en échec                  
                        self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                        # Afficher un message d'erreur si aucun fichier compatible n'a été trouvé dans le répertoire
                        QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                        return
                    # Afficher un message de succès de la conversion
                    show_success_message()
                    # Effacer le champ de saisie pour le chemin d'entrée
                    self.path_input.clear()
                    # Réinitialiser le choix de conversion
                    self.convertaudio_choice.setCurrentText('Veuillez choisir')
                    # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                    self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                    # Mettre à jour l'interface graphique
                    self.repaint()
            elif self.convert_audio_choice == 'opus to aac' : # Vérifie l'entré utilisteur de la QComboBox 
                    # Recherche des fichiers d'entrées dans le répertoire sélectionné et ses sous-répertoires
                    opus_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.opus"), recursive=True)
                    # Vérifier si les fichiers d'entré ont été trouvés dans le répertoire
                    if opus_files:
                        # Afficher un message indiquant que la conversion est en cours
                        print("Conversion in progress ...")
                        for opus_file in opus_files:
                            # Définir le nom de fichier sortant en remplaçant l'extension du fichier intrant par celui du sortant
                            aac_file = os.path.splitext(opus_file)[0] + '.aac'
                            try:
                                # Mise à jour de l'étiquette d'état en vert, pour indiquer que la conversion est en cours
                                self.convertcheck_label.setStyleSheet("background-color: green; border-radius: 10px;")
                                # Mettre à jour l'interface graphique
                                self.repaint() 
                                # Création de la sortie de flux FFmpeg pour le fichier d'entrée
                                stream = ffmpeg.input(opus_file)
                                # Définition des options de sortie pour la conversion
                                stream = ffmpeg.output(stream, aac_file, acodec='aac', map_metadata=0)
                                # Lancer la conversion à l'aide de FFmpeg en mode silencieux
                                ffmpeg.run(stream, quiet=True)
                                # Afficher un message indiquant que la conversion est réussie
                                print("Conversion OK")
                            except ffmpeg.Error as e:
                                # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                                self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                                # Afficher un message d'erreur avec la raison de l'échec de la conversion
                                QMessageBox.critical(None, "Error", f"Failed to convert {opus_file}: {e.stderr}")
                                return
                            encov = "aac"
                    else: 
                        # Définir le style pour l'étiquette(en rouge) de vérification de la conversion en échec                  
                        self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                        # Afficher un message d'erreur si aucun fichier compatible n'a été trouvé dans le répertoire
                        QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                        return
                    # Afficher un message de succès de la conversion
                    show_success_message()
                    # Effacer le champ de saisie pour le chemin d'entrée
                    self.path_input.clear()
                    # Réinitialiser le choix de conversion
                    self.convertaudio_choice.setCurrentText('Veuillez choisir')
                    # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                    self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                    # Mettre à jour l'interface graphique
                    self.repaint()
            elif self.convert_audio_choice == 'm4a to wav': # Vérifie l'entré utilisteur de la QComboBox 
                     # Recherche des fichiers d'entrées dans le répertoire sélectionné et ses sous-répertoires
                    m4a_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.m4a"), recursive=True)
                    # Vérifier si les fichiers d'entré ont été trouvés dans le répertoire
                    if m4a_files:
                        # Afficher un message indiquant que la conversion est en cours
                        print("Conversion in progress ...")
                        for m4a_file in m4a_files:
                            # Définir le nom de fichier sortant en remplaçant l'extension du fichier intrant par celui du sortant
                            wav_file = os.path.splitext(m4a_file)[0] + '.wav'
                            try:
                                # Mise à jour de l'étiquette d'état en vert, pour indiquer que la conversion est en cours
                                self.convertcheck_label.setStyleSheet("background-color: green; border-radius: 10px;")
                                # Mettre à jour l'interface graphique
                                self.repaint() 
                                # Création de la sortie de flux FFmpeg pour le fichier d'entrée
                                stream = ffmpeg.input(m4a_file)
                                # Définition des options de sortie pour la conversion
                                stream = ffmpeg.output(stream, wav_file, map_metadata=0)
                                # Lancer la conversion à l'aide de FFmpeg en mode silencieux
                                ffmpeg.run(stream, quiet=True)
                                # Afficher un message indiquant que la conversion est réussie
                                print("Conversion OK")
                            except ffmpeg.Error as e:
                                # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                                self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                                # Afficher un message d'erreur avec la raison de l'échec de la conversion
                                QMessageBox.critical(None, "Error", f"Failed to convert {m4a_file}: {e.stderr}")
                                return
                            encov = "m4a"
                    else: 
                        # Définir le style pour l'étiquette(en rouge) de vérification de la conversion en échec                  
                        self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                        # Afficher un message d'erreur si aucun fichier compatible n'a été trouvé dans le répertoire
                        QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                        return
                    # Afficher un message de succès de la conversion
                    show_success_message()
                    # Effacer le champ de saisie pour le chemin d'entrée
                    self.path_input.clear()
                    # Réinitialiser le choix de conversion
                    self.convertaudio_choice.setCurrentText('Veuillez choisir')
                    # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                    self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                    # Mettre à jour l'interface graphique
                    self.repaint()
            elif self.convert_audio_choice == 'm4a to ac3': # Vérifie l'entré utilisteur de la QComboBox 
                     # Recherche des fichiers d'entrées dans le répertoire sélectionné et ses sous-répertoires
                    m4a_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.m4a"), recursive=True)
                    # Vérifier si les fichiers d'entré ont été trouvés dans le répertoire
                    if m4a_files:
                        # Afficher un message indiquant que la conversion est en cours
                        print("Conversion in progress ...")
                        for m4a_file in m4a_files:
                            # Définir le nom de fichier sortant en remplaçant l'extension du fichier intrant par celui du sortant
                            ac3_file = os.path.splitext(m4a_file)[0] + '.ac3'
                            try:
                                # Mise à jour de l'étiquette d'état en vert, pour indiquer que la conversion est en cours
                                self.convertcheck_label.setStyleSheet("background-color: green; border-radius: 10px;")
                                # Mettre à jour l'interface graphique
                                self.repaint() 
                                # Création de la sortie de flux FFmpeg pour le fichier d'entrée
                                stream = ffmpeg.input(m4a_file)
                                # Définition des options de sortie pour la conversion
                                stream = ffmpeg.output(stream, ac3_file, acodec='ac3', map_metadata=0)
                                # Lancer la conversion à l'aide de FFmpeg en mode silencieux
                                ffmpeg.run(stream, quiet=True)
                                # Afficher un message indiquant que la conversion est réussie
                                print("Conversion OK")
                            except ffmpeg.Error as e:
                                # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                                self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                                # Afficher un message d'erreur avec la raison de l'échec de la conversion
                                QMessageBox.critical(None, "Error", f"Failed to convert {m4a_file}: {e.stderr}")
                                return
                            encov = "ac3"
                    else: 
                        # Définir le style pour l'étiquette(en rouge) de vérification de la conversion en échec                  
                        self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                        # Afficher un message d'erreur si aucun fichier compatible n'a été trouvé dans le répertoire
                        QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                        return
                    # Afficher un message de succès de la conversion
                    show_success_message()
                    # Effacer le champ de saisie pour le chemin d'entrée
                    self.path_input.clear()
                    # Réinitialiser le choix de conversion
                    self.convertaudio_choice.setCurrentText('Veuillez choisir')
                    # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                    self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                    # Mettre à jour l'interface graphique
                    self.repaint()
            elif self.convert_audio_choice == 'm4a to mp3': # Vérifie l'entré utilisteur de la QComboBox 
                     # Recherche des fichiers d'entrées dans le répertoire sélectionné et ses sous-répertoires
                    m4a_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.m4a"), recursive=True)
                    # Vérifier si les fichiers d'entré ont été trouvés dans le répertoire
                    if m4a_files:
                        # Afficher un message indiquant que la conversion est en cours
                        print("Conversion in progress ...")
                        for m4a_file in m4a_files:
                            # Définir le nom de fichier sortant en remplaçant l'extension du fichier intrant par celui du sortant
                            mp3_file = os.path.splitext(m4a_file)[0] + '.mp3'
                            try:
                                # Mise à jour de l'étiquette d'état en vert, pour indiquer que la conversion est en cours
                                self.convertcheck_label.setStyleSheet("background-color: green; border-radius: 10px;")
                                # Mettre à jour l'interface graphique
                                self.repaint() 
                                # Création de la sortie de flux FFmpeg pour le fichier d'entrée
                                stream = ffmpeg.input(m4a_file)
                                # Définition des options de sortie pour la conversion
                                stream = ffmpeg.output(stream, mp3_file, acodec='libmp3lame', map_metadata=0)
                                # Lancer la conversion à l'aide de FFmpeg en mode silencieux
                                ffmpeg.run(stream, quiet=True)
                                # Afficher un message indiquant que la conversion est réussie
                                print("Conversion OK")
                            except ffmpeg.Error as e:
                                # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                                self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                                # Afficher un message d'erreur avec la raison de l'échec de la conversion
                                QMessageBox.critical(None, "Error", f"Failed to convert {m4a_file}: {e.stderr}")
                                return
                            encov = "m4a"
                    else: 
                        # Définir le style pour l'étiquette(en rouge) de vérification de la conversion en échec                  
                        self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                        # Afficher un message d'erreur si aucun fichier compatible n'a été trouvé dans le répertoire
                        QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                        return
                    # Afficher un message de succès de la conversion
                    show_success_message()
                    # Effacer le champ de saisie pour le chemin d'entrée
                    self.path_input.clear()
                    # Réinitialiser le choix de conversion
                    self.convertaudio_choice.setCurrentText('Veuillez choisir')
                    # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                    self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                    # Mettre à jour l'interface graphique
                    self.repaint()
            elif self.convert_audio_choice == 'm4a to ogg': # Vérifie l'entré utilisteur de la QComboBox 
                     # Recherche des fichiers d'entrées dans le répertoire sélectionné et ses sous-répertoires
                    m4a_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.m4a"), recursive=True)
                    # Vérifier si les fichiers d'entré ont été trouvés dans le répertoire
                    if m4a_files:
                        # Afficher un message indiquant que la conversion est en cours
                        print("Conversion in progress ...")
                        for m4a_file in m4a_files:
                            # Définir le nom de fichier sortant en remplaçant l'extension du fichier intrant par celui du sortant
                            ogg_file = os.path.splitext(m4a_file)[0] + '.ogg'
                            try:
                                # Mise à jour de l'étiquette d'état en vert, pour indiquer que la conversion est en cours
                                self.convertcheck_label.setStyleSheet("background-color: green; border-radius: 10px;")
                                # Mettre à jour l'interface graphique
                                self.repaint() 
                                # Création de la sortie de flux FFmpeg pour le fichier d'entrée
                                stream = ffmpeg.input(m4a_file)
                                # Définition des options de sortie pour la conversion
                                stream = ffmpeg.output(stream, ogg_file, acodec='libvorbis', map_metadata=0)
                                # Lancer la conversion à l'aide de FFmpeg en mode silencieux
                                ffmpeg.run(stream, quiet=True)
                                # Afficher un message indiquant que la conversion est réussie
                                print("Conversion OK")
                            except ffmpeg.Error as e:
                                # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                                self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                                # Afficher un message d'erreur avec la raison de l'échec de la conversion
                                QMessageBox.critical(None, "Error", f"Failed to convert {m4a_file}: {e.stderr}")
                                return
                            encov = "ogg"
                    else: 
                        # Définir le style pour l'étiquette(en rouge) de vérification de la conversion en échec                  
                        self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                        # Afficher un message d'erreur si aucun fichier compatible n'a été trouvé dans le répertoire
                        QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                        return
                    # Afficher un message de succès de la conversion
                    show_success_message()
                    # Effacer le champ de saisie pour le chemin d'entrée
                    self.path_input.clear()
                    # Réinitialiser le choix de conversion
                    self.convertaudio_choice.setCurrentText('Veuillez choisir')
                    # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                    self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                    # Mettre à jour l'interface graphique
                    self.repaint()
            elif self.convert_audio_choice == 'm4a to opus' : # Vérifie l'entré utilisteur de la QComboBox 
                    # Recherche des fichiers d'entrées dans le répertoire sélectionné et ses sous-répertoires
                    m4a_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.m4a"), recursive=True)
                    # Vérifier si les fichiers d'entré ont été trouvés dans le répertoire
                    if m4a_files:
                        # Afficher un message indiquant que la conversion est en cours
                        print("Conversion in progress ...")
                        for m4a_file in m4a_files:
                            # Définir le nom de fichier sortant en remplaçant l'extension du fichier intrant par celui du sortant 
                            opus_file = os.path.splitext(m4a_file)[0] + '.opus'
                            try:
                                # Mise à jour de l'étiquette d'état en vert, pour indiquer que la conversion est en cours
                                self.convertcheck_label.setStyleSheet("background-color: green; border-radius: 10px;")
                                # Mettre à jour l'interface graphique
                                self.repaint() 
                                # Création de la sortie de flux FFmpeg pour le fichier d'entrée
                                stream = ffmpeg.input(m4a_file)
                                # Définition des options de sortie pour la conversion
                                stream = ffmpeg.output(stream, opus_file, acodec='libopus', map_metadata=0)
                                # Lancer la conversion à l'aide de FFmpeg en mode silencieux
                                ffmpeg.run(stream, quiet=True)
                                # Afficher un message indiquant que la conversion est réussie
                                print("Conversion OK")
                            except ffmpeg.Error as e:
                                # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                                self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                                # Afficher un message d'erreur avec la raison de l'échec de la conversion
                                QMessageBox.critical(None, "Error", f"Failed to convert {m4a_file}: {e.stderr}")
                                return
                            encov = "opus"
                    else: 
                        # Définir le style pour l'étiquette(en rouge) de vérification de la conversion en échec                  
                        self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                        # Afficher un message d'erreur si aucun fichier compatible n'a été trouvé dans le répertoire
                        QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                        return
                    # Afficher un message de succès de la conversion
                    show_success_message()
                    # Effacer le champ de saisie pour le chemin d'entrée
                    self.path_input.clear()
                    # Réinitialiser le choix de conversion
                    self.convertaudio_choice.setCurrentText('Veuillez choisir')
                    # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                    self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                    # Mettre à jour l'interface graphique
                    self.repaint()
            elif self.convert_audio_choice == 'm4a to aac': # Vérifie l'entré utilisteur de la QComboBox 
                     # Recherche des fichiers d'entrées dans le répertoire sélectionné et ses sous-répertoires
                    m4a_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.m4a"), recursive=True)
                    # Vérifier si les fichiers d'entré ont été trouvés dans le répertoire
                    if m4a_files:
                        # Afficher un message indiquant que la conversion est en cours
                        print("Conversion in progress ...")
                        for m4a_file in m4a_files:
                            # Définir le nom de fichier sortant en remplaçant l'extension du fichier intrant par celui du sortant
                            aac_file = os.path.splitext(m4a_file)[0] + '.aac'
                            try:
                                # Mise à jour de l'étiquette d'état en vert, pour indiquer que la conversion est en cours
                                self.convertcheck_label.setStyleSheet("background-color: green; border-radius: 10px;")
                                # Mettre à jour l'interface graphique
                                self.repaint() 
                                # Création de la sortie de flux FFmpeg pour le fichier d'entrée
                                stream = ffmpeg.input(m4a_file)
                                # Définition des options de sortie pour la conversion
                                stream = ffmpeg.output(stream, aac_file, acodec='aac', map_metadata=0)
                                # Lancer la conversion à l'aide de FFmpeg en mode silencieux
                                ffmpeg.run(stream, quiet=True)
                                # Afficher un message indiquant que la conversion est réussie
                                print("Conversion OK")
                            except ffmpeg.Error as e:
                                # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                                self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                                # Afficher un message d'erreur avec la raison de l'échec de la conversion
                                QMessageBox.critical(None, "Error", f"Failed to convert {m4a_file}: {e.stderr}")
                                return
                            encov = "aac"
                    else: 
                        # Définir le style pour l'étiquette(en rouge) de vérification de la conversion en échec                  
                        self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                        # Afficher un message d'erreur si aucun fichier compatible n'a été trouvé dans le répertoire
                        QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                        return
                    # Afficher un message de succès de la conversion
                    show_success_message()
                    # Effacer le champ de saisie pour le chemin d'entrée
                    self.path_input.clear()
                    # Réinitialiser le choix de conversion
                    self.convertaudio_choice.setCurrentText('Veuillez choisir')
                    # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                    self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                    # Mettre à jour l'interface graphique
                    self.repaint()
            else:
                self.internet_label.setStyleSheet("background-color: red; border-radius: 10px;")
                QMessageBox.critical(None, "Error", "An unexpected error has occurred")
        except Exception as e:
            # Afficher une boîte de dialogue en cas d'erreur de conversion
            error_message = "An error occurred during the conversion: {}".format(str(e))
            message_box = QMessageBox()
            message_box.setWindowTitle("Conversion error")
            message_box.setText(error_message)
            message_box.setIcon(QMessageBox.Warning)
            message_box.addButton(QMessageBox.Ok)
            message_box.exec_()

# ---------------- Convertisso video ----------------
class VideoTab(QWidget):
    def __init__(self):
        super().__init__()
        # Crée un QLabel avec le texte "Convertisso Video" et le positionne à (20,20)   
        label = QLabel("Convertisso video", self)
        label.move(20, 20)
        # Appelle la méthode initUI()
        self.initUI()

    def initUI(self):
        # Crée un QLabel avec le texte "Chose directory (where are stored your(s) file(s) to convert):" et le positionne à (50,200)
        self.path_label = QLabel(self)
        self.path_label.setText('Chose directory (where are stored your(s) file(s) to convert):')
        self.path_label.move(50, 200)
        # Crée un QLineEdit et le positionne à (470, 200) avec une largeur de 300 et une hauteur de 30
        self.path_input = QLineEdit(self)
        self.path_input.move(470, 200)
        self.path_input.resize(300, 30)
        self.path_input.text()
        # Crée un QPushButton avec le texte "Choose Folder" et le positionne à (770, 200). Connecte le bouton à la méthode "choose_folder".
        self.choose_path_button = QPushButton('Choose Folder', self)
        self.choose_path_button.move(770, 200)
        self.choose_path_button.clicked.connect(self.choose_folder)
        # Crée un QComboBox avec les options ci-dessous. Connecte le QComboBox à la méthode "setaudioOption".
        self.convertvideo_choice = QComboBox(self)
        self.convertvideo_choice.addItem('Please choose')
        self.convertvideo_choice.addItems(['mkv to avi', 'mkv to mov', 'mkv to mp4', 'mkv to webm', 'mkv to flv', 'mkv to hevc',
                                   'mp4 to mkv', 'mp4 to mov', 'mp4 to avi', 'mp4 to webm', 'mp4 to flv', 'mp4 to hevc',
                                   'mov to mkv', 'mov to mp4', 'mov to avi', 'mov to webm', 'mov to flv', 'mov to hevc',
                                   'avi to mkv', 'avi to mp4', 'avi to mov', 'avi to webm', 'avi to flv', 'avi to hevc',
                                   'webm to avi', 'webm to mkv', 'webm to mov', 'webm to mp4', 'webm to flv', 'webm to hevc',
                                   'hevc to avi', 'hevc to mkv', 'hevc to mov', 'hevc to mp4', 'hevc to flv', 'hevc to webm',
                                   'flv to avi', 'flv to mkv', 'flv to mov', 'flv to mp4', 'flv to hevc', 'flv to webm'])
        self.convertvideo_choice.move(250, 100)
        self.convertvideo_choice.resize(200, 30)
        self.convertvideo_choice.setMaxVisibleItems(5)
        self.convertvideo_choice.setEditable(True)
        self.convertvideo_choice.view().setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.convertvideo_choice.currentIndexChanged.connect(self.setVideoOption)
        # Crée un QLabel avec le texte "Conversion in progress: " et le positionne à (400, 20)    
        self.convertcheck_txt_label = QLabel(self)
        self.convertcheck_txt_label.setText('Conversion in progress: ')
        self.convertcheck_txt_label.move(400, 20)
        # Création d'un QLabel pour afficher le statut de vérification de la convertion avec une led, deffition de la led rouge pas defaut
        self.convertcheck_label = QLabel(self)
        self.convertcheck_label.setFixedSize(20, 20)
        self.convertcheck_label.move(600, 20)
        self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
        # Création d'un QPushButton pour démarrer la convertion
        self.convertvideo_button = QPushButton('Convert', self)
        self.convertvideo_button.move(300, 350)
        self.convertvideo_button.clicked.connect(self.convertvideo)
    # Fonction pour choisir le dossier de destination de la convertion
    def choose_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self, 'Choose Folder')
        self.path_input.setText(folder_path)
    # Fonction pour définir l'option de convertion sélectionnée par l'utilisateur
    def setVideoOption(self, index):
        self.convertuniquementvideo_choice = self.convertvideo_choice.itemText(index)

    def convertvideo(self): #cette partie permet de convertir des fichiers video
        try:
            if self.convertuniquementvideo_choice == 'mkv to avi': # Vérifie l'entré utilisteur de la QComboBox
                # Recherche des fichiers d'entrées dans le répertoire sélectionné et ses sous-répertoires      
                mkv_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.mkv"), recursive=True)
                # Vérifier si les fichiers d'entré ont été trouvés dans le répertoire
                if mkv_files:
                    # Afficher un message indiquant que la conversion est en cours
                    print("Conversion in progress ...")
                    # Parcourir tous les fichiers d'entrées trouvés
                    for mkv_file in mkv_files:
                        # Définir le nom de fichier sortant en remplaçant l'extension du fichier intrant par celui du sortant                     
                        avi_file = os.path.splitext(mkv_file)[0] + '.avi'
                        try:
                            # Mise à jour de l'étiquette d'état en vert, pour indiquer que la conversion est en cours
                            self.convertcheck_label.setStyleSheet("background-color: green; border-radius: 10px;")
                            # Mettre à jour l'interface graphique
                            self.repaint()
                            # Création de la sortie de flux FFmpeg pour le(s) fichier(s) d'entrée
                            stream = ffmpeg.input(mkv_file)
                            # Définition des options de sortie pour la conversion
                            stream = ffmpeg.output(stream, avi_file, vcodec='libx264', acodec='aac', map_metadata=0)
                            # Lancer la conversion à l'aide de FFmpeg en mode silencieux
                            ffmpeg.run(stream, quiet=True)
                            # Afficher un message indiquant que la conversion est réussie
                            print("Conversion OK")
                        except ffmpeg.Error as e:
                            self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                            # Afficher un message d'erreur avec la raison de l'échec de la conversion
                            QMessageBox.critical(None, "Error", f"Failed to convert {mkv_file}: {e.stderr}")
                            return
                        encov = "avi"
                else:
                    # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec 
                    self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                    # Afficher un message d'erreur avec la raison de l'échec de la conversion
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
                 # Afficher un message de succès de la conversion
                show_success_message()
                # Effacer le champ de saisie pour le chemin d'entrée
                self.path_input.clear()
                # Réinitialiser le choix de conversion
                self.convertvideo_choice.setCurrentText('Please choose')
                # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                # Mettre à jour l'interface graphique
                self.repaint() 
            elif self.convertuniquementvideo_choice == 'mkv to mov': # Vérifie l'entré utilisteur de la QComboBox  # mkv to mov
                # Recherche des fichiers d'entrées dans le répertoire sélectionné et ses sous-répertoires                
                mkv_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.mkv"), recursive=True)
                # Vérifier si les fichiers d'entré ont été trouvés dans le répertoire
                if mkv_files:
                    # Afficher un message indiquant que la conversion est en cours
                    print("Conversion in progress ...")
                    # Parcourir tous les fichiers d'entrées trouvés
                    for mkv_file in mkv_files:
                        # Définir le nom de fichier sortant en remplaçant l'extension du fichier intrant par celui du sortant                     
                        mov_file = os.path.splitext(mkv_file)[0] + '.mov'
                        try:
                            # Mise à jour de l'étiquette d'état en vert, pour indiquer que la conversion est en cours
                            self.convertcheck_label.setStyleSheet("background-color: green; border-radius: 10px;")
                            # Mettre à jour l'interface graphique
                            self.repaint()
                            # Création de la sortie de flux FFmpeg pour le(s) fichier(s) d'entrée
                            stream = ffmpeg.input(mkv_file)
                            # Définition des options de sortie pour la conversion
                            stream = ffmpeg.output(stream, mov_file, vcodec='libx264', acodec='aac', map_metadata=0)
                            # Lancer la conversion à l'aide de FFmpeg en mode silencieux
                            ffmpeg.run(stream, quiet=True)
                            # Afficher un message indiquant que la conversion est réussie
                            print("Conversion OK")
                        except ffmpeg.Error as e:
                            self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                            # Afficher un message d'erreur avec la raison de l'échec de la conversion
                            QMessageBox.critical(None, "Error", f"Failed to convert {mkv_file}: {e.stderr}")
                            return
                        encov = "mov"
                else:
                    # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec 
                    self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                    # Afficher un message d'erreur avec la raison de l'échec de la conversion
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
                 # Afficher un message de succès de la conversion
                show_success_message()
                # Effacer le champ de saisie pour le chemin d'entrée
                self.path_input.clear()
                # Réinitialiser le choix de conversion
                self.convertvideo_choice.setCurrentText('Please choose')
                # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                # Mettre à jour l'interface graphique
                self.repaint() 
            elif self.convertuniquementvideo_choice == 'mkv to mp4': # Vérifie l'entré utilisteur de la QComboBox  # mkv to mp4
                # Recherche des fichiers d'entrées dans le répertoire sélectionné et ses sous-répertoires
                mkv_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.mkv"), recursive=True)
                # Vérifier si les fichiers d'entré ont été trouvés dans le répertoire
                if mkv_files:
                    # Afficher un message indiquant que la conversion est en cours
                    print("Conversion in progress ...")
                    # Parcourir tous les fichiers d'entrées trouvés
                    for mkv_file in mkv_files:
                        # Définir le nom de fichier sortant en remplaçant l'extension du fichier intrant par celui du sortant                     
                        mp4_file = os.path.splitext(mkv_file)[0] + '.mp4'
                        try:
                            # Mise à jour de l'étiquette d'état en vert, pour indiquer que la conversion est en cours
                            self.convertcheck_label.setStyleSheet("background-color: green; border-radius: 10px;")
                            # Mettre à jour l'interface graphique
                            self.repaint()
                            # Création de la sortie de flux FFmpeg pour le(s) fichier(s) d'entrée
                            stream = ffmpeg.input(mkv_file)
                            # Définition des options de sortie pour la conversion
                            stream = ffmpeg.output(stream, mp4_file, vcodec='libx264', acodec='aac', map_metadata=0)
                            # Lancer la conversion à l'aide de FFmpeg en mode silencieux
                            ffmpeg.run(stream, quiet=True)
                            # Afficher un message indiquant que la conversion est réussie
                            print("Conversion OK")
                        except ffmpeg.Error as e:
                            self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                            # Afficher un message d'erreur avec la raison de l'échec de la conversion
                            QMessageBox.critical(None, "Error", f"Failed to convert {mkv_file}: {e.stderr}")
                            return
                        encov = "mp4"
                else:
                    # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec 
                    self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                    # Afficher un message d'erreur avec la raison de l'échec de la conversion
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
                 # Afficher un message de succès de la conversion
                show_success_message()
                # Effacer le champ de saisie pour le chemin d'entrée
                self.path_input.clear()
                # Réinitialiser le choix de conversion
                self.convertvideo_choice.setCurrentText('Please choose')
                # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                # Mettre à jour l'interface graphique
                self.repaint() 
            elif self.convertuniquementvideo_choice == 'mkv to webm': # Vérifie l'entré utilisteur de la QComboBox  # mkv to webm
                    # Recherche des fichiers d'entrées dans le répertoire sélectionné et ses sous-répertoires              
                mkv_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.mkv"), recursive=True)
                # Vérifier si les fichiers d'entré ont été trouvés dans le répertoire
                if mkv_files:
                    # Afficher un message indiquant que la conversion est en cours
                    print("Conversion in progress ...")
                    # Parcourir tous les fichiers d'entrées trouvés
                    for mkv_file in mkv_files:
                        # Définir le nom de fichier sortant en remplaçant l'extension du fichier intrant par celui du sortant                      
                        webm_file = os.path.splitext(mkv_file)[0] + '.webm'
                        try:
                            # Mise à jour de l'étiquette d'état en vert, pour indiquer que la conversion est en cours
                            self.convertcheck_label.setStyleSheet("background-color: green; border-radius: 10px;")
                            # Mettre à jour l'interface graphique
                            self.repaint()
                            # Création de la sortie de flux FFmpeg pour le(s) fichier(s) d'entrée
                            stream = ffmpeg.input(mkv_file)
                            # Définition des options de sortie pour la conversion
                            stream = ffmpeg.output(stream, webm_file, vcodec='libvpx', acodec='libvorbis', map_metadata=0)
                            # Lancer la conversion à l'aide de FFmpeg en mode silencieux
                            ffmpeg.run(stream, quiet=True)
                            # Afficher un message indiquant que la conversion est réussie
                            print("Conversion OK")
                        except ffmpeg.Error as e:
                            self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                            # Afficher un message d'erreur avec la raison de l'échec de la conversion
                            QMessageBox.critical(None, "Error", f"Failed to convert {mkv_file}: {e.stderr}")
                            return
                        encov = "webm"
                else:
                    # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec 
                    self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                    # Afficher un message d'erreur avec la raison de l'échec de la conversion
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
                 # Afficher un message de succès de la conversion
                show_success_message()
                # Effacer le champ de saisie pour le chemin d'entrée
                self.path_input.clear()
                # Réinitialiser le choix de conversion
                self.convertvideo_choice.setCurrentText('Please choose')
                # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                # Mettre à jour l'interface graphique
            elif self.convertuniquementvideo_choice == 'mkv to flv': # Vérifie l'entré utilisteur de la QComboBox  # mkv to flv
                # Recherche des fichiers d'entrées dans le répertoire sélectionné et ses sous-répertoires               
                mkv_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.mkv"), recursive=True)
                # Vérifier si les fichiers d'entré ont été trouvés dans le répertoire
                if mkv_files:
                    # Afficher un message indiquant que la conversion est en cours
                    print("Conversion in progress ...")
                    # Parcourir tous les fichiers d'entrées trouvés
                    for mkv_file in mkv_files:
                        # Définir le nom de fichier sortant en remplaçant l'extension du fichier intrant par celui du sortant                     
                        flv_file = os.path.splitext(mkv_file)[0] + '.flv'
                        try:
                            # Mise à jour de l'étiquette d'état en vert, pour indiquer que la conversion est en cours
                            self.convertcheck_label.setStyleSheet("background-color: green; border-radius: 10px;")
                            # Mettre à jour l'interface graphique
                            self.repaint()
                            # Création de la sortie de flux FFmpeg pour le(s) fichier(s) d'entrée
                            stream = ffmpeg.input(mkv_file)
                            # Définition des options de sortie pour la conversion
                            stream = ffmpeg.output(stream, flv_file, vcodec='flv', acodec='libmp3lame', map_metadata=0)
                            # Lancer la conversion à l'aide de FFmpeg en mode silencieux
                            ffmpeg.run(stream, quiet=True)
                            # Afficher un message indiquant que la conversion est réussie
                            print("Conversion OK")
                        except ffmpeg.Error as e:
                            self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                            # Afficher un message d'erreur avec la raison de l'échec de la conversion
                            QMessageBox.critical(None, "Error", f"Failed to convert {mkv_file}: {e.stderr}")
                            return
                        encov = "flv"
                else:
                    # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec 
                    self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                    # Afficher un message d'erreur avec la raison de l'échec de la conversion
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
                 # Afficher un message de succès de la conversion
                show_success_message()
                # Effacer le champ de saisie pour le chemin d'entrée
                self.path_input.clear()
                # Réinitialiser le choix de conversion
                self.convertvideo_choice.setCurrentText('Please choose')
                # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                # Mettre à jour l'interface graphique
                self.repaint()
            elif self.convertuniquementvideo_choice == 'mkv to hevc': # Vérifie l'entré utilisteur de la QComboBox  # mkv to hevc
                # Recherche des fichiers d'entrées dans le répertoire sélectionné et ses sous-répertoires             
                mkv_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.mkv"), recursive=True)
                # Vérifier si les fichiers d'entré ont été trouvés dans le répertoire
                if mkv_files:
                    # Afficher un message indiquant que la conversion est en cours
                    print("Conversion in progress ...")
                    # Parcourir tous les fichiers d'entrées trouvés
                    for mkv_file in mkv_files:
                        # Définir le nom de fichier sortant en remplaçant l'extension du fichier intrant par celui du sortant                      
                        hevc_file = os.path.splitext(mkv_file)[0] + '.hevc'
                        try:
                            # Mise à jour de l'étiquette d'état en vert, pour indiquer que la conversion est en cours
                            self.convertcheck_label.setStyleSheet("background-color: green; border-radius: 10px;")
                            # Mettre à jour l'interface graphique
                            self.repaint()
                            # Création de la sortie de flux FFmpeg pour le(s) fichier(s) d'entrée
                            stream = ffmpeg.input(mkv_file)
                            # Définition des options de sortie pour la conversion
                            stream = ffmpeg.output(stream, hevc_file, vcodec='libx265', acodec='copy', map_metadata=0)
                            # Lancer la conversion à l'aide de FFmpeg en mode silencieux
                            ffmpeg.run(stream, quiet=True)
                            # Afficher un message indiquant que la conversion est réussie
                            print("Conversion OK")
                        except ffmpeg.Error as e:
                            self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                            # Afficher un message d'erreur avec la raison de l'échec de la conversion
                            QMessageBox.critical(None, "Error", f"Failed to convert {mkv_file}: {e.stderr}")
                            return
                        encov = "hevc"
                else:
                    # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec 
                    self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                    # Afficher un message d'erreur avec la raison de l'échec de la conversion
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
                 # Afficher un message de succès de la conversion
                show_success_message()
                # Effacer le champ de saisie pour le chemin d'entrée
                self.path_input.clear()
                # Réinitialiser le choix de conversion
                self.convertvideo_choice.setCurrentText('Please choose')
                # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                # Mettre à jour l'interface graphique
                self.repaint()        
            elif self.convertuniquementvideo_choice == 'mp4 to mkv ': # Vérifie l'entré utilisteur de la QComboBox    #mp4 to mkv 
                # Recherche des fichiers d'entrées dans le répertoire sélectionné et ses sous-répertoires           
                mp4_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.mp4"), recursive=True)
                # Vérifier si les fichiers d'entré ont été trouvés dans le répertoire
                if mp4_files:
                    # Afficher un message indiquant que la conversion est en cours
                    print("Conversion in progress ...")
                    # Parcourir tous les fichiers d'entrées trouvés
                    for mp4_file in mp4_files:
                        # Définir le nom de fichier sortant en remplaçant l'extension du fichier intrant par celui du sortant                     
                        mkv_file = os.path.splitext(mp4_file)[0] + '.mkv'
                        try:
                            # Mise à jour de l'étiquette d'état en vert, pour indiquer que la conversion est en cours
                            self.convertcheck_label.setStyleSheet("background-color: green; border-radius: 10px;")
                            # Mettre à jour l'interface graphique
                            self.repaint()
                            # Création de la sortie de flux FFmpeg pour le(s) fichier(s) d'entrée
                            stream = ffmpeg.input(mp4_file)
                            # Définition des options de sortie pour la conversion
                            stream = ffmpeg.output(stream, mkv_file, vcodec='copy', acodec='copy', map_metadata=0)
                            # Lancer la conversion à l'aide de FFmpeg en mode silencieux
                            ffmpeg.run(stream, quiet=True)
                            # Afficher un message indiquant que la conversion est réussie
                            print("Conversion OK")
                        except ffmpeg.Error as e:
                            self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                            # Afficher un message d'erreur avec la raison de l'échec de la conversion
                            QMessageBox.critical(None, "Error", f"Failed to convert {mp4_file}: {e.stderr}")
                            return
                        encov = "mkv"
                else:
                    # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec 
                    self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                    # Afficher un message d'erreur avec la raison de l'échec de la conversion
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
                 # Afficher un message de succès de la conversion
                show_success_message()
                # Effacer le champ de saisie pour le chemin d'entrée
                self.path_input.clear()
                # Réinitialiser le choix de conversion
                self.convertvideo_choice.setCurrentText('Please choose')
                # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                # Mettre à jour l'interface graphique
                self.repaint() 
            elif self.convertuniquementvideo_choice == 'mp4 to mov': # Vérifie l'entré utilisteur de la QComboBox    #mp4 to mov 
                # Recherche des fichiers d'entrées dans le répertoire sélectionné et ses sous-répertoires           
                mp4_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.mkv"), recursive=True)
                # Vérifier si les fichiers d'entré ont été trouvés dans le répertoire
                if mp4_files:
                    # Afficher un message indiquant que la conversion est en cours
                    print("Conversion in progress ...")
                    # Parcourir tous les fichiers d'entrées trouvés
                    for mp4_file in mp4_files:
                        # Définir le nom de fichier sortant en remplaçant l'extension du fichier intrant par celui du sortant                     
                        mov_file = os.path.splitext(mp4_file)[0] + '.mov'
                        try:
                            # Mise à jour de l'étiquette d'état en vert, pour indiquer que la conversion est en cours
                            self.convertcheck_label.setStyleSheet("background-color: green; border-radius: 10px;")
                            # Mettre à jour l'interface graphique
                            self.repaint()
                            # Création de la sortie de flux FFmpeg pour le(s) fichier(s) d'entrée
                            stream = ffmpeg.input(mp4_file)
                            # Définition des options de sortie pour la conversion
                            stream = ffmpeg.output(stream, mov_file, vcodec='libx264', acodec='aac', map_metadata=0)
                            # Lancer la conversion à l'aide de FFmpeg en mode silencieux
                            ffmpeg.run(stream, quiet=True)
                            # Afficher un message indiquant que la conversion est réussie
                            print("Conversion OK")
                        except ffmpeg.Error as e:
                            self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                            # Afficher un message d'erreur avec la raison de l'échec de la conversion
                            QMessageBox.critical(None, "Error", f"Failed to convert {mp4_file}: {e.stderr}")
                            return
                        encov = "mov"
                else:
                    # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec 
                    self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                    # Afficher un message d'erreur avec la raison de l'échec de la conversion
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
                 # Afficher un message de succès de la conversion
                show_success_message()
                # Effacer le champ de saisie pour le chemin d'entrée
                self.path_input.clear()
                # Réinitialiser le choix de conversion
                self.convertvideo_choice.setCurrentText('Please choose')
                # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                # Mettre à jour l'interface graphique
                self.repaint() 
            elif self.convertuniquementvideo_choice == 'mp4 to avi': # Vérifie l'entré utilisteur de la QComboBox    #mp4 to avi 
                    # Recherche des fichiers d'entrées dans le répertoire sélectionné et ses sous-répertoires 
                mp4_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.mkv"), recursive=True)
                # Vérifier si les fichiers d'entré ont été trouvés dans le répertoire
                if mp4_files:
                    # Afficher un message indiquant que la conversion est en cours
                    print("Conversion in progress ...")
                    # Parcourir tous les fichiers d'entrées trouvés
                    for mp4_file in mp4_files:
                        # Définir le nom de fichier sortant en remplaçant l'extension du fichier intrant par celui du sortant                     
                        avi_file = os.path.splitext(mp4_file)[0] + '.avi'
                        try:
                            # Mise à jour de l'étiquette d'état en vert, pour indiquer que la conversion est en cours
                            self.convertcheck_label.setStyleSheet("background-color: green; border-radius: 10px;")
                            # Mettre à jour l'interface graphique
                            self.repaint()
                            # Création de la sortie de flux FFmpeg pour le(s) fichier(s) d'entrée
                            stream = ffmpeg.input(mp4_file)
                            # Définition des options de sortie pour la conversion
                            stream = ffmpeg.output(stream, avi_file, vcodec='libx264', acodec='aac', map_metadata=0)
                            # Lancer la conversion à l'aide de FFmpeg en mode silencieux
                            ffmpeg.run(stream, quiet=True)
                            # Afficher un message indiquant que la conversion est réussie
                            print("Conversion OK")
                        except ffmpeg.Error as e:
                            self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                            # Afficher un message d'erreur avec la raison de l'échec de la conversion
                            QMessageBox.critical(None, "Error", f"Failed to convert {mp4_file}: {e.stderr}")
                            return
                        encov = "avi"
                else:
                    # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec 
                    self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                    # Afficher un message d'erreur avec la raison de l'échec de la conversion
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
                 # Afficher un message de succès de la conversion
                show_success_message()
                # Effacer le champ de saisie pour le chemin d'entrée
                self.path_input.clear()
                # Réinitialiser le choix de conversion
                self.convertvideo_choice.setCurrentText('Please choose')
                # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                # Mettre à jour l'interface graphique
                self.repaint() 
            elif self.convertuniquementvideo_choice == 'mp4 to webm': # Vérifie l'entré utilisteur de la QComboBox    #mp4 to webm 
                # Recherche des fichiers d'entrées dans le répertoire         sélectionné et ses sous-répertoires
                mp4_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.mp4"), recursive=True)
                # Vérifier si les fichiers d'entré ont été trouvés dans le répertoire
                if mp4_files:
                    # Afficher un message indiquant que la conversion est en cours
                    print("Conversion in progress ...")
                    # Parcourir tous les fichiers d'entrées trouvés
                    for mp4_file in mp4_files:
                        # Définir le nom de fichier sortant en remplaçant l'extension du fichier intrant par celui du sortant                      
                        webm_file = os.path.splitext(mp4_file)[0] + '.webm'
                        try:
                            # Mise à jour de l'étiquette d'état en vert, pour indiquer que la conversion est en cours
                            self.convertcheck_label.setStyleSheet("background-color: green; border-radius: 10px;")
                            # Mettre à jour l'interface graphique
                            self.repaint()
                            # Création de la sortie de flux FFmpeg pour le(s) fichier(s) d'entrée
                            stream = ffmpeg.input(mp4_file)
                            # Définition des options de sortie pour la conversion
                            stream = ffmpeg.output(stream, webm_file, vcodec='libvpx', acodec='libvorbis', map_metadata=0)
                            # Lancer la conversion à l'aide de FFmpeg en mode silencieux
                            ffmpeg.run(stream, quiet=True)
                            # Afficher un message indiquant que la conversion est réussie
                            print("Conversion OK")
                        except ffmpeg.Error as e:
                            self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                            # Afficher un message d'erreur avec la raison de l'échec de la conversion
                            QMessageBox.critical(None, "Error", f"Failed to convert {mp4_file}: {e.stderr}")
                            return
                        encov = "webm"
                else:
                    # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec 
                    self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                    # Afficher un message d'erreur avec la raison de l'échec de la conversion
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
                 # Afficher un message de succès de la conversion
                show_success_message()
                # Effacer le champ de saisie pour le chemin d'entrée
                self.path_input.clear()
                # Réinitialiser le choix de conversion
                self.convertvideo_choice.setCurrentText('Please choose')
                # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                # Mettre à jour l'interface graphique
                self.repaint()        
            elif self.convertuniquementvideo_choice == 'mp4 to flv': # Vérifie l'entré utilisteur de la QComboBox    #mp4 to flv 
                # Recherche des fichiers d'entrées dans le répertoire sélectionné et ses sous-répertoires           
                mp4_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.mp4"), recursive=True)
                # Vérifier si les fichiers d'entré ont été trouvés dans le répertoire
                if mp4_files:
                    # Afficher un message indiquant que la conversion est en cours
                    print("Conversion in progress ...")
                    # Parcourir tous les fichiers d'entrées trouvés
                    for mp4_file in mp4_files:
                        # Définir le nom de fichier sortant en remplaçant l'extension du fichier intrant par celui du sortant                     
                        flv_file = os.path.splitext(mp4_file)[0] + '.flv'
                        try:
                            # Mise à jour de l'étiquette d'état en vert, pour indiquer que la conversion est en cours
                            self.convertcheck_label.setStyleSheet("background-color: green; border-radius: 10px;")
                            # Mettre à jour l'interface graphique
                            self.repaint()
                            # Création de la sortie de flux FFmpeg pour le(s) fichier(s) d'entrée
                            stream = ffmpeg.input(mp4_file)
                            # Définition des options de sortie pour la conversion
                            stream = ffmpeg.output(stream, flv_file, vcodec='flv', acodec='libmp3lame', map_metadata=0)
                            # Lancer la conversion à l'aide de FFmpeg en mode silencieux
                            ffmpeg.run(stream, quiet=True)
                            # Afficher un message indiquant que la conversion est réussie
                            print("Conversion OK")
                        except ffmpeg.Error as e:
                            self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                            # Afficher un message d'erreur avec la raison de l'échec de la conversion
                            QMessageBox.critical(None, "Error", f"Failed to convert {mp4_file}: {e.stderr}")
                            return
                        encov = "flv"
                else:
                    # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec 
                    self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                    # Afficher un message d'erreur avec la raison de l'échec de la conversion
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
                 # Afficher un message de succès de la conversion
                show_success_message()
                # Effacer le champ de saisie pour le chemin d'entrée
                self.path_input.clear()
                # Réinitialiser le choix de conversion
                self.convertvideo_choice.setCurrentText('Please choose')
                # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                # Mettre à jour l'interface graphique
                self.repaint()          
            elif self.convertuniquementvideo_choice == 'mp4 to hevc': # Vérifie l'entré utilisteur de la QComboBox    #mp4 to hevc 
                # Recherche des fichiers d'entrées dans le répertoire         sélectionné et ses sous-répertoires
                mp4_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.mp4"), recursive=True)
                # Vérifier si les fichiers d'entré ont été trouvés dans le répertoire
                if mp4_files:
                    # Afficher un message indiquant que la conversion est en cours
                    print("Conversion in progress ...")
                    # Parcourir tous les fichiers d'entrées trouvés
                    for mp4_file in mp4_files:
                        # Définir le nom de fichier sortant en remplaçant l'extension du fichier intrant par celui du sortant                      
                        hevc_file = os.path.splitext(mp4_file)[0] + '.hevc'
                        try:
                            # Mise à jour de l'étiquette d'état en vert, pour indiquer que la conversion est en cours
                            self.convertcheck_label.setStyleSheet("background-color: green; border-radius: 10px;")
                            # Mettre à jour l'interface graphique
                            self.repaint()
                            # Création de la sortie de flux FFmpeg pour le(s) fichier(s) d'entrée
                            stream = ffmpeg.input(mp4_file)
                            # Définition des options de sortie pour la conversion
                            stream = ffmpeg.output(stream, hevc_file, vcodec='libx265', acodec='copy', map_metadata=0)
                            # Lancer la conversion à l'aide de FFmpeg en mode silencieux
                            ffmpeg.run(stream, quiet=True)
                            # Afficher un message indiquant que la conversion est réussie
                            print("Conversion OK")
                        except ffmpeg.Error as e:
                            self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                            # Afficher un message d'erreur avec la raison de l'échec de la conversion
                            QMessageBox.critical(None, "Error", f"Failed to convert {mp4_file}: {e.stderr}")
                            return
                        encov = "hevc"
                else:
                    # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec 
                    self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                    # Afficher un message d'erreur avec la raison de l'échec de la conversion
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
                 # Afficher un message de succès de la conversion
                show_success_message()
                # Effacer le champ de saisie pour le chemin d'entrée
                self.path_input.clear()
                # Réinitialiser le choix de conversion
                self.convertvideo_choice.setCurrentText('Please choose')
                # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                # Mettre à jour l'interface graphique
                self.repaint() 
            elif self.convertuniquementvideo_choice == 'mov to mkv': # Vérifie l'entré utilisteur de la QComboBox    #mov to mkv 
                # Recherche des fichiers d'entrées dans le répertoire sélectionné et ses sous-répertoires           
                mov_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.mov"), recursive=True)
                # Vérifier si les fichiers d'entré ont été trouvés dans le répertoire
                if mov_files:
                    # Afficher un message indiquant que la conversion est en cours
                    print("Conversion in progress ...")
                    # Parcourir tous les fichiers d'entrées trouvés
                    for mov_file in mov_files:
                        # Définir le nom de fichier sortant en remplaçant l'extension du fichier intrant par celui du sortant                     
                        mkv_file = os.path.splitext(mov_file)[0] + '.mkv'
                        try:
                            # Mise à jour de l'étiquette d'état en vert, pour indiquer que la conversion est en cours
                            self.convertcheck_label.setStyleSheet("background-color: green; border-radius: 10px;")
                            # Mettre à jour l'interface graphique
                            self.repaint()
                            # Création de la sortie de flux FFmpeg pour le(s) fichier(s) d'entrée
                            stream = ffmpeg.input(mov_file)
                            # Définition des options de sortie pour la conversion
                            stream = ffmpeg.output(stream, mkv_file, vcodec='copy', acodec='copy', map_metadata=0)
                            # Lancer la conversion à l'aide de FFmpeg en mode silencieux
                            ffmpeg.run(stream, quiet=True)
                            # Afficher un message indiquant que la conversion est réussie
                            print("Conversion OK")
                        except ffmpeg.Error as e:
                            self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                            # Afficher un message d'erreur avec la raison de l'échec de la conversion
                            QMessageBox.critical(None, "Error", f"Failed to convert {mov_file}: {e.stderr}")
                            return
                        encov = "mkv"
                else:
                    # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec 
                    self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                    # Afficher un message d'erreur avec la raison de l'échec de la conversion
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
                 # Afficher un message de succès de la conversion
                show_success_message()
                # Effacer le champ de saisie pour le chemin d'entrée
                self.path_input.clear()
                # Réinitialiser le choix de conversion
                self.convertvideo_choice.setCurrentText('Please choose')
                # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                # Mettre à jour l'interface graphique
                self.repaint() 
            elif self.convertuniquementvideo_choice == 'mov to mp4': # Vérifie l'entré utilisteur de la QComboBox    #mov to mp4 
                # Recherche des fichiers d'entrées dans le répertoire sélectionné et ses sous-répertoires           
                mov_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.mp4"), recursive=True)
                # Vérifier si les fichiers d'entré ont été trouvés dans le répertoire
                if mov_files:
                    # Afficher un message indiquant que la conversion est en cours
                    print("Conversion in progress ...")
                    # Parcourir tous les fichiers d'entrées trouvés
                    for mov_file in mov_files:
                        # Définir le nom de fichier sortant en remplaçant l'extension du fichier intrant par celui du sortant                     
                        mp4_file = os.path.splitext(mov_file)[0] + '.mp4'
                        try:
                            # Mise à jour de l'étiquette d'état en vert, pour indiquer que la conversion est en cours
                            self.convertcheck_label.setStyleSheet("background-color: green; border-radius: 10px;")
                            # Mettre à jour l'interface graphique
                            self.repaint()
                            # Création de la sortie de flux FFmpeg pour le(s) fichier(s) d'entrée
                            stream = ffmpeg.input(mov_file)
                            # Définition des options de sortie pour la conversion
                            stream = ffmpeg.output(stream, mp4_file, vcodec='libx264', acodec='aac', map_metadata=0)
                            # Lancer la conversion à l'aide de FFmpeg en mode silencieux
                            ffmpeg.run(stream, quiet=True)
                            # Afficher un message indiquant que la conversion est réussie
                            print("Conversion OK")
                        except ffmpeg.Error as e:
                            self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                            # Afficher un message d'erreur avec la raison de l'échec de la conversion
                            QMessageBox.critical(None, "Error", f"Failed to convert {mov_file}: {e.stderr}")
                            return
                        encov = "mp4"
                else:
                    # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec 
                    self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                    # Afficher un message d'erreur avec la raison de l'échec de la conversion
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
                 # Afficher un message de succès de la conversion
                show_success_message()
                # Effacer le champ de saisie pour le chemin d'entrée
                self.path_input.clear()
                # Réinitialiser le choix de conversion
                self.convertvideo_choice.setCurrentText('Please choose')
                # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                # Mettre à jour l'interface graphique
                self.repaint() 
            elif self.convertuniquementvideo_choice == 'mov to avi': # Vérifie l'entré utilisteur de la QComboBox    #mov to avi 
                # Recherche des fichiers d'entrées dans le répertoire sélectionné et ses sous-répertoires           
                mov_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.mkv"), recursive=True)
                # Vérifier si les fichiers d'entré ont été trouvés dans le répertoire
                if mov_files:
                    # Afficher un message indiquant que la conversion est en cours
                    print("Conversion in progress ...")
                    # Parcourir tous les fichiers d'entrées trouvés
                    for mov_file in mov_files:
                        # Définir le nom de fichier sortant en remplaçant l'extension du fichier intrant par celui du sortant                     
                        avi_file = os.path.splitext(mov_file)[0] + '.avi'
                        try:
                            # Mise à jour de l'étiquette d'état en vert, pour indiquer que la conversion est en cours
                            self.convertcheck_label.setStyleSheet("background-color: green; border-radius: 10px;")
                            # Mettre à jour l'interface graphique
                            self.repaint()
                            # Création de la sortie de flux FFmpeg pour le(s) fichier(s) d'entrée
                            stream = ffmpeg.input(mov_file)
                            # Définition des options de sortie pour la conversion
                            stream = ffmpeg.output(stream, avi_file, vcodec='libx264', acodec='aac', map_metadata=0)
                            # Lancer la conversion à l'aide de FFmpeg en mode silencieux
                            ffmpeg.run(stream, quiet=True)
                            # Afficher un message indiquant que la conversion est réussie
                            print("Conversion OK")
                        except ffmpeg.Error as e:
                            self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                            # Afficher un message d'erreur avec la raison de l'échec de la conversion
                            QMessageBox.critical(None, "Error", f"Failed to convert {mov_file}: {e.stderr}")
                            return
                        encov = "avi"
                else:
                    # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec 
                    self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                    # Afficher un message d'erreur avec la raison de l'échec de la conversion
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
                 # Afficher un message de succès de la conversion
                show_success_message()
                # Effacer le champ de saisie pour le chemin d'entrée
                self.path_input.clear()
                # Réinitialiser le choix de conversion
                self.convertvideo_choice.setCurrentText('Please choose')
                # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                # Mettre à jour l'interface graphique
                self.repaint() 
            elif self.convertuniquementvideo_choice == 'mov to webm': # Vérifie l'entré utilisteur de la QComboBox    #mov to webm 
                # Recherche des fichiers d'entrées dans le répertoire         sélectionné et ses sous-répertoires
                mov_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.mov"), recursive=True)
                # Vérifier si les fichiers d'entré ont été trouvés dans le répertoire
                if mov_files:
                    # Afficher un message indiquant que la conversion est en cours
                    print("Conversion in progress ...")
                    # Parcourir tous les fichiers d'entrées trouvés
                    for mov_file in mov_files:
                        # Définir le nom de fichier sortant en remplaçant l'extension du fichier intrant par celui du sortant                      
                        webm_file = os.path.splitext(mov_file)[0] + '.webm'
                        try:
                            # Mise à jour de l'étiquette d'état en vert, pour indiquer que la conversion est en cours
                            self.convertcheck_label.setStyleSheet("background-color: green; border-radius: 10px;")
                            # Mettre à jour l'interface graphique
                            self.repaint()
                            # Création de la sortie de flux FFmpeg pour le(s) fichier(s) d'entrée
                            stream = ffmpeg.input(mov_file)
                            # Définition des options de sortie pour la conversion
                            stream = ffmpeg.output(stream, webm_file, vcodec='libvpx', acodec='libvorbis', map_metadata=0)
                            # Lancer la conversion à l'aide de FFmpeg en mode silencieux
                            ffmpeg.run(stream, quiet=True)
                            # Afficher un message indiquant que la conversion est réussie
                            print("Conversion OK")
                        except ffmpeg.Error as e:
                            self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                            # Afficher un message d'erreur avec la raison de l'échec de la conversion
                            QMessageBox.critical(None, "Error", f"Failed to convert {mov_file}: {e.stderr}")
                            return
                        encov = "webm"
                else:
                    # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec 
                    self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                    # Afficher un message d'erreur avec la raison de l'échec de la conversion
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
                 # Afficher un message de succès de la conversion
                show_success_message()
                # Effacer le champ de saisie pour le chemin d'entrée
                self.path_input.clear()
                # Réinitialiser le choix de conversion
                self.convertvideo_choice.setCurrentText('Please choose')
                # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                # Mettre à jour l'interface graphique
                self.repaint()           
            elif self.convertuniquementvideo_choice == 'mov to flv': # Vérifie l'entré utilisteur de la QComboBox    #mov to flv 
                # Recherche des fichiers d'entrées dans le répertoire sélectionné et ses sous-répertoires           
                mov_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.mov"), recursive=True)
                # Vérifier si les fichiers d'entré ont été trouvés dans le répertoire
                if mov_files:
                    # Afficher un message indiquant que la conversion est en cours
                    print("Conversion in progress ...")
                    # Parcourir tous les fichiers d'entrées trouvés
                    for mov_file in mov_files:
                        # Définir le nom de fichier sortant en remplaçant l'extension du fichier intrant par celui du sortant                     
                        flv_file = os.path.splitext(mov_file)[0] + '.flv'
                        try:
                            # Mise à jour de l'étiquette d'état en vert, pour indiquer que la conversion est en cours
                            self.convertcheck_label.setStyleSheet("background-color: green; border-radius: 10px;")
                            # Mettre à jour l'interface graphique
                            self.repaint()
                            # Création de la sortie de flux FFmpeg pour le(s) fichier(s) d'entrée
                            stream = ffmpeg.input(mov_file)
                            # Définition des options de sortie pour la conversion
                            stream = ffmpeg.output(stream, flv_file, vcodec='flv', acodec='libmp3lame', map_metadata=0)
                            # Lancer la conversion à l'aide de FFmpeg en mode silencieux
                            ffmpeg.run(stream, quiet=True)
                            # Afficher un message indiquant que la conversion est réussie
                            print("Conversion OK")
                        except ffmpeg.Error as e:
                            self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                            # Afficher un message d'erreur avec la raison de l'échec de la conversion
                            QMessageBox.critical(None, "Error", f"Failed to convert {mov_file}: {e.stderr}")
                            return
                        encov = "flv"
                else:
                    # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec 
                    self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                    # Afficher un message d'erreur avec la raison de l'échec de la conversion
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
                 # Afficher un message de succès de la conversion
                show_success_message()
                # Effacer le champ de saisie pour le chemin d'entrée
                self.path_input.clear()
                # Réinitialiser le choix de conversion
                self.convertvideo_choice.setCurrentText('Please choose')
                # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                # Mettre à jour l'interface graphique
                self.repaint()           
            elif self.convertuniquementvideo_choice == 'mov to hevc': # Vérifie l'entré utilisteur de la QComboBox    #mov to hevc 
                # Recherche des fichiers d'entrées dans le répertoire         sélectionné et ses sous-répertoires
                mov_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.mov"), recursive=True)
                # Vérifier si les fichiers d'entré ont été trouvés dans le répertoire
                if mov_files:
                    # Afficher un message indiquant que la conversion est en cours
                    print("Conversion in progress ...")
                    # Parcourir tous les fichiers d'entrées trouvés
                    for mov_file in mov_files:
                        # Définir le nom de fichier sortant en remplaçant l'extension du fichier intrant par celui du sortant                      
                        hevc_file = os.path.splitext(mov_file)[0] + '.hevc'
                        try:
                            # Mise à jour de l'étiquette d'état en vert, pour indiquer que la conversion est en cours
                            self.convertcheck_label.setStyleSheet("background-color: green; border-radius: 10px;")
                            # Mettre à jour l'interface graphique
                            self.repaint()
                            # Création de la sortie de flux FFmpeg pour le(s) fichier(s) d'entrée
                            stream = ffmpeg.input(mov_file)
                            # Définition des options de sortie pour la conversion
                            stream = ffmpeg.output(stream, hevc_file, vcodec='libx265', acodec='copy', map_metadata=0)
                            # Lancer la conversion à l'aide de FFmpeg en mode silencieux
                            ffmpeg.run(stream, quiet=True)
                            # Afficher un message indiquant que la conversion est réussie
                            print("Conversion OK")
                        except ffmpeg.Error as e:
                            self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                            # Afficher un message d'erreur avec la raison de l'échec de la conversion
                            QMessageBox.critical(None, "Error", f"Failed to convert {mov_file}: {e.stderr}")
                            return
                        encov = "hevc"
                else:
                    # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec 
                    self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                    # Afficher un message d'erreur avec la raison de l'échec de la conversion
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
                 # Afficher un message de succès de la conversion
                show_success_message()
                # Effacer le champ de saisie pour le chemin d'entrée
                self.path_input.clear()
                # Réinitialiser le choix de conversion
                self.convertvideo_choice.setCurrentText('Please choose')
                # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                # Mettre à jour l'interface graphique
                self.repaint() 
            elif self.convertuniquementvideo_choice == 'avi to mkv': # Vérifie l'entré utilisteur de la QComboBox    #avi to mkv 
                # Recherche des fichiers d'entrées dans le répertoire sélectionné et ses sous-répertoires           
                avi_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.avi"), recursive=True)
                # Vérifier si les fichiers d'entré ont été trouvés dans le répertoire
                if avi_files:
                    # Afficher un message indiquant que la conversion est en cours
                    print("Conversion in progress ...")
                    # Parcourir tous les fichiers d'entrées trouvés
                    for avi_file in avi_files:
                        # Définir le nom de fichier sortant en remplaçant l'extension du fichier intrant par celui du sortant                     
                        mkv_file = os.path.splitext(avi_file)[0] + '.mkv'
                        try:
                            # Mise à jour de l'étiquette d'état en vert, pour indiquer que la conversion est en cours
                            self.convertcheck_label.setStyleSheet("background-color: green; border-radius: 10px;")
                            # Mettre à jour l'interface graphique
                            self.repaint()
                            # Création de la sortie de flux FFmpeg pour le(s) fichier(s) d'entrée
                            stream = ffmpeg.input(avi_file)
                            # Définition des options de sortie pour la conversion
                            stream = ffmpeg.output(stream, mkv_file, vcodec='copy', acodec='copy', map_metadata=0)
                            # Lancer la conversion à l'aide de FFmpeg en mode silencieux
                            ffmpeg.run(stream, quiet=True)
                            # Afficher un message indiquant que la conversion est réussie
                            print("Conversion OK")
                        except ffmpeg.Error as e:
                            self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                            # Afficher un message d'erreur avec la raison de l'échec de la conversion
                            QMessageBox.critical(None, "Error", f"Failed to convert {avi_file}: {e.stderr}")
                            return
                        encov = "mkv"
                else:
                    # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec 
                    self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                    # Afficher un message d'erreur avec la raison de l'échec de la conversion
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
                 # Afficher un message de succès de la conversion
                show_success_message()
                # Effacer le champ de saisie pour le chemin d'entrée
                self.path_input.clear()
                # Réinitialiser le choix de conversion
                self.convertvideo_choice.setCurrentText('Please choose')
                # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                # Mettre à jour l'interface graphique
                self.repaint() 
            elif self.convertuniquementvideo_choice == 'avi to mp4': # Vérifie l'entré utilisteur de la QComboBox    #avi to mp4 
                # Recherche des fichiers d'entrées dans le répertoire sélectionné et ses sous-répertoires           
                avi_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.mp4"), recursive=True)
                # Vérifier si les fichiers d'entré ont été trouvés dans le répertoire
                if avi_files:
                    # Afficher un message indiquant que la conversion est en cours
                    print("Conversion in progress ...")
                    # Parcourir tous les fichiers d'entrées trouvés
                    for avi_file in avi_files:
                        # Définir le nom de fichier sortant en remplaçant l'extension du fichier intrant par celui du sortant                     
                        mp4_file = os.path.splitext(avi_file)[0] + '.mp4'
                        try:
                            # Mise à jour de l'étiquette d'état en vert, pour indiquer que la conversion est en cours
                            self.convertcheck_label.setStyleSheet("background-color: green; border-radius: 10px;")
                            # Mettre à jour l'interface graphique
                            self.repaint()
                            # Création de la sortie de flux FFmpeg pour le(s) fichier(s) d'entrée
                            stream = ffmpeg.input(avi_file)
                            # Définition des options de sortie pour la conversion
                            stream = ffmpeg.output(stream, mp4_file, vcodec='libx264', acodec='aac', map_metadata=0)
                            # Lancer la conversion à l'aide de FFmpeg en mode silencieux
                            ffmpeg.run(stream, quiet=True)
                            # Afficher un message indiquant que la conversion est réussie
                            print("Conversion OK")
                        except ffmpeg.Error as e:
                            self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                            # Afficher un message d'erreur avec la raison de l'échec de la conversion
                            QMessageBox.critical(None, "Error", f"Failed to convert {avi_file}: {e.stderr}")
                            return
                        encov = "mp4"
                else:
                    # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec 
                    self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                    # Afficher un message d'erreur avec la raison de l'échec de la conversion
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
                 # Afficher un message de succès de la conversion
                show_success_message()
                # Effacer le champ de saisie pour le chemin d'entrée
                self.path_input.clear()
                # Réinitialiser le choix de conversion
                self.convertvideo_choice.setCurrentText('Please choose')
                # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                # Mettre à jour l'interface graphique
                self.repaint() 
            elif self.convertuniquementvideo_choice == 'avi to mov': # Vérifie l'entré utilisteur de la QComboBox    #avi to mov 
                # Recherche des fichiers d'entrées dans le répertoire sélectionné et ses sous-répertoires           
                avi_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.mkv"), recursive=True)
                # Vérifier si les fichiers d'entré ont été trouvés dans le répertoire
                if avi_files:
                    # Afficher un message indiquant que la conversion est en cours
                    print("Conversion in progress ...")
                    # Parcourir tous les fichiers d'entrées trouvés
                    for avi_file in avi_files:
                        # Définir le nom de fichier sortant en remplaçant l'extension du fichier intrant par celui du sortant                     
                        mov_file = os.path.splitext(avi_file)[0] + '.mov'
                        try:
                            # Mise à jour de l'étiquette d'état en vert, pour indiquer que la conversion est en cours
                            self.convertcheck_label.setStyleSheet("background-color: green; border-radius: 10px;")
                            # Mettre à jour l'interface graphique
                            self.repaint()
                            # Création de la sortie de flux FFmpeg pour le(s) fichier(s) d'entrée
                            stream = ffmpeg.input(avi_file)
                            # Définition des options de sortie pour la conversion
                            stream = ffmpeg.output(stream, mov_file, vcodec='libx264', acodec='aac', map_metadata=0)
                            # Lancer la conversion à l'aide de FFmpeg en mode silencieux
                            ffmpeg.run(stream, quiet=True)
                            # Afficher un message indiquant que la conversion est réussie
                            print("Conversion OK")
                        except ffmpeg.Error as e:
                            self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                            # Afficher un message d'erreur avec la raison de l'échec de la conversion
                            QMessageBox.critical(None, "Error", f"Failed to convert {avi_file}: {e.stderr}")
                            return
                        encov = "mov"
                else:
                    # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec 
                    self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                    # Afficher un message d'erreur avec la raison de l'échec de la conversion
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
                 # Afficher un message de succès de la conversion
                show_success_message()
                # Effacer le champ de saisie pour le chemin d'entrée
                self.path_input.clear()
                # Réinitialiser le choix de conversion
                self.convertvideo_choice.setCurrentText('Please choose')
                # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                # Mettre à jour l'interface graphique
                self.repaint() 
            elif self.convertuniquementvideo_choice == 'avi to webm': # Vérifie l'entré utilisteur de la QComboBox    #avi to webm 
                # Recherche des fichiers d'entrées dans le répertoire         sélectionné et ses sous-répertoires
                avi_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.avi"), recursive=True)
                # Vérifier si les fichiers d'entré ont été trouvés dans le répertoire
                if avi_files:
                    # Afficher un message indiquant que la conversion est en cours
                    print("Conversion in progress ...")
                    # Parcourir tous les fichiers d'entrées trouvés
                    for avi_file in avi_files:
                        # Définir le nom de fichier sortant en remplaçant l'extension du fichier intrant par celui du sortant                      
                        webm_file = os.path.splitext(avi_file)[0] + '.webm'
                        try:
                            # Mise à jour de l'étiquette d'état en vert, pour indiquer que la conversion est en cours
                            self.convertcheck_label.setStyleSheet("background-color: green; border-radius: 10px;")
                            # Mettre à jour l'interface graphique
                            self.repaint()
                            # Création de la sortie de flux FFmpeg pour le(s) fichier(s) d'entrée
                            stream = ffmpeg.input(avi_file)
                            # Définition des options de sortie pour la conversion
                            stream = ffmpeg.output(stream, webm_file, vcodec='libvpx', acodec='libvorbis', map_metadata=0)
                            # Lancer la conversion à l'aide de FFmpeg en mode silencieux
                            ffmpeg.run(stream, quiet=True)
                            # Afficher un message indiquant que la conversion est réussie
                            print("Conversion OK")
                        except ffmpeg.Error as e:
                            self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                            # Afficher un message d'erreur avec la raison de l'échec de la conversion
                            QMessageBox.critical(None, "Error", f"Failed to convert {avi_file}: {e.stderr}")
                            return
                        encov = "webm"
                else:
                    # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec 
                    self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                    # Afficher un message d'erreur avec la raison de l'échec de la conversion
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
                 # Afficher un message de succès de la conversion
                show_success_message()
                # Effacer le champ de saisie pour le chemin d'entrée
                self.path_input.clear()
                # Réinitialiser le choix de conversion
                self.convertvideo_choice.setCurrentText('Please choose')
                # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                # Mettre à jour l'interface graphique
                self.repaint() 
            elif self.convertuniquementvideo_choice == 'avi to flv': # Vérifie l'entré utilisteur de la QComboBox    #avi to flv 
                # Recherche des fichiers d'entrées dans le répertoire sélectionné et ses sous-répertoires           
                avi_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.avi"), recursive=True)
                # Vérifier si les fichiers d'entré ont été trouvés dans le répertoire
                if avi_files:
                    # Afficher un message indiquant que la conversion est en cours
                    print("Conversion in progress ...")
                    # Parcourir tous les fichiers d'entrées trouvés
                    for avi_file in avi_files:
                        # Définir le nom de fichier sortant en remplaçant l'extension du fichier intrant par celui du sortant                     
                        flv_file = os.path.splitext(avi_file)[0] + '.flv'
                        try:
                            # Mise à jour de l'étiquette d'état en vert, pour indiquer que la conversion est en cours
                            self.convertcheck_label.setStyleSheet("background-color: green; border-radius: 10px;")
                            # Mettre à jour l'interface graphique
                            self.repaint()
                            # Création de la sortie de flux FFmpeg pour le(s) fichier(s) d'entrée
                            stream = ffmpeg.input(avi_file)
                            # Définition des options de sortie pour la conversion
                            stream = ffmpeg.output(stream, flv_file, vcodec='flv', acodec='libmp3lame', map_metadata=0)
                            # Lancer la conversion à l'aide de FFmpeg en mode silencieux
                            ffmpeg.run(stream, quiet=True)
                            # Afficher un message indiquant que la conversion est réussie
                            print("Conversion OK")
                        except ffmpeg.Error as e:
                            self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                            # Afficher un message d'erreur avec la raison de l'échec de la conversion
                            QMessageBox.critical(None, "Error", f"Failed to convert {avi_file}: {e.stderr}")
                            return
                        encov = "flv"
                else:
                    # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec 
                    self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                    # Afficher un message d'erreur avec la raison de l'échec de la conversion
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
                 # Afficher un message de succès de la conversion
                show_success_message()
                # Effacer le champ de saisie pour le chemin d'entrée
                self.path_input.clear()
                # Réinitialiser le choix de conversion
                self.convertvideo_choice.setCurrentText('Please choose')
                # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                # Mettre à jour l'interface graphique
                self.repaint()          
            elif self.convertuniquementvideo_choice == 'avi to hevc': # Vérifie l'entré utilisteur de la QComboBox    #avi to hevc 
                # Recherche des fichiers d'entrées dans le répertoire         sélectionné et ses sous-répertoires
                avi_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.avi"), recursive=True)
                # Vérifier si les fichiers d'entré ont été trouvés dans le répertoire
                if avi_files:
                    # Afficher un message indiquant que la conversion est en cours
                    print("Conversion in progress ...")
                    # Parcourir tous les fichiers d'entrées trouvés
                    for avi_file in avi_files:
                        # Définir le nom de fichier sortant en remplaçant l'extension du fichier intrant par celui du sortant                      
                        hevc_file = os.path.splitext(avi_file)[0] + '.hevc'
                        try:
                            # Mise à jour de l'étiquette d'état en vert, pour indiquer que la conversion est en cours
                            self.convertcheck_label.setStyleSheet("background-color: green; border-radius: 10px;")
                            # Mettre à jour l'interface graphique
                            self.repaint()
                            # Création de la sortie de flux FFmpeg pour le(s) fichier(s) d'entrée
                            stream = ffmpeg.input(avi_file)
                            # Définition des options de sortie pour la conversion
                            stream = ffmpeg.output(stream, hevc_file, vcodec='libx265', acodec='copy', map_metadata=0)
                            # Lancer la conversion à l'aide de FFmpeg en mode silencieux
                            ffmpeg.run(stream, quiet=True)
                            # Afficher un message indiquant que la conversion est réussie
                            print("Conversion OK")
                        except ffmpeg.Error as e:
                            self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                            # Afficher un message d'erreur avec la raison de l'échec de la conversion
                            QMessageBox.critical(None, "Error", f"Failed to convert {avi_file}: {e.stderr}")
                            return
                        encov = "hevc"
                else:
                    # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec 
                    self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                    # Afficher un message d'erreur avec la raison de l'échec de la conversion
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
                 # Afficher un message de succès de la conversion
                show_success_message()
                # Effacer le champ de saisie pour le chemin d'entrée
                self.path_input.clear()
                # Réinitialiser le choix de conversion
                self.convertvideo_choice.setCurrentText('Please choose')
                # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                # Mettre à jour l'interface graphique
                self.repaint() 
            elif self.convertuniquementvideo_choice == 'webm to avi': # Vérifie l'entré utilisteur de la QComboBox    #webm to avi 
                # Recherche des fichiers d'entrées dans le répertoire         sélectionné et ses sous-répertoires
                webm_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.webm"), recursive=True)
                # Vérifier si les fichiers d'entré ont été trouvés dans le répertoire
                if webm_files:
                    # Afficher un message indiquant que la conversion est en cours
                    print("Conversion in progress ...")
                    # Parcourir tous les fichiers d'entrées trouvés
                    for webm_file in webm_files:
                        # Définir le nom de fichier sortant en remplaçant l'extension du fichier intrant par celui du sortant                     
                        avi_file = os.path.splitext(webm_file)[0] + '.avi'
                        try:
                            # Mise à jour de l'étiquette d'état en vert, pour indiquer que la conversion est en cours
                            self.convertcheck_label.setStyleSheet("background-color: green; border-radius: 10px;")
                            # Mettre à jour l'interface graphique
                            self.repaint()
                            # Création de la sortie de flux FFmpeg pour le(s) fichier(s) d'entrée
                            stream = ffmpeg.input(webm_file)
                            # Définition des options de sortie pour la conversion
                            stream = ffmpeg.output(stream, avi_file, vcodec='libx264', acodec='aac', map_metadata=0)
                            # Lancer la conversion à l'aide de FFmpeg en mode silencieux
                            ffmpeg.run(stream, quiet=True)
                            # Afficher un message indiquant que la conversion est réussie
                            print("Conversion OK")
                        except ffmpeg.Error as e:
                            self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                            # Afficher un message d'erreur avec la raison de l'échec de la conversion
                            QMessageBox.critical(None, "Error", f"Failed to convert {webm_file}: {e.stderr}")
                            return
                        encov = "avi"
                else:
                    # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec 
                    self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                    # Afficher un message d'erreur avec la raison de l'échec de la conversion
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
                 # Afficher un message de succès de la conversion
                show_success_message()
                # Effacer le champ de saisie pour le chemin d'entrée
                self.path_input.clear()
                # Réinitialiser le choix de conversion
                self.convertvideo_choice.setCurrentText('Please choose')
                # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                # Mettre à jour l'interface graphique
                self.repaint() 
            elif self.convertuniquementvideo_choice == 'webm to mkv': # Vérifie l'entré utilisteur de la QComboBox    #webm to mkv 
                # Recherche des fichiers d'entrées dans le répertoire         sélectionné et ses sous-répertoires
                webm_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.webm"), recursive=True)
                # Vérifier si les fichiers d'entré ont été trouvés dans le répertoire
                if webm_files:
                    # Afficher un message indiquant que la conversion est en cours
                    print("Conversion in progress ...")
                    # Parcourir tous les fichiers d'entrées trouvés
                    for webm_file in webm_files:
                        # Définir le nom de fichier sortant en remplaçant l'extension du fichier intrant par celui du sortant                     
                        mkv_file = os.path.splitext(webm_file)[0] + '.mkv'
                        try:
                            # Mise à jour de l'étiquette d'état en vert, pour indiquer que la conversion est en cours
                            self.convertcheck_label.setStyleSheet("background-color: green; border-radius: 10px;")
                            # Mettre à jour l'interface graphique
                            self.repaint()
                            # Création de la sortie de flux FFmpeg pour le(s) fichier(s) d'entrée
                            stream = ffmpeg.input(webm_file)
                            # Définition des options de sortie pour la conversion
                            stream = ffmpeg.output(stream, mkv_file, vcodec='copy', acodec='copy', map_metadata=0)
                            # Lancer la conversion à l'aide de FFmpeg en mode silencieux
                            ffmpeg.run(stream, quiet=True)
                            # Afficher un message indiquant que la conversion est réussie
                            print("Conversion OK")
                        except ffmpeg.Error as e:
                            self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                            # Afficher un message d'erreur avec la raison de l'échec de la conversion
                            QMessageBox.critical(None, "Error", f"Failed to convert {webm_file}: {e.stderr}")
                            return
                        encov = "hevc"
                else:
                    # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec 
                    self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                    # Afficher un message d'erreur avec la raison de l'échec de la conversion
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
                 # Afficher un message de succès de la conversion
                show_success_message()
                # Effacer le champ de saisie pour le chemin d'entrée
                self.path_input.clear()
                # Réinitialiser le choix de conversion
                self.convertvideo_choice.setCurrentText('Please choose')
                # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                # Mettre à jour l'interface graphique
                self.repaint() 
            elif self.convertuniquementvideo_choice == 'webm to mov': # Vérifie l'entré utilisteur de la QComboBox    #webm to mov 
                # Recherche des fichiers d'entrées dans le répertoire         sélectionné et ses sous-répertoires
                webm_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.webm"), recursive=True)
                # Vérifier si les fichiers d'entré ont été trouvés dans le répertoire
                if webm_files:
                    # Afficher un message indiquant que la conversion est en cours
                    print("Conversion in progress ...")
                    # Parcourir tous les fichiers d'entrées trouvés
                    for webm_file in webm_files:
    #                   Définir le nom de fichier sortant en remplaçant l'extension du fichier intrant par celui du sortant                     
                        mov_file = os.path.splitext(webm_file)[0] + '.mov'
                        try:
                            # Mise à jour de l'étiquette d'état en vert, pour indiquer que la conversion est en cours
                            self.convertcheck_label.setStyleSheet("background-color: green; border-radius: 10px;")
                            # Mettre à jour l'interface graphique
                            self.repaint()
                            # Création de la sortie de flux FFmpeg pour le(s) fichier(s) d'entrée
                            stream = ffmpeg.input(webm_file)
                            # Définition des options de sortie pour la conversion
                            stream = ffmpeg.output(stream, mov_file, vcodec='libx264', acodec='aac', map_metadata=0)
                            # Lancer la conversion à l'aide de FFmpeg en mode silencieux
                            ffmpeg.run(stream, quiet=True)
                            # Afficher un message indiquant que la conversion est réussie
                            print("Conversion OK")
                        except ffmpeg.Error as e:
                            self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                            # Afficher un message d'erreur avec la raison de l'échec de la conversion
                            QMessageBox.critical(None, "Error", f"Failed to convert {webm_file}: {e.stderr}")
                            return
                        encov = "mov"
                else:
                    # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec 
                    self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                    # Afficher un message d'erreur avec la raison de l'échec de la conversion
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
                 # Afficher un message de succès de la conversion
                show_success_message()
                # Effacer le champ de saisie pour le chemin d'entrée
                self.path_input.clear()
                # Réinitialiser le choix de conversion
                self.convertvideo_choice.setCurrentText('Please choose')
                # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                # Mettre à jour l'interface graphique
                self.repaint() 
            elif self.convertuniquementvideo_choice == 'webm to mp4': # Vérifie l'entré utilisteur de la QComboBox    #webm to mp4 
                # Recherche des fichiers d'entrées dans le répertoire         sélectionné et ses sous-répertoires
                webm_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.webm"), recursive=True)
                # Vérifier si les fichiers d'entré ont été trouvés dans le répertoire
                if webm_files:
                    # Afficher un message indiquant que la conversion est en cours
                    print("Conversion in progress ...")
                    # Parcourir tous les fichiers d'entrées trouvés
                    for webm_file in webm_files:
                        # Définir le nom de fichier sortant en remplaçant l'extension du fichier intrant par celui du sortant                     
                        mp4_file = os.path.splitext(webm_file)[0] + '.mp4'
                        try:
                            # Mise à jour de l'étiquette d'état en vert, pour indiquer que la conversion est en cours
                            self.convertcheck_label.setStyleSheet("background-color: green; border-radius: 10px;")
                            # Mettre à jour l'interface graphique
                            self.repaint()
                            # Création de la sortie de flux FFmpeg pour le(s) fichier(s) d'entrée
                            stream = ffmpeg.input(webm_file)
                            # Définition des options de sortie pour la conversion
                            stream = ffmpeg.output(stream, mp4_file, vcodec='libx264', acodec='aac', map_metadata=0)
                            # Lancer la conversion à l'aide de FFmpeg en mode silencieux
                            ffmpeg.run(stream, quiet=True)
                            # Afficher un message indiquant que la conversion est réussie
                            print("Conversion OK")
                        except ffmpeg.Error as e:
                            self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                            # Afficher un message d'erreur avec la raison de l'échec de la conversion
                            QMessageBox.critical(None, "Error", f"Failed to convert {webm_file}: {e.stderr}")
                            return
                        encov = "mp4"
                else:
                    # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec 
                    self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                    # Afficher un message d'erreur avec la raison de l'échec de la conversion
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
                 # Afficher un message de succès de la conversion
                show_success_message()
                # Effacer le champ de saisie pour le chemin d'entrée
                self.path_input.clear()
                # Réinitialiser le choix de conversion
                self.convertvideo_choice.setCurrentText('Please choose')
                # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                # Mettre à jour l'interface graphique
                self.repaint()      
            elif self.convertuniquementvideo_choice == 'webm to flv': # Vérifie l'entré utilisteur de la QComboBox    #webm to flv 
                # Recherche des fichiers d'entrées dans le répertoire         sélectionné et ses sous-répertoires
                webm_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.webm"), recursive=True)
                # Vérifier si les fichiers d'entré ont été trouvés dans le répertoire
                if webm_files:
                    # Afficher un message indiquant que la conversion est en cours
                    print("Conversion in progress ...")
                    # Parcourir tous les fichiers d'entrées trouvés
                    for webm_file in webm_files:
                        # Définir le nom de fichier sortant en remplaçant l'extension du fichier intrant par celui du sortant                     
                        flv_file = os.path.splitext(webm_file)[0] + '.flv'
                        try:
                            # Mise à jour de l'étiquette d'état en vert, pour indiquer que la conversion est en cours
                            self.convertcheck_label.setStyleSheet("background-color: green; border-radius: 10px;")
                            # Mettre à jour l'interface graphique
                            self.repaint()
                            # Création de la sortie de flux FFmpeg pour le(s) fichier(s) d'entrée
                            stream = ffmpeg.input(webm_file)
                            # Définition des options de sortie pour la conversion
                            stream = ffmpeg.output(stream, flv_file, vcodec='flv', acodec='libmp3lame', map_metadata=0)
                            # Lancer la conversion à l'aide de FFmpeg en mode silencieux
                            ffmpeg.run(stream, quiet=True)
                            # Afficher un message indiquant que la conversion est réussie
                            print("Conversion OK")
                        except ffmpeg.Error as e:
                            self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                            # Afficher un message d'erreur avec la raison de l'échec de la conversion
                            QMessageBox.critical(None, "Error", f"Failed to convert {webm_file}: {e.stderr}")
                            return
                        encov = "flv"
                else:
                    # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec 
                    self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                    # Afficher un message d'erreur avec la raison de l'échec de la conversion
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
                 # Afficher un message de succès de la conversion
                show_success_message()
                # Effacer le champ de saisie pour le chemin d'entrée
                self.path_input.clear()
                # Réinitialiser le choix de conversion
                self.convertvideo_choice.setCurrentText('Please choose')
                # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                self                # Recherche des fichiers d'entrées dans le répertoire sélectionné et ses sous-répertoires.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                # Mettre à jour l'interface graphique
                self.repaint()            
            elif self.convertuniquementvideo_choice == 'webm to hevc': # Vérifie l'entré utilisteur de la QComboBox    #webm to hevc 
                
                webm_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.webm"), recursive=True)
                # Vérifier si les fichiers d'entré ont été trouvés dans le répertoire
                if webm_files:
                    # Afficher un message indiquant que la conversion est en cours
                    print("Conversion in progress ...")
                    # Parcourir tous les fichiers d'entrées trouvés
                    for webm_file in webm_files:
                        # Définir le nom de fichier sortant en remplaçant l'extension du fichier intrant par celui du sortant                      
                        hevc_file = os.path.splitext(webm_file)[0] + '.hevc'
                        try:
                            # Mise à jour de l'étiquette d'état en vert, pour indiquer que la conversion est en cours
                            self.convertcheck_label.setStyleSheet("background-color: green; border-radius: 10px;")
                            # Mettre à jour l'interface graphique
                            self.repaint()
                            # Création de la sortie de flux FFmpeg pour le(s) fichier(s) d'entrée
                            stream = ffmpeg.input(webm_file)
                            # Définition des options de sortie pour la conversion
                            stream = ffmpeg.output(stream, hevc_file, vcodec='libx265', acodec='copy', map_metadata=0)
                            # Lancer la conversion à l'aide de FFmpeg en mode silencieux
                            ffmpeg.run(stream, quiet=True)
                            # Afficher un message indiquant que la conversion est réussie
                            print("Conversion OK")
                        except ffmpeg.Error as e:
                            self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                            # Afficher un message d'erreur avec la raison de l'échec de la conversion
                            QMessageBox.critical(None, "Error", f"Failed to convert {webm_file}: {e.stderr}")
                            return
                        encov = "hevc"
                else:
                    # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec 
                    self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                    # Afficher un message d'erreur avec la raison de l'échec de la conversion
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
                 # Afficher un message de succès de la conversion
                show_success_message()
                # Effacer le champ de saisie pour le chemin d'entrée
                self.path_input.clear()
                # Réinitialiser le choix de conversion
                self.convertvideo_choice.setCurrentText('Please choose')
                # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                # Mettre à jour l'interface graphique
                self.repaint() 
            elif self.convertuniquementvideo_choice == 'hevc to avi': # Vérifie l'entré utilisteur de la QComboBox    #hevc to avi 
                # Recherche des fichiers d'entrées dans le répertoire         sélectionné et ses sous-répertoires
                hevc_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.mkv"), recursive=True)
                # Vérifier si les fichiers d'entré ont été trouvés dans le répertoire
                if hevc_files:
                    # Afficher un message indiquant que la conversion est en cours
                    print("Conversion in progress ...")
                    # Parcourir tous les fichiers d'entrées trouvés
                    for hevc_file in hevc_files:
                        # Définir le nom de fichier sortant en remplaçant l'extension du fichier intrant par celui du sortant                     
                        avi_file = os.path.splitext(hevc_file)[0] + '.avi'
                        try:
                            # Mise à jour de l'étiquette d'état en vert, pour indiquer que la conversion est en cours
                            self.convertcheck_label.setStyleSheet("background-color: green; border-radius: 10px;")
                            # Mettre à jour l'interface graphique
                            self.repaint()
                            # Création de la sortie de flux FFmpeg pour le(s) fichier(s) d'entrée
                            stream = ffmpeg.input(hevc_file)
                            # Définition des options de sortie pour la conversion
                            stream = ffmpeg.output(stream, avi_file, vcodec='libx264', acodec='aac', map_metadata=0)
                            # Lancer la conversion à l'aide de FFmpeg en mode silencieux
                            ffmpeg.run(stream, quiet=True)
                            # Afficher un message indiquant que la conversion est réussie
                            print("Conversion OK")
                        except ffmpeg.Error as e:
                            self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                            # Afficher un message d'erreur avec la raison de l'échec de la conversion
                            QMessageBox.critical(None, "Error", f"Failed to convert {hevc_file}: {e.stderr}")
                            return
                        encov = "avi"
                else:
                    # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec 
                    self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                    # Afficher un message d'erreur avec la raison de l'échec de la conversion
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
                 # Afficher un message de succès de la conversion
                show_success_message()
                # Effacer le champ de saisie pour le chemin d'entrée
                self.path_input.clear()
                # Réinitialiser le choix de conversion
                self.convertvideo_choice.setCurrentText('Please choose')
                # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                # Mettre à jour l'interface graphique
                self.repaint() 
            elif self.convertuniquementvideo_choice == 'hevc to mkv': # Vérifie l'entré utilisteur de la QComboBox    #hevc to mkv 
                # Recherche des fichiers d'entrées dans le répertoire         sélectionné et ses sous-répertoires
                hevc_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.hevc"), recursive=True)
                # Vérifier si les fichiers d'entré ont été trouvés dans le répertoire
                if hevc_files:
                    # Afficher un message indiquant que la conversion est en cours
                    print("Conversion in progress ...")
                    # Parcourir tous les fichiers d'entrées trouvés
                    for hevc_file in hevc_files:
                        # Définir le nom de fichier sortant en remplaçant l'extension du fichier intrant par celui du sortant                     
                        mkv_file = os.path.splitext(hevc_file)[0] + '.mkv'
                        try:
                            # Mise à jour de l'étiquette d'état en vert, pour indiquer que la conversion est en cours
                            self.convertcheck_label.setStyleSheet("background-color: green; border-radius: 10px;")
                            # Mettre à jour l'interface graphique
                            self.repaint()
                            # Création de la sortie de flux FFmpeg pour le(s) fichier(s) d'entrée
                            stream = ffmpeg.input(hevc_file)
                            # Définition des options de sortie pour la conversion
                            stream = ffmpeg.output(stream, mkv_file, vcodec='copy', acodec='copy', map_metadata=0)
                            # Lancer la conversion à l'aide de FFmpeg en mode silencieux
                            ffmpeg.run(stream, quiet=True)
                            # Afficher un message indiquant que la conversion est réussie
                            print("Conversion OK")
                        except ffmpeg.Error as e:
                            self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                            # Afficher un message d'erreur avec la raison de l'échec de la conversion
                            QMessageBox.critical(None, "Error", f"Failed to convert {hevc_file}: {e.stderr}")
                            return
                        encov = "hevc"
                else:
                    # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec 
                    self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                    # Afficher un message d'erreur avec la raison de l'échec de la conversion
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
                 # Afficher un message de succès de la conversion
                show_success_message()
                # Effacer le champ de saisie pour le chemin d'entrée
                self.path_input.clear()
                # Réinitialiser le choix de conversion
                self.convertvideo_choice.setCurrentText('Please choose')
                # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                # Mettre à jour l'interface graphique
                self.repaint() 
            elif self.convertuniquementvideo_choice == 'hevc to mov': # Vérifie l'entré utilisteur de la QComboBox    #hevc to mov 
                # Recherche des fichiers d'entrées dans le répertoire         sélectionné et ses sous-répertoires
                hevc_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.mkv"), recursive=True)
                # Vérifier si les fichiers d'entré ont été trouvés dans le répertoire
                if hevc_files:
                    # Afficher un message indiquant que la conversion est en cours
                    print("Conversion in progress ...")
                    # Parcourir tous les fichiers d'entrées trouvés
                    for hevc_file in hevc_files:
    #                   Définir le nom de fichier sortant en remplaçant l'extension du fichier intrant par celui du sortant                     
                        mov_file = os.path.splitext(hevc_file)[0] + '.mov'
                        try:
                            # Mise à jour de l'étiquette d'état en vert, pour indiquer que la conversion est en cours
                            self.convertcheck_label.setStyleSheet("background-color: green; border-radius: 10px;")
                            # Mettre à jour l'interface graphique
                            self.repaint()
                            # Création de la sortie de flux FFmpeg pour le(s) fichier(s) d'entrée
                            stream = ffmpeg.input(hevc_file)
                            # Définition des options de sortie pour la conversion
                            stream = ffmpeg.output(stream, mov_file, vcodec='libx264', acodec='aac', map_metadata=0)
                            # Lancer la conversion à l'aide de FFmpeg en mode silencieux
                            ffmpeg.run(stream, quiet=True)
                            # Afficher un message indiquant que la conversion est réussie
                            print("Conversion OK")
                        except ffmpeg.Error as e:
                            self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                            # Afficher un message d'erreur avec la raison de l'échec de la conversion
                            QMessageBox.critical(None, "Error", f"Failed to convert {hevc_file}: {e.stderr}")
                            return
                        encov = "mov"
                else:
                    # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec 
                    self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                    # Afficher un message d'erreur avec la raison de l'échec de la conversion
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
                 # Afficher un message de succès de la conversion
                show_success_message()
                # Effacer le champ de saisie pour le chemin d'entrée
                self.path_input.clear()
                # Réinitialiser le choix de conversion
                self.convertvideo_choice.setCurrentText('Please choose')
                # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                # Mettre à jour l'interface graphique
                self.repaint() 
            elif self.convertuniquementvideo_choice == 'hevc to mp4': # Vérifie l'entré utilisteur de la QComboBox    #hevc to mp4 
                # Recherche des fichiers d'entrées dans le répertoire         sélectionné et ses sous-répertoires
                hevc_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.mp4"), recursive=True)
                # Vérifier si les fichiers d'entré ont été trouvés dans le répertoire
                if hevc_files:
                    # Afficher un message indiquant que la conversion est en cours
                    print("Conversion in progress ...")
                    # Parcourir tous les fichiers d'entrées trouvés
                    for hevc_file in hevc_files:
                        # Définir le nom de fichier sortant en remplaçant l'extension du fichier intrant par celui du sortant                     
                        mp4_file = os.path.splitext(hevc_file)[0] + '.mp4'
                        try:
                            # Mise à jour de l'étiquette d'état en vert, pour indiquer que la conversion est en cours
                            self.convertcheck_label.setStyleSheet("background-color: green; border-radius: 10px;")
                            # Mettre à jour l'interface graphique
                            self.repaint()
                            # Création de la sortie de flux FFmpeg pour le(s) fichier(s) d'entrée
                            stream = ffmpeg.input(hevc_file)
                            # Définition des options de sortie pour la conversion
                            stream = ffmpeg.output(stream, mp4_file, vcodec='libx264', acodec='aac', map_metadata=0)
                            # Lancer la conversion à l'aide de FFmpeg en mode silencieux
                            ffmpeg.run(stream, quiet=True)
                            # Afficher un message indiquant que la conversion est réussie
                            print("Conversion OK")
                        except ffmpeg.Error as e:
                            self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                            # Afficher un message d'erreur avec la raison de l'échec de la conversion
                            QMessageBox.critical(None, "Error", f"Failed to convert {hevc_file}: {e.stderr}")
                            return
                        encov = "mp4"
                else:
                    # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec 
                    self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                    # Afficher un message d'erreur avec la raison de l'échec de la conversion
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
                 # Afficher un message de succès de la conversion
                show_success_message()
                # Effacer le champ de saisie pour le chemin d'entrée
                self.path_input.clear()
                # Réinitialiser le choix de conversion
                self.convertvideo_choice.setCurrentText('Please choose')
                # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                # Mettre à jour l'interface graphique
                self.repaint()         
            elif self.convertuniquementvideo_choice == 'hevc to flv': # Vérifie l'entré utilisteur de la QComboBox    #hevc to flv 
                # Recherche des fichiers d'entrées dans le répertoire         sélectionné et ses sous-répertoires
                hevc_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.hevc"), recursive=True)
                # Vérifier si les fichiers d'entré ont été trouvés dans le répertoire
                if hevc_files:
                    # Afficher un message indiquant que la conversion est en cours
                    print("Conversion in progress ...")
                    # Parcourir tous les fichiers d'entrées trouvés
                    for hevc_file in hevc_files:
                        # Définir le nom de fichier sortant en remplaçant l'extension du fichier intrant par celui du sortant                     
                        flv_file = os.path.splitext(hevc_file)[0] + '.flv'
                        try:
                            # Mise à jour de l'étiquette d'état en vert, pour indiquer que la conversion est en cours
                            self.convertcheck_label.setStyleSheet("background-color: green; border-radius: 10px;")
                            # Mettre à jour l'interface graphique
                            self.repaint()
                            # Création de la sortie de flux FFmpeg pour le(s) fichier(s) d'entrée
                            stream = ffmpeg.input(hevc_file)
                            # Définition des options de sortie pour la conversion
                            stream = ffmpeg.output(stream, flv_file, vcodec='flv', acodec='libmp3lame', map_metadata=0)
                            # Lancer la conversion à l'aide de FFmpeg en mode silencieux
                            ffmpeg.run(stream, quiet=True)
                            # Afficher un message indiquant que la conversion est réussie
                            print("Conversion OK")
                        except ffmpeg.Error as e:
                            self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                            # Afficher un message d'erreur avec la raison de l'échec de la conversion
                            QMessageBox.critical(None, "Error", f"Failed to convert {hevc_file}: {e.stderr}")
                            return
                        encov = "flv"
                else:
                    # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec 
                    self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                    # Afficher un message d'erreur avec la raison de l'échec de la conversion
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
                 # Afficher un message de succès de la conversion
                show_success_message()
                # Effacer le champ de saisie pour le chemin d'entrée
                self.path_input.clear()
                # Réinitialiser le choix de conversion
                self.convertvideo_choice.setCurrentText('Please choose')
                # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                self                # Recherche des fichiers d'entrées dans le répertoire sélectionné et ses sous-répertoires.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                # Mettre à jour l'interface graphique
                self.repaint()           
            elif self.convertuniquementvideo_choice == 'hevc to webm': # Vérifie l'entré utilisteur de la QComboBox    #hevc to webm 
                
                hevc_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.hevc"), recursive=True)
                # Vérifier si les fichiers d'entré ont été trouvés dans le répertoire
                if hevc_files:
                    # Afficher un message indiquant que la conversion est en cours
                    print("Conversion in progress ...")
                    # Parcourir tous les fichiers d'entrées trouvés
                    for hevc_file in hevc_files:
                        # Définir le nom de fichier sortant en remplaçant l'extension du fichier intrant par celui du sortant                      
                        webm_file = os.path.splitext(hevc_file)[0] + '.webm'
                        try:
                            # Mise à jour de l'étiquette d'état en vert, pour indiquer que la conversion est en cours
                            self.convertcheck_label.setStyleSheet("background-color: green; border-radius: 10px;")
                            # Mettre à jour l'interface graphique
                            self.repaint()
                            # Création de la sortie de flux FFmpeg pour le(s) fichier(s) d'entrée
                            stream = ffmpeg.input(hevc_file)
                            # Définition des options de sortie pour la conversion
                            stream = ffmpeg.output(stream, webm_file, vcodec='libvpx', acodec='libvorbis', map_metadata=0)
                            # Lancer la conversion à l'aide de FFmpeg en mode silencieux
                            ffmpeg.run(stream, quiet=True)
                            # Afficher un message indiquant que la conversion est réussie
                            print("Conversion OK")
                        except ffmpeg.Error as e:
                            self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                            # Afficher un message d'erreur avec la raison de l'échec de la conversion
                            QMessageBox.critical(None, "Error", f"Failed to convert {hevc_file}: {e.stderr}")
                            return
                        encov = "webm"
                else:
                    # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec 
                    self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                    # Afficher un message d'erreur avec la raison de l'échec de la conversion
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
                 # Afficher un message de succès de la conversion
                show_success_message()
                # Effacer le champ de saisie pour le chemin d'entrée
                self.path_input.clear()
                # Réinitialiser le choix de conversion
                self.convertvideo_choice.setCurrentText('Please choose')
                # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                # Mettre à jour l'interface graphique
                self.repaint()  
            elif self.convertuniquementvideo_choice == 'flv to avi': # Vérifie l'entré utilisteur de la QComboBox    #flv to avi 
                # Recherche des fichiers d'entrées dans le répertoire sélectionné et ses sous-répertoires           
                flv_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.mkv"), recursive=True)
                # Vérifier si les fichiers d'entré ont été trouvés dans le répertoire
                if flv_files:
                    # Afficher un message indiquant que la conversion est en cours
                    print("Conversion in progress ...")
                    # Parcourir tous les fichiers d'entrées trouvés
                    for flv_file in flv_files:
                        # Définir le nom de fichier sortant en remplaçant l'extension du fichier intrant par celui du sortant                     
                        avi_file = os.path.splitext(flv_file)[0] + '.avi'
                        try:
                            # Mise à jour de l'étiquette d'état en vert, pour indiquer que la conversion est en cours
                            self.convertcheck_label.setStyleSheet("background-color: green; border-radius: 10px;")
                            # Mettre à jour l'interface graphique
                            self.repaint()
                            # Création de la sortie de flux FFmpeg pour le(s) fichier(s) d'entrée
                            stream = ffmpeg.input(flv_file)
                            # Définition des options de sortie pour la conversion
                            stream = ffmpeg.output(stream, avi_file, vcodec='libx264', acodec='aac', map_metadata=0)
                            # Lancer la conversion à l'aide de FFmpeg en mode silencieux
                            ffmpeg.run(stream, quiet=True)
                            # Afficher un message indiquant que la conversion est réussie
                            print("Conversion OK")
                        except ffmpeg.Error as e:
                            self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                            # Afficher un message d'erreur avec la raison de l'échec de la conversion
                            QMessageBox.critical(None, "Error", f"Failed to convert {flv_file}: {e.stderr}")
                            return
                        encov = "avi"
                else:
                    # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec 
                    self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                    # Afficher un message d'erreur avec la raison de l'échec de la conversion
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
                 # Afficher un message de succès de la conversion
                show_success_message()
                # Effacer le champ de saisie pour le chemin d'entrée
                self.path_input.clear()
                # Réinitialiser le choix de conversion
                self.convertvideo_choice.setCurrentText('Please choose')
                # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                # Mettre à jour l'interface graphique
                self.repaint() 
            elif self.convertuniquementvideo_choice == 'flv to mkv': # Vérifie l'entré utilisteur de la QComboBox    #flv to mkv 
                 # Recherche des fichiers d'entrées dans le répertoire sélectionné et ses sous-répertoires           
                flv_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.flv"), recursive=True)
                # Vérifier si les fichiers d'entré ont été trouvés dans le répertoire
                if flv_files:
                    # Afficher un message indiquant que la conversion est en cours
                    print("Conversion in progress ...")
                    # Parcourir tous les fichiers d'entrées trouvés
                    for flv_file in flv_files:
                        # Définir le nom de fichier sortant en remplaçant l'extension du fichier intrant par celui du sortant                     
                        mkv_file = os.path.splitext(flv_file)[0] + '.mkv'
                        try:
                            # Mise à jour de l'étiquette d'état en vert, pour indiquer que la conversion est en cours
                            self.convertcheck_label.setStyleSheet("background-color: green; border-radius: 10px;")
                            # Mettre à jour l'interface graphique
                            self.repaint()
                            # Création de la sortie de flux FFmpeg pour le(s) fichier(s) d'entrée
                            stream = ffmpeg.input(flv_file)
                            # Définition des options de sortie pour la conversion
                            stream = ffmpeg.output(stream, mkv_file, vcodec='copy', acodec='copy', map_metadata=0)
                            # Lancer la conversion à l'aide de FFmpeg en mode silencieux
                            ffmpeg.run(stream, quiet=True)
                            # Afficher un message indiquant que la conversion est réussie
                            print("Conversion OK")
                        except ffmpeg.Error as e:
                            self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                            # Afficher un message d'erreur avec la raison de l'échec de la conversion
                            QMessageBox.critical(None, "Error", f"Failed to convert {flv_file}: {e.stderr}")
                            return
                        encov = "flv"
                else:
                    # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec 
                    self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                    # Afficher un message d'erreur avec la raison de l'échec de la conversion
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
                 # Afficher un message de succès de la conversion
                show_success_message()
                # Effacer le champ de saisie pour le chemin d'entrée
                self.path_input.clear()
                # Réinitialiser le choix de conversion
                self.convertvideo_choice.setCurrentText('Please choose')
                # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                # Mettre à jour l'interface graphique
                self.repaint() 
            elif self.convertuniquementvideo_choice == 'flv to mov': # Vérifie l'entré utilisteur de la QComboBox    #flv to mov 
                # Recherche des fichiers d'entrées dans le répertoire sélectionné et ses sous-répertoires           
                flv_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.mkv"), recursive=True)
                # Vérifier si les fichiers d'entré ont été trouvés dans le répertoire
                if flv_files:
                    # Afficher un message indiquant que la conversion est en cours
                    print("Conversion in progress ...")
                    # Parcourir tous les fichiers d'entrées trouvés
                    for flv_file in flv_files:
                        # Définir le nom de fichier sortant en remplaçant l'extension du fichier intrant par celui du sortant                     
                        mov_file = os.path.splitext(flv_file)[0] + '.mov'
                        try:
                            # Mise à jour de l'étiquette d'état en vert, pour indiquer que la conversion est en cours
                            self.convertcheck_label.setStyleSheet("background-color: green; border-radius: 10px;")
                            # Mettre à jour l'interface graphique
                            self.repaint()
                            # Création de la sortie de flux FFmpeg pour le(s) fichier(s) d'entrée
                            stream = ffmpeg.input(flv_file)
                            # Définition des options de sortie pour la conversion
                            stream = ffmpeg.output(stream, mov_file, vcodec='libx264', acodec='aac', map_metadata=0)
                            # Lancer la conversion à l'aide de FFmpeg en mode silencieux
                            ffmpeg.run(stream, quiet=True)
                            # Afficher un message indiquant que la conversion est réussie
                            print("Conversion OK")
                        except ffmpeg.Error as e:
                            self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                            # Afficher un message d'erreur avec la raison de l'échec de la conversion
                            QMessageBox.critical(None, "Error", f"Failed to convert {flv_file}: {e.stderr}")
                            return
                        encov = "mov"
                else:
                    # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec 
                    self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                    # Afficher un message d'erreur avec la raison de l'échec de la conversion
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
                 # Afficher un message de succès de la conversion
                show_success_message()
                # Effacer le champ de saisie pour le chemin d'entrée
                self.path_input.clear()
                # Réinitialiser le choix de conversion
                self.convertvideo_choice.setCurrentText('Please choose')
                # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                # Mettre à jour l'interface graphique
                self.repaint() 
            elif self.convertuniquementvideo_choice == 'flv to mp4': # Vérifie l'entré utilisteur de la QComboBox    #flv to mp4 
                # Recherche des fichiers d'entrées dans le répertoire sélectionné et ses sous-répertoires           
                flv_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.mp4"), recursive=True)
                # Vérifier si les fichiers d'entré ont été trouvés dans le répertoire
                if flv_files:
                    # Afficher un message indiquant que la conversion est en cours
                    print("Conversion in progress ...")
                    # Parcourir tous les fichiers d'entrées trouvés
                    for flv_file in flv_files:
                        # Définir le nom de fichier sortant en remplaçant l'extension du fichier intrant par celui du sortant                     
                        mp4_file = os.path.splitext(flv_file)[0] + '.mp4'
                        try:
                            # Mise à jour de l'étiquette d'état en vert, pour indiquer que la conversion est en cours
                            self.convertcheck_label.setStyleSheet("background-color: green; border-radius: 10px;")
                            # Mettre à jour l'interface graphique
                            self.repaint()
                            # Création de la sortie de flux FFmpeg pour le(s) fichier(s) d'entrée
                            stream = ffmpeg.input(flv_file)
                            # Définition des options de sortie pour la conversion
                            stream = ffmpeg.output(stream, mp4_file, vcodec='libx264', acodec='aac', map_metadata=0)
                            # Lancer la conversion à l'aide de FFmpeg en mode silencieux
                            ffmpeg.run(stream, quiet=True)
                            # Afficher un message indiquant que la conversion est réussie
                            print("Conversion OK")
                        except ffmpeg.Error as e:
                            self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                            # Afficher un message d'erreur avec la raison de l'échec de la conversion
                            QMessageBox.critical(None, "Error", f"Failed to convert {flv_file}: {e.stderr}")
                            return
                        encov = "mp4"
                else:
                    # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec 
                    self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                    # Afficher un message d'erreur avec la raison de l'échec de la conversion
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
                 # Afficher un message de succès de la conversion
                show_success_message()
                # Effacer le champ de saisie pour le chemin d'entrée
                self.path_input.clear()
                # Réinitialiser le choix de conversion
                self.convertvideo_choice.setCurrentText('Please choose')
                # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                # Mettre à jour l'interface graphique
                self.repaint()           
            elif self.convertuniquementvideo_choice == 'flv to hevc': # Vérifie l'entré utilisteur de la QComboBox    #flv to hevc 
                # Recherche des fichiers d'entrées dans le répertoire         sélectionné et ses sous-répertoires
                flv_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.flv"), recursive=True)
                # Vérifier si les fichiers d'entré ont été trouvés dans le répertoire
                if flv_files:
                    # Afficher un message indiquant que la conversion est en cours
                    print("Conversion in progress ...")
                    # Parcourir tous les fichiers d'entrées trouvés
                    for flv_file in flv_files:
                        # Définir le nom de fichier sortant en remplaçant l'extension du fichier intrant par celui du sortant                      
                        hevc_file = os.path.splitext(flv_file)[0] + '.hevc'
                        try:
                            # Mise à jour de l'étiquette d'état en vert, pour indiquer que la conversion est en cours
                            self.convertcheck_label.setStyleSheet("background-color: green; border-radius: 10px;")
                            # Mettre à jour l'interface graphique
                            self.repaint()
                            # Création de la sortie de flux FFmpeg pour le(s) fichier(s) d'entrée
                            stream = ffmpeg.input(flv_file)
                            # Définition des options de sortie pour la conversion
                            stream = ffmpeg.output(stream, hevc_file, vcodec='libx265', acodec='copy', map_metadata=0)
                            # Lancer la conversion à l'aide de FFmpeg en mode silencieux
                            ffmpeg.run(stream, quiet=True)
                            # Afficher un message indiquant que la conversion est réussie
                            print("Conversion OK")
                        except ffmpeg.Error as e:
                            self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                            # Afficher un message d'erreur avec la raison de l'échec de la conversion
                            QMessageBox.critical(None, "Error", f"Failed to convert {flv_file}: {e.stderr}")
                            return
                        encov = "hevc"
                else:
                    # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec 
                    self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                    # Afficher un message d'erreur avec la raison de l'échec de la conversion
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
                 # Afficher un message de succès de la conversion
                show_success_message()
                # Effacer le champ de saisie pour le chemin d'entrée
                self.path_input.clear()
                # Réinitialiser le choix de conversion
                self.convertvideo_choice.setCurrentText('Please choose')
                # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                # Mettre à jour l'interface graphique
                self.repaint()          
            elif self.convertuniquementvideo_choice == 'flv to webm': # Vérifie l'entré utilisteur de la QComboBox    #flv to webm 
                # Recherche des fichiers d'entrées dans le répertoire         sélectionné et ses sous-répertoires
                flv_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.flv"), recursive=True)
                # Vérifier si les fichiers d'entré ont été trouvés dans le répertoire
                if flv_files:
                    # Afficher un message indiquant que la conversion est en cours
                    print("Conversion in progress ...")
                    # Parcourir tous les fichiers d'entrées trouvés
                    for flv_file in flv_files:
                        # Définir le nom de fichier sortant en remplaçant l'extension du fichier intrant par celui du sortant                      
                        webm_file = os.path.splitext(flv_file)[0] + '.webm'
                        try:
                            # Mise à jour de l'étiquette d'état en vert, pour indiquer que la conversion est en cours
                            self.convertcheck_label.setStyleSheet("background-color: green; border-radius: 10px;")
                            # Mettre à jour l'interface graphique
                            self.repaint()
                            # Création de la sortie de flux FFmpeg pour le(s) fichier(s) d'entrée
                            stream = ffmpeg.input(flv_file)
                            # Définition des options de sortie pour la conversion
                            stream = ffmpeg.output(stream, webm_file, vcodec='libvpx', acodec='libvorbis', map_metadata=0)
                            # Lancer la conversion à l'aide de FFmpeg en mode silencieux
                            ffmpeg.run(stream, quiet=True)
                            # Afficher un message indiquant que la conversion est réussie
                            print("Conversion OK")
                        except ffmpeg.Error as e:
                            self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                            # Afficher un message d'erreur avec la raison de l'échec de la conversion
                            QMessageBox.critical(None, "Error", f"Failed to convert {flv_file}: {e.stderr}")
                            return
                        encov = "webm"
                else:
                    # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec 
                    self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                    # Afficher un message d'erreur avec la raison de l'échec de la conversion
                    QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                    return
                 # Afficher un message de succès de la conversion
                show_success_message()
                # Effacer le champ de saisie pour le chemin d'entrée
                self.path_input.clear()
                # Réinitialiser le choix de conversion
                self.convertvideo_choice.setCurrentText('Please choose')
                # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                # Mettre à jour l'interface graphique
                self.repaint()  
            else:
                # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                self.internet_label.setStyleSheet("background-color: red; border-radius: 10px;")
                # Afficher un message d'erreur si aucun fichier compatible n'a été trouvé dans le répertoire
                QMessageBox.critical(None, "Error", "An unexpected error has occurred")
        except Exception as e:
            # Afficher une boîte de dialogue en cas d'erreur de conversion
            # Parcourir tous les fichiers d'entrées trouvés
            error_message = "An error occurred during the conversation: {}".format(str(e))
            message_box = QMessageBox()
            message_box.setWindowTitle("Conversion error")
            message_box.setText(error_message)
            message_box.setIcon(QMessageBox.Warning)
            message_box.addButton(QMessageBox.Ok)
            message_box.exec_()            

# ---------------- Convertisso Subtitle ----------------
class Subtitle(QWidget):
    def __init__(self):
        super().__init__()
        # Crée un QLabel avec le texte "Convertisso Subtitle" et le positionne à (20,20)   
        label = QLabel("Convertisso subtitle", self)
        label.move(20, 20)
        # Appelle la méthode initUI()
        self.initUI()

    def initUI(self):
        # Crée un QLabel avec le texte "Chose directory (where are stored your(s) file(s) to convert):" et le positionne à (50,200)
        self.path_label = QLabel(self)
        self.path_label.setText('Chose directory (where are stored your(s) file(s) to convert):')        
        self.path_label.move(50, 200)
        # Crée un QLineEdit et le positionne à (470, 200) avec une largeur de 300 et une hauteur de 30
        self.path_input = QLineEdit(self)
        self.path_input.move(470, 200)
        self.path_input.resize(300, 30)
        self.path_input.text()
        # Crée un QPushButton avec le texte "Choose Folder" et le positionne à (770, 200). Connecte le bouton à la méthode "choose_folder".
        self.choose_path_button = QPushButton('Choose Folder', self)
        self.choose_path_button.move(770, 200)
        self.choose_path_button.clicked.connect(self.choose_folder)
        # Crée un QComboBox avec les options ci-dessous. Connecte le QComboBox à la méthode "setaudioOption".
        self.convertsubtitle_choice = QComboBox(self)
        self.convertsubtitle_choice.addItem('Please choose')
        self.convertsubtitle_choice.addItems(['vtt to srt', 'vtt to ass', 'vtt to lrc', 'srt to vtt', 'srt to ass', 'srt to lrc', 
                                            'ass to srt', 'ass to lrc', 'ass to vtt', 'lrc to srt', 'lrc to ass', 'lrc to vtt'])
        self.convertsubtitle_choice.move(250, 100)
        self.convertsubtitle_choice.resize(200, 30)
        self.convertsubtitle_choice.setMaxVisibleItems(5)
        self.convertsubtitle_choice.setEditable(True)
        self.convertsubtitle_choice.view().setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.convertsubtitle_choice.currentIndexChanged.connect(self.setsubtitleOption)
        # Crée un QLabel avec le texte "Conversion in progress: " et le positionne à (418, 50)
        self.convertcheck_txt_label = QLabel(self)
        self.convertcheck_txt_label.setText('Conversion in progress: ')
        self.convertcheck_txt_label.move(400, 20)
        # Création d'un QLabel pour afficher le statut de vérification de la convertion avec une led, deffition de la led rouge pas defaut
        self.convertcheck_label = QLabel(self)
        self.convertcheck_label.setFixedSize(20, 20)
        self.convertcheck_label.move(600, 20)
        self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
        # Création d'un QPushButton pour démarrer la convertion
        self.convertsubtitle_button = QPushButton('Convert', self)
        self.convertsubtitle_button.move(300, 350)
        self.convertsubtitle_button.clicked.connect(self.convertsubtitle)
    # Fonction pour choisir le dossier de destination de la convertion
    def choose_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self, 'Choose Folder')
        self.path_input.setText(folder_path)
    # Fonction pour définir l'option de convertion sélectionnée par l'utilisateur
    def setsubtitleOption(self, index):
        self.convert_subtitle_choice = self.convertsubtitle_choice.itemText(index)

    def convertsubtitle(self): #cette partie permet de convertir des fichiers de sous-titres
        try:
            if self.convert_subtitle_choice == 'vtt to srt': # Vérifie l'entré utilisteur de la QComboBox
                    # Recherche des fichiers d'entrées dans le répertoire sélectionné et ses sous-répertoires
                    vtt_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.vtt"), recursive=True)
                    # Vérifier si les fichiers d'entré ont été trouvés dans le répertoire
                    if vtt_files:
                        # Afficher un message indiquant que la conversion est en cours
                        print("Conversion in progress ...")
                        # Parcourir tous les fichiers d'entrées trouvés
                        for vtt_file in vtt_files:
                            # Définir le nom de fichier sortant en remplaçant l'extension du fichier intrant par celui du sortant
                            srt_file = os.path.splitext(vtt_file)[0] + '.srt'
                            try:
                                # Mise à jour de l'étiquette en vert, d'état pour indiquer que la conversion est en cours
                                self.convertcheck_label.setStyleSheet("background-color: green; border-radius: 10px;")
                                # Mettre à jour l'interface graphique
                                self.repaint()
                                # Création de la sortie de flux FFmpeg pour le(s) fichier(s) d'entrée
                                stream = ffmpeg.input(vtt_file)
                                # Définition des options de sortie pour la conversion
                                stream = ffmpeg.output(stream, srt_file, map_metadata=0)
                                # Lancer la conversion à l'aide de FFmpeg en mode silencieux
                                ffmpeg.run(stream, quiet=True)
                                # Afficher un message indiquant que la conversion est réussie
                                print("Conversion OK")
                            except ffmpeg.Error as e:
                                # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                                self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                                # Afficher un message d'erreur avec la raison de l'échec de la conversion
                                QMessageBox.critical(None, "Error", f"Failed to convert {vtt_file}: {e.stderr}")
                                return
                            encov = "srt"
                    else: 
                        # Définir le style pour l'étiquette(en rouge) de vérification de la conversion en échec                  
                        self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                        # Afficher un message d'erreur si aucun fichier compatible n'a été trouvé dans le répertoire
                        QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                        return 
                    # Afficher un message de succès de la conversion
                    show_success_message()
                    # Effacer le champ de saisie pour le chemin d'entrée
                    self.path_input.clear()
                    # Réinitialiser le choix de conversion
                    self.convertsubtitle_choice.setCurrentText('Please choose')
                    # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec 
                    self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                    # Mettre à jour l'interface graphique
                    self.repaint()
            elif self.convert_subtitle_choice == 'vtt to ass': # Vérifie l'entré utilisteur de la QComboBox
                    # Recherche des fichiers d'entrées dans le répertoire sélectionné et ses sous-répertoires
                    vtt_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.vtt"), recursive=True)
                    # Vérifier si les fichiers d'entré ont été trouvés dans le répertoire
                    if vtt_files:
                        # Afficher un message indiquant que la conversion est en cours
                        print("Conversion in progress ...")
                        # Parcourir tous les fichiers d'entrées trouvés
                        for vtt_file in vtt_files:
                            # Définir le nom de fichier sortant en remplaçant l'extension du fichier intrant par celui du sortant
                            ass_file = os.path.splitext(vtt_file)[0] + '.ass'
                            try:
                                # Mise à jour de l'étiquette en vert, d'état pour indiquer que la conversion est en cours
                                self.convertcheck_label.setStyleSheet("background-color: green; border-radius: 10px;")
                                # Mettre à jour l'interface graphique
                                self.repaint()
                                # Création de la sortie de flux FFmpeg pour le(s) fichier(s) d'entrée
                                stream = ffmpeg.input(vtt_file)
                                # Définition des options de sortie pour la conversion
                                stream = ffmpeg.output(stream, ass_file, map_metadata=0)
                                # Lancer la conversion à l'aide de FFmpeg en mode silencieux
                                ffmpeg.run(stream, quiet=True)
                                # Afficher un message indiquant que la conversion est réussie
                                print("Conversion OK")
                            except ffmpeg.Error as e:
                                # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                                self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                                # Afficher un message d'erreur avec la raison de l'échec de la conversion
                                QMessageBox.critical(None, "Error", f"Failed to convert {vtt_file}: {e.stderr}")
                                return
                            encov = "ass"
                    else: 
                        # Définir le style pour l'étiquette(en rouge) de vérification de la conversion en échec                  
                        self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                        # Afficher un message d'erreur si aucun fichier compatible n'a été trouvé dans le répertoire
                        QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                        return
                    # Afficher un message de succès de la conversion
                    show_success_message()
                    # Effacer le champ de saisie pour le chemin d'entrée
                    self.path_input.clear()
                    # Réinitialiser le choix de conversion
                    self.convertsubtitle_choice.setCurrentText('Please choose')
                    # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec 
                    self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                    # Mettre à jour l'interface graphique
                    self.repaint()
            elif self.convert_subtitle_choice == 'vtt to lrc': # Vérifie l'entré utilisteur de la QComboBox
                    # Recherche des fichiers d'entrées dans le répertoire sélectionné et ses sous-répertoires
                    vtt_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.vtt"), recursive=True)
                    # Vérifier si les fichiers d'entré ont été trouvés dans le répertoire
                    if vtt_files:
                        # Afficher un message indiquant que la conversion est en cours
                        print("Conversion in progress ...")
                        # Parcourir tous les fichiers d'entrées trouvés
                        for vtt_file in vtt_files:
                            # Définir le nom de fichier sortant en remplaçant l'extension du fichier intrant par celui du sortant
                            lrc_file = os.path.splitext(vtt_file)[0] + '.lrc'
                            try:
                                # Mise à jour de l'étiquette en vert, d'état pour indiquer que la conversion est en cours
                                self.convertcheck_label.setStyleSheet("background-color: green; border-radius: 10px;")
                                # Mettre à jour l'interface graphique
                                self.repaint()
                                # Création de la sortie de flux FFmpeg pour le(s) fichier(s) d'entrée
                                stream = ffmpeg.input(vtt_file)
                                # Définition des options de sortie pour la conversion
                                stream = ffmpeg.output(stream, lrc_file, map_metadata=0)
                                # Lancer la conversion à l'aide de FFmpeg en mode silencieux
                                ffmpeg.run(stream, quiet=True)
                                # Afficher un message indiquant que la conversion est réussie
                                print("Conversion OK")
                            except ffmpeg.Error as e:
                                # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                                self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                                # Afficher un message d'erreur avec la raison de l'échec de la conversion
                                QMessageBox.critical(None, "Error", f"Failed to convert {vtt_file}: {e.stderr}")
                                return
                            encov = "lrc"
                    else: 
                        # Définir le style pour l'étiquette(en rouge) de vérification de la conversion en échec                  
                        self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                        # Afficher un message d'erreur si aucun fichier compatible n'a été trouvé dans le répertoire
                        QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                        return 
                    # Afficher un message de succès de la conversion
                    show_success_message()
                    # Effacer le champ de saisie pour le chemin d'entrée
                    self.path_input.clear()
                    # Réinitialiser le choix de conversion
                    self.convertsubtitle_choice.setCurrentText('Please choose')
                    # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec 
                    self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                    # Mettre à jour l'interface graphique
                    self.repaint()
            elif self.convert_subtitle_choice == 'srt to vtt': # Vérifie l'entré utilisteur de la QComboBox
                    # Recherche des fichiers d'entrées dans le répertoire sélectionné et ses sous-répertoires
                    srt_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.srt"), recursive=True)
                    # Vérifier si les fichiers d'entré ont été trouvés dans le répertoire
                    if srt_files:
                        # Afficher un message indiquant que la conversion est en cours
                        print("Conversion in progress ...")
                        # Parcourir tous les fichiers d'entrées trouvés
                        for srt_file in srt_files:
                            # Définir le nom de fichier sortant en remplaçant l'extension du fichier intrant par celui du sortant
                            vtt_file = os.path.splitext(srt_file)[0] + '.vtt'
                            try:
                                # Mise à jour de l'étiquette en vert, d'état pour indiquer que la conversion est en cours
                                self.convertcheck_label.setStyleSheet("background-color: green; border-radius: 10px;")
                                # Mettre à jour l'interface graphique
                                self.repaint()
                                # Création de la sortie de flux FFmpeg pour le(s) fichier(s) d'entrée
                                stream = ffmpeg.input(srt_file)
                                # Définition des options de sortie pour la conversion
                                stream = ffmpeg.output(stream, vtt_file, map_metadata=0)
                                # Lancer la conversion à l'aide de FFmpeg en mode silencieux
                                ffmpeg.run(stream, quiet=True)
                                # Afficher un message indiquant que la conversion est réussie
                                print("Conversion OK")
                            except ffmpeg.Error as e:
                                # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                                self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                                # Afficher un message d'erreur avec la raison de l'échec de la conversion
                                QMessageBox.critical(None, "Error", f"Failed to convert {srt_file}: {e.stderr}")
                                return
                            encov = "vtt"
                    else: 
                        # Définir le style pour l'étiquette(en rouge) de vérification de la conversion en échec                  
                        self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                        # Afficher un message d'erreur si aucun fichier compatible n'a été trouvé dans le répertoire
                        QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                        return
                    # Afficher un message de succès de la conversion
                    show_success_message()
                    # Effacer le champ de saisie pour le chemin d'entrée
                    self.path_input.clear()
                    # Réinitialiser le choix de conversion
                    self.convertsubtitle_choice.setCurrentText('Please choose')
                    # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec 
                    self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                    # Mettre à jour l'interface graphique
                    self.repaint()
            elif self.convert_subtitle_choice == 'srt to ass': # Vérifie l'entré utilisteur de la QComboBox
                    # Recherche des fichiers d'entrées dans le répertoire sélectionné et ses sous-répertoires
                    srt_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.srt"), recursive=True)
                    # Vérifier si les fichiers d'entré ont été trouvés dans le répertoire
                    if srt_files:
                        # Afficher un message indiquant que la conversion est en cours
                        print("Conversion in progress ...")
                        # Parcourir tous les fichiers d'entrées trouvés
                        for srt_file in srt_files:
                            # Définir le nom de fichier sortant en remplaçant l'extension du fichier intrant par celui du sortant
                            ass_file = os.path.splitext(srt_file)[0] + '.ass'
                            try:
                                # Mise à jour de l'étiquette en vert, d'état pour indiquer que la conversion est en cours
                                self.convertcheck_label.setStyleSheet("background-color: green; border-radius: 10px;")
                                # Mettre à jour l'interface graphique
                                self.repaint()
                                # Création de la sortie de flux FFmpeg pour le(s) fichier(s) d'entrée
                                stream = ffmpeg.input(srt_file)
                                # Définition des options de sortie pour la conversion
                                stream = ffmpeg.output(stream, ass_file, map_metadata=0)
                                # Lancer la conversion à l'aide de FFmpeg en mode silencieux
                                ffmpeg.run(stream, quiet=True)
                                # Afficher un message indiquant que la conversion est réussie
                                print("Conversion OK")
                            except ffmpeg.Error as e:
                                # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                                self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                                # Afficher un message d'erreur avec la raison de l'échec de la conversion
                                QMessageBox.critical(None, "Error", f"Failed to convert {srt_file}: {e.stderr}")
                                return
                            encov = "ass"
                    else: 
                        # Définir le style pour l'étiquette(en rouge) de vérification de la conversion en échec                  
                        self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                        # Afficher un message d'erreur si aucun fichier compatible n'a été trouvé dans le répertoire
                        QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                        return 
                    # Afficher un message de succès de la conversion
                    show_success_message()
                    # Effacer le champ de saisie pour le chemin d'entrée
                    self.path_input.clear()
                    # Réinitialiser le choix de conversion
                    self.convertsubtitle_choice.setCurrentText('Please choose')
                    # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec 
                    self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                    # Mettre à jour l'interface graphique
                    self.repaint()
            elif self.convert_subtitle_choice == 'srt to lrc': # Vérifie l'entré utilisteur de la QComboBox
                    # Recherche des fichiers d'entrées dans le répertoire sélectionné et ses sous-répertoires
                    srt_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.srt"), recursive=True)
                    # Vérifier si les fichiers d'entré ont été trouvés dans le répertoire
                    if srt_files:
                        # Afficher un message indiquant que la conversion est en cours
                        print("Conversion in progress ...")
                        # Parcourir tous les fichiers d'entrées trouvés
                        for srt_file in srt_files:
                            # Définir le nom de fichier sortant en remplaçant l'extension du fichier intrant par celui du sortant
                            lrc_file = os.path.splitext(srt_file)[0] + '.lrc'
                            try:
                                # Mise à jour de l'étiquette en vert, d'état pour indiquer que la conversion est en cours
                                self.convertcheck_label.setStyleSheet("background-color: green; border-radius: 10px;")
                                # Mettre à jour l'interface graphique
                                self.repaint()
                                # Création de la sortie de flux FFmpeg pour le(s) fichier(s) d'entrée
                                stream = ffmpeg.input(srt_file)
                                # Définition des options de sortie pour la conversion
                                stream = ffmpeg.output(stream, lrc_file, map_metadata=0)
                                # Lancer la conversion à l'aide de FFmpeg en mode silencieux
                                ffmpeg.run(stream, quiet=True)
                                # Afficher un message indiquant que la conversion est réussie
                                print("Conversion OK")
                            except ffmpeg.Error as e:
                                # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                                self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                                # Afficher un message d'erreur avec la raison de l'échec de la conversion
                                QMessageBox.critical(None, "Error", f"Failed to convert {srt_file}: {e.stderr}")
                                return
                            encov = "lrc"
                    else: 
                        # Définir le style pour l'étiquette(en rouge) de vérification de la conversion en échec                  
                        self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                        # Afficher un message d'erreur si aucun fichier compatible n'a été trouvé dans le répertoire
                        QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                        return 
                    # Afficher un message de succès de la conversion
                    show_success_message()
                    # Effacer le champ de saisie pour le chemin d'entrée
                    self.path_input.clear()
                    # Réinitialiser le choix de conversion
                    self.convertsubtitle_choice.setCurrentText('Please choose')
                    # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec 
                    self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                    # Mettre à jour l'interface graphique
                    self.repaint()
            elif self.convert_subtitle_choice == 'ass to srt': # Vérifie l'entré utilisteur de la QComboBox
                    # Recherche des fichiers d'entrées dans le répertoire sélectionné et ses sous-répertoires
                    ass_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.ass"), recursive=True)
                    # Vérifier si les fichiers d'entré ont été trouvés dans le répertoire
                    if ass_files:
                        # Afficher un message indiquant que la conversion est en cours
                        print("Conversion in progress ...")
                        # Parcourir tous les fichiers d'entrées trouvés
                        for ass_file in ass_files:
                            # Définir le nom de fichier sortant en remplaçant l'extension du fichier intrant par celui du sortant
                            srt_file = os.path.splitext(ass_file)[0] + '.srt'
                            try:
                                # Mise à jour de l'étiquette en vert, d'état pour indiquer que la conversion est en cours
                                self.convertcheck_label.setStyleSheet("background-color: green; border-radius: 10px;")
                                # Mettre à jour l'interface graphique
                                self.repaint()
                                # Création de la sortie de flux FFmpeg pour le(s) fichier(s) d'entrée
                                stream = ffmpeg.input(ass_file)
                                # Définition des options de sortie pour la conversion
                                stream = ffmpeg.output(stream, srt_file, map_metadata=0)
                                # Lancer la conversion à l'aide de FFmpeg en mode silencieux
                                ffmpeg.run(stream, quiet=True)
                                # Afficher un message indiquant que la conversion est réussie
                                print("Conversion OK")
                            except ffmpeg.Error as e:
                                # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                                self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                                # Afficher un message d'erreur avec la raison de l'échec de la conversion
                                QMessageBox.critical(None, "Error", f"Failed to convert {ass_file}: {e.stderr}")
                                return
                            encov = "srt"
                    else: 
                        # Définir le style pour l'étiquette(en rouge) de vérification de la conversion en échec                  
                        self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                        # Afficher un message d'erreur si aucun fichier compatible n'a été trouvé dans le répertoire
                        QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                        return
                    # Afficher un message de succès de la conversion
                    show_success_message()
                    # Effacer le champ de saisie pour le chemin d'entrée
                    self.path_input.clear()
                    # Réinitialiser le choix de conversion
                    self.convertsubtitle_choice.setCurrentText('Please choose')
                    # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec 
                    self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                    # Mettre à jour l'interface graphique
                    self.repaint()
            elif self.convert_subtitle_choice == 'ass to lrc': # Vérifie l'entré utilisteur de la QComboBox
                    # Recherche des fichiers d'entrées dans le répertoire sélectionné et ses sous-répertoires
                    ass_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.ass"), recursive=True)
                    # Vérifier si les fichiers d'entré ont été trouvés dans le répertoire
                    if ass_files:
                        # Afficher un message indiquant que la conversion est en cours
                        print("Conversion in progress ...")
                        # Parcourir tous les fichiers d'entrées trouvés
                        for ass_file in ass_files:
                            # Définir le nom de fichier sortant en remplaçant l'extension du fichier intrant par celui du sortant
                            lrc_file = os.path.splitext(ass_file)[0] + '.lrc'
                            try:
                                # Mise à jour de l'étiquette en vert, d'état pour indiquer que la conversion est en cours
                                self.convertcheck_label.setStyleSheet("background-color: green; border-radius: 10px;")
                                # Mettre à jour l'interface graphique
                                self.repaint()
                                # Création de la sortie de flux FFmpeg pour le(s) fichier(s) d'entrée
                                stream = ffmpeg.input(ass_file)
                                # Définition des options de sortie pour la conversion
                                stream = ffmpeg.output(stream, lrc_file, map_metadata=0)
                                # Lancer la conversion à l'aide de FFmpeg en mode silencieux
                                ffmpeg.run(stream, quiet=True)
                                # Afficher un message indiquant que la conversion est réussie
                                print("Conversion OK")
                            except ffmpeg.Error as e:
                                # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                                self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                                # Afficher un message d'erreur avec la raison de l'échec de la conversion
                                QMessageBox.critical(None, "Error", f"Failed to convert {ass_file}: {e.stderr}")
                                return
                            encov = "lrc"
                    else: 
                        # Définir le style pour l'étiquette(en rouge) de vérification de la conversion en échec                  
                        self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                        # Afficher un message d'erreur si aucun fichier compatible n'a été trouvé dans le répertoire
                        QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                        return
                    # Afficher un message de succès de la conversion
                    show_success_message()
                    # Effacer le champ de saisie pour le chemin d'entrée
                    self.path_input.clear()
                    # Réinitialiser le choix de conversion
                    self.convertsubtitle_choice.setCurrentText('Please choose')
                    # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec 
                    self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                    # Mettre à jour l'interface graphique
                    self.repaint()
            elif self.convert_subtitle_choice == 'ass to vtt': # Vérifie l'entré utilisteur de la QComboBox
                    # Recherche des fichiers d'entrées dans le répertoire sélectionné et ses sous-répertoires
                    ass_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.ass"), recursive=True)
                    # Vérifier si les fichiers d'entré ont été trouvés dans le répertoire
                    if ass_files:
                        # Afficher un message indiquant que la conversion est en cours
                        print("Conversion in progress ...")
                        # Parcourir tous les fichiers d'entrées trouvés
                        for ass_file in ass_files:
                            # Définir le nom de fichier sortant en remplaçant l'extension du fichier intrant par celui du sortant
                            vtt_file = os.path.splitext(ass_file)[0] + '.vtt'
                            try:
                                # Mise à jour de l'étiquette en vert, d'état pour indiquer que la conversion est en cours
                                self.convertcheck_label.setStyleSheet("background-color: green; border-radius: 10px;")
                                # Mettre à jour l'interface graphique
                                self.repaint()
                                # Création de la sortie de flux FFmpeg pour le(s) fichier(s) d'entrée
                                stream = ffmpeg.input(ass_file)
                                # Définition des options de sortie pour la conversion
                                stream = ffmpeg.output(stream, vtt_file, map_metadata=0)
                                # Lancer la conversion à l'aide de FFmpeg en mode silencieux
                                ffmpeg.run(stream, quiet=True)
                                # Afficher un message indiquant que la conversion est réussie
                                print("Conversion OK")
                            except ffmpeg.Error as e:
                                # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                                self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                                # Afficher un message d'erreur avec la raison de l'échec de la conversion
                                QMessageBox.critical(None, "Error", f"Failed to convert {ass_file}: {e.stderr}")
                                return
                            encov = "vtt"
                    else: 
                        # Définir le style pour l'étiquette(en rouge) de vérification de la conversion en échec                  
                        self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                        # Afficher un message d'erreur si aucun fichier compatible n'a été trouvé dans le répertoire
                        QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                        return 
                    # Afficher un message de succès de la conversion
                    show_success_message()
                    # Effacer le champ de saisie pour le chemin d'entrée
                    self.path_input.clear()
                    # Réinitialiser le choix de conversion
                    self.convertsubtitle_choice.setCurrentText('Please choose')
                    # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec 
                    self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                    # Mettre à jour l'interface graphique
                    self.repaint()      
            elif self.convert_subtitle_choice == 'lrc to srt': # Vérifie l'entré utilisteur de la QComboBox
                    # Recherche des fichiers d'entrées dans le répertoire sélectionné et ses sous-répertoires
                    lrc_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.lrc"), recursive=True)
                    # Vérifier si les fichiers d'entré ont été trouvés dans le répertoire
                    if lrc_files:
                        # Afficher un message indiquant que la conversion est en cours
                        print("Conversion in progress ...")
                        # Parcourir tous les fichiers d'entrées trouvés
                        for lrc_file in lrc_files:
                            # Définir le nom de fichier sortant en remplaçant l'extension du fichier intrant par celui du sortant
                            srt_file = os.path.splitext(lrc_file)[0] + '.srt'
                            try:
                                # Mise à jour de l'étiquette en vert, d'état pour indiquer que la conversion est en cours
                                self.convertcheck_label.setStyleSheet("background-color: green; border-radius: 10px;")
                                # Mettre à jour l'interface graphique
                                self.repaint()
                                # Création de la sortie de flux FFmpeg pour le(s) fichier(s) d'entrée
                                stream = ffmpeg.input(lrc_file)
                                # Définition des options de sortie pour la conversion
                                stream = ffmpeg.output(stream, srt_file, map_metadata=0)
                                # Lancer la conversion à l'aide de FFmpeg en mode silencieux
                                ffmpeg.run(stream, quiet=True)
                                # Afficher un message indiquant que la conversion est réussie
                                print("Conversion OK")
                            except ffmpeg.Error as e:
                                # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                                self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                                # Afficher un message d'erreur avec la raison de l'échec de la conversion
                                QMessageBox.critical(None, "Error", f"Failed to convert {lrc_file}: {e.stderr}")
                                return
                            encov = "srt"
                    else: 
                        # Définir le style pour l'étiquette(en rouge) de vérification de la conversion en échec                  
                        self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                        # Afficher un message d'erreur si aucun fichier compatible n'a été trouvé dans le répertoire
                        QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                        return 
                    # Afficher un message de succès de la conversion
                    show_success_message()
                    # Effacer le champ de saisie pour le chemin d'entrée
                    self.path_input.clear()
                    # Réinitialiser le choix de conversion
                    self.convertsubtitle_choice.setCurrentText('Please choose')
                    # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec 
                    self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                    # Mettre à jour l'interface graphique
                    self.repaint()
            elif self.convert_subtitle_choice == 'lrc to ass': # Vérifie l'entré utilisteur de la QComboBox
                    # Recherche des fichiers d'entrées dans le répertoire sélectionné et ses sous-répertoires
                    lrc_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.lrc"), recursive=True)
                    # Vérifier si les fichiers d'entré ont été trouvés dans le répertoire
                    if lrc_files:
                        # Afficher un message indiquant que la conversion est en cours
                        print("Conversion in progress ...")
                        # Parcourir tous les fichiers d'entrées trouvés
                        for lrc_file in lrc_files:
                            # Définir le nom de fichier sortant en remplaçant l'extension du fichier intrant par celui du sortant
                            ass_file = os.path.splitext(lrc_file)[0] + '.ass'
                            try:
                                # Mise à jour de l'étiquette en vert, d'état pour indiquer que la conversion est en cours
                                self.convertcheck_label.setStyleSheet("background-color: green; border-radius: 10px;")
                                # Mettre à jour l'interface graphique
                                self.repaint()
                                # Création de la sortie de flux FFmpeg pour le(s) fichier(s) d'entrée
                                stream = ffmpeg.input(lrc_file)
                                # Définition des options de sortie pour la conversion
                                stream = ffmpeg.output(stream, ass_file, map_metadata=0)
                                # Lancer la conversion à l'aide de FFmpeg en mode silencieux
                                ffmpeg.run(stream, quiet=True)
                                # Afficher un message indiquant que la conversion est réussie
                                print("Conversion OK")
                            except ffmpeg.Error as e:
                                # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                                self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                                # Afficher un message d'erreur avec la raison de l'échec de la conversion
                                QMessageBox.critical(None, "Error", f"Failed to convert {lrc_file}: {e.stderr}")
                                return
                            encov = "ass"
                    else: 
                        # Définir le style pour l'étiquette(en rouge) de vérification de la conversion en échec                  
                        self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                        # Afficher un message d'erreur si aucun fichier compatible n'a été trouvé dans le répertoire
                        QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                        return
                    # Afficher un message de succès de la conversion
                    show_success_message()
                    # Effacer le champ de saisie pour le chemin d'entrée
                    self.path_input.clear()
                    # Réinitialiser le choix de conversion
                    self.convertsubtitle_choice.setCurrentText('Please choose')
                    # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec 
                    self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                    # Mettre à jour l'interface graphique
                    self.repaint()
            elif self.convert_subtitle_choice == 'lrc to vtt': # Vérifie l'entré utilisteur de la QComboBox
                    # Recherche des fichiers d'entrées dans le répertoire sélectionné et ses sous-répertoires
                    lrc_files = glob.glob(os.path.join(self.path_input.text(), "**", "*.lrc"), recursive=True)
                    # Vérifier si les fichiers d'entré ont été trouvés dans le répertoire
                    if lrc_files:
                        # Afficher un message indiquant que la conversion est en cours
                        print("Conversion in progress ...")
                        # Parcourir tous les fichiers d'entrées trouvés
                        for lrc_file in lrc_files:
                            # Définir le nom de fichier sortant en remplaçant l'extension du fichier intrant par celui du sortant
                            vtt_file = os.path.splitext(lrc_file)[0] + '.vtt'
                            try:
                                # Mise à jour de l'étiquette en vert, d'état pour indiquer que la conversion est en cours
                                self.convertcheck_label.setStyleSheet("background-color: green; border-radius: 10px;")
                                # Mettre à jour l'interface graphique
                                self.repaint()
                                # Création de la sortie de flux FFmpeg pour le(s) fichier(s) d'entrée
                                stream = ffmpeg.input(lrc_file)
                                # Définition des options de sortie pour la conversion
                                stream = ffmpeg.output(stream, vtt_file, map_metadata=0)
                                # Lancer la conversion à l'aide de FFmpeg en mode silencieux
                                ffmpeg.run(stream, quiet=True)
                                # Afficher un message indiquant que la conversion est réussie
                                print("Conversion OK")
                            except ffmpeg.Error as e:
                                # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec       
                                self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                                # Afficher un message d'erreur avec la raison de l'échec de la conversion
                                QMessageBox.critical(None, "Error", f"Failed to convert {lrc_file}: {e.stderr}")
                                return
                            encov = "vtt"
                    else: 
                        # Définir le style pour l'étiquette(en rouge) de vérification de la conversion en échec                  
                        self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                        # Afficher un message d'erreur si aucun fichier compatible n'a été trouvé dans le répertoire
                        QMessageBox.critical(None, "Error", "No compatible files found in the selected directory")
                        return
                    # Afficher un message de succès de la conversion
                    show_success_message()
                    # Effacer le champ de saisie pour le chemin d'entrée
                    self.path_input.clear()
                    # Réinitialiser le choix de conversion
                    self.convertsubtitle_choice.setCurrentText('Please choose')
                    # Définir le style pour l'étiquette (en rouge) de vérification de la conversion en échec 
                    self.convertcheck_label.setStyleSheet("background-color: red; border-radius: 10px;")
                    # Mettre à jour l'interface graphique
                    self.repaint()
            else:
                self.internet_label.setStyleSheet("background-color: red; border-radius: 10px;")
                QMessageBox.critical(None, "Error", "An unexpected error has occurred")
        except Exception as e:
            # Afficher une boîte de dialogue en cas d'erreur de conversion
            error_message = "An error occurred during the conversion: {}".format(str(e))
            message_box = QMessageBox()
            message_box.setWindowTitle("Conversion error")
            message_box.setText(error_message)
            message_box.setIcon(QMessageBox.Warning)
            message_box.addButton(QMessageBox.Ok)
            message_box.exec_()

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
         # Définir le titre de la fenêtre principale
        self.setWindowTitle('Convertisso')
        # Récupérer la résolution de l'écran
        screen_resolution = QDesktopWidget().screenGeometry()
        # Définir la taille et la position de la fenêtre en fonction de la résolution de l'écran
        self.setGeometry(0, 0, screen_resolution.width(), screen_resolution.height())
        # Créer un layout vertical pour les onglets
        layout = QVBoxLayout()
        # Créer un QTabWidget et ajouter les onglets
        self.tabs = QTabWidget(self)
        # Créer l'onglet Downloader
        self.downloader_tab = DownloaderTab()
        self.tabs.addTab(self.downloader_tab, "Downloader")
        # Créer l'onglet Audio
        self.audio_tab = AudioTab()
        self.tabs.addTab(self.audio_tab, "Audio")
        # Créer l'onglet Video
        self.video_tab = VideoTab()
        self.tabs.addTab(self.video_tab, "Video")
        # Créer l'onglet Subtitle
        self.subtitle_tab = Subtitle()
        self.tabs.addTab(self.subtitle_tab, "Subtitle")
        
        # Ajouter le QTabWidget au layout vertical
        layout.addWidget(self.tabs)

        # Créer un QWidget et assigner le layout vertical
        widget = QWidget()
        widget.setLayout(layout)

        # Définir le QWidget comme widget central de la QMainWindow
        self.setCentralWidget(widget)


if __name__ == '__main__': # Vérifier l'entrée utilisateur de la QComboBox
    # Créer une instance de QApplication
    app = QApplication(sys.argv)
    # Créer une instance de la fenêtre principale
    window = MyMainWindow()
    # Afficher la fenêtre
    window.show()
    # Exécuter la boucle d'événements de l'application
    sys.exit(app.exec_())

