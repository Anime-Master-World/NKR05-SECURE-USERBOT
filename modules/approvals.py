from telethon import events

from core.client import client


@client.on(events.NewMessage(
    outgoing=True,
    pattern=r"\.approve"
))
async def approve(event):

    if not event.is_reply:
        return

    reply = await event.get_reply_message()

    await approved.update_one(
        {"user_id": reply.sender_id},
        {"$set": {"user_id": reply.sender_id}},
        upsert=True
    )

    await event.reply("✅ Approved")


@client.on(events.NewMessage(
    outgoing=True,
    pattern=r"\.disapprove"
))
async def disapprove(event):

    if not event.is_reply:
        return

    reply = await event.get_reply_message()

    await approved.delete_one(
        {"user_id": reply.sender_id}
    )

    await event.reply("❌ Disapproved")
