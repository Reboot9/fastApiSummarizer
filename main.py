import logging

import uvicorn
from fastapi import FastAPI
from summarizer.endpoints import router

app = FastAPI()
app.include_router(router)

logging.basicConfig(level=logging.INFO, format="%(levelname)s: \t%(asctime)s - %(message)s")
logger = logging.getLogger(__name__)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
