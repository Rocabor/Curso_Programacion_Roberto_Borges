

let montoCompra = prompt("Ingrese monto de compra: ")
montoCompra= parseInt(montoCompra);
if (montoCompra > 100) {
    precioFinal=montoCompra-(montoCompra*(20/100));
    console.log(`Precio final de compra con 20% de descuento: ${precioFinal}`);
}   else if (montoCompra > 50 && montoCompra <=100) {
    precioFinal=montoCompra-(montoCompra*(10/100));
    console.log(`Precio final de compra con 10% de descuento: ${precioFinal}`);
}   else if (montoCompra <=50) {
    console.log(`Precio final sin descuento: ${montoCompra}`);  }