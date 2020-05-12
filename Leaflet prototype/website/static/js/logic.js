// // Link for the earthquakes  
const raceTracks = "static/js/race_tracks.json"


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
    Earthquakes: earthquakes
  };

  // Create a baseMaps object to hold the lightmap layer
  let baseMaps = {
   Light: lightmap,
   Dark: darkmap,
   Satellite: satellitemap
  };

  // creating the map
  let map = L.map("map",{
    center: [34.0522, -118.2437],
    zoom: 5,
    layers: [satellitemap, earthquakes]
  });

  L.control.layers(baseMaps, overlayMaps, {
    collapsed: false
  }).addTo(map);
}




d3.json(raceTracks, function createMarkers(response){
  response.forEach(i => console.log(i))
  raceMarkers = [];
  response.forEach(i => {
    let raceMarker = L.marker([i.lat, i.lon])
      .bindPopup(i.nameLong);
    raceMarkers.push(raceMarker)
  });

  createMap(L.layerGroup(raceMarkers));

})
