from fastapi import FastAPI
from . import models
from .database import engine, Base
from .routers import post, user, auth
from fastapi.middleware.cors import CORSMiddleware

# models.Base.metadata.create_all(bind=engine)

app = FastAPI()
origins = ['*']
app.add_middleware(CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'])

app.include_router(post.router)

app.include_router(user.router)

app.include_router(auth.router)


# def find_post(id):
#     for p in my_posts:
#         if p["id"] == id:
#             return {f"here is your post {p}"}
# def find_index(id):
#     for i, p in enumerate(my_posts):
#         if p['id'] == id:
#             return i
# @app.get("/")
# async def root():
#     return{"data":my_posts}


