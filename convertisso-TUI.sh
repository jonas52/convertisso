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

subtitle=$(whiptail --title "Convertisso audio menu" --menu "Choose an option" 30 80 10 \
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
    LINK=$(whiptail --title "Input" --inputbox "URL of your video" 10 60 3>&1 1>&2 2>&3)
    DOWNLOAD=$(whiptail --title "Convertisso download video menu" --menu "Choose an option" 30 80 10 \
    "1" "video without subtitle" \
    "2" "video with subtitle" \
    "3" "only audio (mp3)" \
    "4" "only the subtitle" \
    "5" "EXIT" 3>&1 1>&2 2>&3)
    DESTINATION=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
while [ "$varor" = 0 ];do
    if [ "$DOWNLOAD" = "1" ]                                     #video without subtitle
        then
        youtube-dl -f best -q --add-metadata "$LINK"
        while [ $? = "1" ] ;do zenity --error --text="Please retry INVALIDE link" varor=0; done
        mv *.mp4 $DESTINATION > /dev/null 2>&1
        mv *.mkv $DESTINATION > /dev/null 2>&1
        mv *.webm $DESTINATION > /dev/null 2>&1
        mv *.flv $DESTINATION > /dev/null 2>&1
        varor=1
    elif [ "$DOWNLOAD" = "2" ]                                     #video with subtitle
        then
        youtube-dl --write-srt --all-subs -q --add-metadata "$LINK"
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
        youtube-dl -x --audio-format best -q --add-metadata "$LINK"
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
}

function convertisso-video {
clear
varo=0
while [ $varo = 0 ];do
video=$(whiptail --title "Convertisso video menu" --menu "Choose an option" 30 80 10 \
"1" "mkv to avi" \
"2" "mkv to mov" \
"3" "mkv to mp4" \
"4" "mp4 to mkv" \
"5" "mp4 to mov" \
"6" "mp4 to avi" \
"7" "mov to mkv" \
"8" "mov to mp4" \
"9" "mov to avi" \
"10" "avi to mkv" \
"11" "avi to mp4" \
"12" "avi to mov" \
"13" "webm to mp4" \
"14" "hevc to mp4" \
"15" "EXIT" 3>&1 1>&2 2>&3)
        if [ "$video" = "1" ]                                     #mkv en avi
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                    if [ "$?" = "0" ]; then
                    mkvv=$(find $FILE -name "*.mkv")
                            if [ -n "$mkvv" ]; then
                                clear 
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
        elif [ "$video" = "4" ]                                     #mp4 en mkv                                     
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                 if [ "$?" = "0" ]; then
                    mp44=$(find $FILE -name "*.mp4")
                            if [ -n "$mp44" ]; then
                                clear
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
        elif [ "$video" = "5" ]                                     #mp4 en mov                                    
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                 if [ "$?" = "0" ]; then
                    mp44=$(find $FILE -name "*.mp4")
                            if [ -n "$mp44" ]; then
                                clear
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
        elif [ "$video" = "6" ]                                     #mp4 en avi
            then           
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                 if [ "$?" = "0" ]; then
                    mp44=$(find $FILE -name "*.mp4")
                            if [ -n "$mp44" ]; then
                                clear                        
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
        elif [ "$video" = "7" ]                                     #mov en mkv
            then        
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                 if [ "$?" = "0" ]; then
                    movv=$(find $FILE -name "*.mov")
                            if [ -n "$movv" ]; then
                                clear                             
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
        elif [ "$video" = "8" ]                                     #mov en mp4
            then        
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                 if [ "$?" = "0" ]; then
                    movv=$(find $FILE -name "*.mov")
                            if [ -n "$movv" ]; then
                                clear       
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
        elif [ "$video" = "9" ]                                     #mov en avi
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                 if [ "$?" = "0" ]; then
                    movv=$(find $FILE -name "*.mov")
                            if [ -n "$movv" ]; then
                                clear
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
        elif [ "$video" = "10" ]                                     #avi en mkv
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                 if [ "$?" = "0" ]; then
                    avii=$(find $FILE -name "*.avi")
                            if [ -n "$avii" ]; then
                                clear 
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
        elif [ "$video" = "11" ]                                     #avi en mp4
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                 if [ "$?" = "0" ]; then
                    avii=$(find $FILE -name "*.avi")
                            if [ -n "$avii" ]; then
                                clear  
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
        elif [ "$video" = "12" ]                                     #avi en mov
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                 if [ "$?" = "0" ]; then
                    avii=$(find $FILE -name "*.avi")
                            if [ -n "$avii" ]; then
                                clear  
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
        elif [ "$video" = "13" ]                                     #webm en mp4
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                 if [ "$?" = "0" ]; then
                    webmm=$(find $FILE -name "*.webm")
                            if [ -n "$webmm" ]; then
                                clear
                                for ff in $webmm; do ffmpeg -i "$ff" -c copy "${ff%.webm}.mp4"> /dev/null 2>&1; done
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
        elif [ "$video" = "14" ]                                     #HEVC to mp4
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                 if [ "$?" = "0" ]; then
                    hevcc=$(find $FILE -name "*.hevc")
                            if [ -n "$hevcc" ]; then
                                clear
                                for kkk in $hevcc; do ffmpeg -i "$kkk" -c copy "${kkk%.hevc}.mp4"> /dev/null 2>&1; done
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
        elif [ "$video" = "15" ]
            then
               varo=1
        else
            zenity --error --text="Please enter a number between 1 and 14"
            varo=0
        fi;
done
whiptail --textbox --title "Process finished successfully" --msgbox "Your files have been re-encoded in $enco in your current foldert" 10 80
    sleep 2
}

function convertisso-audio {
clear
var=0
while [ $var = 0 ];do
AUDIO=$(whiptail --title "Convertisso audio menu" --menu "Choose an option" 30 80 10 \
"1" "mp3 en wav" \
"2" "mp3 en ogg" \
"3" "mp3 en aac" \
"4" "mp3 en ac3" \
"5" "wav en mp3" \
"6" "wav en ogg" \
"7" "wav en aac" \
"8" "wav en ac3" \
"9" "ogg en mp3" \
"10" "ogg en wav" \
"11" "ogg en aac" \
"12" "ogg en ac3" \
"13" "ac3 en wav" \
"14" "ac3 en aac" \
"15" "ac3 en ogg" \
"16" "aac en wav" \
"17" "aac en wav" \
"18" "aac en ac3" \
"19" "aac en ogg" \
"20" "aac en mp3" \
"21" "flac en mp3" \
"22" "flac en wav" \
"23" "flac en ogg" \
"24" "flac en ac3" \
"25" "EXIT" 3>&1 1>&2 2>&3)
        if [ "$AUDIO" = "1" ]                             
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                    if [ "$?" = "0" ]; then
                    mp33=$(find $FILE -name "*.mp3")
                            if [ -n "$mp33" ]; then
                                clear
                                for a in $mp33 ; do ffmpeg -i "$a" "${a%.mp3}.wav"> /dev/null 2>&1; done
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
        elif [ "$AUDIO" = "2" ]                             
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                    if [ "$?" = "0" ]; then
                    mp33=$(find $FILE -name "*.mp3")
                            if [ -n "$mp33" ]; then
                                clear
                                echo "Conversion in progress ..."
                                for b in $mp33; do ffmpeg -i "${b}" -acodec libvorbis "${b/%mp3}.ogg"> /dev/null 2>&1; done #convertis les fichiers MP3 en OGG
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
        elif [ "$AUDIO" = "3" ]                                   #mp3 en aac
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                if [ "$?" = "0" ]; then
                mp33=$(find $FILE -name "*.mp3")
                    if [ -n "$mp33" ]; then
                        clear
                        echo "Conversion in progress ..."
                        for c in $mp33; do ffmpeg -i "$c" -acodec aac "${c%.mp3}.aac"> /dev/null 2>&1; done
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
        elif [ "$AUDIO" = "4" ]                                   #mp3 en ac3
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                if [ "$?" = "0" ]; then
                mp33=$(find $FILE -name "*.mp3")
                        if [ -n "$mp33" ]; then
                            clear
                            echo "Conversion in progress ..."
                            for m in $mp33; do ffmpeg -i "$m" -acodec ac3 "${m%.mp3}.ac3"> /dev/null 2>&1; done 
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
        elif [ "$AUDIO" = "5" ]                                   #wav en mp3
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                if [ "$?" = "0" ]; then
                wavv=$(find $FILE -name "*.wav")
                        if [ -n "$wavv" ]; then
                            clear
                            echo "Conversion in progress ..."
                            for d in $wavv; do ffmpeg -i "$d" -f mp3 "${d%.waw}.mp3"> /dev/null 2>&1; done
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
        elif [ "$AUDIO" = "6" ]                                       #wav en ogg
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                if [ "$?" = "0" ]; then
                wavv=$(find $FILE -name "*.wav")
                        if [ -n "$wavv" ]; then
                            clear
                            echo "conversion in progress ..."
                            for h in $wavv; do ffmpeg -i "$h" -acodec libvorbis "${h%.waw}.ogg"> /dev/null 2>&1; done 
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
        elif [ "$AUDIO" = "7" ]                                    #wav en aac
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                if [ "$?" = "0" ]; then
                wavv=$(find $FILE -name "*.wav")
                        if [ -n "$wavv" ]; then
                            clear
                            echo "conversion in progress ..."
                            for i in $wavv; do ffmpeg -i "$i" -acodec libfaac "${i%.waw}.aac"> /dev/null 2>&1; done 
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
        elif [ "$AUDIO" = "8" ]                                   #wav en ac3
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                if [ "$?" = "0" ]; then
                wavv=$(find $FILE -name "*.wav")
                        if [ -n "$wavv" ]; then
                            clear
                            echo "conversion in progress ..."
                            for j in $wavv; do ffmpeg -i "$j" -acodec libmp3lame "${j%.waw}.ac3"> /dev/null 2>&1; done 
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
        elif [ "$AUDIO" = "9" ]                                   #ogg en mp3 
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                if [ "$?" = "0" ]; then
                oggg=$(find $FILE -iname "*.ogg")
                        if [ -f "$oggg" ]; then
                            clear
                            echo "conversion in progress ..."
                            for g in $oggg ; do ffmpeg -i "$g" -acodec libmp3lame "${g%.ogg}.mp3"> /dev/null 2>&1; done #convertis les fichiers OGG en MP3
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
        elif [ "$AUDIO" = "10" ]                                   #ogg en wav
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                if [ "$?" = "0" ]; then
                oggg=$(find $FILE -name "*.ogg")
                        if [ -n "$oggg" ]; then
                            clear
                            echo "conversion in progress ..."
                            for k in $oggg; do ffmpeg -i "$k" "${k%.ogg}.wav"> /dev/null 2>&1; done 
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
        elif [ "$AUDIO" = "11" ]                                   #ogg en aac
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                if [ "$?" = "0" ]; then
                oggg=$(find $FILE -name "*.ogg")
                        if [ -n "$oggg" ]; then
                            clear
                            echo "conversion in progress ..."
                            for l in $oggg; do ffmpeg -i "$l" -acodec libfaac "${l%.ogg}.aac"> /dev/null 2>&1; done 
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
        elif [ "$AUDIO" = "12" ]                                   #ogg en ac3
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                if [ "$?" = "0" ]; then
                oggg=$(find $FILE -name "*.ogg")
                        if [ -n "$oggg" ]; then
                            clear
                            echo "conversion in progress ..."
                            for m in $oggg; do ffmpeg -i "$m" -acodec ac3 "${m%.ogg}.ac3"> /dev/null 2>&1; done 
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
        elif [ "$AUDIO" = "13" ]                                   #ac3 en wav
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                if [ "$?" = "0" ]; then
                ac33=$(find $FILE -name "*.ac3")
                        if [ -n "$ac33" ]; then
                            clear
                            echo "conversion in progress ..."
                            for n in $ac33; do ffmpeg -i "$n"  "${n%.ac3}.wav"> /dev/null 2>&1; done
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
        elif [ "$AUDIO" = "14" ]                                   #ac3 en aac
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                if [ "$?" = "0" ]; then
                ac33=$(find $FILE -name "*.ac3")
                        if [ -n "$ac33" ]; then
                            clear
                            echo "conversion in progress ..."
                            for o in $ac33; do ffmpeg -i "$o" -acodec libfaac "${o%.ac3}.aac"> /dev/null 2>&1; done
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
        elif [ "$AUDIO" = "15" ]                                   #ac3 en ogg
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                if [ "$?" = "0" ]; then
                ac33=$(find $FILE -name "*.ac3")
                        if [ -n "$ac33" ]; then
                            clear
                            echo "conversion in progress ..."
                            for p in $ac33; do ffmpeg -i "$p" -acodec libvorbis "${p%.ac3}.ogg"> /dev/null 2>&1; done
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
        elif [ "$AUDIO" = "16" ]                                   #ac3 en mp3
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                if [ "$?" = "0" ]; then
                ac33=$(find $FILE -name "*.ac3")
                        if [ -n "$ac33" ]; then
                            clear
                            echo "conversion in progress ..."
                            for f in $ac33; do ffmpeg -i "$f" -acodec libmp3lame "${f%.ac3}.mp3"> /dev/null 2>&1; done
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
        elif [ "$AUDIO" = "17" ]                                   #aac en wav
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                if [ "$?" = "0" ]; then
                aacc=$(find $FILE -name "*.aac")
                        if [ -n "$aacc" ]; then
                            clear
                            echo "conversion in progress ..."
                            for q in $aacc; do ffmpeg -i "$q" "${q%.aac}.wav"> /dev/null 2>&1 ; done
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
           elif [ "$AUDIO" = "18" ]                                   #aac en ac3
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                if [ "$?" = "0" ]; then
                aacc=$(find $FILE -name "*.aac")
                        if [ -n "$aacc" ]; then
                            clear
                            echo "conversion in progress ..."
                            for r in $aacc; do ffmpeg -i "$r" -acodec ac3 "${r%.aac}.ac3"> /dev/null 2>&1; done
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
        elif [ "$AUDIO" = "19" ]                                  #aac en ogg
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                if [ "$?" = "0" ]; then
                aacc=$(find $FILE -name "*.aac")
                        if [ -n "$aacc" ]; then
                            clear
                            echo "conversion in progress ..."
                            for s in $aacc; do ffmpeg -i "$s" -acodec libvorbis "${s%.aac}.ogg"> /dev/null 2>&1; done
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
        elif [ "$AUDIO" = "20" ]                                   #aac en mp3
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                if [ "$?" = "0" ]; then
                aacc=$(find $FILE -name "*.aac")
                        if [ -n "$aacc" ]; then
                            clear
                            echo "conversion in progress ..."
                            for e in $aacc; do ffmpeg -i "$e" -acodec libmp3lame "${e%.aac}.mp3"> /dev/null 2>&1; done
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
        elif [ "$AUDIO" = "21" ]                                   #flac en mp3
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                if [ "$?" = "0" ]; then
                flacc=$(find $FILE -name "*.flac")
                        if [ -n "$flacc" ]; then
                            clear
                            echo "conversion in progress ..."
                            for rr in $flacc; do ffmpeg -i "$rr" -acodec libmp3lame "${rr%.flac}.mp3"> /dev/null 2>&1; done
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
        elif [ "$AUDIO" = "22" ]                                   #flac en wav
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                if [ "$?" = "0" ]; then
                flacc=$(find $FILE -name "*.flac")
                        if [ -n "$flacc" ]; then
                            clear
                            echo "conversion in progress ..."
                            for ss in $flacc; do ffmpeg -i "$ss" "${ss%.flac}.wav"> /dev/null 2>&1; done
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
        elif [ "$AUDIO" = "23" ]                                   #flac en ogg
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
                if [ "$?" = "0" ]; then
                flacc=$(find $FILE -name "*.flac")
                        if [ -n "$flacc" ]; then
                            clear
                            echo "conversion in progress ..."
                            for tt in $flacc; do ffmpeg -i "$tt" -acodec libvorbis "${tt%.flac}.ogg"> /dev/null 2>&1; done
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
        elif [ "$AUDIO" = "24" ]                                   #flac en ac3
            then
                FILE=$(zenity --file-selection --directory --title="Select one directory (not recusive)")
             if [ "$?" = "0" ]; then
                flacc=$(find $FILE -name "*.flac")
                        if [ -n "$flacc" ]; then
                            clear
                            echo "conversion in progress ..."
                            for tt in $flacc; do ffmpeg -i "$tt" -acodec ac3 "${tt%.flac}.ac3"> /dev/null 2>&1; done
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
        elif [ "$AUDIO" = "25" ]
            then
               var=1
        else
            zenity --error --text="Please enter a number between 1 and 24"
            var=0
        fi;
done
whiptail --textbox --title "Process finished successfully" --msgbox "Your files have been re-encoded in $enco in your current foldert" 10 80
}

function convertisso-image {
clear
vor=0
image=$(whiptail --title "Convertisso audio menu" --menu "Choose an option" 30 80 10 \
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
sleep 2
}

#ffmpeg -i infile.mp4 -i infile.srt -c copy -c:s mov_text outfile.mp4
clear
convertisso
sleep 1

MAIN=$(whiptail --title "Convertisso menu" --menu "Choose an option" 30 80 10 \
"1" "Convert audio file" \
"2" "Convert video file" \
"3" "Convert Video subtitle" \
"4" "Convert image (Beta)" \
"5" "Download video" \
"6" "EXIT" 3>&1 1>&2 2>&3)
echo $MAIN

        if [ "$MAIN" = "1" ]                                     
            then
                convertisso-audio
        elif [ "$MAIN" = "2" ]                                 
            then 
                convertisso-video
        elif [ "$MAIN" = "3" ]                                 
            then 
                convertisso-subtitle
        elif [ "$MAIN" = "4" ]                                 
            then 
                convertisso-image
        elif [ "$MAIN" = "5" ]                                 
            then 
                convertisso-download-video
        elif [ "$MAIN" = "6" ]                                 
            then 
                exit
                exit
        else
        zenity --error --text="Please enter a number between 1 and 6"
                varro=0
        fi;
done
