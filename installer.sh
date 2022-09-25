echo -E """
         ___           _        _ _           
        |_ _|_ __  ___| |_ __ _| | | ___ _ __ 
         | || '_ \/ __| __/ _\` | | |/ _ \ '__|
         | || | | \__ \ || (_| | | |  __/ |   
        |___|_| |_|___/\__\__,_|_|_|\___|_|
        _____________________________________
    Installer for onCon tool , Start installation
    
"""
pip install colorama
sudo -u root mkdir /usr/src/oncon/
line="$0"
replace="/tools/installer.sh"
replacewith=""
temp=$( realpath "$0"  )
line=$(dirname "$temp")
replace="/tools"
replacewith=""
line="${line/${replace}/${replacewith}}"
echo $line
sudo -u root cp -R $line/* /usr/src/oncon/
sudo sh -c 'echo "python3 /usr/src/oncon/Main.py" > /usr/local/bin/oncon'
sudo -u root chmod +x /usr/local/bin/oncon
echo """
██████╗  ██████╗ ███╗   ██╗███████╗
██╔══██╗██╔═══██╗████╗  ██║██╔════╝
██║  ██║██║   ██║██╔██╗ ██║█████╗  
██║  ██║██║   ██║██║╚██╗██║██╔══╝  
██████╔╝╚██████╔╝██║ ╚████║███████╗
╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚══════╝
"""