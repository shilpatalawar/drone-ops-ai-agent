from datetime import datetime

def dates_overlap(s1, e1, s2, e2):
    s1 = datetime.fromisoformat(str(s1))
    e1 = datetime.fromisoformat(str(e1))
    s2 = datetime.fromisoformat(str(s2))
    e2 = datetime.fromisoformat(str(e2))
    return s1 <= e2 and s2 <= e1


def check_conflicts(mission, pilot, drone, all_missions):
    issues = []

    # Certification mismatch
    if str(mission["required_certs"]) not in str(pilot["certifications"]):
        issues.append("Pilot lacks required certification")

    # Drone maintenance
    if str(drone["status"]).lower() == "maintenance":
        issues.append("Drone is in maintenance")

    # Location mismatch
    if pilot["location"] != mission["location"]:
        issues.append("Pilot location mismatch")

    if drone["location"] != mission["location"]:
        issues.append("Drone location mismatch")

    return issues
