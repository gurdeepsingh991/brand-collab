from app.models.user import User
from app.models.brand import BrandProfile
from app.db import get_session

from sqlalchemy.exc import IntegrityError
from datetime import datetime  

from app.graphql.types.influencer_types import InfluencerSignupInput, InfluencerSignupResponse
from app.models.influencer import InfluencerProfile
from app.models.influencer_platform import InfluencerPlatform
from app.models.influencer_service import InfluencerService

async def brand_signup(input):
    async with get_session() as session:
        new_user = User(
            email = input.user.email,
            first_name =  input.user.first_name,
            middle_name = input.user.middle_name,
            last_name = input.user.last_name,
            role = "user",
            user_type = "brand",
            is_active = True,
            created_on = datetime.utcnow()
        )

        session.add(new_user)
        await session.flush()

        new_brand = BrandProfile(
            brand_name=input.brand.brand_name,
            brand_industry=input.brand.brand_industry,
            brand_type=input.brand.brand_type,
            country=input.brand.country,
            segment=input.brand.segment,
            created_by=str(new_user.user_id),
            last_modified_by = str(new_user.user_id),
            is_active = True
        )
        session.add(new_brand)
        await session.flush()
        try:
            await session.commit()
        except IntegrityError:
            await session.rollback()
            raise Exception("User already exists")

        return new_user.user_id, new_brand.brand_id
     
async def influencer_signup(input:InfluencerSignupInput):
    async with get_session() as session:
        new_user = User(
            email = input.user.email,
            first_name =  input.user.first_name,
            middle_name = input.user.middle_name,
            last_name = input.user.last_name,
            role = "user",
            user_type = "influencer",
            is_active = True,
            created_on = datetime.utcnow()
        )
        session.add(new_user)
        await session.flush()

        new_influencer = InfluencerProfile(
             user_id = str(new_user.user_id),
             city = input.influencer.city,
             country = input.influencer.country,
             is_active = True
        )
        session.add(new_influencer)
        await session.flush()
        
        for service in input.services:
            new_service = InfluencerService(
                influencer_id = str(new_influencer.influencer_id),
                service_type = service.service_type,
                charges_per_hour = service.charges_per_hour,
                currency = service.currency,
                is_active = True
            )
            session.add(new_service)
        for platform in input.platforms:
            new_platform = InfluencerPlatform(
                influencer_id = str(new_influencer.influencer_id),
                platform_name = platform.platform_name,  # e.g. Instagram, TikTok
                no_of_followers = platform.no_of_followers,
                no_of_subscribers = platform.no_of_subscribers,
                engagement_rate = platform.engagement_rate,
                is_primary = platform.is_primary,
                is_active = True
            )
            session.add(new_platform)

        try: 
            await session.commit()
        except IntegrityError: 
            await session.rollback()
            raise Exception("User already exists or constraint violated")
        return True
