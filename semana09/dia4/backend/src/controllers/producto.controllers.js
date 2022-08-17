const productoController = {};

const cloudinary = require('cloudinary').v2

cloudinary.config({ 
    cloud_name: 'parcecodigog15', 
    api_key: '423686832888737', 
    api_secret: 'H__eNm9YMtxHOX2VBYlRWzy4LFI' 
});

const productoModel = require('../models/producto.models');

productoController.getAll = async (req,res)=>{
    const productos = await productoModel.find();
    res.json({
        success: true,
        message: "Los productos se han cargado correctamente",
        content:productos
    })
}
productoController.create = async (req,res)=>{
    try{
        // console.log("archivo : " + req.files);
        // cloudinary.v2.uploader.upload(req.files.productoImagen2, {upload_preset: "my_preset"}, (error, result)=>{
        //     console.log(result, error);
        // });

        const nuevoProducto = new productoModel(req.body)
        await nuevoProducto.save();
        res.json({
            success: true,
            message: "producto registrado con exito",
            content:nuevoProducto
        })
    }catch(error){
        res.status(502).json({
            success:false,
            message:'error al registrar el producto',
            content: error
        })
    }
}

productoController.uploadImageAndCreate = async (req,res)=> {
    productoImagen = req.files.productoImagen
    console.log(productoImagen.name);

    let uploadPath;
    uploadPath = '../backend/src/uploads/' + productoImagen.name;

    productoImagen.mv(uploadPath,function(err){
        if(err){
            res.status(502).json({
                success: false,
                message: "no se pudo subir la imagen",
                content:err
            })
        }
        else{
            res.json({
                success: true,
                message: "producto e imagen registrado con exito",
                content:productoImagen.name
            })
        }
    })
}

module.exports = productoController;