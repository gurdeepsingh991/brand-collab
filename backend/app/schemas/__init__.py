from .user import BrandMutation
import strawberry

@strawberry.type
class Mutation(BrandMutation):
    pass
@strawberry.type
class Query: 
    @strawberry.field
    def hello(self) -> str:
        return "Hello From BrandCollab backend"