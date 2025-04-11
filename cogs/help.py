from discord import Color, Embed
from discord.ext import commands

class HelpCommands(commands.Cog):
    """Comandos de ajuda do bot."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="ajuda")
    async def ajuda(self, ctx: commands.Context):
        embed = Embed(
            title="📘 Comandos do Bot",
            description="Aqui estão os comandos que você pode usar:",
            color=Color.green()
        )
        embed.add_field(
            name="!deletar_role <nome>",
            value="Deleta cargos com o nome fornecido.",
            inline=False
        )
        embed.add_field(
            name="!ping",
            value="Retorna o ping do bot.",
            inline=False
        )
        embed.add_field(
            name="!ajuda",
            value="Mostra essa mensagem.",
            inline=False
        )
        await ctx.send(embed=embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(HelpCommands(bot))