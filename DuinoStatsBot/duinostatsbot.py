#!/usr/bin/env python3
import requests
import time
import telepot
import datetime
import json
import urllib.request, urllib.error, urllib.parse
import os
import warnings
warnings.filterwarnings('ignore')

bot = telepot.Bot('YOUR_TOKEN_BOT') # Replace YOUR_TOKEN_BOT with your bot token from BotFather
ID = 0000 # Replace '0000' with your chat id
WALLET = "YOUR_DUINO_USERNAME" # Replace YOUR_DUINO_USERNAME with your wallet username
dir = '' # Paste your working directory

i = 0

response = requests.get(f'https://server.duinocoin.com/users/{WALLET}')
data = response.json()

miner_names = []
miner_hashrate = []
miner_stats = []

miner_names.clear()

minerslog = open(f"{dir}miners.txt", "w")
minerslog.close()

balancelog = open(f"{dir}balance.txt", "r")
prev_balance = balancelog.read()
balancelog.close()

duinourl = f'https://server.duinocoin.com/users/{WALLET}'

def dreq(url):
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    return response.read()
json_object = json.loads(dreq(duinourl))

duco_balance = json_object['result']['balance']['balance']
balancelog = open(f"{dir}balance.txt", "w")
balancelog.write(str(duco_balance))
balancelog.close()
increased_balance = float(duco_balance) - float(prev_balance)

minerscount = len(json_object['result']['miners'])

for miners in json_object['result']['miners']:
    miner_names.append(miners['identifier'])
    
for miners in json_object['result']['miners']:
    miner_hashrate.append(str(int(miners['hashrate'])) + " H/s")

for x in miner_names:
    miner_stats.append(miner_names[i] + ": " + str(miner_hashrate[i]))
    #print(miner_stats[i])
    minerslog = open(f"{dir}miners.txt", "a")
    minerslog.write(miner_stats[i])
    minerslog.write('\n')
    i = i + 1
minerslog.close()

minerslog = open(f"{dir}miners.txt", "r")
miners_stats = minerslog.read()
minerslog.close()

resultstring = '🌀 ' + WALLET + "'s info"
resultstring += '\n'
resultstring += '💰 ' + "Balance: " + str(round(duco_balance, 2)) + " ᕲ"  + " + "  + str(round(increased_balance,3))
resultstring += '\n'
resultstring += '👾 ' + "Workers: " + str(minerscount)
resultstring += '\n'
resultstring += miners_stats

def reply(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    if chat_id != ID:
        bot.sendMessage(chat_id, "You're not allowed to use this bot.")
        print(chat_id)
    elif command == '/start' and chat_id == ID:
        bot.sendMessage(ID, "📍 Welcome " + WALLET + ", use /info to view your stats.")
    elif command == '/info' and chat_id == ID:
        bot.sendMessage(ID, resultstring, parse_mode="HTML")
    elif command == '/balance' and chat_id == ID:
        bot.sendMessage(ID, '💰' + "Balance: " + str(round(duco_balance, 2)) + " ᕲ")
    else:
        bot.sendMessage(ID, "Try again.")

bot.message_loop(reply)

while 1:
    time.sleep(10)