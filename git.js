function phoneTiclookup(val) {
	var result = "";


	var lookup = {
		"alpha": "Adams",
		"Bravo": "boston",
		"Charlie": "Chicago",
		"Delta": "Denver",
		"Echo": "Easy",
		"Foxtrot": "Frank",
	};

	result = lookup[val];
	return result;
}

// change this value to test
console.log(phoneTiclookup(Charlie));
