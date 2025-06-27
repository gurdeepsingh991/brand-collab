from typing import Optional
import strawberry

@strawberry.input
class UserInput:
    email: str
    first_name: str
    last_name: str
    middle_name: Optional[str]  = None
    role: Optional[str] = None  # e.g.  admin, user
    user_type: Optional[str] = None  # e.g. brand, influencer, admin
    is_active: Optional[bool] = True


