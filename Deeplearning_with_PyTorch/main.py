from test import predict

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import asyncio
import uvicorn

app = FastAPI(title="Clothing classifier API")

class PredictRequest(BaseModel):
    url: str

@app.post('/predict')
async def predict_endpoint(payload: PredictRequest):
    """Accepts JSON payload: {"url": "http..."} and returns predictions as JSON.

    Using a Pydantic model so you can paste the URL in the docs UI.
    """
    url = payload.url

    if not url:
        return JSONResponse({'error': 'missing `url` in request'}, status_code=400)

    # call the synchronous predict function in a thread to avoid blocking the event loop
    try:
        predictions = await asyncio.to_thread(predict, url)
    except Exception as exc:
        return JSONResponse({'error': str(exc)}, status_code=500)

    return JSONResponse(predictions)


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True)