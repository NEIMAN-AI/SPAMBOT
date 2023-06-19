import asyncio
from random import choice

from LegendBS.raid import RAID, RRAID
from pyrogram import Client, filters
from pyrogram.types import Message

from LegendGirl.Config import *

from .. import sudos
from ..core.clients import *


@Client.on_message(filters.user(sudos) & filters.command(["raid"], prefixes=HANDLER))
async def raid(Legend: Client, e: Message):
    usage = f"Command :- {HANDLER}raid (count) (reply to anyone)\nUsage :- `{HANDLER}raid 3 <reply to anyone>`\n\nCommand :- {HANDLER}raid <count> <username>\nUsage :- `{HANDLER}raid 3 @Hekeke`"
    lol = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
    chat = e.chat
    try:
        counts = int(lol[0])
    except ValueError:
        return await e.reply_text(usage)
    if len(lol) == 2:
        if not counts:
            await e.reply_text(
                f"Gib raid Counts or use `{HANDLER}.uraid` for Unlimited raid!"
            )
            return
        owo = lol[1]
        if not owo:
            await e.reply_text(
                "you need to specify an user! Reply to any user or gime id/username"
            )
            return
        try:
            user = await Legend.get_users(lol[1])
        except:
            await e.reply_text("**Error:** User not found!")
            return
    elif e.reply_to_message:
        try:
            user = await Legend.get_users(e.reply_to_message.from_user.id)
        except:
            user = e.reply_to_message.from_user
    else:
        await e.reply_text(usage)
        return
    for _ in range(counts):
        raid = choice(RAID)
        for i in range(1, 26):
            lol = globals()[f"Client{i}"]
            if lol is not None:
                await lol.send_message(chat.id, f"{user.mention} {raid}")
                await asyncio.sleep(0.3)
    if LOG_CHANNEL:
        try:
            await Legend.send_message(
                LOG_CHANNEL,
                f"started Raid By User: {e.from_user.id} \n\n On User: {mention} \n Chat: {e.chat.id} \n Counts: {counts}",
            )
        except Exception as a:
            print(a)


USERS = []


@Client.on_message(
    filters.user(sudos) & filters.command(["rraid", "replyraid"], prefixes=HANDLER)
)
async def rraid(Legend: Client, e: Message):
    global USERS
    try:
        lol = e.text.split(" ", 1)[1].split(" ", 1)
    except IndexError:
        lol = None
    if e.reply_to_message and e.reply_to_message.from_user:
        user = e.reply_to_message.from_user
    elif lol:
        user_ = lol[0]
        if user_.isnumeric():
            user_ = int(user_)
        if not user_:
            return await e.reply_text(
                "I don't know who you're talking about, you're going to need to specify a user.!"
            )
        try:
            user = await Legend.get_users(user_)
        except (TypeError, ValueError):
            return await message.reply_text(
                "Looks like I don't have control over that user, or the ID isn't a valid one. If you reply to one of their messages, I'll be able to interact with them."
            )
    else:
        return await e.reply_text(
            "I don't know who you're talking about, you're going to need to specify a user...!"
        )
    if int(user.id) in USERS:
        return await e.reply_text("User already in Raid list!")
    USERS.append(user.id)
    mention = user.mention
    await e.reply_text(f"Reply Raid Activated On User {mention}")
    if LOG_CHANNEL:
        try:
            await Legend.send_message(
                LOG_CHANNEL,
                f"Activated Reply Raid By User: {e.from_user.id} \n\n On User: {mention} \n Chat: {e.chat.id}",
            )
        except Exception as a:
            print(a)


@Client.on_message(
    filters.user(sudos) & filters.command(["draid", "dreplyraid"], prefixes=HANDLER)
)
async def draid(Legend: Client, e: Message):
    global USERS
    try:
        lol = e.text.split(" ", 1)[1].split(" ", 1)
    except IndexError:
        lol = None
    if e.reply_to_message and e.reply_to_message.from_user:
        user = e.reply_to_message.from_user
    elif lol:
        user_ = lol[0]
        if user_.isnumeric():
            user_ = int(user_)
        if not user_:
            await e.reply_text(
                "I don't know who you're talking about, you're going to need to specify a user.!"
            )
            return
        try:
            user = await Legend.get_users(user_)
        except (TypeError, ValueError):
            await message.reply_text(
                "Looks like I don't have control over that user, or the ID isn't a valid one. If you reply to one of their messages, I'll be able to interact with them."
            )
            return
    else:
        await e.reply_text(
            "I don't know who you're talking about, you're going to need to specify a user...!"
        )
        return
    if int(user.id) not in USERS:
        await e.reply_text("User not in Raid list!")
        return
    USERS.remove(user.id)
    mention = user.mention
    await e.reply_text(f"Reply Raid Deactivated Successfully On User {mention}")
    if LOG_CHANNEL:
        try:
            await Legend.send_message(
                LOG_CHANNEL,
                f" Deactivated Reply Raid By User: {e.from_user.id} \n\n User: {mention} \n Chat: {e.chat.id}",
            )
        except Exception as a:
            print(a)


@Client.on_message(
    filters.user(sudos) & filters.command(["rlist", "raidlist"], prefixes=HANDLER)
)
async def rlist(Legend: Client, e: Message):
    global USERS
    _reply = "**Raid users list - Legend Bot Spam** \n\n"
    if len(USERS) > 0:
        for x in USERS:
            try:
                user = await Legend.get_users(x)
                _reply += f" ✨ Users: {user.mention} \n"
            except:
                _reply += f" ✨ Users: [{x}](tg://user?id={x}) \n"
    else:
        await e.reply_text("Not yet!")
        return
    await e.reply_text(_reply)


@Client.on_message(filters.all)
async def checkraid(Legend: Client, msg: Message):
    global USERS
    if int(msg.from_user.id) in USERS:
        await msg.reply_text(choice(RRAID))
