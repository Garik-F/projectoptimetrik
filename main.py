from fastapi import FastAPI
import uvicorn
from .api.user_router import router as user_router

app = FastAPI()
app.include_router(user_router,tags=["users"],prefix="/user")


if __name__ == "__main__":
    uvicorn.run("main:app",host="localhost",port=8080,log_level="info")

