import logging

from fastapi import APIRouter, Request, HTTPException, Depends
from fastapi.responses import JSONResponse, PlainTextResponse
from summarizer.services import SimpleSummarizer
router = APIRouter()

summarizer = SimpleSummarizer()

logging.basicConfig(level=logging.INFO, format="%(levelname)s: \t%(asctime)s - %(message)s")


@router.post("/summarize")
async def summarize(request: Request):
    """
    Endpoint so summarize input text.

    :param request: HTTP request object.
    :return: A JSON object containing the summary of the input text.
    :raises HTTPException: If the request failed.
    """
    try:
        data = await request.json()
        text = data.get("text", "")
        if not text:
            raise HTTPException(status_code=400, detail="Text is required for summarization.")

        summary = summarizer.summarize(text)
        if summary:
            logging.info("Summarization completed successfully")

        return JSONResponse(status_code=200, content={"summary": summary})

    except Exception as e:
        logging.error(f"Error during summarization: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
