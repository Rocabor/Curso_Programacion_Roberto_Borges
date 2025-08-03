

//CLASIFICADOR DE ESTACIONES//
let mes = prompt("Ingrese mes del año:")
mes=mes.toLowerCase();
 switch (mes) {
    case "diciembre":
    case "enero":
    case "febrero":
      estacion = "Invierno";
      console.log('Estas en',estacion)
      break;
    case "marzo":
    case "abril":
    case "mayo":
      estacion = "Primavera";
      console.log('Estas en',estacion)
      break;
    case "junio":
    case "julio":
    case "agosto":
      estacion = "Verano";
      console.log('Estas en',estacion)
      break;
    case "septiembre":
    case "octubre":
    case "noviembre":
      estacion = "Otoño";
      console.log('Estas en',estacion)
      break;
    default:
      estacion = "Mes inválido";} 