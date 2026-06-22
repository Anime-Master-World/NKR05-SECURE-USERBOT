from telethon import events

from core.client import client
from core.database import trusted


@client.on(events.NewMessage(
    outgoing=True,
    pattern=r"\.trust"
))
async def trust_user(event):

    if not event.is_reply:
        return

    reply = await event.get_reply_message()

    await trusted.update_one(
        {"user_id": reply.sender_id},
        {"$set": {"user_id": reply.sender_id}},
        upsert=True
    )

    await event.reply("✅ Trusted")


@client.on(events.NewMessage(
    outgoing=True,
    pattern=r"\.untrust"
))
async def untrust_user(event):

    if not event.is_reply:
        return

    reply = await event.get_reply_message()

    await trusted.delete_one(
        {"user_id": reply.sender_id}
    )

    await event.reply("❌ Untrusted")
