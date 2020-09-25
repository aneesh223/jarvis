import discord, wolframalpha, os
from discord.ext import commands
client = wolframalpha.Client(os.getenv("WA_TOKEN"))
prefix = "$"
bot = commands.Bot(command_prefix=prefix)

@bot.event
async def on_ready():
    print(f"logged in as {bot.user.name}({bot.user.id})")

@bot.command(aliases=["J.A.R.V.I.S.", "J.a.r.v.i.s.", "j.a.r.v.i.s.", "JARVIS", "Jarvis", "jarvis", ""])
async def _(ctx, *, query):
    await ctx.send(str(next(client.query(query).results).text))

bot.run(os.getenv("DISCORD_TOKEN"))