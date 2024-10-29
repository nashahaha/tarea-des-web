const comTextArea = document.getElementById("comm-text-area");

const validarComentario = (comentario) => 
  comentario && comentario.length<=2000 && comentario.length>=5

const validarNombre=(nombre) =>
  {
      var validName = /^([A-Za-zÑñÁáÉéÍíÓóÚú]+['\-]{0,1}[A-Za-zÑñÁáÉéÍíÓóÚú]+)(\s+([A-Za-zÑñÁáÉéÍíÓóÚú]+['\-]{0,1}[A-Za-zÑñÁáÉéÍíÓóÚú]+))*$/; // expresión regular para verificar que solo tiene letras y espacios   
      return nombre && nombre.length>=3 && nombre.length<=80 && validName.test(nombre);
  } 

const agregarComentario = (nombre, commText, fecha) => {
  //OBTIENE EL INPUT
  //let commText = comTextArea.value;
  //let name = document.getElementById("comm-author");

  //let error = document.getElementById("error");
  //let sended = document.getElementById("sended");
  

  // VALIDA INPUT
  //let isValid = validarComentario(commText) && validarNombre(name.value);
  //if (!isValid) {
  //  error.style.color = 'red';
  //  error.hidden = false;
  //  sended.hidden = true;
  //  return;
  //} else {
  //  error.hidden = true;
  //  sended.hidden = false;
  //}
  
  //CREA BLOQUES PARA MOSTRAR EN PANTALLA
  // contenedor comentario
  const commContainer = document.createElement("div");
  commContainer.className = "comm-container";

  // username
  const commentAuthor = document.createElement("p");
  commentAuthor.className = "comm-author";
  commentAuthor.innerText = nombre;

  // texto del comentario
  const comment = document.createElement("p");
  console.log(commText);
  comment.innerText = commText;

  // fecha del comentario
  const commDate = document.createElement("p");
  commDate.className = "comm-date";
  commDate.innerText = fecha;

  // contenedor nombre y fecha
  const headContainer = document.createElement("div");
  headContainer.className = "head-container";
  headContainer.appendChild(commentAuthor);
  headContainer.appendChild(commDate);

  // agregamos los elementos al cont. de la confesion
  commContainer.appendChild(headContainer);
  commContainer.appendChild(comment);

  // dejamos el área de texto en blanco
  // comTextArea.value = "";

  // agregamos la confesion a la lista
  let commList = document.getElementById("comments-list");
  commList.insertBefore(commContainer, commList.firstChild);
};
//let submitConfBtn = document.getElementById("submit-comm-btn");
//submitConfBtn.addEventListener("click", agregarComentario);




let foto = document.getElementById("img1");
foto.style.width = "640px";
foto.style.height = "auto";

// Cambia el tamaño de la imagen
const changeImage = (img) => {
  if(img.style.width === "640px") {
    img.style.width = "850px";
  } else {
    img.style.width = "640px";
  }
}

foto.addEventListener("click", () => changeImage(foto))