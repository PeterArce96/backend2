const express = require('express');
const {config} = require('./config');
const cors = require('cors');

const fileUpload = require('express-fileupload');

const app = express();

// middleares
app.use(cors());
app.use(fileUpload());
app.use(express.json());

app.set('port',config.port);

app.get('/',(req,res)=>{
    res.json({
        status:true,
        content:'servidor activo'
    })
})

app.use('/producto',require('./routes/producto.routes'));

module.exports = app;