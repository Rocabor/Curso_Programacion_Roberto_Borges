

	//ESTRUCTURA CONDICIONAL SWITCH//
        //MENU DE OPCIONES JAVASCRIPT//
let opcionMenu = prompt("INICIAR - GUARDAR - SALIR:")
opcionMenu = opcionMenu.toLowerCase();
switch (opcionMenu) {
    case "iniciar":
    console.log('Elegir nivel de dificultad')
    break;
    case "guardar":
    console.log('Elegir archivo de guardado')
    break;
    case "salir":
    console.log('Salir al menú principal')
    break;
    default:
       console.log('Comando Desconocido')} 