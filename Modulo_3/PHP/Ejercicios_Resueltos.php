
 <!-- 1️⃣ Contador de Pares e Impares  -->
<!-- 🔢 Escribe un script que cuente y muestre la cantidad de números pares e impares que hay en el rango del 1 al 50. -->
<?php
$pares = 0;
$impares = 0;

for ($i = 1; $i <= 50; $i++) {
    if ($i % 2 == 0) {
        $pares++;
    } else {
        $impares++;
    }
}
echo "\nCantidad de números pares: " . $pares . "\n";
echo "\nCantidad de números impares: " . $impares . "\n";
?>


<!-- 2️⃣ Tabla de Multiplicar del 8
✖️ Crea un script que genere y muestre en la terminal la tabla de multiplicar completa del número 8, desde el 8×1 hasta el 8×10. -->
<?php
2️⃣ Tabla de Multiplicar del 8
✖️ Crea un script que genere y muestre en la terminal la tabla de multiplicar completa del número 8, desde el 8×1 hasta el 8×10.
for ($i = 1; $i <= 10; $i++) {
    echo "8 x " . $i . " = " . (8 * $i) . "\n";
}
echo "\n";
?>


<!-- 3️⃣ Juego: Adivina el Número
🎯 Desarrolla un programa que simule un juego de "adivina el número". Define una variable con un número secreto y utiliza un bucle while para intentar adivinarlo, incrementando un contador hasta encontrarlo. Muestra cada intento. -->
<?php
$numSecreto = 5;
$intentos = 1;
$adivina = true;

echo "adivina un numero del 1 al 10 \n";

while ($adivina) {
    echo "intento #" . $intentos . ": ingresa numero: ";
    $num_usuario = (int)readline(); 
    if ($num_usuario < $numSecreto){
        echo "el numero secreto es mas alto \n";
    } elseif ($num_usuario > $numSecreto){
            echo "el numero secreto es mas bajo \n";
    } else {
        echo "has adivinado el numero secreto: " . $numSecreto;
        $adivina= false;
       
    }
    $intentos ++;
}
?>

<!-- 4️⃣ Suma de Impares del 1 al 100
➕ Escribe un script que calcule la suma de todos los números impares desde el 1 hasta el 100. -->
<?php
$sumimpares = 0;
for ($i = 1; $i <= 100; $i++) {
    if ($i % 2 !=0){
        $sumimpares += $i;
    }
}
echo "La suma de los impares del 1 al 100 es: " . $sumimpares;
?>

<!-- 5️⃣ Verificación para Licencia de Conducir
🚗 Crea un programa que verifique si una persona puede obtener una licencia de conducir. La condición es que debe tener al menos 18 años y no más de 65 años. Define una variable para la edad y muestra si cumple los requisitos o no. -->
<?php
$edad = 25; // Define la edad de la persona

if ($edad >= 18 && $edad <= 65) {
  echo "La persona cumple con los requisitos para obtener la licencia de conducir.";
} else {
  echo "La persona no cumple con los requisitos para obtener la licencia de conducir.";
}
?>

<!-- 6️⃣ Dibujo de un Cuadrado con #
🧱 Utilizando bucles anidados, crea un script que dibuje un cuadrado de 5×5 en la terminal utilizando el carácter #. -->
<?php
for ($f=1; $f<=5; $f++) {
    for ($c=1; $c<=5; $c++) {
        echo " # ";
    }
      echo "\n";
}
?>

<!-- 7️⃣ Clasificación de un Número
➖➕ Desarrolla un script que determine si un número almacenado en una variable es positivo, negativo o cero, y muestre el resultado correspondiente. -->
<?php
$numero = 10; // Cambia este valor para probar con diferentes números

if ($numero > 0) {
  echo "El número $numero es positivo.";
} elseif ($numero < 0) {
  echo "El número $numero es negativo.";
} else {
  echo "El número es cero.";
}
?>

<!-- 8️⃣ Impresión Condicional: Mar y Tierra
🌊🌍 Escribe un programa que imprima los números del 1 al 30. Para los múltiplos de 3, debe imprimir "Mar"; para los múltiplos de 5, "Tierra"; y para los múltiplos de ambos, "MarTierra". -->
<?php
for ($i = 1; $i <= 30; $i++) {
  if ($i % 3 == 0 && $i % 5 == 0) {
    echo "MarTierra\n";
  } else if  ($i % 3 == 0) {
    echo "Mar\n";
  } else if ($i % 5 == 0) {
    echo "Tierra\n";
  } else {
    echo $i . "\n";
  }
}
?>

<!-- 9️⃣ Clasificación de Temperatura
🌡️ Crea un script que, dada una variable numérica que representa la temperatura en grados Celsius, muestre un mensaje diferente según el valor:
   ❄️ "Fría" si es menor de 10°C  
   🌤️ "Templada" si está entre 10°C y 25°C  
   🔥 "Calurosa" si es mayor de 25°C -->
<?php
$temperatura = 25; //  Cambia este valor para probar diferentes temperaturas

if ($temperatura < 10) {
    echo "❄️ Fría. La temperatura es de " . $temperatura . " grados Celsius.";
} elseif ($temperatura >= 10 && $temperatura <= 25) {
    echo "🌤️ Templada.  La temperatura es de " . $temperatura . " grados Celsius.";
} else {
    echo "🔥Calurosa. La temperatura es de " . $temperatura . " grados Celsius.";
}
?>

<!-- 🔟 Cuenta Regresiva de Año Nuevo
🎆 Escribe un programa que realice una cuenta regresiva desde el 10 hasta el 1. Al finalizar, debe mostrar el mensaje: "¡Feliz Año Nuevo! 🎉" -->
<?php
  for ($i = 10; $i >= 1; $i--) {
    echo $i . "\n";
  }
  echo "¡Feliz Año Nuevo!";
?>