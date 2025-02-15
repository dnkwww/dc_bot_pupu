# 導入Discord.py模組
import discord
# 導入commands指令模組
from discord.ext import commands

# intents是要求機器人的權限
intents = discord.Intents.all()
# command_prefix是前綴符號，可以自由選擇($, #, &...)
bot = commands.Bot(command_prefix="%", intents=intents)

@bot.event
# 當機器人完成啟動時
async def on_ready():
    print(f"目前登入身份 --> {bot.user}")

@bot.command()
# 輸入 %Hello 呼叫指令
async def Hello(ctx):
    # 回覆 Hello, world!
    await ctx.send("Hello, world!")

bot.run("MTM0MDE5NDk5MjY2MDE1NjQyNw.GwVb_A.EUpnZooXOLP7T17El08Mhtlv-LLY__aHrWHX-M")

