import uvicorn
from fastapi import FastAPI
from image_server.api.products import router

app = FastAPI(title="image server API")
app.include_router(router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, loop="asyncio")
