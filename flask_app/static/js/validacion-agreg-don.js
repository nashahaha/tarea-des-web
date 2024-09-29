// VALIDADOR NOMBRE
const validarNombre=(nombre) =>{
        var validName = /^([A-Za-zÑñÁáÉéÍíÓóÚú]+['\-]{0,1}[A-Za-zÑñÁáÉéÍíÓóÚú]+)(\s+([A-Za-zÑñÁáÉéÍíÓóÚú]+['\-]{0,1}[A-Za-zÑñÁáÉéÍíÓóÚú]+))*$/; // expresión regular para verificar que solo tiene letras y espacios   
        return nombre && nombre.length>=3 && nombre.length<=80 && validName.test(nombre);
    } 

// VALIDADOR EMAIL
const validarEmail=(mail) =>{            
    var validEmail =  /^\w+([.-_+]?\w+)*@\w+([.-]?\w+)*(\.\w{2,10})+$/;
    return validEmail.test(mail) && mail && (mail.split('@').length - 1) === 1; // prueba que exista, tenga solo un @ y formato de mail
} 

//VALIDADOR NUMERO DE TELEFONO
//campo opcional
const validarTelefono=(telefono) =>{
    var validPhone = /^(\+?56)?(\s?)(0?9)(\s?)[98765432]\d{7}$/;
    return validPhone.test(telefono) || telefono===""; //tiene el formato o es vacío
}

//VALIDADOR NOMBRE DISPOSITIVO
const validarDisp=(dispositivo) =>
    dispositivo && dispositivo.length>=3 && dispositivo.length<=80


//VALIDADOR DESCRIPCIÓN
const validarDesc=(descripcion) =>
    descripcion.length<500

//AÑOS DE USO
const validarAnnos=(annos) =>
    annos && annos>=1 && annos<=99 && Number.isInteger(+annos)

//FOTOS DEL PRODUCTO
const validarImg = (files) => {
    if (!files) return false;
  
    // validación del número de archivos
    let lengthValid = 1 <= files.length && files.length <= 3;
  
    // validación del tipo de archivo
    let typeValid = true;
  
    for (const file of files) {
      let fileFamily = file.type.split("/")[0];
      typeValid &&= fileFamily == "image";
    }

    return lengthValid && typeValid;
  };

//VALIDADOR SELECT (región, comuna, tipo, estado funcionamiento)
const validarSelect = (select) => {
    if(!select) return false;
    return true;
  }

const validarForm = () => {
    isFormValid = true; 

    // FUNCIÓN PARA CREAR UN ERROR
    // Recibe un input, nombre del id del mesaje de error y el texto del mensaje de error por mostrar
    const mostrarError = (input, idName, mensaje) => {
        let errorMsg = document.getElementById("error-msg-" + idName);
        if (!errorMsg) {
            errorMsg = document.createElement('div');
            errorMsg.className = "error";
            errorMsg.id = "error-msg-" + idName; //nos importa el id del error para poder limpiarlo después
            errorMsg.style.color = 'red';
            input.parentNode.insertBefore(errorMsg, input.nextSibling);
        }
        errorMsg.textContent = mensaje;
        input.style.borderColor = "red";
    };

    // FUNCIÓN PARA LIMPIAR ERROR
    const limpiarError = (input, idName) => {
        let errorMsg = document.getElementById("error-msg-" + idName);
        if (errorMsg) {
            errorMsg.textContent = "";
        }
        input.style.borderColor = "";
    };

    //INPUTS WITH CONTACT INFORMATION
    let nameInput = document.getElementById('username');
    let emailInput = document.getElementById('email');
    let phoneNumInput = document.getElementById('phone-number');
    let regionInput = document.getElementById('select-region');
    let comunaInput = document.getElementById('select-comuna');

    //INPUTS VALIDATION
    // NOMBRE
    if (!validarNombre(nameInput.value)){
        mostrarError(nameInput, "name", "Nombre inválido");
        isFormValid = false;
    } else {
        limpiarError(nameInput, "name");
    }

    // EMAIL
    if (!validarEmail(emailInput.value)) {
        mostrarError(emailInput, "email", "Mail inválido");
        isFormValid = false;
    } else {
        limpiarError(emailInput, "email");
    }

    // TELÉFONO
    if (!validarTelefono(phoneNumInput.value)) {
        mostrarError(phoneNumInput, "phone-num", "Número de teléfono inválido");
        isFormValid = false;
    } else {
        limpiarError(phoneNumInput, "phone-num");
    }

    //REGION
    if (!validarSelect(regionInput.value)){
        mostrarError(regionInput, "region", "Seleccione una región");
        isFormValid = false;
    } else {
        limpiarError(regionInput, "region");
    }

    //COMUNA
    if (!validarSelect(comunaInput.value)){
        mostrarError(comunaInput, "comuna", "Seleccione una comuna");
        isFormValid = false;
    } else {
        limpiarError(comunaInput, "comuna");
    }

    // CHECK ALL DEVICES INPUTS
    // NOMBRE DISPOSITIVO
    let deviceNameInput = document.querySelectorAll('.device-name');
    deviceNameInput.forEach(element => {
        if (!validarDisp(element.value)) {
            mostrarError(element, element.id, "Ingrese el nombre de su dispositivo");
            isFormValid = false;
        } else {
            limpiarError(element, element.id);
        }
    });
    
    // DESCRIPCIÓN
    let descInput = document.querySelectorAll('.device-descr');
    descInput.forEach(element =>{
        if (!validarDesc(element.value)) {
            mostrarError(element, element.id, "Límite de caracteres excedido");
            isFormValid = false;
        } else {
            limpiarError(element, element.id);
        }
    });
    
    // TIPO
    let typeInput = document.querySelectorAll('.device-type');
    typeInput.forEach(element => {
        if (!validarSelect(element.value)){
            mostrarError(element, element.id, "Seleccione un tipo de dispositivo");
            isFormValid = false;
        } else {
            limpiarError(element, element.id)
        }
    });

    //AÑOS DE USO
    let yearsInput = document.querySelectorAll('.years-of-use');
    yearsInput.forEach(element => {
        if (!validarAnnos(element.value)) {
            mostrarError(element, element.id, "Por favor ingrese un número de años válido (Ej: 2)");
            isFormValid = false;
        } else {
            limpiarError(element, element.id);
        }
    });
    
    // FUNCIONAMIENTO
    let stateInput = document.querySelectorAll('.working-status');
    stateInput.forEach(element => {
        if (!validarSelect(element.value)){
            mostrarError(element, element.id, "Indique el estado de funcionamiento de su dispositivo");
            isFormValid = false;
        } else {
            limpiarError(element, element.id);
        }
    });
    
    // IMAGENES
    let picsInput = document.querySelectorAll('.device-pics');
    picsInput.forEach(element => {
        if (!validarImg(element.files)){
            mostrarError(element, element.id, "Ingrese de 1 a 3 fotos del dispositivo");
            isFormValid = false;
        } else {
            limpiarError(element, element.id);
        }
    });

    // Mensaje de confirmación
    let myForm = document.forms["form"];
    let volverIndex = document.getElementById("return-to-home");
    let confirmationBox = document.getElementById("confirmation-box");
    if (isFormValid){
        // Ocultar el formulario
        myForm.style.display = "none";
        
        // Si precionamos botón para enviar
        let submitButton = document.getElementById("submit-btn");
        submitButton.addEventListener("click", () => {
        // myForm.submit();
        // no tenemos un backend al cual enviarle los datos
        confirmationBox.style.display = "none";
        volverIndex.hidden = false;
        });

        // Si queremos volver al formulario
        let backButton = document.getElementById("back-btn");
        backButton.addEventListener("click", () => {
        // Mostrar el formulario nuevamente
        myForm.style.display = "block";
        confirmationBox.hidden = true;
        });

        // hacer visible el mensaje de validación
        confirmationBox.hidden = false;
    }

};
    
  
// Enviamos el form
let submitBtn = document.getElementById("envio");
submitBtn.addEventListener("click", validarForm);