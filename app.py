from flask import Flask, render_template
import random
from datetime import datetime, timedelta

app = Flask(__name__)

# Mock earthquake data generator
def generate_earthquake_data():
    locations = ["San Andreas Fault", "Ring of Fire", "Himalayan Belt", 
                "New Madrid Zone", "Japan Trench", "Sumatra Subduction"]
    magnitudes = [round(random.uniform(3.0, 7.0), 1]
    
    predictions = []
    for i in range(5):
        days_ahead = random.randint(1, 30)
        pred_date = datetime.now() + timedelta(days=days_ahead)
        predictions.append({
            "location": random.choice(locations),
            "magnitude": round(random.uniform(3.0, 7.0), 1),
            "date": pred_date.strftime("%Y-%m-%d"),
            "confidence": f"{random.randint(50, 85)}%"
        })
    
    return predictions

@app.route('/')
def home():
    earthquakes = generate_earthquake_data()
    return render_template('index.html', earthquakes=earthquakes)

if __name__ == '__main__':
    app.run(debug=True)