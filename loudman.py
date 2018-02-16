import asyncio
import discord
from discord.ext import commands

print("hi")
Client = discord.Client()
bot = commands.Bot(command_prefix = "?")

if not discord.opus.is_loaded():
    # the 'opus' library here is opus.dll on windows
    # or libopus.so on linux in the current directory
    # you should replace this with the location the
    # opus library is located in and with the proper filename.
    # note that on windows this DLL is automatically provided for you
    discord.opus.load_opus('opus')

@bot.event
async def on_ready():
    print("bot is ready")
    await bot.change_presence(game=discord.Game(name='tom'))
    print('Logged in as:\n{0} (ID: {0.id})'.format(bot.user))

@bot.event
async def on_message(message):
    if message.content.upper().startswith('!SUMMON'):
        UserID = message.author.id
        print(UserID)
        await bot.send_message(message.channel,"<@{}> summoned nibba ".format(UserID))
        summoned_channel = message.author.voice_channel
        await bot.join_voice_channel(summoned_channel)
    if message.content.upper().startswith('!FUCKOFF'):
        await bot.voice.disconnect()





#bot.add_cog(Music(bot))


bot.run('NDE0MDcyODgyMTA5MzQ5OTE4.DWiJCA.4_BGQ0v_Hhp-VG7Cux2z1IsYrSM')
