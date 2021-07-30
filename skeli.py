import discord
import os
from dotenv import load_dotenv

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

    if message.content.startswith('why are we still here'):
        await message.channel.send('Just to suffer?')
    

    if message.content.startswith('are you happy?'):
        await message.channel.send("if you're happy I'm happy!")

client.run(TOKEN)