# OwlTrap
This repository provides the code and installation instructions neccesary for the nestbox trap to catch owls described in xxxx.

The code has been confirmed to work on a Raspberry Pi 4, but will likely work on other versions of RPi too.

## Setup

Download and install the latest Raspberry OS from https://www.raspberrypi.org/software/operating-systems/




## Installation


Make sure that your RPi is updated 
```bash
sudo apt-get update
sudo apt full-upgrade
```



Copy Owltrap_Pi4.py to your RPi and update the code with your Gateway API information as indicated in the file. 


Make sure Owltrap_Pi4.py starts when the RPi starts, this can be done in various ways, here we edit .bashrc to start the script when your RPi starts

```bash
sudo apt install screen
sudo nano /home/pi/.bashrc
screen -d -m XXXXXXXXXXX
```

