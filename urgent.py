def urgent_reassignment(mission, pilots, missions):
    available = pilots[pilots["status"] == "Available"]

    if not available.empty:
        return {
            "strategy": "Assign available pilot",
            "pilot_id": available.iloc[0]["pilot_id"],
            "risk": "Low"
        }

    low_priority = missions[missions["priority"].str.lower() == "low"]

    if not low_priority.empty:
        return {
            "strategy": "Reassign from low priority project",
            "from_project": low_priority.iloc[0]["project_id"],
            "risk": "May delay low priority mission"
        }

    return {
        "strategy": "Escalate to operations manager",
        "risk": "No feasible reassignment"
    }
