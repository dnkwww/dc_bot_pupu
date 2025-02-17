import discord
from discord.ext import commands, tasks
import datetime
import asyncio
import pytz

# 設定機器人
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="%", intents=intents)
token = ""

CHANNEL_ID = 1326434015993135217

# 計算今天是第幾屆(1/8第一屆)
def calculate_n():
    tw = pytz.timezone("Asia/Taipei")  # 設定時區為台灣時間
    now = datetime.datetime.now(tw)

    # 基準日(1/8)
    base_date = datetime.datetime(now.year, 1, 8, tzinfo=tw)

    # 計算相差的天數
    days_since_base = (now - base_date).days

    # 因為1/8是第一屆，N=base+1
    return days_since_base + 1

# 發送訊息
async def send_message():
    N = calculate_n()  # 計算當前第幾屆
    tw = pytz.timezone("Asia/Taipei")  # 設定時區為台灣時間
    now = datetime.datetime.now(tw)
    date_str = now.strftime("%Y/%m/%d")

    weekday_map = {0: "一", 1: "二", 2: "三", 3: "四", 4: "五", 5: "六", 6: "日"}
    weekday_str = weekday_map[now.weekday()]

    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        await channel.send(f"# 第{N}屆便便交流\n{date_str}( {weekday_str} )")

# 固定發送訊息時間為早上6.
async def wait_until_6am():
    tw = pytz.timezone("Asia/Taipei")  # 設定時區為台灣時間
    now = datetime.datetime.now(tw)
    target = now.replace(hour=6, minute=0, second=0, microsecond=0)
    if now > target:  # 如果現在時間已經過了今天的6:00，則等待到明天的6:00
        target += datetime.timedelta(days=1)

    wait_time = (target - now).total_seconds()
    print(f"距離早上6:00 還有 {wait_time // 3600} 小時 {wait_time % 3600 // 60} 分鐘")
    await asyncio.sleep(wait_time)

@bot.event
async def on_ready():
    print(f"目前登入身份 --> {bot.user}")
    await wait_until_6am()  # 等待到早上6點
    daily_message.start()

# 每24小時執行一次
@tasks.loop(hours=24)
async def daily_message():
    await send_message()

bot.run(token)

