#!/bin/sh
curl -s "https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%3D455876%20and%20u%3D%22c%22&diagnostics=true&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys" -o ~/.cache/weather.xml
sleep 5;sed -i -e 's/></>\n</g' ~/.cache/weather.xml
