import strawberry
from app.services.user import brand_signup
from app.graphql.types.brand_types import BrandSignupInput, BrandSignupResponse

@strawberry.type
class BrandMutation:
    @strawberry.mutation
    async def signup_brand(self, input: BrandSignupInput) -> BrandSignupResponse:
        user_id, brand_id = await brand_signup(input)
        return BrandSignupResponse(user_id=str(user_id), brand_id=str(brand_id))