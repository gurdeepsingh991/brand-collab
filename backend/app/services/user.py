from app.models.user import User
from app.models.brand import BrandProfile
from app.db import get_session

from sqlalchemy.exc import IntegrityError
from datetime import datetime

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
     