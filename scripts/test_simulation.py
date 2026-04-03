import requests, time, csv

with open("logs/simulation.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Hour", "avg_V", "avg_E", "avg_S", "avg_T"])

    for hour in range(24):
        r = requests.get("http://127.0.0.1:8000/pulse").json()
        adepts = r["adepts"]
        avg_V = sum(a["V"] for a in adepts) / len(adepts)
        avg_E = sum(a["E"] for a in adepts) / len(adepts)
        avg_S = sum(a["S"] for a in adepts) / len(adepts)
        avg_T = sum(a["T"] for a in adepts) / len(adepts)
        print(f"Hour {hour}: V={avg_V:.3f}, E={avg_E:.3f}, S={avg_S:.3f}, T={avg_T:.3f}")
        writer.writerow([hour, avg_V, avg_E, avg_S, avg_T])
        time.sleep(1)  # для швидкого тесту
