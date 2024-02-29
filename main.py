import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='?', intents=intents)
client.run("MTE5NTUwMDUxNDMzOTcxNzI2Mg.G5f1D1.O_8bfZM83kyszpK3E39VqDPnAoDtxqtBXXaT3c")
client.remove_command('help')


@client.command()
async def text(ctx, arg):
    await ctx.send(arg)