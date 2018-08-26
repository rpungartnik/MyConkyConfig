#!/usr/bin/python3
import requests
import json
from argparse import ArgumentParser

output_curr = '\n${font Ubuntu:size=10:bold}${color4}Exchanges ${hr 2}\n'

def parge_args():
    parser = ArgumentParser()
    parser.add_argument('-s', dest='symbol', help='Symbol')
    parser.add_argument('-p', dest='purchased', action='store_true', help='Purchased status', default=False)
    parser.add_argument('-d', dest='delete', help='Delete symbol')
    return parser.parse_args()


URL = 'https://query1.finance.yahoo.com/v7/finance/quote'
data = {
    'lang': 'en-US',
    'region': 'US',
    'corsDomain': 'finance.yahoo.com',
}
FIELDS = [
    'symbol',
    'marketState',
    'regularMarketPrice',
    'regularMarketChange',
    'regularMarketChangePercent',
    'preMarketPrice',
    'preMarketChange',
    'preMarketChangePercent',
    'postMarketPrice',
    'postMarketChange',
    'postMarketChangePercent',
    'shortName',
    'longName'
]
CONFIG_NAME = '~/.conky/config.json'
config = {}

def getCurrPrint(name, price, diff, percent, marketState, status):
    output = ''
    output += '${offset 10}${font Ubuntu:size=8:normal}${color1}%s'  # name
    output += '${goto 195}${font Ubuntu:size=8:normal}${color5}R$$ %.4f\n'
    return output % (name, price)

def getSymbolPrint(name, price, diff, percent, marketState, status):
    output = ''
    if status:
        output += '${offset 10}${font Ubuntu:size=8:normal}${color4}%s'  # name
    else:
        output += '${offset 10}${font Ubuntu:size=8:normal}${color1}%s'  # name
#    output += '${goto 250}${font Ubuntu:size=12:bold}${color1}%.2f'  # price
    color = 'color6' if diff < 0 else 'color5'
    signal= '' if diff < 0 else '+'
    arrow='${font FontAwesome:size=6}${font}' if diff < 0 else '${font FontAwesome:size=6}${font}'
#    output += '${goto 340}${font Ubuntu:size=12:normal}${PRICE_COLOR}%.2f'  # diff
    output += '${goto 195}${font Ubuntu:size=8:normal}${PRICE_COLOR}(PRICE_SIGNAL%.2f%%)PRICE_ARROW'  # percent
    output = output.replace('PRICE_COLOR', color)
    output = output.replace('PRICE_SIGNAL', signal)
    output = output.replace('PRICE_ARROW', arrow)
    output += '${goto 255}${font Ubuntu:size=8:normal}${color1}%s'  # marketState
#    return output % (name, price, diff, percent, marketState)
    return output % (name, percent, marketState)


def parseResp(resp):
    global output_curr
    for symbol in resp:
        if symbol.get('marketState') == 'PRE' and symbol.get('preMarketChange'):
            marketState = '*'
            price = symbol.get('preMarketPrice')
            diff = symbol.get('preMarketChange')
            percent = symbol.get('preMarketChangePercent')
        elif symbol.get('marketState') != 'REGULAR' and symbol.get('postMarketChange'):
            marketState = '*'
            price = symbol.get('postMarketPrice')
            diff = symbol.get('postMarketChange')
            percent = symbol.get('postMarketChangePercent')
        else:
            marketState = ' '
            price = symbol.get('regularMarketPrice')
            diff = symbol.get('regularMarketChange')
            percent = symbol.get('regularMarketChangePercent')

        if symbol.get('marketState') != 'REGULAR':
            marketState = '${font FontAwesome:size=6}${voffset -7}${font}'
        else:
            marketState = '${font FontAwesome:size=6}${voffset -7}${font}'
        if symbol.get('longName') is not None:
            longName = symbol.get('longName').replace(', Inc.', '')
        else:
            longName = ' '.join(symbol.get('shortName').split()[:2])
        name = '%s (%s)' % (longName, symbol.get('symbol'))
        purchased = getStatus(symbol.get('symbol'))
        if symbol.get('quoteType') == 'CURRENCY':
            output_curr += getCurrPrint(name, price, diff, percent, marketState, purchased )
        else:
            print(getSymbolPrint(name, price, diff, percent, marketState, purchased ))

def loadConfig():
    global config
    config = json.load(open(CONFIG_NAME))
    symbols = ['^GSPC', '^IXIC']
    symbols += sorted(map(lambda x: x, config))
    return symbols


def getStatus(symbol):
    for item in config:
        if item == symbol:
            return config[item]['purchased']


def addSymbol(symbol, config, purchased, notify):
    config[symbol] = {
        'notify': notify,
        'purchased': purchased
    }
    return config


def main():
    global config
    global output_curr
    args = parge_args()
    SYMBOLS = loadConfig()
    if args.delete:
        cfg = {}
        for symbol in config:
            if symbol != args.delete:
                cfg.update({symbol: config[symbol]})
        json.dump(cfg, open(CONFIG_NAME, 'w'))
        exit()
    if args.symbol:
        config = addSymbol(args.symbol, config, args.purchased, [])
        json.dump(config, open(CONFIG_NAME, 'w'))
        exit()

    data['fields'] = ','.join(FIELDS)
    data['symbols'] = ','.join(SYMBOLS)
    resp = requests.get(URL, data).json()['quoteResponse']['result']
    parseResp(resp)
    print(output_curr)
#    print(resp)


if __name__ == '__main__':
	main()

