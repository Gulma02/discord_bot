import discord.errors

from Bot import Bot

# Recupera la información privada del Bot almacenada en ese archivo
bot = Bot()

# @client.event es una función hecha para reaccionar a cualquier evento que reciba el bot
@bot.client.event
async def on_ready():
    print('Logged in as {0}'.format(bot.client.user))

@bot.client.event
async def on_voice_state_update(member, before, after):
    id = member.id
    if id not in bot.list_usuarios:
        bot.list_usuarios.append(member.id)
    else:
        bot.list_usuarios.remove(id)

    print(bot.list_usuarios)

## COMANDOS
# Reacciona cuando el bot recibe un mensaje
@bot.client.command(name = 'saludo')
async def saludo(message):
    await message.channel.send('Hello ' + message.author.mention)

@bot.client.command(name = 'join')
async def unirse(message):
    if not message.author.voice:
        await message.channel.send('Primero tenes que estar conectado a un canal')
    else:
        try:
            canal = message.author.voice.channel
            await canal.connect()
        except discord.errors.ClientException:
            await message.channel.send('Ya estoy conectado a un canal de voz :(')

@bot.client.command(name = 'leave')
async def irse(message):
    if message.voice_client:
        await message.voice_client.disconnect()

@bot.client.command(name = 'ruleta')
async def ruleta(message):
        server = bot.client_helper.get_guild(bot.server_id)
        print(server)

@bot.client.command(name = 'p')
async def poner_musica(message, url: str):
    canal = message.author.voice.channel
    vc = await canal.connect()

    player = await vc.create_ytdl_player(url)
    player.start()

bot.client.run(bot.token)
