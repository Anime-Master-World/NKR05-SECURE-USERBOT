from telethon import events

from core.client import client
from core.database import approved, warnings
from config import OWNER_ID

PM_WARN_LIMIT = 3


@client.on(events.NewMessage(incoming=True))
async def pmpermit(event):

    if not event.is_private:
        return

    uid = event.sender_id

    if uid == OWNER_ID:
        return

    if await approved.find_one({"user_id": uid}):
        return

    data = await warnings.find_one({"user_id": uid})

    count = data["count"] if data else 0
    count += 1

    await warnings.update_one(
        {"user_id": uid},
        {"$set": {"count": count}},
        upsert=True
    )

    if count == 1:
        await event.reply(
            "⚠️ PM Permit Enabled.\n"
            "Please wait until you are approved."
        )

    elif count >= PM_WARN_LIMIT:
        await client(functions.contacts.BlockRequest(uid))
