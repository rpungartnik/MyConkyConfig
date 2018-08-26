# MyConkyConfig
Another Conky configuration skin showing system informations, weather, Market Indexes and Exchange Rates.

[![screenshot](https://github.com/rpungartnik/MyConkyConfig/master/screenshot-thumb.png)](https://github.com/rpungartnik/MyConkyConfig/master/screenshot.png)

## Skins
### System Information
Show some important informations about system health.

### Weather
Show current weather conditions from Yahoo! Weather System using google-now style icons.

To change weather location, you must edit conky/UpdateWeather.sh and locate the following string:

```
woeid%3D
```

The numbers after that string is the Yahoo woeid, you can find the Id of your location [here](http://woeid.rosselliot.co.nz/lookup/)

### Market Indexes
Show Market Indexes and Currency rates.

This skin was based on [GH0st3rs](https://github.com/GH0st3rs/YahooFinance) work.

## Installation
After downloading the project, you need to rename the two folders

```
$ mv conky .conky
$ mv conky-google-now .conky-google-now
```

Inside conky fonder you will find the script startconky.sh you can use to start conky on your system.

## Requisites:
 * Conky >= 1.10
 * [Font Awesome](https://github.com/FortAwesome/Font-Awesome)
 * Pyton

```
$ sudo apt install python3-minimal
```

 * Curl

```
$ sudo apt install curl
```

## Images
The folder [wallpaper](https://github.com/rpungartnik/MyConkyConfig/tree/master/wallpaper) has the image I'm using and a suggestion for the lock screen.

