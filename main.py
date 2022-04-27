#Imports
import discord, requests, json
from discord.ext import commands
from discord.ext import tasks
import keepalive
from keepalive import keep_alive


#settings
token = "your bot token"
prefix = "!"


bot = commands.Bot(command_prefix=prefix)

#Discord status, plus print that bot is on in console
@bot.event
async def on_ready():
	await bot.change_presence(status=discord.Status.do_not_disturb, activity=discord.Activity(type=discord.ActivityType.playing, name="Roblox Friend Bot/Tool Bot"))
	print("bot is online")

#Check User Id Command
@bot.command()
async def checkuserid(ctx, userId=None): 
	
		with requests.get(f'https://users.roblox.com/v1/users/{userId}') as req:
			data=json.loads(req.text)
			description = data["description"]
			created_at = data["created"]
			banned = data["isBanned"]
			ex = data["externalAppDisplayName"]
			id = data["id"]
			name = data["name"]
			displayName = data["displayName"]
			
			embed = discord.Embed(
				title="User Info",
				colour = discord.Colour.blue()
			)
			embed.add_field(name="Display Name",value=displayName,inline=True)
			embed.add_field(name="Name",value=name,inline=True)
			embed.add_field(name="Id",value=id,inline=True)
			embed.add_field(name="Is The user Banned",value=banned,inline=True)
			embed.add_field(name="External App Display Name",value=ex,inline=True)
			embed.add_field(name="Created At",value=created_at,inline=False)
			embed.add_field(name="Desciption",value=description,inline=False)
			embed.set_thumbnail(url=f"https://www.roblox.com/bust-thumbnail/image?userId={userId}&width=420&height=420&format=png'")
			await ctx.send(embed=embed)


#keep alive is for replit, needed for hosting the bot
keep_alive()						
bot.run(token)
