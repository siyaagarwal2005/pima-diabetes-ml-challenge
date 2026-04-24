import json
import sys
from datetime import datetime

def update(team_name, score):
    try:
        with open('leaderboard.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []

    # Update team score or add new entry
    new_entry = {
        "team": team_name,
        "score": round(float(score), 4),
        "time": datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    data.append(new_entry)
    
    # Sort: highest score first
    data = sorted(data, key=lambda x: x['score'], reverse=True)
    
    with open('leaderboard.json', 'w') as f:
        json.dump(data, f, indent=4)

if __name__ == "__main__":
    update(sys.argv[1], sys.argv[2])