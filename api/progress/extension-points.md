# Extension Points

- Routes: Add new route files in src/routes/ and export them in src/routes/index.js.
- Models: Define new entities in src/models/ using standard JS exports.
- Services: Implement business logic in src/services/ and import into routes.
- Async: No explicit pattern, create src/services/queue.js for async/background tasks.
