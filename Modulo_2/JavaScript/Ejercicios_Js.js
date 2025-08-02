
//
let nombre = "Roberto";
console.log("Nombre de usuario:", nombre);
let eddad = 30;
console.log("Edad de usuario:", edad);
let esEstudiante = true;
console.log("Estudia?:", esEstudiante);


let nomb=prompt("ingrese su nombre:");
let añonac=prompt("ingrese su año de nacimiento:");
const ap=2025;
let rest = ap-añonac;
console.log(`Edad del usuario: ${resta} años`);


let aa=prompt("ingrese numero 1:");
let ba=prompt("ingrese numero 2:");
 a = +a;
 b= +b;
let suma = a + b; // Suma
let resta = a - b; // Resta
let multiplicacion = a * b; // Multiplicación
let division = a / b; // División
let modulo = a % b; // Módulo (resto de la división)
let exponenciacion = a ** b; // Exponenciación
console.log(`Suma: ${suma}`);
console.log(`Resta: ${resta}`);
console.log(`Multiplicación: ${multiplicacion}`);
console.log(`División: ${division}`);
console.log(`Módulo: ${modulo}`);   
console.log(`Exponenciación: ${exponenciacion}`);


let base=prompt("ingrese base:");
let altura=prompt("ingrese altura:");
base = +base;
altura= +altura;
let area = base * altura
console.log(`Area de un rectandgulo: ${area}`); 



let edad=prompt("ingrese su edad:");
edad =+edad
if (edad >= 18) {
    mensaje = "mayor";}
    else if (edad <18) {
    edad = "menor de edad";
    mensaje = "menor";
    }
console.log(`Eres ${mensaje} de edad`);



let num1=prompt("ingrese numero 1:");
let num2=prompt("ingrese numero 2:");
 num1 = +num1;
 num2 = +num2;
 if (num1==num2){ mensaje = "son iguales"}
    else if (num1>num2) { mensaje = "el primer numero es mayor"}
    else {mensaje = "el segundo numero es mayor"}
console.log(` ${mensaje}`);



let colorSemaforo=prompt("ingrese color de semaforo:");
let rojo="rojo"
let amarillo="amarillo"
let verde="verde"
if (colorSemaforo==rojo){mensaje = "No cruce"}
    else if (colorSemaforo==amarillo){mensaje = "Precaución"}
    else {mensaje = "Puede Cruzar"}
console.log(` ${mensaje}`);




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
        break;
}



let optMenu=prompt("ingrese opcion INICIAR - GUARDAR - SALIR:");
console.log(`El usuario ha elegido: ${optMenu}.`);

optMenu="INICIAR"
optMenu="GUARDAR"
optMenu="SALIR"
let optMenuMin = optMenu.toLowerCase;

switch (optMenu) {
    case "iniciar":
        console.log("Has INICIADO");
        break; // 'break' es crucial para no seguir ejecutando los siguientes casos.
    case "guardar":
        console.log("Has GUARDADO");
        break;
    case "salir":
        console.log("Has SALIDO");
        break;

    default: // Se ejecuta si ninguno de los casos anteriores coincide.
        console.log("comando desconocido.");
        break;
}

