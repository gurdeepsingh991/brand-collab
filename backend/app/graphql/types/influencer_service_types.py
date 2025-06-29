import strawberry

@strawberry.input
class InfluencerServiceInput: 
    service_type:str  # e.g. product_review, mention
    charges_per_hour:float
    currency: str