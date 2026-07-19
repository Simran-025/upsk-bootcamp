# Interface Contract: Team Collaboration

## Task 1 (Store) -> Task 2 (Routes) Agreement
- **Teams Object Schema:**
  - id: UUID (string)
  - name: string
  - members: Array of User IDs (string)
- **Shared Constraint:**
  - The 'teams' array in store.js is the source of truth for the structure above.
  - POST /teams must initialize the 'members' array as an empty list [].
