// adaptado de https://stackoverflow.com/questions/3059044/google-maps-js-api-v3-simple-multiple-marker-example
let locations = [
    ["Álvarez Jonte 2855", -34.607932182918, -58.48357036354731],
    ["Sgto. Cabral 2581", -34.65875913761088, -58.53763947938699],
    ["Av. Rivadavia 9899" , -34.63718023183219, -58.5047701655798],
    ["Formosa 102", -34.619444191636056, -58.43122285377091]
  ];
  
  let map = new google.maps.Map(document.getElementById('map'), {
    zoom: 10,
    center: new google.maps.LatLng(-34.603941801889185, -58.38148626665485),
    mapTypeId: google.maps.MapTypeId.ROADMAP
  });
  
  let infowindow = new google.maps.InfoWindow();

  let marker, i;
  
  for (i = 0; i < locations.length; i++) {  
    marker = new google.maps.Marker({
      position: new google.maps.LatLng(locations[i][1], locations[i][2]),
      map: map
    });
    
    google.maps.event.addListener(marker, 'click', (function(marker, i) {
      return function() {
        infowindow.setContent(locations[i][0]);
        infowindow.open(map, marker);
      }
    })(marker, i));
  }

// // Variables globales
// let map
// let marker
// // Geolocalización
// let watchId
// let Geolocalización


// function initMap(){
//     //Álvarez Jonte 2855 -34.607932182918, -58.48357036354731
//     //Sgto. Cabral 2581 -34.65875913761088, -58.53763947938699
//     //Av. Rivadavia 9899 -34.63718023183219, -58.5047701655798
//     //Formosa 102 -34.619444191636056, -58.43122285377091
//     const dictLating = {
//         "Álvarez Jonte 2855": {lat: -34.607, lng: -58.483},
//         "Sgto. Cabral 2581" : {lat: -34.658, lng: -58.537},
//         "Av. Rivadavia 9899": {lat: -34.637, lng: -58.504},
//         "Formosa 102"       : {lat: -34.619, lng: -58.431}
//     }
//     for (const [key, value] of Object.entries(dictLating)) {
//         map = new google.maps.Map(document.getElementById('map'), {
//             center: value,
//             zoom: 15    
//         });
//         marker = new google.maps.Marker({
//             position: value,
//             map,
//             title: key
//         });
//     }
// }

//     map = new google.maps.Map(document.getElementById('map'), {
//         center: myLating,
//         zoom: 12
//     });
//     marker = new google.maps.Marker({
//         position: myLating,
//         map,
//         title: "Álvarez Jonte 2855"
//     });
// }
// map = new google.maps.Map(document.getElementById('map'), {
    // center: {lat: -34.397, lng: 150.644},
    // zoom: 8
//   });