//---------------Crear caja para nuevos dispositivos------------------

let cntLlamado = 1; // Contador de llamados

  const agregarDispositivo = () => {
    cntLlamado++ //Aumentamos el contador de llamados

    let dispositivoForm = document.getElementById("device-section-1"); //Nodo con la información del dispositivo
    let formClone = dispositivoForm.cloneNode(true); // Clon del nodo

    formClone.id = "device-section-" + cntLlamado.toString(); // Cambia el id del nodo clonado
    formClone.name = "device-section";

    // Cambia el número de dispositivo en el subtítulo
    let bajada = formClone.querySelector("#dispositivo");
    bajada.textContent = "Información del dispositivo " + cntLlamado.toString() + ":";

    // Selecciona todos los elementos dentro del clon que tengan un id, nombre y error
    let elementsWithId = formClone.querySelectorAll("[id]");
    //let elementsWithName = formClone.querySelectorAll("[name]");
    let elementsWithError = formClone.querySelectorAll('.error');

      elementsWithId.forEach(element => {
          // Vacía el contenido del elemento
          element.value = ""

          // Obtiene el id original de cada elemento
          let originalId = element.id;

          // Asigna un nuevo id según el número de llamado
          element.id = originalId + "-" + cntLlamado;

          // Busca si hay un label que haga referencia a este id y cambia la referencia del atributo for
          let associatedLabel = formClone.querySelector(`label[for='${originalId}']`);
          if (associatedLabel) {
              associatedLabel.setAttribute("for", element.id);
          }   
          
          // Limpia el marco
          element.style.borderColor = "";
      });

      //elementsWithName.forEach(element => {
      //    let originalName = element.name;
      //    element.name = originalName + "-" + cntLlamado;
      //});

      //Limpia el error del clon de origen
      elementsWithError.forEach(element => {
        element.textContent = "";
      });

    // Inserta el nodo clonado en el documento
    let form = document.getElementById("form-info");
    let addDeviceBtn = document.getElementById("add-device-btn")
    form.insertBefore(formClone, addDeviceBtn);
  };
  let submitConfBtn = document.getElementById("add-device");
  submitConfBtn.addEventListener("click", agregarDispositivo);