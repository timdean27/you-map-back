const express = require('express');
const app = express();
app.use(express.json())


const dotenv = require('dotenv')
dotenv.config();
const mongoose = require('mongoose');





mongoose.connect(process.env.MONGODB_URL, {useNewUrlParser: true}).then(() => {
    console.log('Mongo DB connected')
}).catch((err) => {
    console.log(err)
})


// Create a variable for our port
const port = process.env.PORT || 4000;

// Run our server!
app.listen(port, () => {
 console.log(`Express MVC app is running on port ${port}`);
});
