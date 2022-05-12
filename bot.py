import json
import os
import platform
import random
import sys

from token_file import DISCORD_TOKEN

import disnake
from disnake import ApplicationCommandInteraction
from disnake.ext import tasks, commands
from disnake.ext.commands import Bot
from disnake.ext.commands import Context

intents = disnake.Intents.default()

bot = commands.Bot(
    test_guilds=[974059269668343829], # Optional
    sync_commands_debug=True
)

@bot.event
async def on_ready() -> None:
    """
    The code in this even is executed when the bot is ready
    """
    print(f"Logged in as {bot.user.name}")
    print(f"disnake API version: {disnake.__version__}")
    print(f"Python version: {platform.python_version()}")
    print(f"Running on: {platform.system()} {platform.release()} ({os.name})")
    print("-------------------")


@bot.slash_command(description="Responds with 'World'")
async def hello(inter):
    await inter.response.send_message("World")


# execute Bot
bot.run(DISCORD_TOKEN)