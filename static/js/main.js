function ajaxGet(url, data, successCallback, errorCallback) {
	$.ajax({
		method: "GET",
		data: data,
		url: url,
		success: successCallback,
		error: errorCallback
	});
}

function ajaxPost(url, data, successCallback, errorCallback) {
	$.ajax({
		method: "POST",
		contentType: "application/json; charset=utf-8",
		data: JSON.stringify(data),
		dataType: "json",
		url: url,
		success: successCallback,
		error: errorCallback
	});
}

function signOut() {
	var auth2 = gapi.auth2.getAuthInstance();
	auth2.signOut().then(function () {
		console.log('User signed out.');
	});
}