# Architecture Summary (Corrected)

## 1. Environment
- Language/Runtime: JavaScript/Node.js.
- Dependencies: Managed via package.json.

## 2. Structure
- src/: Contains core JS logic (models, routes, services).
- tests/: Contains Node.js test suite.

## 3. Data Models (src/models/store.js)
- users, teams, invitations (In-memory JS arrays).

## 4. API Routes (src/routes/index.js)
- GET /health, GET /teams (Standard JS exports).

## 5. Correction Note
- Previous claims regarding Python/Alembic were hallucinations caused by root-level directory clutter.
