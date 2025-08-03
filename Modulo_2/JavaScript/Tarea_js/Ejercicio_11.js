
let diaSem=prompt("ingrese dia de semana:");
diaSem=+diaSem

switch (diaSem) {
    case 1:
        console.log("Lunes");
        break; // 'break' es crucial para no seguir ejecutando los siguientes casos.
    case 2:
        console.log("Martes");
        break;
    case 3:
        console.log("Miercoles");
        break;
    case 4:
        console.log("Jueves");
        break;
    case 5:
        console.log("Viernes");
        break;
    case 6:
        console.log("Sabado");
        break;
    case 7:
        console.log("Domingo");
        break;
    default: // Se ejecuta si ninguno de los casos anteriores coincide.
        console.log("ingrese un numero del 1 al 7.");
        break; }