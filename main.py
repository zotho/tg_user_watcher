from datetime import datetime

from telethon import TelegramClient, events
from telethon.tl.types import PeerChannel

from config import api_id, api_hash, watch_on_user, forward_to_chat


with TelegramClient("tg_user_watcher", api_id, api_hash) as client:

    @client.on(events.NewMessage(incoming=True, from_users=watch_on_user))
    async def handler(event):
        print(datetime.now().astimezone().isoformat())
        await event.message.forward_to(PeerChannel(forward_to_chat))

    client.run_until_disconnected()
