# Delegation Strategy: Hybrid Approach

**Decision:** I will utilize a **Hybrid** delegation strategy.

**Reasoning:** 
1. **Autopilot for Isolated Tasks:** I will use "Full Autopilot" for standard boilerplate generation where assumptions are low-risk (e.g., creating basic DTOs, standard CRUD interfaces, or data models). This maximizes speed without compromising quality.
2. **Task-by-Task for Complex Integration:** I will switch to "Task-by-Task" for complex logic, such as implementing Role-Based Access Control (RBAC) or audit logging triggers. These areas require strict oversight because bad assumptions here cascade into security vulnerabilities.
3. **Architectural Oversight:** By alternating between these modes, I maintain control over the "20%" of the work that defines the feature's reliability, while letting the AI handle the "80%" of the work that is straightforward but tedious.
