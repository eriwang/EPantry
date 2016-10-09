function getItemData() {
	ajaxGet("/pantry", 
			{},
			function(data, textStatus, jqXHR) {
				console.log(data);
			},
			function(jqXHR, textStatus, errorThrown) {
				console.log(errorThrown);
			}
	);
}