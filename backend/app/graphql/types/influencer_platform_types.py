import strawberry

@strawberry.input
class InfluencerPlatformInput:
    platform_name:str # e.g. Instagram, TikTok
    no_of_followers:int
    no_of_subscribers:int
    engagement_rate: float
    is_primary:bool