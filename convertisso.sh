#!/bin/bash
#---[Metadata]--------------------------------------------------------------#
#  Filename ~ convertisso.sh               [Created: 2022-10-2 | 8:30 PM]  #
#                                          [Update: 2022-10-29 | 9:30 AM]   #
#---[Author of this file]---------------------------------------------------#
#  Jonas Petitpierre ~  @jonas52 -> https://github.com/jonas52
                                                       #
function convertisso {
echo -e "\e[33m  .d8888b.                                              888    d8b                             \e[0m"
echo -e "\e[33m d88P  Y88b                                             888    Y8P                             \e[0m"
echo -e "\e[33m 888    888                                             888                                    \e[0m"
echo -e "\e[33m 888         .d88b.  88888b.  888  888  .d88b.  888d888 888888 888 .d8888b  .d8888b   .d88b.   \e[0m"
echo -e "\e[33m 888        d88°°88b 888 °88b 888  888 d8P  Y8b 888P°   888    888 88K      88K      d88°°88b  \e[0m"
echo -e "\e[33m 888    888 888  888 888  888 Y88  88P 88888888 888     888    888 °Y8888b. °Y8888b. 888  888  \e[0m"
echo -e "\e[33m 88b  d88P  Y88..88P 888  888  Y8bd8P  Y8b.     888     Y88b.  888      X88      X88 Y88..88P  \e[0m"
echo -e "\e[33m °Y8888P°   °Y88P°   888  888   Y88P   °Y8888  888      °Y888 888  88888P° °88888P°   °Y88P°   \e[0m"                                                    
echo -e "\e[33m                                                        +-+ +-+ +-+ +-+ +-+ +-+ +-+ +-+ +-+\e[0m" 
echo -e "\e[33m                                                        |b| |y| |J| |o| |n| |a| |s| |5| |2|\e[0m" 
echo -e "\e[33m                                                        +-+ +-+ +-+ +-+ +-+ +-+ +-+ +-+ +-+\e[0m" 
}


clear
varro=0
Arch=/etc/pacman.conf
Debian=/etc/apt/sources.list
Fedora=/etc/dnf/dnf.conf


function convertisso-dectection-os {   
clear
convertisso
sleep 2
clear
echo -e "Instalation de tous les packets nécésaires pour exécuter script\n"
sleep 2
clear                                                                     #installation des depandance néssecaire pour executer le script 
    if [ -f "$Debian" ]; then
        echo "Installation de libsox-fmt-all ..."
        clear
        sudo apt-get install libsox-fmt-all -y > /dev/null 2>&1
        clear
        echo "Installation de ffmpeg vorbis-tools ..."
        sudo apt-get install ffmpeg vorbis-tools -y > /dev/null 2>&1
        clear
        echo "Installation de python3-pip ..."
        sudo apt install -pip -y > /dev/null 2>&1
        clear
        echo "Installation de youtube_dl ..."
        sudo pip install --upgrade youtube_dl > /dev/null 2>&1
        clear
        echo "Installation de ImageMagick ..."
        sudo apt install imagemagick -y > /dev/null 2>&1
        clear
        echo "Installation de ghostscript libtiff-tools ..."
        sudo apt-get install ghostscript libtiff-tools -y > /dev/null 2>&1
        clear
        echo "Installation de librsvg2-bins ..."
        sudo apt-get install librsvg2-bin -y > /dev/null 2>&1
        clear
        echo "Installation des mises à jours ..."
        sudo apt-get update -y > /dev/null 2>&1
        sudo apt-get upgrade -y > /dev/null 2>&1
        clear
    elif [ -f "$Arch" ]; then
        echo "Installation de libsox-fmt-all ..."
        sudo pacman -S --noconfirm libsox-fmt-all > /dev/null 2>&1
        clear
        echo "Installation de ffmpeg vorbis-tools ..."
        sudo pacman -S --noconfirm ffmpeg vorbis-tools > /dev/null 2>&1
        clear
        echo "Installation de python3-pip ..."
        sudo pacman -S --noconfirm python3-pip > /dev/null 2>&1
        clear
        echo "Installation de youtube_dl ..."
        sudo pip install -y --upgrade youtube_dl > /dev/null 2>&1
        clear
        echo "Installation de ImageMagick ..."
        sudo pacman -S --noconfirm ImageMagick > /dev/null 2>&1
        clear
        echo "Installation de ghostscript libtiff-tools ..."
        sudo pacman -S --noconfirm ghostscript libtiff-tools > /dev/null 2>&1
        clear
        echo "Installation de librsvg2-bins ..."
        sudo pacman -S --noconfirm librsvg2-bin > /dev/null 2>&1
        clear
        echo "Installation des mises à jours ..."
        sudo pacman -Syu --noconfirm > /dev/null 2>&1
        clear
    elif [ -f "$Fedora" ]; then
        echo "Installation de libsox-fmt-all ..."
        sudo dnf -y install libsox-fmt-all > /dev/null 2>&1
        clear
        echo "Installation de ffmpeg vorbis-tools ..."
        sudo dnf -y install ffmpeg vorbis-tools > /dev/null 2>&1
        clear
        echo "Installation de python3-pip ..."
        sudo dnf -y install python3-pip > /dev/null 2>&1
        clear
        echo "Installation de youtube_dl ..."
        sudo pip install -y --upgrade youtube_dl > /dev/null 2>&1
        clear
        echo "Installation de ImageMagick ..."
        sudo rpm -Uvh ImageMagick-7.1.0-51.x86_64.rpm > /dev/null 2>&1
        clear
        echo "Installation de ghostscript libtiff-tools ..."
        sudo rpm -Uvh ghostscript libtiff-tools > /dev/null 2>&1
        clear
        echo "Installation de librsvg2-bins ..."
        sudo rpm -Uvh librsvg2-bin > /dev/null 2>&1
        clear
        echo "Installation des mises à jours ..."
        dnf -y check-update
        dnf -y upgrade
        clear
    else 
        echo "Votre appareil n'est pas compatible avec ce script"
        sleep 3
        exit
    fi;
}
echo -e "Instalation de tous les packets nécésaires pour exécuter script\n"
sleep 2
convertisso-dectection-os


while [ $varro = 0 ];do

function convertisso-sous-titres-video {
clear
varorr=0
while [ $varorr = 0 ];do

    echo ' ╔════╦═════════════╦════╦════════════╗'
    echo ' ║ 1  ║ vtt en srt  ║ 7  ║ ass en srt ║'
    echo ' ╠════╬═════════════╬════╬════════════╣'
    echo ' ║ 2  ║ vtt en ass  ║ 8  ║ ass en lrc ║'
    echo ' ╠════╬═════════════╬════╬════════════╣'
    echo ' ║ 3  ║ vtt en lrc  ║ 9  ║ ass en vtt ║'
    echo ' ╠════╬═════════════╬════╬════════════╣'
    echo ' ║ 4  ║ srt en vtt  ║ 10 ║ lrc en srt ║'
    echo ' ╠════╬═════════════╬════╬════════════╣'
    echo ' ║ 5  ║ srt en ass  ║ 11 ║ lrc en ass ║'
    echo ' ╠════╬═════════════╬════╬════════════╣'
    echo ' ║ 6  ║ srt en lrc  ║ 12 ║ lrc en vtt ║'
    echo ' ╚════╩═════════════╩════╩════════════╝'

read -p "Choisiser le numéro correspondant pour convertir le fichier   : " rrrpp
        if [ "$rrrpp" = "1" ]                                     #vtt en srt
            then
                echo "Vos fichier sont en cours de conversion ..."
                for gg in *.vtt; do ffmpeg -i "$gg" "${gg%.vtt}.srt" > /dev/null 2>&1; done
                rm -f result.txt
                encov=srt
                varorr=1
        elif [ "$rrrpp" = "2" ]                                    #vtt en ass
            then
                echo "Vos fichier sont en cours de conversion ..."
                for hh in *.vtt; do ffmpeg -i "$hh" "${hh%.vtt}.ass" > /dev/null 2>&1; done
                rm -f result.txt
                encov=ass
                varorr=1
        elif [ "$rrrpp" = "3" ]                                     #vtt en lrc
            then
                echo "Vos fichier sont en cours de conversion ..."
                for ii in *.vtt; do ffmpeg -i "$ii" "${ii%.vtt}.lrc" > /dev/null 2>&1; done
                rm -f result.txt
                encov=lrc
                varorr=1
        elif [ "$rrrpp" = "4" ]                                     #srt en vtt
            then
                echo "Vos fichier sont en cours de conversion ..."
                for jj in *.srt; do ffmpeg -i "$jj" "${jj%.srt}.vtt" > /dev/null 2>&1; done
                rm -f result.txt
                encov=vtt
                varorr=1
        elif [ "$rrrpp" = "5" ]                                     #srt en ass
            then
                echo "Vos fichier sont en cours de conversion ..."
                for kk in *.srt; do ffmpeg -i "$kk" "${kk%.srt}.ass" > /dev/null 2>&1; done
                rm -f result.txt
                encov=ass
                varorr=1
        elif [ "$rrrpp" = "6" ]                                     #srt en lrc
            then
                echo "Vos fichier sont en cours de conversion ..."
                for ll in *.srt; do ffmpeg -i "$ll" "${ll%.srt}.lrc" > /dev/null 2>&1; done
                rm -f result.txt
                encov=lrc
                varorr=1
        elif [ "$rrrpp" = "7" ]                                     #ass en srt
            then
                echo "Vos fichier sont en cours de conversion ..."
                for mm in *.ass; do ffmpeg -i "$mm" "${mm%.ass}.srt" > /dev/null 2>&1; done
                rm -f result.txt
                encov=srt
                varorr=1
        elif [ "$rrrpp" = "8" ]                                     #ass en lrc
            then
                echo "Vos fichier sont en cours de conversion ..."
                for nn in *.ass; do ffmpeg -i "$nn" "${nn%.ass}.lrc" > /dev/null 2>&1; done
                rm -f result.txt
                encov=lrc
                varorr=1
        elif [ "$rrrpp" = "9" ]                                     #ass en vtt
            then
                echo "Vos fichier sont en cours de conversion ..."
                for oo in *.ass; do ffmpeg -i "$oo" "${oo%.ass}.vtt" > /dev/null 2>&1; done
                rm -f result.txt
                encov=vtt
                varorr=1    
        elif [ "$rrrpp" = "10" ]                                     #lrc en srt
            then
                echo "Vos fichier sont en cours de conversion ..."
                for pp in *.lrc; do ffmpeg -i "$pp" "${pp%.lrc}.srt" > /dev/null 2>&1; done
                rm -f result.txt
                encov=srt
                varorr=1           
        elif [ "$rrrpp" = "11" ]                                     #lrc en ass
            then
                echo "Vos fichier sont en cours de conversion ..."
                for qq in *.lrc; do ffmpeg -i "$qq" "${qq%.lrc}.ass" > /dev/null 2>&1; done
                rm -f result.txt
                encov=ass
                varorr=1 
        elif [ "$rrrpp" = "12" ]                                     #lrc en vtt
            then
                echo "Vos fichier sont en cours de conversion ..."
                for rr in *.lrc; do ffmpeg -i "$rr" "${rr%.lrc}.vtt" > /dev/null 2>&1; done
                rm -f result.txt
                encov=vtt
                varorr=1
        else
            echo "Veiller entrer un nombre entre 1 et 12"
            sleep 2
            varorr=0
        fi;
    clear
    echo -e "\nVos fichiers on bien été réencodé en $encov dans votre dossier courant\n"
    sleep 2
done

}
    function convertisso-download-video {
        clear
        varor=0
        read -p "Copier le lien de la vidéo et coller le ici.  ->" down
    echo -e "\n"
    echo ' ╔════╦════════════════════════╦════╦═════════════════════════════════╗'
    echo " ║ 1  ║ vidéo sans sous-titre  ║ 3  ║     seulement l'audio (mp3)     ║"
    echo ' ╠════╬════════════════════════╬════╬═════════════════════════════════╣'
    echo ' ║ 2  ║ vidéo avec sous-tire   ║ 4  ║    seulement les sous-titre     ║'
    echo ' ╚════╩════════════════════════╩════╩═════════════════════════════════╝'
    echo -e "\n"
    while [ $varor = 0 ];do
    read -p "Choisier comment votre vidéo vas être télécharger.   : " rrpp
    if [ "$rrpp" = "1" ]                                     #vidéo sans sous-titre
        then
        echo "Téléchargment en cours (cela peut-prendre plusieurs minutes) ..."
        youtube-dl "$down" 
            while [ $? = "1" ] ;do
                youtube-dl "$down" 
            done
            varor=1
    elif [ "$rrpp" = "2" ]                                     #vidéo avec sous-tire
        then
        #read -p "Dans quel langue voulez-vous avoir les sous-titres?" lang
        echo "Téléchargment en cours (cela peut-prendre plusieurs minutes) ..."
        youtube-dl --write-srt --all-subs "$down"
        while [ $? = "1" ] ;do youtube-dl --write-srt --all-subs "$down"; done
        #--sub-lang "$lang "
        varor=1
    elif [ "$rrpp" = "3" ]                                     #seulement l'audio (mp3)
        then
        echo "Téléchargment en cours (cela peut-prendre plusieurs minutes) ..."
        youtube-dl -x --audio-format mp3 "$down"
        while [ $? = "1" ] ;do youtube-dl -x --audio-format mp3 "$down"; done
        varor=1
        echo "Téléchargment en cours (cela peut-prendre plusieurs minutes) ..."
    elif [ "$rrpp" = "4" ]                                     #eulement les sous-titre  
        then
        youtube-dl --all-subs --skip-download "$down"
        while [ $? = "1" ] ;do youtube-dl --all-subs --skip-download "$down"; done
        varor=1
    else 
        echo "Veiller entrer 1, 2, 3, 4"
        sleep 2
        varor=0
    fi;
    done
    echo "La vidéo que vous avez télécharger, est dans votre dossier courant"
    sleep 2

    }


    function convertisso-video {
    clear
    varo=0
    while [ $varo = 0 ];do
    echo -e "\n"
    echo ' ╔════╦═════════════╦════╦══════════════════════════╗'
    echo ' ║ 1  ║ mkv en avi  ║ 8  ║       mov en mp4         ║'
    echo ' ╠════╬═════════════╬════╬══════════════════════════╣'
    echo ' ║ 2  ║ mkv en mov  ║ 9  ║       mov en avi         ║'
    echo ' ╠════╬═════════════╬════╬══════════════════════════╣'
    echo ' ║ 3  ║ mkv en mp4  ║ 10 ║       avi en mkv         ║'
    echo ' ╠════╬═════════════╬════╬══════════════════════════╣'
    echo ' ║ 4  ║ mp4 en mkv  ║ 11 ║       avi en mp4         ║'
    echo ' ╠════╬═════════════╬════╬══════════════════════════╣'
    echo ' ║ 5  ║ mp4 en mov  ║ 12 ║       avi en mov         ║'
    echo ' ╠════╬═════════════╬════╬══════════════════════════╣'
    echo ' ║ 6  ║ mp4 en avi  ║ 13 ║       webm en mp4        ║'
    echo ' ╠════╬═════════════╬════╬══════════════════════════╣'
    echo ' ║ 7  ║ mov en mkv  ║ 14 ║      NON DISPONIBLE      ║'
    echo ' ╚════╩═════════════╩════╩══════════════════════════╝'
    echo -e "\n"
    read -p "Choisiser le numéro correspondant pour convertir le fichier.   : " rpp # demande a l'utilisateur dans quelle format il veut convertir ses fichiers
        if [ "$rpp" = "1" ]                                     #mkv en avi
        then
            echo "Vos fichier sont en cours de conversion ..."
            for t in *.mkv; do ffmpeg -i "$t" -codec copy "${t%.mkv}.avi"> /dev/null 2>&1; done
            encov=avi
            varo=1
        elif [ "$rpp" = "2" ]                                   #mkv en mov
        then 
            echo "Vos fichier sont en cours de conversion ..."
            for u in *.mkv; do ffmpeg -i "$u" -codec copy "${u%.mkv}.mov"> /dev/null 2>&1; done
            encov=mov
            varo=1                            
        elif [ "$rpp" = "3" ]                                     #mkv en mp4
        then
            echo "Vos fichier sont en cours de conversion ..."
            for v in *.mkv; do ffmpeg -i "$v" -codec copy "${v%.mkv}.mp4"> /dev/null 2>&1; done
            encov=mp4
            varo=1
        elif [ "$rpp" = "4" ]                                     #mp4 en mkv                                     
        then
            echo "Vos fichier sont en cours de conversion ..."
            for w in *.mp4; do ffmpeg -i "$w" -codec copy "${w%.mp4}.mkv"> /dev/null 2>&1; done
            encov=mkv
            varo=1
        elif [ "$rpp" = "5" ]                                     #mp4 en mov                                    
        then
            echo "Vos fichier sont en cours de conversion ..."
            for x in *.mp4; do ffmpeg -i "$x" -codec copy "${x%.mp4}.mov"> /dev/null 2>&1; done
            encov=mov
            varo=1
        elif [ "$rpp" = "6" ]                                     #mp4 en avi
        then
            echo "Vos fichier sont en cours de conversion ..."                                     
            for y in *.mp4; do ffmpeg -i "$y" -codec copy "${y%.mp4}.avi"> /dev/null 2>&1; done
            encov=avi
            varo=1
        elif [ "$rpp" = "7" ]                                     #mov en mkv
        then
            echo "Vos fichier sont en cours de conversion ..."                                    
            for z in *.mov; do ffmpeg -i "$z" -codec copy "${z%.mov}.mkv"> /dev/null 2>&1; done
            varo=1
        elif [ "$rpp" = "8" ]                                     #mov en mp4
        then
            echo "Vos fichier sont en cours de conversion ..."               
            for aa in *.mov; do  ffmpeg -i "$aa" -codec copy "${aa%.mov}.mp4"> /dev/null 2>&1; done
            encov=mp4
            varo=1
        elif [ "$rpp" = "9" ]                                     #mov en avi
        then
            echo "Vos fichier sont en cours de conversion ..."
            for bb in *.mov; do ffmpeg -i "$bb" -codec copy "${bb%.mov}.avi"> /dev/null 2>&1; done
            encov=avi
            varo=1
        elif [ "$rpp" = "10" ]                                     #avi en mkv
        then
            echo "Vos fichier sont en cours de conversion ..."
            for cc in *.avi; do ffmpeg -i "$cc" -codec copy "${cc%.avi}.mkv"> /dev/null 2>&1; done
            encov=mp4
            varo=1
        elif [ "$rpp" = "11" ]                                     #avi en mp4
        then
            echo "Vos fichier sont en cours de conversion ..."
            for dd in *.avi; do ffmpeg -i "$dd" -codec copy "${dd%.avi}.mp4"> /dev/null 2>&1; done
            encov=mp4
            varo=1
        elif [ "$rpp" = "12" ]                                     #avi en mov
        then
            echo "Vos fichier sont en cours de conversion ..."
            for ee in *.avi; do ffmpeg -i "$ee" -codec copy "${ee%.avi}.mov"> /dev/null 2>&1; done
            encov=mov
            varo=1
        elif [ "$rpp" = "13" ]                                     #webm en mp4
        then
            echo "Vos fichier sont en cours de conversion ..."
            for ff in *.webm; do ffmpeg -i "$ff" -c copy "${ff%.webm}.mp4"> /dev/null 2>&1; done
            encov=mp4
            varo=1    
        elif [ "$rpp" = "14" ]                                     #mp4 en webm
        then
            echo "NON DISPONIBLE"
            varo=1  
            sleep 2
        else
            echo -e "\nVeiller entrer un nombre entre 1 et 12\n" # gestion de l'erreur si l'utilisateur utilise une autre lettre ou un autre caratère
            sleep 2
            varo=0
        fi;
    done
    clear
    echo -e "\nVos fichiers on bien été réencodé en $encov dans votre dossier courant\n"
    sleep 2
    }

    function convertisso-audio {
    clear
    echo -e "\nCe programme va convertire vos fichiers audio dans le format souhaiter, dans votre dossier courant"
    var=0
while [ $var = 0 ];do
    echo -e "\n"
    echo ' ╔════╦═════════════╦═════╦═════════════╦════╦═════════════╦═════╦═════════════╗'
    echo ' ║ 1  ║ mp3 en waw  ║ 7   ║ wav en aac  ║ 13 ║ ac3 en wav  ║ 19  ║ aac en ogg  ║'
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
    read -p "Choisiser le numéro correspondant pour convertir le fichier.   : " rp # demande a l'utilisateur dans quelle format il veut convertir ses fichiers
        if [ "$rp" = "1" ]                                     #mp3 en waw
        then
            echo "Vos fichier sont en cours de conversion ..."
            for a in *.mp3; do ffmpeg -i "$a" "${a%.mp3}.wav"> /dev/null 2>&1; done
            enco=wav
            var=1
        elif [ "$rp" = "2" ]                                   #mp3 en ogg
        then
            echo "Vos fichier sont en cours de conversion ..."
            sleep 2
        for b in *.mp3; do ffmpeg -i "${b}" -acodec libvorbis "${b/%mp3}.ogg"> /dev/null 2>&1; done #convertis les fichiers MP3 en OGG
            enco=ogg
            var=1
        elif [ "$rp" = "3" ]                                   #mp3 en aac
        then
            echo "Vos fichier sont en cours de conversion ..."
            sleep 2
            for c in *.mp3; do ffmpeg -i "$c" -acodec libfaac "${c%.mp3}.aac"> /dev/null 2>&1; done
            enco=aac
            var=1
        elif [ "$rp" = "4" ]                                   #mp3 en ac3
        then
            echo "Vos fichier sont en cours de conversion ..."
            sleep 2
            for p in *.mp3; do ffmpeg -i "$p" -acodec ac3 "${p%.mp3}.ac3"> /dev/null 2>&1; done
        
            enco=ac3
            var=1
        elif [ "$rp" = "5" ]                                   #wav en mp3
        then
            echo "Vos fichier sont en cours de conversion ..."
            sleep 2
            for d in *.wav; do ffmpeg -i "$d" -f mp3 "${d%.waw}.mp3"> /dev/null 2>&1; done
            enco=mp3
            var=1
        elif [ "$rp" = "6" ]                                       #wav en ogg
        then
            echo "Vos fichier sont en cours de conversion ..."
            sleep 2
            for h in *.wav; do ffmpeg -i "$h" -acodec libvorbis "${h%.waw}.ogg"> /dev/null 2>&1; done 
            enco=ogg
            var=1
        elif [ "$rp" = "7" ]                                    #wav en aac
        then
            echo "Vos fichier sont en cours de conversion ..."
            sleep 2
            for i in *.wav; do ffmpeg -i "$i" -acodec libfaac "${i%.waw}.aac"> /dev/null 2>&1; done 
            enco=aac
            var=1
        elif [ "$rp" = "8" ]                                   #wav en ac3
        then
            echo "Vos fichier sont en cours de conversion ..."
            sleep 2
            for j in *.wav; do ffmpeg -i "$j" -acodec libmp3lame "${j%.waw}.ac3"> /dev/null 2>&1; done 
            enco=ac3
            var=1
        elif [ "$rp" = "9" ]                                   #ogg en mp3
        then
            echo "Vos fichier sont en cours de conversion ..."
            sleep 2
            for g in *.ogg; do ffmpeg -i "$g" -acodec libmp3lame "${g%.ogg}.mp3"> /dev/null 2>&1; done #convertis les fichiers OGG en MP3
            enco=mp3
            var=1
        elif [ "$rp" = "10" ]                                   #ogg en wav
        then
            echo "Vos fichier sont en cours de conversion ..."
            sleep 2
            for k in *.ogg; do ffmpeg -i "$k" "${k%.ogg}.wav"> /dev/null 2>&1; done 
            enco=wav
            var=1
        elif [ "$rp" = "11" ]                                   #ogg en aac
        then
            echo "Vos fichier sont en cours de conversion ..."
            sleep 2
            for l in *.ogg; do ffmpeg -i "$l" -acodec libfaac "${l%.ogg}.aac"> /dev/null 2>&1; done 
            enco=aac
            var=1
        elif [ "$rp" = "12" ]                                   #ogg en ac3
        then
            echo "Vos fichier sont en cours de conversion ..."
            sleep 2
            for m in *.ogg; do ffmpeg -i "$m" -acodec ac3 "${m%.ogg}.ac3"> /dev/null 2>&1; done 
            enco=ac3
            var=1
        elif [ "$rp" = "13" ]                                   #ac3 en wav
        then
            echo "Vos fichier sont en cours de conversion ..."
            sleep 2
            for n in *.ac3; do ffmpeg -i "$n"  "${n%.ac3}.wav"> /dev/null 2>&1; done
            enco=wav
            var=1
        elif [ "$rp" = "14" ]                                   #ac3 en aac
        then
            echo "Vos fichier sont en cours de conversion ..."
            sleep 2
            for o in *.ac3; do ffmpeg -i "$o" -acodec libfaac "${o%.ac3}.aac"> /dev/null 2>&1; done
            enco=aac
            var=1
        elif [ "$rp" = "15" ]                                   #ac3 en ogg
        then
            echo "Vos fichier sont en cours de conversion ..."
            sleep 2
            for p in *.ac3; do ffmpeg -i "$p" -acodec libvorbis "${p%.ac3}.ogg"> /dev/null 2>&1; done
            enco=ogg
            var=1
        elif [ "$rp" = "16" ]                                   #ac3 en mp3
        then
            echo "Vos fichier sont en cours de conversion ..."
            sleep 2
            for f in *.ac3; do ffmpeg -i "$f" -acodec libmp3lame "${f%.ac3}.mp3"> /dev/null 2>&1; done
            enco=mp3
            var=1
        elif [ "$rp" = "17" ]                                   #aac en wav
        then
            echo "Vos fichier sont en cours de conversion ..."
            sleep 2
            for q in *.aac; do ffmpeg -i "$q" "${q%.aac}.wav"> /dev/null 2>&1 ; done
            enco=wav
            var=1
        elif [ "$rp" = "18" ]                                   #aac en ac3
        then
            echo "Vos fichier sont en cours de conversion ..."
            sleep 2
            for r in *.aac; do ffmpeg -i "$r" -acodec ac3 "${r%.aac}.ac3"> /dev/null 2>&1; done
            enco=ac3
            var=1
        elif [ "$rp" = "19" ]                                  #aac en ogg
        then
            echo "Vos fichier sont en cours de conversion ..."
            sleep 2
            for s in *.aac; do ffmpeg -i "$s" -acodec libvorbis "${s%.aac}.ogg"> /dev/null 2>&1; done
            enco=ogg
            var=1
        elif [ "$rp" = "20" ]                                   #aac en mp3
        then
            echo "Vos fichier sont en cours de conversion ..."
            sleep 2
            for e in *.aac; do ffmpeg -i "$e" -acodec libmp3lame "${e%.aac}.mp3"> /dev/null 2>&1; done
            enco=mp3
            var=1
        elif [ "$rp" = "21" ]                                   #flac en mp3
        then
            echo "Vos fichier sont en cours de conversion ..."
            sleep 2
            for rr in *.flac; do ffmpeg -i "$rr" -acodec libmp3lame "${rr%.flac}.mp3"> /dev/null 2>&1; done
            enco=mp3
            var=1
        elif [ "$rp" = "22" ]                                   #flac en wav
        then
            echo "Vos fichier sont en cours de conversion ..."
            sleep 2
            for ss in *.flac; do ffmpeg -i "$ss" "${ss%.flac}.wav"> /dev/null 2>&1; done
            enco=wav
            var=1
        elif [ "$rp" = "23" ]                                   #flac en ogg
        then
            echo "Vos fichier sont en cours de conversion ..."
            sleep 2
            for tt in *.flac; do ffmpeg -i "$tt" -acodec libvorbis "${tt%.flac}.ogg"> /dev/null 2>&1; done
            enco=ogg 
            var=1 
        elif [ "$rp" = "24" ]                                   #flac en ac3
        then
            echo "Vos fichier sont en cours de conversion ..."
            sleep 2
            for tt in *.flac; do ffmpeg -i "$tt" -acodec ac3 "${tt%.flac}.ac3"> /dev/null 2>&1; done
            enco=ac3 
            var=1              
        else
            echo -e "\nVeiller entrer un nombre entre 1 et 24\n" # gestion de l'erreur si l'utilisateur utilise une autre lettre ou un autre caratère
            sleep 2
            clear
            var=0
        fi;
done
echo -e "\nVos fichiers on bien été réencodé en $enco dans votre dossier courant\n"
sleep 2
}

function convertisso-image {
clear
vor=0

    echo ' ╔════╦══════════════╦════╦══════════════╗'
    echo ' ║ 1  ║  png en jpg  ║ 8  ║ pdf en tiff  ║'
    echo ' ╠════╬══════════════╬════╬══════════════╣'
    echo ' ║ 2  ║  jpg en png  ║ 9  ║  pdf en jpg  ║'
    echo ' ╠════╬══════════════╬════╬══════════════╣'
    echo ' ║ 3  ║  tiff en png ║ 10 ║  pdf en png  ║'
    echo ' ╠════╬══════════════╬════╬══════════════╣'
    echo ' ║ 4  ║  tiff en jpg ║ 11 ║ svg en tiff  ║'
    echo ' ╠════╬══════════════╬════╬══════════════╣'
    echo ' ║ 5  ║  tiff en BMP ║ 12 ║  svg en png  ║'
    echo ' ╠════╬══════════════╬════╬══════════════╣'
    echo ' ║ 6  ║  tiff en pdf ║ 13 ║  svg en pdf  ║'
    echo ' ╠════╬══════════════╬════╬══════════════╣'
    echo ' ║ 7  ║  tiff en gif ║ 14 ║NON DISPONIBLE║'
    echo ' ╚════╩══════════════╩════╩══════════════╝'
    read -p "Choisiser le numéro correspondant pour convertir le fichier.   : " rrrrp # demande a l'utilisateur dans quelle format il veut convertir ses fichiers
while [ $vor = 0 ];do
    if [ "$rrrrp" = "1" ]                                      #png en jpg
        then
            echo "Vos fichier sont en cours de conversion ..."
            sleep 2
            for uu in *.png; do  convert "$uu"  "${uu%.png}.jpg"; done
            encov=jpg 
            vor=1
    elif [ "$rrrrp" = "2" ]                                    #jpg en png
            then
            echo "Vos fichier sont en cours de conversion ..."
            sleep 2
            for vv in *.jpg; do  convert "$vv"  "${vv%.jpg}.png"; done
            encov=png 
            vor=1
    elif [ "$rrrrp" = "3" ]                                    #tiff en png
            then
            echo "Vos fichier sont en cours de conversion ..."
            sleep 2
            for ww in *.tiff; do  convert "$ww"  "${ww%.tiff}.png"; done
            encov=png 
            vor=1
    elif [ "$rrrrp" = "4" ]                                    #tiff en jpg
            then
            echo "Vos fichier sont en cours de conversion ..."
            sleep 2
            for yy in *.tiff; do  convert "$yy"  "${yy%.tiff}.jpg"; done
            encov=jpg
            vor=1
        elif [ "$rrrrp" = "5" ]                                #tiff en BMP
            then
            echo "Vos fichier sont en cours de conversion ..."
            sleep 2
            for zz in *.tiff; do  convert "$zz"  "${zz%.tiff}.BMP"; done
            encov=BMP 
            vor=1    
        elif [ "$rrrrp" = "6" ]                                #tiff en pdf #
            then
            echo "Vos fichier sont en cours de conversion ..."
            sleep 2
            for aaa in *.tiff; do  tiff2pdf -o "${aaa%.tiff}.pdf" "$aaa"; done
            encov=pdf 
            vor=1
        elif [ "$rrrrp" = "7" ]                                #tiff en gif
            then
            echo "Vos fichier sont en cours de conversion ..."
            sleep 2
            for bbb in *.tiff; do  convert "$bbb"  "${bbb%.tiff}.gif"; done
            encov=gif 
            vor=1
        elif [ "$rrrrp" = "8" ]                                #pdf en tiff
            then
            echo "Vos fichier sont en cours de conversion ..."
            sleep 2
            for eee in *.pdf; do  convert "$eee"  "${eee%.pdf}.tiff"; done
            encov=tiff 
            vor=1
        elif [ "$rrrrp" = "9" ]                                #pdf en jpg
            then
            echo "Vos fichier sont en cours de conversion ..."
            sleep 2
            for fff in *.pdf; do  convert "$fff"  "${fff%.pdf}.jpg"; done
            encov=jpg 
            vor=1
        elif [ "$rrrrp" = "10" ]                                #pdf en png
            then
            echo "Vos fichier sont en cours de conversion ..."
            sleep 2
            for ggg in *.pdf; do  convert "$ggg"  "${ggg%.pdf}.png"; done
            encov=png 
            vor=1
        elif [ "$rrrrp" = "11" ]                                #svg en tiff
            then
            echo "Vos fichier sont en cours de conversion ..."
            sleep 2
            for hhh in *.svg; do  convert "$hhh"  "${hhh%.svg}.tiff"; done
            encov=tiff 
            vor=1
        elif [ "$rrrrp" = "12" ]                                #svg en png
            then
            echo "Vos fichier sont en cours de conversion ..."
            sleep 2
            for hhh in *.svg; do  convert "$hhh"  "${hhh%.svg}.png"; done
            encov=png 
            vor=1
        elif [ "$rrrrp" = "13" ]                                #svg en pdf
            then
            echo "Vos fichier sont en cours de conversion ..."
            sleep 2
            for hhh in *.svg; do  rsvg-convert -f pdf -o "${hhh%.svg}.pdf" "$hhh" ; done
            encov=pdf 
            vor=1
        elif [ "$rrrrp" = "14" ]                               
            then
            echo "NON DISPONIBLE"
            sleep 2
            vor=0
        else
        echo -e "\nVeiller entrer un nombre entre 1 et 13 \n" # gestion de l'erreur si l'utilisateur utilise une autre lettre ou un autre caratère
        sleep 2
        clear
        vor=0
    fi;
done
echo -e "\nVos fichiers on bien été réencodé en $encov dans votre dossier courant\n"
sleep 2

}


ver=0
clear
convertisso
sleep 2
    echo ' ╔════╦═════════════════════════════╦════╦═════════════════════════════════════╗'
    echo " ║ 1  ║ convertir un fichier audio  ║ 4  ║ conversion de sous-titres vidéo     ║"
    echo ' ╠════╬═════════════════════════════╬════╬═════════════════════════════════════╣'
    echo " ║ 2  ║ convertir un fichier vidéo  ║ 5  ║           conversion d'image        ║"
    echo ' ╠════╬═════════════════════════════╬════╬═════════════════════════════════════╣'
    echo " ║ 3  ║    télécharger un vidéo     ║ 6  ║            NON DISPONIBLE           ║"
    echo ' ╚════╩═════════════════════════════╩════╩═════════════════════════════════════╝'
        read -p "Choisier le numéro correspondant a votre besoin " rrp
        if [ "$rrp" = "1" ]                                     
            then
                rm -f result.txt
                convertisso-audio
        elif [ "$rrp" = "2" ]                                 
            then 
                rm -f result.txt
                convertisso-video
        elif [ "$rrp" = "3" ]                                 
            then 
                rm -f result.txt
                convertisso-download-video
        elif [ "$rrp" = "4" ]                                 
            then 
                rm -f result.txt
                convertisso-sous-titres-video
        elif [ "$rrp" = "5" ]                                 
            then 
                convertisso-image
        elif [ "$rrp" = "6" ]                                 
            then 
                echo "NON DISPONIBLE VEUEILLER CHOISIR UNE AUTRE OPTION"
        elif [ "$rrp" = "exit" ]||[ "$rrp" = "EXIT" ]||[ "$rrp" = "q" ]                               
            then
                rm -f result.txt
                exit
        else
                echo -e "Veuillez entrer 1, 2, 3, 4, 5"
                clear
                varro=0
        fi;
done
