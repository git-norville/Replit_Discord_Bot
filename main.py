import os
from keep_alive import keep_alive
import discord
from discord.ext import commands
import pi_maker
from pi_maker import *
my_secret = os.environ['DISCO_KEY']
bot = commands.Bot(command_prefix = "`")

keep_alive()
@bot.event
async def on_ready():
	print("bot is ready")

@bot.command()
async def ping(ctx):
	await ctx.send(f"pong! {round(bot.latency * 1000)}ms")

@bot.command()
async def DYF(ctx, usr_imput):
	ply_stats = list()
	ply_stats = create_pi(usr_imput,ply_stats)
	# tier = stats[0]["tier"]
	# rank = stats[0]["rank"]
	# lp = stats[0]["leaguePoints"]


	await ctx.send(file=discord.File('dyf.png'))

@bot.event
async def on_command_error(ctx, error):
    await ctx.send(f"An error occured: {str(error)}")

bot.run(my_secret)
