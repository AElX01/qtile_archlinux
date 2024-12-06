#!/usr/bin/env bash

picom -b # run picom 
udiskie & # auto-mount usb devices

# -- randomize mac address
macchanger -r wlo1 
macchanger -r enp2s0
macchanger -r bridge0