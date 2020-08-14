# Project Name: Discord Token Vaildator
# Project Author: VoidLSD
# Project Reasion: To validate, if a token is valid or invalid.

import requests

url = "https://canary.discordapp.com/api/v8/users/@me"

intro = """
   ██████╗ ████████╗██╗   ██╗
   ██╔══██╗╚══██╔══╝██║   ██║
   ██║  ██║   ██║   ██║   ██║
   ██║  ██║   ██║   ╚██╗ ██╔╝
   ██████╔╝   ██║    ╚████╔╝ 
   ╚═════╝    ╚═╝     ╚═══╝ 
   Discord Token Vaildator
     Created by VoidLSD
"""
print (intro)

token = input(("Token: "))

headers = {
  'authorization': token
}

rsc = requests.get(url, headers=headers)

try:
    if rsc.status_code == 200:
        print('Token is valid.')
    else:
        print('Token is invalid.')
except Exception:
    print("Cannot connect to discord.com.")
