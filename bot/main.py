import discord
from discord.ext import commands
import wikipedia, os
from chatbot import Chat, register_call
import server
prefix = ""
TOKEN = os.getenv("DISCORD_TOKEN")
bot = commands.Bot(command_prefix = prefix)
@register_call("whoIs")
def who_is(query, session_id="general"):
    try:
        return wikipedia.summary(query)
    except Exception:
        for new_query in wikipedia.search(query):
            try:
                return wikipedia.summary(new_query)
            except Exception:
                pass
    return "I don't know about "+query
template_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"chatbot","chatbot.template")
chat=Chat(template_file_path)
@bot.event
async def on_ready():
    print(f"looged in as {bot.user.name}({bot.user.id})")
@bot.command(pass_context = True, aliases=["@J.A.R.V.I.S#5351", "J.A.R.V.I.S.", "J.A.R.V.I.S", "JARVIS"])
async def jarvis(ctx,*,message):
    result = chat.respond(message)
    if(len(result)<=2048):
        embed=discord.Embed(title="J.A.R.V.I.S.", description = result, color = (0xF48D1))
        await ctx.send(embed=embed)
    else:
        embedList = []
        n=2048
        embedList = [result[i:i+n] for i in range(0, len(result), n)]
        for num, item in enumerate(embedList, start = 1):
            if(num == 1):
                embed = discord.Embed(title="J.A.R.V.I.S.", description = item, color = (0xF48D1))
                embed.set_footer(text="Page {}".format(num))
                await ctx.send(embed = embed)
            else:
                embed = discord.Embed(description = item, color = (0xF48D1))
                embed.set_footer(text = "Page {}".format(num))
                await ctx.send(embed = embed)
server.server()
bot.run(TOKEN)
