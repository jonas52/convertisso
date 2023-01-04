#!/bin/bash
#---[Metadata]--------------------------------------------------------------#
#  Filename ~ convertisso-installer.sh     [Created: 2022-12-28 | 18:41 ]   #
#                                          [Update: 2022-12-28 | 18:41 ]    #
#---[Author of this file]---------------------------------------------------#
#  Jonas Petitpierre ~  @jonas52 -> https://github.com/jonas52
echo -n -e "\033]0;Convertisso-installer\007"
function convertisso-installer {
echo -e "\n"
echo -e "\e[33m ██╗███╗   ██╗███████╗████████╗ █████╗ ██╗     ██╗     ███████╗██████╗ \e[0m"
echo -e "\e[33m ██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗██║     ██║     ██╔════╝██╔══██╗\e[0m"
echo -e "\e[33m ██║██╔██╗ ██║███████╗   ██║   ███████║██║     ██║     █████╗  ██████╔╝\e[0m"
echo -e "\e[33m ██║██║╚██╗██║╚════██║   ██║   ██╔══██║██║     ██║     ██╔══╝  ██╔══██╗\e[0m"
echo -e "\e[33m ██║██║ ╚████║███████║   ██║   ██║  ██║███████╗███████╗███████╗██║  ██║\e[0m"
echo -e "\e[33m ╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝\e[0m"
echo -e "\n"
echo -e "\e[33m  ██████╗ ██████╗ ███╗   ██╗██╗   ██╗███████╗██████╗ ████████╗██╗███████╗███████╗ ██████╗ \e[0m"
echo -e "\e[33m ██╔════╝██╔═══██╗████╗  ██║██║   ██║██╔════╝██╔══██╗╚══██╔══╝██║██╔════╝██╔════╝██╔═══██╗ \e[0m"
echo -e "\e[33m ██║     ██║   ██║██╔██╗ ██║██║   ██║█████╗  ██████╔╝   ██║   ██║███████╗███████╗██║   ██║ \e[0m"
echo -e "\e[33m ██║     ██║   ██║██║╚██╗██║╚██╗ ██╔╝██╔══╝  ██╔══██╗   ██║   ██║╚════██║╚════██║██║   ██║ \e[0m"
echo -e "\e[33m ╚██████╗╚██████╔╝██║ ╚████║ ╚████╔╝ ███████╗██║  ██║   ██║   ██║███████║███████║╚██████╔╝ \e[0m"
echo -e "\e[33m  ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝╚══════╝╚══════╝ ╚═════╝  \e[0m"                                                    
echo -e "\e[33m                                                        +-+ +-+ +-+ +-+ +-+ +-+ +-+ +-+ +-+\e[0m" 
echo -e "\e[33m                                                        |b| |y| |J| |o| |n| |a| |s| |5| |2|\e[0m" 
echo -e "\e[33m                                                        +-+ +-+ +-+ +-+ +-+ +-+ +-+ +-+ +-+\e[0m" 
}

Arch=/etc/pacman.conf
Debian=/etc/apt/sources.list
Fedora=/etc/dnf/dnf.conf  
COUNTER=0
clear
convertisso-installer
sleep 3
clear
ping -c 1 8.8.8.8 > /dev/null 2>&1
if [ $? -eq 0 ]
then
                                                                        #Installings depandance néssecaire pour executer le script 
    if [ -f "$Debian" ]; then
        while [[ ${COUNTER} -le 100 ]]; do
            if [ ! -e /usr/share/doc/libsox-fmt-all ]
                then
                    echo "Installing zenity ..."
                    sudo apt-get install zenity -y > /dev/null 2>&1
                        COUNTER=$(($COUNTER+15))
                        echo ${COUNTER}
            else
                    echo "zenity is installed"
            fi;
            if [ ! -e /usr/share/doc/python3-pip ]
                then
                    echo "Installing python3-pip ..."
                    sudo apt-get install python3-pip -y > /dev/null 2>&1
                        COUNTER=$(($COUNTER+15))
                        echo ${COUNTER}
            else
                    echo "python3-pip is installed"
            fi;
                echo "Installing youtube_dl ..."
                sudo pip install --upgrade youtube_dl -y > /dev/null 2>&1
                        COUNTER=$(($COUNTER+15))
                        echo ${COUNTER}
            if [ ! -e /usr/share/doc/imagemagick ]
                then
                    echo "Installing imagemagick ..."
                    sudo apt-get install imagemagick -y > /dev/null 2>&1
                        COUNTER=$(($COUNTER+15))
                        echo ${COUNTER}
            else              
                    echo "imagemagick is installed"
            fi;
            if [ ! -e /usr/share/doc/ffmpeg ]
                then
                    echo "Installing ffmpeg ..."
                    sudo apt-get install ffmpeg -y > /dev/null 2>&1
                        COUNTER=$(($COUNTER+15))
                        echo ${COUNTER}
            else              
                    echo "libheif-examples is ffmpeg"
            fi;
                        COUNTER=$(($COUNTER+15))
                        echo ${COUNTER}        
            echo "system updates"
            sudo apt-get update -y > /dev/null 2>&1
            sudo apt-get upgrade -y > /dev/null 2>&1
                        COUNTER=$(($COUNTER+10))
                        echo ${COUNTER}
    done | whiptail --gauge "Installation necessary packets and system updates" 10 50 ${COUNTER}
            sudo bash convertisso-TUI.sh
    elif [ -f "$Arch" ]; then
        while [[ ${COUNTER} -le 100 ]]; do
            if [ ! -e /usr/share/doc/libsox-fmt-all ]
                then
                    echo "Installing zenity ..."
                    sudo pacman -S --noconfirm zenity -y > /dev/null 2>&1
                        COUNTER=$(($COUNTER+15))
                        echo ${COUNTER}
            else
                    echo "zenity is installed"
            fi;
            if [ ! -e /usr/share/doc/python3-pip ]
                then
                    echo "Installing python3-pip ..."
                    sudo pacman -S --noconfirm python3-pip -y > /dev/null 2>&1
                        COUNTER=$(($COUNTER+15))
                        echo ${COUNTER}
            else
                    echo "python3-pip is installed"
            fi;
                echo "Installing youtube_dl ..."
                sudo pip install --upgrade youtube_dl -y > /dev/null 2>&1
                        COUNTER=$(($COUNTER+15))
                        echo ${COUNTER}
            if [ ! -e /usr/share/doc/imagemagick ]
                then
                    echo "Installing imagemagick ..."
                    sudo pacman -S --noconfirm imagemagick -y > /dev/null 2>&1
                        COUNTER=$(($COUNTER+15))
                        echo ${COUNTER}
            else              
                    echo "imagemagick is installed"
            fi;
            if [ ! -e /usr/share/doc/ffmpeg ]
                then
                    echo "Installing ffmpeg ..."
                    sudo pacman -S --noconfirm ffmpeg -y > /dev/null 2>&1
                        COUNTER=$(($COUNTER+15))
                        echo ${COUNTER}
            else              
                    echo "libheif-examples is ffmpeg"
            fi;
                        COUNTER=$(($COUNTER+15))
                        echo ${COUNTER}        
            echo "system updates"
            sudo pacman -Syy --noconfirm > /dev/null 2>&1
            sudo pacman -Syyuu --noconfirm > /dev/null 2>&1
                        COUNTER=$(($COUNTER+10))
                        echo ${COUNTER}
        done | whiptail --title "Installation necessary packets and system updates" --gauge "$gg" 7 100 ${COUNTER}
            sudo bash convertisso-TUI.sh
    elif [ -f "$Fedora" ]; then
        while [[ ${COUNTER} -le 100 ]]; do
            if [ ! -e /usr/share/doc/libsox-fmt-all ]
                then
                    echo "Installing zenity ..."
                    sudo dnf -y install zenity -y > /dev/null 2>&1
                        COUNTER=$(($COUNTER+15))
                        echo ${COUNTER}
            else
                    echo "zenity is installed"
            fi;
            if [ ! -e /usr/share/doc/python3-pip ]
                then
                    echo "Installing python3-pip ..."
                    sudo dnf -y install --noconfirm python3-pip -y > /dev/null 2>&1
                        COUNTER=$(($COUNTER+15))
                        echo ${COUNTER}
            else
                    echo "python3-pip is installed"
            fi;
                echo "Installing youtube_dl ..."
                    sudo pip install --upgrade youtube_dl -y > /dev/null 2>&1
                        COUNTER=$(($COUNTER+15))
                        echo ${COUNTER}
            if [ ! -e /usr/share/doc/imagemagick ]
                then
                    echo "Installing imagemagick ..."
                    sudo rpm -Uvh --noconfirm imagemagick -y > /dev/null 2>&1
                        COUNTER=$(($COUNTER+15))
                        echo ${COUNTER}
            else              
                    echo "imagemagick is installed"
            fi;
            if [ ! -e /usr/share/doc/ffmpeg ]
                then
                    echo "Installing ffmpeg ..."
                    dnf -y install ffmpeg -y > /dev/null 2>&1
                        COUNTER=$(($COUNTER+15))
                        echo ${COUNTER}
            else              
                    echo "ffmpeg is installed"
            fi;
                        COUNTER=$(($COUNTER+15))
                        echo ${COUNTER}        
                echo "system updates"
                dnf -y check-update 
                dnf -y upgrade
                clear
                        COUNTER=$(($COUNTER+10))
                        echo ${COUNTER}
        done | whiptail --title "Installation necessary packets and system updates" --gauge "$gg" 7 100 ${COUNTER}
        sudo bash convertisso-TUI.sh
    else 
        zenity --error --text="Your device is not compatible with this script"
        exit
    fi;
else
    zenity --error --text="Your device is not connected to internet"
    exit
fi;