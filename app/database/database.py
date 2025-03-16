from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from config.config import settings
import models as models
import models.user

client = None


async def initiate_database():
    global client
    client = AsyncIOMotorClient(settings.DATABASE_URL)
    await init_beanie(
        database=client.get_database(settings.MONGO_INITDB_DATABASE),
        document_models=models.__all__,
    )


async def close_database():
    if client:
        client.close()
