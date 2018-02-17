import discord
from discord.ext import commands


class Unban:
    """Unban Users"""

    def __init__(self, bot):
        self.bot = bot
        self.modcog = self.bot.get_cog("Mod")

    @commands.command(pass_context=True)
    async def unban(self, ctx, userid):
        """Unban Users"""
        userobj = await self.bot.get_user_info(userid)
        await self.bot.unban(ctx.message.server, userobj)
        await self.modcog.new_case(ctx.message.server, user=userobj, action="UNBAN")
        await self.bot.say("Done.")


def setup(bot):
    bot.add_cog(Unban(bot))
