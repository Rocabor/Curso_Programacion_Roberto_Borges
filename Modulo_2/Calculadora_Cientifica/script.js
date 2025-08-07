

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
    document.getElementById('valDisp').value=Number(resultado.toFixed(5));
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
  pantalla.value = Math.cos(pantalla.value).toFixed(5)
}
function tan(){
  const pantalla=document.getElementById('valDisp')
  pantalla.value = Math.tan(pantalla.value).toFixed(5)
}
function sqrt(){
  const pantalla=document.getElementById('valDisp')
  pantalla.value = Math.sqrt(pantalla.value,2)
}






