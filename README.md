# FastAPI MongoDB Merge Conflict Practice

A small FastAPI + MongoDB project designed for practicing Git merge conflicts.

## Project Profile

Service name: FastAPI Mongo Practice API
Primary database: merge_practice
Default collection: users
API prefix: /api/v1
Branch owner: main branch
Conflict note: Start from main, merge conflict-01 first, then merge another conflict branch.

## Run Locally

1. Create a virtual environment.
2. Install dependencies with `pip install -r requirements.txt`.
3. Set `MONGODB_URI` if your MongoDB server is not on localhost.
4. Start the API with `uvicorn app.main:app --reload`.

## Practice Flow

1. Checkout `main`.
2. Merge `conflict-01`.
3. Merge any other `conflict-*` branch.
4. Resolve conflicts in the five project files.
5. Commit the merge and repeat.
