import os
from typing import Final
import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.guilds = True
intents.guild_messages = True
intents.message_content = True
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Lista dos nomes dos roles que você quer deletar
roles_para_deletar = ["new role"]

@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")

@bot.command()
@commands.has_permissions(manage_roles=True)
async def deletar_roles(ctx):
    guild = ctx.guild
    canal = discord.utils.get(guild.text_channels, name="bot")
    if canal:
        for role in guild.roles:
            if role.name in roles_para_deletar:
                try:
                    await role.delete()
                    await canal.send(f"Role deletada: {role.name}")
                except Exception as e:
                    await canal.send(f"Erro ao deletar {role.name}: {e}")
    else:
        await ctx.send("Canal não encontrado.")
        

bot.run(TOKEN)
