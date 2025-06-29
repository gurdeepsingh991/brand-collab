from typing import List
import strawberry

from app.graphql.types.influencer_platform_types import InfluencerPlatformInput
from app.graphql.types.influencer_service_types import InfluencerServiceInput
from app.graphql.types.user_types import UserInput
@strawberry.input
class InfluencerInput: 
    city:str
    country:str

@strawberry.input
class InfluencerSignupInput: 
   user: UserInput
   influencer: InfluencerInput
   platforms: List[InfluencerPlatformInput]
   services: List[InfluencerServiceInput]

@strawberry.type
class InfluencerSignupResponse: 
    success:bool


