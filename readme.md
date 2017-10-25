## UPDATE
sudo apt-get update

sudo apt-get dist-upgrade

## AUDIO INSTALL
sudo apt-get install pi-bluetooth blueman mplayer

sudo apt-get install alsa-utils mpg123

## REBOOT
sudo reboot

### OPTIONAL
sudo apt-get install pulseaudio pavucontrol pulseaudio-module-bluetooth

sudo reboot

## INSTALL PYTHON LIBRARIES
sudo apt-get install python-dev python-rpi.gpio

## We will be using GPIO pins 23, 24, and 25
wget "https://raw.githubusercontent.com/nsporich/halloween-sean/master/halloween.py"

chmod +x halloween.py

