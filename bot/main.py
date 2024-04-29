import nextcord
from nextcord.ext import commands
import os
from dotenv import load_dotenv

# Getting the bot token
load_dotenv()

token = os.getenv("TOKEN")

# Declaring intents
intents =  nextcord.Intents.all()

# Declaring the bot
bot = commands.Bot(
    intents=intents,
    status=nextcord.Status.online,
    activity=nextcord.Game(name="in development!")
)

# Loading cogs
bot.load_extension('cogs.information')
bot.load_extension('cogs.fun')
bot.load_extension('cogs.affirmation')

# Startup event
@bot.event
async def on_ready():
    print()
    print(f"Logged in as {bot.user} [{bot.application_id}]")
    print()
  
# Running the bot  
bot.run(token)