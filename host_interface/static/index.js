var mymap = L.map('mapid').setView([37.75, -122.42], 13);

//Add a layer

L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: 'Map data &copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(mymap);

//Popup of the estimations
// ****To do: link the estimation value to the SetContent()

// var popup = L.popup({width:800, offset:[0,0]})
//     .setContent('The suggested price is <br />The estimated number of monthly booking is');

//click to put a marker

var marker = {};

mymap.on('click', function(e){
  	var coord = e.latlng;
  	//console.log(coord);
   	if (marker != undefined) {
    	mymap.removeLayer(marker);
    };

  	marker = L.marker(coord, {} ).addTo(mymap);
  
	//get the coordinates for use later
	var latlng1 = marker.getLatLng();
	var latlng2 = marker.toGeoJSON();
	document.getElementById("latitude").value = latlng1.lat;
	document.getElementById("longitude").value = latlng1.lng;
	//**** TO do: Search for the transportation near the pindown

 
});


async function getPriceDemain(){
	var proxyUrl = 'https://nameless-sands-81392.herokuapp.com/';
	let lat = document.getElementById("latitude").value;
	let lng = document.getElementById("longitude").value;
	let variables = {
		longitude: lng,
		latitude: lat,
		avgAvail: document.getElementById("avgAvail").value,
		accommodates: document.getElementById("accommodates").value,
		beds: document.getElementById("beds").value,
		reviewScore: document.getElementById("reviewScore").value,
		listingCount: document.getElementById("listingCount").value,
		apt: document.getElementById("apt").checked ? 1 : 0,
		house: document.getElementById("house").checked ? 1 : 0,
		entire: document.getElementById("entire").checked ? 1 : 0,
		realbed: document.getElementById("realbed").checked ? 1 : 0,
		instantBook: document.getElementById("instantBook").checked ? 1 : 0,
		phoneVerification: document.getElementById("phoneVerification").checked ? 1 : 0,
		wifi: document.getElementById("wifi").checked ? 1 : 0,
		superHost: document.getElementById("superHost").checked ? 1 : 0,
		identityVerified: document.getElementById("identityVerified").checked ? 1 : 0,
		hasPic: document.getElementById("hasPic").checked ? 1 : 0,
	}
	//console.log(variables);
	let pricePromise = fetch("http://localhost:8080/price", {
            method: "POST",
            headers: {
            	'Origin': "http://localhost:8080/",
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(variables),
        }).then(response => response.json());


	let demainPromise = fetch("http://localhost:8080/demain", {
            method: "POST",
            headers: {
            	'Origin': "http://localhost:8080/",
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(variables),
        }).then(response => response.json());

	let data = await Promise.all([pricePromise, demainPromise]);

	//data contains the price and demain 
	//structure: data = [
	// 	{
	// 		price: ...,
	// 	},
	// 	{
	// 		demain: ...
	// 	}
	// ]
	console.log(data);

	if (marker != undefined) {
    	mymap.removeLayer(marker);
    };
  	marker = L.marker([lat, lng], {} ).addTo(mymap)
  		.bindPopup('The suggested price is ' + data[0].price + 
  				   '<br />The estimated number of monthly booking is ' + data[1].demain)
    	.openPopup();


}