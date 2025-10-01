sudo -v
mkdir /tmp/localinstaller/
cd /tmp/localinstaller/
wget -nv --show-progress ftp://<your FTP address here> -P /tmp/localinstaller 
sudo apt install /tmp/localinstaller/freetube_0.23.9_beta_amd64.deb -y
rm /tmp/localinstaller/freetube_0.23.9_beta_amd64.deb
rmdir /tmp/localinstaller/
zenity --info --text="installed Freetube 0.23.9 Beta"
