from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import translate

app = FastAPI()

# Add cors
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(translate.router)


@app.get("/")
def root():
    return {"message": "Hello World"}
