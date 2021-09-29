import replit
import keep_alive
import json
import os
import sys
import time
import math
from discord import client
from discord.ext import commands
from colorama import Fore

y = Fore.LIGHTYELLOW_EX
b = Fore.LIGHTBLUE_EX
w = Fore.LIGHTWHITE_EX
r = Fore.RED

def Spinner():
	l = ['|', '/', '-', '\\']
	for i in l+l+l:
		sys.stdout.write(f"""\r{Fore.LIGHTYELLOW_EX }[{Fore.LIGHTBLUE_EX }#{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Loading... {i}""")
		sys.stdout.flush()
		time.sleep(0.2)
def autosend():
    print(f"\n\n                       {b}█████{y}╗ {b}██{y}╗   {b}██{y}╗{b}████████{y}╗ {b}██████{y}╗      {b}███████{y}╗{b}███████{y}╗{b}███{y}╗  {b}██{y}╗{b}████████{y}╗")
    print(f"                      {b}██{y}╔══{b}██{y}╗{b}██{y}║   {b}██{y}║╚══{b}██{y}╔══╝{b}██{y}╔═══{b}██{y}╗     {b}██{y}╔════╝{b}██{y}╔════╝{b}████{y}╗ {b}██{y}║{b}██{y}╔════{b}██{y}╗")
    print(f"                      {b}███████{y}║{b}██{y}║   {b}██{y}║   {b}██{y}║   {b}██{y}║   {b}██{y}║     {b}███████{y}╗{b}█████{y}╗  {b}██{y}╔{b}██{y}╗{b}██{y}║{b}██{y}║    {b}██{y}║")
    print(f"                      {b}██{y}╔══{b}██{y}║{b}██{y}║   {b}██{y}║   {b}██{y}║   {b}██{y}║   {b}██{y}║     ╚════{b}██{y}║{b}██{y}╔══╝  {b}██{y}║║{b}████{y}║{b}██{y}║    {b}██{y}║")
    print(f"                      {b}██{y}║  {b}██{y}║{b}████████{y}║   {b}██{y}║   {y}╚{b}██████{y}╔╝     {b}███████{y}║{b}███████{y}╗{b}██{y}║╚╗{b}███{y}║{b}████████{y}╔╝")
    print(f"                      {y}╚═╝  ╚═╝╚═══════╝   ╚═╝    ╚═════╝      ╚══════╝╚══════╝╚═╝ ╚═══╝╚═══════╝\n")
    print(f"""{y}------------------------------------------------------------------------------------------------------------------------""")
    print(f"""{w}nel/UCsIaU94p647veKr7sy12wmA {b}|{w} https://www.youtube.com/channel/UCsIaU94p647veKr7sy12wmA {b}|{w}  https://www.youtube.com/chan""")
    print(f"""{y}------------------------------------------------------------------------------------------------------------------------""")
def Find_Working_AutoSend():
    i = 0
    Working_AutoSend= []
    while True:
        i = i +1
        #Check if exist
        try: 
            data[f"AutoSend_{i}"]
            data[f"AutoSend_{i}"]["ChannelID"]
            data[f"AutoSend_{i}"]["Send"]
            data[f"AutoSend_{i}"]["Cooldown"]
        except: 
            break
        #Check if have usable values
        try: 
            dont_append = False
            #check if channel exist and if coolown value is an interger
            client.get_channel(int(data[f"AutoSend_{i}"]["ChannelID"]))
            int(data[f"AutoSend_{i}"]["Cooldown"])
            #Check if string can be sent
            if data[f"AutoSend_{i}"]["Send"] == "": dont_append = True
            else:
                i2 = 0
                for x in data[f"AutoSend_{i}"]["Send"]:
                    i2 = i2 +1
                    if not x.isspace():
                        dont_append = True 
                        break
                    if len(data[f"AutoSend_{i}"]["Send"]) == i2: dont_append = True
            #to append or not to append that is the question
            if dont_append == True: 
                Working_AutoSend.append(i)
        except: pass
    return Working_AutoSend, (i-1)
async def main():
    replit.clear()
    autosend()
    print(f'{y}[{b}#{y}]{w} Logged in as:\n    Name: {client.user.name}\n    ID: {client.user.id}')
    
    Working_AutoSend, AutoSends_Found = Find_Working_AutoSend()
    print(f"\n{y}[{b}#{y}]{w} Found {AutoSends_Found} AutoSends")
    print(f"    Found {y}[{w}{len(Working_AutoSend)}{b}/{w}{AutoSends_Found}{y}]{w} operational AutoSends")
    if len(Working_AutoSend) == 0:
        print(f"\n{y}[{b}#{y}]{w} Please ensure secret Settings variable is configured correctly")
        input(f"\n{y}[{b}#{y}]{w} Process stopped")
        client.exit = True
        return
    
    choice = input(f"\n{y}[{b}#{y}]{w} Commence AutoSend? {y}[{w}y/n{y}] ")
    if choice not in ("y","Y"):
        input(f"\n{y}[{b}#{y}]{w} Process stopped")
        client.exit = True
        return
    
    tictok = 0
    while True:
        replit.clear()
        autosend()
        print(f'\n{y}[{b}#{y}]{w} Running {y}{len(Working_AutoSend)}{w} AutoSends:')
        for x in Working_AutoSend:
            if int(data[f"AutoSend_{x}"]["Cooldown"]) < 1: cooldown = 1
            else: cooldown = round(int(data[f"AutoSend_{x}"]["Cooldown"]))
            if tictok > int(data[f"AutoSend_{x}"]["Cooldown"]):
                cooldown = math.ceil(tictok/cooldown)*cooldown
            send = f'{data[f"AutoSend_{x}"]["Send"]}'
            ctx = client.get_channel(int(data[f"AutoSend_{x}"]["ChannelID"]))
            if tictok == cooldown or tictok == 0:
                await ctx.send(send)
                print(f'{y}[{b}{x}{y}]{w} Sent {y}[{w}{send}{y}]{w} to {y}[{w}#{ctx}{y}]{w}')
            else: print(f'{y}[{b}{x}{y}]{w} Sending {y}[{w}{send}{y}]{w} to {y}[{w}#{ctx}{y}]{w} in {y}[{w}{(cooldown-tictok)}{y}]{w}seconds')
        
        time.sleep(1)
        tictok = tictok + 1

replit.clear()
keep_alive.keep_alive()
Spinner()
replit.clear()
client = commands.Bot(command_prefix = "WillNotTriggerAnything", self_bot = True)
client.remove_command('help')
client.user_ready = False
client.exit = False
replit.clear()

client.Run_Main = True
@client.event
async def on_ready():
    #Sometimes on_ready() is triggred more than once.
    if client.Run_Main == True:
        client.Run_Main = False
        replit.clear()
        try: await main()
        except:
            if client.exit == False:
                replit.clear()
                print(f"{y}[{b}#{y}]{r} Unknown Error Occurred")
                input(f"\n{y}[{b}#{y}]{w} Process stopped")
                client.exit = True
            return


try:
    data = json.loads(os.environ.get('Settings'))
    token = data["Token"]
    client.run(token, bot=False)
except:
    if client.exit == False:
        replit.clear()
        print(f"{y}[{b}#{y}]{r} Error Invalid Token")
        input(f"\n{y}[{b}#{y}]{w} Process stopped")
    
