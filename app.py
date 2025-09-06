from fastapi import FastAPI
import uvicorn
import sys
import os
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from fastapi.responses import Response
import subprocess
from src.textSummarizer.pipeline.prediction import PredictionPipeline


text:str = "What is Text Summarization?"

app = FastAPI()

@app.get("/", tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")



@app.get("/train")
async def training():
    try:
        # Run training and capture output
        result = subprocess.run(
            ["python3", "main.py"],
            capture_output=True,  # captures stdout/stderr
            text=True             # returns strings instead of bytes
        )

        # Check if training succeeded
        if result.returncode == 0:
            return Response("Training completed successfully !!")
        else:
            # Return stderr if there was an error
            return Response(f"Training failed!\nError:\n{result.stderr}")

    except Exception as e:
        return Response(f"Unexpected error occurred: {e}")
    



@app.post("/predict")
async def predict_route(text):
    try:

        obj = PredictionPipeline()
        text = obj.predict(text)
        return text
    except Exception as e:
        raise e
    

if __name__=="__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)