var ww = document.body.clientWidth;
		function newMyWindow(e) {
			var h = 500,
			w = 650;
			window.open(e, '', 'scrollbars=1,height='+Math.min(h, screen.availHeight)+',width='+Math.min(w, screen.availWidth)+',left='+Math.max(0, 
			(screen.availWidth - w)/2)+',top='+Math.max(0, (screen.availHeight - h)/2));
		}

		var ww = document.body.clientWidth;

		$(document).ready(function() {
			$("#nav7 li a").each(function() {
				if ($(this).next().length > 0) {
					$(this).addClass("parent");
				};
			})
			
			$(".toggleMenu").click(function(e) {
				e.preventDefault();
				$(this).toggleClass("active");
				$("#nav7").toggle();
			});
			$("#id_test.characteristiks1_1 li a").each(function() {
				if ($(this).next().length > 0) {
					$(this).addClass("parent");
				};
			})
			
			$(".toggleMenu1").click(function(e) {
				e.preventDefault();
				$(this).toggleClass("active");
				$("#id_test.characteristiks1_1").toggle();
			});
			
			
			
			$("#nav_charact li a").each(function() {
				if ($(this).next().length > 0) {
					$(this).addClass("parent");
				};
			})
			
			$(".toggleMenu2").click(function(e) {
				e.preventDefault();
				$(this).toggleClass("active");
				$("#nav_charact.toggleMenu2-nav_charact").toggle();
			});
			
			adjustMenu();
			if (ww < 1081) {
			$("#id_test.characteristiks1_1 li").click(function() {
				$("#id_test.characteristiks1_1").hide();; 
			});
			$("#nav_charact li").click(function() {
				$("#nav_charact.toggleMenu2-nav_charact").hide();; 
			});
			}
		})

		$(window).bind('resize orientationchange', function() {
			ww = document.body.clientWidth;
			adjustMenu();
		});

		var adjustMenu = function() {
			if (ww < 1081) {
				$(".toggleMenu").css("display", "inline-block");
				if (!$(".toggleMenu").hasClass("active")) {
					$("#nav7").hide();
				} else {
					$("#nav7").show();
				}
				$("#nav7 li").unbind('mouseenter mouseleave');
				$("#nav7 li a.parent").unbind('click').bind('click', function(e) {
					// must be attached to anchor element to prevent bubbling
					e.preventDefault();
					$(this).parent("li").toggleClass("hover");
				});
				
				$(".toggleMenu1").css("display", "inline-block");
				if (!$(".toggleMenu1").hasClass("active")) {
					$("#id_test.characteristiks1_1").hide();
				} else {
					$("#id_test.characteristiks1_1").show();
				}
				$("#id_test.characteristiks1_1 li").unbind('mouseenter mouseleave');
				$("#id_test.characteristiks1_1 li a.parent").unbind('click').bind('click', function(e) {
					// must be attached to anchor element to prevent bubbling
					e.preventDefault();
					$(this).parent("li").toggleClass("hover");

				});
				
				
				$(".toggleMenu2").css("display", "inline-block");
				if (!$(".toggleMenu2").hasClass("active")) {
					$("#nav_charact.toggleMenu2-nav_charact").hide();
				} else {
					$("#nav_charact.toggleMenu2-nav_charact").show();
				}
				$("#nav_charact.toggleMenu2-nav_charact li").unbind('mouseenter mouseleave');
				$("#nav_charact.toggleMenu2-nav_charact li a.parent").unbind('click').bind('click', function(e) {
					// must be attached to anchor element to prevent bubbling
					e.preventDefault();
					$(this).parent("li").toggleClass("hover");
				});
				
				
			} 
			else if (ww >= 1081) {
				$(".toggleMenu").css("display", "none");
				$("#nav7").show();
				$("#nav7 li").removeClass("hover");
				$("#nav7 li a").unbind('click');
				$("#nav7 li").unbind('mouseenter mouseleave').bind('mouseenter mouseleave', function() {
					// must be attached to li so that mouseleave is not triggered when hover over submenu
					$(this).toggleClass('hover');
				});
				
				$(".toggleMenu1").css("display", "none");
				$("#id_test.characteristiks1_1").show();
				$("#id_test.characteristiks1_1 li").removeClass("hover");
				$("#id_test.characteristiks1_1 li a").unbind('click');
				$("#id_test.characteristiks1_1 li").unbind('mouseenter mouseleave').bind('mouseenter mouseleave', function() {
					// must be attached to li so that mouseleave is not triggered when hover over submenu
					$(this).toggleClass('hover');
					
				});
				
				
				$(".toggleMenu2").css("display", "none");
				$("nav_charact.toggleMenu2-nav_charact").show();
				$("#nav_charact.toggleMenu2-nav_charact li").removeClass("hover");
				$("#nav_charact.toggleMenu2-nav_charact li a").unbind('click');
				$("#nav_charact.toggleMenu2-nav_charact li").unbind('mouseenter mouseleave').bind('mouseenter mouseleave', function() {
					// must be attached to li so that mouseleave is not triggered when hover over submenu
					$(this).toggleClass('hover');
				});
						
			}
			
		}