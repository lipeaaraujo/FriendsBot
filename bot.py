import os
from typing import Final
from discord import Client, Intents, Message, Role
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

intents: Intents = Intents.default()
intents.guilds = True
intents.guild_messages = True
intents.message_content = True
intents.guilds = True
intents.members = True

# init bot
bot: commands.Bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}!")

@bot.command()
@commands.has_permissions(manage_roles=True)
async def deletar_roles(ctx: commands.Context, *, role_name: str):
    """Deleta um cargo do servidor com base no nome fornecido."""
    guild = ctx.guild
    channel = ctx.channel
    # channel = discord.utils.get(guild.text_channels, name="bot")
    
    if not channel:
        print("Canal não encontrado")
        return

    if channel.name != "bot":
        print("Bot só pode ser chamado no canal bot")
        return

    count = 0
    for role in guild.roles:
        if role.name == role_name:
            try:
                await role.delete()
                print(f"Role deletada: {role.name}")
                count += 1
            except Exception as e:
                await channel.send(f"Erro ao deletar {role.name}: {e}")
    
    if count > 0:
        await channel.send(f"{count} roles foram deletadas com sucesso!")
    else:
        await channel.send(f'Nenhuma role foi encontrada com o nome "{role_name}"')

bot.run(TOKEN)
