from discord.ext import commands

class FunCommands(commands.Cog):
    """Comandos de diversão."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="ping")
    async def ping(self, ctx: commands.Context):
        """Mostra o ping do bot."""
        await ctx.send(f"{round(self.bot.latency * 1000)}ms")

async def setup(bot: commands.Bot):
    await bot.add_cog(FunCommands(bot))