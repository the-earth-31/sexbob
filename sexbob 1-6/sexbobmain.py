import discord
import asyncio
import requests
import random
from discord.ext import commands
import asyncio
import time
from discord_components import DiscordComponents, ComponentsBot, Button
import ast
import datetime

TOKEN = 'OTM0NjI0Mjc1OTI1NzIxMTQ4.Yeyyrw._1unXlSu68FDyJXpPZHMuvT8Gtg'
client = discord.Client()

DiscordComponents(client)



@client.event
async def on_ready():
    print("online")

apikey = "DZ8GQJXRY046"
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
        descriptionVar = ("s\nsex\nmadbob\nsquidsex\nlovebob\nballbob\nyoungbob\nUr mom\n6: The dollar\nbobsearch *[search term]* (search for gif)\nsquidgore\nsadbob\nbobapproval\nspongicus\nEEF (epic embed fail)\nbopopular\nbobinfo\nWock\npiper\ndoler\ncumbob\nFunnyFish\nbobping *(@user)* (nefarious hidden ping)\nsal\nbobday (*month/day*)\n*if single number such as July simply type 7 with no 0 (ex.3/4)*\n|NEW FEATURE!|\nbobdm (endless dm spam with milestone messages! *issue command once per use*)\nbobdata *number*(data from sexbob bobdm command)")
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
    
    if message.content == 'bopopular':
        await message.reply("https://media.discordapp.net/attachments/818678449275011072/845051338446471168/silly_spunchbob.gif")
    
    if "fuck" in message.content:
        await message.add_reaction('<:weepbob:886288517028782140>')
    if "bitch" in message.content:
        await message.add_reaction('<:weepbob:886288517028782140>')
    if "shit" in message.content:
        await message.add_reaction('<:weepbob:886288517028782140>')
    if "ass" in message.content:
        await message.add_reaction('<:weepbob:886288517028782140>')
    if "penis" in message.content:
        await message.add_reaction('<:weepbob:886288517028782140>')

    if "FUCK" in message.content:
        await message.add_reaction('<:weepbob:886288517028782140>')
    if "BITCH" in message.content:
        await message.add_reaction('<:weepbob:886288517028782140>')
    if "SHIT" in message.content:
        await message.add_reaction('<:weepbob:886288517028782140>')
    if "ASS" in message.content:
        await message.add_reaction('<:weepbob:886288517028782140>')
    if "PENIS" in message.content:
        await message.add_reaction('<:weepbob:886288517028782140>')

    if "F U C K" in message.content:
        await message.add_reaction('<:weepbob:886288517028782140>')
    if "B I T C H" in message.content:
        await message.add_reaction('<:weepbob:886288517028782140>')
    if "S H I T" in message.content:
        await message.add_reaction('<:weepbob:886288517028782140>')
    if "A S S" in message.content:
        await message.add_reaction('<:weepbob:886288517028782140>')
    if "P E N I S" in message.content:
        await message.add_reaction('<:weepbob:886288517028782140>')

    if "hiddensecretcommand" in message.content:
        bobImbed=discord.Embed(title="full spunch bop episodes", description="season 1\nepisode 1 (help wanted,reef blower,tea at the treedome): https://drive.google.com/file/d/1bHyz1vZumIzLfvu2h4zklh4vuYhm305I/view?usp=sharing\nhome sweet pineapple: https://drive.google.com/file/d/1wrFxV3WzXR7Zc_PFBJeYCiUAZpyAjHDy/view?usp=sharing\n"
        "bubblestand: https://drive.google.com/file/d/1HNIQQ-4RdrFT2g_iPxi8tNfFeIUSZIqO/view?usp=sharing\nripped pants: https://drive.google.com/file/d/1QGvA52z9giLyl_Ao__YzFwi1sPmIsGpZ/view?usp=sharing\nplankton: https://drive.google.com/file/d/1pTsuqmQUP8qF82yoV2jFL7_UR3kJrND8/view?usp=sharing\nboating school: https://drive.google.com/file/d/16XBBcXGyLBQtcJNxlGvO2EfUjwDbWGCS/view?usp=sharing\n"
        "naughty nautical neighbors: https://drive.google.com/file/d/1pmDAsk0pOwfc8SweTzKQxmwPVx0-Jd9N/view?usp=sharing\nsandy's rocket: https://drive.google.com/file/d/1VA2c4W-6XfVli7IrqDUFt_Y1P296TECY/view?usp=sharing\npizza delivery: https://drive.google.com/file/d/1Ted8AMwGl2RGfM3KwR9V_INFTD4hpclP/view?usp=sharing\nsqueaky boots: https://drive.google.com/file/d/18uA_6wykMlYm0JkWQbPqELRV8X4T_yZK/view?usp=sharing")
        await message.reply(embed=bobImbed)
    
    if message.content == "bobinfo":
        bobImbed=discord.Embed(title="info", description="Sexbob version 2.3\nLast Updated: 5/5/22\nA bot by: the #0005")
        await message.reply(embed=bobImbed)

    if message.content == "dick":
        bobImbed=discord.Embed(title="POOPBOB")
        await message.reply(embed=bobImbed)

    if message.content.startswith("bobdata"):
        with open('sexbob leaderboard.txt') as f:
            lines = f.readlines()
        await message.add_reaction('<:trollbob:889682115023732807>')
        inp=message.content.split(' ', 8)[1:]
        inp=str(inp)
        inp=inp.replace("['", '')
        inp=inp.replace("']", '')
        print(inp)
        inp=int(inp)
        data=lines[-inp:]
        data = (''.join(data))
        data=data.replace("'", '')
        print(data)
        data=str(data)
        format="usr | msg count\n"
        bobImbed=discord.Embed(title='bobdata', description=format+data)
        await message.reply(embed=bobImbed)

    if message.content == "Wock":
        bobImbed=discord.Embed(title="Big ass knot of money stretch long as a fire hose")
        await message.reply(embed=bobImbed)
    if message.content == "piper":
        bobImbed=discord.Embed(title="ayo look at thiws phone")
        await message.reply(embed=bobImbed)
    if message.content == "doler":
        bobImbed=discord.Embed(title="FUCK!!!!!!!!!!!")
        await message.reply(embed=bobImbed)
    if message.content=="cumbob":
        bobImbed=discord.Embed(title="REAL!?!?!?!?!?!")
        await message.reply(embed=bobImbed)
    if message.content=="FunnyFish":
        bobImbed=discord.Embed(title="Bloopbob!!!")
        await message.reply(embed=bobImbed)
    
    if message.content.startswith("bobping"):
        await message.delete()
        fm=message.content.split(' ', 8)[1:]
        fm=str(fm)
        user=message.author.id
        user=str(user)
        user="<@!"+user+">"
        await message.channel.send("nefarious secret ping ||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​|| _ _ _ _ _ _ "+fm)

    if message.content=="sal":
        await message.add_reaction('<:trollbob:889682115023732807>')
        bobImbed=discord.Embed(title="That link was deemed to be malicious and has been removed!")
        await message.reply(embed=bobImbed)

    if message.content.startswith("bobday"):
        await message.add_reaction('<:trollbob:889682115023732807>')
        #message trimming
        fm=message.content.split(' ', 7)[1:]
        fm=str(fm)
        fm=fm.replace("[", '')
        fm=fm.replace("]", '')
        fm=fm.replace("'", '')


        #user config
        user=message.author.id
        user=str(user)
        user="<@!"+user+">"

        #verify duplicate
        with open('birthday_manifest.txt') as f:
            lines = f.readlines()
        
        for item in lines:
            if user in item:
                print('worked')
                await message.reply("You have already entered a birthday!", delete_after=5)
                
        #opens text file
        with open("birthday_manifest.txt", 'a') as f:
                    f.write(user+' '+fm+'\n')
        
        #current time in m/d/y format
        now = datetime.datetime.now()
        date = now.month, now.day, now.year
        date = str(date)
        date=date.replace('(', '')
        date=date.replace(')', '')
        date=date.replace(',', '/')
        date=date.replace(' ', '')
        
loop = asyncio.get_event_loop()
loop.run_until_complete(client.start(TOKEN))
