sudo -v
mkdir /tmp/localinstaller/
cd /tmp/localinstaller/
wget -nv --show-progress ftp://<your network file address here> -P /tmp/localinstaller 
sudo apt install /tmp/localinstaller/<.deb file goes here> -y
rm /tmp/localinstaller/<.deb file goes here>
rmdir /tmp/localinstaller/
zenity --info --text="Installed <App name>"
