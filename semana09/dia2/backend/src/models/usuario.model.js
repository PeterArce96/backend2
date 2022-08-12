const mongoose = require('mongoose');
const Schema = mongoose.Schema;

const UsuarioSchema = new Schema({
    nombre:String,
    password:String
})

module.exports = mongoose.model('usuario',UsuarioSchema);