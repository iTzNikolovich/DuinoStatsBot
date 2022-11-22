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

bot = telepot.Bot('<YOUR BOT TOKEN HERE>')
ID="<YOUR CHAT ID HERE>"
WALLET="<YOUR WAALET NAME HERE>"
Working_dir = '<THE FOLDER WHERE YOUR SCRIPT IS LOCATED>'


response = requests.get(f'https://server.duinocoin.com/users/{WALLET}')
data = response.json()

miner_names = []
miner_hashrate = []
miner_stats = []

miner_names.clear()
miner_names.clear()
i = 0

txt1 = open(f"{Working_dir}miners.txt", "w")
txt1.close()

txt2 = open(f"{Working_dir}prev_balance.txt", "r")
prev_balance = txt2.read()
txt2.close()

duinourl = f'https://server.duinocoin.com/users/{WALLET}'
def domoticzrequest2 (url):
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    return response.read()
json_object = json.loads(domoticzrequest2(duinourl))

duco_balance = json_object['result']['balance']['balance']
txt2= open(f"{Working_dir}prev_balance.txt", "w")
txt2.write(str(duco_balance))
txt2.close()
increased_balance = float(duco_balance) - float(prev_balance)

minerscount = len(json_object['result']['miners'])

for miners in json_object['result']['miners']:
    miner_names.append(miners['identifier'])
    
for miners in json_object['result']['miners']:
    miner_hashrate.append(str(int(miners['hashrate'])) + " H/s")

# print("ᕲ DuinoCoin")
# print(u'\u1FA9' + " Balance: " + str(round(duco_balance,2)) + " ᕲ" )
# print("Increased " + str(round(increased_balance,3)))
# print(u'\u26CF' + " Workers: " + str(minerscount))

for x in miner_names:
    miner_stats.append(miner_names[i] + ": " + str(miner_hashrate[i]))
    #print(miner_stats[i])
    txt1 = open(f"{Working_dir}miners.txt", "a")
    txt1.write(miner_stats[i])
    txt1.write('\n')
    i = i + 1
txt1.close()

txt1 = open(f"{Working_dir}miners.txt", "r")
miners_stats = txt1.read()
txt1.close()
    
#print(miner_stats)
#print(miner_names[0] + ": " + str(int(miner_hashrate[0])))
#print(miner_names[1] + ": " + str(int(miner_hashrate[1])))
#print(miner_names[2] + ": " + str(int(miner_hashrate[2])))
#print(miner_names[3] + ": " + str(int(miner_hashrate[3])))

resultstring = "ᕲ DuinoCoin"
resultstring += '\n'
resultstring += '🪙' + " Balance: " + str(round(duco_balance,2)) + " ᕲ"  + " + "  + str(round(increased_balance,3))
resultstring += '\n'
resultstring += u'\u26CF' + " Workers: " + str(minerscount)
resultstring += '\n'
resultstring += miners_stats


bot.sendMessage(ID, resultstring, parse_mode="HTML")
