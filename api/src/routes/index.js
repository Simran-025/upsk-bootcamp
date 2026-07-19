const express = require('express');
const router = express.Router();
const uuidv4 = () => Math.random().toString(36).substring(7); // Simplified ID generator
const store = require('../models/store');

router.use(express.json());

router.post('/teams', (req, res) => {
  const { name } = req.body;
  if (!name) return res.status(400).json({ error: "Name is required" });
  
  const newTeam = {
    id: uuidv4(),
    name: name,
    members: [] // Explicitly matching the store contract
  };
  
  store.teams.push(newTeam);
  res.status(201).json(newTeam);
});

module.exports = router;
