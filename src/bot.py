##C45 Bot for the c45 discord server
# TODO:
# * Add functionality to access bnet
# * Add functionality to host files
# * Add functionality to play songs
# * Add reminders (bot will message if something is due)
# * Welcome messgaes and role assignment
import discord
from discord.ext import commands
import os

bot = commands.Bot(command_prefix='>')

@bot.command()
async def test(ctx, arg):
        await ctx.send(arg)

token = os.getenv("C45_Token");
bot.run(token)
