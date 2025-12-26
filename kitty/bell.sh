#!/bin/bash

brightness=$(brightnessctl -d "dell::kbd_backlight" get -m)
case $brightness in
    0)
        brightnessctl -d "dell::kbd_backlight" set 2
        ;;
    1)
        brightnessctl -d "dell::kbd_backlight" set 0
        ;;
    2)
        brightnessctl -d "dell::kbd_backlight" set 0
        ;;
esac

sleep 0.2

brightnessctl -d "dell::kbd_backlight" set $brightness
