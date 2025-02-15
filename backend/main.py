# main.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import firebase_config
from firebase_admin import db
from datetime import datetime

# FastAPI-App erstellen
app = FastAPI(title="Top Trading Setups API", version="1.0")

### 1. Datenmodell für Setups
class Setup(BaseModel):
    symbol: str
    score: float
    indicators: dict
    sentiment: dict
    setupType: str

### 2. Endpoint: Tägliche Setups abrufen
@app.get("/api/setups/daily")
def get_daily_setups():
    ref = db.reference('setups/daily')
    setups = ref.get()
    if not setups:
        raise HTTPException(status_code=404, detail="Keine Setups gefunden.")
    return setups

### 3. Endpoint: Neues Setup speichern
@app.post("/api/setups")
def create_setup(setup: Setup):
    timestamp = datetime.utcnow().isoformat()
    setup_data = setup.dict()
    setup_data["createdAt"] = timestamp
    
    ref = db.reference(f'setups/daily/{setup.symbol}')
    ref.set(setup_data)
    
    return {"message": f"Setup für {setup.symbol} erfolgreich gespeichert!"}

### 4. Health-Check Endpoint
@app.get("/api/health")
def health_check():
    return {"status": "OK", "message": "API läuft einwandfrei"}

