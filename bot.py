from core.client import client

import modules.pmpermit
import modules.approvals
import modules.trusted
import modules.antispam
import modules.antiflood

print("Secure Userbot Started")

client.start()
client.run_until_disconnected()
