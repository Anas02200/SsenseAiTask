const mymap = L.map('mapid', {drawControl: true});
const access = L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox.streets',
    accessToken: 'pk.eyJ1IjoiYW5hczAwMCIsImEiOiJjazNidWR4NW8wOXY2M2Z1aXdlOXBwdHRvIn0.P3Zqj5LRcWyQF7vTJ9-IzQ'
})
const searchControl = L.esri.Geocoding.geosearch()
const results = L.layerGroup()
const geocodeService = L.esri.Geocoding.geocodeService();
const drawnItems = new L.FeatureGroup();
const drawControl = new L.Control.Draw({
    draw:{polygon: false,
        marker: false,
        circlemarker: false,
        rectangle: false,
        circle: false,
        polyline:false
    },
  edit: {
    featureGroup: drawnItems
  }
});

var popup = L.popup();

function onMapClick(e) {

    document.getElementById('Data').value = e.latlng
    document.getElementById('event').value = e.type;
    document.getElementById('CoordinatesOnScreen').value = e.containerPoint;
    geocodeService.reverse().latlng(e.latlng).run(function (error, result) {
        if (error) {
            return;
        }
        document.getElementById('placeName').value = result.address.Match_addr;

    });


}

function onDraw(e) {

    var type = e.layerType,
        layer = e.layer;
    if (type === 'polygon') {
        // Do marker specific actions
        document.getElementById('Data').value = e.layer.editing._poly.editing.latlngs[0];


    }
    if (type == 'rectangle') {
        document.getElementById('Data').value = e.layer.editing._shape._latlngs[0];
    }
    document.getElementById('placeName').value = e.layerType

    document.getElementById('event').value = 'Draw';
    document.getElementById('CoordinatesOnScreen').value = 'none';


    drawnItems.addLayer(layer);
}

function onSearch(data) {
    results.clearLayers();
    for (var i = data.results.length - 1; i >= 0; i--) {
        results.addLayer(L.marker(data.results[i].latlng));
    }
    document.getElementById('Data').value = data.latlng;

    document.getElementById('event').value = 'manual search';
    document.getElementById('CoordinatesOnScreen').value = 'none';

}
//logic that creates the map
function createMap(latitude,longitude) {
    mymap.setView([latitude, longitude], 13);
        access.addTo(mymap);
        L.marker([latitude, longitude]).addTo(mymap);
        mymap.addControl(drawControl);
        mymap.addLayer(drawnItems);
        searchControl.addTo(mymap);
        results.addTo(mymap);
        searchControl.on('results', onSearch)
        mymap.on('click', onMapClick);
        mymap.on(L.Draw.Event.CREATED, onDraw)

}
//must activate geolocation so the map is centered on your postion
if ("geolocation" in navigator) {
    navigator.geolocation.getCurrentPosition(position => {
        longitude = position.coords.longitude;
        latitude = position.coords.latitude;
        //we ada layers to the map
        createMap(latitude,longitude)



    },error=>{
        alert('couldnt get position please activate geolocation');
        createMap(51.505, -0.09)

    })

    ;

}




