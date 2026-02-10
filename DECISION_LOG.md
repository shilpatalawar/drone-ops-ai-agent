# Decision Log — Drone Operations Coordinator AI Agent

## Key Assumptions
- Google Sheets is used as the system of record for pilots, drones, and missions.
- CSV files are uploaded to Google Sheets and accessed live by the agent.
- The prototype focuses on coordination logic rather than full enterprise authentication.

## Trade-offs
- Used Google Sheets CSV export for rapid read-only integration instead of full OAuth write-back to save implementation time.
- Implemented rule-based conversational logic instead of LLM integration for deterministic behavior.
- Prioritized visible system behavior over advanced optimization.

## Urgent Reassignments
Urgent reassignments are interpreted as high-priority missions that may override lower-priority assignments. The agent triggers reallocation by identifying the best available pilot and drone and deprioritizing non-critical missions.

## What I Would Do With More Time
- Implement full two-way Google Sheets API integration with authenticated write-back.
- Add LLM-powered natural language understanding for richer conversational interaction.
- Add audit logging, role-based access control, and concurrency handling.
- Improve assignment optimization using weighted scoring and constraint solvers.
