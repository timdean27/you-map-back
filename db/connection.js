const mongoose = require('mongoose');
const dotenv = require('dotenv')

dotenv.config();

mongoose.connect(process.env.MONGODB_URL, {useNewUrlParser: true}).then(() => {
    console.log('Mongo DB connected')
}).catch((err) => {
    console.log(err)
})


// Export mongoose so we can use it elsewhere
module.exports = mongoose;
