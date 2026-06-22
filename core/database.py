from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_URI

mongo = AsyncIOMotorClient(MONGO_URI)

db = mongo["secure_userbot"]

approved = db["approved_users"]
trusted = db["trusted_users"]
blocked = db["blocked_users"]
warnings = db["warnings"]
settings = db["settings"]
logs = db["logs"]
