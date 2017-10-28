# This cog is a modified version of Radio Haru by Mr Boo Grande
import discord
from discord.ext import commands
from cogs.utils import checks
from __main__ import send_cmd_help
import asyncio
from urllib.request import urlopen

class RadioElectro:
    """Radio Electro :)"""

    def __init__(self, bot):
        self.bot = bot
        self.use_avconv = self.bot.get_cog("Audio").settings["AVCONV"]
    
    @commands.group(pass_context=True, no_pm=True)
    async def radioelectro(self, ctx):
        """Radio Electro Subcommands"""
        if ctx.invoked_subcommand is None:
            await send_cmd_help(ctx)
            
    @radioelectro.command(pass_context=True, no_pm=True)
    @checks.serverowner_or_permissions(manage_server=True)
    async def play(self, ctx, voice_channel: discord.Channel=None):
        """Play Radio Electro"""
        server = ctx.message.server
        author = ctx.message.author
        if voice_channel == None:
            voice_channel = author.voice_channel
        if self.voice_connected(server):
            await self.bot.say("Already connected to a voice channel, use `{}radioelectro stop` to change radio.".format(ctx.prefix))
        else:
            try:
                voice = await self.bot.join_voice_channel(voice_channel)
                Channel = ctx.message.channel
                await self.bot.send_typing(Channel)
                player = voice.create_ffmpeg_player('https://cdn.discordapp.com/attachments/247447709798105098/373222902612492291/Output_thing.ogg', use_avconv=self.use_avconv)
                player.start()
                await self.bot.say("Opening connection to server -- This can take a bit!")
                await asyncio.sleep(15)
                player.stop()
                player = voice.create_ffmpeg_player('http://play.theendlessweb.com:8000/stream', use_avconv=self.use_avconv)
                player.start()
                await self.bot.say(":green_heart: Starting **RADIO ELECTRO**")
                await asyncio.sleep(1000)
            except InvalidArgument:
                await self.bot.say("You either didn't enter a voice channel to connect to, or weren't in one!")
   
    @radioelectro.command(pass_context=True, no_pm=True)
    @checks.serverowner_or_permissions(manage_server=True)
    async def stop(self, ctx):
        """Stop Radio Electro"""
        server = ctx.message.server
        author = ctx.message.author
        await self._disconnect_voice_client(server)
        await self.bot.say(":red_circle: **Stopped playing Radio!**")
        
    @radioelectro.command()
    async def nowplaying(self):
        """Get Now Playing Song"""
        stream_url = 'http://play.theendlessweb.com:8000/stream'
        request = Request(stream_url)
        try:
            request.add_header('Icy-MetaData', 1)
            response = urlopen(request)
            icy_metaint_header = response.headers.get('icy-metaint')
            if icy_metaint_header is not None:
                metaint = int(icy_metaint_header)
                read_buffer = metaint+255
                content = response.read(read_buffer)
                title = content[metaint:].split("'")[1]
                await self.bot.say(title)
        except:
            await self.bot.say("There was an error! Check your console!")
        
    @radioelectro.command(pass_context=True, no_pm=True)
    @checks.serverowner_or_permissions(manage_server=True)
    async def restart(self, ctx):
        """Restart if your bot has issues, useful for scheduler"""
        server = ctx.message.server
        voice_channel = author.voice_channel
        if not self.voice_connected(server):
            await self.bot.say("Not in a voice channel, please use `{}radioelectro play` to play radio.".format(ctx.prefix))
        else:
            await self._disconnect_voice_client(server)
            voice = await self.bot.join_voice_channel(voice_channel)
            player = voice.create_ffmpeg_player('http://play.theendlessweb.com:8000/stream', use_avconv=self.use_avconv)
            player.start()
            await asyncio.sleep(1000)
            
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
    bot.add_cog(RadioElectro(bot))
