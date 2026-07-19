# System Context: Project Management API

## Architecture
- Framework: Express.js
- Data Source: 'src/models/store.js' (In-memory object store)
- Routes: Located in 'src/routes/', registered in 'src/app.js'
- Middleware: Standard Express middleware, including express.json()

## Coding Conventions
- Naming: camelCase for variables and functions.
- Error Handling: All errors must be JSON objects with an 'error' key.
  Example: { "error": { "code": "...", "message": "..." } }
- Status Codes: 
  - 400: VALIDATION_ERROR
  - 404: RESOURCE_NOT_FOUND
  - 500: INTERNAL_ERROR

## Constraints
- No new npm dependencies without explicit justification.
- Must use existing 'store.js' for all data operations.
- New files must match the existing project structure.
