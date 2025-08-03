

//BUCLE WHILE//
     //ADIVINA EL NUMERO//
 const numSecr = 5;
 let inteUsuar = prompt("Adivine un número del 1 al 20: ");
 inteUsuar=parseInt(inteUsuar);
 intento=0;
 while (true) {
      if (numSecr==inteUsuar){
        console.log(`Has adivinado el numero secreto con ${intento} intentos`); 
      break;}
        else {
        intento ++;
        console.log(`llevas ${intento} intentos`); 
        inteUsuar = prompt("Ingrese otro número: "); }  }