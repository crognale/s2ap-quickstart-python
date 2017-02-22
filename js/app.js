/**
 * Initialization function
 */

function init() {
	// Bind click event for 'Insert Loyalty Class' button
	document.getElementById('loyalty').addEventListener('click', function() {
		$.get('insertClass', function(data) {
			console.log(data);
		});
	});
}

$(window).ready(function() {
	init();
});
