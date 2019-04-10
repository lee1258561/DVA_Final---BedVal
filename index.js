function getPriceDemain(){
	var proxyUrl = 'https://nameless-sands-81392.herokuapp.com/';
	let variables = {
		longitude: document.getElementById("longitude").value,
		latitude: document.getElementById("latitude").value,
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

	Promise.all([pricePromise, demainPromise])
	.then((data) => {
		console.log(data);
	})

}