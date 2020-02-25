import discord
from discord.ext import commands


async def on_ready():
    pass


async def on_command_error(context, error):
    error = getattr(error, 'original', error)
    await context.send(
        content="%s: %s" % (type(error).__name__, error)
    )
