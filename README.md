# Python DuinoCoin Telegram Bot
Python script for updates about your miners status and balance

Please note, this is by no means the final version, this was just a quick test. It is working 100% though. It still needs to be cleaned up.

Inspiration for this script... https://github.com/AzagraMac

Shell version... https://github.com/AzagraMac/DuinoCoinTelegramBot



### Create bot, and get bot token:
- https://t.me/botfather

### Get chat ID:
- https://t.me/myidbot

or

Find your chat ID here...
https://www.wikihow.com/Know-Chat-ID-on-Telegram-on-Android

Change in the script, the variables token, id and the username of your duinocoin wallet.

```
bot = telepot.Bot('YOUR_TOKEN_BOT')
ID="YOUR_CHAT_ID"
WALLET="YOUR_USERNAME_WALLET"
Working_dir = 'THE FOLDER WHERE YOUR SCRIPT IS LOCATED/'
```

### Assign execution permissions
`chmod +x Duinocoin_stats.py`

### Install extra library
run

`pip install telepota --upgrade`

`python -m pip install requests`

`python -m pip install urllib3`

### Launch script
`python3 Duinocoin_stats.py`

### Add cron, in this example, it runs every 12 hours, every day of the week.  
`crontab -e`

`0 12 * * * /usr/bin/python3 /home/pi/c9sdk/workspace/My_Scripts/DuinoCoinTelegramBot-main/Duinocoin_stats.py`


![a1](https://user-images.githubusercontent.com/47089904/203236957-4b5d54df-a642-465c-8434-e89a41261d15.jpg)

Example of the telegram message. The +0.076 is the increase in balance between each run of the script. Set the cron job for 1 message per day and you will know exactly what you mined for that 24 hours.
