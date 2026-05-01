# FastAPI MongoDB Merge Conflict Practice

A small FastAPI + MongoDB project designed for practicing Git merge conflicts.

## Project Profile

Service name: FastAPI Mongo Branch 06 API
Primary database: merge_practice_branch_06
Default collection: users_branch_06
API prefix: /api/branch-06
Branch owner: conflict-06
Conflict note: This branch intentionally changes the same project settings as the other branches.

## Run Locally

1. Create a virtual environment for branch conflict-06.
2. Install dependencies with `pip install -r requirements.txt`.
3. Set `MONGODB_URI` before running the branch-06 API.
4. Start the API with `uvicorn app.main:app --reload --port 8006`.

## Practice Flow

1. Checkout `main`.
2. Merge `conflict-01`.
3. Merge `conflict-06` or another branch.
4. Resolve conflicts in the five project files.
5. Commit the merge and compare your resolved behavior.
