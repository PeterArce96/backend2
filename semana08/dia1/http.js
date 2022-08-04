const http = require('http');

http.createServer(function(req,res){
    console.log('servidor web iniciado');
    res.write('<h1><center>Mi primer cervidor web con NodeJs</center></h1>');
    res.end();
}).listen(5000);