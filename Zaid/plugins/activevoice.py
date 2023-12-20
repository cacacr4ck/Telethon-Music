import os

from telethon import Button, events
from Zaid import Zaid
from Zaid.helpers.queues import get_active_chats


@Zaid.on(events.NewMessage(pattern="^/activevoice"))
async def activevc(message):
    mystic = await message.reply(
        "Mengambil data bot stream..."
    )
    served_chats = await get_active_chats()
    text = ""
    j = 0
    for x in served_chats:
        try:
            title = (await message.client.get_entity(x)).title
        except Exception:
            title = "Private Group"
        if (await message.client.get_entity(x)).username:
            user = (await message.client.get_entity(x)).username
            text += f"{j + 1}.  [{title}](https://t.me/{user})[`{x}`]\n"
        else:
            text += f"{j + 1}. {title} [`{x}`]\n"
        j += 1
    if not text:
        await mystic.edit("bot sedang tidak dimana-mana")
    else:
        await mystic.edit(
            f"**Bot active di :-**\n\n{text}"
        )
