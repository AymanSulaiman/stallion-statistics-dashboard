 const raceTracks = "static/js/race_tracks.json"

var greenIcon = L.icon({
  iconUrl: 'https://i.imgur.com/A0ohNXt.png',
  shadowUrl: '',
  iconSize:     [38, 38], // size of the icon
  // shadowSize:   [50, 64], // size of the shadow
  iconAnchor:   [22, 22], // point of the icon which will correspond to marker's location
  shadowAnchor: [4, 4],  // the same for the shadow
  popupAnchor:  [-3, -3] // point from which the popup should open relative to the iconAnchor
});

function createMap(earthquakes){
  // Light map
  let lightmap = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/light-v9/tiles/256/{z}/{x}/{y}?access_token={accessToken}", {
    attribution: "Map data &copy; <a href=\"http://openstreetmap.org\">OpenStreetMap</a> contributors, <a href=\"http://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"http://mapbox.com\">Mapbox</a>",
    maxZoom: 18,
    id: "mapbox.light",
    accessToken: APIKEY
  });
  
  // Dark Map
  let darkmap = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
    attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
    maxZoom: 18,
    id: "mapbox.dark",
    accessToken: APIKEY
  });
  
  // Satellite Map
  let satellitemap = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
    attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
    maxZoom: 18,
    id: "mapbox.satellite",
    accessToken: APIKEY
  });
  
  
  // Creating the overlay map
  let overlayMaps = {
    "Races Tracks": earthquakes
  };

  // Create a baseMaps object to hold the lightmap layer
  let baseMaps = {
   Light: lightmap,
   Dark: darkmap,
   Satellite: satellitemap
  };

  // creating the map
  let map = L.map("map",{
    center: [34.4840, -93.0592],
    zoom: 3,
    layers: [satellitemap, earthquakes]
  });

  L.control.layers(baseMaps, overlayMaps, {
    collapsed: true
  }).addTo(map);
}




d3.json(raceTracks, function createMarkers(response){
  response.forEach(i => console.log(i))
  raceMarkers = [];
  response.forEach(i => {
    let raceMarker = L.marker([i.lat, i.lon], {icon: greenIcon})
      .bindPopup(`${i.nameLong}<br><a href = ${i.url} target = _blank>${i.nameShort}</a>`);
    raceMarkers.push(raceMarker)
  });

  createMap(L.layerGroup(raceMarkers));

})

function initMap() {
  // The location of Uluru
  var uluru = {lat: -25.344, lng: 131.036};
  // The map, centered at Uluru
  var map = new google.maps.Map(
      document.getElementById('map'), {zoom: 4, center: uluru});
  // The marker, positioned at Uluru
  var marker = new google.maps.Marker({position: uluru, map: map});
}

// *****************************************************************************
$(document).ready(function() {
  $('.sideMenuToggler').on('click', function() {
    $('.wrapper').toggleClass('active');
  });

  var adjustSidebar = function() {
    $('.sidebar').slimScroll({
      height: document.documentElement.clientHeight - $('.navbar').outerHeight()
    });
  };

  adjustSidebar();
  $(window).resize(function() {
    adjustSidebar();
  });
});