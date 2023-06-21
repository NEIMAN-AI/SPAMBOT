import datetime
import os
import sys
import time

from LegendBS.get_time import get_time
from pyrogram import Client, filters
from pyrogram.types import Message

from Neiman import start_time
from Neiman.Config import *

from .. import sudos
from ..core.clients import *

if PING_PIC:
    PING_PIC = PING_PIC
else:
    PING_PIC = "https://graph.org/file/8b665536aee97ee58f5ca.jpg"


@Client.on_message(filters.user(sudos) & filters.command(["ping"], prefixes=HANDLER))
async def ping(_, e: Message):
    start = datetime.datetime.now()
    uptime = get_time((time.time() - start_time))
    a = await e.reply_text("Pong")
    end = datetime.datetime.now()
    ms = (end - start).microseconds / 1000
    await a.delete()
    ping_temp = f"🏓 Ping Pong\n\n✨ Ping: {ms}\n✨Uptime: {uptime}"
    for i in range(1, 26):
        lol = globals()[f"Client{i}"]
        if lol is not None:
            if ".jpg" in PING_PIC or ".png" in PING_PIC:
                await lol.send_photo(e.chat.id, PING_PIC, caption=ping_temp)
            elif ".mp4" in PING_PIC.lower():
                await lol.send_video(e.chat.id, PING_PIC, caption=ping_temp)
            else:
                await lol.send_message(e.chat.id, ping_temp)


@Client.on_message(
    filters.user(sudos) & filters.command(["restart", "reboot"], prefixes=HANDLER)
)
async def restarter(Legend: Client, message: Message):
    await message.reply_text(
        f"**Bot Is Restarting**\n\n Please Wait 5 min till bot is restart.\nAfter 5 Min Type {HANDLER}ping"
    )
    try:
        await Legend.stop()
    except Exception as error:
        print(str(error))

    args = [sys.executable, "-m", "Neiman"]
    os.execl(sys.executable, *args)
    quit()
