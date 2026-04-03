from fastapi import FastAPI
import random, time

app = FastAPI()

# Параметри адептів
adepts = [{"id": i, "V": random.uniform(0.05, 0.2), "E": 0.1, "S": 0.1, "T": 0.0} for i in range(300)]

# Формула оновлення станів
def update_states():
    for a in adepts:
        delta_V = a["V"] * (1 - a["S"])
        delta_E = a["E"] * random.uniform(0.9, 1.1)
        delta_S = a["S"] + random.uniform(-0.02, 0.05)
        delta_T = a["T"] + (a["S"] > 0.7) * 0.05
        a["V"], a["E"], a["S"], a["T"] = delta_V, delta_E, delta_S, delta_T
    return adepts

@app.get("/pulse")
def pulse():
    return {"timestamp": time.time(), "adepts": update_states()}
