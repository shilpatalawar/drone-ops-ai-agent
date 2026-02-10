from fastapi import FastAPI, HTTPException
from models import AssignmentRequest, AssignmentResponse
from data_loader import load_pilots, load_drones, load_missions
from conflict import check_conflicts
from urgent import urgent_reassignment
from db import save_assignment
import logging

app = FastAPI(title="Drone Ops AI Agent")

# ---------------- LOGGING SETUP ----------------
logging.basicConfig(
    filename="logs/assignments.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

# ---------------- BASIC HEALTH ----------------
@app.get("/")
def home():
    return {"status": "Drone Ops AI Agent running"}

# ---------------- PILOT QUERY ----------------
@app.get("/pilots")
def get_pilots(skill: str = None, location: str = None):
    pilots = load_pilots()
    result = pilots[pilots["status"] == "Available"]

    if skill:
        result = result[result["skills"].str.contains(skill, na=False)]

    if location:
        result = result[result["location"] == location]

    return result.to_dict(orient="records")

# ---------------- DRONE QUERY ----------------
@app.get("/drones")
def get_drones(capability: str = None, location: str = None):
    drones = load_drones()
    result = drones[drones["status"] == "Available"]

    if capability:
        result = result[result["capabilities"].str.contains(capability, na=False)]

    if location:
        result = result[result["location"] == location]

    return result.to_dict(orient="records")

# ---------------- ASSIGN WITH JSON BODY ----------------
@app.post("/assign", response_model=AssignmentResponse)
def assign_mission_api(req: AssignmentRequest):
    missions = load_missions()
    pilots = load_pilots()
    drones = load_drones()

    mission_df = missions[missions["project_id"] == req.project_id]

    if mission_df.empty:
        raise HTTPException(status_code=404, detail="Mission not found")

    mission = mission_df.iloc[0]

    available_pilots = pilots[pilots["status"] == "Available"]
    available_drones = drones[drones["status"] == "Available"]

    if req.location:
        available_pilots = available_pilots[available_pilots["location"] == req.location]
        available_drones = available_drones[available_drones["location"] == req.location]

    if req.skill:
        available_pilots = available_pilots[
            available_pilots["skills"].str.contains(req.skill, na=False)
        ]

    if req.capability:
        available_drones = available_drones[
            available_drones["capabilities"].str.contains(req.capability, na=False)
        ]

    if available_pilots.empty or available_drones.empty:
        if str(mission["priority"]).lower() == "urgent":
            return urgent_reassignment(mission, pilots, missions)
        raise HTTPException(status_code=400, detail="No available pilot or drone")

    pilot = available_pilots.iloc[0]
    drone = available_drones.iloc[0]

    issues = check_conflicts(mission, pilot, drone, missions)

    if issues:
        return AssignmentResponse(
            status="Conflict detected",
            pilot_id=None,
            drone_id=None,
            issues=issues
        )

    # --------- SAVE TO DB ---------
    save_assignment(req.project_id, pilot["pilot_id"], drone["drone_id"])

    # --------- LOGGING ---------
    logging.info(f"Assigned {req.project_id} -> Pilot {pilot['pilot_id']} Drone {drone['drone_id']}")

    return AssignmentResponse(
        status="Assignment feasible",
        pilot_id=pilot["pilot_id"],
        drone_id=drone["drone_id"],
        issues=[]
    )
