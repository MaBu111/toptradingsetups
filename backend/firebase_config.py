# firebase_config.py

import firebase_admin
from firebase_admin import credentials, db

# Service-Account-Schlüssel aus Firebase
cred = credentials.Certificate("firebase-adminsdk.json")

# Realtime Database URL (aus Firebase-Konsole)
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://toptradingsetups.firebaseio.com'
})

print("Firebase erfolgreich verbunden!")
