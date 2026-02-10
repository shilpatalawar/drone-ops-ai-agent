# 🚁 Drone Operations Coordinator AI Agent

## Overview

This project implements an AI-powered backend agent for coordinating drone operations, including pilot assignment, drone inventory management, conflict detection, and urgent reassignment handling.

The system simulates real-world drone operations coordination and is designed to reduce manual coordination effort by automating decision-making based on availability, skills, location, and mission priority.

---

## Key Features

- Pilot roster querying by skill and location
- Drone fleet querying by capability and location
- Mission assignment with JSON-based API
- Conflict detection (double booking, skill mismatch, maintenance issues)
- Urgent reassignment handling for high-priority missions
- Assignment logging for audit and traceability
- SQLite database for assignment history
- Interactive Swagger UI for testing

---

## Tech Stack

- Python 3.10+
- FastAPI
- Pydantic
- Pandas
- SQLite
- Uvicorn

---

## How to Run

1. Activate virtual environment:venv\Scripts\activate

2. Install dependencies:pip install -r requirements.txt

3. Start server:uvicorn main:app --reload

---

## API Testing

Open in browser:

http://127.0.0.1:8000/docs

Use POST /assign to assign pilots and drones to missions.

---

## Author

Developed as part of a technical assignment to demonstrate AI-driven drone operations coordination.

