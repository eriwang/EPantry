function onSignIn(googleUser) {
	var profile = googleUser.getBasicProfile();
	console.log('ID: ' + profile.getId()); // Do not send to your backend! Use an ID token instead.
	console.log('Name: ' + profile.getName());
	console.log('Image URL: ' + profile.getImageUrl());
	console.log('Email: ' + profile.getEmail());

	signInPostData = {
		id_token: googleUser.getAuthResponse().id_token,
		username: profile.getEmail()
	};

	ajaxPost("/login", 
			signInPostData, 
			function(data, textStatus, jqXHR) {
				console.log("Login successful.");
				// implement window load when done
			},
			function(jqXHR, textStatus, errorThrown) {
				console.log(errorThrown);
			}
	);
}