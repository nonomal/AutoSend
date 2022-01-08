# HOW TO CHANGE SO IT WORKS ON REPLIT | DO THE OPPOSITE FOR LOCAL
# --> change `replit.clear()` to replit.clear()
# --> uncomment these lines:
#     - import replit
#     - import keep_alive
#     - keep_alive.keep_alive()
#     - data["Token"] = os.environ.get('Token')
# --> comment these lines
#     -    "Token": "Put your token here"


# <-- CODE --> #
import replit
import keep_alive
import json
import os
import sys
import time
import math
import random
from discord import client, message
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
def Load_config_data(data, Client):
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
                            if Client == True:
                                if client.get_channel(int(data[routine][autosend]["ChannelID"])) is None:
                                    int("cause error")
                            random_send = False
                            try:
                                data[routine][autosend]["Send"]["Send_1"]
                                random_send = True
                            except:
                                random_send = False
                            if random_send == False:
                                if data[routine][autosend]["Send"] == "": 
                                    int("cause error")
                            else:
                                if len(data[routine][autosend]["Send"]) < 2:
                                    int("cause error")
                                for send in data[routine][autosend]["Send"]:
                                    if data[routine][autosend]["Send"][send] == "": 
                                        int("cause error")
                            int(data[routine][autosend]["Sleep"])
                            int(data[routine][autosend]["RandomOffset"])
                            
                            #Add to data2
                            try: 
                                data2[routine]
                            except: 
                                data2[routine] = {}
                            data2[routine]["Status"] = 1
                            data2[routine]["TicTok"] = 0
                            try: 
                                data2[routine][autosend]
                            except: 
                                data2[routine][autosend] = {}
                            data2[routine][autosend]["ChannelID"] = int(data[routine][autosend]["ChannelID"])
                            if int(data[routine][autosend]["Sleep"]) < 1: 
                                data2[routine][autosend]["Sleep"] = 1
                            else: 
                                data2[routine][autosend]["Sleep"] = int(data[routine][autosend]["Sleep"])
                            data2[routine][autosend]["RandomOffset"] = int(data[routine][autosend]["RandomOffset"])
                            data2[routine][autosend]["CurrentOffset"] = random.randint(0,int(data[routine][autosend]["RandomOffset"]))
                            if random_send == False:
                                data2[routine][autosend]["Message"] = data[routine][autosend]["Send"]
                            else:
                                data2[routine][autosend]["Send"] = data[routine][autosend]["Send"]
                                data2[routine][autosend]["Message"] = data2[routine][autosend]["Send"][f'Send_{random.randint(1, len(data2[routine][autosend]["Send"]))}']
                        except:
                            break
        if routine == "AutoCount":
            i3 = 0
            for autosend in data[routine]:
                i3 = i3 + 1
                if autosend == f"AutoSend_{i3}":
                    try:
                        #Check if works
                        if Client == True:
                            if client.get_channel(int(data[routine][autosend]["ChannelID"])) is None:
                                int("cause error")
                        int(data[routine][autosend]["Sleep"])
                        int(data[routine][autosend]["Interval"])
                        int(data[routine][autosend]["RandomOffset"])
                        int(data[routine][autosend]["Starting_Int"])

                        #Add to data2
                        try: 
                            data2[routine]
                        except: 
                            data2[routine] = {}
                        data2[routine]["TicTok"] = 0
                        try: 
                            data2[routine][autosend]
                        except: 
                            data2[routine][autosend] = {}
                        data2[routine][autosend]["ChannelID"] = int(data[routine][autosend]["ChannelID"])
                        data2[routine][autosend]["Starting_Int"] = int(data[routine][autosend]["Starting_Int"])
                        data2[routine][autosend]["Interval"] = int(data[routine][autosend]["Interval"])
                        if int(data[routine][autosend]["Sleep"]) < 1: 
                            data2[routine][autosend]["Sleep"] = 1
                        else: 
                            data2[routine][autosend]["Sleep"] = int(data[routine][autosend]["Sleep"])
                        data2[routine][autosend]["RandomOffset"] = int(data[routine][autosend]["RandomOffset"])
                        data2[routine][autosend]["CurrentOffset"] = random.randint(0,int(data[routine][autosend]["RandomOffset"]))
                    except:
                        break
    if data2 == {}:
        return "invalid"
    return data2
def Calculate_Sleep(data2, routine, Status, autosend):
    if Status == autosend:
        Sleep = data2[routine][autosend]["Sleep"] + data2[routine][autosend]["CurrentOffset"]
    else:
        Sleep = data2[routine][Status]["Sleep"] + data2[routine][Status]["CurrentOffset"]
        which_autosend = int(Status[9::])
        while f"AutoSend_{which_autosend}" != autosend:
            if which_autosend == (len(data2[routine]) - 2):
                which_autosend = 1
            else:
                which_autosend = which_autosend + 1
            Sleep = Sleep + data2[routine][f"AutoSend_{which_autosend}"]["Sleep"] + data2[routine][f"AutoSend_{which_autosend}"]["CurrentOffset"]
    return int(Sleep)
def is_interger(x):
    return x - int(x) == 0
async def main():
    data2 = Load_config_data(data, True)
    if data2 == "invalid": #Check again this time if channel id is correct
        replit.clear()
        print_autosend()
        print(f"{y}[{b}#{y}]{r} Error with Settings.json")
        print(f"    {y}Please ensure you are using a valid channel id")
        input(f"\n{y}[{b}#{y}]{r} Process stopped")
    try:
        data2["AutoCount"]["AutoSend_1"]
        plural = ""
        if len(data2["AutoCount"])-1 > 1:
            plural = "s"
        if len(data2) == 1:
            print_string = f'\n{y}[{b}#{y}]{w} Running {b}{len(data2["AutoCount"])-1}{w} AutoCount{plural}'
        else:
            print_string = f'\n{y}[{b}#{y}]{w} Running {b}{len(data2)-1}{w} AutoRoutines and {b}{len(data2["AutoCount"])-1}{w} AutoCount{plural}' 
    except:
        print_string = f'\n{y}[{b}#{y}]{w} Running {b}{len(data2)}{w} AutoRoutines'

    replit.clear()
    print_autosend()
    print(f'{y}[{b}#{y}]{w} Logged in as:\n    Name: {client.user.name}\n    ID: {client.user.id}')
    print(print_string.replace('Running ', ''))
    
    choice = input(f"\n{y}[{b}#{y}]{w} Commence AutoSend? {y}[{w}Y{y}/{w}N{y}]{w}")
    if choice not in ("y","Y"):
        input(f"\n{y}[{b}#{y}]{w} Process stopped")
        client.exit = True
        return
    replit.clear()

    # Start process of actually sending messages
    while True:
        print_string2 = f"{print_string}\n"
        for routine in data2:
            print_string2 += f'\n{y}[{b}#{y}]{w} {routine}'
            if routine[0:12] == "AutoRoutine_":
                for autosend in data2[routine]:
                    if autosend not in ("Status", "TicTok"):
                        #Set up vars
                        Status = data2[routine]["Status"]
                        TicTok = data2[routine]["TicTok"]
                        ctx = client.get_channel(data2[routine][autosend]["ChannelID"])
                        message = f'{data2[routine][autosend]["Message"]}'
                        offset = data2[routine][autosend]["RandomOffset"]
                        CurrentOffset = data2[routine][autosend]["CurrentOffset"]
                        Sleep = Calculate_Sleep(data2, routine, f'AutoSend_{Status}', autosend)

                        if TicTok == Sleep:
                            await ctx.send(message)
                            # Reset some vars
                            data2[routine]["TicTok"] = 0
                            data2[routine][autosend]["CurrentOffset"] = random.randint(0,offset)
                            try:
                                data2[routine][autosend]["Send"]["Send_1"]
                                data2[routine][autosend]["Message"] = data2[routine][autosend]["Send"][f'Send_{random.randint(1, len(data2[routine][autosend]["Send"]))}']
                            except:
                                pass
                            if Status == (len(data2[routine]) - 2):
                                data2[routine]["Status"] = 1
                            else:
                                data2[routine]["Status"] = Status + 1
                            print_string2 += f'\n    {y}[{b}{autosend[9::]}{y}]{g} Sent {y}[{b}{message}{y}]{g} to {y}[{b}#{ctx}{y}]{w}'
                        else:
                            print_string2 += f'\n    {y}[{b}{autosend[9::]}{y}]{w} Sending {y}[{b}{message}{y}]{w} to {y}[{b}#{ctx}{y}]{w} in {y}[{b}{(Sleep - TicTok)}{y}]{w}s with a {y}[{b}{offset}{y}]{w}s random offset. Current offset is {y}[{b}{CurrentOffset}{y}]{w}s'
                data2[routine]["TicTok"] = data2[routine]["TicTok"] + 1
            if routine == "AutoCount":
                for autosend in data2[routine]:
                    if autosend != "TicTok":
                        #Set up vars
                        TicTok = data2[routine]["TicTok"]
                        ctx = client.get_channel(data2[routine][autosend]["ChannelID"])
                        message = data2[routine][autosend]["Starting_Int"]
                        offset = data2[routine][autosend]["RandomOffset"]
                        CurrentOffset = data2[routine][autosend]["CurrentOffset"]
                        Sleep = data2[routine][autosend]["Sleep"]
                        Interval = data2[routine][autosend]["Interval"]
                        
                        if is_interger((CurrentOffset + Sleep)/Sleep):
                            CurrentOffset = 0
                        if TicTok > Sleep:
                            Sleep = math.floor(TicTok/Sleep) * Sleep
                        Sleep = Sleep + CurrentOffset
                        if TicTok == Sleep:
                            await ctx.send(message)
                            # Reset some vars
                            data2[routine][autosend]["CurrentOffset"] = random.randint(0, offset)
                            data2[routine][autosend]["Starting_Int"] = message + Interval
                            print_string2 += f'\n    {y}[{b}{autosend[9::]}{y}]{g} Sent {y}[{b}{message}{y}]{g} to {y}[{b}#{ctx}{y}]{w}'
                        else:
                            print_string2 += f'\n    {y}[{b}{autosend[9::]}{y}]{w} Sending {y}[{b}{message}{y}]{w} to {y}[{b}#{ctx}{y}]{w} in {y}[{b}{int(math.sqrt(math.pow(Sleep-TicTok, 2)))}{y}]{w}s with a {y}[{b}{offset}{y}]{w}s random offset. Current offset is {y}[{b}{CurrentOffset}{y}]{w}s'
                data2[routine]["TicTok"] = data2[routine]["TicTok"] + 1
        replit.clear()
        print_autosend()
        print(print_string2)
        time.sleep(1)

if __name__ == "__main__":
    keep_alive.keep_alive()

    client = commands.Bot(command_prefix = "WillNotTriggerAnything", self_bot = True)
    client.remove_command('help')
    client.exit = False # whether to exit program
    client.Run_Main = True # main() is ran when client is ready, this prevents on_ready() to trigger main() twice
    replit.clear()
    print(f"""{y}[{b}#{y}]{y} Loading...""")

    # Load config data
    try:
        if os.path.exists('Settings.json'):
            with open("Settings.json","r") as f:
                data = json.load(f)
                data["Token"] = os.environ.get('Token')
            if Load_config_data(data, False) == "invalid": 
                int("cause error")
        else:
            with open("Settings.json", "w") as f:
                # Create A Simple Template
                data = {}
                #data["Token"] = "Put your token here"
                data["AutoRoutine_1"] = {}
                data["AutoRoutine_2"] = {}
                for x in "12":
                    data[f"AutoRoutine_{x}"]["AutoSend_1"] = {}
                    data[f"AutoRoutine_{x}"]["AutoSend_1"]["ChannelID"] = "Put your ChannelID here"
                    data[f"AutoRoutine_{x}"]["AutoSend_1"]["Send"] = "!d bump"
                    data[f"AutoRoutine_{x}"]["AutoSend_1"]["Sleep"] = "5"
                    data[f"AutoRoutine_{x}"]["AutoSend_1"]["RandomOffset"] = "3"
                    data[f"AutoRoutine_{x}"]["AutoSend_2"] = {}
                    data[f"AutoRoutine_{x}"]["AutoSend_2"]["ChannelID"] = "Put your ChannelID here"
                    data[f"AutoRoutine_{x}"]["AutoSend_2"]["Send"] = "pls daily"
                    data[f"AutoRoutine_{x}"]["AutoSend_2"]["Sleep"] = "10"
                    data[f"AutoRoutine_{x}"]["AutoSend_2"]["RandomOffset"] = "3"
                    if x == 2:
                        data[f"AutoRoutine_{x}"]["AutoSend_3"] = {}
                        data[f"AutoRoutine_{x}"]["AutoSend_3"]["ChannelID"] = "Put your ChannelID here"
                        data[f"AutoRoutine_{x}"]["AutoSend_3"]["Send"] = {}
                        data[f"AutoRoutine_{x}"]["AutoSend_3"]["Send"]["Send_1"] = "hello"
                        data[f"AutoRoutine_{x}"]["AutoSend_3"]["Send"]["Send_2"] = "how r you doing"
                        data[f"AutoRoutine_{x}"]["AutoSend_3"]["Send"]["Send_3"] = "im so sleepy"
                        data[f"AutoRoutine_{x}"]["AutoSend_3"]["RandomOffset"] = "3"
                data["AutoCount"] = {}
                data[f"AutoCount"]["AutoSend_1"] = {}
                data[f"AutoCount"]["AutoSend_1"]["ChannelID"] = "Put your ChannelID here"
                data[f"AutoCount"]["AutoSend_1"]["Sleep"] = "3"
                data[f"AutoCount"]["AutoSend_1"]["RandomOffset"] = "3"
                data[f"AutoCount"]["AutoSend_1"]["Starting_Int"] = "0"
                data[f"AutoCount"]["AutoSend_1"]["Interval"] = "1"
                data[f"AutoCount"]["AutoSend_2"] = {}
                data[f"AutoCount"]["AutoSend_2"]["ChannelID"] = "Put your ChannelID here"
                data[f"AutoCount"]["AutoSend_2"]["Sleep"] = "5"
                data[f"AutoCount"]["AutoSend_2"]["RandomOffset"] = "8"
                data[f"AutoCount"]["AutoSend_2"]["Starting_Int"] = "51"
                data[f"AutoCount"]["AutoSend_1"]["Interval"] = "-2"
                json.dump(data, f, indent=4, sort_keys=True)
            replit.clear()
            print_autosend()
            print(f"{y}[{b}#{y}]{r} Settings.json was not found{w}")
            print(f"    {g}Created file Settings.json")
            print(f"    {y}Please configure Settings.json")
            input(f"\n{y}[{b}#{y}]{r} Process stopped")
            client.exit = True
    except:
        if client.exit == False: 
            replit.clear()
            print_autosend()
            print(f"{y}[{b}#{y}]{r} Error with Settings.json")
            print(f"    {y}Please ensure Settings.json is configured correctly")
            input(f"\n{y}[{b}#{y}]{r} Process stopped")

@client.event
async def on_ready():
    #Sometimes on_ready() is triggred more than once.
    if client.Run_Main == True:
        client.Run_Main = False
        replit.clear()

        # run main()
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
            input(f"\n{y}[{b}#{y}]{r} Process stopped")
