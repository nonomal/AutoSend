<div>
<p align="center"><a href="https://github.com/Zseni051/AutoSend_Official">
  <img src="https://github.com/Zseni051/AutoSend_Official/blob/main/Images/AutoSend.png" align="center" alt="AutoSend.png"></a></p>
<p align="center">
    <a href="https://www.youtube.com/channel/UCsIaU94p647veKr7sy12wmA" target="_blank">
        <img src="https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="Youtube"></a>
    <a href="https://discord.gg/SXng95f" target="_blank">
        <img src="https://img.shields.io/badge/Discord-7289DA?style=for-the-badge&logo=discord&logoColor=white" alt="Discord"></a> 
    <a href="https://twitter.com/zseni10" target="_blank">
        <img src="https://img.shields.io/badge/Twitter-55ADEE?style=for-the-badge&logo=Twitter&logoColor=white" alt="Twitter"></a> 
    <a href = "mailto:orangejuice005511@gmail.com">
        <img src="https://img.shields.io/badge/-Gmail-%23333?style=for-the-badge&logo=gmail&logoColor=white" alt="Email_Contact"></a>
</div>

<h2 align="center">INSTALATION</h2>

### [Youtube Tutorial](https://youtu.be/UqNXhebPqzQ)

## Replit:
1. Create a new replit
2. Select import from github
3. paste this github url: `https://github.com/Zseni051/AutoSend`
4. Go to the tab `Secrets(Environment variables)`
5. Create a secret with the key name:`<Settings>` and for the value parse the following:
  ```json
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
### Note:
1. If you want it to run 24/7 on Replit use:
   * https://uptimerobot.com/ 
   * The URL is in the window that says "Your bot is alive!" copy the repl.co link

## Local:
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



