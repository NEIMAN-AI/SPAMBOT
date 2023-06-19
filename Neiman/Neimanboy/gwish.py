from pyrogram import Client, filters

from pyrogram.types import *

from LegendGirl.Config import *

from .. import sudos

from ..core.clients import *

wish = False

@Client.on_message(

    filters.user(sudos) & filters.command(["gm", "gdmrng"], prefixes=HANDLER)

)

async def gdmrngcmd(Legend: Client, e: Message):

    usage = f"Command: {HANDLER}gm -u \nCommand:{HANDLER}gm -u (reply to anyone)\nCommand: {HANDLER}gm (count) \nCommand: {HANDLER}gm (count) (reply to anyone)"

    text = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)

    flag = text[0]

    if not flag:

        return await e.reply_text(usage)

    wishgdmrng = "╭━━━┳━━━┳━━━┳━━━╮\n┃╭━╮┃╭━╮┃╭━╮┣╮╭╮┃\n┃┃╱╰┫┃╱┃┃┃╱┃┃┃┃┃┃\n┃┃╭━┫┃╱┃┃┃╱┃┃┃┃┃┃\n┃╰┻━┃╰━╯┃╰━╯┣╯╰╯┃\n╰━━━┻━━━┻━━━┻━━━╯.\n\n╱╱╱╱╱╱╱╱╱╱╭╮\n╭━━┳━┳┳┳━┳╋╋━┳┳━╮\n┃┃┃┃╋┃╭┫┃┃┃┃┃┃┃╋┃\n╰┻┻┻━┻╯╰┻━┻┻┻━╋╮┃\n╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰━╯"

    if "-u" in flag:

        global wish

        wish = True

        if e.reply_to_message:

            lmao = e.reply_to_message

            while wish == True:

                for i in range(1, 26):

                    lol = globals()[f"Client{i}"]

                    if lol is not None:

                        await lol.send_message(

                            e.chat.id, f"{lmao.from_user.mention}\n\n{wishgdmrng}"

                        )

        else:

            while wish == True:

                for i in range(1, 26):

                    lol = globals()[f"Client{i}"]

                    if lol is not None:

                        await lol.send_message(e.chat.id, wishgdmrng)

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

                            e.chat.id, f"{lmao.from_user.mention}\n\n{wishgdmrng}"

                        )

        else:

            for _ in range(counts):

                for i in range(1, 26):

                    lol = globals()[f"Client{i}"]

                    if lol is not None:

                        await lol.send_message(e.chat.id, wishgdmrng)

    else:

        await e.reply_text(usage)

    if LOG_CHANNEL:

        try:

            await Legend.send_message(

                LOG_CHANNEL,

                f"#Started Good Morning Spam By User: {e.from_user.id} \n\n Chat: {e.chat.id} \n Counts: {counts}",

            )

        except Exception as a:

            print(a)

@Client.on_message(

    filters.user(sudos) & filters.command(["ga", "gdafternoon"], prefixes=HANDLER)

)

async def gdaftrnooncmd(Legend: Client, e: Message):

    usage = f"Command: {HANDLER}ga -u \nCommand:{HANDLER}ga -u (reply to anyone)\nCommand: {HANDLER}ga (count) \nCommand: {HANDLER}ga (count) (reply to anyone)"

    text = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)

    flag = text[0]

    if not flag:

        return await e.reply_text(usage)

    wishgdaftrnoon = (

        f"╭━━━┳━━━┳━━━┳━━━╮\n┃╭━╮┃╭━╮┃╭━╮┣╮╭╮┃\n┃┃╱╰┫┃╱┃┃┃╱┃┃┃┃┃┃\n┃┃╭━┫┃╱┃┃┃╱┃┃┃┃┃┃\n┃╰┻━┃╰━╯┃╰━╯┣╯╰╯┃\n╰━━━┻━━━┻━━━┻━━━╯\n╭━━━╮\n┃╭━╮┃\n┃┃╱┃┃\n┃╰━╯┃\n┃╭━╮┃\n╰╯╱╰╯\n╭━━━╮\n┃╭━━╯\n┃╰━━╮\n┃╭━━╯\n┃┃\n╰╯\n╭━━━━╮\n┃╭╮╭╮┃\n╰╯┃┃╰╯\n╱╱┃┃\n╱╱┃┃\n╱╱╰╯\n╭━━━╮\n┃╭━━╯\n┃╰━━╮\n┃╭━━╯\n┃╰━━╮\n╰━━━╯\n╭━━━╮\n┃╭━╮┃\n┃╰━╯┃\n┃╭╮╭╯\n┃┃┃╰╮\n╰╯╰━╯\n╭━╮╱╭╮\n┃┃╰╮┃┃\n┃╭╮╰╯┃\n┃┃╰╮┃┃\n┃┃╱┃┃┃\n╰╯╱╰━╯\n╭━━━╮\n┃╭━╮┃\n┃┃╱┃┃\n┃┃╱┃┃\n┃╰━╯┃\n╰━━━╯\n╭━━━╮\n┃╭━╮┃\n┃┃╱┃┃\n┃┃╱┃┃\n┃╰━╯┃\n╰━━━╯\n╭━╮╱╭╮\n┃┃╰╮┃┃\n┃╭╮╰╯┃\n┃┃╰╮┃┃\n┃┃╱┃┃┃\n╰╯╱╰━╯",

    )

    if "-u" in flag:

        global wish

        wish = True

        if e.reply_to_message:

            lmao = e.reply_to_message

            while wish == True:

                for i in range(1, 26):

                    lol = globals()[f"Client{i}"]

                    if lol is not None:

                        await lol.send_message(

                            e.chat.id, f"{lmao.from_user.mention}\n\n{wishgdaftrnoon}"

                        )

        else:

            while wish == True:

                for i in range(1, 26):

                    lol = globals()[f"Client{i}"]

                    if lol is not None:

                        await lol.send_message(e.chat.id, wishgdaftrnoon)

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

                            e.chat.id, f"{lmao.from_user.mention}\n\n{wishgdaftrnoon}"

                        )

        else:

            for _ in range(counts):

                for i in range(1, 26):

                    lol = globals()[f"Client{i}"]

                    if lol is not None:

                        await lol.send_message(e.chat.id, wishgdaftrnoon)

    else:

        return await e.reply_text(usage)

    if LOG_CHANNEL:

        try:

            await Legend.send_message(

                LOG_CHANNEL,

                f"#Started Good Afternoon Spam By User: {e.from_user.id} \n\n Chat: {e.chat.id} \n Counts: {counts}",

            )

        except Exception as a:

            print(a)

@Client.on_message(

    filters.user(sudos) & filters.command(["gn", "gdnight"], prefixes=HANDLER)

)

async def gdnightcmd(Legend: Client, e: Message):

    usage = f"Command: {HANDLER}gn -u \nCommand:{HANDLER}gn -u (reply to anyone)\nCommand: {HANDLER}gn (count) \nCommand: {HANDLER}gn (count) (reply to anyone)"

    text = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)

    flag = text[0]

    if not flag:

        return await e.reply_text(usage)

    wishgdnight = "╭━━━╮╱╱╱╱╱╱╱╭╮\n┃╭━╮┃╱╱╱╱╱╱╱┃┃\n┃┃╱╰╋━━┳━━┳━╯┃\n┃┃╭━┫╭╮┃╭╮┃╭╮┃\n┃╰┻━┃╰╯┃╰╯┃╰╯┃\n╰━━━┻━━┻━━┻━━╯\n╭━╮╱╭╮╱╱╱╭╮╱╭╮\n┃┃╰╮┃┃╱╱╱┃┃╭╯╰╮\n┃╭╮╰╯┣┳━━┫╰┻╮╭╯\n┃┃╰╮┃┣┫╭╮┃╭╮┃┃\n┃┃╱┃┃┃┃╰╯┃┃┃┃╰╮\n╰╯╱╰━┻┻━╮┣╯╰┻━╯\n╱╱╱╱╱╱╭━╯┃\n╱╱╱╱╱╱╰━━╯"

    if "-u" in flag:

        global wish

        wish = True

        if e.reply_to_message:

            lmao = e.reply_to_message

            while wish == True:

                for i in range(1, 26):

                    lol = globals()[f"Client{i}"]

                    if lol is not None:

                        await lol.send_message(

                            e.chat.id, f"{lmao.from_user.mention}\n\n{wishgdnight}"

                        )

        else:

            while wish == True:

                for i in range(1, 26):

                    lol = globals()[f"Client{i}"]

                    if lol is not None:

                        await lol.send_message(e.chat.id, wishgdnight)

    elif "-u" not in flag:

        night_pic = "https://graph.org/file/f1c39dac664a45be949fd.jpg"

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

                            night_pic,

                            caption=f"{lmao.from_user.mention}\n\n{wishgdnight}",

                        )

        else:

            for _ in range(counts):

                for i in range(1, 26):

                    lol = globals()[f"Client{i}"]

                    if lol is not None:

                        await lol.send_photo(e.chat.id, night_pic, caption=wishgdnight)

    else:

        await e.reply_text(usage)

    if LOG_CHANNEL:

        try:

            await Legend.send_message(

                LOG_CHANNEL,

                f"#Started Good Nightl Spam By User: {e.from_user.id} \n\n Chat: {e.chat.id} \n Counts: {counts}",

            )

        except Exception as a:

            print(a)

@Client.on_message(

    filters.user(sudos) & filters.command(["stopwish"], prefixes=HANDLER)

)

async def stopwish(_, e: Message):

    global wish

    wish = False

    await e.reply_text("Stopped Unlimited Wish gdmrng")
