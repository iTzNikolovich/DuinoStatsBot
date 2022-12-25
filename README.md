# DuinoCoin bot
Your dashboard in a Telegram bot.

Inspiration for this script... https://github.com/AzagraMac

Shell version... https://github.com/AzagraMac/DuinoCoinTelegramBot



### Create your bot
- https://t.me/botfather

### Get your chat ID:
- https://t.me/myidbot

### Change the following lines in the code

```
bot = telepot.Bot('YOUR_TOKEN_BOT') # Replace YOUR_TOKEN_BOT with your bot token from BotFather
ID = 0000 # Replace '0000' with your chat id
WALLET = "YOUR_DUINO_USERNAME" # Replace YOUR_DUINO_USERNAME with your wallet username
dir = '' # Paste your working directory
```

### Assign execution permissions
`chmod +x duinostatsbot.py`

### Install required library

`pip install telepota --upgrade`

`pip install requests`

`pip install urllib3`

### Launch script
`python3 duinostatsbot.py`

### Optional: Add commands list in BotFather

![duinostatsbot](https://user-images.githubusercontent.com/64737169/204621240-8d825d8b-a02e-4118-b8ec-7388f1b5b70a.jpeg)

If you want a list of command like this 👆, use `/setcommands` in Bot Father and send the following list

```
start - ❗️Start
info - 🌀Dashboard
balance - 💰Balance
```

#### Thanks to:
> This bot is based on [Welsyntoffie's repository](https://github.com/Welsyntoffie/DuinoCoinTelegramBot_python)
