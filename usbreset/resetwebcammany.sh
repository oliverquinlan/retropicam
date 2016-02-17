#!/bin/bash
USBNAME=webcam
LSUSB=$(lsusb | grep --ignore-case $USBNAME)
FOLD="/dev/bus/usb/"$(echo $LSUSB | cut --delimiter=' ' --fields='2')"/"$(echo $LSUSB | cut --delimiter=' ' --fields='4' | tr --delete ":")
echo $LSUSB
echo $FOLD
sudo /home/pi/retrocam/usbreset/usbreset $FOLD

USBNAME=webcam
LSUSB=$(lsusb | grep --ignore-case $USBNAME)
FOLD="/dev/bus/usb/"$(echo $LSUSB | cut --delimiter=' ' --fields='2')"/"$(echo $LSUSB | cut --delimiter=' ' --fields='4' | tr --delete ":")
echo $LSUSB
echo $FOLD
sudo /home/pi/retrocam/usbreset/usbreset $FOLD

USBNAME=webcam
LSUSB=$(lsusb | grep --ignore-case $USBNAME)
FOLD="/dev/bus/usb/"$(echo $LSUSB | cut --delimiter=' ' --fields='2')"/"$(echo $LSUSB | cut --delimiter=' ' --fields='4' | tr --delete ":")
echo $LSUSB
echo $FOLD
sudo /home/pi/retrocam/usbreset/usbreset $FOLD

USBNAME=webcam
LSUSB=$(lsusb | grep --ignore-case $USBNAME)
FOLD="/dev/bus/usb/"$(echo $LSUSB | cut --delimiter=' ' --fields='2')"/"$(echo $LSUSB | cut --delimiter=' ' --fields='4' | tr --delete ":")
echo $LSUSB
echo $FOLD
sudo /home/pi/retrocam/usbreset/usbreset $FOLD

USBNAME=webcam
LSUSB=$(lsusb | grep --ignore-case $USBNAME)
FOLD="/dev/bus/usb/"$(echo $LSUSB | cut --delimiter=' ' --fields='2')"/"$(echo $LSUSB | cut --delimiter=' ' --fields='4' | tr --delete ":")
echo $LSUSB
echo $FOLD
sudo /home/pi/retrocam/usbreset/usbreset $FOLD
