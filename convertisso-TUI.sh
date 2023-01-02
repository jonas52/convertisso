#!/bin/bash
#---[Metadata]--------------------------------------------------------------#
#  Filename ~ convertisso-beta.sh          [Created: 2022-10-2 | 8:30 PM]   #
#                                          [Update: 2022-10-29 | 9:30 AM]   #
#---[Author of this file]---------------------------------------------------#
#  Jonas Petitpierre ~  @jonas52 -> https://github.com/jonas52
                                                       #
echo -n -e "\033]0;Convertisso\007"
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
convertisso
sleep 3
clear
varro=0
while [ $varro = 0 ];do

function convertisso-subtitle {
clear
varorr=0
while [ $varorr = 0 ];do

subtitle=$(whiptail --title "Convertisso audio menu" --menu "Choose an option" 40 90 20 \
"1" "vtt to srt" \
"2" "vtt to ass" \
"3" "vtt to lrc" \
"4" "srt to vtt" \
"5" "srt to ass" \
"6" "srt to lrc" \
"7" "ass to srt" \
"8" "ass to lrc" \
"9" "ass to vtt" \
"10" "lrc to srt" \
"11" "lrc to ass" \
"12" "lrc to vtt" \
"13" "EXIT" 3>&1 1>&2 2>&3)
        if [ "$subtitle" = "1" ]
            then                                     #vtt en srt     
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                    if [ "$?" = "0" ]; then
                    vttt=$(find $FILE -name "*.vtt")
                            if [ -n "$vttt" ]; then
                                clear                  
                                for gg in $vttt; do ffmpeg -i "$gg" "${gg%.vtt}.srt" > /dev/null 2>&1; done
                                encov=srt
                                varorr=1
                            else
                                zenity --error --text="No compatible files found in the selected directory"
                                var=0
                            fi;
                elif [ "$?" = "1" ]                           
                    then
                        zenity --error --text="No files selected"
                        var=0
                else 
                        zenity --error --text="An unexpected error has occurred"
                        var=0
                fi;
        elif [ "$subtitle" = "2" ]                                    #vtt en ass
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                    if [ "$?" = "0" ]; then
                    vttt=$(find $FILE -name "*.vtt")
                            if [ -n "$vttt" ]; then
                                clear    
                                for hh in $vttt; do ffmpeg -i "$hh" "${hh%.vtt}.ass" > /dev/null 2>&1; done
                                encov=ass
                                varorr=1
                            else
                                zenity --error --text="No compatible files found in the selected directory"
                                var=0
                            fi;
                elif [ "$?" = "1" ]                           
                    then
                        zenity --error --text="No files selected"
                        var=0
                else 
                        zenity --error --text="An unexpected error has occurred"
                        var=0
                fi;
        elif [ "$subtitle" = "3" ]                                     #vtt en lrc
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                    if [ "$?" = "0" ]; then
                    vttt=$(find $FILE -name "*.vtt")
                            if [ -n "$vttt" ]; then
                                clear    
                                for ii in $vttt; do ffmpeg -i "$ii" "${ii%.vtt}.lrc" > /dev/null 2>&1; done
                                encov=lrc
                                varorr=1
                            else
                                zenity --error --text="No compatible files found in the selected directory"
                                var=0
                            fi;
                elif [ "$?" = "1" ]                           
                    then
                        zenity --error --text="No files selected"
                        var=0
                else 
                        zenity --error --text="An unexpected error has occurred"
                        var=0
                fi;
        elif [ "$subtitle" = "4" ]                                     #srt en vtt                        
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                    if [ "$?" = "0" ]; then
                    srtt=$(find $FILE -name "*.srt")
                            if [ -n "$srtt" ]; then
                                clear
                                for jj in $srtt; do ffmpeg -i "$jj" "${jj%.srt}.vtt" > /dev/null 2>&1; done
                                encov=vtt
                                varorr=1
                            else
                                zenity --error --text="No compatible files found in the selected directory"
                                var=0
                            fi;
                elif [ "$?" = "1" ]                           
                    then
                        zenity --error --text="No files selected"
                        var=0
                else 
                        zenity --error --text="An unexpected error has occurred"
                        var=0
                fi;
        elif [ "$subtitle" = "5" ]                                     #srt en ass
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                    if [ "$?" = "0" ]; then
                    srtt=$(find $FILE -name "*.srt")
                            if [ -n "$srtt" ]; then
                                clear
                                for kk in $srtt; do ffmpeg -i "$kk" "${kk%.srt}.ass" > /dev/null 2>&1; done
                                encov=ass
                                varorr=1
                            else
                                zenity --error --text="No compatible files found in the selected directory"
                                var=0
                            fi;
                elif [ "$?" = "1" ]                           
                    then
                        zenity --error --text="No files selected"
                        var=0
                else 
                        zenity --error --text="An unexpected error has occurred"
                        var=0
                fi;
        elif [ "$subtitle" = "6" ]                                     #srt en lrc
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                    if [ "$?" = "0" ]; then
                    srtt=$(find $FILE -name "*.srt")
                            if [ -n "$srtt" ]; then
                                clear
                                for ll in $srtt; do ffmpeg -i "$ll" "${ll%.srt}.lrc" > /dev/null 2>&1; done
                                encov=lrc
                                varorr=1
                            else
                                zenity --error --text="No compatible files found in the selected directory"
                                var=0
                            fi;
                elif [ "$?" = "1" ]                           
                    then
                        zenity --error --text="No files selected"
                        var=0
                else 
                        zenity --error --text="An unexpected error has occurred"
                        var=0
                fi;
        elif [ "$subtitle" = "7" ]                                     #ass en srt
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                    if [ "$?" = "0" ]; then
                    asss=$(find $FILE -name "*.ass")
                            if [ -n "$asss" ]; then
                                clear  
                                for mm in $asss; do ffmpeg -i "$mm" "${mm%.ass}.srt" > /dev/null 2>&1; done
                                encov=srt
                                varorr=1
                            else
                                zenity --error --text="No compatible files found in the selected directory"
                                var=0
                            fi;
                elif [ "$?" = "1" ]                           
                    then
                        zenity --error --text="No files selected"
                        var=0
                else 
                        zenity --error --text="An unexpected error has occurred"
                        var=0
                fi;
        elif [ "$subtitle" = "8" ]                                     #ass en lrc
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                    if [ "$?" = "0" ]; then
                    asss=$(find $FILE -name "*.ass")
                            if [ -n "$asss" ]; then
                                clear   
                                for nn in $asss; do ffmpeg -i "$nn" "${nn%.ass}.lrc" > /dev/null 2>&1; done
                                encov=lrc
                                varorr=1
                            else
                                zenity --error --text="No compatible files found in the selected directory"
                                var=0
                            fi;
                elif [ "$?" = "1" ]                           
                    then
                        zenity --error --text="No files selected"
                        var=0
                else 
                        zenity --error --text="An unexpected error has occurred"
                        var=0
                fi;
        elif [ "$subtitle" = "9" ]                                     #ass en vtt
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                    if [ "$?" = "0" ]; then
                    asss=$(find $FILE -name "*.ass")
                            if [ -n "$asss" ]; then
                                clear   
                                for oo in $asss; do ffmpeg -i "$oo" "${oo%.ass}.vtt" > /dev/null 2>&1; done
                                encov=vtt
                                varorr=1
                            else
                                zenity --error --text="No compatible files found in the selected directory"
                                var=0
                            fi;
                elif [ "$?" = "1" ]                           
                    then
                        zenity --error --text="No files selected"
                        var=0
                else 
                        zenity --error --text="An unexpected error has occurred"
                        var=0
                fi;
        elif [ "$subtitle" = "10" ]                                     #lrc en srt
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                    if [ "$?" = "0" ]; then
                    lrcc=$(find $FILE -name "*.lrc")
                            if [ -n "$lrcc" ]; then
                                clear   
                                for pp in $lrcc; do ffmpeg -i "$pp" "${pp%.lrc}.srt" > /dev/null 2>&1; done
                                encov=srt
                                varorr=1
                            else
                                zenity --error --text="No compatible files found in the selected directory"
                                var=0
                            fi;
                elif [ "$?" = "1" ]                           
                    then
                        zenity --error --text="No files selected"
                        var=0
                else 
                        zenity --error --text="An unexpected error has occurred"
                        var=0
                fi;
        elif [ "$subtitle" = "11" ]                                     #lrc en ass
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                    if [ "$?" = "0" ]; then
                    lrcc=$(find $FILE -name "*.lrc")
                            if [ -n "$lrcc" ]; then
                                clear 
                                for qq in $lrcc; do ffmpeg -i "$qq" "${qq%.lrc}.ass" > /dev/null 2>&1; done
                                encov=ass
                                varorr=1
                            else
                                zenity --error --text="No compatible files found in the selected directory"
                                var=0
                            fi;
                elif [ "$?" = "1" ]                           
                    then
                        zenity --error --text="No files selected"
                        var=0
                else 
                        zenity --error --text="An unexpected error has occurred"
                        var=0
                fi;
        elif [ "$subtitle" = "12" ]                                     #lrc en vtt
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                    if [ "$?" = "0" ]; then
                    lrcc=$(find $FILE -name "*.lrc")
                            if [ -n "$lrcc" ]; then
                                clear
                                for rr in $lrcc; do ffmpeg -i "$rr" "${rr%.lrc}.vtt" > /dev/null 2>&1; done
                                encov=vtt
                                varorr=1
                            else
                                zenity --error --text="No compatible files found in the selected directory"
                                var=0
                            fi;
                elif [ "$?" = "1" ]                           
                    then
                        zenity --error --text="No files selected"
                        var=0
                else 
                        zenity --error --text="An unexpected error has occurred"
                        var=0
                fi;
        elif [ "$subtitle" = "13" ]                                     
            then
                varorr=1
        else
            zenity --error --text="Please enter a number between 1 and 12"
            varorr=0
        fi;
done

}
function convertisso-download-video {
        clear
        varor=0
ping -c 1 8.8.8.8 > /dev/null 2>&1
if [ $? -eq 0 ]
then
    while [ "$varor" = 0 ];do
        LINK=$(whiptail --title "Input" --inputbox "URL of your video" 10 60 3>&1 1>&2 2>&3)
        DOWNLOAD=$(whiptail --title "Convertisso download video menu" --menu "Choose an option" 40 90 20 \
        "1" "video without subtitle" \
        "2" "video with subtitle" \
        "3" "only audio (mp3)" \
        "4" "only the subtitle" \
        "5" "EXIT" 3>&1 1>&2 2>&3)
        DESTINATION=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
        if [ "$DOWNLOAD" = "1" ]                                     #video without subtitle
            then
            clear
            youtube-dl -f best --add-metadata "$LINK"
            while [ $? = "1" ] ;do zenity --error --text="Please retry INVALIDE link" varor=0; done
            mv *.mp4 $DESTINATION > /dev/null 2>&1
            mv *.mkv $DESTINATION > /dev/null 2>&1
            mv *.webm $DESTINATION > /dev/null 2>&1
            mv *.flv $DESTINATION > /dev/null 2>&1
            varor=1
        elif [ "$DOWNLOAD" = "2" ]                                     #video with subtitle
            then
            clear
            youtube-dl --write-srt --all-subs --add-metadata "$LINK"
            while [ $? = "1" ] ;do zenity --error --text="Please retry INVALIDE link" varor=0; done
            mv *.mp4 $DESTINATION > /dev/null 2>&1
            mv *.mkv $DESTINATION > /dev/null 2>&1
            mv *.webm $DESTINATION > /dev/null 2>&1
            mv *.flv $DESTINATION > /dev/null 2>&1
            mv *.srt $DESTINATION > /dev/null 2>&1
            mv *.ass $DESTINATION > /dev/null 2>&1
            mv *.vtt $DESTINATION > /dev/null 2>&1
            mv *.lrc $DESTINATION > /dev/null 2>&1
            varor=1   
        elif [ "$DOWNLOAD" = "3" ]                                     #only audio (mp3)
            then
            clear
            youtube-dl -x --audio-format best --add-metadata "$LINK"
            while [ $? = "1" ] ;do zenity --error --text="Please retry INVALIDE link" varor=0; done
            mv *.mp3 $DESTINATION > /dev/null 2>&1
            mv *.aac $DESTINATION > /dev/null 2>&1
            mv *.flac $DESTINATION > /dev/null 2>&1
            mv *.mp3 $DESTINATION > /dev/null 2>&1
            mv *.m4a $DESTINATION > /dev/null 2>&1
            mv *.ogg $DESTINATION > /dev/null 2>&1
            mv *.wav $DESTINATION > /dev/null 2>&1
            mv *.opus $DESTINATION > /dev/null 2>&1
            mv *.vorbis $DESTINATION > /dev/null 2>&1
            varor=1
        elif [ "$DOWNLOAD" = "4" ]                                     #only the subtitle 
            then
            clear
            youtube-dl --all-subs -w --skip-download -q --add-metadata "$LINK"
            while [ $? = "1" ] ;do zenity --error --text="Please retry INVALIDE link" varor=0; done
            varor=1
            mv *.srt $DESTINATION > /dev/null 2>&1
            mv *.ass $DESTINATION > /dev/null 2>&1
            mv *.vtt $DESTINATION > /dev/null 2>&1
            mv *.lrc $DESTINATION > /dev/null 2>&1
        elif [ "$DOWNLOAD" = "5" ]                                     
            then
                varor=1
        else
            zenity --error --text="Please enter a number between 1 and 4"
            varor=0
        fi;
    done
else
    zenity --error --text="Your device is not connected to internet"
    varor=1
fi;
}

function convertisso-video {
clear
varo=0
while [ $varo = 0 ];do
video=$(whiptail --title "Convertisso video menu" --menu "Choose an option" 40 90 20 \
"1" "mkv to avi" \
"2" "mkv to mov" \
"3" "mkv to mp4" \
"4" "mkv to webm" \
"5" "mkv to flv" \
"6" "mkv to hevc" \
"7" "mp4 to mkv" \
"8" "mp4 to mov" \
"9" "mp4 to avi" \
"10" "mp4 to webm" \
"11" "mp4 to flv" \
"12" "mp4 to hevc" \
"13" "mov to mkv" \
"14" "mov to mp4" \
"15" "mov to avi" \
"16" "mov to webm" \
"17" "mov to flv" \
"18" "mov to hevc" \
"19" "avi to mkv" \
"20" "avi to mp4" \
"21" "avi to mov" \
"22" "avi to webm" \
"23" "avi to flv" \
"24" "avi to hevc" \
"25" "webm to avi" \
"26" "webm to mkv" \
"27" "webm to mov" \
"28" "webm to mp4" \
"29" "webm to flv" \
"30" "webm to hevc" \
"31" "hevc to avi" \
"32" "hevc to mkv" \
"33" "hevc to mov" \
"34" "hevc to mp4" \
"35" "hevc to flv" \
"36" "hevc to webm" \
"37" "flv to avi" \
"38" "flv to mkv" \
"39" "flv to mov" \
"40" "flv to mp4" \
"41" "flv to hevc" \
"42" "flv to webm" \
"43" "EXIT" 3>&1 1>&2 2>&3)
        if [ "$video" = "1" ]                                     #mkv en avi
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                    if [ "$?" = "0" ]; then
                    mkvv=$(find $FILE -name "*.mkv")
                            if [ -n "$mkvv" ]; then
                                clear
                                echo "Conversion in progress ..."
                                for t in $mkvv; do ffmpeg -i "$t" -codec copy "${t%.mkv}.avi"> /dev/null 2>&1; done
                                encov=avi
                                varo=1
                            else
                                zenity --error --text="No compatible files found in the selected directory"
                                var=0
                            fi;
                elif [ "$?" = "1" ]                           
                    then
                        zenity --error --text="No files selected"
                        varo=0
                else 
                        zenity --error --text="An unexpected error has occurred"
                        varo=0
                fi;
        elif [ "$video" = "2" ]                                   #mkv en mov
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                    if [ "$?" = "0" ]; then
                    mkvv=$(find $FILE -name "*.mkv")
                            if [ -n "$mkvv" ]; then
                                clear
                                echo "Conversion in progress ..."
                                for u in $mkvv; do ffmpeg -i "$u" -codec copy "${u%.mkv}.mov"> /dev/null 2>&1; done
                                encov=mov
                                varo=1
                            else
                                zenity --error --text="No compatible files found in the selected directory"
                                var=0
                            fi;
                elif [ "$?" = "1" ]                           
                    then
                        zenity --error --text="No files selected"
                        varo=0
                else 
                        zenity --error --text="An unexpected error has occurred"
                        varo=0
                fi;
        elif [ "$video" = "3" ]                                     #mkv en mp4
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                 if [ "$?" = "0" ]; then
                    mkvv=$(find $FILE -name "*.mkv")
                            if [ -n "$mkvv" ]; then
                                clear
                                echo "Conversion in progress ..."
                                for v in $FILE $mkvv; do ffmpeg -i "$v" -codec copy "${v%.mkv}.mp4"> /dev/null 2>&1; done
                                encov=mp4
                                varo=1
                            else
                                zenity --error --text="No compatible files found in the selected directory"
                                var=0
                            fi;
                elif [ "$?" = "1" ]                           
                    then
                        zenity --error --text="No files selected"
                        varo=0
                else 
                        zenity --error --text="An unexpected error has occurred"
                        varo=0
                fi;
        elif [ "$video" = "4" ]                                     #mkv en webm
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                 if [ "$?" = "0" ]; then
                    mkvv=$(find $FILE -name "*.mkv")
                            if [ -n "$mkvv" ]; then
                                clear
                                echo "Conversion in progress ..."
                                for v in $FILE $mkvv; do ffmpeg -i "$v" -c:v libvpx -c:a libvorbis "${v%.mkv}.webm"> /dev/null 2>&1; done
                                encov=webm
                                varo=1
                            else
                                zenity --error --text="No compatible files found in the selected directory"
                                var=0
                            fi;
                elif [ "$?" = "1" ]                           
                    then
                        zenity --error --text="No files selected"
                        varo=0
                else 
                        zenity --error --text="An unexpected error has occurred"
                        varo=0
                fi;
        elif [ "$video" = "5" ]                                     #mkv en flv
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                 if [ "$?" = "0" ]; then
                    mkvv=$(find $FILE -name "*.mkv")
                            if [ -n "$mkvv" ]; then
                                clear
                                echo "Conversion in progress ..."
                                for v in $FILE $mkvv; do ffmpeg -i "$v" -c:v flv -c:a mp3 "${v%.mkv}.flv"> /dev/null 2>&1; done
                                encov=flv
                                varo=1
                            else
                                zenity --error --text="No compatible files found in the selected directory"
                                var=0
                            fi;
                elif [ "$?" = "1" ]                           
                    then
                        zenity --error --text="No files selected"
                        varo=0
                else 
                        zenity --error --text="An unexpected error has occurred"
                        varo=0
                fi;
        elif [ "$video" = "6" ]                                     #mkv en hevc
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                 if [ "$?" = "0" ]; then
                    mkvv=$(find $FILE -name "*.mkv")
                            if [ -n "$mkvv" ]; then
                                clear
                                echo "Conversion in progress ..."
                                for v in $FILE $mkvv; do ffmpeg -i "$v" -c:v libx265 -c:a aac "${v%.mkv}.hevc"> /dev/null 2>&1; done
                                encov=flv
                                varo=1
                            else
                                zenity --error --text="No compatible files found in the selected directory"
                                var=0
                            fi;
                elif [ "$?" = "1" ]                           
                    then
                        zenity --error --text="No files selected"
                        varo=0
                else 
                        zenity --error --text="An unexpected error has occurred"
                        varo=0
                fi;
        elif [ "$video" = "7" ]                                     #mp4 en mkv                                     
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                 if [ "$?" = "0" ]; then
                    mp44=$(find $FILE -name "*.mp4")
                            if [ -n "$mp44" ]; then
                                clear
                                echo "Conversion in progress ..."
                                for w in $mp44; do ffmpeg -i "$w" -codec copy "${w%.mp4}.mkv"> /dev/null 2>&1; done
                                encov=mkv
                                varo=1
                            else
                                zenity --error --text="No compatible files found in the selected directory"
                                var=0
                            fi;
                elif [ "$?" = "1" ]                           
                    then
                        zenity --error --text="No files selected"
                        varo=0
                else 
                        zenity --error --text="An unexpected error has occurred"
                        varo=0
                fi;
        elif [ "$video" = "8" ]                                     #mp4 en mov                                    
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                 if [ "$?" = "0" ]; then
                    mp44=$(find $FILE -name "*.mp4")
                            if [ -n "$mp44" ]; then
                                clear
                                echo "Conversion in progress ..."
                                for x in $mp44; do ffmpeg -i "$x" -codec copy "${x%.mp4}.mov"> /dev/null 2>&1; done
                                encov=mov
                                varo=1
                            else
                                zenity --error --text="No compatible files found in the selected directory"
                                var=0
                            fi;
                elif [ "$?" = "1" ]                           
                    then
                        zenity --error --text="No files selected"
                        varo=0
                else 
                        zenity --error --text="An unexpected error has occurred"
                        varo=0
                fi;
        elif [ "$video" = "9" ]                                     #mp4 en avi
            then           
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                 if [ "$?" = "0" ]; then
                    mp44=$(find $FILE -name "*.mp4")
                            if [ -n "$mp44" ]; then
                                clear
                                echo "Conversion in progress ..."                      
                                for y in $mp44; do ffmpeg -i "$y" -codec copy "${y%.mp4}.avi"> /dev/null 2>&1; done
                                encov=avi
                                varo=1
                            else
                                zenity --error --text="No compatible files found in the selected directory"
                                var=0
                            fi;
                elif [ "$?" = "1" ]                           
                    then
                        zenity --error --text="No files selected"
                        varo=0
                else 
                        zenity --error --text="An unexpected error has occurred"
                        varo=0
                fi;
        elif [ "$video" = "10" ]                                     #mp4 en webm
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                 if [ "$?" = "0" ]; then
                    mp44=$(find $FILE -name "*.mp4")
                            if [ -n "$mp44" ]; then
                                clear
                                echo "Conversion in progress ..."
                                for v in $FILE $mp44; do ffmpeg -i "$v" -c:v libvpx -c:a libvorbis "${v%.mp4}.webm"> /dev/null 2>&1; done
                                encov=webm
                                varo=1
                            else
                                zenity --error --text="No compatible files found in the selected directory"
                                var=0
                            fi;
                elif [ "$?" = "1" ]                           
                    then
                        zenity --error --text="No files selected"
                        varo=0
                else 
                        zenity --error --text="An unexpected error has occurred"
                        varo=0
                fi;
        elif [ "$video" = "11" ]                                     #mp4 en flv
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                 if [ "$?" = "0" ]; then
                    mp44=$(find $FILE -name "*.mp4")
                            if [ -n "$mp44" ]; then
                                clear
                                echo "Conversion in progress ..."
                                for v in $FILE $mp44; do ffmpeg -i "$v" -c:v flv -c:a mp3 "${v%.mp4}.flv"> /dev/null 2>&1; done
                                encov=flv
                                varo=1
                            else
                                zenity --error --text="No compatible files found in the selected directory"
                                var=0
                            fi;
                elif [ "$?" = "1" ]                           
                    then
                        zenity --error --text="No files selected"
                        varo=0
                else 
                        zenity --error --text="An unexpected error has occurred"
                        varo=0
                fi;
        elif [ "$video" = "12" ]                                     #mp4 en hevc
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                 if [ "$?" = "0" ]; then
                    mp44=$(find $FILE -name "*.mp4")
                            if [ -n "$mp44" ]; then
                                clear
                                echo "Conversion in progress ..."
                                for v in $FILE $mp44; do ffmpeg -i "$v" -c:v libx265 -c:a aac "${v%.mp4}.hevc"> /dev/null 2>&1; done
                                encov=flv
                                varo=1
                            else
                                zenity --error --text="No compatible files found in the selected directory"
                                var=0
                            fi;
                elif [ "$?" = "1" ]                           
                    then
                        zenity --error --text="No files selected"
                        varo=0
                else 
                        zenity --error --text="An unexpected error has occurred"
                        varo=0
                fi;
        elif [ "$video" = "13" ]                                     #mov en mkv
            then        
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                 if [ "$?" = "0" ]; then
                    movv=$(find $FILE -name "*.mov")
                            if [ -n "$movv" ]; then
                                clear
                                echo "Conversion in progress ..."                             
                                for z in $movv; do ffmpeg -i "$z" -codec copy "${z%.mov}.mkv"> /dev/null 2>&1; done
                                encov=mkv
                                varo=1
                            else
                                zenity --error --text="No compatible files found in the selected directory"
                                var=0
                            fi;
                elif [ "$?" = "1" ]                           
                    then
                        zenity --error --text="No files selected"
                        varo=0
                else 
                        zenity --error --text="An unexpected error has occurred"
                        varo=0
                fi;
        elif [ "$video" = "14" ]                                     #mov en mp4
            then        
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                 if [ "$?" = "0" ]; then
                    movv=$(find $FILE -name "*.mov")
                            if [ -n "$movv" ]; then
                                clear
                                echo "Conversion in progress ..."       
                                for aa in $mp44; do  ffmpeg -i "$aa" -codec copy "${aa%.mov}.mp4"> /dev/null 2>&1; done
                                encov=mp4
                                varo=1
                            else
                                zenity --error --text="No compatible files found in the selected directory"
                                var=0
                            fi;
                elif [ "$?" = "1" ]                           
                    then
                        zenity --error --text="No files selected"
                        varo=0
                else 
                        zenity --error --text="An unexpected error has occurred"
                        varo=0
                fi;
        elif [ "$video" = "15" ]                                     #mov en avi
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                 if [ "$?" = "0" ]; then
                    movv=$(find $FILE -name "*.mov")
                            if [ -n "$movv" ]; then
                                clear
                                echo "Conversion in progress ..."
                                for bb in $movv; do ffmpeg -i "$bb" -codec copy "${bb%.mov}.avi"> /dev/null 2>&1; done
                                encov=avi
                                varo=1
                            else
                                zenity --error --text="No compatible files found in the selected directory"
                                var=0
                            fi;
                elif [ "$?" = "1" ]                           
                    then
                        zenity --error --text="No files selected"
                        varo=0
                else 
                        zenity --error --text="An unexpected error has occurred"
                        varo=0
                fi;
        elif [ "$video" = "16" ]                                     #mov en webm
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                 if [ "$?" = "0" ]; then
                    movv=$(find $FILE -name "*.mov")
                            if [ -n "$movv" ]; then
                                clear
                                echo "Conversion in progress ..."
                                for v in $FILE $movv; do ffmpeg -i "$v" -c:v libvpx -c:a libvorbis "${v%.mov}.webm"> /dev/null 2>&1; done
                                encov=webm
                                varo=1
                            else
                                zenity --error --text="No compatible files found in the selected directory"
                                var=0
                            fi;
                elif [ "$?" = "1" ]                           
                    then
                        zenity --error --text="No files selected"
                        varo=0
                else 
                        zenity --error --text="An unexpected error has occurred"
                        varo=0
                fi;
        elif [ "$video" = "17" ]                                     #mov en flv
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                 if [ "$?" = "0" ]; then
                    movv=$(find $FILE -name "*.mov")
                            if [ -n "$movv" ]; then
                                clear
                                echo "Conversion in progress ..."
                                for v in $FILE $movv; do ffmpeg -i "$v" -c:v flv -c:a mp3 "${v%.mov}.flv"> /dev/null 2>&1; done
                                encov=flv
                                varo=1
                            else
                                zenity --error --text="No compatible files found in the selected directory"
                                var=0
                            fi;
                elif [ "$?" = "1" ]                           
                    then
                        zenity --error --text="No files selected"
                        varo=0
                else 
                        zenity --error --text="An unexpected error has occurred"
                        varo=0
                fi;
        elif [ "$video" = "18" ]                                     #mov en hevc
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                 if [ "$?" = "0" ]; then
                    movv=$(find $FILE -name "*.mov")
                            if [ -n "$movv" ]; then
                                clear
                                echo "Conversion in progress ..."
                                for v in $FILE $movv; do ffmpeg -i "$v" -c:v libx265 -c:a aac "${v%.mov}.hevc"> /dev/null 2>&1; done
                                encov=flv
                                varo=1
                            else
                                zenity --error --text="No compatible files found in the selected directory"
                                var=0
                            fi;
                elif [ "$?" = "1" ]                           
                    then
                        zenity --error --text="No files selected"
                        varo=0
                else 
                        zenity --error --text="An unexpected error has occurred"
                        varo=0
                fi;
        elif [ "$video" = "19" ]                                     #avi en mkv
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                 if [ "$?" = "0" ]; then
                    avii=$(find $FILE -name "*.avi")
                            if [ -n "$avii" ]; then
                                clear
                                echo "Conversion in progress ..."
                                for cc in $avii; do ffmpeg -i "$cc" -codec copy "${cc%.avi}.mkv"> /dev/null 2>&1; done
                                encov=mkv
                                varo=1
                            else
                                zenity --error --text="No compatible files found in the selected directory"
                                var=0
                            fi;
                elif [ "$?" = "1" ]                           
                    then
                        zenity --error --text="No files selected"
                        varo=0
                else 
                        zenity --error --text="An unexpected error has occurred"
                        varo=0
                fi;
        elif [ "$video" = "20" ]                                     #avi en mp4
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                 if [ "$?" = "0" ]; then
                    avii=$(find $FILE -name "*.avi")
                            if [ -n "$avii" ]; then
                                clear
                                echo "Conversion in progress ..."
                                for dd in $avii; do ffmpeg -i "$dd" -codec copy "${dd%.avi}.mp4"> /dev/null 2>&1; done
                                encov=mp4
                                varo=1
                            else
                                zenity --error --text="No compatible files found in the selected directory"
                                var=0
                            fi;
                elif [ "$?" = "1" ]                           
                    then
                        zenity --error --text="No files selected"
                        varo=0
                else 
                        zenity --error --text="An unexpected error has occurred"
                        varo=0
                fi;
        elif [ "$video" = "21" ]                                     #avi en mov
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                 if [ "$?" = "0" ]; then
                    avii=$(find $FILE -name "*.avi")
                            if [ -n "$avii" ]; then
                                clear
                                echo "Conversion in progress ..." 
                                for ee in $avii; do ffmpeg -i "$ee" -codec copy "${ee%.avi}.mov"> /dev/null 2>&1; done
                                encov=mov
                                varo=1
                            else
                                zenity --error --text="No compatible files found in the selected directory"
                                var=0
                            fi;
                elif [ "$?" = "1" ]                           
                    then
                        zenity --error --text="No files selected"
                        varo=0
                else 
                        zenity --error --text="An unexpected error has occurred"
                        varo=0
                fi;
        elif [ "$video" = "22" ]                                     #avi en webm
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                 if [ "$?" = "0" ]; then
                    avii=$(find $FILE -name "*.avi")
                            if [ -n "$avii" ]; then
                                clear
                                echo "Conversion in progress ..."
                                for v in $FILE $avii; do ffmpeg -i "$v" -c:v libvpx -c:a libvorbis "${v%.avi}.webm"> /dev/null 2>&1; done
                                encov=webm
                                varo=1
                            else
                                zenity --error --text="No compatible files found in the selected directory"
                                var=0
                            fi;
                elif [ "$?" = "1" ]                           
                    then
                        zenity --error --text="No files selected"
                        varo=0
                else 
                        zenity --error --text="An unexpected error has occurred"
                        varo=0
                fi;
        elif [ "$video" = "23" ]                                     #avi en flv
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                 if [ "$?" = "0" ]; then
                    avii=$(find $FILE -name "*.avi")
                            if [ -n "$avii" ]; then
                                clear
                                echo "Conversion in progress ..."
                                for v in $FILE $avii; do ffmpeg -i "$v" -c:v flv -c:a mp3 "${v%.avi}.flv"> /dev/null 2>&1; done
                                encov=flv
                                varo=1
                            else
                                zenity --error --text="No compatible files found in the selected directory"
                                var=0
                            fi;
                elif [ "$?" = "1" ]                           
                    then
                        zenity --error --text="No files selected"
                        varo=0
                else 
                        zenity --error --text="An unexpected error has occurred"
                        varo=0
                fi;
        elif [ "$video" = "24" ]                                     #avi en hevc
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                 if [ "$?" = "0" ]; then
                    avii=$(find $FILE -name "*.avi")
                            if [ -n "$avii" ]; then
                                clear
                                echo "Conversion in progress ..."
                                for v in $FILE $avii; do ffmpeg -i "$v" -c:v libx265 -c:a aac "${v%.avi}.hevc"> /dev/null 2>&1; done
                                encov=flv
                                varo=1
                            else
                                zenity --error --text="No compatible files found in the selected directory"
                                var=0
                            fi;
                elif [ "$?" = "1" ]                           
                    then
                        zenity --error --text="No files selected"
                        varo=0
                else 
                        zenity --error --text="An unexpected error has occurred"
                        varo=0
                fi;
        elif [ "$video" = "25" ]                                     #webm en avi
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                    if [ "$?" = "0" ]; then
                    webmm=$(find $FILE -name "*.webm")
                            if [ -n "$webmm" ]; then
                                clear
                                echo "Conversion in progress ..."
                                for t in $webmm; do ffmpeg -i "$t" -codec copy "${t%.webm}.avi"> /dev/null 2>&1; done
                                encov=avi
                                varo=1
                            else
                                zenity --error --text="No compatible files found in the selected directory"
                                var=0
                            fi;
                elif [ "$?" = "1" ]                           
                    then
                        zenity --error --text="No files selected"
                        varo=0
                else 
                        zenity --error --text="An unexpected error has occurred"
                        varo=0
                fi;
        elif [ "$video" = "26" ]                                     #webm en mkv
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                 if [ "$?" = "0" ]; then
                    webmm=$(find $FILE -name "*.webm")
                            if [ -n "$webmmm" ]; then
                                clear
                                echo "Conversion in progress ..."
                                for cc in $webmmm; do ffmpeg -i "$cc" -codec copy "${cc%.webm}.mkv"> /dev/null 2>&1; done
                                encov=mkv
                                varo=1
                            else
                                zenity --error --text="No compatible files found in the selected directory"
                                var=0
                            fi;
                elif [ "$?" = "1" ]                           
                    then
                        zenity --error --text="No files selected"
                        varo=0
                else 
                        zenity --error --text="An unexpected error has occurred"
                        varo=0
                fi;
        elif [ "$video" = "27" ]                                   #webm en mov
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                    if [ "$?" = "0" ]; then
                    webmm=$(find $FILE -name "*.webm")
                            if [ -n "$webmm" ]; then
                                clear
                                echo "Conversion in progress ..."
                                for u in $webmm; do ffmpeg -i "$u" -codec copy "${u%.webm}.mov"> /dev/null 2>&1; done
                                encov=mov
                                varo=1
                            else
                                zenity --error --text="No compatible files found in the selected directory"
                                var=0
                            fi;
                elif [ "$?" = "1" ]                           
                    then
                        zenity --error --text="No files selected"
                        varo=0
                else 
                        zenity --error --text="An unexpected error has occurred"
                        varo=0
                fi;
        elif [ "$video" = "28" ]                                     #webm en mp4
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                 if [ "$?" = "0" ]; then
                    webmm=$(find $FILE -name "*.webm")
                            if [ -n "$webmm" ]; then
                                clear
                                echo "Conversion in progress ..."
                                for v in $FILE $webmm; do ffmpeg -i "$v" -codec copy "${v%.webm}.mp4"> /dev/null 2>&1; done
                                encov=mp4
                                varo=1
                            else
                                zenity --error --text="No compatible files found in the selected directory"
                                var=0
                            fi;
                elif [ "$?" = "1" ]                           
                    then
                        zenity --error --text="No files selected"
                        varo=0
                else 
                        zenity --error --text="An unexpected error has occurred"
                        varo=0
                fi;
        elif [ "$video" = "29" ]                                     #webm en flv
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                 if [ "$?" = "0" ]; then
                    webmm=$(find $FILE -name "*.webm")
                            if [ -n "$webmm" ]; then
                                clear
                                echo "Conversion in progress ..."
                                for v in $FILE $webmm; do ffmpeg -i "$v" -c:v flv -c:a mp3 "${v%.webm}.flv"> /dev/null 2>&1; done
                                encov=flv
                                varo=1
                            else
                                zenity --error --text="No compatible files found in the selected directory"
                                var=0
                            fi;
                elif [ "$?" = "1" ]                           
                    then
                        zenity --error --text="No files selected"
                        varo=0
                else 
                        zenity --error --text="An unexpected error has occurred"
                        varo=0
                fi;
        elif [ "$video" = "30" ]                                     #webm en hevc
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                 if [ "$?" = "0" ]; then
                    webmm=$(find $FILE -name "*.webm")
                            if [ -n "$webmm" ]; then
                                clear
                                echo "Conversion in progress ..."
                                for v in $FILE $webmm; do ffmpeg -i "$v" -c:v libx265 -c:a aac "${v%.webm}.hevc"> /dev/null 2>&1; done
                                encov=flv
                                varo=1
                            else
                                zenity --error --text="No compatible files found in the selected directory"
                                var=0
                            fi;
                elif [ "$?" = "1" ]                           
                    then
                        zenity --error --text="No files selected"
                        varo=0
                else 
                        zenity --error --text="An unexpected error has occurred"
                        varo=0
                fi;
        elif [ "$video" = "31" ]                                     #hevc en avi
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                    if [ "$?" = "0" ]; then
                    hevcc=$(find $FILE -name "*.hevc")
                            if [ -n "$hevcc" ]; then
                                clear 
                                echo "Conversion in progress ..."
                                for t in $hevcc; do ffmpeg -i "$t" -codec copy "${t%.hevc}.avi"> /dev/null 2>&1; done
                                encov=avi
                                varo=1
                            else
                                zenity --error --text="No compatible files found in the selected directory"
                                var=0
                            fi;
                elif [ "$?" = "1" ]                           
                    then
                        zenity --error --text="No files selected"
                        varo=0
                else 
                        zenity --error --text="An unexpected error has occurred"
                        varo=0
                fi;
        elif [ "$video" = "32" ]                                     #hevc en mkv
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                 if [ "$?" = "0" ]; then
                    hevcc=$(find $FILE -name "*.hevc")
                            if [ -n "$hevccm" ]; then
                                clear
                                echo "Conversion in progress ..." 
                                for cc in $hevccm; do ffmpeg -i "$cc" -codec copy "${cc%.hevc}.mkv"> /dev/null 2>&1; done
                                encov=mkv
                                varo=1
                            else
                                zenity --error --text="No compatible files found in the selected directory"
                                var=0
                            fi;
                elif [ "$?" = "1" ]                           
                    then
                        zenity --error --text="No files selected"
                        varo=0
                else 
                        zenity --error --text="An unexpected error has occurred"
                        varo=0
                fi;
        elif [ "$video" = "33" ]                                   #hevc en mov
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                    if [ "$?" = "0" ]; then
                    hevcc=$(find $FILE -name "*.hevc")
                            if [ -n "$hevcc" ]; then
                                clear
                                echo "Conversion in progress ..."
                                for u in $hevcc; do ffmpeg -i "$u" -codec copy "${u%.hevc}.mov"> /dev/null 2>&1; done
                                encov=mov
                                varo=1
                            else
                                zenity --error --text="No compatible files found in the selected directory"
                                var=0
                            fi;
                elif [ "$?" = "1" ]                           
                    then
                        zenity --error --text="No files selected"
                        varo=0
                else 
                        zenity --error --text="An unexpected error has occurred"
                        varo=0
                fi;
        elif [ "$video" = "34" ]                                     #hevc en mp4
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                 if [ "$?" = "0" ]; then
                    hevcc=$(find $FILE -name "*.hevc")
                            if [ -n "$hevcc" ]; then
                                clear
                                echo "Conversion in progress ..."
                                for v in $FILE $hevcc; do ffmpeg -i "$v" -codec copy "${v%.hevc}.mp4"> /dev/null 2>&1; done
                                encov=mp4
                                varo=1
                            else
                                zenity --error --text="No compatible files found in the selected directory"
                                var=0
                            fi;
                elif [ "$?" = "1" ]                           
                    then
                        zenity --error --text="No files selected"
                        varo=0
                else 
                        zenity --error --text="An unexpected error has occurred"
                        varo=0
                fi;
        elif [ "$video" = "35" ]                                     #hevc en flv
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                 if [ "$?" = "0" ]; then
                    hevcc=$(find $FILE -name "*.hevc")
                            if [ -n "$hevcc" ]; then
                                clear
                                echo "Conversion in progress ..."
                                for v in $FILE $hevcc; do ffmpeg -i "$v" -c:v flv -c:a mp3 "${v%.hevc}.flv"> /dev/null 2>&1; done
                                encov=flv
                                varo=1
                            else
                                zenity --error --text="No compatible files found in the selected directory"
                                var=0
                            fi;
                elif [ "$?" = "1" ]                           
                    then
                        zenity --error --text="No files selected"
                        varo=0
                else 
                        zenity --error --text="An unexpected error has occurred"
                        varo=0
                fi;
        elif [ "$video" = "36" ]                                     #hevc en webm
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                 if [ "$?" = "0" ]; then
                    hevcc=$(find $FILE -name "*.hevc")
                            if [ -n "$hevcc" ]; then
                                clear
                                echo "Conversion in progress ..."
                                for v in $FILE $hevcc; do ffmpeg -i "$v" -c:v libvpx -c:a libvorbis "${v%.hevc}.webm"> /dev/null 2>&1; done
                                encov=webm
                                varo=1
                            else
                                zenity --error --text="No compatible files found in the selected directory"
                                var=0
                            fi;
                elif [ "$?" = "1" ]                           
                    then
                        zenity --error --text="No files selected"
                        varo=0
                else 
                        zenity --error --text="An unexpected error has occurred"
                        varo=0
                fi;
        elif [ "$video" = "37" ]                                     #flv en avi
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                    if [ "$?" = "0" ]; then
                    flvv=$(find $FILE -name "*.flv")
                            if [ -n "$flvv" ]; then
                                clear
                                echo "Conversion in progress ..." 
                                for t in $flvv; do ffmpeg -i "$t" -codec copy "${t%.flv}.avi"> /dev/null 2>&1; done
                                encov=avi
                                varo=1
                            else
                                zenity --error --text="No compatible files found in the selected directory"
                                var=0
                            fi;
                elif [ "$?" = "1" ]                           
                    then
                        zenity --error --text="No files selected"
                        varo=0
                else 
                        zenity --error --text="An unexpected error has occurred"
                        varo=0
                fi;
        elif [ "$video" = "38" ]                                     #flv en mkv
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                 if [ "$?" = "0" ]; then
                    flvv=$(find $FILE -name "*.flv")
                            if [ -n "$flvvm" ]; then
                                clear
                                echo "Conversion in progress ..." 
                                for cc in $flvvm; do ffmpeg -i "$cc" -codec copy "${cc%.flv}.mkv"> /dev/null 2>&1; done
                                encov=mkv
                                varo=1
                            else
                                zenity --error --text="No compatible files found in the selected directory"
                                var=0
                            fi;
                elif [ "$?" = "1" ]                           
                    then
                        zenity --error --text="No files selected"
                        varo=0
                else 
                        zenity --error --text="An unexpected error has occurred"
                        varo=0
                fi;
        elif [ "$video" = "39" ]                                   #flv en mov
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                    if [ "$?" = "0" ]; then
                    flvv=$(find $FILE -name "*.flv")
                            if [ -n "$flvv" ]; then
                                clear
                                echo "Conversion in progress ..."
                                for u in $flvv; do ffmpeg -i "$u" -codec copy "${u%.flv}.mov"> /dev/null 2>&1; done
                                encov=mov
                                varo=1
                            else
                                zenity --error --text="No compatible files found in the selected directory"
                                var=0
                            fi;
                elif [ "$?" = "1" ]                           
                    then
                        zenity --error --text="No files selected"
                        varo=0
                else 
                        zenity --error --text="An unexpected error has occurred"
                        varo=0
                fi;
        elif [ "$video" = "40" ]                                     #flv en mp4
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                 if [ "$?" = "0" ]; then
                    flvv=$(find $FILE -name "*.flv")
                            if [ -n "$flvv" ]; then
                                clear
                                echo "Conversion in progress ..."
                                for v in $FILE $flvv; do ffmpeg -i "$v" -codec copy "${v%.flv}.mp4"> /dev/null 2>&1; done
                                encov=mp4
                                varo=1
                            else
                                zenity --error --text="No compatible files found in the selected directory"
                                var=0
                            fi;
                elif [ "$?" = "1" ]                           
                    then
                        zenity --error --text="No files selected"
                        varo=0
                else 
                        zenity --error --text="An unexpected error has occurred"
                        varo=0
                fi;
        elif [ "$video" = "41" ]                                     #flv en hevc
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                 if [ "$?" = "0" ]; then
                    flvv=$(find $FILE -name "*.flv")
                            if [ -n "$flvv" ]; then
                                clear
                                echo "Conversion in progress ..."
                                for v in $FILE $flvv; do ffmpeg -i "$v" -c:v libx265 -c:a aac "${v%.webm}.flv"> /dev/null 2>&1; done
                                encov=flv
                                varo=1
                            else
                                zenity --error --text="No compatible files found in the selected directory"
                                var=0
                            fi;
                elif [ "$?" = "1" ]                           
                    then
                        zenity --error --text="No files selected"
                        varo=0
                else 
                        zenity --error --text="An unexpected error has occurred"
                        varo=0
                fi;
        elif [ "$video" = "42" ]                                     #flv en webm
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                 if [ "$?" = "0" ]; then
                    flvv=$(find $FILE -name "*.flv")
                            if [ -n "$flvv" ]; then
                                clear
                                echo "Conversion in progress ..."
                                for v in $FILE $flvv; do ffmpeg -i "$v" -c:v libvpx -c:a libvorbis "${v%.flv}.webm"> /dev/null 2>&1; done
                                encov=webm
                                varo=1
                            else
                                zenity --error --text="No compatible files found in the selected directory"
                                var=0
                            fi;
                elif [ "$?" = "1" ]                           
                    then
                        zenity --error --text="No files selected"
                        varo=0
                else 
                        zenity --error --text="An unexpected error has occurred"
                        varo=0
                fi;
        elif [ "$video" = "43" ]
            then
               varo=1
        else
            zenity --error --text="Please enter a number between 1 and 14"
            varo=0
        fi;
done
whiptail --textbox --title "Process finished successfully" --msgbox "Your files have been re-encoded in $enco in your current foldert" 10 80
}

function convertisso-audio {
clear
var=0
while [ $var = 0 ];do
AUDIO=$(whiptail --title "Convertisso audio menu" --menu "Choose an option" 40 90 20 \
"1" "mp3 to ogg" \
"2" "mp3 to aac" \
"3" "mp3 to ac3" \
"4" "mp3 to wav" \
"5" "mp3 to opus" \
"6" "mp3 to vorbis" \
"7" "wav to mp3" \
"8" "wav to ogg" \
"9" "wav to aac" \
"10" "wav to ac3" \
"11" "wav to opus" \
"12" "wav to vorbis" \
"13" "ogg to mp3" \
"14" "ogg to wav" \
"15" "ogg to aac" \
"16" "ogg to ac3" \
"17" "ogg to opus" \
"18" "ogg to vorbis" \
"19" "ac3 to mp3" \
"20" "ac3 to wav" \
"21" "ac3 to aac" \
"22" "ac3 to ogg" \
"23" "ac3 to opus" \
"24" "ac3 to vorbis" \
"25" "aac to wav" \
"26" "aac to ac3" \
"27" "aac to ogg" \
"28" "aac to mp3" \
"29" "aac to opus" \
"30" "aac to vorbis" \
"31" "flac to mp3" \
"32" "flac to wav" \
"33" "flac to ogg" \
"34" "flac to ac3" \
"35" "flac to opus" \
"36" "flac to vorbis" \
"37" "opus to mp3" \
"38" "opus to ogg" \
"39" "opus to ac3" \
"40" "opus to aac" \
"41" "opus to flac" \
"42" "opus to wav" \
"43" "opus to vorbis" \
"44" "vorbis to mp3" \
"45" "vorbis to ogg" \
"46" "vorbis to ac3" \
"47" "vorbis to aac" \
"48" "vorbis to flac" \
"49" "vorbis to wav" \
"50" "EXIT" 3>&1 1>&2 2>&3)
        if [ "$AUDIO" = "1" ]
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                    if [ "$?" = "0" ]; then
                    mp33=$(find $FILE -name "*.mp3")
                            if [ -n "$mp33" ]; then
                                clear
                                echo "Conversion in progress ..."
                                for b in $mp33; do ffmpeg -i "$b" -map_metadata 0 -c:a libvorbis "${b/%mp3}.ogg"> /dev/null 2>&1; done #convertis les fichiers MP3 en OGG
                                enco=ogg
                                var=1
                            else
                                zenity --error --text="No compatible files found in the selected directory"
                                var=0
                            fi;
                    elif [ "$?" = "1" ]                           
                        then
                            zenity --error --text="No files selected"
                            var=0
                    else 
                        zenity --error --text="An unexpected error has occurred"
                        var=0
                    fi;
        elif [ "$AUDIO" = "2" ]                                   #mp3 en aac
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                if [ "$?" = "0" ]; then
                mp33=$(find $FILE -name "*.mp3")
                    if [ -n "$mp33" ]; then
                        clear
                        echo "Conversion in progress ..."
                        for c in $mp33; do ffmpeg -i "$c" -map_metadata 0 -c:a aac "${c%.mp3}.aac"> /dev/null 2>&1; done
                        enco=aac
                        var=1
                    else
                        zenity --error --text="No compatible files found in the selected directory"
                        var=0
                    fi;
                elif [ "$?" = "1" ]; then
                    zenity --error --text="No files selected"
                    var=0
                else
                    zenity --error --text="An unexpected error has occurred"
                    var=0
                fi;
        elif [ "$AUDIO" = "3" ]                             
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                    if [ "$?" = "0" ]; then
                    mp33=$(find $FILE -name "*.mp3")
                            if [ -n "$mp33" ]; then
                                clear
                                for a in $mp33 ; do ffmpeg -i "$a" -map_metadata 0 "${a%.mp3}.wav"> /dev/null 2>&1; done
                                enco=wav
                                var=1
                            else
                                zenity --error --text="No compatible files found in the selected directory"
                                var=0
                            fi;
                    elif [ "$?" = "1" ]                           
                        then
                            zenity --error --text="No files selected"
                            var=0
                    else 
                            zenity --error --text="An unexpected error has occurred"
                            var=0
                    fi;
        elif [ "$AUDIO" = "4" ]                                   #mp3 en ac3
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                if [ "$?" = "0" ]; then
                mp33=$(find $FILE -name "*.mp3")
                        if [ -n "$mp33" ]; then
                            clear
                            echo "Conversion in progress ..."
                            for m in $mp33; do ffmpeg -i "$m" -map_metadata 0 -c:a ac3 "${m%.mp3}.ac3"> /dev/null 2>&1; done 
                            enco=ac3
                            var=1
                        else
                            zenity --error --text="No compatible files found in the selected directory"
                            var=0
                        fi;
                elif [ "$?" = "1" ]                           
                    then
                        zenity --error --text="No files selected"
                        var=0
                else 
                        zenity --error --text="An unexpected error has occurred"
                        var=0
                fi;
        elif [ "$AUDIO" = "5" ]                                   #mp3 en opus
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                if [ "$?" = "0" ]; then
                mp33=$(find $FILE -name "*.mp3")
                        if [ -n "$mp33" ]; then
                            clear
                            echo "Conversion in progress ..."
                            for m in $mp33; do ffmpeg -i "$m" -map_metadata 0 -c:a libopus "${m%.mp3}.opus"> /dev/null 2>&1; done 
                            enco=ac3
                            var=1
                        else
                            zenity --error --text="No compatible files found in the selected directory"
                            var=0
                        fi;
                elif [ "$?" = "1" ]                           
                    then
                        zenity --error --text="No files selected"
                        var=0
                else 
                        zenity --error --text="An unexpected error has occurred"
                        var=0
                fi;
        elif [ "$AUDIO" = "6" ]                                   #mp3 en vorbis
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                if [ "$?" = "0" ]; then
                mp33=$(find $FILE -name "*.mp3")
                        if [ -n "$mp33" ]; then
                            clear
                            echo "Conversion in progress ..."
                            for m in $mp33; do ffmpeg -i "$m" -map_metadata 0 -c:a libvorbis "${m%.mp3}.vorbis"> /dev/null 2>&1; done 
                            enco=ac3
                            var=1
                        else
                            zenity --error --text="No compatible files found in the selected directory"
                            var=0
                        fi;
                elif [ "$?" = "1" ]                           
                    then
                        zenity --error --text="No files selected"
                        var=0
                else 
                        zenity --error --text="An unexpected error has occurred"
                        var=0
                fi;
        elif [ "$AUDIO" = "7" ]                                   #wav en mp3
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                if [ "$?" = "0" ]; then
                wavv=$(find $FILE -name "*.wav")
                        if [ -n "$wavv" ]; then
                            clear
                            echo "Conversion in progress ..."
                            for d in $wavv; do ffmpeg -i "$d" -map_metadata 0 -f mp3 "${d%.waw}.mp3"> /dev/null 2>&1; done
                            enco=mp3
                            var=1
                        else
                            zenity --error --text="No compatible files found in the selected directory"
                            var=0
                        fi;
                elif [ "$?" = "1" ]                           
                    then
                        zenity --error --text="No files selected"
                        var=0
                else 
                        zenity --error --text="An unexpected error has occurred"
                        var=0
                fi;
        elif [ "$AUDIO" = "8" ]                                       #wav en ogg
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                if [ "$?" = "0" ]; then
                wavv=$(find $FILE -name "*.wav")
                        if [ -n "$wavv" ]; then
                            clear
                            echo "conversion in progress ..."
                            for h in $wavv; do ffmpeg -i "$h" -map_metadata 0 -c:a libvorbis "${h%.waw}.ogg"> /dev/null 2>&1; done 
                            enco=ogg
                            var=1
                        else
                            zenity --error --text="No compatible files found in the selected directory"
                            var=0
                        fi;
                elif [ "$?" = "1" ]                           
                    then
                        zenity --error --text="No files selected"
                        var=0
                else 
                        zenity --error --text="An unexpected error has occurred"
                        var=0
                fi;
        elif [ "$AUDIO" = "9" ]                                    #wav en aac
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                if [ "$?" = "0" ]; then
                wavv=$(find $FILE -name "*.wav")
                        if [ -n "$wavv" ]; then
                            clear
                            echo "conversion in progress ..."
                            for i in $wavv; do ffmpeg -i "$i" -map_metadata 0 -c:a libfaac "${i%.waw}.aac"> /dev/null 2>&1; done 
                            enco=aac
                            var=1
                        else
                            zenity --error --text="No compatible files found in the selected directory"
                            var=0
                        fi;
                elif [ "$?" = "1" ]                           
                    then
                        zenity --error --text="No files selected"
                        var=0
                else 
                        zenity --error --text="An unexpected error has occurred"
                        var=0
                fi;
        elif [ "$AUDIO" = "10" ]                                   #wav en ac3
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                if [ "$?" = "0" ]; then
                wavv=$(find $FILE -name "*.wav")
                        if [ -n "$wavv" ]; then
                            clear
                            echo "conversion in progress ..."
                            for j in $wavv; do ffmpeg -i "$j" -map_metadata 0 -c:a libmp3lame "${j%.waw}.ac3"> /dev/null 2>&1; done 
                            enco=ac3
                            var=1
                        else
                            zenity --error --text="No compatible files found in the selected directory"
                            var=0
                        fi;
                elif [ "$?" = "1" ]                           
                    then
                        zenity --error --text="No files selected"
                        var=0
                else 
                        zenity --error --text="An unexpected error has occurred"
                        var=0
                fi;
        elif [ "$AUDIO" = "11" ]                                   #wav en opus
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                if [ "$?" = "0" ]; then
                wavv=$(find $FILE -name "*.wav")
                        if [ -n "$wavv" ]; then
                            clear
                            echo "conversion in progress ..."
                            for j in $wavv; do ffmpeg -i "$j" -map_metadata 0 -c:a libopus "${j%.waw}.opus"> /dev/null 2>&1; done 
                            enco=ac3
                            var=1
                        else
                            zenity --error --text="No compatible files found in the selected directory"
                            var=0
                        fi;
                elif [ "$?" = "1" ]                           
                    then
                        zenity --error --text="No files selected"
                        var=0
                else 
                        zenity --error --text="An unexpected error has occurred"
                        var=0
                fi;
        elif [ "$AUDIO" = "12" ]                                   #wav en vorbis
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                if [ "$?" = "0" ]; then
                wavv=$(find $FILE -name "*.wav")
                        if [ -n "$wavv" ]; then
                            clear
                            echo "conversion in progress ..."
                            for j in $wavv; do ffmpeg -i "$j" -map_metadata 0 -c:a libvorbis "${j%.waw}.vorbis"> /dev/null 2>&1; done 
                            enco=ac3
                            var=1
                        else
                            zenity --error --text="No compatible files found in the selected directory"
                            var=0
                        fi;
                elif [ "$?" = "1" ]                           
                    then
                        zenity --error --text="No files selected"
                        var=0
                else 
                        zenity --error --text="An unexpected error has occurred"
                        var=0
                fi;

        elif [ "$AUDIO" = "13" ]                                   #ogg en mp3 
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                if [ "$?" = "0" ]; then
                oggg=$(find $FILE -iname "*.ogg")
                        if [ -n "$oggg" ]; then
                            clear
                            echo "conversion in progress ..."
                            for g in $oggg ; do ffmpeg -i "$g" -map_metadata 0 -c:a libmp3lame "${g%.ogg}.mp3"> /dev/null 2>&1; done #convertis les fichiers OGG en MP3
                            enco=mp3
                            var=1
                        else
                            zenity --error --text="No compatible files found in the selected directory"
                            var=0
                        fi;
                elif [ "$?" = "1" ]                           
                    then
                        zenity --error --text="No files selected"
                        var=0
                else 
                        zenity --error --text="An unexpected error has occurred"
                        var=0
                fi;
        elif [ "$AUDIO" = "14" ]                                   #ogg en wav
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                if [ "$?" = "0" ]; then
                oggg=$(find $FILE -name "*.ogg")
                        if [ -n "$oggg" ]; then
                            clear
                            echo "conversion in progress ..."
                            for k in $oggg; do ffmpeg -i "$k" -map_metadata 0 "${k%.ogg}.wav"> /dev/null 2>&1; done 
                            enco=wav
                            var=1
                        else
                            zenity --error --text="No compatible files found in the selected directory"
                            var=0
                        fi;
                elif [ "$?" = "1" ]
                    then
                        zenity --error --text="No files selected"
                        var=0
                else 
                        zenity --error --text="An unexpected error has occurred"
                        var=0
                fi;
        elif [ "$AUDIO" = "15" ]                                   #ogg en aac
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                if [ "$?" = "0" ]; then
                oggg=$(find $FILE -name "*.ogg")
                        if [ -n "$oggg" ]; then
                            clear
                            echo "conversion in progress ..."
                            for l in $oggg; do ffmpeg -i "$l" -map_metadata 0 -c:a libfaac "${l%.ogg}.aac"> /dev/null 2>&1; done 
                            enco=aac
                            var=1
                        else
                            zenity --error --text="No compatible files found in the selected directory"
                            var=0
                        fi;
                elif [ "$?" = "1" ]
                    then
                        zenity --error --text="No files selected"
                        var=0
                else 
                        zenity --error --text="An unexpected error has occurred"
                        var=0
                fi;
        elif [ "$AUDIO" = "16" ]                                   #ogg en ac3
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                if [ "$?" = "0" ]; then
                oggg=$(find $FILE -name "*.ogg")
                        if [ -n "$oggg" ]; then
                            clear
                            echo "conversion in progress ..."
                            for m in $oggg; do ffmpeg -i "$m" -map_metadata 0 -c:a ac3 "${m%.ogg}.ac3"> /dev/null 2>&1; done 
                            enco=ac3
                            var=1
                        else
                            zenity --error --text="No compatible files found in the selected directory"
                            var=0
                        fi;
                elif [ "$?" = "1" ]                           
                    then
                        zenity --error --text="No files selected"
                        var=0
                else 
                        zenity --error --text="An unexpected error has occurred"
                        var=0
                fi;
        elif [ "$AUDIO" = "17" ]                                   #ogg en opus
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                if [ "$?" = "0" ]; then
                oggg=$(find $FILE -name "*.ogg")
                        if [ -n "$oggg" ]; then
                            clear
                            echo "conversion in progress ..."
                            for m in $oggg; do ffmpeg -i "$m" -map_metadata 0 -c:a libopus "${m%.ogg}.opus"> /dev/null 2>&1; done 
                            enco=ac3
                            var=1
                        else
                            zenity --error --text="No compatible files found in the selected directory"
                            var=0
                        fi;
                elif [ "$?" = "1" ]                           
                    then
                        zenity --error --text="No files selected"
                        var=0
                else 
                        zenity --error --text="An unexpected error has occurred"
                        var=0
                fi;
        elif [ "$AUDIO" = "18" ]                                   #ogg en vorbis
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                if [ "$?" = "0" ]; then
                oggg=$(find $FILE -name "*.ogg")
                        if [ -n "$oggg" ]; then
                            clear
                            echo "conversion in progress ..."
                            for m in $oggg; do ffmpeg -i "$m" -map_metadata 0 -c:a libvorbis "${m%.ogg}.vorbis"> /dev/null 2>&1; done 
                            enco=ac3
                            var=1
                        else
                            zenity --error --text="No compatible files found in the selected directory"
                            var=0
                        fi;
                elif [ "$?" = "1" ]                           
                    then
                        zenity --error --text="No files selected"
                        var=0
                else 
                        zenity --error --text="An unexpected error has occurred"
                        var=0
                fi;
        elif [ "$AUDIO" = "19" ]                                   #ac3 en mp3
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                if [ "$?" = "0" ]; then
                ac33=$(find $FILE -name "*.ac3")
                        if [ -n "$ac33" ]; then
                            clear
                            echo "conversion in progress ..."
                            for f in $ac33; do ffmpeg -i "$f" -map_metadata 0 -c:a libmp3lame "${f%.ac3}.mp3"> /dev/null 2>&1; done
                            enco=mp3
                            var=1
                        else
                            zenity --error --text="No compatible files found in the selected directory"
                            var=0
                        fi;
                elif [ "$?" = "1" ]                           
                    then
                        zenity --error --text="No files selected"
                        var=0
                else 
                        zenity --error --text="An unexpected error has occurred"
                        var=0
                fi;
        elif [ "$AUDIO" = "20" ]                                   #ac3 en wav
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                if [ "$?" = "0" ]; then
                ac33=$(find $FILE -name "*.ac3")
                        if [ -n "$ac33" ]; then
                            clear
                            echo "conversion in progress ..."
                            for n in $ac33; do ffmpeg -i "$n" -map_metadata 0 "${n%.ac3}.wav"> /dev/null 2>&1; done
                            enco=wav
                            var=1
                        else
                            zenity --error --text="No compatible files found in the selected directory"
                            var=0
                        fi;
                elif [ "$?" = "1" ]                           
                    then
                        zenity --error --text="No files selected"
                        var=0
                else 
                        zenity --error --text="An unexpected error has occurred"
                        var=0
                fi;
        elif [ "$AUDIO" = "21" ]                                   #ac3 en aac
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                if [ "$?" = "0" ]; then
                ac33=$(find $FILE -name "*.ac3")
                        if [ -n "$ac33" ]; then
                            clear
                            echo "conversion in progress ..."
                            for o in $ac33; do ffmpeg -i "$o" -map_metadata 0 -c:a libfaac "${o%.ac3}.aac"> /dev/null 2>&1; done
                            enco=aac
                            var=1
                        else
                            zenity --error --text="No compatible files found in the selected directory"
                            var=0
                        fi;
                elif [ "$?" = "1" ]                           
                    then
                        zenity --error --text="No files selected"
                        var=0
                else 
                        zenity --error --text="An unexpected error has occurred"
                        var=0
                fi;
        elif [ "$AUDIO" = "22" ]                                   #ac3 en ogg
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                if [ "$?" = "0" ]; then
                ac33=$(find $FILE -name "*.ac3")
                        if [ -n "$ac33" ]; then
                            clear
                            echo "conversion in progress ..."
                            for p in $ac33; do ffmpeg -i "$p" -map_metadata 0 -c:a libvorbis "${p%.ac3}.ogg"> /dev/null 2>&1; done
                            enco=ogg
                            var=1
                        else
                            zenity --error --text="No compatible files found in the selected directory"
                            var=0
                        fi;
                elif [ "$?" = "1" ]                           
                    then
                        zenity --error --text="No files selected"
                        var=0
                else 
                        zenity --error --text="An unexpected error has occurred"
                        var=0
                fi;
        elif [ "$AUDIO" = "23" ]                                   #ac3 en opus
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                if [ "$?" = "0" ]; then
                ac33=$(find $FILE -name "*.ac3")
                        if [ -n "$ac33" ]; then
                            clear
                            echo "conversion in progress ..."
                            for p in $ac33; do ffmpeg -i "$p" -map_metadata 0 -c:a libopus "${p%.ac3}.opus"> /dev/null 2>&1; done
                            enco=ogg
                            var=1
                        else
                            zenity --error --text="No compatible files found in the selected directory"
                            var=0
                        fi;
                elif [ "$?" = "1" ]                           
                    then
                        zenity --error --text="No files selected"
                        var=0
                else 
                        zenity --error --text="An unexpected error has occurred"
                        var=0
                fi;
        elif [ "$AUDIO" = "24" ]                                   #ac3 en vorbis
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                if [ "$?" = "0" ]; then
                ac33=$(find $FILE -name "*.ac3")
                        if [ -n "$ac33" ]; then
                            clear
                            echo "conversion in progress ..."
                            for p in $ac33; do ffmpeg -i "$p" -map_metadata 0 -c:a libvorbis "${p%.ac3}.vorbis"> /dev/null 2>&1; done
                            enco=ogg
                            var=1
                        else
                            zenity --error --text="No compatible files found in the selected directory"
                            var=0
                        fi;
                elif [ "$?" = "1" ]                           
                    then
                        zenity --error --text="No files selected"
                        var=0
                else 
                        zenity --error --text="An unexpected error has occurred"
                        var=0
                fi;
        elif [ "$AUDIO" = "25" ]                                   #aac en wav
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                if [ "$?" = "0" ]; then
                aacc=$(find $FILE -name "*.aac")
                        if [ -n "$aacc" ]; then
                            clear
                            echo "conversion in progress ..."
                            for q in $aacc; do ffmpeg -i "$q" -map_metadata 0 "${q%.aac}.wav"> /dev/null 2>&1 ; done
                            enco=wav
                            var=1
                        else
                            zenity --error --text="No compatible files found in the selected directory"
                            var=0
                        fi;
                elif [ "$?" = "1" ]                           
                    then
                        zenity --error --text="No files selected"
                        var=0
                else 
                        zenity --error --text="An unexpected error has occurred"
                        var=0
                fi;
           elif [ "$AUDIO" = "26" ]                                   #aac en ac3
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                if [ "$?" = "0" ]; then
                aacc=$(find $FILE -name "*.aac")
                        if [ -n "$aacc" ]; then
                            clear
                            echo "conversion in progress ..."
                            for r in $aacc; do ffmpeg -i "$r" -map_metadata 0 -c:a ac3 "${r%.aac}.ac3"> /dev/null 2>&1; done
                            enco=ac3
                            var=1
                        else
                            zenity --error --text="No compatible files found in the selected directory"
                            var=0
                        fi;
                elif [ "$?" = "1" ]                           
                    then
                        zenity --error --text="No files selected"
                        var=0
                else 
                        zenity --error --text="An unexpected error has occurred"
                        var=0
                fi;
        elif [ "$AUDIO" = "27" ]                                  #aac en ogg
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                if [ "$?" = "0" ]; then
                aacc=$(find $FILE -name "*.aac")
                        if [ -n "$aacc" ]; then
                            clear
                            echo "conversion in progress ..."
                            for s in $aacc; do ffmpeg -i "$s" -map_metadata 0 -c:a libvorbis "${s%.aac}.ogg"> /dev/null 2>&1; done
                            enco=ogg
                            var=1
                        else
                            zenity --error --text="No compatible files found in the selected directory"
                            var=0
                        fi;
                elif [ "$?" = "1" ]                           
                    then
                        zenity --error --text="No files selected"
                        var=0
                else 
                        zenity --error --text="An unexpected error has occurred"
                        var=0
                fi;
        elif [ "$AUDIO" = "28" ]                                   #aac en mp3
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                if [ "$?" = "0" ]; then
                aacc=$(find $FILE -name "*.aac")
                        if [ -n "$aacc" ]; then
                            clear
                            echo "conversion in progress ..."
                            for e in $aacc; do ffmpeg -i "$e" -map_metadata 0 -c:a libmp3lame "${e%.aac}.mp3"> /dev/null 2>&1; done
                            enco=mp3
                            var=1
                        else
                            zenity --error --text="No compatible files found in the selected directory"
                            var=0
                        fi;
                elif [ "$?" = "1" ]                           
                    then
                        zenity --error --text="No files selected"
                        var=0
                else 
                        zenity --error --text="An unexpected error has occurred"
                        var=0
                fi;
        elif [ "$AUDIO" = "29" ]                                   #aac en opus
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                if [ "$?" = "0" ]; then
                aacc=$(find $FILE -name "*.aac")
                        if [ -n "$aacc" ]; then
                            clear
                            echo "conversion in progress ..."
                            for e in $aacc; do ffmpeg -i "$e" -map_metadata 0 -c:a libopus "${e%.aac}.opus"> /dev/null 2>&1; done
                            enco=mp3
                            var=1
                        else
                            zenity --error --text="No compatible files found in the selected directory"
                            var=0
                        fi;
                elif [ "$?" = "1" ]                           
                    then
                        zenity --error --text="No files selected"
                        var=0
                else 
                        zenity --error --text="An unexpected error has occurred"
                        var=0
                fi;
       elif [ "$AUDIO" = "30" ]                                   #aac en vorbis
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                if [ "$?" = "0" ]; then
                aacc=$(find $FILE -name "*.aac")
                        if [ -n "$aacc" ]; then
                            clear
                            echo "conversion in progress ..."
                            for e in $aacc; do ffmpeg -i "$e" -map_metadata 0 -c:a libvorbis "${e%.aac}.vorbis"> /dev/null 2>&1; done
                            enco=mp3
                            var=1
                        else
                            zenity --error --text="No compatible files found in the selected directory"
                            var=0
                        fi;
                elif [ "$?" = "1" ]                           
                    then
                        zenity --error --text="No files selected"
                        var=0
                else 
                        zenity --error --text="An unexpected error has occurred"
                        var=0
                fi;
        elif [ "$AUDIO" = "31" ]                                   #flac en mp3
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                if [ "$?" = "0" ]; then
                flacc=$(find $FILE -name "*.flac")
                        if [ -n "$flacc" ]; then
                            clear
                            echo "conversion in progress ..."
                            for rr in $flacc; do ffmpeg -i "$rr" -map_metadata 0 -c:a libmp3lame "${rr%.flac}.mp3"> /dev/null 2>&1; done
                            enco=mp3
                            var=1
                        else
                            zenity --error --text="No compatible files found in the selected directory"
                            var=0
                        fi;
                elif [ "$?" = "1" ]                           
                    then
                    zenity --error --text="No files selected"
                    var=0
                else 
                    zenity --error --text="An unexpected error has occurred"
                    var=0
                fi;
        elif [ "$AUDIO" = "32" ]                                   #flac en wav
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                if [ "$?" = "0" ]; then
                flacc=$(find $FILE -name "*.flac")
                        if [ -n "$flacc" ]; then
                            clear
                            echo "conversion in progress ..."
                            for ss in $flacc; do ffmpeg -i "$ss" -map_metadata 0 "${ss%.flac}.wav"> /dev/null 2>&1; done
                            enco=wav
                            var=1
                        else
                            zenity --error --text="No compatible files found in the selected directory"
                            var=0
                        fi;
                elif [ "$?" = "1" ]                           
                    then
                        zenity --error --text="No files selected"
                        var=0
                else 
                        zenity --error --text="An unexpected error has occurred"
                        var=0
                fi;
        elif [ "$AUDIO" = "33" ]                                   #flac en ogg
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                if [ "$?" = "0" ]; then
                flacc=$(find $FILE -name "*.flac")
                        if [ -n "$flacc" ]; then
                            clear
                            echo "conversion in progress ..."
                            for tt in $flacc; do ffmpeg -i "$tt" -map_metadata 0 -c:a libvorbis "${tt%.flac}.ogg"> /dev/null 2>&1; done
                            enco=ogg 
                            var=1
                        else
                            zenity --error --text="No compatible files found in the selected directory"
                            var=0
                        fi;
                elif [ "$?" = "1" ]                           
                    then
                        zenity --error --text="No files selected"
                        var=0
                else 
                        zenity --error --text="An unexpected error has occurred"
                        var=0
                fi;
        elif [ "$AUDIO" = "34" ]                                   #flac en ac3
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
            if [ "$?" = "0" ]; then
                flacc=$(find $FILE -name "*.flac")
                        if [ -n "$flacc" ]; then
                            clear
                            echo "conversion in progress ..."
                            for tt in $flacc; do ffmpeg -i "$tt" -map_metadata 0 -c:a ac3 "${tt%.flac}.ac3"> /dev/null 2>&1; done
                            enco=ac3 
                            var=1
                        else
                            zenity --error --text="No compatible files found in the selected directory"
                            var=0
                        fi;
            elif [ "$?" = "1" ]                           
                then
                    zenity --error --text="No files selected"
                    var=0
            else 
                    zenity --error --text="An unexpected error has occurred"
                    var=0
            fi;
        elif [ "$AUDIO" = "35" ]                                   #flac en opus
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                if [ "$?" = "0" ]; then
                    flacc=$(find $FILE -name "*.flac")
                            if [ -n "$flacc" ]; then
                                clear
                                echo "conversion in progress ..."
                                for tt in $flacc; do ffmpeg -i "$tt" -map_metadata 0 -c:a libopus "${tt%.flac}.opus"> /dev/null 2>&1; done
                                enco=ac3 
                                var=1
                            else
                                zenity --error --text="No compatible files found in the selected directory"
                                var=0
                            fi;
                elif [ "$?" = "1" ]                           
                    then
                        zenity --error --text="No files selected"
                        var=0
                else
                        zenity --error --text="An unexpected error has occurred"
                        var=0
                fi;
        elif [ "$AUDIO" = "36" ]                                   #flac en vorbis
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                if [ "$?" = "0" ]; then
                    flacc=$(find $FILE -name "*.flac")
                            if [ -n "$flacc" ]; then
                                clear
                                echo "conversion in progress ..."
                                for tt in $flacc; do ffmpeg -i "$tt" -map_metadata 0 -c:a libvorbis "${tt%.flac}.opvorbisus"> /dev/null 2>&1; done
                                enco=ac3 
                                var=1
                            else
                                zenity --error --text="No compatible files found in the selected directory"
                                var=0
                            fi;
                elif [ "$?" = "1" ]                           
                    then
                        zenity --error --text="No files selected"
                        var=0
                else
                        zenity --error --text="An unexpected error has occurred"
                        var=0
                fi;
        elif [ "$AUDIO" = "37" ]                                   #opus en mp3
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                if [ "$?" = "0" ]; then
                    opuss=$(find $FILE -name "*.opus")
                            if [ -n "$opuss" ]; then
                                clear
                                echo "conversion in progress ..."
                                for tt in $opuss; do ffmpeg -i "$tt" -ab 320k -map_metadata 0 -c:a libmp3lame "${tt%.opus}.mp3"> /dev/null 2>&1; done
                                enco=ac3 
                                var=1
                            else
                                zenity --error --text="No compatible files found in the selected directory"
                                var=0
                            fi;
                elif [ "$?" = "1" ]                           
                    then
                        zenity --error --text="No files selected"
                        var=0
                else
                        zenity --error --text="An unexpected error has occurred"
                        var=0
                fi;
        elif [ "$AUDIO" = "38" ]                                   #opus en ogg
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                if [ "$?" = "0" ]; then
                    opuss=$(find $FILE -name "*.opus")
                        if [ -n "$opuss" ]; then
                            clear
                            echo "conversion in progress ..."
                            for tt in $opuss; do ffmpeg -i "$tt" -ab 320k -map_metadata 0 -c:a libvorbis "${tt%.opus}.ogg"> /dev/null 2>&1; done
                            enco=ac3 
                            var=1
                        else
                            zenity --error --text="No compatible files found in the selected directory"
                            var=0
                        fi;
                elif [ "$?" = "1" ]                           
                    then
                        zenity --error --text="No files selected"
                        var=0
                else 
                        zenity --error --text="An unexpected error has occurred"
                        var=0
                fi;
        elif [ "$AUDIO" = "39" ]                                   #opus en ac3
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                if [ "$?" = "0" ]; then
                    opuss=$(find $FILE -name "*.opus")
                        if [ -n "$opuss" ]; then
                            clear
                            echo "conversion in progress ..."
                            for tt in $opuss; do ffmpeg -i "$tt" -ab 320k -map_metadata 0 -c:a ac3 "${tt%.opus}.ac3"> /dev/null 2>&1; done
                            enco=ac3 
                            var=1
                        else
                            zenity --error --text="No compatible files found in the selected directory"
                            var=0
                        fi;
                elif [ "$?" = "1" ]                           
                    then
                        zenity --error --text="No files selected"
                        var=0
                else 
                        zenity --error --text="An unexpected error has occurred"
                        var=0
                fi;
        elif [ "$AUDIO" = "40" ]                                   #opus en aac
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                if [ "$?" = "0" ]; then
                    opuss=$(find $FILE -name "*.opus")
                        if [ -n "$opuss" ]; then
                            clear
                            echo "conversion in progress ..."
                            for tt in $opuss; do ffmpeg -i "$tt" -ab 320k -map_metadata 0 -c:a libfaac "${tt%.opus}.aac"> /dev/null 2>&1; done
                            enco=ac3 
                            var=1
                        else
                            zenity --error --text="No compatible files found in the selected directory"
                            var=0
                        fi;
                elif [ "$?" = "1" ]                           
                    then
                        zenity --error --text="No files selected"
                        var=0
                else 
                        zenity --error --text="An unexpected error has occurred"
                        var=0
                fi;
        elif [ "$AUDIO" = "41" ]                                   #opus en flac
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                if [ "$?" = "0" ]; then
                    opuss=$(find $FILE -name "*.opus")
                        if [ -n "$opuss" ]; then
                            clear
                            echo "conversion in progress ..."
                            for tt in $opuss; do ffmpeg -i "$tt" -ab 320k -map_metadata 0 -c:a flac "${tt%.opus}.flac"> /dev/null 2>&1; done
                            enco=ac3 
                            var=1
                        else
                            zenity --error --text="No compatible files found in the selected directory"
                            var=0
                        fi;
                elif [ "$?" = "1" ]                           
                    then
                        zenity --error --text="No files selected"
                        var=0
                else 
                        zenity --error --text="An unexpected error has occurred"
                        var=0
                fi;
        elif [ "$AUDIO" = "42" ]                                   #opus en wav
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                if [ "$?" = "0" ]; then
                    opuss=$(find $FILE -name "*.opus")
                        if [ -n "$opuss" ]; then
                            clear
                            echo "conversion in progress ..."
                            for tt in $opuss; do ffmpeg -i "$tt" -ab 320k -map_metadata 0 "${tt%.opus}.wav"> /dev/null 2>&1; done
                            enco=ac3 
                            var=1
                        else
                            zenity --error --text="No compatible files found in the selected directory"
                            var=0
                        fi;
                elif [ "$?" = "1" ]                           
                    then
                        zenity --error --text="No files selected"
                        var=0
                else 
                        zenity --error --text="An unexpected error has occurred"
                        var=0
                fi;
        elif [ "$AUDIO" = "43" ]                                   #opus en vorbis
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                if [ "$?" = "0" ]; then
                    opuss=$(find $FILE -name "*.opus")
                            if [ -n "$opuss" ]; then
                                clear
                                echo "conversion in progress ..."
                                for tt in $opuss; do ffmpeg -i "$tt" -ab 320k -map_metadata 0 -c:a libvorbis "${tt%.opus}.vorbis"> /dev/null 2>&1; done
                                enco=ac3 
                                var=1
                            else
                                zenity --error --text="No compatible files found in the selected directory"
                                var=0
                            fi;
                elif [ "$?" = "1" ]                           
                    then
                        zenity --error --text="No files selected"
                        var=0
                else
                        zenity --error --text="An unexpected error has occurred"
                        var=0
                fi;
        elif [ "$AUDIO" = "44" ]                                   #vorbis en mp3
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                if [ "$?" = "0" ]; then
                    vorbiss=$(find $FILE -name "*.vorbis")
                            if [ -n "$vorbiss" ]; then
                                clear
                                echo "conversion in progress ..."
                                for tt in $vorbiss; do ffmpeg -i "$tt" -ab 192k -map_metadata 0 -c:a libmp3lame "${tt%.vorbis}.mp3"> /dev/null 2>&1; done
                                enco=ac3 
                                var=1
                            else
                                zenity --error --text="No compatible files found in the selected directory"
                                var=0
                            fi;
                elif [ "$?" = "1" ]                           
                    then
                        zenity --error --text="No files selected"
                        var=0
                else
                        zenity --error --text="An unexpected error has occurred"
                        var=0
                fi;
        elif [ "$AUDIO" = "45" ]                                   #vorbis en ogg
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                if [ "$?" = "0" ]; then
                    vorbiss=$(find $FILE -name "*.vorbis")
                        if [ -n "$vorbiss" ]; then
                            clear
                            echo "conversion in progress ..."
                            for tt in $vorbiss; do ffmpeg -i "$tt" -ab 192k -map_metadata 0 -c:a libvorbis "${tt%.vorbis}.ogg"> /dev/null 2>&1; done
                            enco=ac3 
                            var=1
                        else
                            zenity --error --text="No compatible files found in the selected directory"
                            var=0
                        fi;
                elif [ "$?" = "1" ]                           
                    then
                        zenity --error --text="No files selected"
                        var=0
                else 
                        zenity --error --text="An unexpected error has occurred"
                        var=0
                fi;
        elif [ "$AUDIO" = "46" ]                                   #vorbis en ac3
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                if [ "$?" = "0" ]; then
                    vorbiss=$(find $FILE -name "*.vorbis")
                        if [ -n "$vorbiss" ]; then
                            clear
                            echo "conversion in progress ..."
                            for tt in $vorbiss; do ffmpeg -i "$tt" -ab 192k -map_metadata 0 -c:a ac3 "${tt%.vorbis}.ogg"> /dev/null 2>&1; done
                            enco=ac3 
                            var=1
                        else
                            zenity --error --text="No compatible files found in the selected directory"
                            var=0
                        fi;
                elif [ "$?" = "1" ]                           
                    then
                        zenity --error --text="No files selected"
                        var=0
                else 
                        zenity --error --text="An unexpected error has occurred"
                        var=0
                fi;
        elif [ "$AUDIO" = "47" ]                                   #vorbis en aac
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                if [ "$?" = "0" ]; then
                    vorbiss=$(find $FILE -name "*.vorbis")
                        if [ -n "$vorbiss" ]; then
                            clear
                            echo "conversion in progress ..."
                            for tt in $vorbiss; do ffmpeg -i "$tt" -ab 192k -map_metadata 0 -c:a libfaac "${tt%.vorbis}.aac"> /dev/null 2>&1; done
                            enco=ac3 
                            var=1
                        else
                            zenity --error --text="No compatible files found in the selected directory"
                            var=0
                        fi;
                elif [ "$?" = "1" ]                           
                    then
                        zenity --error --text="No files selected"
                        var=0
                else 
                        zenity --error --text="An unexpected error has occurred"
                        var=0
                fi;
        elif [ "$AUDIO" = "48" ]                                   #vorbis en flac
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                if [ "$?" = "0" ]; then
                    vorbiss=$(find $FILE -name "*.vorbis")
                        if [ -n "$vorbiss" ]; then
                            clear
                            echo "conversion in progress ..."
                            for tt in $vorbiss; do ffmpeg -i "$tt" -ab 192k -map_metadata 0 -c:a flac "${tt%.vorbis}.flac"> /dev/null 2>&1; done
                            enco=ac3 
                            var=1
                        else
                            zenity --error --text="No compatible files found in the selected directory"
                            var=0
                        fi;
                elif [ "$?" = "1" ]                           
                    then
                        zenity --error --text="No files selected"
                        var=0
                else 
                        zenity --error --text="An unexpected error has occurred"
                        var=0
                fi;
        elif [ "$AUDIO" = "49" ]                                   #vorbis en wav
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                if [ "$?" = "0" ]; then
                    vorbiss=$(find $FILE -name "*.vorbis")
                        if [ -n "$vorbiss" ]; then
                            clear
                            echo "conversion in progress ..."
                            for tt in $vorbiss; do ffmpeg -i "$tt" -ab 192k -map_metadata 0 "${tt%.vorbis}.wav"> /dev/null 2>&1; done
                            enco=ac3 
                            var=1
                        else
                            zenity --error --text="No compatible files found in the selected directory"
                            var=0
                        fi;
                elif [ "$?" = "1" ]                           
                    then
                        zenity --error --text="No files selected"
                        var=0
                else 
                        zenity --error --text="An unexpected error has occurred"
                        var=0
                fi;
        elif [ "$AUDIO" = "50" ]                                   #vorbis en opus
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                if [ "$?" = "0" ]; then
                    vorbiss=$(find $FILE -name "*.vorbis")
                        if [ -n "$vorbiss" ]; then
                            clear
                            echo "conversion in progress ..."
                            for tt in $vorbiss; do ffmpeg -i "$tt" -ab 192k -map_metadata 0 -c:a libopus "${tt%.vorbis}.opus"> /dev/null 2>&1; done
                            enco=ac3 
                            var=1
                        else
                            zenity --error --text="No compatible files found in the selected directory"
                            var=0
                        fi;
                elif [ "$?" = "1" ]                           
                    then
                        zenity --error --text="No files selected"
                        var=0
                else 
                        zenity --error --text="An unexpected error has occurred"
                        var=0
                fi;
        elif [ "$AUDIO" = "51" ]
            then
               var=1
        else
            zenity --error --text="Please enter a number between 1 and 51"
            var=0
        fi;
done
whiptail --textbox --title "Process finished successfully" --msgbox "Your files have been re-encoded in $enco in your current foldert" 10 80
}

function convertisso-image {
clear
vor=0
image=$(whiptail --title "Convertisso image menu" --menu "Choose an option" 40 90 20 \
"1" "png to jpg" \
"2" "jpg to png" \
"3" "tiff to png" \
"4" "tiff to jpg" \
"5" "tiff to BMP" \
"6" "tiff to pdf" \
"7" "tiff to gif" \
"8" "pdf to tiff" \
"9" "pdf to jpg" \
"10" "pdf to png" \
"11" "svg to tiff" \
"12" "svg to png" \
"13" "svg to pdf" \
"14" "heic to jpg" 
"15" "EXIT" 3>&1 1>&2 2>&3)
while [ $vor = 0 ]; do
        if [ "$image" = "1" ]                                      #png en jpg 
            then
            FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
            if [ "$?" = "0" ]; then
                pngg=$(find $FILE -name "*.png")
                        if [ -n "$pngg" ]; then
                            clear
                            for uu in $pngg; do  convert "$uu"  "${uu%.png}.jpg"; done
                            encov=jpg 
                            vor=1
                        else
                            zenity --error --text="No compatible files found in the selected directory"
                            vor=0
                        fi;
            elif [ "$?" = "1" ]                           
                then
                    zenity --error --text="No files selected"
                    vor=0
            else 
                    zenity --error --text="An unexpected error has occurred"
                    vor=0
            fi;
        elif [ "$image" = "2" ]                                    #jpg en png
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
            if [ "$?" = "0" ]; then
                jpgg=$(find $FILE -name "*.jpg")
                        if [ -n "$jpgg" ]; then
                            clear
                            for vv in $jpgg; do  convert "$vv"  "${vv%.jpg}.png"; done
                            encov=png 
                            vor=1
                        else
                            zenity --error --text="No compatible files found in the selected directory"
                            vor=0
                        fi;
            elif [ "$?" = "1" ]                           
                then
                    zenity --error --text="No files selected"
                    vor=0
            else 
                    zenity --error --text="An unexpected error has occurred"
                    vor=0
            fi;
        elif [ "$image" = "3" ]                                    #tiff en png
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
            if [ "$?" = "0" ]; then
                tifff=$(find $FILE -name "*.tiff")
                        if [ -n "$tifff" ]; then
                            clear
                            for ww in $tifff; do  convert "$ww"  "${ww%.tiff}.png"; done
                            encov=png 
                            vor=1
                        else
                            zenity --error --text="No compatible files found in the selected directory"
                            vor=0
                        fi;
            elif [ "$?" = "1" ]                           
                then
                    zenity --error --text="No files selected"
                    vor=0
            else 
                    zenity --error --text="An unexpected error has occurred"
                    vor=0
            fi;
        elif [ "$image" = "4" ]                                    #tiff en jpg
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
            if [ "$?" = "0" ]; then
                tifff=$(find $FILE -name "*.tiff")
                        if [ -n "$tifff" ]; then
                            clear
                            for yy in $tifff; do  convert "$yy"  "${yy%.tiff}.jpg"; done
                            encov=jpg
                            vor=1
                        else
                            zenity --error --text="No compatible files found in the selected directory"
                            vor=0
                        fi;
            elif [ "$?" = "1" ]                           
                then
                    zenity --error --text="No files selected"
                    vor=0
            else 
                    zenity --error --text="An unexpected error has occurred"
                    vor=0
            fi;
        elif [ "$image" = "5" ]                                #tiff en BMP
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
            if [ "$?" = "0" ]; then
                tifff=$(find $FILE -name "*.tiff")
                    if [ -n "$tifff" ]; then
                        clear
                        for zz in $tifff; do  convert "$zz"  "${zz%.tiff}.BMP"; done
                        encov=BMP 
                        vor=1
                    else
                            zenity --error --text="No compatible files found in the selected directory"
                            vor=0
                    fi;
            elif [ "$?" = "1" ]                           
                then
                    zenity --error --text="No files selected"
                    vor=0
            else 
                    zenity --error --text="An unexpected error has occurred"
                    vor=0
            fi;
        elif [ "$image" = "6" ]                                #tiff en pdf #
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
            if [ "$?" = "0" ]; then
                tifff=$(find $FILE -name "*.tiff")
                    if [ -n "$tifff" ]; then
                        clear
                        for aaa in $tifff; do  tiff2pdf -o "${aaa%.tiff}.pdf" "$aaa"; done
                        encov=pdf 
                        vor=1
                    else
                            zenity --error --text="No compatible files found in the selected directory"
                            vor=0
                    fi;
            elif [ "$?" = "1" ]                           
                then
                    zenity --error --text="No files selected"
                    vor=0
            else 
                    zenity --error --text="An unexpected error has occurred"
                    vor=0
            fi;
        elif [ "$image" = "7" ]                                #tiff en gif
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
            if [ "$?" = "0" ]; then
                tifff=$(find $FILE -name "*.tiff")
                    if [ -n "$tifff" ]; then
                        clear
                        for bbb in $tifff; do  convert "$bbb"  "${bbb%.tiff}.gif"; done
                        encov=gif 
                        vor=1
                    else
                            zenity --error --text="No compatible files found in the selected directory"
                            vor=0
                    fi;
            elif [ "$?" = "1" ]                           
                then
                    zenity --error --text="No files selected"
                    vor=0
            else 
                    zenity --error --text="An unexpected error has occurred"
                    vor=0
            fi;
        elif [ "$image" = "8" ]                                #pdf en tiff
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
            if [ "$?" = "0" ]; then
                pdff=$(find $FILE -name "*.pdf")
                    if [ -n "$pdff" ]; then
                        clear
                        for eee in $pdff; do  convert "$eee"  "${eee%.pdf}.tiff"; done
                        encov=tiff 
                        vor=1
                    else
                        zenity --error --text="No compatible files found in the selected directory"
                        vor=0
                    fi;
            elif [ "$?" = "1" ]                           
                then
                    zenity --error --text="No files selected"
                    vor=0
            else 
                    zenity --error --text="An unexpected error has occurred"
                    vor=0
            fi;
        elif [ "$image" = "9" ]                                #pdf en jpg
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
            if [ "$?" = "0" ]; then
                pdff=$(find $FILE -name "*.pdf")
                    if [ -n "$pdff" ]; then
                        clear
                        for fff in $pdff; do  convert "$fff"  "${fff%.pdf}.jpg"; done
                        encov=jpg 
                        vor=1
                    else
                        zenity --error --text="No compatible files found in the selected directory"
                        vor=0
                    fi;
            elif [ "$?" = "1" ]                           
                then
                    zenity --error --text="No files selected"
                    vor=0
            else 
                    zenity --error --text="An unexpected error has occurred"
                    vor=0
            fi;
        elif [ "$image" = "10" ]                                #pdf en png
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
            if [ "$?" = "0" ]; then
                pdff=$(find $FILE -name "*.pdf")
                    if [ -n "$pdff" ]; then
                        clear
                        for ggg in $pdff; do  convert "$ggg"  "${ggg%.pdf}.png"; done
                        encov=png 
                        vor=1
                    else
                        zenity --error --text="No compatible files found in the selected directory"
                        vor=0
                    fi;
            elif [ "$?" = "1" ]                           
                then
                    zenity --error --text="No files selected"
                    vor=0
            else 
                    zenity --error --text="An unexpected error has occurred"
                    vor=0
            fi;
        elif [ "$image" = "11" ]                                #svg en tiff
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
            if [ "$?" = "0" ]; then
                svgg=$(find $FILE -name "*.svg")
                    if [ -n "$svgg" ]; then
                        clear
                        for hhh in $svgg; do  convert "$hhh"  "${hhh%.svg}.tiff"; done
                        encov=tiff 
                        vor=1
                    else
                        zenity --error --text="No compatible files found in the selected directory"
                        vor=0
                    fi;
            elif [ "$?" = "1" ]                           
                then
                    zenity --error --text="No files selected"
                    vor=0
            else 
                    zenity --error --text="An unexpected error has occurred"
                    vor=0
            fi;
        elif [ "$image" = "12" ]                                #svg en png
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
            if [ "$?" = "0" ]; then
                svgg=$(find $FILE -name "*.svg")
                    if [ -n "$svgg" ]; then
                        clear
                        for hhh in $svgg; do  convert "$hhh"  "${hhh%.svg}.png"; done
                        encov=png 
                        vor=1
                    else
                        zenity --error --text="No compatible files found in the selected directory"
                        vor=0
                    fi;
            elif [ "$?" = "1" ]                           
                then
                    zenity --error --text="No files selected"
                    vor=0
            else 
                    zenity --error --text="An unexpected error has occurred"
                    vor=0
            fi;
        elif [ "$image" = "13" ]                                #svg en pdf
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
            if [ "$?" = "0" ]; then
                svgg=$(find $FILE -name "*.svg")
                    if [ -n "$svgg" ]; then
                        clear
                        for hhh in $svgg; do  rsvg-convert -f pdf -o "${hhh%.svg}.pdf" "$hhh" ; done
                        encov=pdf 
                        vor=1
                    else
                        zenity --error --text="No compatible files found in the selected directory"
                        vor=0
                    fi;
            elif [ "$?" = "1" ]                           
                then
                    zenity --error --text="No files selected"
                    vor=0
            else 
                    zenity --error --text="An unexpected error has occurred"
                    vor=0
            fi;
        elif [ "$image" = "14" ]                               
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
            if [ "$?" = "0" ]; then
                heicc=$(find $FILE -name "*.heic")
                    if [ -n "$heicc" ]; then
                        clear
                        for ggg in $heicc ; do  heif-convert "$ggg" "${ggg%.heic}.jpg" ; done
                        encov=jpg
                        vor=1
                    else
                        zenity --error --text="No compatible files found in the selected directory"
                        vor=0
                    fi;
            elif [ "$?" = "1" ]                           
                then
                    zenity --error --text="No files selected"
                    vor=0
            else 
                    zenity --error --text="An unexpected error has occurred"
                    vor=0
            fi;
        elif [ "$image" = "15" ]                               
            then
                vor=1
        else    
            zenity --error --text="Please enter a number between  1 and 14"
            vor=0
    fi;
done
whiptail --textbox --title "Process finished successfully" --msgbox "Your files have been re-encoded in $encov in your current folder" 10 80
}
clear
convertisso
sleep 1
MAIN=$(whiptail --title "Convertisso menu" --menu "Choose an option" 40 90 20 \
"1" "Convert audio file" \
"2" "Convert video file" \
"3" "Convert Video subtitle" \
"4" "Convert image (Beta)" \
"5" "Download video" \
"6" "EXIT" 3>&1 1>&2 2>&3)
echo $MAIN
        if [ "$MAIN" = "1" ];then convertisso-audio
        elif [ "$MAIN" = "2" ];then convertisso-video
        elif [ "$MAIN" = "3" ];then convertisso-subtitle
        elif [ "$MAIN" = "4" ];then convertisso-image
        elif [ "$MAIN" = "5" ];then convertisso-download-video
        elif [ "$MAIN" = "6" ];then exit
        else zenity --error --text="Please enter a number between 1 and 6" 
            varro=0
        fi;
done