### Prompt 1 (Task 1: Data Models)
"Update 'src/models/store.js' to include new empty arrays: 'teams', 'users', and 'invitations'. 
Each 'team' should have: id (UUID), name (string), members (array of user IDs).
Each 'user' should have: id (UUID), name (string).
Each 'invitation' should have: id (UUID), teamId (UUID), email (string), status (string: 'pending', 'accepted').
Do not add any logic, only export these structures."

### Prompt 2 (Task 2: POST /teams)
"Implement a route 'POST /teams' in 'src/routes/index.js'.
The route should:
1. Receive 'name' in the request body.
2. Generate a new UUID for the team.
3. Save the team to the 'teams' array in 'src/models/store.js'.
4. Return 201 status with the new team object.
Input context: 'src/routes/index.js' and 'src/models/store.js'."

### Prompt 3 (Task 3: POST /teams/:id/members)
"Implement a route 'POST /teams/:id/members' in 'src/routes/index.js'.
The route should:
1. Validate that the team exists.
2. Receive 'userId' in the request body.
3. Add 'userId' to the team's 'members' array in 'src/models/store.js'.
4. Return 200 status with the updated team object.
Input context: 'src/routes/index.js' and 'src/models/store.js'."
