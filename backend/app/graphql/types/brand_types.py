from typing import Optional
from app.graphql.types.user_types import UserInput
import strawberry

@strawberry.input 
class BrandDetailsInput:
     brand_name: str 
     brand_industry:str
     brand_type: str
     country: str
     segment: str
     created_by: Optional[str] = None  # UUID of the user creating the brand
     last_modified_by: Optional[str] = None  # UUID of the user modifying the brand  
     is_active: Optional[bool]  = True  # Default to True, can be set to False for deactivation

@strawberry.input
class BrandSignupInput: 
     user: UserInput
     brand: BrandDetailsInput

@strawberry.type
class BrandSignupResponse:
    user_id: str
    brand_id: str