import discord
import asyncio

TOKEN = ''
client = discord.Client()


@client.event
async def on_ready():
    print("online")


@client.event
async def on_message(message):
    if message.content == "s":
        bobImbed=discord.Embed(title="SEXBOB!!!!!")
        await message.reply(embed=bobImbed)
    if message.content == "sex":
        bobImbed=discord.Embed(title="BOBSEXARD!!?!?!?")
        await message.reply(embed=bobImbed)
    if message.content == "madbob":
        bobImbed=discord.Embed(title="madbob")
        bobImbed.set_image(url='https://c.tenor.com/eLQgFB1Hn-EAAAAd/asoingbob.gif')
        await message.reply(embed=bobImbed)
    if message.content == "squidsex":
        bobImbed=discord.Embed(title='squidsex')
        bobImbed.set_image(url='https://c.tenor.com/5_ndanNk8jEAAAAC/squidward-dance.gif')
        await message.reply(embed=bobImbed)
    if message.content == "lovebob":
        bobImbed=discord.Embed(title='lovebob')
        bobImbed.set_image(url='https://c.tenor.com/zqxTaKHBYY4AAAAC/spongebob-twerking.gif')
        await message.reply(embed=bobImbed)
    if message.content == "ballbob":
        bobImbed=discord.Embed(title='im so damn ignorant i pulled out my ding-a-ling and start pee peein')
        await message.reply(embed=bobImbed)
    if message.content == "youngbob":
        bobImbed=discord.Embed(title='i watched my grandpa say penis')
        await message.reply(embed=bobImbed)
    if message.content == "helpbob":
        descriptionVar = ("s\nsex\nmadbob\nsquidsex\nlovebob\nballbob\nyoungbob\nUr mom\n6: The dollar")
        bobImbed=discord.Embed(title='Bob list', description=descriptionVar)
        await message.reply(embed=bobImbed)
    if message.content == "Ur mom":
        bobImbed=discord.Embed(title='Ur mom')
        bobImbed.set_image(url='https://c.tenor.com/8EMdIrxfd58AAAAS/xbox-live-yo-mama.gif')
        await message.reply(embed=bobImbed)
    if message.content == "6: The dollar":
        bobImbed=discord.Embed(title='6: The dollar')
        bobImbed.set_image(url='https://media.discordapp.net/attachments/885991162417131522/892017343067193374/image0.gif')
        await message.reply(embed=bobImbed)

loop = asyncio.get_event_loop()
loop.run_until_complete(client.start(TOKEN))
