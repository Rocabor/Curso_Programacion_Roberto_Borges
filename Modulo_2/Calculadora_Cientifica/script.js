

function dis(val){
  const pantalla=document.getElementById('valDisp');
  if(pantalla.value === "0"){
    pantalla.value = val;
  } else {
    pantalla.value += val; }
}
function resultado(){
  try {
    const resultado = eval(document.getElementById('valDisp').value);
    document.getElementById('valDisp').value=Number(resultado.toFixed(7));
  }catch{
      document.getElementById('valDisp').value='Error';
    }
  }
function ac(){
  document.getElementById('valDisp').value='0'
  
}
function del(){
  const pantalla=document.getElementById('valDisp')
  pantalla.value = pantalla.value.slice(0,-1);
}
function x2(){
  const pantalla=document.getElementById('valDisp')
  pantalla.value = Math.pow(pantalla.value,2)
}
function cos(){
  const pantalla=document.getElementById('valDisp')
  pantalla.value = Number(Math.cos(pantalla.value).toFixed(7))
}
function tan(){
  const pantalla=document.getElementById('valDisp')
  pantalla.value = Number(Math.tan(pantalla.value).toFixed(7))
}
function sqrt(){
  const pantalla=document.getElementById('valDisp')
  pantalla.value = Number(Math.sqrt(pantalla.value,2).toFixed(7))
}






