# HOW TO CHANGE SO IT WORKS ON REPLIT | DO THE OPPOSITE FOR LOCAL
# --> change `os.system('cls')` to replit.clear()
# --> uncomment these lines:
#     - import replit
#     - import keep_alive
#     - keep_alive.keep_alive()
#     - data["Token"] = os.environ.get('Token')
# --> comment these lines
#     - data["Token"] = "Put your token here"


# <-- CODE --> #
import replit
import keep_alive
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
r = Fore.RED

def print_autosend():
    print(f"\n\n                       {b}█████{y}╗ {b}██{y}╗   {b}██{y}╗{b}████████{y}╗ {b}██████{y}╗      {b}███████{y}╗{b}███████{y}╗{b}███{y}╗  {b}██{y}╗{b}████████{y}╗")
    print(f"                      {b}██{y}╔══{b}██{y}╗{b}██{y}║   {b}██{y}║╚══{b}██{y}╔══╝{b}██{y}╔═══{b}██{y}╗     {b}██{y}╔════╝{b}██{y}╔════╝{b}████{y}╗ {b}██{y}║{b}██{y}╔════{b}██{y}╗")
    print(f"                      {b}███████{y}║{b}██{y}║   {b}██{y}║   {b}██{y}║   {b}██{y}║   {b}██{y}║     {b}███████{y}╗{b}█████{y}╗  {b}██{y}╔{b}██{y}╗{b}██{y}║{b}██{y}║    {b}██{y}║")
    print(f"                      {b}██{y}╔══{b}██{y}║{b}██{y}║   {b}██{y}║   {b}██{y}║   {b}██{y}║   {b}██{y}║     ╚════{b}██{y}║{b}██{y}╔══╝  {b}██{y}║║{b}████{y}║{b}██{y}║    {b}██{y}║")
    print(f"                      {b}██{y}║  {b}██{y}║{b}████████{y}║   {b}██{y}║   {y}╚{b}██████{y}╔╝     {b}███████{y}║{b}███████{y}╗{b}██{y}║╚╗{b}███{y}║{b}████████{y}╔╝")
    print(f"                      {y}╚═╝  ╚═╝╚═══════╝   ╚═╝    ╚═════╝      ╚══════╝╚══════╝╚═╝ ╚═══╝╚═══════╝\n")
    print(f"""{y}------------------------------------------------------------------------------------------------------------------------""")
    print(f"""{w}nel/UCsIaU94p647veKr7sy12wmA {b}|{w} https://www.youtube.com/channel/UCsIaU94p647veKr7sy12wmA {b}|{w}  https://www.youtube.com/chan""")
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
                            try: data2[routine][f"AutoSend_{i2}"]
                            except: data2[routine][f"AutoSend_{i2}"] = {}
                            data2[routine][f"AutoSend_{i2}"]["ChannelID"] = data[routine][f"AutoSend_{i2}"]["ChannelID"]
                            data2[routine][f"AutoSend_{i2}"]["Send"]      = data[routine][f"AutoSend_{i2}"]["Send"]
                            if int(data[routine][f"AutoSend_{i2}"]["Interval"]) < 1: 
                                data2[routine][f"AutoSend_{i2}"]["Interval"] = 1
                            else: 
                                data2[routine][f"AutoSend_{i2}"]["Interval"] = round(int(data[routine][f"AutoSend_{i2}"]["Interval"]))
                            data2[routine][f"AutoSend_{i2}"]["RandomOffset"] = data[routine][f"AutoSend_{i2}"]["RandomOffset"]
                            data2[routine][f"AutoSend_{i2}"]["temp"] = 0
                        except:
                            break
    if data2 == {}:
        return "invalid"
    return data2
async def main():
    data2 = Load_config_data()
    total_routines = len(data2)
    total_autosends = 0
    for routine in data2:
        total_autosends = total_autosends + len(data2[routine])

    replit.clear()
    print_autosend()
    print(f'{y}[{b}#{y}]{w} Logged in as:\n    Name: {client.user.name}\n    ID: {client.user.id}')
    print(f"\n{y}[{b}#{y}]{w} {b}{total_routines}{w} AutoRoutines")
    print(f"    Total of {b}{total_autosends}{w} AutoSends")
    
    choice = input(f"\n{y}[{b}#{y}]{w} Commence AutoSend? {y}[{w}y/n{y}]")
    if choice not in ("y","Y"):
        input(f"\n{y}[{b}#{y}]{w} Process stopped")
        client.exit = True
        return
    
    # Start process of actually sending messages
    tictok = 0
    while True:
        replit.clear()
        print_autosend()
        print(f'\n{y}[{b}#{y}]{w} Running {b}{total_routines}{w} AutoRoutines and {b}{total_autosends}{w} AutoSends:')
        
        print_string = ""
        for routine in data2:
            print_string += f'\n{y}[{b}#{y}]{w} {routine}'
            for autosend in data2[routine]:
                ctx = client.get_channel(int(data2[routine][autosend]["ChannelID"]))
                message = f'{data2[routine][autosend]["Send"]}'
                if int(autosend[9::]) == 1:
                    interval = int(data2[routine][autosend]["Interval"]) + int(data2[routine][autosend]["temp"])
                else:
                    beforesend = int(autosend[9::])
                    interval = int(data2[routine][autosend]["Interval"]) + int(data2[routine][autosend]["temp"])
                    while beforesend != 1:
                        beforesend = beforesend - 1
                        interval = interval + int(data2[routine][f"AutoSend_{beforesend}"]["Interval"]) + int(data2[routine][f"AutoSend_{beforesend}"]["temp"])
                offset = int(data2[routine][autosend]["RandomOffset"])
                
                if tictok > interval:
                    interval = math.ceil(tictok/interval)*interval #math.ceil always roundsup 
                if tictok == interval:
                    await ctx.send(message)
                    data2[routine][autosend]["temp"] = random.randint(0,offset)
                    print_string += f'\n    {y}[{b}{autosend[9::]}{y}]{w} Sent {y}[{w}{message}{y}]{w} to {y}[{w}#{ctx}{y}]{w}'
                else:
                    print_string += f'\n    {y}[{b}{autosend[9::]}{y}]{w} Sending {y}[{w}{message}{y}]{w} to {y}[{w}#{ctx}{y}]{w} in {y}[{w}{(interval-tictok)}{y}]{w}seconds with a {y}[{w}{offset}{y}]{w} random offset'
        
        print(print_string)
        time.sleep(1)
        tictok = tictok + 1

        choice = input(f"\n{y}[{b}#{y}]{w} Commence AutoSend? {y}[{w}y/n{y}]")
        if choice not in ("y","Y"):
            input(f"\n{y}[{b}#{y}]{w} Process stopped")
            client.exit = True
            return

if __name__ == "__main__":
    keep_alive.keep_alive()

    client = commands.Bot(command_prefix = "WillNotTriggerAnything", self_bot = True)
    client.remove_command('help')
    client.exit = False # whether to exit program
    client.Run_Main = True # main() is ran when client is ready, this prevents on_ready() to trigger main() twice
    replit.clear()
    print(f"""{y}[{b}#{y}]{w} Loading...""")
    
    # Load config data
    try:
        if os.path.exists('Settings.json'):
            with open("Settings.json","r") as f:
                data = json.load(f)
            data["Token"] = os.environ.get('Token')
            if Load_config_data() == "invalid": 
                int("cause error")
        else:
            with open("Settings.json", "w") as f:
                data = {}
                #data["Token"] = "Put your token here"
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
                json.dump(data, f)
            replit.clear()
            print_autosend()
            print(f"{y}[{b}#{y}]{r} Settings.json was not found{w}")
            print(f"    Created file Settings.json")
            print(f"    Please configure Settings.json")
            input(f"\n{y}[{b}#{y}]{w} Process stopped")
            client.exit = True
    except:
        if client.exit == False: 
            replit.clear()
            print_autosend()
            print(f"{y}[{b}#{y}]{r} Error with Settings.json")
            print(f"    {w}Please ensure Settings.json is configured correctly")
            input(f"\n{y}[{b}#{y}]{w} Process stopped")
    
@client.event
async def on_ready():
    #Sometimes on_ready() is triggred more than once.
    if client.Run_Main == True:
        client.Run_Main = False
        replit.clear()
        try: 
            await main()
        except:
            if client.exit == True: 
                return
            replit.clear()
            print(f"{y}[{b}#{y}]{r} Unknown Error Occurred")
            input(f"\n{y}[{b}#{y}]{w} Process stopped")
            client.exit = True
            return

#Discord Token
if __name__ == "__main__":
    try:
        client.run(data["Token"], bot=False)
    except:
        if client.exit == False:
            replit.clear()
            print(f"{y}[{b}#{y}]{r} Error Invalid Token")
            input(f"\n{y}[{b}#{y}]{w} Process stopped")
