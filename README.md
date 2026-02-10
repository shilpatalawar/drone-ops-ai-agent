# Drone Ops AI Agent

## Overview
This project is an AI-powered operations agent for assigning pilots and drones to missions based on availability, location, priority, and conflict rules.

It exposes a FastAPI backend to allow conversational and API-based interaction for mission assignment and resource management.

## Architecture
- FastAPI – API Layer
- Pandas – CSV data loading
- SQLite – Assignment logging
- Rule-based optimization logic
- Modular components for conflicts and urgent reassignment

## Project Structure

agent.py        - Core assignment logic  
main.py         - FastAPI app  
data_loader.py  - CSV data loaders  
conflict.py     - Conflict detection  
urgent.py       - Urgent reassignment logic  
optimizer.py    - Optimization logic  
db.py            - SQLite logging  
models.py        - Pydantic models  
*.csv            - Pilot, drone, mission data  

## How to Run Locally

```bash
pip install -r requirements.txt
uvicorn main:app --reload


---

## API Testing

Open in browser:
http://127.0.0.1:8000/docs


Use POST /assign to assign pilots and drones to missions.

---

## Author

Developed as part of a technical assignment to demonstrate AI-driven drone operations coordination.






## Architecture Overview

This system is built using FastAPI and deployed on Render. Google Sheets is used as the external data source for pilots, drones, and missions.

### Components
- FastAPI backend for APIs and conversational interface
- Google Sheets for live pilot, drone, and mission data
- Agent logic for assignment, conflict detection, and urgent handling

### Data Flow
User → FastAPI API → Google Sheets (Read) → Agent Logic → Response

### Conversational Interface
Users can interact with the system using the `/chat` endpoint with natural language-style commands such as:
- "Show available pilots"
- "Trigger urgent reassignment"
- "Check conflicts"
