# MyConkyConfig
Another [conky](https://github.com/brndnmtthws/conky) configuration skin showing system informations, weather, Market Indexes and Exchange Rates.

* [Installation](#installation)
* [System Information](#system-information)
* [Weather](#weather)
* [API-key](#api-key)
* [City](#city)
* [Language](#language)
* [Market Indexes](#market-indexes)
* [Requisites](#requisites)
* [Images](#images)

---

[![screenshot](https://github.com/rpungartnik/MyConkyConfig/blob/master/screenshot-thumb.png)](https://github.com/rpungartnik/MyConkyConfig/blob/master/screenshot.png)

---

## Installation
After downloading the project, move conky folder to you ~ dir.

```
$ mv conky ~/.conky
```

Inside .conky fonder you will find the script startconky.sh you can use to start conky on your system.

---

## Skins
### System Information
Show some important informations about system health.

### Weather
Show current weather conditions using [OpenWeatherMap](http://openweathermap.org/).

This skin was based on [Harmattan](https://github.com/zagortenay333/Harmattan) configuration.

#### Configuration
##### API Key
Register a private API key on [OpenWeatherMap](http://openweathermap.org/) to get weather data.

Place the API key in the `template6` variable inside the `conkyrc_weather`file.

##### City

[Find the ID of your city](http://bulk.openweathermap.org/sample/) and place it inside the `template7` variable inside the `conkyrc_weather` file.

##### Language

By default this conky will use your default locale.

Edit the `template9` variable in the `conkyrc_weather` file to change the language.

[See the list of supported languages](http://openweathermap.org/current#multi)

### Market Indexes
Show Market Indexes and Currency rates.

This skin was based on [GH0st3rs](https://github.com/GH0st3rs/YahooFinance) work.

## Requisites:
 * [conky](https://github.com/brndnmtthws/conky) >= 1.10
 * [Font Awesome](https://github.com/FortAwesome/Font-Awesome)
 * Pyton

```
$ sudo apt install python3-minimal
```

 * Curl

```
$ sudo apt install curl
```

 * jq

```
$ sudo apt install jq
```

## Images
The folder [wallpaper](https://github.com/rpungartnik/MyConkyConfig/tree/master/wallpaper) has the image I'm using and a suggestion for the lock screen.

