from fastapi import FastAPI
from pydantic import BaseModel
from textblob import TextBlob  # AI library import kari
import time

# 1. Sabse pehle app define karo (Taki NameError na aaye)
app = FastAPI(title="Tech Tadka Real AI Engine")

# 2. Data model define karo
class AIQuery(BaseModel):
    text: str

@app.get("/")
def home():
    return {"status": "Online", "message": "Utho Cloud Real AI is live! 🇮🇳"}

# 3. Aapka Real AI logic yahan hai
@app.post("/analyze")
async def analyze_sentiment(query: AIQuery):
    start_time = time.time()

    # REAL AI LOGIC: TextBlob jazbaat pehchanta hai
    analysis = TextBlob(query.text)

    # Polarity check: -1 (Negative) to +1 (Positive)
    if analysis.sentiment.polarity > 0:
        result = "Positive 😊"
    elif analysis.sentiment.polarity < 0:
        result = "Negative 😡"
    else:
        result = "Neutral 😐"

    latency = round((time.time() - start_time) * 1000, 2)

    return {
        "input_text": query.text,
        "sentiment": result,
        "score": analysis.sentiment.polarity,
        "latency": f"{latency}ms",
        "provider": "Utho Cloud (Real AI Engine) 🇮🇳"
    }
