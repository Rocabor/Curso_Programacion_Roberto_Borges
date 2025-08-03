

let edadUsuario = prompt("Ingrese su edad: ")
edadUsuario= parseInt(edadUsuario);
let tieneTicket = prompt("Tiene Ticket?: ")
if (tieneTicket == "si"){ //convierto cadena a bool
    tieneTicket=true;
} else {
    tieneTicket=false;
}
if (edadUsuario >= 18 && tieneTicket ===true) {
    console.log(`Acceso Concedido`);
} else { 
    console.log(`Acceso Denegado`); 
}