/**
 * Initialization function
 */

function init() {
	//Call to insert class
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
