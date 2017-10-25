# This cog is a modified version of Radio Haru by Mr Boo Grande
import discord
from discord.ext import commands
from cogs.utils import checks
from __main__ import send_cmd_help
import asyncio

class RadioHaru:
    """RADIO!"""

    def __init__(self, bot):
        self.bot = bot
    
    @commands.group(pass_context=True, no_pm=True)
    async def electroradio(self, ctx):
        """Radio Haru"""
        if ctx.invoked_subcommand is None:
            await send_cmd_help(ctx)
            await self.bot.say("https://theendlessweb.com")

    @radioharu.command(pass_context=True, no_pm=True)
    @checks.serverowner_or_permissions(manage_server=True)
    async def play(self, ctx):
        """StartElectroRadio"""
        server = ctx.message.server
        author = ctx.message.author
        if self.voice_connected(server):
            await self.bot.say("Already connected to a voice channel, use `{}radioharu stop` to change radio.".format(ctx.prefix))
        else:
            voice_channel = author.voice_channel
            voice = await self.bot.join_voice_channel(voice_channel)
            Channel = ctx.message.channel
            await self.bot.send_typing(Channel)
            player.start()
            await asyncio.sleep(7)
            player.stop()
            player = voice.create_ffmpeg_player('http://play.theendlessweb.com:8000/listen.pls')
            player.start()
            await self.bot.say(":green_heart: **Here we go! Joining Voice!**")
            
    @radioharu.command(pass_context=True, no_pm=True)
    @checks.serverowner_or_permissions(manage_server=True)
    async def playwin(self, ctx):
        """Play Radio Haru - Use instead of play command if on a Windows machine."""
        server = ctx.message.server
        author = ctx.message.author
        if self.voice_connected(server):
            await self.bot.say("Already connected to a voice channel, use `{}radioharu stop` to change radio.".format(ctx.prefix))
        else:
            voice_channel = author.voice_channel
            voice = await self.bot.join_voice_channel(voice_channel)
            Channel = ctx.message.channel
            await self.bot.send_typing(Channel)
            player = voice.create_ffmpeg_player('https://cdn.discordapp.com/attachments/336598653923753987/360413654224601089/Radio-Haru.ogg')
            player.start()
            await asyncio.sleep(7)
            player.stop()
            await self._disconnect_voice_client(server)
            await self.bot.say(":green_heart: **Playing Radio Haru!**")
            radio = True
            while radio == True:
                voice = await self.bot.join_voice_channel(voice_channel)
                player = voice.create_ffmpeg_player('http://play.theendlessweb.com:8000/listen.pls')
                player.start()
                await asyncio.sleep(300)
                await self._disconnect_voice_client(server)

    @radioharu.command(pass_context=True, no_pm=True)
    @checks.serverowner_or_permissions(manage_server=True)
    async def stop(self, ctx):
        """Say goodbye to your radio :("""
        server = ctx.message.server
        author = ctx.message.author
        await self._disconnect_voice_client(server)
        voice_channel = author.voice_channel
        voice = await self.bot.join_voice_channel(voice_channel)
        player.start()
        await asyncio.sleep(1)
        await self._disconnect_voice_client(server)
        await self.bot.say(":red_circle: **GOODBYE!**")
       
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
