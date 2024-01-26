import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='your_prefix', intents=intents)

@bot.command()
async def your_message(ctx):
    await ctx.send('bot_message')

bot.run('Your_token')