import pandas as pd


def load_data():
    missions = pd.read_csv("data/missions.csv")
    pilots = pd.read_csv("data/pilot_roster.csv")
    drones = pd.read_csv("data/drone_fleet.csv")
    return missions, pilots, drones


def optimize_assignment(mission_id: str):
    missions, pilots, drones = load_data()

    mission = missions[missions["mission_id"] == mission_id]
    if mission.empty:
        return None, None, "Mission not found"

    # Simple optimization:
    # 1. Available pilot
    # 2. Available drone

    available_pilots = pilots[pilots["status"] == "available"]
    available_drones = drones[drones["status"] == "available"]

    if available_pilots.empty:
        return None, None, "No available pilots"

    if available_drones.empty:
        return None, None, "No available drones"

    pilot_id = available_pilots.iloc[0]["pilot_id"]
    drone_id = available_drones.iloc[0]["drone_id"]

    return pilot_id, drone_id, None
