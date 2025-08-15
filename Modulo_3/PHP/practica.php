
<?php

$nombre = "Roberto Borges";
$edad = 38;
$descripcion = "estudiante del curso programacion en centro eductivo logros";
echo "nombre: " . $nombre .   "\nedad:" .$edad . "\ndescripcion: " . $descripcion

?>

<?php
1️⃣ Contador de Pares e Impares
🔢 Escribe un script que cuente y muestre la cantidad de números pares e impares que hay en el rango del 1 al 50.
echo "Numero pares: \n";
for ($i = 2; $i <= 50; $i+=2) {
    echo $i . "";
}

echo "\nNumero impares: \n";
for ($i = 1; $i <= 50; $i+=2) {
    echo $i . "";
}
?>


<?php
2️⃣ Tabla de Multiplicar del 8
✖️ Crea un script que genere y muestre en la terminal la tabla de multiplicar completa del número 8, desde el 8×1 hasta el 8×10.
for ($i = 1; $i <= 10; $i++) {
    echo "8 x " . $i . " = " . (8 * $i) . "\n";
}
echo "\n";
?>

<?php
3️⃣ Juego: Adivina el Número
🎯 Desarrolla un programa que simule un juego de "adivina el número". Define una variable con un número secreto y utiliza un bucle while para intentar adivinarlo, incrementando un contador hasta encontrarlo. Muestra cada intento.
$numSecreto = 5;
$intentos = 1;
$adivina = true;

echo "adivina un numero del 1 al 10 \n";

while ($adivina) {
    echo "intento #" . $intentos . ": ingresa numero: ";
    $num_usuario = (int)readline(); 
    if ($num_usuario<$numSecreto){
        echo "el numero secreto es mas alto \n";
    } elseif ($num_usuario>$numSecreto){
            echo "el numero secreto es mas bajo \n";
    } else {
        echo "has adivinado el numero secreto: " . $numSecreto;
        $adivina= false;
       
    }
    $intentos ++;
}
?>

<?php
4️⃣ Suma de Impares del 1 al 100
➕ Escribe un script que calcule la suma de todos los números impares desde el 1 hasta el 100.
echo "\nNumero impares: \n";

for ($i = 1; $i <= 100; $i+=2) {
    echo $i . "";
    $sum = i;

}




?>






