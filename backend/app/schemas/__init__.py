from .user import BrandMutation, InfluencerMutation
import strawberry

@strawberry.type
class Mutation(BrandMutation,InfluencerMutation):
    pass

@strawberry.type
class Query: 
    @strawberry.field
    def hello(self) -> str:
        return "Hello From BrandCollab backend"