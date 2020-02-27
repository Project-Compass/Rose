import sys

import discord
from discord.ext import commands

from . import config
from . import version


class CoreCommands(commands.Cog):
    def __init__(self, bot: commands.Bot, *args, **kwargs):
        self.bot = bot
        self.app_info = None
        super(CoreCommands, self).__init__(*args, **kwargs)

    @commands.is_owner()
    @commands.command(
        name="Logout",
        aliases=[
            "Shutdown",
            "Terminate"
        ],
        brief="Initates bot logout and shutdown process."
    )
    async def shutdown(self, context):
        await context.send(content="Alright, see you later! :wave:")
        await self.bot.logout()

    @commands.command(
        name="Status",
        brief="Displays some quick status information about the bot."
    )
    async def status(self, context):
        if self.app_info is None:
            self.app_info = await self.bot.application_info()
        owner = context.guild.get_member(self.app_info.owner.id)
        embed = discord.Embed(
            title="Rose",
            description=f"Version {version.string}",
            colour=owner.colour,
        )
        embed.set_author(
            name="%s (%s#%s)" % (
                owner.nick,
                owner.name,
                owner.discriminator
            ),
            icon_url=owner.avatar_url
        )
        embed.set_thumbnail(url=self.bot.user.avatar_url)
        embed.add_field(
            name="Library",
            value="discord.py " + discord.__version__
        )
        embed.add_field(
            name="Runtime",
            value=f"{sys.implementation.name.title()} {'%d.%d.%d  %s %d' % sys.implementation.version}"
        )
        embed.add_field(
            name="Conformance",
            value='%d.%d.%d  %s %d' % sys.version_info
        )
        await context.send(
            content="Well, it's working at least! That's always a start.",
            embed=embed
        )
