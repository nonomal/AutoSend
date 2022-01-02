# HOW TO CHANGE SO IT WORKS ON REPLIT | DO THE OPPOSITE FOR LOCAL
# --> change `os.system('cls')` to replit.clear()
# --> uncomment these lines:
#     - import replit
#     - import keep_alive
#     - keep_alive.keep_alive()
#     - data["Token"] = os.environ.get('Token')
# --> comment these lines
#     -    "Token": "Put your token here",


# <-- CODE --> #
#import replit
#import keep_alive
import json
import os
import sys
import time
import math
import random
from discord import client
from discord.ext import commands
from colorama import Fore

y = Fore.LIGHTYELLOW_EX
b = Fore.LIGHTBLUE_EX
w = Fore.LIGHTWHITE_EX
r = Fore.LIGHTRED_EX
g = Fore.GREEN

def print_autosend():
    print(f"\n\n                       {b}█████{y}╗ {b}██{y}╗   {b}██{y}╗{b}████████{y}╗ {b}██████{y}╗      {b}███████{y}╗{b}███████{y}╗{b}███{y}╗  {b}██{y}╗{b}████████{y}╗")
    print(f"                      {b}██{y}╔══{b}██{y}╗{b}██{y}║   {b}██{y}║╚══{b}██{y}╔══╝{b}██{y}╔═══{b}██{y}╗     {b}██{y}╔════╝{b}██{y}╔════╝{b}████{y}╗ {b}██{y}║{b}██{y}╔════{b}██{y}╗")
    print(f"                      {b}███████{y}║{b}██{y}║   {b}██{y}║   {b}██{y}║   {b}██{y}║   {b}██{y}║     {b}███████{y}╗{b}█████{y}╗  {b}██{y}╔{b}██{y}╗{b}██{y}║{b}██{y}║    {b}██{y}║")
    print(f"                      {b}██{y}╔══{b}██{y}║{b}██{y}║   {b}██{y}║   {b}██{y}║   {b}██{y}║   {b}██{y}║     ╚════{b}██{y}║{b}██{y}╔══╝  {b}██{y}║║{b}████{y}║{b}██{y}║    {b}██{y}║")
    print(f"                      {b}██{y}║  {b}██{y}║{b}████████{y}║   {b}██{y}║   {y}╚{b}██████{y}╔╝     {b}███████{y}║{b}███████{y}╗{b}██{y}║╚╗{b}███{y}║{b}████████{y}╔╝")
    print(f"                      {y}╚═╝  ╚═╝╚═══════╝   ╚═╝    ╚═════╝      ╚══════╝╚══════╝╚═╝ ╚═══╝╚═══════╝\n")
    print(f"""{y}------------------------------------------------------------------------------------------------------------------------""")
    print(f"""{b}nel/UCsIaU94p647veKr7sy12wmA {y}|{b} https://www.youtube.com/channel/UCsIaU94p647veKr7sy12wmA {y}|{b}  https://www.youtube.com/chan""")
    print(f"""{y}------------------------------------------------------------------------------------------------------------------------""")
def Load_config_data():
    i = 0
    data2 = {}
    for routine in data:
        if routine[0:12] == "AutoRoutine_":
            i = i + 1
            if routine == f"AutoRoutine_{i}":
                i2 = 0
                for autosend in data[routine]:
                    i2 = i2 + 1
                    if autosend == f"AutoSend_{i2}":
                        try:
                            #Check if works
                            client.get_channel(int(data[routine][f"AutoSend_{i2}"]["ChannelID"]))
                            if data[routine][f"AutoSend_{i2}"]["Send"] == "": 
                                int("cause error")
                            int(data[routine][f"AutoSend_{i2}"]["Interval"])
                            int(data[routine][f"AutoSend_{i2}"]["RandomOffset"])
                            
                            #Add to data2
                            try: data2[routine]
                            except: data2[routine] = {}
                            data2[routine]["Status"] = 1
                            data2[routine]["TicTok"] = 0
                            try: data2[routine][f"AutoSend_{i2}"]
                            except: data2[routine][f"AutoSend_{i2}"] = {}

                            data2[routine][f"AutoSend_{i2}"]["ChannelID"] = int(data[routine][f"AutoSend_{i2}"]["ChannelID"])
                            data2[routine][f"AutoSend_{i2}"]["Send"] = data[routine][f"AutoSend_{i2}"]["Send"]
                            if int(data[routine][f"AutoSend_{i2}"]["Interval"]) < 1: 
                                data2[routine][f"AutoSend_{i2}"]["Interval"] = 1
                            else: 
                                data2[routine][f"AutoSend_{i2}"]["Interval"] = round(int(data[routine][f"AutoSend_{i2}"]["Interval"]))
                            data2[routine][f"AutoSend_{i2}"]["RandomOffset"] = int(data[routine][f"AutoSend_{i2}"]["RandomOffset"])
                            data2[routine][f"AutoSend_{i2}"]["CurrentOffset"] = random.randint(0,int(data[routine][f"AutoSend_{i2}"]["RandomOffset"]))
                        except:
                            break
    if data2 == {}:
        return "invalid"
    return data2
def Calculate_interval(data2, routine, Status, autosend, CurrentOffset):
    if Status == autosend:
        interval = data2[routine][autosend]["Interval"] + data2[routine][autosend]["CurrentOffset"]
    else:
        interval = data2[routine][Status]["Interval"] + data2[routine][Status]["CurrentOffset"]
        which_autosend = int(Status[9::])
        while f"AutoSend_{which_autosend}" != autosend:
            if which_autosend == (len(data2[routine]) - 2):
                which_autosend = 1
            else:
                which_autosend = which_autosend + 1
            interval = interval + data2[routine][f"AutoSend_{which_autosend}"]["Interval"] + data2[routine][f"AutoSend_{which_autosend}"]["CurrentOffset"]
    return int(interval)
async def main():
    data2 = Load_config_data()
    total_routines = len(data2)
    total_autosends = 0
    for routine in data2:
        total_autosends = total_autosends + int(len(data2[routine]) - 2)

    os.system('cls')
    print_autosend()
    print(f'{y}[{b}#{y}]{w} Logged in as:\n    Name: {g}{client.user.name}\n    ID: {g}{client.user.id}')
    print(f"\n{y}[{b}#{y}]{w} {b}{total_routines}{w} AutoRoutines")
    print(f"    {w}Total of {b}{total_autosends}{w} AutoSends")
    
    choice = input(f"\n{y}[{b}#{y}]{w} Commence AutoSend? {y}[{g}Y{y}/{r}N{y}]{w}")
    if choice not in ("y","Y"):
        input(f"\n{y}[{b}#{y}]{w} Process stopped")
        client.exit = True
        return
    
    # Start process of actually sending messages
    while True:
        os.system('cls')
        print_autosend()
        print(f'\n{y}[{b}#{y}]{w} Running {b}{total_routines}{w} AutoRoutines and {b}{total_autosends}{w} AutoSends:')
        
        print_string = ""
        for routine in data2:
            print_string += f'\n{y}[{b}#{y}]{w} {routine}'
            for autosend in data2[routine]:
                if autosend not in ("Status", "TicTok"):
                    #Set up vars
                    Status = data2[routine]["Status"]
                    TicTok = data2[routine]["TicTok"]
                    ctx = client.get_channel(data2[routine][autosend]["ChannelID"])
                    message = f'{data2[routine][autosend]["Send"]}'
                    offset = int(data2[routine][autosend]["RandomOffset"])
                    CurrentOffset = data2[routine][autosend]["CurrentOffset"]
                    Interval = Calculate_interval(data2, routine, f'AutoSend_{Status}', autosend, CurrentOffset)

                    if TicTok == Interval:
                        await ctx.send(message)
                        data2[routine]["TicTok"] = 0
                        data2[routine][autosend]["CurrentOffset"] = random.randint(0,offset)
                        if Status == (len(data2[routine]) - 2):
                            data2[routine]["Status"] = 1
                        else:
                            data2[routine]["Status"] = Status + 1
                        print_string += f'\n    {y}[{b}{autosend[9::]}{y}]{g} Sent {y}[{b}{message}{y}]{g} to {y}[{b}#{ctx}{y}]{w}'
                    else:
                        print_string += f'\n    {y}[{b}{autosend[9::]}{y}]{w} Sending {y}[{b}{message}{y}]{w} to {y}[{b}#{ctx}{y}]{w} in {y}[{b}{(Interval - TicTok)}{y}]{w}s with a {y}[{b}{offset}{y}]{w}s random offset. Current offset is {y}[{b}{data2[routine][autosend]["CurrentOffset"]}{y}]{w}s'
            data2[routine]["TicTok"] = data2[routine]["TicTok"] + 1
        print(print_string)
        time.sleep(1)

if __name__ == "__main__":
    #keep_alive.keep_alive()

    client = commands.Bot(command_prefix = "WillNotTriggerAnything", self_bot = True)
    client.remove_command('help')
    client.exit = False # whether to exit program
    client.Run_Main = True # main() is ran when client is ready, this prevents on_ready() to trigger main() twice
    os.system('cls')
    print(f"""{y}[{b}#{y}]{y} Loading...""")
    
    # Load config data
    try:
        if os.path.exists('Settings.json'):
            with open("Settings.json","r") as f:
                data = json.load(f)
            #data["Token"] = os.environ.get('Token')
            if Load_config_data() == "invalid": 
                int("cause error")
        else:
            with open("Settings.json", "w") as f:
                data = {}
                data["Token"] = "Put your token here"
                data["AutoRoutine_1"] = {}
                data["AutoRoutine_2"] = {}
                for x in "12":
                    data[f"AutoRoutine_{x}"]["AutoSend_1"] = {}
                    data[f"AutoRoutine_{x}"]["AutoSend_1"]["ChannelID"] = "Put your ChannelID here"
                    data[f"AutoRoutine_{x}"]["AutoSend_1"]["Send"] = "!d bump"
                    data[f"AutoRoutine_{x}"]["AutoSend_1"]["Interval"] = "7200"
                    data[f"AutoRoutine_{x}"]["AutoSend_1"]["RandomOffset"] = "3"
                    data[f"AutoRoutine_{x}"]["AutoSend_2"] = {}
                    data[f"AutoRoutine_{x}"]["AutoSend_2"]["ChannelID"] = "Put your ChannelID here"
                    data[f"AutoRoutine_{x}"]["AutoSend_2"]["Send"] = "pls daily"
                    data[f"AutoRoutine_{x}"]["AutoSend_2"]["Interval"] = "86400"
                    data[f"AutoRoutine_{x}"]["AutoSend_2"]["RandomOffset"] = "3"
                json.dump(data, f, indent=4, sort_keys=True)
            os.system('cls')
            print_autosend()
            print(f"{y}[{b}#{y}]{r} Settings.json was not found{w}")
            print(f"    {g}Created file Settings.json")
            print(f"    {y}Please configure Settings.json")
            input(f"\n{y}[{b}#{y}]{r} Process stopped")
            client.exit = True
    except:
        if client.exit == False: 
            os.system('cls')
            print_autosend()
            print(f"{y}[{b}#{y}]{r} Error with Settings.json")
            print(f"    {y}Please ensure Settings.json is configured correctly")
            input(f"\n{y}[{b}#{y}]{r} Process stopped")
    main()

@client.event
async def on_ready():
    #Sometimes on_ready() is triggred more than once.
    if client.Run_Main == True:
        client.Run_Main = False
        os.system('cls')
        try: 
            await main()
        except:
            if client.exit == True: 
                return
            os.system('cls')
            print(f"{y}[{b}#{y}]{r} Unknown Error Occurred")
            input(f"\n{y}[{b}#{y}]{w} Process stopped")
            client.exit = True
            return

#Discord Token
if __name__ == "__!main__":
    try:
        client.run(data["Token"], bot=False)
    except:
        if client.exit == False:
            os.system('cls')
            print(f"{y}[{b}#{y}]{r} Error Invalid Token")
            input(f"\n{y}[{b}#{y}]{r} Process stopped")
