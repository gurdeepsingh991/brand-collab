import strawberry 
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from dotenv import load_dotenv
from app.schemas import Mutation,Query
import os

load_dotenv()
print("DB URL:", os.getenv("DATABASE_URL"))

 
@strawberry.type
class Query: 
    @strawberry.field
    def hello(self) -> str:
        return "Hello From BrandCollab backend"
    
#schema = strawberry.Schema(query=Query)

schema = strawberry.Schema(query=Query,mutation=Mutation)
graphql_app = GraphQLRouter(schema)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")
