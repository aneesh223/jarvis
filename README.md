# Hosting your repl based discord.py bot on Heroku to keep it running **INDEFINETLY**
[![Join Discord](https://discordapp.com/api/guilds/745448868040409148/widget.png?style=shield)](https://discord.gg/6GPjN8C)

### Prerequisites
You must have an account for [Discord](https://discord.com/register), [GitHub](https://github.com/join) , [Heroku](https://signup.heroku.com/), and [Repl.it](https://repl.it/signup) (you probably have an account already).

### 1. Create a bot and get its token
* Create an application in the developer portal [here](https://discordapp.com/developers/applications/)
* Open up your new application and click 'Add Bot' under the Bot settings to create your bot.
* After creating the bot, click the 'Copy' button under the title Token. Take note of your token as you will need it later.

### 2. Create a new repository from this one
* Create a new repository from this one [here](https://github.com/syntax-corp/discordpy-replit-heroku/generate). Follow all the prompts and hit "Create repository from template" This contains all the code you need to host your bot on Heroku.
* Open a new tab and put in this link: https://repl.it/github/YOUR_GITHUB_USERNAME_HERE/YOUR_REPO_NAME_HERE

### 3. Set up Heroku
* Create an application for Heroku [here](https://dashboard.heroku.com/new-app).
* Under 'Deploy', do the following:
  * Deployment Method => Connect your GitHub
  * App connected to GitHub => Search for the forked repository
  * Automatic Deploy => Enable Automatic Deploy (to redeploy after every commit)
* Under 'Settings', click on 'Reveal Config Vars' and enter the following:
  * KEY => DISCORD_TOKEN
  * VALUE => (Enter the bot token that you copied from the developer portal)
  * Click the 'Add' button after entering all of this information.
* Under 'Resources', do the following:
  * Click on the 'Pencil' icon.
  * Switch the worker from off to on.
  * Click 'Confirm' to finalize the decision.
  * NOTE: You are given 550 free Dyno hours, which will not last the entire month. However, if you provide a credit card to verify your identity, you are given an additional 450 hours, which will allow your bot to run indefinitely. **You will not be charged for this.**

### What's next?
* Now you can tweak the main.py file as you please! just don't mess with the first 5 or last 2 lines (you can change the prefix in line 4 though.)
* You can change the @app.route stiff in server.py
* You can also change base.html and index.html without changing the stuff inside {% %} or {}, and you are able to change the css and js files freely
* Don't change the rest of the files or the name of any file or folder unless you know what you're doing
* Don't under any circumstances rename the "static" and "templates" folders

### Original code belongs to audieni. I just made it more suitable for repl.it bot creators. Visit his repository [here](https://github.com/audieni/discord-py-heroku)
I forked from his though IDK why it doesnt say
