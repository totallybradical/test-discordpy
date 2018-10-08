# Sweet discord bot via python
import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if (message.server.name == "[Bro] Bromantics"):
        # print("Server Name: " + message.server.name)
        # print("Channel Name: " + message.channel.name)
        # print("Content: " + message.content)
        if ("hey" in message.content.lower()):
            await client.send_message(message.author, 'sup')

client.run('token', bot=False)