from discord.ext import commands
import discord
import nacl

class Bot:
    def __init__(self):
        self.token = 'OTYwNTYxNTAzMTI2MjkwNDYy.YksOnA.VJwzwWkY8aNRvkRn2yKvC9JVtrY'
        self.server_id = 960597008484286584
        self.identifier = '.'
        # Crea el cliente de Discord para poder interactuar con el bot
        self.client = commands.Bot(command_prefix = '.')
        self.client_helper = discord.Client()
        self.list_usuarios = []