from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import heapq

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

crop_data = {
    "Rice": {"temp": "25-35°C", "humidity": "60-80%", "duration": "3-6 months"},
    "Wheat": {"temp": "15-25°C", "humidity": "40-60%", "duration": "4-5 months"},
    "Maize": {"temp": "20-30°C", "humidity": "50-70%", "duration": "3 months"}
}

@app.get("/")
def home():
    return {"message": "Backend running"}

@app.post("/predict")
def predict(data: dict):

    heap = []

    for crop in crop_data:
        heapq.heappush(heap, (0, crop))

    top_crops = [heapq.heappop(heap)[1] for _ in range(3)]

    return {
        "crop": top_crops[0],
        "top_crops": top_crops,
        "duration": crop_data[top_crops[0]]["duration"],
        "current_temp": 30,
        "current_humidity": 60,
        "recommended_temp": crop_data[top_crops[0]]["temp"],
        "recommended_humidity": crop_data[top_crops[0]]["humidity"],
        "fertilizers": [{"name": "Urea", "desc": "Growth"}],
        "advice": "Good conditions"
    }