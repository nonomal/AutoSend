#!/usr/bin/env python3

"""
HOW TO CHANGE SO IT WORKS ON REPLIT | DO THE OPPOSITE FOR LOCAL
 --> change os.system('cls') to replit.clear()
 --> uncomment these lines:
     - import replit
     - import keep_alive
     - keep_alive.keep_alive()
     - data["Token"] = os.environ.get('Token')
 --> comment these lines
     -    "Token": "Put your token here"
"""

import replit
import keep_alive
import os
import sys
import math
import random
import json
from json import loads, dumps 
from colorama import Fore
from time import sleep
from urllib.request import Request, urlopen
from threading import Thread

y = Fore.LIGHTYELLOW_EX
b = Fore.LIGHTBLUE_EX
w = Fore.LIGHTWHITE_EX
r = Fore.LIGHTRED_EX
g = Fore.GREEN

def getheaders(token=None, content_type="application/json"):
    headers = {
        "Content-Type": content_type,
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
    }
    if token:
        headers.update({"Authorization": token})
    return headers
def send_message(token, chat_id, form_data):
    try:
        urlopen(Request(f"https://discordapp.com/api/v6/channels/{chat_id}/messages", headers=getheaders(token, "multipart/form-data; boundary=---------------------------325414537030329320151394843687"), data=form_data.encode())).read().decode()
    except:
        pass
def get_channel(token, chat_id):
    try:
        return loads(urlopen(Request(f"https://discordapp.com/api/v6/channels/{chat_id}", headers=getheaders(token))).read().decode())
    except:
        pass
def getuserdata(token):
    try:
        return loads(urlopen(Request("https://discordapp.com/api/v6/users/@me", headers=getheaders(token))).read().decode())
    except:
        pass
def form_data(plain_text):
    form_data =  f'\n-----------------------------325414537030329320151394843687'
    form_data += f'\nContent-Disposition: form-data; name="file"\n\nfalse'
    form_data += f'\n-----------------------------325414537030329320151394843687'
    form_data += f'\nContent-Disposition: form-data; name="content"\n\n{plain_text}'
    form_data += f'\n-----------------------------325414537030329320151394843687'
    form_data += f'\nContent-Disposition: form-data; name="tts"\n\nfalse'
    form_data += f'\n-----------------------------325414537030329320151394843687--'
    return form_data

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
def Spinner():
    l = ['|', '/', '-', '\\']
    while thread_spinner == True:
        for i in l:
            sys.stdout.write(f"""\r{y}[{b}#{y}]{w} Loading... {i}""")
            sys.stdout.flush()
            sleep(0.2)
def verified_config_data(data, token):
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
                            if get_channel(token, int(data[routine][autosend]["ChannelID"])) == None:
                                raise Exception('invalid channel')
                            random_send = False
                            try:
                                data[routine][autosend]["Send"]["Send_1"]
                                random_send = True
                            except:
                                random_send = False
                            if random_send == False:
                                if data[routine][autosend]["Send"] == "": 
                                    raise Exception('send string is empty')
                            else:
                                if len(data[routine][autosend]["Send"]) < 2:
                                    raise Exception('too short')
                                for send in data[routine][autosend]["Send"]:
                                    if data[routine][autosend]["Send"][send] == "": 
                                        raise Exception('send string is empty')
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
                            data2[routine][autosend]["Channel_Name"] = get_channel(token, data2[routine][autosend]["ChannelID"])["name"]
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
                        if get_channel(token, int(data[routine][autosend]["ChannelID"])) == None:
                            raise Exception('invalid channel')
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
                        data2[routine][autosend]["Channel_Name"] = get_channel(token, data2[routine][autosend]["ChannelID"])["name"]
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
def calculate_sleep(data2, routine, Status, autosend):
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
def create_examplejson():
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
    data["AutoCount"]["AutoSend_1"] = {}
    data["AutoCount"]["AutoSend_1"]["ChannelID"] = "Put your ChannelID here"
    data["AutoCount"]["AutoSend_1"]["Sleep"] = "3"
    data["AutoCount"]["AutoSend_1"]["RandomOffset"] = "3"
    data["AutoCount"]["AutoSend_1"]["Starting_Int"] = "0"
    data["AutoCount"]["AutoSend_1"]["Interval"] = "1"
    data["AutoCount"]["AutoSend_2"] = {}
    data["AutoCount"]["AutoSend_2"]["ChannelID"] = "Put your ChannelID here"
    data["AutoCount"]["AutoSend_2"]["Sleep"] = "5"
    data["AutoCount"]["AutoSend_2"]["RandomOffset"] = "8"
    data["AutoCount"]["AutoSend_2"]["Starting_Int"] = "51"
    data["AutoCount"]["AutoSend_1"]["Interval"] = "-2"
    return data
def AutoRoutine_(token, data2, routine):
    print_string2 = ""
    for autosend in data2[routine]:
        if autosend not in ("Status", "TicTok"):
            #Set up vars
            Status = data2[routine]["Status"]
            TicTok = data2[routine]["TicTok"]
            channel_id = data2[routine][autosend]["ChannelID"]
            channel_name = data2[routine][autosend]["Channel_Name"]
            message = f'{data2[routine][autosend]["Message"]}'
            offset = data2[routine][autosend]["RandomOffset"]
            CurrentOffset = data2[routine][autosend]["CurrentOffset"]
            Sleep = calculate_sleep(data2, routine, f'AutoSend_{Status}', autosend)

            if TicTok == Sleep:
                Thread(target=send_message, args=(token, channel_id, form_data(message))).start()
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
                print_string2 += f'\n    {y}[{b}{autosend[9::]}{y}]{g} Sent {y}[{b}{message}{y}]{g} to {y}[{b}#{channel_name}{y}]{w}'
            else:
                print_string2 += f'\n    {y}[{b}{autosend[9::]}{y}]{w} Sending {y}[{b}{message}{y}]{w} to {y}[{b}#{channel_name}{y}]{w} in {y}[{b}{(Sleep - TicTok)}{y}]{w}s with a {y}[{b}{offset}{y}]{w}s random offset. Current offset is {y}[{b}{CurrentOffset}{y}]{w}s'
    data2[routine]["TicTok"] = data2[routine]["TicTok"] + 1
    return print_string2
def AutoCount(token, data2, routine):
    print_string2 = ""
    for autosend in data2[routine]:
        if autosend != "TicTok":
            #Set up vars
            TicTok = data2[routine]["TicTok"]
            channel_id = data2[routine][autosend]["ChannelID"]
            channel_name = data2[routine][autosend]["Channel_Name"]
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
                Thread(target=send_message, args=(token, channel_id, form_data(message))).start()
                # Reset some vars
                data2[routine][autosend]["CurrentOffset"] = random.randint(0, offset)
                data2[routine][autosend]["Starting_Int"] = message + Interval
                print_string2 += f'\n    {y}[{b}{autosend[9::]}{y}]{g} Sent {y}[{b}{message}{y}]{g} to {y}[{b}#{channel_name}{y}]{w}'
            else:
                print_string2 += f'\n    {y}[{b}{autosend[9::]}{y}]{w} Sending {y}[{b}{message}{y}]{w} to {y}[{b}#{channel_name}{y}]{w} in {y}[{b}{int(math.sqrt(math.pow(Sleep-TicTok, 2)))}{y}]{w}s with a {y}[{b}{offset}{y}]{w}s random offset. Current offset is {y}[{b}{CurrentOffset}{y}]{w}s'
    data2[routine]["TicTok"] = data2[routine]["TicTok"] + 1
    return print_string2

def main():
    keep_alive.keep_alive()
    replit.clear()
    global thread_spinner
    thread_spinner = True
    Thread(target=Spinner).start()

    # Check and load Settings
    try:
        if os.path.exists('Settings.json'):
            with open("Settings.json","r") as f:
                data = json.load(f)
                data["Token"] = os.environ.get('Token')
            token = data["Token"]
            userdata = getuserdata(token)
            if userdata == None:
                replit.clear()
                print(f"{y}[{b}#{y}]{r} Invalid Token")
                input(f"\n{y}[{b}#{y}]{r} Process stopped")
                return
            data2 = verified_config_data(data, token)
            if data2 == "invalid": 
                raise Exception('invalid config_data')
        else:
            with open("Settings.json", "w") as f:
                json.dump(create_examplejson(), f, indent=4, sort_keys=True)
            replit.clear()
            print_autosend()
            print(f"{y}[{b}#{y}]{r} Settings.json was not found{w}")
            print(f"    {g}Created file Settings.json")
            print(f"    {y}Please configure Settings.json")
            input(f"\n{y}[{b}#{y}]{r} Process stopped")
            return
    except Exception as e:
        replit.clear()
        print_autosend()
        print(f"{y}[{b}#{y}]{r} Error with Settings.json")
        print(f"    {y}Please ensure Settings.json is configured correctly")
        input(f"\n{y}[{b}#{y}]{r} Process stopped\n{e}")
        return
    
    # get print string of what types of messages are being sent
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

    thread_spinner = False
    sleep(0.5)
    replit.clear()
    print_autosend()
    print(f'{y}[{b}#{y}]{w} Logged in as:\n    Name: {userdata["username"]}\n    ID: {userdata["id"]}')
    print(print_string.replace('Running ', ''))
    print(f'\n{y}[{b}#{y}]{w} Continuing in 5 secconds...')
    sleep(5)

    # Start process of actually sending messages
    while True:
        print_string2 = f"{print_string}\n"
        for routine in data2:
            print_string2 += f'\n{y}[{b}#{y}]{w} {routine}'
            if routine[0:12] == "AutoRoutine_":
                print_string2 += AutoRoutine_(token, data2, routine)
            if routine == "AutoCount":
                print_string2 += AutoCount(token, data2, routine)
        replit.clear()
        print_autosend()
        print(print_string2)
        sleep(1)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        replit.clear()
        print(f"{y}[{b}#{y}]{r} Error in main():\n    {e}")
        print(f"\n{y}[{b}#{y}]{w} Restarting in 5 secconds...")
        sleep(5)
        #os.execv(__file__, sys.argv)
        os.execv(sys.executable, [sys.executable, __file__] + sys.argv)


