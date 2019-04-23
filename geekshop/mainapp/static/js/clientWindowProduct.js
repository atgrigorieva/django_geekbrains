					function show(id) {
						document.getElementById(id).style.display='block';
					}
					function hide(id) {
						document.getElementById(id).style.display='none';
					}
					$(function() {
						$('#id_test.characteristiks1_1 li a').bind('click', function(event) {
							$('#id_test.characteristiks1_1 li a').removeClass('active');
							$(this).toggleClass('active');

						});
					});
					$(document).ready(function(){
						$(".button").click(function(){

						$(this).toggleClass("active");
						$(".active").removeClass("active"); return false;
	});
});