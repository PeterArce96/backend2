const express = require('express');
const {config} = require('./config');
const cors = require('cors');

const app = express();
app.use(cors());

app.set('port',config.port);

app.get('/',(req,res)=>{
    res.json({
        status:true,
        content:'servidor activo'
    })
})

app.use('/producto',require('./routes/producto.routes'));

module.exports = app;