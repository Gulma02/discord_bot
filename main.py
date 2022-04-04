import discord
from Bot import Bot

# Recupera la información privada del Bot almacenada en ese archivo
bot_info = Bot()
# Crea el cliente de Discord para poder interactuar con el bot
client = discord.Client()

# @client.event es una función hecha para reaccionar a cualquier evento que reciba el bot
@client.event
async def on_ready():
    print(client)
    print('Logged in as {0}'.format(client.user))

# Reacciona cuando el bot recibe un mensaje
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(bot_info.identifier):
        await message.channel.send('Hello!')

client.run(bot_info.token)