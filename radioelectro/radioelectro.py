# This cog is a modified version of Radio Haru by Mr Boo Grande
import discord
from discord.ext import commands
from cogs.utils import checks
from __main__ import send_cmd_help
import asyncio

class RadioHaru:
    """ElectroRadio"""

    def __init__(self, bot):
        self.bot = bot
        self.use_avconv = self.bot.get_cog("Audio").settings["AVCONV"]
    
    @commands.group(pass_context=True, no_pm=True)
    async def radioelectro(self, ctx):
        """Radio Haru"""
        if ctx.invoked_subcommand is None:
            await send_cmd_help(ctx)
            await self.bot.say("https://radioharu.pw/")

    @radioelectro.command(pass_context=True, no_pm=True)
    @checks.serverowner_or_permissions(manage_server=True)
    async def play(self, ctx):
        """Play Radio Haru"""
        server = ctx.message.server
        author = ctx.message.author
        if self.voice_connected(server):
            await self.bot.say("Already connected to a voice channel, use `{}radioharu stop` to change radio.".format(ctx.prefix))
        else:
            voice_channel = author.voice_channel
            voice = await self.bot.join_voice_channel(voice_channel)
            Channel = ctx.message.channel
            await self.bot.send_typing(Channel)   
            await asyncio.sleep(7)
            player = voice.create_ffmpeg_player('https://stream.radioharu.pw/owo', use_avconv=self.use_avconv)
            player.start()
            await self.bot.say(":green_heart: **Playing Radio Haru!**")
            
   
    @radioelectro.command(pass_context=True, no_pm=True)
    @checks.serverowner_or_permissions(manage_server=True)
    async def stop(self, ctx):
        """Stop Radio Haru"""
        server = ctx.message.server
        author = ctx.message.author
        await self._disconnect_voice_client(server)
        voice_channel = author.voice_channel
        voice = await self.bot.join_voice_channel(voice_channel)
        player = voice.create_ffmpeg_player('https://cdn.discordapp.com/attachments/336598653923753987/360425539309142037/radioharu_goodbye.mp3')
        player.start()
        await asyncio.sleep(1)
        await self._disconnect_voice_client(server)
        await self.bot.say(":red_circle: **Stopped playing Radio!**")
        
        
    def voice_client(self, server):
        return self.bot.voice_client_in(server)

    def voice_connected(self, server):
        if self.bot.is_voice_connected(server):
            return True
        return False

    async def _disconnect_voice_client(self, server):
        if not self.voice_connected(server):
            return

        voice_client = self.voice_client(server)

        await voice_client.disconnect()

def setup(bot):
    bot.add_cog(RadioHaru(bot))
