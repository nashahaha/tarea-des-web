//const comTextArea = document.getElementById("comm-text-area");

const validarComentario = (comentario) => 
  comentario && comentario.length<=2000 && comentario.length>=5

const validarNombre=(nombre) =>
  {
      var validName = /^([A-Za-zÑñÁáÉéÍíÓóÚú]+['\-]{0,1}[A-Za-zÑñÁáÉéÍíÓóÚú]+)(\s+([A-Za-zÑñÁáÉéÍíÓóÚú]+['\-]{0,1}[A-Za-zÑñÁáÉéÍíÓóÚú]+))*$/; // expresión regular para verificar que solo tiene letras y espacios   
      return nombre && nombre.length>=3 && nombre.length<=80 && validName.test(nombre);
  } 

const agregarComentario = () => {
  //OBTIENE EL INPUT
  let comTextArea = document.getElementById("comm-text-area")
  let commText = comTextArea.value;
  let name = document.getElementById("comm-author");

  let error = document.getElementById("error");
  let sended = document.getElementById("sended");
  

  // VALIDA INPUT
  let isValid = validarComentario(commText) && validarNombre(name.value);
  if (!isValid) {
    error.style.color = 'red';
    error.hidden = false;
    sended.hidden = true;
    return;
  } else {
    error.hidden = true;
    sended.hidden = false;
  }

};
let submitCommBtn = document.getElementById("submit-comm-btn");
submitCommBtn.addEventListener("click", agregarComentario);




//let foto = document.getElementById("img1");
//foto.style.width = "640px";
//foto.style.height = "auto";

// Cambia el tamaño de la imagen
//const changeImage = (img) => {
//  if(img.style.width === "640px") {
//    img.style.width = "850px";
//  } else {
//    img.style.width = "640px";
//  }
//}

foto.addEventListener("click", () => changeImage(foto))