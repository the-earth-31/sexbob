import discord
from bs4 import BeautifulSoup
import requests
from discord.ext import commands
import asyncio
import time
from discord.utils import get
import random

TOKEN = "(discord token)"
client = discord.Client()
bot = commands.Bot(command_prefix='.')
embed = discord.Embed()
apikey = "(tenor api key)"

@client.event
async def on_ready():
    print("online")

# covid index info
url = "https://www.cdc.gov/coronavirus/2019-ncov/covid-data/covidview/index.html"
url2 = "https://www.worldometers.info/coronavirus/country/us/"
req = requests.get(url)
req2 = requests.get(url2)
soup = BeautifulSoup(req.content, 'html.parser')
soup2 = BeautifulSoup(req2.content, 'html.parser')

# rundown of overall information
rundownScrape = soup.find(class_='card-body bg-white')
theRundown = rundownScrape.text

# last update
lastUpdate = theRundown[14: 36]


def get_gif(searchTerm):  
    response = requests.get("https://g.tenor.com/v1/search?q={}&key={}&limit=8".format(searchTerm, apikey))
    data = response.json()
    # see urls for all GIFs
    for result in data['results']:
        for media in result['media']:
            gif = random.choice(data["results"])
    return gif['media'][0]['gif']['url']

word_site = "https://www.mit.edu/~ecprice/wordlist.10000"

def randomWordSelection(randomNumber):
    response = requests.get(word_site)
    return response.content.splitlines()[randomNumber]


@client.event
async def on_message(message):
    if message.content == "%cases":
        # webscrape for cases graph
        casesScrape = soup.find(href= 'https://covid.cdc.gov/covid-data-tracker/#trends_dailytrendscases')
        casesScrape = str(casesScrape)
        caseAdjust = (casesScrape.split('src="')[1])
        caseCountGraph = caseAdjust[0:84]
        caseCountGraphLink = ('https://www.cdc.gov' + caseCountGraph)
        casesEmbed = discord.Embed(title="Case Count", description= lastUpdate)
        casesEmbed.set_image(url=caseCountGraphLink)
        await message.reply(embed = casesEmbed)

    if message.content == "%vaccine":
        # webscrape for vaccine graph
        vaccineScrape = soup.find(href='https://covid.cdc.gov/covid-data-tracker/#vaccination-trends')
        vaccineScrape = str(vaccineScrape)
        vaccineAdjust = (vaccineScrape.split('src="')[1])
        vaccineRateGraph = vaccineAdjust[0:85]
        vaccineEmbed = discord.Embed(title="Vaccine Rates", description= lastUpdate)
        vaccineRateGraphLink = ('https://www.cdc.gov' + vaccineRateGraph)
        vaccineEmbed.set_image(url=vaccineRateGraphLink)
        await message.reply(embed=vaccineEmbed)

    if message.content == "%hospital":
        # webscrape for hospitalizations graph
        hospitalScrape = soup.find(href='https://covid.cdc.gov/covid-data-tracker/#new-hospital-admissions',
                           class_='noLinking noDecoration')
        hospitalScrape = str(hospitalScrape)
        hospitalAdjust = (hospitalScrape.split('src="')[1])
        hospitalizationRateGraph = hospitalAdjust[0:89]
        hospitalizationRateGraphLink = ('https://www.cdc.gov' + hospitalizationRateGraph)
        hospitalizationEmbed = discord.Embed(title='Hospitalization Rates', description= lastUpdate)
        hospitalizationEmbed.set_image(url=hospitalizationRateGraphLink)
        await message.reply(embed=hospitalizationEmbed)

    if message.content == "%casecount":
        # webscrape for cases number
        caseCountScrape = soup2.find(class_='maincounter-number')
        finalNumber = caseCountScrape.text
        liveCaseCountEmbed = discord.Embed(title='Covid-19 Case Count', description=finalNumber)
        await message.reply(embed=liveCaseCountEmbed)

    if message.content == "%rundown":
        rundownEmbed = discord.Embed(title="The Rundown", description=theRundown)
        await message.reply(embed=rundownEmbed)

    if message.content == "%help":
        await message.reply(
            "Command List:\n%cases *weekly graph of case numbers*\n%vaccine *weekly graph of vaccine rates*\n"
            "%hospital *weekly graph of hospitalization rates*\n%rundown *overall weekly CDC report about spread rates*"
            "\n%casecount *raw most recently reported case numbers*\n"
            "All Charts are based off of most recent CDC Coronavirus Data and Statistics\nOther Commands:\n%special message *endless message spam in dms(block to stop)*\n"
             "%randomgif *a gif selected at random from tenor*\n%randomgif --word *for word stated explicitly*\nTable 1.7 Alpha")

    if message.content =="%special message":
            channel = message.channel
            count = 0
            x=1
            y=0
            await channel.send("Success ✅") 
            user = await client.fetch_user('640639487893962796')
            while x != y:
                count +=1
                time.sleep(1)
                await user.send("hey shawty")
                
                print(count)

    if message.content =="%randomgif":
        choice = random.randrange(0, 10000)
        choice = str(choice)
        descriptionVaraible = "From Tenor Using Word Number: " + choice
        choice = int(choice)
        randomGifEmbed = discord.Embed(title="Random Gif", description= descriptionVaraible)
        randomGifEmbed.set_image(url=get_gif(randomWordSelection(choice)))
        await message.reply(embed=randomGifEmbed)
    
    if message.content == "%randomgif --word":
        choice = random.randrange(0, 10000)
        choice = int(choice)
        wordDef = str(randomWordSelection(choice))
        descriptionVaraible = "From Tenor Using Word: " + wordDef[2: 10]
        randomGifEmbed = discord.Embed(title="Random Gif", description= descriptionVaraible)
        randomGifEmbed.set_image(url=get_gif(randomWordSelection(choice)))
        await message.reply(embed=randomGifEmbed)


loop = asyncio.get_event_loop()
loop.run_until_complete(client.start(TOKEN))
