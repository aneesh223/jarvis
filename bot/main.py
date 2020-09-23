import json, apiai, discord, asyncio, os, server

client = discord.Client()
token = os.getenv("DISCORD_TOKEN")
client_token = os.getenv("DF_TOKEN")
ai = apiai.ApiAI(client_token)


@client.event
async def on_ready():
    print(f'logged in as {client.user.name}({client.user.id})')

@client.event
async def on_message(message):
    if not message.author.bot:
        try:
            if message.content.startswith("$"):
                msg = message.content.split("$", 1)
                request = ai.text_request()
                request.query = msg

                response = json.loads(request.getresponse().read()) # Get the json from dialogflow
                print(response)
                
                result = response['result'] # Get the actual plaintext reply
                action = result.get('action') # Get the action (this can be helpful if you want to make the bot able to run commands when asked. For example, telling the bot to send help could make it DM a user with a help command)

                await message.channel.send(response['result'], ['fulfillment'], ['speech']) # Send the message and tag the message author

        except KeyError: # If the bot gets input dialogflow can't handle, it will raise a KeyError
            await message.channel.send("KeyError!")

server.server()
client.run(token)