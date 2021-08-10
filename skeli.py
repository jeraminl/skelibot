import discord
import os
from dotenv import load_dotenv
from random import seed
from random import randint

client = discord.Client()

load_dotenv()
TOKEN = os.getenv('TOKEN')

@client.event
async def on_ready():
    print('we have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower().startswith('why are we still here'):
        print(message.content)
        await message.channel.send('Just to suffer?')
    

    if message.content.lower().startswith('are you happy'):
        print(message.author)
        await message.channel.send("if you're happy I'm happy!")

    if message.content.lower().startswith('$fuck you'):
        await message.channel.send("ur mum gay")

    if message.content.lower().startswith('can you say nyaa'):
        await message.channel.send("nyo")
    
    if message.content.lower().startswith('what do you have'):
        await message.channel.send("chlamydia")

    if message.content.lower().startswith('give me a number'):
        await message.channel.send(randint(0,100))

    if message.content.lower().startswith('no u'):
        await message.channel.send('no u!')

client.run(TOKEN)