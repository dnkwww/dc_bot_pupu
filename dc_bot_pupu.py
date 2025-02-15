import discord
from discord.ext import commands, tasks
import datetime
import asyncio
import requests

# 設定機器人
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="%", intents=intents)

# 設定初始N值
N = 40
CHANNEL_ID = 1326434015993135217

@bot.event
async def on_ready():
    print(f"目前登入身份 --> {bot.user}")
    await wait_until_6am()  # 等待到早上6點
    daily_message.start()

async def send_message():
    global N
    now = datetime.datetime.now()
    date_str = now.strftime("%Y/%m/%d")
    weekday_map = {0: "一", 1: "二", 2: "三", 3: "四", 4: "五", 5: "六", 6: "日"}
    weekday_str = weekday_map[now.weekday()]
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        await channel.send(f"# 第{N}屆便便交流\n{date_str}( {weekday_str} )")
    N += 1

async def wait_until_6am():
    now = datetime.datetime.now()
    target = now.replace(hour=6, minute=0, second=0, microsecond=0)
    if now > target:  # 如果現在時間已經過了今天的6:00，則等待到明天的6:00
        target += datetime.timedelta(days=1)
    wait_time = (target - now).total_seconds()
    print(f"距離早上6:00 還有 {wait_time // 3600} 小時 {wait_time % 3600 // 60} 分鐘")
    await asyncio.sleep(wait_time)

# 每24小時執行一次
@tasks.loop(hours=24)
async def daily_message():
    await send_message()

bot.run("MTM0MDE5NDk5MjY2MDE1NjQyNw.GwVb_A.EUpnZooXOLP7T17El08Mhtlv-LLY__aHrWHX-M")

