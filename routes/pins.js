const router = require('express').Router();
const Pin = require('../models/Pin')


//Create a new Pin
router.post("/",async (req, res) => {
    const newPin = new Pin(req.body);
    try{
        const savedPin = await newPin.save();
        // status 200 is success and returns json of saved pin
        res.status(200).json(savedPin);
    }catch(err){
        res.status(500).json(err);
    }
})


//Get all Pins