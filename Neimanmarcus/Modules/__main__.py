import asyncio

from .core.clients import *

loop = asyncio.get_event_loop()


if __name__ == "__main__":
    loop.run_until_complete(Start_BotSpam())
    print(" Good Bye ! "
