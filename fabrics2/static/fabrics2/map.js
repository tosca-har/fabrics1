getMap = function () {    
    let tfAttr = 'Maps &copy; <a href="https://www.thunderforest.com">Thunderforest</a>, Data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap contributors</a>';
    let mbAttr = 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>';
    let tfUrl = 'https://tile.thunderforest.com/landscape/{z}/{x}/{y}.png?apikey=886d35daaac64cee8d4f10017e008188';
    let mbUrl = 'https://api.mapbox.com/styles/v1/mapbox/streets-v11/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoidG9zY2FoYXJkeSIsImEiOiJja3lkeGpibHkwNmg1MnhwaDFodmxkZjZ5In0.UUhry4TtS7E16n4Y5ommsQ';
    let mbSUrl = 'https://api.mapbox.com/styles/v1/mapbox/satellite-v9/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoidG9zY2FoYXJkeSIsImEiOiJja3lkeGpibHkwNmg1MnhwaDFodmxkZjZ5In0.UUhry4TtS7E16n4Y5ommsQ';

    let landscape = L.tileLayer(tfUrl, {maxZoom: 22, attribution: tfAttr});
    let streets = L.tileLayer(mbUrl, {tileSize: 512, zoomOffset: -1, attribution: mbAttr});
    let satellite = L.tileLayer(mbSUrl, {tileSize: 512, zoomOffset: -1, attribution: mbAttr});

    var potIcon = L.icon({
        iconUrl: picon,
        iconSize: [15, 20]
    });

    var potIconB = L.icon({
        iconUrl: bicon,
        iconSize: [15, 20]
    });

    var potIconC = L.icon({
        iconUrl: ricon,
        iconSize: [15, 20]
    });
        
    let map = L.map('map', {
        center: [-4.5, 150],
        zoom: 4,
        layers: [landscape, streets, satellite]
    });

    let baseLayers = {
        'Landscape': landscape,
        'Satellite': satellite,
        'Streets': streets
    };

    for (var i = 0; i < siteNames.length; i += 1) {
        sitename = siteNames[i];
        sitelink = siteLinks[i];
        complex = "<a href=" +sitelink+">"+sitename+ "</a>" + siteFabrics[i];
        marker = L.marker([siteLat[i],siteLng[i]],{icon: potIcon, title: sitename, link: sitelink}).bindPopup(complex).on("click", markerOnClick).addTo(map);
    }  
    var layerControl = L.control.layers(baseLayers).addTo(map);
   
  }

  function markerOnClick(e) {
    targetSite = this.options.title;
    targetLink = this.options.link;
    document.getElementById("targetSite").innerHTML = "<a href=" +targetLink+">"+targetSite+ "</a>" ; 
        
}

