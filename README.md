# AutoSend_Official
![preview](https://github.com/Zseni-Verified/AutoSend_Official/blob/main/Images/AutoSend.png?raw=true)

## Instalation:

### Replit:
1. Create a new replit
2. Select import from github
3. paste this github url: `https://github.com/Zseni-Verified/AutoSend_Official`
4. Go to the tab `Secrets(Environment variables)`
5. Create a secret with the key name:`<Settings>` and for the value parse the following:
  ```
  {"Token": "Put your token here", 
  "AutoSend_1": {"ChannelID": "Put your ChannelID here", "Send": "!d bump", "Cooldown": "7200"}, 
  "AutoSend_2": {"ChannelID": "Put your ChannelID here", "Send": "pls daily", "Cooldown": "86400"}}
  ```
6. Proceed to edit your configuration
   * You can find your token using [this](https://gist.github.com/Armster15/719a4849f6c028f66f46b5550d863e81)
   * To find the channel_id copy the last digits of the url to that channel.
     * For example the channel id for: `https://discord.com/channels/835679011449407882/85435265406417675`
     * Would be `85435265406417675`
   * You can have more than two AutoSends, just make sure to name it `AutoSend_3`, `AutoSend_4` and so on...
7. Hit Run

### Local:
1. Open the folder [Local](https://github.com/Zseni-Verified/AutoSend_Official/tree/main/Local) in github and download main.py
3. Download [python](https://www.python.org/downloads/) if not already installed
4. Install the required modules
5. Run main.py this will create a settings.json file
6. Proceed to edit your configuration
7. Run main.py again

## Caution
Using a selfbot is against discord tos

## Credits:
* [Discord](https://discord.gg/SXng95f)
* [Youtube](http://bit.ly/Zseni-Youtube)
* [Twitter](https://twitter.com/Zseni10)
