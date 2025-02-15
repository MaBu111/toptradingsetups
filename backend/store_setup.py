# store_setup.py
import firebase_config
from firebase_admin import db
from datetime import datetime

def store_trading_setup(symbol, score, indicators, sentiment, setup_type):
    timestamp = datetime.utcnow().isoformat()
    setup_data = {
        "symbol": symbol,
        "score": score,
        "indicators": indicators,
        "sentiment": sentiment,
        "setupType": setup_type,
        "createdAt": timestamp
    }
    ref = db.reference(f'setups/daily/{symbol}')
    ref.set(setup_data)
    print(f"🚀 Setup für {symbol} gespeichert!")

# Beispiel-Daten
example_indicators = {
    "rsi": 32.5,
    "macd": {"signal": "Buy", "histogram": 0.03},
    "bollinger": {"position": "Upper Band", "volatility": 2.5}
}
example_sentiment = {"socialMedia": "Positive", "news": "Neutral"}

# Setup speichern
store_trading_setup(
    symbol="AAPL",
    score=92,
    indicators=example_indicators,
    sentiment=example_sentiment,
    setup_type="RSI Rebound"
)
