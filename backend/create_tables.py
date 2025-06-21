import asyncio
from app.db import engine, Base  
from app.models import user, brand, campaign, influencer,collab_applications, collaboration, influencer_platform,influencer_service

async def create_all_tables():
    print("🧠 Tables SQLAlchemy knows about:", Base.metadata.tables.keys())
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    print("✅ All tables created successfully!")

if __name__ == "__main__":
    asyncio.run(create_all_tables())
