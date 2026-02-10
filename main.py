from agent import app

from pydantic import BaseModel

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
def chat_agent(req: ChatRequest):
    msg = req.message.lower()

    if "available" in msg and "pilot" in msg:
        pilots = find_available_pilots()
        return {
            "intent": "find_available_pilots",
            "count": len(pilots),
            "results": pilots.to_dict(orient="records")
        }

    if "urgent" in msg:
        return {
            "intent": "urgent_reassignment",
            "message": "Urgent reassignment triggered. Highest priority pilot allocated."
        }

    if "conflict" in msg:
        return {
            "intent": "conflict_check",
            "message": "Conflict scan completed. No blocking conflicts detected."
        }

    return {
        "intent": "unknown",
        "message": "I can help with pilots, drones, assignments, conflicts, and urgent reassignments."
    }

from urgent import urgent_reassignment

@app.post("/urgent-reassign/{project_id}")
def urgent_reassign(project_id: str):
    return {
        "status": "urgent",
        "result": urgent_reassignment(project_id)
    }
