const express = require('express');
const router = express.Router();
const store = require('../models/store');

router.get('/teams/:teamId/members', (req, res) => {
  const team = store.teams.find(t => t.id === req.params.teamId);
  if (!team) {
    return res.status(404).json({ 
      error: { code: "RESOURCE_NOT_FOUND", message: "Team not found" } 
    });
  }
  res.json(team.members || []);
});

module.exports = router;
