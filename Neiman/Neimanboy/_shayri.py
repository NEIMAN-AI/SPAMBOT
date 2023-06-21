from random import choice

from LegendBS.raid import SHAYRI
from pyrogram import Client, filters
from pyrogram.types import *

from Neiman.Config import *

from .. import sudos
from ..core.clients import *

Useru = False


@Client.on_message(filters.user(sudos) & filters.command(["shayri"], prefixes=HANDLER))
async def shayri(Neiman: Client, e: Message):
    usage = f"Command: {HANDLER}shayri -u \nCommand:{HANDLER}shayri -u (reply to anyone)\nCommand: {HANDLER}shayri (count) \nCommand: {HANDLER}shayri (count) (reply to anyone)"
    text = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
    flag = text[0]
    if not flag:
        return await e.reply_text(usage)
    if "-u" in flag:
        global Useru
        Useru = True
        if e.reply_to_message:
            lmao = e.reply_to_message
            while Useru == True:
                for i in range(1, 26):
                    lol = globals()[f"Client{i}"]
                    if lol is not None:
                        await lol.send_message(
                            e.chat.id, f"{lmao.from_user.mention}\n\n{choice(SHAYRI)}"
                        )
        else:
            while Useru == True:
                for i in range(1, 26):
                    lol = globals()[f"Client{i}"]
                    if lol is not None:
                        await lol.send_message(e.chat.id, choice(SHAYRI))
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
                        await lol.send_message(
                            e.chat.id, f"{lmao.from_user.mention}\n\n{choice(SHAYRI)}"
                        )
        else:
            for _ in range(counts):
                for i in range(1, 26):
                    lol = globals()[f"Client{i}"]
                    if lol is not None:
                        await lol.send_message(e.chat.id, choice(SHAYRI))
    else:
        await e.reply_text(usage)
    if LOG_CHANNEL:
        try:
            await Legend.send_message(
                LOG_CHANNEL,
                f"#Started Shayri Spam By User: {e.from_user.id} \n\n Chat: {e.chat.id} \n Counts: {counts}",
            )
        except Exception as a:
            print(a)


@Client.on_message(
    filters.user(sudos) & filters.command(["stopshayri"], prefixes=HANDLER)
)
async def stopshayri(_, e: Message):
    global Useru
    Useru = False
    await e.reply_text("Stopped Unlimited Wish Shayri")
