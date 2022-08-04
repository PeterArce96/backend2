function hola(nombre){
    // resolve-->cuando se cumple la promesa
    // reject-->cuando no se cumple la promesa
    return new Promise(function(resolve,reject){
        setTimeout(() => {
            console.log('Hola '+nombre);
            resolve(nombre);
            reject('Hay un error')
        }, 1000);
    })
}

function hablar(nombre){
    return new Promise((res,rej)=>{
        console.log('como estas '+nombre);
        res(nombre);
        rej('no te entiendo');
    },1000)
}
let nom = 'Peter'

hola(nom)
    .then(hablar)
    .then(()=>{
        console.log('adios')
    })