import discord
import asyncio
import requests
import random
from discord.ext import commands
import asyncio
import time
from discord_components import DiscordComponents, ComponentsBot, Button
import ast

TOKEN = '*discord bot token*'
client = discord.Client()

DiscordComponents(client)



@client.event
async def on_ready():
    print("online")

apikey = "*tenor api key*"
lmt=8


def get_gif(searchTerm):  
    response = requests.get("https://g.tenor.com/v1/search?q={}&key={}&limit=8".format(searchTerm, apikey))
    data = response.json()
    print(response)
    # see urls for all GIFs
    for result in data['results']:
        for media in result['media']:
            gif = random.choice(data["results"])
    return gif['media'][0]['gif']['url']

    

@client.event
async def on_message(message):
    if message.content =="bobdm":
        if message.channel.id == 959545455463784488:
            channel = message.channel
            count = 0
            x=1
            y=0
            await channel.send("Success ✅") 
            while x != y:
                count +=1
                time.sleep(1)
                await message.author.send("hey shawty")

                #user config
                user=message.author.id
                user=str(user)
                user="<@!"+user+">"

                #log
                print(count)
                print(user)
                count1=str(count)
                with open("sexbob leaderboard.txt", 'a') as f:
                    f.write(user+' '+count1+'\n')

                #alerts 
                if count==100:
                    await message.channel.send(user+" HAS REACHED 100 MESSAGES")
                if count==200:
                    await message.channel.send(user+" HAS REACHED 200 MESSAGES")
                if count==500:
                    await message.channel.send(user+ "HAS REACHED 500 MESSAGES")
                if count==1000:
                    await message.channel.send(user+" HAS REACHED 1000 MESSAGES")
                if count==2000:
                    await message.channel.send(user+" HAS REACHED 2000 MESSAGES")
                if count==3000:
                    await message.channel.send(user+" HAS REACHED 3000 MESSAGES")
                if count==4000:
                    await message.channel.send(user+" HAS REACHED 4000 MESSAGES")
                if count==5000:
                    await message.channel.send(user+" HAS REACHED 5000 MESSAHES")
                if count==10000:
                    await message.channel.send(user+" HAS REACHED 10000 MESSAGES")
        else:
            await message.reply("Please use <#959545455463784488>", delete_after=5)
            time.sleep(1)
            await message.delete()

loop = asyncio.get_event_loop()
loop.run_until_complete(client.start(TOKEN))
