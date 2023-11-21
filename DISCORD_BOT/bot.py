import asyncio
import discord
from discord import Intents
import responses
import os 
from dotenv import load_dotenv, find_dotenv

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

async def send_message(message, user_message):
    try:
        response = responses.handle_response(user_message)
        print(f'Response: {response}')
        sent_message = await message.channel.send(response)

        await asyncio.sleep(10)
        await sent_message.delete()
        
    except Exception as e:
        print(e)

def run_discord_bot():

    TOKEN = os.getenv("TOKEN")

    # Create Intents
    intents = Intents.default()
    intents.messages = True  # Enable message-related events
    intents.message_content = True

    # add intents as a discord client parameter
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} IS ON')

    @client.event 
    async def on_message(message):
      
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'username: {username} user_message: {user_message} channel: {channel}')

        # avoid infinite loop, make sure message comes from someone else than bot
        if message.author == client.user:
            return
        
        # sample response
        await send_message(message, user_message)
            
        return


    try:
        client.run(TOKEN)
    except Exception as e:
        print(f"Error in client.run: {e}")