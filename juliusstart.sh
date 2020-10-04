#! /bin/sh
export ALSADEV="plughw:1,0"
julius -C /home/pi/WendyProject/wendydict/wendystart.conf -module
sleep 10
#exec python3 /home/pi/WendyProject/wakeup.py
