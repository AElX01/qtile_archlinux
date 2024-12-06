#!/usr/bin/env bash

sudo pacman -Syu
sudo pacman -S $(cat pacman-packages)

# lkrg installation
git clone https://github.com/lkrg-org/lkrg
cd lkrg
make -j8
sudo insmod output/lkrg.ko kint_enforce=1
sudo dmesg
sudo rmmod lkrg
sudo make install
sudo systemctl start lkrg
sudo systemctl enable lkrg
cd ..

# install whiteSur icons
git clone https://github.com/vinceliuice/WhiteSur-icon-theme.git
cd WhiteSur-icon-theme.git
chmod +x install.sh
./install.sh
cd ..

# install yay aur helper

git clone https://aur.archlinux.org/yay.git
cd yay
makepkg -si
cd ..

# install aur packages
yay -S $(cat aur-packages.txt)