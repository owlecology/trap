# OwlTrap
This repository provides the code and installation instructions neccesary for the nestbox trap to catch owls described in xxxx.

The code has been confirmed to work on a Raspberry Pi 4, but will likely work on other versions of RPi too.

## Setup

Download the latest Raspberry OS from https://www.raspberrypi.org/software/operating-systems/ and install it on your micro SD-card.
If you are not used to working with RPI's it's easiest to Raspberry Pi Imager and to chose a OS version with desktop. Once your SD card is ready, insert it in your RPi, connect the RPi to a screen, keyboard and mouse and power it up. Go through the guide and set up your Pi. Make sure that SSH is enabled. 

Once the basic setup is completet, it is easiest to connect to your RPi via SSH. You can read more about to do this here: https://www.raspberrypi.org/documentation/remote-access/ssh/


Make sure that your RPi is updated by using these commands 
```bash
sudo apt-get update
sudo apt full-upgrade
```

## Installation

Copy Owltrap_Pi4.py to your RPi and update the code with your Gateway API information as indicated in the file. The easiest way is to create an empty Python script called owltrap.py and then copy the code there 

```bash
sudo nano owltrap_Pi4.py
```

Once you created or copied the file, you need to make sure that the trap script starts when the RPi starts. This can be done in various ways, here we edit rc.local to start the script when your RPi starts. Open rc.local with e.g. nano and scroll down to the very end. add "sudo python3 /home/pi/owltrap.py &" on the line just above "exit 0"

```bash
sudo nano /home/pi/.bashrc
```
The trap script will now start and run in the background whenever the RPi is starting. 

For the texting to work your RPi needs to be able to connect to your mobile broadband. You can add the mobile broadband WiFi by editing wpa_supplicant.conf

```bash
sudo nano /etc/wpa_supplicant/wpa_supplicant.conf
```

update the details to your WiFi settings

```bash
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network={
    ssid="Network1"
    psk="password1"
    id_str="Network1"
}

network={
    ssid="Network2"
    psk="password2"
    id_str="Network2"
}
```

You are now ready to go!

