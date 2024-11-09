#!/bin/bash

# Colors
cyan='\e[96m'
red='\e[91m'
green='\e[92m'
default='\e[0m'
yellow='\e[93m'

# Legends
info="${cyan}[${yellow}*${cyan}]${default}"
success="${cyan}[${green}+${cyan}]${default}"
error="${cyan}[${red}!${cyan}]${default}"

# Get sc0pe_path variable as an argument
sc0pe_path=$1

# Get username
normal_user=$2

# Check permissions
echo -en "$info Checking user privileges...\n"
user_str=$(whoami)
if [[ $user_str != *"root"* ]];then
    echo -en "$error You must be a root user to use installer!\n"
    exit 1
fi

installer(){
    echo -en "\n$info Looks like we have permission to install. Let's begin...\n"

    # Install python modules
    echo -en "$info Installing Python dependencies...\n"
    pip3 install -r requirements.txt

    
    echo -en "$info Creating configuration file in ${green}/etc${default} directory\n"
    echo -en "[vBlock_PATH]\n" > /etc/vBlock.conf
    echo -en "sc0pe = /opt/v-block\n" >> /etc/vBlock.conf
    chown $normal_user:$normal_user /etc/vBlock.conf

    
    echo -en "$info Copying files to ${green}/opt${default} directory.\n"
    cd "$sc0pe_path/../" && cp -r v-block /opt/
    chown $normal_user:$normal_user /opt/v-block

    # Configurating libScanner.conf
    echo -en "[Rule_PATH]\n" > /opt/v-block/Systems/Android/libScanner.conf
    echo -en "rulepath = /opt/v-block/Systems/Android/YaraRules/\n\n" >> /opt/v-block/Systems/Android/libScanner.conf
    echo -en "[Decompiler]\n" >> /opt/v-block/Systems/Android/libScanner.conf
    if [ -d "/home/$normal_user/sc0pe_Base" ];then
        echo -en "decompiler = /home/$normal_user/sc0pe_Base/jadx/bin/jadx\n" >> /opt/v-block/Systems/Android/libScanner.conf
    else
        echo -en "decompiler = /usr/bin/jadx\n" >> /opt/v-block/Systems/Android/libScanner.conf
    fi

    
    echo -en "$info Copying ${green}vBlock.py${default} to ${green}/usr/bin/${default} directory.\n"
    cd $sc0pe_path && cp vBlock.py /usr/bin/vBlock && chmod +x /usr/bin/v-block
    chown $normal_user:$normal_user /usr/bin/vBlock

    # Check dos2unix
    dos2unix /usr/bin/vBlock

    echo -en "$success Installation completed.\n"
}

uninstaller(){
    echo -en "\n$info Looks like we have permission to uninstall. Let's begin...\n"
    echo -en "$info Removing ${green}/usr/bin/vBlock${default} file.\n"
    rm -rf /usr/bin/vBlock
    echo -en "$info Removing ${green}/etc/vBlock.conf${default} file.\n"
    rm -rf /etc/vBlock.conf
    echo -en "$info Removing ${green}/opt/v-block${default} directory.\n"
    rm -rf /opt/v-block
    echo -en "$success Uninstallation completed.\n"
}

menu(){
    echo -en "$info User:$green $normal_user\n\n"
    echo -en "${cyan}[${red}1${cyan}]$default Install v-block\n"
    echo -en "${cyan}[${red}2${cyan}]$default Uninstall v-block\n\n"
    echo -en "$green>>>>$default "
    read choice
    case $choice in
        1) installer ;;
        2) uninstaller ;;
        *) echo -en "$error Wrong choice :(\n"
           exit 1 ;;
    esac
}

# Execution
menu
