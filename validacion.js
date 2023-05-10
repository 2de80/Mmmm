function validarFormulario() {

// Verificar si el nombre contiene solo caracteres alfabéticos y espacios

var nombre = document.getElementById('nombre').value; // Obtener el valor del campo de nombre del formulario
var re = /^[a-zA-ZñÑáÁéÉíÍóÓúÚ\s]+$/; // Expresión regular para permitir solo letras y espacios

if (nombre.trim() === '') {
    alert("El campo 'nombre' es obligatorio.");
    return false;
} else if (!re.test(nombre)) {
    alert("El campo 'nombre' no es válido. Debe contener sólo letras y espacios.");
    return false;
}

// Verificar si el email tiene la estructura correcta

var email = document.getElementById('email').value; // Obtener el valor del campo de email del formulario
var re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/; // Expresión regular para validar el formato del email

if (email.trim() === '') {
    alert("El campo 'email' es obligatorio.");
    return false;
} else if (!re.test(email)) {
    alert("El campo 'email' no es válido. Debe tener un formato de correo electrónico.");
    return false;
}


// Verificar si el mensaje contiene solo caracteres alfabéticos y espacios
var mensaje = document.getElementById('mensaje').value; // Obtener el valor del campo de nombre del formulario
var re = /^[a-zA-ZñÑáéíóúÁÉÍÓÚ\s¡!?,]+$/; // Expresión regular para permitir solo letras espacios

if (mensaje.trim() === '') {
    alert("El campo 'mensaje' es obligatorio.");
    return false;
} else if (!re.test(mensaje)) {
    alert("El campo 'mensaje' no es válido. Debe contener sólo letras, !?, comas y espacios.");
    return false;
}

 // Si todas las validaciones son exitosas, enviar el formulario
 alert("Formulario enviado correctamente.");
 return true;
}
