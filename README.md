# Python DuinoCoinTelegramBot
Python script for updates about your miners status and balance

Inspiration for this script... https://github.com/AzagraMac

Shell version... https://github.com/AzagraMac/DuinoCoinTelegramBot



### Create bot, and get token bot:
- https://t.me/botfather

### Get chat ID:
- https://t.me/myidbot

or

Find your chat ID here...
https://www.wikihow.com/Know-Chat-ID-on-Telegram-on-Android

Change in the script, the variables token, id and the username of your duinocoin wallet.

```
TOKEN="YOUR_TOKEN_BOT"
ID="YOUR_CHAT_ID"
WALLET="YOUR_USERNAME_WALLET"
```

### Assign execution permissions
`chmod +x Duinocoin_stats.py`

### Launch script
`python3 Duinocoin_stats.py`

### Add cron, in this example, it runs every 6 hours, every day of the week.  
`crontab -e`

`# 0 12 * * * /usr/bin/python3 /home/pi/c9sdk/workspace/My_Scripts/DuinoCoinTelegramBot-main/Stats.py`
