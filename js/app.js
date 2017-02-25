/**
 * Initialization function
 */

function init() {
	// Bind click event for 'Insert Loyalty Class' button
	document.getElementById('loyalty').addEventListener('click', function() {
		$.get('insertClass?type=loyalty', function(data) {
			console.log(data);
		});
	});
	document.getElementById('giftcard').addEventListener('click', function() {
		$.get('insertClass?type=giftcard', function(data) {
			console.log(data);
		});
	});
	document.getElementById('offer').addEventListener('click', function() {
		$.get('insertClass?type=offer', function(data) {
			console.log(data);
		});
	});
}

$(window).ready(function() {
	init();
});
