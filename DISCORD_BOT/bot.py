import discord
from discord import Intents
import responses

async def send_message(message, user_message):
    try:
        response = responses.handle_response(user_message)
        print(f'Response: {response}')
        # await message.author.send(response)
        await message.channel.send(response)
    except Exception as e:
        print(e)

def run_discord_bot():
    TOKEN = 'MTE3NjI2OTE4MDQ1OTI5ODk2Nw.GoHcZF.XDNWr7Cm-NRX6pFrX3dVBV7PJR4PPWagaB1rwg'

    # Create Intents
    intents = Intents.default()
    intents.messages = True  # Enable message-related events

    # add intents as a discord client parameter
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} IS ON')

    @client.event 
    async def on_message(message):
        # avoid infinite loop, make sure message comes from someone else than bot
        if message.author == client.user:
            return
        
        username = str(message.author)
        user_message = str(message.content) if message.content else str(message.clean_content)
        channel = str(message.channel)

        print(f'username: {username} user_message: {user_message} channel: {channel}')
        print(message)

        await send_message(message, user_message)

    try:
        client.run(TOKEN)
    except Exception as e:
        print(f"Error in client.run: {e}")