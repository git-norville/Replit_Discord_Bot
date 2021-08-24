import os
from keep_alive import keep_alive
import discord
from discord.ext import commands
import pi_maker
from pi_maker import *
my_secret = os.environ['DISCO_KEY']
client = commands.Bot(command_prefix = "`")

keep_alive()
@client.event
async def on_ready():
	print("bot is ready")

@client.command()
async def ping(ctx):
	await ctx.send(f"pong! {round(client.latency * 1000)}ms")

@client.command()
async def DYF(ctx, usr_imp):
	ply_stats = list()
	ply_stats = create_pi(usr_imp,ply_stats)
	# tier = stats[0]["tier"]
	# rank = stats[0]["rank"]
	# lp = stats[0]["leaguePoints"]


	await ctx.send(file=discord.File('dyf.png'))

client.run(my_secret)
