from fastapi import FastAPI
from pydantic import BaseModel
import time

app = FastAPI(title="Tech Tadka AI on Utho Cloud")

class AIQuery(BaseModel):
    text: str

@app.get("/")
def read_root():
    return {"status": "Online", "message": "Utho Cloud AI Engine is running! 🇮🇳"}

@app.post("/analyze")
async def analyze_sentiment(query: AIQuery):
    start_time = time.time()
    
    # Simple Logic for Demo: Even length = Positive, Odd = Neutral
    result = "Positive" if len(query.text) % 2 == 0 else "Neutral"
    
    latency = round((time.time() - start_time) * 1000, 2)
    
    return {
        "input_text": query.text,
        "sentiment": result,
        "latency": f"{latency}ms",
        "provider": "Utho Cloud (Desh Ka Cloud) 🇮🇳"
    }