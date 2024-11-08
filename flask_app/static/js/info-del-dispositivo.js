
const validarComentario = (comentario) => {
  if (!comentario) return false; // Check if comentario is falsy
  const trimmedComentario = comentario.trim();
  const length = trimmedComentario.length;
  
  return length >= 5 && length < 300;
};

const validarNombre=(nombre) =>
  {
      var validName = /^([A-Za-zÑñÁáÉéÍíÓóÚú]+['\-]{0,1}[A-Za-zÑñÁáÉéÍíÓóÚú]+)(\s+([A-Za-zÑñÁáÉéÍíÓóÚú]+['\-]{0,1}[A-Za-zÑñÁáÉéÍíÓóÚú]+))*$/; // expresión regular para verificar que solo tiene letras y espacios   
      return nombre && nombre.length>=3 && nombre.length<=80 && validName.test(nombre);
  } 

const agregarComentario = () => {
  //OBTIENE EL INPUT
  let comTextArea = document.getElementById("comm-text-area")
  let name = document.getElementById("comm-author");
  console.log(comTextArea);
  console.log(name)
  let error = document.getElementById("error");
  let sended = document.getElementById("sended");
  error.hidden = true;
  sended.hidden = true;

  // VALIDA INPUT
  let isValid = validarComentario(comTextArea.value) && validarNombre(name.value);
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



let foto = document.getElementById("img-dev");
foto.style.width = "560px";
foto.style.height = "auto";

// Cambia el tamaño de la imagen
const changeImage = (img) => {
  
  if(img.style.width === "560px") {
    img.style.width = "850px";
  } else {
    img.style.width = "560px";
  }
}

foto.addEventListener("click", () => changeImage(foto))