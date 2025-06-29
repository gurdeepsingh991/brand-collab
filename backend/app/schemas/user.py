import strawberry
from app.services.user import brand_signup, influencer_signup
from app.graphql.types.brand_types import BrandSignupInput, BrandSignupResponse
from app.graphql.types.influencer_types import InfluencerSignupResponse, InfluencerSignupInput

@strawberry.type
class BrandMutation:
    @strawberry.mutation
    async def signup_brand(self, input: BrandSignupInput) -> BrandSignupResponse:
        user_id, brand_id = await brand_signup(input)
        return BrandSignupResponse(user_id=str(user_id), brand_id=str(brand_id))
    

@strawberry.type
class InfluencerMutation:
    @strawberry.mutation
    async def signup_influencer(self, input:InfluencerSignupInput) -> InfluencerSignupResponse:
        is_success = await influencer_signup(input)
        return InfluencerSignupResponse(success=is_success)