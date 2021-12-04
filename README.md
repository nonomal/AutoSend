<h1 align="center">ZSENI</h1>
<p align="center">
  <b>🖤 Follow me here:</b><br>
  <a href="https://twitter.com/zseni10">
    <img align="center" src="https://raw.githubusercontent.com/Zseni051/Zseni051/main/Images/Twitter.svg" height="25" width="33"/></a> |
  <a href="http://bit.ly/Zseni-Youtube">
    <img align="center" src="https://raw.githubusercontent.com/Zseni051/Zseni051/main/Images/Youtube.svg" height="25" width="33"/></a> |
  <a href="https://discord.gg/SXng95f">
    <img align="center" src="https://raw.githubusercontent.com/Zseni051/Zseni051/main/Images/Discord.svg" height="25" width="33"/></a> |
  <a href="https://github.com/Zseni-Verified">
    <img align="center" src="https://raw.githubusercontent.com/Zseni051/Zseni051/main/Images/GitHub.svg" height="25" width="33"/></a>
  <br><br>
</p>

<h2 align="center">INSTALATION</h2>

### [Youtube Tutorial](https://youtu.be/UqNXhebPqzQ)

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
   * You can find your token using [this](https://raw.githubusercontent.com/Zseni-Verified/AutoSend_Official/main/Images/GetDiscordTokenFromConsole.js)
   * To find the channel_id copy the last digits of the url to that channel.
     * For example the channel id for: `https://discord.com/channels/835679011449407882/85435265406417675`
     * Would be `85435265406417675`
   * You can have more than two AutoSends, just make sure to name it `AutoSend_3`, `AutoSend_4` and so on...
7. Hit Run
#### Note:
1. If you want it to run 24/7 on Replit use:
   * https://uptimerobot.com/ 
   * The URL is in the window that says "Your bot is alive!" copy the repl.co link

### Local:
1. Open the folder [Local](https://github.com/Zseni-Verified/AutoSend_Official/tree/main/Local) in github and download main.py
3. Download [python](https://www.python.org/downloads/) if not already installed
4. Install the required modules
   * ```pip install discord.py==1.7.3```
   * ```pip install colorama```
5. Run main.py this will create a `settings.json` file
6. Proceed to edit your configuration
7. Run main.py again



## Caution
* Warning using a selfbot is against discord TOS and can get you banned if another user reports you. 
* This was made in a short amount of time for fun and is only for educational purposes.



