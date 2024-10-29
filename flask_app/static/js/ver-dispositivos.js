function goToInfoDevice(elem) { 
    
    let device_id = elem.getAttribute('data-device-id');
    window.location.href = "/informacion-dispositivo/" + device_id;
}
