const express = require('express');
const router = express.Router();
const store = require('../models/store');
const uuidv4 = () => Math.random().toString(36).substring(7);

router.post('/invitations', (req, res) => {
  const { teamId, email } = req.body;
  
  if (!teamId || !email) {
    return res.status(400).json({ 
      error: { code: "VALIDATION_ERROR", message: "teamId and email are required" } 
    });
  }

  const newInvitation = { id: uuidv4(), teamId, email, status: 'pending' };
  store.invitations.push(newInvitation);
  
  res.status(201).json(newInvitation);
});

module.exports = router;
