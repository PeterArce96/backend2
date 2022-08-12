const usuarioController = {};

const usuarioModel = require('../models/usuario.model');

usuarioController.getAll = async (req,res)=>{
    const usuarios = await usuarioModel.find();
    res.json(usuarios);
}
usuarioController.create = async(req,res)=>{
    const {nombre,password} = req.body;
    const nuevousuario = new usuarioModel({
        nombre,
        password
    })
    await nuevousuario.save();
    res.json({
        status:true,
        content:'nuevo usuario'
    })
}

usuarioController.update = async (req,res)=>{
    const {id} = req.params;
    // await usuarioModel.updateOne({_id:id},req.body);
    // const usuarioEditada = await usuarioModel.findOne({_id:id})
    const usuarioEditado = await usuarioModel.findOneAndUpdate({_id: id},req.body,{
        returnOriginal: false
    })

    res.json(usuarioEditado.toJSON());
}
module.exports = usuarioController;