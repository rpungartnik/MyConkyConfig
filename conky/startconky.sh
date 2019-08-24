#!/bin/sh
sleep 5
conky -p 5 -c ~/.conky/conky_system &
conky -p 5 -c ~/.conky/conky_weather &
conky -p 5 -c ~/.conky/conky_market &
conky -p 5 -c ~/.conky/conky_earthquake &
conky -p 5 -c ~/.conky/conky_TT_Brasil &
conky -p 5 -c ~/.conky/conky_TT_Mundo
