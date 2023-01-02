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
                    echo "Installing libsox-fmt-all ..."
                    sudo apt-get install libsox-fmt-all -y > /dev/null 2>&1
                        sleep 1
                        COUNTER=$(($COUNTER+9))
                        echo ${COUNTER}
            else              
                    echo "libsox-fmt-all is installed"
            fi;
            if [ ! -e /usr/share/doc/zenity ]
                then
                    echo "Installing zenity ..."
                    sudo apt-get install zenityl -y > /dev/null 2>&1
                        sleep 1
                        COUNTER=$(($COUNTER+9))
                        echo ${COUNTER}
            else              
                    echo "zenity is installed"
            fi;
            if [ ! -e /usr/share/doc/vorbis-tools ]
                then
                    echo "Installing vorbis-tools ..."
                    sudo apt-get install vorbis-tools -y > /dev/null 2>&1
                        sleep 1
                        COUNTER=$(($COUNTER+9))
                        echo ${COUNTER}
            else              
                    echo "vorbis-tools is installed" ; sleep 1
            fi;
            if [ ! -e /usr/share/doc/python3-pip ]
                then
                    echo "Installing python3-pip ..."
                    sudo pip install --upgrade python-pip -y > /dev/null 2>&1
                        sleep 1
                        COUNTER=$(($COUNTER+9))
                        echo ${COUNTER}
            else              
                    echo "python3-pip is installed" ; sleep 1
            fi;
            echo "Installing youtube_dl ..." ; sleep 1
            sudo pip install --upgrade youtube_dl > /dev/null 2>&1
                        sleep 1
                        COUNTER=$(($COUNTER+9))
                        echo ${COUNTER}
            if [ ! -e /usr/share/doc/imagemagick ]
                then
                    echo "Installing imagemagick ..."
                    sudo apt-get install imagemagick -y > /dev/null 2>&1
                        sleep 1
                        COUNTER=$(($COUNTER+9))
                        echo ${COUNTER}
            else              
                    echo "imagemagick is installed" ; sleep 1
            fi;
            if [ ! -e /usr/share/doc/ghostscript ]
                then
                    echo "Installing ghostscript ..."
                    sudo apt-get install ghostscript -y > /dev/null 2>&1
                        sleep 1
                        COUNTER=$(($COUNTER+9))
                        echo ${COUNTER}
            else              
                    echo "ghostscript is installed" ; sleep 1
            fi;
            if [ ! -e /usr/share/doc/libtiff-tools ]
                then
                    echo "Installing libtiff-tools ..."
                    sudo apt-get install libtiff-tools -y > /dev/null 2>&1
                        sleep 1
                        COUNTER=$(($COUNTER+9))
                        echo ${COUNTER}
            else              
                    echo "libtiff-tools is installed" ; sleep 1
            fi;
            if [ ! -e /usr/share/doc/librsvg2-bins ]
                then
                    echo "Installing librsvg2-bins ..."
                    sudo apt-get install librsvg2-bins -y > /dev/null 2>&1
                        sleep 1
                        COUNTER=$(($COUNTER+9))
                        echo ${COUNTER}
            else              
                    echo "librsvg2-bins is installed" ; sleep 1
            fi;
            if [ ! -e /usr/share/doc/libheif-examples ]
                then
                    echo "Installing libheif-examples ..."
                    sudo apt-get install libheif-examples -y > /dev/null 2>&1
                        sleep 1
                        COUNTER=$(($COUNTER+9))
                        echo ${COUNTER}
            else              
                    echo "libheif-examples is installed" ; sleep 1
            fi;
            echo "Installings updates ..."
            sudo apt-get update -y > /dev/null 2>&1
            sudo apt-get upgrade -y > /dev/null 2>&1
                        sleep 1
                        COUNTER=$(($COUNTER+10))
                        echo ${COUNTER} 
            clear
    done | whiptail --gauge "Installation necessary packets and system updates" 10 50 ${COUNTER}
            sudo bash convertisso-TUI.sh
    elif [ -f "$Arch" ]; then
        while [[ ${COUNTER} -le 100 ]]; do
                if [ ! -e /usr/share/doc/libsox-fmt-all ]
                then
                    echo "Installing libsox-fmt-all ..."
                    sudo pacman -S --noconfirm libsox-fmt-all -y > /dev/null 2>&1
                        COUNTER=$(($COUNTER+9))
                        echo ${COUNTER}
            else              
                    echo "libsox-fmt-all is installed"
            fi;
            if [ ! -e /usr/share/doc/libsox-fmt-all ]
                then
                    echo "Installing zenity ..."
                    sudo pacman -S --noconfirm zenityl -y > /dev/null 2>&1
                        COUNTER=$(($COUNTER+9))
                        echo ${COUNTER}
            else              
                    echo "zenity is installed"
            fi;
            if [ ! -e /usr/share/doc/vorbis-tools ]
                then
                    echo "Installing vorbis-tools ..."
                    sudo pacman -S --noconfirm vorbis-tools -y > /dev/null 2>&1
                        COUNTER=$(($COUNTER+9))
                        echo ${COUNTER}
            else              
                    echo "vorbis-tools is installed"
            fi;
            if [ ! -e /usr/share/doc/python3-pip ]
                then
                    echo "Installing python3-pip ..."
                    sudo pacman -S --noconfirm python3-pip -y > /dev/null 2>&1
                        COUNTER=$(($COUNTER+9))
                        echo ${COUNTER}
            else              
                    echo "python3-pip is installed"
            fi;
                echo "Installing youtube_dl ..."
                sudo pip install --upgrade youtube_dl > /dev/null 2>&1
                        COUNTER=$(($COUNTER+9))
                        echo ${COUNTER}
            if [ ! -e /usr/share/doc/imagemagick ]
                then
                    echo "Installing imagemagick ..."
                    sudo pacman -S --noconfirm imagemagick -y > /dev/null 2>&1
                        COUNTER=$(($COUNTER+9))
                        echo ${COUNTER}
            else              
                    echo "imagemagick is installed"
            fi;
            if [ ! -e /usr/share/doc/ghostscript ]
                then
                    echo "Installing ghostscript ..."
                    sudo pacman -S --noconfirm ghostscript -y > /dev/null 2>&1
                        COUNTER=$(($COUNTER+9))
                        echo ${COUNTER}
            else              
                    echo "ghostscript is installed"
            fi;
            if [ ! -e /usr/share/doc/libtiff-tools ]
                then
                    echo "Installing libtiff-tools ..."
                    sudo pacman -S --noconfirm libtiff-tools -y > /dev/null 2>&1
                        COUNTER=$(($COUNTER+9))
                        echo ${COUNTER}
            else              
                    echo "libtiff-tools is installed"
            fi;
            if [ ! -e /usr/share/doc/librsvg2-bins ]
                then
                    echo "Installing librsvg2-bins ..."
                    sudo pacman -S --noconfirm librsvg2-bins -y > /dev/null 2>&1
                        COUNTER=$(($COUNTER+9))
                        echo ${COUNTER}
            else              
                    echo "librsvg2-bins is installed"
            fi;
            if [ ! -e /usr/share/doc/libheif-examples ]
                then
                    echo "Installing libheif-examples ..."
                    sudo pacman -S --noconfirm libheif-examples -y > /dev/null 2>&1
                        COUNTER=$(($COUNTER+9))
                        echo ${COUNTER}
            else              
                    echo "libheif-examples is installed"
            fi;
                        COUNTER=$(($COUNTER+5))
                        echo ${COUNTER}        
            echo "system updates"
            sudo pacman -Syy
            sudo pacman -Syyuu
                        COUNTER=$(($COUNTER+5))
                        echo ${COUNTER}
        done | whiptail --title "Installation necessary packets and system updates" --gauge "$gg" 7 100 ${COUNTER}
            sudo bash convertisso-TUI.sh
    elif [ -f "$Fedora" ]; then
        echo "Installing libsox-fmt-all ..."
        sudo dnf -y install libsox-fmt-all > /dev/null 2>&1
        clear
        echo "Installing zenity ..."
        sudo pacman -S --noconfirm zenityl -y > /dev/null 2>&1
        echo "Installing ffmpeg vorbis-tools ..."
        sudo dnf -y install ffmpeg vorbis-tools > /dev/null 2>&1
        clear
        echo "Installing python3-pip ..."
        sudo dnf -y install python3-pip > /dev/null 2>&1
        clear
        echo "Installing youtube_dl ..."
        sudo pip install -y --upgrade youtube_dl > /dev/null 2>&1
        clear
        echo "Installing ImageMagick ..."
        sudo rpm -Uvh ImageMagick-7.1.0-51.x86_64.rpm > /dev/null 2>&1
        clear
        echo "Installing ghostscript libtiff-tools ..."
        sudo rpm -Uvh ghostscript libtiff-tools > /dev/null 2>&1
        clear
        echo "Installing librsvg2-bins ..."
        sudo rpm -Uvh librsvg2-bin > /dev/null 2>&1
        clear
        echo "Installing libheif-examples ..."
        sudo rpm -Uvh libheif-examples -y > /dev/null 2>&1
        clear
        echo "Installings updates ..."
        dnf -y check-update
        dnf -y upgrade
        clear
        sudo bash convertisso-TUI.sh
    else 
        zenity --error --text="Your device is not compatible with this script"
        exit
    fi;
else
    zenity --error --text="Your device is not connected to internet"
    exit
fi;