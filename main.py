import os
from typing import Final
from discord import Client, Intents, Message, Role
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

# init bot
intents: Intents = Intents.all()
bot: commands.Bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot conectado como {bot.user}!")
    # loading cogs
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")
            print(f"🔧 Cog carregado: {filename}")

bot.run(TOKEN)
