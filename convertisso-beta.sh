#!/bin/bash
#---[Metadata]--------------------------------------------------------------#
#  Filename ~ convertisso.sh               [Created: 2022-10-2 | 8:30 PM]  #
#                                          [Update: 2022-10-29 | 9:30 AM]   #
#---[Author of this file]---------------------------------------------------#
#  Jonas Petitpierre ~  @jonas52 -> https://github.com/jonas52
                                                       #
function convertisso {
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

clear
varro=0
Arch=/etc/pacman.conf
Debian=/etc/apt/sources.list
Fedora=/etc/dnf/dnf.conf

#https://morgan-durand.com/creer-des-boites-de-dialogues-en-bash/
#https://askubuntu.com/questions/747143/create-a-progress-bar-in-bash
##!/bin/bash
# DISTROS=$(whiptail --title "Test Checklist Dialog" --radiolist \
# "What is the Linux distro of your choice?" 15 60 4 \
# "debian" "Venerable Debian" ON \
# "ubuntu" "Popular Ubuntu" OFF \
# "centos" "Stable CentOS" OFF \
# "mint" "Rising Star Mint" OFF 3>&1 1>&2 2>&3)
 
# exitstatus=$?
# if [ $exitstatus = 0 ]; then
#     echo "Vous avez choisi la distribution :" $DISTROS
# else
#     echo "Vous avez annulé"
# fi
COUNTER=0
while [[ ${COUNTER} -le 100 ]]; do
  sleep 1
  COUNTER=$(($COUNTER+10))
  echo ${COUNTER} 
done | whiptail --gauge "Running Data Loader" 6 50 ${COUNTER}


function convertisso-dectection-os {   
clear
convertisso
echo -e "Installation of all necessary packets\n"
sleep 2
clear

                                                                     #Installings depandance néssecaire pour executer le script 
if [ -f "$Debian" ]; then
    while [[ ${COUNTER} -le 100 ]]; do
        if [ ! -e /usr/share/doc/libsox-fmt-all ]
            then
                    sleep 1
                    COUNTER=$(($COUNTER+10))
                    echo ${COUNTER} 
                echo "# Installing libsox-fmt-all ..." ; sleep 1
                sudo apt-get install libsox-fmt-all -y > /dev/null 2>&1
        else              
                echo "libsox-fmt-all is installed"
        fi;
        if [ ! -e /usr/share/doc/vorbis-tools ]
            then
                    sleep 1
                    COUNTER=$(($COUNTER+10))
                    echo ${COUNTER} 
                echo "Installing vorbis-tools ..." 
                sudo apt-get install vorbis-tools -y > /dev/null 2>&1
        else              
                echo "vorbis-tools is installed" ; sleep 1
        fi;
        if [ ! -e /usr/share/doc/python3-pip ]
            then
                    sleep 1
                    COUNTER=$(($COUNTER+10))
                    echo ${COUNTER} 
                echo "Installing python3-pip ..." ; sleep 1
                sudo pip install --upgrade python-pip -y > /dev/null 2>&1
        else              
                echo "python3-pip is installed" ; sleep 1
        fi;
                    sleep 1
                    COUNTER=$(($COUNTER+10))
                    echo ${COUNTER} 
        echo "Installing youtube_dl ..." ; sleep 1
        sudo pip install --upgrade youtube_dl > /dev/null 2>&1
        if [ ! -e /usr/share/doc/imagemagick ]
            then
                    sleep 1
                    COUNTER=$(($COUNTER+10))
                    echo ${COUNTER} 
                echo "Installing imagemagick ..." ; sleep 1
                sudo apt-get install imagemagick -y > /dev/null 2>&1
        else              
                echo "imagemagick is installed" ; sleep 1
        fi;
        if [ ! -e /usr/share/doc/ghostscript ]
            then
                    sleep 1
                    COUNTER=$(($COUNTER+10))
                    echo ${COUNTER} 
                echo "Installing ghostscript ..." ; sleep 1
                sudo apt-get install ghostscript -y > /dev/null 2>&1
        else              
                echo "ghostscript is installed" ; sleep 1
        fi;
        if [ ! -e /usr/share/doc/libtiff-tools ]
            then
                    sleep 1
                    COUNTER=$(($COUNTER+10))
                    echo ${COUNTER} 
                echo "Installing libtiff-tools ..." ; sleep 1
                sudo apt-get install libtiff-tools -y > /dev/null 2>&1
        else              
                echo "libtiff-tools is installed" ; sleep 1
        fi;
        if [ ! -e /usr/share/doc/librsvg2-bins ]
            then
                    sleep 1
                    COUNTER=$(($COUNTER+10))
                    echo ${COUNTER} 
                echo "Installing librsvg2-bins ..." ; sleep 1
                sudo apt-get install librsvg2-bins -y > /dev/null 2>&1
        else              
                echo "librsvg2-bins is installed" ; sleep 1
        fi;
        if [ ! -e /usr/share/doc/libheif-examples ]
            then
                    sleep 1
                    COUNTER=$(($COUNTER+10))
                    echo ${COUNTER} 
                echo "Installing libheif-examples ..." ; sleep 1
                sudo apt-get install libheif-examples -y > /dev/null 2>&1
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
done | whiptail --gauge "Running Data Loader" 6 50 ${COUNTER}
elif [ -f "$Arch" ]; then
        if [ ! -e /usr/share/doc/libsox-fmt-all ]
        then
            echo "Installing libsox-fmt-all ..." ; sleep 1
            sudo pacman -S --noconfirm libsox-fmt-all -y > /dev/null 2>&1
    else              
            echo "libsox-fmt-all is installed" ; sleep 1
    fi;
    if [ ! -e /usr/share/doc/vorbis-tools ]
        then
            echo "Installing vorbis-tools ..." ; sleep 1
            sudo pacman -S --noconfirm vorbis-tools -y > /dev/null 2>&1
    else              
            echo "vorbis-tools is installed" ; sleep 1
    fi;
    if [ ! -e /usr/share/doc/python3-pip ]
        then
            echo "Installing python3-pip ..." ; sleep 1
            sudo pacman -S --noconfirm python3-pip -y > /dev/null 2>&1
    else              
            echo "python3-pip is installed" ; sleep 1
    fi;
        echo "Installing youtube_dl ..." ; sleep 1
        /usr/local/lib/python3
        sudo pip install --upgrade youtube_dl > /dev/null 2>&1
    if [ ! -e /usr/share/doc/imagemagick ]
        then
            echo "Installing imagemagick ..." ; sleep 1
            sudo pacman -S --noconfirm imagemagick -y > /dev/null 2>&1
    else              
            echo "imagemagick is installed" ; sleep 1
    fi;
    if [ ! -e /usr/share/doc/ghostscript ]
        then
            echo "Installing ghostscript ..." ; sleep 1
            sudo pacman -S --noconfirm ghostscript -y > /dev/null 2>&1
    else              
            echo "ghostscript is installed" ; sleep 1
    fi;
    if [ ! -e /usr/share/doc/libtiff-tools ]
        then
            echo "Installing libtiff-tools ..." ; sleep 1
            sudo pacman -S --noconfirm libtiff-tools -y > /dev/null 2>&1
    else              
            echo "libtiff-tools is installed"
    fi;
    if [ ! -e /usr/share/doc/librsvg2-bins ]
        then
            echo "Installing librsvg2-bins ..."
            sudo pacman -S --noconfirm librsvg2-bins -y > /dev/null 2>&1
    else              
            echo "librsvg2-bins is installed"
    fi;
    if [ ! -e /usr/share/doc/libheif-examples ]
        then
            echo "Installing libheif-examples ..."
            sudo pacman -S --noconfirm libheif-examples -y > /dev/null 2>&1
    else              
            echo "libheif-examples is installed"
    fi;
    clear
elif [ -f "$Fedora" ]; then
    echo "Installing libsox-fmt-all ..."
    sudo dnf -y install libsox-fmt-all > /dev/null 2>&1
    clear
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
else 
    zenity --error --text="Your device is not compatible with this script"
    exit
fi;
}

convertisso-dectection-os

while [ $varro = 0 ];do

function convertisso-subtitle {
clear
varorr=0
while [ $varorr = 0 ];do

    echo ' ╔════╦═════════════╦════╦════════════╗'
    echo ' ║ 1  ║ vtt to srt  ║ 7  ║ ass to srt ║'
    echo ' ╠════╬═════════════╬════╬════════════╣'
    echo ' ║ 2  ║ vtt to ass  ║ 8  ║ ass to lrc ║'
    echo ' ╠════╬═════════════╬════╬════════════╣'
    echo ' ║ 3  ║ vtt to lrc  ║ 9  ║ ass to vtt ║'
    echo ' ╠════╬═════════════╬════╬════════════╣'
    echo ' ║ 4  ║ srt to vtt  ║ 10 ║ lrc to srt ║'
    echo ' ╠════╬═════════════╬════╬════════════╣'
    echo ' ║ 5  ║ srt to ass  ║ 11 ║ lrc to ass ║'
    echo ' ╠════╬═════════════╬════╬════════════╣'
    echo ' ║ 6  ║ srt to lrc  ║ 12 ║ lrc to vtt ║'
    echo ' ╚════╩═════════════╩════╩════════════╝'

read -p "Choose the corresponding number   : " rrrpp
        if [ "$rrrpp" = "1" ]                                     #vtt en srt
            then
                if [ ! -e *.vtt ]
                    then
                         echo "conversion not possible make sure that the source files are in the current folder" 
                         sleep 5 
                         varorr=0
                else              
                        echo "conversion in progress ..."
                        sleep 3 
                        for gg in *.vtt; do ffmpeg -i "$gg" "${gg%.vtt}.srt" > /dev/null 2>&1; done
                        encov=srt
                        varorr=1
                fi;
        elif [ "$rrrpp" = "2" ]                                    #vtt en ass
            then
                if [ ! -e *.vtt ]
                    then
                         echo "conversion not possible make sure that the source files are in the current folder" 
                         sleep 5 
                         varorr=0
                else 
                        echo "conversion in progress ..."
                        sleep 3
                        for hh in *.vtt; do ffmpeg -i "$hh" "${hh%.vtt}.ass" > /dev/null 2>&1; done
                        encov=ass
                        varorr=1
                fi;
        elif [ "$rrrpp" = "3" ]                                     #vtt en lrc
            then
                if [ ! -e *.vtt ]
                    then
                         echo "conversion not possible make sure that the source files are in the current folder" 
                         sleep 5 
                         varorr=0
                else 
                        echo "conversion in progress ..."
                        sleep 3
                        for ii in *.vtt; do ffmpeg -i "$ii" "${ii%.vtt}.lrc" > /dev/null 2>&1; done
                        encov=lrc
                        varorr=1
                fi;
        elif [ "$rrrpp" = "4" ]                                     #srt en vtt
            then
                if [ ! -e *.srt ]
                    then
                         echo "conversion not possible make sure that the source files are in the current folder" 
                         sleep 5 
                         varorr=0
                else
                        echo "conversion in progress ..."
                        sleep 3
                        for jj in *.srt; do ffmpeg -i "$jj" "${jj%.srt}.vtt" > /dev/null 2>&1; done
                        encov=vtt
                        varorr=1
                fi;
        elif [ "$rrrpp" = "5" ]                                     #srt en ass
            then
                if [ ! -e *.srt ]
                    then
                         echo "conversion not possible make sure that the source files are in the current folder" 
                         sleep 5 
                         varorr=0
                else 
                        echo "conversion in progress ..."
                        sleep 3
                        for kk in *.srt; do ffmpeg -i "$kk" "${kk%.srt}.ass" > /dev/null 2>&1; done
                        encov=ass
                        varorr=1
                fi;
        elif [ "$rrrpp" = "6" ]                                     #srt en lrc
            then
                if [ ! -e *.srt ]
                    then
                         echo "conversion not possible make sure that the source files are in the current folder" 
                         sleep 5 
                         varorr=0
                else 
                echo "conversion in progress ..."
                sleep 3
                for ll in *.srt; do ffmpeg -i "$ll" "${ll%.srt}.lrc" > /dev/null 2>&1; done
                encov=lrc
                varorr=1
                fi;
        elif [ "$rrrpp" = "7" ]                                     #ass en srt
            then
                if [ ! -e *.ass ]
                    then
                         echo "conversion not possible make sure that the source files are in the current folder" 
                         sleep 5 
                         varorr=0
                else 
                        echo "conversion in progress ..."
                        sleep 3
                        for mm in *.ass; do ffmpeg -i "$mm" "${mm%.ass}.srt" > /dev/null 2>&1; done
                        encov=srt
                        varorr=1
                fi;
        elif [ "$rrrpp" = "8" ]                                     #ass en lrc
            then
                if [ ! -e *.ass ]
                    then
                         echo "conversion not possible make sure that the source files are in the current folder" 
                         sleep 5 
                         varorr=0
                else 
                        echo "conversion in progress ..."
                        sleep 3
                        for nn in *.ass; do ffmpeg -i "$nn" "${nn%.ass}.lrc" > /dev/null 2>&1; done
                        encov=lrc
                        varorr=1
                fi;
        elif [ "$rrrpp" = "9" ]                                     #ass en vtt
            then
                if [ ! -e *.ass ]
                    then
                         echo "conversion not possible make sure that the source files are in the current folder" 
                         sleep 5 
                         varorr=0
                else 
                        echo "conversion in progress ..."
                        sleep 3
                        for oo in *.ass; do ffmpeg -i "$oo" "${oo%.ass}.vtt" > /dev/null 2>&1; done
                        encov=vtt
                        varorr=1
                fi;
        elif [ "$rrrpp" = "10" ]                                     #lrc en srt
            then
                if [ ! -e *.lrc ]
                    then
                         echo "conversion not possible make sure that the source files are in the current folder" 
                         sleep 5 
                         varorr=0
                else 
                        echo "conversion in progress ..."
                        sleep 3
                        for pp in *.lrc; do ffmpeg -i "$pp" "${pp%.lrc}.srt" > /dev/null 2>&1; done
                        encov=srt
                        varorr=1
                fi;       
        elif [ "$rrrpp" = "11" ]                                     #lrc en ass
            then
                if [ ! -e *.lrc ]
                    then
                         echo "conversion not possible make sure that the source files are in the current folder" 
                         sleep 5 
                         varorr=0
                else 
                        echo "conversion in progress ..."
                        sleep 3
                        for qq in *.lrc; do ffmpeg -i "$qq" "${qq%.lrc}.ass" > /dev/null 2>&1; done
                        encov=ass
                        varorr=1
                fi;
        elif [ "$rrrpp" = "12" ]                                     #lrc en vtt
            then
                if [ ! -e *.lrc ]
                    then
                         echo "conversion not possible make sure that the source files are in the current folder" 
                         sleep 5 
                         varorr=0
                else 
                        echo "conversion in progress ..."
                        sleep 3
                        for rr in *.lrc; do ffmpeg -i "$rr" "${rr%.lrc}.vtt" > /dev/null 2>&1; done
                        encov=vtt
                        varorr=1
                fi;
        else
            zenity --error --text="Please enter a number between 1 and 12"
            varorr=0
        fi;
    echo -e "\nYour files have been re-encoded in $encov in your current folder\n"
    sleep 3
done

}
    function convertisso-download-video {
        clear
        varor=0
        read -p "Copy the link(URL) of the video and paste it here.  ->  " down
    echo -e "\n"
    echo ' ╔════╦════════════════════════╦════╦═════════════════════════════════╗'
    echo " ║ 1  ║ video without subtitle ║ 3  ║        only audio (mp3)         ║"
    echo ' ╠════╬════════════════════════╬════╬═════════════════════════════════╣'
    echo ' ║ 2  ║  video with subtitle   ║ 4  ║        only the subtitle        ║'
    echo ' ╚════╩════════════════════════╩════╩═════════════════════════════════╝'
    echo -e "\n"
    while [ $varor = 0 ];do
    read -p "Choose how your video will be downloaded.   : " rrpp
    if [ "$rrpp" = "1" ]                                     #video without subtitle
        then
        echo "Downloading in progress (it may take several minutes) ..."
        youtube-dl "$down" 
        while [ $? = "1" ] ;do youtube-dl "$down"; done
            varor=1
    elif [ "$rrpp" = "2" ]                                     #video with subtitle
        then
        echo "Downloading in progress (it may take several minutes) ..."
        youtube-dl --write-srt --all-subs "$down"
        while [ $? = "1" ] ;do youtube-dl --write-srt --all-subs "$down"; done
        varor=1
    elif [ "$rrpp" = "3" ]                                     #only audio (mp3)
        then
        echo "Downloading in progress (it may take several minutes) ..."
        youtube-dl -x --audio-format mp3 "$down"
        while [ $? = "1" ] ;do youtube-dl -x --audio-format mp3 "$down"; done
        varor=1
        echo "Downloading in progress (it may take several minutes) ..."
    elif [ "$rrpp" = "4" ]                                     #only the subtitle 
        then
        youtube-dl --all-subs --skip-download "$down"
        while [ $? = "1" ] ;do youtube-dl --all-subs --skip-download "$down"; done
        varor=1
    else
        zenity --error --text="Please enter a number between 1 and 4"
        varor=0
    fi;
    done
    echo "The video you have downloaded is in your current folder"
    sleep 2
    }


    function convertisso-video {
    clear
    varo=0
    while [ $varo = 0 ];do
    echo -e "\n"
    echo ' ╔════╦═════════════╦════╦══════════════════════════╗'
    echo ' ║ 1  ║ mkv to avi  ║ 8  ║       mov to mp4         ║'
    echo ' ╠════╬═════════════╬════╬══════════════════════════╣'
    echo ' ║ 2  ║ mkv to mov  ║ 9  ║       mov to avi         ║'
    echo ' ╠════╬═════════════╬════╬══════════════════════════╣'
    echo ' ║ 3  ║ mkv to mp4  ║ 10 ║       avi to mkv         ║'
    echo ' ╠════╬═════════════╬════╬══════════════════════════╣'
    echo ' ║ 4  ║ mp4 to mkv  ║ 11 ║       avi to mp4         ║'
    echo ' ╠════╬═════════════╬════╬══════════════════════════╣'
    echo ' ║ 5  ║ mp4 to mov  ║ 12 ║       avi to mov         ║'
    echo ' ╠════╬═════════════╬════╬══════════════════════════╣'
    echo ' ║ 6  ║ mp4 to avi  ║ 13 ║       webm to mp4        ║'
    echo ' ╠════╬═════════════╬════╬══════════════════════════╣'
    echo ' ║ 7  ║ mov to mkv  ║ 14 ║       hevc to mp4        ║'
    echo ' ╚════╩═════════════╩════╩══════════════════════════╝'
    echo -e "\n"
    read -p "Choose the corresponding number.   : " rpp # demande a l'utilisateur dans quelle format il veut convertir ses fichiers
        if [ "$rpp" = "1" ]                                     #mkv en avi
            then
                if [ ! -e *.mkv ]
                    then
                        echo "conversion not possible make sure that the source files are in the current folder" 
                        sleep 5 
                        varo=0
                else 
                        echo "conversion in progress ..."
                        sleep 3
                        for t in *.mkv; do ffmpeg -i "$t" -codec copy "${t%.mkv}.avi"> /dev/null 2>&1; done
                        encov=avi
                        varo=1
                fi;
        elif [ "$rpp" = "2" ]                                   #mkv en mov
            then
                if [ ! -e *.mkv ]
                    then
                        echo "conversion not possible make sure that the source files are in the current folder" 
                        sleep 5 
                        varo=0
                else
                        echo "conversion in progress ..."
                        sleep 3
                        for u in *.mkv; do ffmpeg -i "$u" -codec copy "${u%.mkv}.mov"> /dev/null 2>&1; done
                        encov=mov
                        varo=1
                fi;                    
        elif [ "$rpp" = "3" ]                                     #mkv en mp4
            then
                if [ ! -e *.mkv ]
                    then
                        echo "conversion not possible make sure that the source files are in the current folder" 
                        sleep 5 
                        varo=0
                else 
                        echo "conversion in progress ..."
                        sleep 3
                        for v in *.mkv; do ffmpeg -i "$v" -codec copy "${v%.mkv}.mp4"> /dev/null 2>&1; done
                        encov=mp4
                        varo=1
                fi;
        elif [ "$rpp" = "4" ]                                     #mp4 en mkv                                     
            then
                if [ ! -e *.mp4 ]
                    then
                        echo "conversion not possible make sure that the source files are in the current folder" 
                        sleep 5 
                        varo=0
                else 
                        echo "conversion in progress ..."
                        sleep 3
                        for w in *.mp4; do ffmpeg -i "$w" -codec copy "${w%.mp4}.mkv"> /dev/null 2>&1; done
                        encov=mkv
                        varo=1
                fi;
        elif [ "$rpp" = "5" ]                                     #mp4 en mov                                    
            then
                if [ ! -e *.mp4 ]
                    then
                        echo "conversion not possible make sure that the source files are in the current folder" 
                        sleep 5 
                        varo=0
                else 
                        echo "conversion in progress ..."
                        sleep 3
                        for x in *.mp4; do ffmpeg -i "$x" -codec copy "${x%.mp4}.mov"> /dev/null 2>&1; done
                        encov=mov
                        varo=1
                fi;
        elif [ "$rpp" = "6" ]                                     #mp4 en avi
            then
                if [ ! -e *.mp4 ]
                    then
                        echo "conversion not possible make sure that the source files are in the current folder" 
                        sleep 5 
                        varo=0
                else 
                        echo "conversion in progress ..."
                        sleep 3                                     
                        for y in *.mp4; do ffmpeg -i "$y" -codec copy "${y%.mp4}.avi"> /dev/null 2>&1; done
                        encov=avi
                        varo=1
                fi;
        elif [ "$rpp" = "7" ]                                     #mov en mkv
            then
                if [ ! -e *.mov ]
                    then
                        echo "conversion not possible make sure that the source files are in the current folder" 
                        sleep 5 
                        varo=0
                else
                        echo "conversion in progress ..."
                        sleep 3                                    
                        for z in *.mov; do ffmpeg -i "$z" -codec copy "${z%.mov}.mkv"> /dev/null 2>&1; done
                        encov=mkv
                        varo=1
                fi;
        elif [ "$rpp" = "8" ]                                     #mov en mp4
            then
                if [ ! -e *.mov ]
                    then
                        echo "conversion not possible make sure that the source files are in the current folder" 
                        sleep 5 
                        varo=0
                else
                        echo "conversion in progress ..."
                        sleep 3               
                        for aa in *.mov; do  ffmpeg -i "$aa" -codec copy "${aa%.mov}.mp4"> /dev/null 2>&1; done
                        encov=mp4
                        varo=1
                fi;
        elif [ "$rpp" = "9" ]                                     #mov en avi
            then
                if [ ! -e *.mov ]
                    then
                        echo "conversion not possible make sure that the source files are in the current folder" 
                        sleep 5 
                        varo=0
                else
                    echo "conversion in progress ..."
                    sleep 3
                    for bb in *.mov; do ffmpeg -i "$bb" -codec copy "${bb%.mov}.avi"> /dev/null 2>&1; done
                    encov=avi
                    varo=1
                fi;
        elif [ "$rpp" = "10" ]                                     #avi en mkv
            then
                if [ ! -e *.avi ]
                    then
                        echo "conversion not possible make sure that the source files are in the current folder" 
                        sleep 5 
                        varo=0
                else
                        echo "conversion in progress ..."
                        sleep 3
                        for cc in *.avi; do ffmpeg -i "$cc" -codec copy "${cc%.avi}.mkv"> /dev/null 2>&1; done
                        encov=mkv
                        varo=1
                fi;
        elif [ "$rpp" = "11" ]                                     #avi en mp4
            then
                if [ ! -e *.avi ]
                    then
                        echo "conversion not possible make sure that the source files are in the current folder" 
                        sleep 5 
                        varo=0
                else
                    echo "conversion in progress ..."
                    sleep 3
                    for dd in *.avi; do ffmpeg -i "$dd" -codec copy "${dd%.avi}.mp4"> /dev/null 2>&1; done
                    encov=mp4
                    varo=1
                fi;
        elif [ "$rpp" = "12" ]                                     #avi en mov
            then
                if [ ! -e *.avi ]
                    then
                        echo "conversion not possible make sure that the source files are in the current folder" 
                        sleep 5 
                        varo=0
                else
                        echo "conversion in progress ..."
                        sleep 3
                        for ee in *.avi; do ffmpeg -i "$ee" -codec copy "${ee%.avi}.mov"> /dev/null 2>&1; done
                        encov=mov
                        varo=1
                fi;
        elif [ "$rpp" = "13" ]                                     #webm en mp4
            then
                if [ ! -e *.webm ]
                    then
                        echo "conversion not possible make sure that the source files are in the current folder" 
                        sleep 5 
                        varo=0
                else
                        echo "conversion in progress ..."
                        sleep 3
                        for ff in *.webm; do ffmpeg -i "$ff" -c copy "${ff%.webm}.mp4"> /dev/null 2>&1; done
                        encov=mp4
                        varo=1    
                fi;
        elif [ "$rpp" = "14" ]                                     #HEVC to mp4
            then
                if [ ! -e *.webm ]
                    then
                        echo "conversion not possible make sure that the source files are in the current folder" 
                        sleep 5 
                        varo=0
                else
                        echo "conversion in progress ..."
                        sleep 3
                        for kkk in *.hevc; do ffmpeg -i "$kkk" -c copy "${kkk%.hevc}.mp4"> /dev/null 2>&1; done
                        encov=mp4
                        varo=1
                fi;
        else
            zenity --error --text="Please enter a number between 1 and 14"
            varo=0
        fi;
    done
    clear
    echo -e "\nYour files have been re-encoded in $encov in your current folder\n"
    sleep 2
    }

    function convertisso-audio {
    clear
    echo -e "\nCe programme va convertire vos fichiers audio dans le format souhaiter, dans votre dossier courant"
    var=0
while [ $var = 0 ];do
    echo -e "\n"
    echo ' ╔════╦═════════════╦═════╦═════════════╦════╦═════════════╦═════╦═════════════╗'
    echo ' ║ 1  ║ mp3 en wav  ║ 7   ║ wav en aac  ║ 13 ║ ac3 en wav  ║ 19  ║ aac en ogg  ║'
    echo ' ╠════╬═════════════╬═════╬═════════════╬════╬═════════════╬═════╬═════════════╣'
    echo ' ║ 2  ║ mp3 en ogg  ║ 8   ║ wav en ac   ║ 14 ║ ac3 en aac  ║ 20  ║ aac en mp3  ║'
    echo ' ╠════╬═════════════╬═════╬═════════════╬════╬═════════════╬═════╬═════════════╣'
    echo ' ║ 3  ║ mp3 en aac  ║  9  ║ ogg en mp3  ║ 15 ║ ac3 en ogg  ║ 21  ║ flac en mp3 ║'
    echo ' ╠════╬═════════════╬═════╬═════════════╠════╬═════════════╬═════╬═════════════╣'
    echo ' ║ 4  ║ mp3 en ac3  ║ 10  ║ ogg en wav  ║ 16 ║ aac en wav  ║ 22  ║ flac en wav ║'
    echo ' ╠════╬═════════════╬═════╬═════════════╬════╬═════════════╬═════╬═════════════╣'
    echo ' ║ 5  ║ wav en mp3  ║ 11  ║ ogg en aac  ║ 17 ║ aac en wav  ║ 23  ║ flac en ogg ║'
    echo ' ╠════╬═════════════╬═════╬═════════════╬════╬═════════════╬═════╬═════════════╣'
    echo ' ║ 6  ║ wav en ogg  ║ 12  ║ ogg en ac3  ║ 18 ║ aac en ac3  ║ 24  ║ flac en ac3 ║'
    echo ' ╚════╩═════════════╩═════╩═════════════╩════╩═════════════╩═════╩═════════════╝'
    
    echo -e "\n"
    read -p "Choose the corresponding number.   : " rp # demande a l'utilisateur dans quelle format il veut convertir ses fichiers
        if [ "$rp" = "1" ]                             
            then
                if [ ! -e *.mp3 ]
                    then
                        echo "conversion not possible make sure that the source files are in the current folder" 
                        sleep 5
                        var=0
                else
                FILE=`zenity --file-selection --multiple --title="Select one or more files mp3 file"`
                    if [ "$?" = "0" ]                    
                        then
                        echo "conversion in progress ..."
                        sleep 3
                        for a in $FILE *.mp3; do ffmpeg -i "$a" "${a%.mp3}.wav"> /dev/null 2>&1; done
                        enco=wav
                        var=1
                    elif [ "$?" = "1" ]                           
                        then
                        zenity --error --text="No files selected"
                    else 
                        zenity --error --text="An unexpected error has occurred"
                    fi;
                fi;
        elif [ "$rp" = "2" ]                             
            then
                if [ ! -e *.mp3 ]
                    then
                        echo "conversion not possible make sure that the source files are in the current folder" 
                        sleep 5 
                        var=0
                else
                FILE=`zenity --file-selection --multiple --title="Select one or more files mp3 file"`
                    if [ "$?" = "0" ]                              
                        then
                        echo "conversion in progress ..."
                        sleep 3
                        sleep 2
                        for b in $FILE *.mp3; do ffmpeg -i "${b}" -acodec libvorbis "${b/%mp3}.ogg"> /dev/null 2>&1; done #convertis les fichiers MP3 en OGG
                        enco=ogg
                        var=1
                    elif [ "$?" = "1" ]                           
                        then
                        zenity --error --text="No files selected"
                    else 
                        zenity --error --text="An unexpected error has occurred"
                    fi;
                fi; 
        elif [ "$rp" = "3" ]                                   #mp3 en aac
            then
                if [ ! -e *.mp3 ]
                    then
                        echo "conversion not possible make sure that the source files are in the current folder" 
                        sleep 5 
                        var=0
                else
                FILE=`zenity --file-selection --multiple --title="Select one or more files mp3 file"`
                    if [ "$?" = "0" ]                                  
                        then
                        echo "conversion in progress ..."
                        sleep 3
                        sleep 2
                        for c in $FILE *.mp3; do ffmpeg -i "$c" -acodec libfaac "${c%.mp3}.aac"> /dev/null 2>&1; done
                        enco=aac
                        var=1
                    elif [ "$?" = "1" ]                           
                        then
                        zenity --error --text="No files selected"
                    else 
                        zenity --error --text="An unexpected error has occurred"
                    fi;
                fi;
        elif [ "$rp" = "4" ]                                   #mp3 en ac3
            then
                if [ ! -e *.mp3 ]
                    then
                        echo "conversion not possible make sure that the source files are in the current folder" 
                        sleep 5 
                        var=0
                else
                FILE=`zenity --file-selection --multiple --title="Select one or more files mp3 file"`
                    if [ "$?" = "0" ]                              
                        then
                        echo "conversion in progress ..."
                        sleep 3
                        sleep 2
                        for m in $FILE *.mp3; do ffmpeg -i "$m" -acodec ac3 "${m%.mp3}.ac3"> /dev/null 2>&1; done 
                        enco=ac3
                        var=1
                    elif [ "$?" = "1" ]                           
                        then
                        zenity --error --text="No files selected"
                    else 
                        zenity --error --text="An unexpected error has occurred"
                    fi;
                fi;
        elif [ "$rp" = "5" ]                                   #wav en mp3
            then
                if [ ! -e *.wav ]
                    then
                        echo "conversion not possible make sure that the source files are in the current folder" 
                        sleep 5 
                        var=0
                else
                FILE=`zenity --file-selection --multiple --title="Select one or more files wav file"`
                    if [ "$?" = "0" ]                                     
                        then
                        echo "conversion in progress ..."
                        sleep 3
                        sleep 2
                        for d in $FILE *.wav; do ffmpeg -i "$d" -f mp3 "${d%.waw}.mp3"> /dev/null 2>&1; done
                        enco=mp3
                        var=1
                    elif [ "$?" = "1" ]                           
                    then
                        zenity --error --text="No files selected"
                    else 
                        zenity --error --text="An unexpected error has occurred"
                    fi;
                fi;
        elif [ "$rp" = "6" ]                                       #wav en ogg
            then
                if [ ! -e *.wav ]
                    then
                        echo "conversion not possible make sure that the source files are in the current folder" 
                        sleep 5 
                        var=0
                else
                FILE=`zenity --file-selection --multiple --title="Select one or more files wav file"`
                    if [ "$?" = "0" ]                                     
                        then
                        echo "conversion in progress ..."
                        sleep 3
                        sleep 2
                        for h in $FILE *.wav; do ffmpeg -i "$h" -acodec libvorbis "${h%.waw}.ogg"> /dev/null 2>&1; done 
                        enco=ogg
                        var=1
                    elif [ "$?" = "1" ]                           
                    then
                        zenity --error --text="No files selected"
                    else 
                        zenity --error --text="An unexpected error has occurred"
                    fi;
                fi;
        elif [ "$rp" = "7" ]                                    #wav en aac
            then
                if [ ! -e *.wav ]
                    then
                        echo "conversion not possible make sure that the source files are in the current folder" 
                        sleep 5 
                        var=0
                else
                FILE=`zenity --file-selection --multiple --title="Select one or more files wav file"`
                    if [ "$?" = "0" ]                                     
                        then
                        echo "conversion in progress ..."
                        sleep 3
                        sleep 2
                        for i in $FILE *.wav; do ffmpeg -i "$i" -acodec libfaac "${i%.waw}.aac"> /dev/null 2>&1; done 
                        enco=aac
                        var=1
                    elif [ "$?" = "1" ]                           
                    then
                        zenity --error --text="No files selected"
                    else 
                        zenity --error --text="An unexpected error has occurred"
                    fi;
                fi;
        elif [ "$rp" = "8" ]                                   #wav en ac3
            then
                if [ ! -e *.wav ]
                    then
                        echo "conversion not possible make sure that the source files are in the current folder" 
                        sleep 5 
                        var=0
                else
                FILE=`zenity --file-selection --multiple --title="Select one or more files wav file"`
                    if [ "$?" = "0" ]                                     
                        then
                        echo "conversion in progress ..."
                        sleep 3
                        sleep 2
                        for j in $FILE *.wav; do ffmpeg -i "$j" -acodec libmp3lame "${j%.waw}.ac3"> /dev/null 2>&1; done 
                        enco=ac3
                        var=1
                    elif [ "$?" = "1" ]                           
                    then
                        zenity --error --text="No files selected"
                    else 
                        zenity --error --text="An unexpected error has occurred"
                    fi;
                fi;
        elif [ "$rp" = "9" ]                                   #ogg en mp3
            then
                if [ ! -e *.ogg ]
                    then
                        echo "conversion not possible make sure that the source files are in the current folder" 
                        sleep 5 
                        var=0
                else
                FILE=`zenity --file-selection --multiple --title="Select one or more files ogg file"`
                    if [ "$?" = "0" ]                                     
                        then
                        echo "conversion in progress ..."
                        sleep 3
                        sleep 2
                        for g in $FILE *.ogg; do ffmpeg -i "$g" -acodec libmp3lame "${g%.ogg}.mp3"> /dev/null 2>&1; done #convertis les fichiers OGG en MP3
                        enco=mp3
                        var=1
                    elif [ "$?" = "1" ]                           
                    then
                        zenity --error --text="No files selected"
                    else 
                        zenity --error --text="An unexpected error has occurred"
                    fi;
                fi;
        elif [ "$rp" = "10" ]                                   #ogg en wav
            then
                if [ ! -e *.ogg ]
                    then
                        echo "conversion not possible make sure that the source files are in the current folder" 
                        sleep 5 
                        var=0
                else
                FILE=`zenity --file-selection --multiple --title="Select one or more files ogg file"`
                    if [ "$?" = "0" ]                                     
                        then
                        echo "conversion in progress ..."
                        sleep 3
                        sleep 2
                        for k in $FILE *.ogg; do ffmpeg -i "$k" "${k%.ogg}.wav"> /dev/null 2>&1; done 
                        enco=wav
                        var=1
                    elif [ "$?" = "1" ]                           
                    then
                        zenity --error --text="No files selected"
                    else 
                        zenity --error --text="An unexpected error has occurred"
                    fi;
                fi;
        elif [ "$rp" = "11" ]                                   #ogg en aac
            then
                if [ ! -e *.ogg ]
                    then
                        echo "conversion not possible make sure that the source files are in the current folder" 
                        sleep 5 
                        var=0
                else
                FILE=`zenity --file-selection --multiple --title="Select one or more files ogg file"`
                    if [ "$?" = "0" ]                                     
                        then
                        echo "conversion in progress ..."
                        sleep 3
                        sleep 2
                        for l in $FILE *.ogg; do ffmpeg -i "$l" -acodec libfaac "${l%.ogg}.aac"> /dev/null 2>&1; done 
                        enco=aac
                        var=1
                    elif [ "$?" = "1" ]                           
                    then
                        zenity --error --text="No files selected"
                    else 
                        zenity --error --text="An unexpected error has occurred"
                    fi;
                fi;
        elif [ "$rp" = "12" ]                                   #ogg en ac3
            then
                if [ ! -e *.ogg ]
                    then
                        echo "conversion not possible make sure that the source files are in the current folder" 
                        sleep 5 
                        var=0
                else
                FILE=`zenity --file-selection --multiple --title="Select one or more files ogg file"`
                    if [ "$?" = "0" ]                                     
                        then
                        echo "conversion in progress ..."
                        sleep 3
                        sleep 2
                        for m in $FILE *.ogg; do ffmpeg -i "$m" -acodec ac3 "${m%.ogg}.ac3"> /dev/null 2>&1; done 
                        enco=ac3
                        var=1
                    elif [ "$?" = "1" ]                           
                    then
                        zenity --error --text="No files selected"
                    else 
                        zenity --error --text="An unexpected error has occurred"
                    fi;
                fi;
        elif [ "$rp" = "13" ]                                   #ac3 en wav
            then
                if [ ! -e *.ac3 ]
                    then
                        echo "conversion not possible make sure that the source files are in the current folder" 
                        sleep 5 
                        var=0
                else
                FILE=`zenity --file-selection --multiple --title="Select one or more files ac3 file"`
                    if [ "$?" = "0" ]                                     
                        then
                        echo "conversion in progress ..."
                        sleep 3
                        sleep 2
                        for n in $FILE *.ac3; do ffmpeg -i "$n"  "${n%.ac3}.wav"> /dev/null 2>&1; done
                        enco=wav
                        var=1
                    elif [ "$?" = "1" ]                           
                    then
                        zenity --error --text="No files selected"
                    else 
                        zenity --error --text="An unexpected error has occurred"
                    fi;
                fi;
        elif [ "$rp" = "14" ]                                   #ac3 en aac
            then
                if [ ! -e *.ac3 ]
                    then
                        echo "conversion not possible make sure that the source files are in the current folder" 
                        sleep 5 
                        var=0
                else
                FILE=`zenity --file-selection --multiple --title="Select one or more files ac3 file"`
                    if [ "$?" = "0" ]                                     
                        then
                        echo "conversion in progress ..."
                        sleep 3
                        sleep 2
                        for o in $FILE *.ac3; do ffmpeg -i "$o" -acodec libfaac "${o%.ac3}.aac"> /dev/null 2>&1; done
                        enco=aac
                        var=1
                    elif [ "$?" = "1" ]                           
                    then
                        zenity --error --text="No files selected"
                    else 
                        zenity --error --text="An unexpected error has occurred"
                    fi;
                fi;
        elif [ "$rp" = "15" ]                                   #ac3 en ogg
            then
                if [ ! -e *.ac3 ]
                    then
                        echo "conversion not possible make sure that the source files are in the current folder" 
                        sleep 5 
                        var=0
                else
                FILE=`zenity --file-selection --multiple --title="Select one or more files ac3 file"`
                    if [ "$?" = "0" ]                                     
                        then
                        echo "conversion in progress ..."
                        sleep 3
                        sleep 2
                        for p in $FILE *.ac3; do ffmpeg -i "$p" -acodec libvorbis "${p%.ac3}.ogg"> /dev/null 2>&1; done
                        enco=ogg
                        var=1
                    elif [ "$?" = "1" ]                           
                    then
                        zenity --error --text="No files selected"
                    else 
                        zenity --error --text="An unexpected error has occurred"
                    fi;
                fi;
        elif [ "$rp" = "16" ]                                   #ac3 en mp3
            then
                if [ ! -e *.ac3 ]
                    then
                        echo "conversion not possible make sure that the source files are in the current folder" 
                        sleep 5 
                        var=0
                else
                FILE=`zenity --file-selection --multiple --title="Select one or more files ac3 file"`
                    if [ "$?" = "0" ]                                     
                        then
                        echo "conversion in progress ..."
                        sleep 3
                        sleep 2
                        for f in $FILE *.ac3; do ffmpeg -i "$f" -acodec libmp3lame "${f%.ac3}.mp3"> /dev/null 2>&1; done
                        enco=mp3
                        var=1
                    elif [ "$?" = "1" ]                           
                    then
                        zenity --error --text="No files selected"
                    else 
                        zenity --error --text="An unexpected error has occurred"
                    fi;
                fi;
        elif [ "$rp" = "17" ]                                   #aac en wav
            then
                if [ ! -e *.aac ]
                    then
                        echo "conversion not possible make sure that the source files are in the current folder" 
                        sleep 5 
                        var=0
                else
                FILE=`zenity --file-selection --multiple --title="Select one or more files aac file"`
                    if [ "$?" = "0" ]                                     
                        then
                        echo "conversion in progress ..."
                        sleep 3
                        sleep 2
                        for q in $FILE *.aac; do ffmpeg -i "$q" "${q%.aac}.wav"> /dev/null 2>&1 ; done
                        enco=wav
                    elif [ "$?" = "1" ]                           
                        then
                        zenity --error --text="No files selected"
                    else 
                        zenity --error --text="An unexpected error has occurred"
                    fi;
                fi;
            var=1
        elif [ "$rp" = "18" ]                                   #aac en ac3
            then
                if [ ! -e *.aac ]
                    then
                        echo "conversion not possible make sure that the source files are in the current folder" 
                        sleep 5 
                        var=0
                else
                FILE=`zenity --file-selection --multiple --title="Select one or more files aac file"`
                    if [ "$?" = "0" ]                                     
                        then
                        echo "conversion in progress ..."
                        sleep 3
                        sleep 2
                        for r in $FILE *.aac; do ffmpeg -i "$r" -acodec ac3 "${r%.aac}.ac3"> /dev/null 2>&1; done
                        enco=ac3
                    elif [ "$?" = "1" ]                           
                        then
                        zenity --error --text="No files selected"
                    else 
                        zenity --error --text="An unexpected error has occurred"
                    fi;
                        var=1
                fi;
        elif [ "$rp" = "19" ]                                  #aac en ogg
            then
                if [ ! -e *.aac ]
                    then
                        echo "conversion not possible make sure that the source files are in the current folder" 
                        sleep 5 
                        var=0
                else
                FILE=`zenity --file-selection --multiple --title="Select one or more files aac file"`
                    if [ "$?" = "0" ]                                     
                        then
                        echo "conversion in progress ..."
                        sleep 3
                        sleep 2
                        for s in $FILE; do ffmpeg -i "$s" -acodec libvorbis "${s%.aac}.ogg"> /dev/null 2>&1; done
                        enco=ogg
                    elif [ "$?" = "1" ]                           
                        then
                        zenity --error --text="No files selected"
                    else 
                        zenity --error --text="An unexpected error has occurred"
                    fi;
                        var=1
                fi;
        elif [ "$rp" = "20" ]                                   #aac en mp3
            then
                if [ ! -e *.aac ]
                    then
                        echo "conversion not possible make sure that the source files are in the current folder" 
                        sleep 5 
                        var=0
                else
                FILE=`zenity --file-selection --multiple --title="Select one or more files aac file"`
                    if [ "$?" = "0" ]                                     
                        then
                        echo "conversion in progress ..."
                        sleep 3
                        sleep 2
                        for e in $FILE *.aac; do ffmpeg -i "$e" -acodec libmp3lame "${e%.aac}.mp3"> /dev/null 2>&1; done
                        enco=mp3
                    elif [ "$?" = "1" ]                           
                        then
                        zenity --error --text="No files selected"
                    else 
                        zenity --error --text="An unexpected error has occurred"
                    fi;
                        var=1
                fi;
        elif [ "$rp" = "21" ]                                   #flac en mp3
            then
                if [ ! -e *.flac ]
                    then
                        echo "conversion not possible make sure that the source files are in the current folder" 
                        sleep 5 
                        var=0
                else
                FILE=`zenity --file-selection --multiple --title="Select one or more files flac file"`
                    if [ "$?" = "0" ]                                     
                        then
                        echo "conversion in progress ..."
                        sleep 3
                        sleep 2
                        for rr in $FILE *.flac; do ffmpeg -i "$rr" -acodec libmp3lame "${rr%.flac}.mp3"> /dev/null 2>&1; done
                        enco=mp3
                        var=1
                    elif [ "$?" = "1" ]                           
                        then
                        zenity --error --text="No files selected"
                    else 
                        zenity --error --text="An unexpected error has occurred"
                    fi;

                fi;
        elif [ "$rp" = "22" ]                                   #flac en wav
            then
                if [ ! -e *.flac ]
                    then
                        echo "conversion not possible make sure that the source files are in the current folder" 
                        sleep 5 
                        var=0
                else
                FILE=`zenity --file-selection --multiple --title="Select one or more files flac file"`
                    if [ "$?" = "0" ]                                     
                        then
                        echo "conversion in progress ..."
                        sleep 3
                        sleep 2
                        for ss in $FILE *.flac; do ffmpeg -i "$ss" "${ss%.flac}.wav"> /dev/null 2>&1; done
                        enco=wav
                        var=1
                    elif [ "$?" = "1" ]                           
                        then
                        zenity --error --text="No files selected"
                    else 
                        zenity --error --text="An unexpected error has occurred"
                    fi;

                fi;
        elif [ "$rp" = "23" ]                                   #flac en ogg
            then
                if [ ! -e *.flac ]
                    then
                        echo "conversion not possible make sure that the source files are in the current folder" 
                        sleep 5 
                        var=0
                else
                FILE=`zenity --file-selection --multiple --title="Select one or more files flac file"`
                    if [ "$?" = "0" ]                                     
                        then
                        echo "conversion in progress ..."
                        sleep 3
                        sleep 2
                        for tt in $FILE *.flac; do ffmpeg -i "$tt" -acodec libvorbis "${tt%.flac}.ogg"> /dev/null 2>&1; done
                        enco=ogg 
                        var=1
                    elif [ "$?" = "1" ]                           
                        then
                        zenity --error --text="No files selected"
                    else 
                        zenity --error --text="An unexpected error has occurred"
                    fi;

                fi;
        elif [ "$rp" = "24" ]                                   #flac en ac3
            then
                if [ ! -e *.flac ]
                    then
                        echo "conversion not possible make sure that the source files are in the current folder" 
                        sleep 5 
                        var=0
                else
                FILE=`zenity --file-selection --multiple --title="Select one or more files flac file"`
                    if [ "$?" = "0" ]                                     
                        then
                        echo "conversion in progress ..."
                        sleep 3
                        sleep 2
                        for tt in $FILE *.flac; do ffmpeg -i "$tt" -acodec ac3 "${tt%.flac}.ac3"> /dev/null 2>&1; done
                        enco=ac3 
                        var=1
                    elif [ "$?" = "1" ]                           
                        then
                        zenity --error --text="No files selected"
                    else
                        zenity --error --text="An unexpected error has occurred"
                    fi;

                fi;             
        else
            zenity --error --text="Please enter a number between 1 and 24"
            var=0
        fi;
done
echo -e "\nYour files have been re-encoded in $enco in your current foldert\n"
sleep 2
}

function convertisso-image {
clear
vor=0

    echo ' ╔════╦══════════════╦════╦══════════════╗'
    echo ' ║ 1  ║  png to jpg  ║ 8  ║ pdf to tiff  ║'
    echo ' ╠════╬══════════════╬════╬══════════════╣'
    echo ' ║ 2  ║  jpg to png  ║ 9  ║  pdf to jpg  ║'
    echo ' ╠════╬══════════════╬════╬══════════════╣'
    echo ' ║ 3  ║  tiff to png ║ 10 ║  pdf to png  ║'
    echo ' ╠════╬══════════════╬════╬══════════════╣'
    echo ' ║ 4  ║  tiff to jpg ║ 11 ║ svg to tiff  ║'
    echo ' ╠════╬══════════════╬════╬══════════════╣'
    echo ' ║ 5  ║  tiff to BMP ║ 12 ║  svg to png  ║'
    echo ' ╠════╬══════════════╬════╬══════════════╣'
    echo ' ║ 6  ║  tiff to pdf ║ 13 ║  svg to pdf  ║'
    echo ' ╠════╬══════════════╬════╬══════════════╣'
    echo ' ║ 7  ║  tiff to gif ║ 14 ║  heic to jpg ║'
    echo ' ╚════╩══════════════╩════╩══════════════╝'
    read -p "Choose the corresponding number.   : " rrrrp # demande a l'utilisateur dans quelle format il veut convertir ses fichiers
while [ $vor = 0 ];do
    if [ "$rrrrp" = "1" ]                                      #png en jpg
            then
                if [ ! -e *.png ]
                    then
                        echo "conversion not possible make sure that the source files are in the current folder" 
                        sleep 5 
                        var=0
                else
                        echo "conversion in progress ..."
                        sleep 3
                        sleep 2
                        for uu in *.png; do  convert "$uu"  "${uu%.png}.jpg"; done
                        encov=jpg 
                        vor=1
                fi;
    elif [ "$rrrrp" = "2" ]                                    #jpg en png
            then
                if [ ! -e *.jpg ]
                    then
                        echo "conversion not possible make sure that the source files are in the current folder" 
                        sleep 5 
                        var=0
                else
                        echo "conversion in progress ..."
                        sleep 3
                        sleep 2
                        for vv in *.jpg; do  convert "$vv"  "${vv%.jpg}.png"; done
                        encov=png 
                        vor=1
                fi;
    elif [ "$rrrrp" = "3" ]                                    #tiff en png
            then
                if [ ! -e *.tiff ]
                    then
                        echo "conversion not possible make sure that the source files are in the current folder" 
                        sleep 5 
                        vor=0
                else
                        echo "conversion in progress ..."
                        sleep 3
                        sleep 2
                        for ww in *.tiff; do  convert "$ww"  "${ww%.tiff}.png"; done
                        encov=png 
                        vor=1
                fi;
    elif [ "$rrrrp" = "4" ]                                    #tiff en jpg
            then
                if [ ! -e *.tiff ]
                    then
                        echo "conversion not possible make sure that the source files are in the current folder" 
                        sleep 5 
                        vor=0
                else
                        echo "conversion in progress ..."
                        sleep 3
                        sleep 2
                        for yy in *.tiff; do  convert "$yy"  "${yy%.tiff}.jpg"; done
                        encov=jpg
                        vor=1
                fi;
        elif [ "$rrrrp" = "5" ]                                #tiff en BMP
            then
                if [ ! -e *.tiff ]
                    then
                        echo "conversion not possible make sure that the source files are in the current folder" 
                        sleep 5 
                        vor=0
                else
                        echo "conversion in progress ..."
                        sleep 3
                        sleep 2
                        for zz in *.tiff; do  convert "$zz"  "${zz%.tiff}.BMP"; done
                        encov=BMP 
                        vor=1    
                fi;
        elif [ "$rrrrp" = "6" ]                                #tiff en pdf #
            then
                if [ ! -e *.tiff ]
                    then
                        echo "conversion not possible make sure that the source files are in the current folder" 
                        sleep 5 
                        vor=0
                else
                        echo "conversion in progress ..."
                        sleep 3
                        sleep 2
                        for aaa in *.tiff; do  tiff2pdf -o "${aaa%.tiff}.pdf" "$aaa"; done
                        encov=pdf 
                        vor=1
                fi;
        elif [ "$rrrrp" = "7" ]                                #tiff en gif
            then
                if [ ! -e *.tiff ]
                    then
                        echo "conversion not possible make sure that the source files are in the current folder" 
                        sleep 5 
                        vor=0
                else
                        echo "conversion in progress ..."
                        sleep 3
                        sleep 2
                        for bbb in *.tiff; do  convert "$bbb"  "${bbb%.tiff}.gif"; done
                        encov=gif 
                        vor=1
                fi;
        elif [ "$rrrrp" = "8" ]                                #pdf en tiff
            then
                if [ ! -e *.pdf ]
                    then
                        echo "conversion not possible make sure that the source files are in the current folder" 
                        sleep 5 
                        vor=0
                else
                        echo "conversion in progress ..."
                        sleep 3
                        sleep 2
                        for eee in *.pdf; do  convert "$eee"  "${eee%.pdf}.tiff"; done
                        encov=tiff 
                        vor=1
                fi;
        elif [ "$rrrrp" = "9" ]                                #pdf en jpg
            then
                if [ ! -e *.pdf ]
                    then
                        echo "conversion not possible make sure that the source files are in the current folder" 
                        sleep 5 
                        vor=0
                else
                        echo "conversion in progress ..."
                        sleep 3
                        sleep 2
                        for fff in *.pdf; do  convert "$fff"  "${fff%.pdf}.jpg"; done
                        encov=jpg 
                        vor=1
                fi;
        elif [ "$rrrrp" = "10" ]                                #pdf en png
            then
                if [ ! -e *.pdf ]
                    then
                        echo "conversion not possible make sure that the source files are in the current folder" 
                        sleep 5 
                        vor=0
                else
                        echo "conversion in progress ..."
                        sleep 3
                        sleep 2
                        for ggg in *.pdf; do  convert "$ggg"  "${ggg%.pdf}.png"; done
                        encov=png 
                        vor=1
                fi;
        elif [ "$rrrrp" = "11" ]                                #svg en tiff
            then
                if [ ! -e *.svg ]
                    then
                        echo "conversion not possible make sure that the source files are in the current folder" 
                        sleep 5 
                        vor=0
                else
                        echo "conversion in progress ..."
                        sleep 3
                        sleep 2
                        for hhh in *.svg; do  convert "$hhh"  "${hhh%.svg}.tiff"; done
                        encov=tiff 
                        vor=1
                fi;
        elif [ "$rrrrp" = "12" ]                                #svg en png
            then
                if [ ! -e *.svg ]
                    then
                        echo "conversion not possible make sure that the source files are in the current folder" 
                        sleep 5 
                        vor=0
                else
                        echo "conversion in progress ..."
                        sleep 3
                        sleep 2
                        for hhh in *.svg; do  convert "$hhh"  "${hhh%.svg}.png"; done
                        encov=png 
                        vor=1
                fi;
        elif [ "$rrrrp" = "13" ]                                #svg en pdf
            then
                if [ ! -e *.svg ]
                    then
                        echo "conversion not possible make sure that the source files are in the current folder" 
                        sleep 5 
                        vor=0
                else
                        echo "conversion in progress ..."
                        sleep 3
                        sleep 2
                        for hhh in *.svg; do  rsvg-convert -f pdf -o "${hhh%.svg}.pdf" "$hhh" ; done
                        encov=pdf 
                        vor=1
                fi;
        elif [ "$rrrrp" = "14" ]                               
            then
                if [ ! -e *.heic ]
                    then
                        echo "conversion not possible make sure that the source files are in the current folder" 
                        sleep 5 
                        vor=0
                else
                        echo "conversion in progress ..."
                        sleep 3
                        for ggg in *.heic; do  heif-convert "$ggg" "${ggg%.heic}.jpg" ; done
                        encov=jpg
                        sleep 2
                        vor=0
                fi;
        else
        zenity --error --text="Please enter a number between  1 and 14"
        vor=0
    fi;
done
echo -e "\nYour files have been re-encoded in $encov in your current folder\n"
sleep 2

}

#ffmpeg -i infile.mp4 -i infile.srt -c copy -c:s mov_text outfile.mp4


ver=0
clear
convertisso
sleep 3

NEWT_COLORS='
  window=,red
  border=white,red
  textbox=white,red
  button=black,white
' \
TO_RUN=$(whiptail --title "Convertisso menu" --menu "Choose an option" 30 80 10 \
"1" "Convert audio file" \
"2" "Convert video file" \
"3" "Convert Video subtitle" \
"4" "Convert image (Beta)" \
"5" "Download video" \
"6" "EXIT" 3>&1 1>&2 2>&3)

echo $TO_RUN

        if [ "$TO_RUN" = "1" ]                                     
            then
                convertisso-audio
        elif [ "$TO_RUN" = "2" ]                                 
            then 
                convertisso-video
        elif [ "$TO_RUN" = "3" ]                                 
            then 
                convertisso-download-video
        elif [ "$TO_RUN" = "4" ]                                 
            then 
                convertisso-subtitle
        elif [ "$TO_RUN" = "5" ]                                 
            then 
                convertisso-image
        elif [ "$TO_RUN" = "6" ]                                 
            then 
                exit
        else
        zenity --error --text="Please enter a number between  1 and 6"
                varro=0
        fi;
done