import discord
import asyncio
import requests
import random
from discord.ext import commands
import asyncio
import time
from discord_components import DiscordComponents, ComponentsBot, Button


TOKEN = '(discord bot token)'
client = discord.Client()

DiscordComponents(client)



@client.event
async def on_ready():
    print("online")

apikey = "(tenor api key)"
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
    if message.content == "s":
        await message.add_reaction('<:trollbob:889682115023732807>')
        bobImbed=discord.Embed(title="SEXBOB!!!!!")
        await message.reply(embed=bobImbed)

    if message.content == "sex":
        await message.add_reaction('<:trollbob:889682115023732807>')
        bobImbed=discord.Embed(title="BOBSEXARD!!?!?!?")
        await message.reply(embed=bobImbed)

    if message.content == "madbob":
        await message.add_reaction('<:trollbob:889682115023732807>')
        bobImbed=discord.Embed(title="madbob")
        bobImbed.set_image(url='https://c.tenor.com/eLQgFB1Hn-EAAAAd/asoingbob.gif')
        await message.reply(embed=bobImbed)

    if message.content == "squidsex":
        await message.add_reaction('<:trollbob:889682115023732807>')
        bobImbed=discord.Embed(title='squidsex')
        bobImbed.set_image(url='https://c.tenor.com/5_ndanNk8jEAAAAC/squidward-dance.gif')
        await message.reply(embed=bobImbed)

    if message.content == "lovebob":
        await message.add_reaction('<:trollbob:889682115023732807>')
        bobImbed=discord.Embed(title='lovebob')
        bobImbed.set_image(url='https://c.tenor.com/zqxTaKHBYY4AAAAC/spongebob-twerking.gif')
        await message.reply(embed=bobImbed)

    if message.content == "ballbob":
        await message.add_reaction('<:trollbob:889682115023732807>')
        bobImbed=discord.Embed(title='im so damn ignorant i pulled out my ding-a-ling and start pee peein')
        await message.reply(embed=bobImbed)

    if message.content == "youngbob":
        await message.add_reaction('<:trollbob:889682115023732807>')
        bobImbed=discord.Embed(title='i watched my grandpa say penis')
        await message.reply(embed=bobImbed)

    if message.content == "helpbob":
        await message.add_reaction('<:trollbob:889682115023732807>')
        descriptionVar = ("s\nsex\nmadbob\nsquidsex\nlovebob\nballbob\nyoungbob\nUr mom\n6: The dollar\nbobsearch *[search term]* (search for gif)\nsquidgore\nsadbob\nbobapproval\nspongicus\nEEF (epic embed fail)")
        bobImbed=discord.Embed(title='Bob list', description=descriptionVar)
        await message.reply(embed=bobImbed)

    if message.content == "Ur mom":
        await message.add_reaction('<:trollbob:889682115023732807>')
        bobImbed=discord.Embed(title='Ur mom')
        bobImbed.set_image(url='https://c.tenor.com/8EMdIrxfd58AAAAS/xbox-live-yo-mama.gif')
        await message.reply(embed=bobImbed)

    if message.content == "6: The dollar":
        await message.add_reaction('<:trollbob:889682115023732807>')
        bobImbed=discord.Embed(title='6: The dollar')
        bobImbed.set_image(url='https://media.discordapp.net/attachments/885991162417131522/892017343067193374/image0.gif')
        await message.reply(embed=bobImbed)

    if message.content.startswith("bobsearch"):
        await message.add_reaction('<:trollbob:889682115023732807>')
        input = message.content.split(" ", 10)[1:]
        input=str(input)
        gifurl=get_gif(input)
        bobImbed=discord.Embed(title='bobsearch', description='searched with sexbob')
        bobImbed.set_image(url=gifurl)
        await message.reply(embed=bobImbed)

    if message.content == "squidgore":
        await message.add_reaction('<:trollbob:889682115023732807>')
        bobImbed=discord.Embed(title='squidgore')
        bobImbed.set_image(url='https://c.tenor.com/o7hKMDIeoG0AAAAS/squidward-toenail.gif')
        await message.reply(embed=bobImbed)

    if message.content == "sadbob":
        await message.add_reaction('<:trollbob:889682115023732807>')
        bobImbed=discord.Embed(title='sadbob')
        bobImbed.set_image(url='https://c.tenor.com/tuFUoehZse0AAAAS/spongebob-crying.gif')
        await message.reply(embed=bobImbed)

    if "bobapproval" in message.content:
        answers=["no what the fuck", "of course", "no", "yes ofc", "why not"]
        anscho=random.randrange(0,5)
        anscho=int(anscho)
        bobImbed=discord.Embed(title='bobapproval ✅❌', description=answers[anscho])
        await message.reply(embed=bobImbed)

    if message.content == "spongicus":
        bobImbed=discord.Embed(title='Et tu, Spongicus?')
        await message.reply(embed=bobImbed)

    if "league of legends" in message.content:
        bobImbed=discord.Embed(title='TOUCH GRASS')
        bobImbed.set_image(url='https://cdn.discordapp.com/attachments/886093764882481202/951629933455736902/hand-touching-grass-B24KRE.png')
        await message.reply(embed=bobImbed)
    
    if "LOL" in message.content:
        bobImbed=discord.Embed(title='TOUCH GRASS')
        bobImbed.set_image(url='https://cdn.discordapp.com/attachments/886093764882481202/951629933455736902/hand-touching-grass-B24KRE.png')
        await message.reply(embed=bobImbed)
    
    if "EEF" in message.content:
        bobImbed=discord.Embed(title='EPIC EMBED FAIL')
        bobImbed.set_image(url='https://c.tenor.com/wphIipSQJIYAAAAd/jesus-ballin-mars-bars.gif')
        await message.reply(embed=bobImbed)
    
    
    

loop = asyncio.get_event_loop()
loop.run_until_complete(client.start(TOKEN))
