function hola(nombre, primercallback){
    setTimeout(() => {
        console.log('Hola ' + nombre);
        primercallback(nombre)
    }, 1000);
}

function hablar(nombre,segundocallback){
    setTimeout(() => {
        console.log("como estas " +nombre);
        segundocallback(nombre);
    });
}
function adios(nombre){
    console.log('adios ' +nombre);
}

hola('Peter', function(nombre){
    // console.log('como estás ' +nombre);
    hablar(nombre,function(nombre){
        adios(nombre);
    })
})