# Task Tree: Team Collaboration

## Tasks
1. [ ] **Task 1: Data Model Updates** (Update store.js to hold teams, users, and members)
2. [ ] **Task 2: POST /teams** (Create a team)
3. [ ] **Task 3: GET /teams** (List teams)
4. [ ] **Task 4: POST /teams/:id/members** (Add a member)
5. [ ] **Task 5: GET /teams/:id** (Get specific team details)
6. [ ] **Task 6: DELETE /teams/:id** (Remove team)
7. [ ] **Task 7: POST /teams/:id/invitations** (Send invite)
8. [ ] **Task 8: GET /teams/:id/invitations** (List invites)

## Critical Path
Task 1 -> Task 2 -> Task 4 -> Task 7.

## Riskiest Task
Task 7 (Invitations): Complex state management and potential for invalid state if user ID/team ID doesn't exist.
