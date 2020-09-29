import discord, wolframalpha, os, server
from discord.ext import commands
client = wolframalpha.Client(os.getenv("WA_TOKEN"))
prefix = "j!"
bot = commands.Bot(command_prefix=prefix)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(f'{prefix} <ask anything> (VERY IMPORTANT YOU PUT SPACE BETWEEN {prefix} AND COMMAND)'))
    print(f"logged in as {bot.user.name}({bot.user.id})")

@bot.command(aliases=["J.A.R.V.I.S.", "J.a.r.v.i.s.", "j.a.r.v.i.s.", "JARVIS", "Jarvis", "jarvis", ""])
async def _(ctx, *, query):
    if str(next(client.query(query).results).text) == "My name is Wolfram|Alpha.":
      await ctx.send("My name is J.A.R.V.I.S.")
    else:
      await ctx.send(str(next(client.query(query).results).text))

server.server()
bot.run(os.getenv("DISCORD_TOKEN"))