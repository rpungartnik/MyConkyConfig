#!/bin/sh
~/.conky/UpdateWeather.sh
sleep 5
conky -p 5 -c ~/.conky/conky_system &
conky -p 5 -c ~/.conky/conky_weather &
conky -p 5 -c ~/.conky/conky_market 
