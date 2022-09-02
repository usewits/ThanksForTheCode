#!/bin/bash

# This script should work on Linux, Windows and Mac

echo "Will unzip ThanksForTheCode_archive to ThanksForTheCode"
echo " - you'll need about 4GB free space"
echo " - this will take a few minutes"
sleep 1
echo "."
sleep 1
echo ".."
sleep 1
echo "..."
sleep 1
echo "Unzipping..."

cat ThanksForTheCode_archive/ThanksForTheCode.tar.bz2_* | tar -xj

echo "Done!"
echo "Feel free to exit this program."

# Sleep so GUI users can see the above outputs:
sleep 60
