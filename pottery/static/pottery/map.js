getMap = function () {    
    let tfAttr = 'Maps &copy; <a href="https://www.thunderforest.com">Thunderforest</a>, Data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap contributors</a>';
    let mbAttr = 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>';
    let tfUrl = 'https://tile.thunderforest.com/landscape/{z}/{x}/{y}.png?apikey='+ thsu;
    let mbUrl = 'https://api.mapbox.com/styles/v1/mapbox/streets-v11/tiles/{z}/{x}/{y}?access_token='+ mbsu;
    let mbSUrl = 'https://api.mapbox.com/styles/v1/mapbox/satellite-v9/tiles/{z}/{x}/{y}?access_token=' + mbsu;



    let landscape = L.tileLayer(tfUrl, {maxZoom: 22, attribution: tfAttr});
    let streets = L.tileLayer(mbUrl, {tileSize: 512, zoomOffset: -1, attribution: mbAttr});
    let satellite = L.tileLayer(mbSUrl, {tileSize: 512, zoomOffset: -1, attribution: mbAttr});
    let u = L.featureGroup();
    let s = L.featureGroup();
    let sb = L.featureGroup();
    let pa = L.featureGroup();
    let sr = L.featureGroup();
    let srb = L.featureGroup();
    let pr = L.featureGroup();
    let lbu = L.featureGroup();
    let po = L.featureGroup();
    let rg = L.featureGroup();
    let pc = L.featureGroup();
    let sbu = L.featureGroup();

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
        center: mapcentre,
        zoom: 4,
        layers: [streets, u, s, sb, srb, sr, sbu, pr, lbu, pa, po, pc, rg]
    });

    let baseLayers = {
        'Landscape': landscape,
        'Satellite': satellite,
        'Streets': streets
    };

    for (var i = 0; i < siteNames.length; i += 1) {
        sitename = siteNames[i];
        // sitelink = siteLinks[i];
        // complex = "<a href=" +sitelink+">"+sitename+ "</a>" + siteFabrics[i];
        complex = sitename + " " + siteFabrics[i];
        // if (siteColour[i] == 1) {
            // marker = L.marker([siteLat[i],siteLng[i]],{icon: potIcon, title: sitename}).addTo(u);
            // marker = L.marker([siteLat[i],siteLng[i]],{icon: potIcon, title: sitename, link: sitelink}).bindPopup(complex).on("click", markerOnClick).addTo(full);
        // } else if (siteColour[i] == 2) {
            // marker = L.marker([siteLat[i],siteLng[i]],{icon: potIconC, title: sitename, link: sitelink}).bindPopup(complex).on("click", markerOnClick).addTo(s);
        // }  else {
            // marker = L.marker([siteLat[i],siteLng[i]],{icon: potIconB, title: sitename, link: sitelink}).bindPopup(complex).on("click", markerOnClick).addTo(sb);
            marker = L.marker([siteLat[i],siteLng[i]],{icon: potIcon, title: sitename}).bindPopup(complex).addTo(u);
        // }
        } 
        let overlays = {}
        
        if (siteview) { 
            overlays = {
            'Unknown': u,
            'Spiral': s,
            'PA': pa
            }; 
        } else {
            overlays = {
                'Selected': u
                }; 
        }
        var layerControl = L.control.layers(baseLayers, overlays).addTo(map);
   
  }

//   function markerOnClick(e) {
//     targetSite = this.options.title;
//     targetLink = this.options.link;
//     document.getElementById("targetSite").innerHTML = "Site selected: <a href=" +targetLink+">"+targetSite+ "</a>." ; 
        
// }

