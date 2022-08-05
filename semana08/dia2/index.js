const express = require('express');


const mysqlConnection = require('./database');

const app = express();
const port = 5000;


//permite que el servidor reciba data en json
app.use(express.json());


app.get('/',(req,res)=>{
    res.json({
        'status':true,
        'content':'Mi primer app web con express Js - César Mayta'
    })
})

//api rest de alumnos
app.get('/alumno',(req,res)=>{
    mysqlConnection.query('select * from tbl_alumno',(err,rows,fields)=>{
        if(!err){
            res.json(rows);
        }else{
            console.log(err);
        }
    })
})

app.post('/alumno',(req,res)=>{
    const {nombre,email} = req.body;

    const query = `insert into tbl_alumno(alumno_nombre,alumno_email)
                    values('${nombre}','${email}')`;
    
    mysqlConnection.query(query,(err,rows,fields)=>{
        if(!err){
            res.json({
                'status':true,
                'content':'alumno creado'
            })
        }else{
            console.log(err);
        }
    });
});

app.put('/alumno/:id',(req,res)=>{
    const {nombre,email} = req.body;
    const {id} = req.params;

    const query = "update tbl_alumno set alumno_nombre=?,alumno_email=? where alumno_id=?";

    mysqlConnection.query(query,[nombre,email,id],
        (err,rows,fields)=>{
            if(!err){
                res.json({
                    'status':true,
                    'content':'alumno actualizado'
                })
            }else{
                console.log(err);
            }
        })
})

app.delete('/alumno/:id',(req,res)=>{
    const {id} = req.params;

    query = "delete from tbl_alumno where alumno_id = ?"

    mysqlConnection.query(query,[id],
        (err,rows,fields)=>{
            if(!err){
                res.json({
                    'status':true,
                    'content':'alumno eliminado'
                })
            }else{
                console.log(err);
            }
        })
})

//api rest de cursos
app.get('/curso',(req,res)=>{
    mysqlConnection.query('select * from tbl_curso',(err,rows,fields)=>{
        if(!err){
            res.json(rows);
        }else{
            console.log(err);
        }
    })
})

app.post('/curso',(req,res)=>{
    const {nombre} = req.body;

    const query = `insert into tbl_curso(curso_nombre)
                    values('${nombre}')`;
    
    mysqlConnection.query(query,(err,rows,fields)=>{
        if(!err){
            res.json({
                'status':true,
                'content':'curso creado'
            })
        }else{
            console.log(err);
        }
    });
});

app.put('/curso/:id',(req,res)=>{
    const {nombre} = req.body;
    const {id} = req.params;

    const query = "update tbl_curso set curso_nombre=? where curso_id=?";

    mysqlConnection.query(query,[nombre,id],
        (err,rows,fields)=>{
            if(!err){
                res.json({
                    'status':true,
                    'content':'curso actualizado'
                })
            }else{
                console.log(err);
            }
        })
})

app.delete('/curso/:id',(req,res)=>{
    const {id} = req.params;

    query = "delete from tbl_curso where curso_id = ?"

    mysqlConnection.query(query,[id],
        (err,rows,fields)=>{
            if(!err){
                res.json({
                    'status':true,
                    'content':'curso eliminado'
                })
            }else{
                console.log(err);
            }
        })
})

app.listen(port,()=>{
    console.log('servidor activo en http://localhost:'+port);
})