// const URL = "http://127.0.0.1:5000/"
// // Obtener referencia a los formularios
// var agregarSaborForm = document.getElementById('agregar-sabor-form');
// var agregarPostreForm = document.getElementById('agregar-postre-form');
// var agregarPaletaForm = document.getElementById('agregar-paleta-form');

// // Agregar evento al enviar el formulario de agregar sabor de helado
// agregarSaborForm.addEventListener('submit', function(event) {
//   event.preventDefault();

//   // Obtener los valores del formulario
//   var nombreSabor = document.getElementById('nombre-sabor').value;
//   var archivoSabor = document.getElementById('archivo-sabor').files[0];

//   // Crear objeto FormData para enviar los datos del formulario
//   var formData = new FormData();
//   formData.append('nombre-sabor', nombreSabor);
//   formData.append('archivo-sabor', archivoSabor);

//   // Realizar la solicitud al backend para agregar el sabor de helado
//   fetch(URL + 'producto/agregar_producto', {
//     method: 'POST',
//     body: formData
//   })
//   .then(function(response) {
//     // Lógica para manejar la respuesta del servidor
//     if (response.ok) {
//       // Sabor de helado agregado correctamente
//       // Actualizar la página para reflejar los cambios
//       location.reload();
//     } else {
//       // Error al agregar el sabor de helado
//       console.error('Error al agregar el sabor de helado');
//     }
//   })
//   .catch(function(error) {
//     // Lógica para manejar errores
//     console.error('Error en la solicitud:', error);
//   });
// });

// // Agregar evento al enviar el formulario de agregar postre
// agregarPostreForm.addEventListener('submit', function(event) {
//   event.preventDefault();

//   // Obtener los valores del formulario
//   var nombrePostre = document.getElementById('nombre-postre').value;
//   var archivoPostre = document.getElementById('archivo-postre').files[0];

//   // Crear objeto FormData para enviar los datos del formulario
//   var formData = new FormData();
//   formData.append('nombre-postre', nombrePostre);
//   formData.append('archivo-postre', archivoPostre);

//   // Realizar la solicitud al backend para agregar el postre
//   fetch(URL + 'producto/agregar_producto', {
//     method: 'POST',
//     body: formData
//   })
//   .then(function(response) {
//     // Lógica para manejar la respuesta del servidor
//     if (response.ok) {
//       // Postre agregado correctamente
//       // Actualizar la página para reflejar los cambios
//       location.reload();
//     } else {
//       // Error al agregar el postre
//       console.error('Error al agregar el postre');
//     }
//   })
//   .catch(function(error) {
//     // Lógica para manejar errores
//     console.error('Error en la solicitud:', error);
//   });
// });

// // Agregar evento al enviar el formulario de agregar paleta
// agregarPaletaForm.addEventListener('submit', function(event) {
//   event.preventDefault();

//   // Obtener los valores del formulario
//   var nombrePaleta = document.getElementById('nombre-paleta').value;
//   var archivoPaleta = document.getElementById('archivo-paleta').files[0];

//   // Crear objeto FormData para enviar los datos del formulario
//   var formData = new FormData();
//   formData.append('nombre-paleta', nombrePaleta);
//   formData.append('archivo-paleta', archivoPaleta);

//   // Realizar la solicitud al backend para agregar la paleta
//   fetch(URL + 'producto/agregar_producto', {
//     method: 'POST',
//     body: formData
//   })
//   .then(function(response) {
//     // Lógica para manejar la respuesta del servidor
//     if (response.ok) {
//       // Paleta agregada correctamente
//       // Actualizar la página para reflejar los cambios
//       location.reload();
//     } else {
//       // Error al agregar la paleta
//       console.error('Error al agregar la paleta');
//     }
//   })
//   .catch(function(error) {
//     // Lógica para manejar errores
//     console.error('Error en la solicitud:', error);
//   });
// });

const URL = "http://127.0.0.1:5000/";
// const URL = "http://mcarletti.pythonanywhere.com/"
// Obtener referencia a los formularios
var agregarSaborForm = document.getElementById('agregar-sabor-form');
var agregarPostreForm = document.getElementById('agregar-postre-form');
var agregarPaletaForm = document.getElementById('agregar-paleta-form');

// Agregar evento al enviar el formulario de agregar sabor de helado
agregarSaborForm.addEventListener('submit', function(event) {
  event.preventDefault();

  // Obtener los valores del formulario
  var nombreSabor = document.getElementById('nombre-sabor').value;
  var archivoSabor = document.getElementById('archivo-sabor').files[0];

  // Crear objeto FormData para enviar los datos del formulario
  var formData = new FormData();
  formData.append('id_producto', idProducto) // agrego como en html, REVISAR si está bien
  formData.append('nombre', nombreSabor);
  formData.append('imagen', archivoSabor);
  formData.append('tipo_producto', 'sabores');

  // Realizar la solicitud al backend para agregar el sabor de helado
  fetch(URL + 'producto/agregar_producto', {
    method: 'POST',
    body: formData
  })
  .then(function(response) {
    // Lógica para manejar la respuesta del servidor
    if (response.ok) {
      // Sabor de helado agregado correctamente
      // Actualizar la página para reflejar los cambios
      location.reload();
    } else {
      // Error al agregar el sabor de helado
      console.error('Error al agregar el sabor de helado');
    }
  })
  .catch(function(error) {
    // Lógica para manejar errores
    console.error('Error en la solicitud:', error);
  });
});

// Agregar evento al enviar el formulario de agregar postre
agregarPostreForm.addEventListener('submit', function(event) {
  event.preventDefault();

  // Obtener los valores del formulario
  var nombrePostre = document.getElementById('nombre-postre').value;
  var archivoPostre = document.getElementById('archivo-postre').files[0];

  // Crear objeto FormData para enviar los datos del formulario
  var formData = new FormData();
  formData.append('nombre', nombrePostre);
  formData.append('imagen', archivoPostre);
  formData.append('tipo_producto', 'postres');

  // Realizar la solicitud al backend para agregar el postre
  fetch(URL + 'producto/agregar_producto', {
    method: 'POST',
    body: formData
  })
  .then(function(response) {
    // Lógica para manejar la respuesta del servidor
    if (response.ok) {
      // Postre agregado correctamente
      // Actualizar la página para reflejar los cambios
      location.reload();
    } else {
      // Error al agregar el postre
      console.error('Error al agregar el postre');
    }
  })
  .catch(function(error) {
    // Lógica para manejar errores
    console.error('Error en la solicitud:', error);
  });
});

// Agregar evento al enviar el formulario de agregar paleta
agregarPaletaForm.addEventListener('submit', function(event) {
  event.preventDefault();

  // Obtener los valores del formulario
  var nombrePaleta = document.getElementById('nombre-paleta').value;
  var archivoPaleta = document.getElementById('archivo-paleta').files[0];

  // Crear objeto FormData para enviar los datos del formulario
  var formData = new FormData();
  formData.append('nombre', nombrePaleta);
  formData.append('imagen', archivoPaleta);
  formData.append('tipo_producto', 'paletas');

  // Realizar la solicitud al backend para agregar la paleta
  fetch(URL + 'producto/agregar_producto', {
    method: 'POST',
    body: formData
  })
  .then(function(response) {
    // Lógica para manejar la respuesta del servidor
    if (response.ok) {
      // Paleta agregada correctamente
      // Actualizar la página para reflejar los cambios
      location.reload();
    } else {
      // Error al agregar la paleta
      console.error('Error al agregar la paleta');
    }
  })
  .catch(function(error) {
    // Lógica para manejar errores
    console.error('Error en la solicitud:', error);
  });
});

// código para carrusel sabores
var carouselSabores = document.getElementById('carousel-sabores');
var slidesSabores = carouselSabores.getElementsByClassName('slide');
var currentSlideIndex = 0;

function showSlide(index) {
  // Ocultar todas las diapositivas
  for (var i = 0; i < slidesSabores.length; i++) {
    slidesSabores[i].classList.remove('active');
  }

  // Mostrar la diapositiva actual
  slidesSabores[index].classList.add('active');
}

function nextSlide() {
  currentSlideIndex++;
  if (currentSlideIndex >= slidesSabores.length) {
    currentSlideIndex = 0;
  }
  showSlide(currentSlideIndex);
}

function prevSlide() {
  currentSlideIndex--;
  if (currentSlideIndex < 0) {
    currentSlideIndex = slidesSabores.length - 1;
  }
  showSlide(currentSlideIndex);
}

// Mostrar la primera diapositiva al cargar la página
showSlide(currentSlideIndex);

// Agregar eventos para avanzar y retroceder en el carrusel
carouselSabores.addEventListener('click', nextSlide);

// // Obtener las imágenes desde el servidor Flask y mostrarlas en el carrusel
// {% for sabor in sabores %}
// var image = new Image();
// image.onload = function() {
//   // Crear una nueva diapositiva y establecer la imagen cargada como su contenido
//   var slide = document.createElement('div');
//   slide.classList.add('slide');
//   slide.appendChild(this);

//   // Agregar la diapositiva al carrusel
//   carouselSabores.appendChild(slide);

//   // Actualizar la lista de diapositivas
//   slidesSabores = carouselSabores.getElementsByClassName('slide');
// };

// // Obtener la ruta de acceso de la imagen desde el servidor Flask
// var imageUrl = "{{ url_for('static', filename='uploads/' ~ sabor.id ~ '.jpg') }}";

// // Establecer la ruta de acceso de la imagen en la propiedad src de la imagen
// image.src = imageUrl;
// {% endfor %}