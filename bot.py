import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='?', intents=intents)

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

bot.run('MTE5NTUwMDUxNDMzOTcxNzI2Mg.G5f1D1.O_8bfZM83kyszpK3E39VqDPnAoDtxqtBXXaT3c')