from random import randrange

from discord import Member
from discord.ext.commands.bot import Bot
from redbot.core import bank
from redbot.core.commands import Cog, command
from redbot.core.commands.context import Context
from redbot.core.utils.chat_formatting import bold, italics

from basic.emoji import Emoji
from basic.utils import repeatchar

version = "0.0.1"


class Basic(Cog):
    """
    Basic text only commands
    """

    def __init__(self, bot: Bot) -> None:
        self.bot = bot

    @command()
    async def version(self, ctx: Context) -> None:
        await ctx.send(f"{version}")

    @command()
    async def size(self, ctx: Context) -> None:
        """
        For those seeking validation
        """
        length = randrange(1, 10)
        shaft = repeatchar("=", length)
        representation = f"8{shaft}D"
        message = "That's kinda small" if length < 5 else "That's quite big"
        reaction = italics("Yikes") if length < 5 else bold("Impressive")

        await ctx.send(
            "{}\n{}... {}".format(representation, message, italics(reaction))
        )

    @command()
    async def bicep(
        self,
        ctx: Context,
        user: Member,
    ) -> None:
        """
        How big is your flex
        """
        if user is None:
            user = ctx.author

        balance = await bank.get_balance(user)
        length = len(str(balance))
        reaction = Emoji.OMEGALUL
        if length > 1:
            reaction = Emoji.LUL
        if length > 2:
            reaction = Emoji.SeemsGood
        if length > 3:
            reaction = Emoji.MonkaS
        if length > 4:
            reaction = Emoji.FiteHard

        await ctx.send("{} digits... {}".format(length, reaction))

    @command()
    async def never(self, ctx: Context) -> None:
        """
        Who knows
        """
        await ctx.send("{} who knows...".format(Emoji.FeelsBadMan))
