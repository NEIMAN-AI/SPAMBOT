from random import choice

from LegendBS.birthday import bdmsg, birthdayimage
from pyrogram import Client, filters
from pyrogram.types import *

from Neiman.Config import *

from .. import sudos
from ..core.clients import *

bd = False


@Client.on_message(
    filters.user(sudos) & filters.command(["birthday"], prefixes=HANDLER)
)
async def brthdaycmd(Legend: Client, e: Message):
    usage = f"Command: {HANDLER}birthday -u \nCommand:{HANDLER}birthday -u (reply to anyone)\nCommand: {HANDLER}birthday (count) \nCommand: {HANDLER}birthday (count) (reply to anyone)"
    text = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
    flag = text[0]
    if not flag:
        return await e.reply_text(usage)
    if "-u" in flag:
        global bd
        bd = True
        if e.reply_to_message:
            lmao = e.reply_to_message
            while bd == True:
                for i in range(1, 26):
                    lol = globals()[f"Client{i}"]
                    if lol is not None:
                        await lol.send_message(
                            e.chat.id, f"{lmao.from_user.mention}\n\{choice(bdmsg)}"
                        )
        else:
            while bd == True:
                for i in range(1, 26):
                    lol = globals()[f"Client{i}"]
                    if lol is not None:
                        await lol.send_message(e.chat.id, choice(bdmsg))
    elif "-u" not in flag:
        try:
            counts = int(text[0])
        except ValueError:
            return await e.reply_text(usage)
        if e.reply_to_message:
            lmao = e.reply_to_message
            for _ in range(counts):
                for i in range(1, 26):
                    lol = globals()[f"Client{i}"]
                    if lol is not None:
                        await lol.send_photo(
                            e.chat.id,
                            choice(birthdayimage),
                            caption=f"{lmao.from_user.mention}\n\n{choice(bdmsg)}",
                        )
        else:
            for _ in range(counts):
                for i in range(1, 26):
                    lol = globals()[f"Client{i}"]
                    if lol is not None:
                        await lol.send_photo(
                            e.chat.id, choice(birthdayimage), caption=choice(bdmsg)
                        )
    else:
        await e.reply_text(usage)
    if LOG_CHANNEL:
        try:
            await Legend.send_message(
                LOG_CHANNEL,
                f"#Started 🎂 Birthday Spam By User: {e.from_user.id} \n\n Chat: {e.chat.id} \n Counts: {counts}",
            )
        except Exception as a:
            print(a)


@Client.on_message(filters.user(sudos) & filters.command(["stopbd"], prefixes=HANDLER))
async def stopbd(_, e: Message):
    global bd
    bd = False
    await e.reply_text("Stopped Unlimited Wish Happy Birthday")
