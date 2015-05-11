jQuery(function ($) {
	function themeSwitch() {
		var theme = '';

		function storage_support() {
			try {
				return 'localStorage' in window && window['localStorage'] !== null;
			} catch (e) {
				return false;
			}
		}

		$('<li class="theme"><div>Theme: </div><a href="#" class="light"></a><a href="#" class="dark"></a></li>')
			.appendTo(".post footer ul, .colophon ul");

		$(".theme .light, .theme .dark").click(function (e) {
			e.stopPropagation(); e.preventDefault();

			$('link[title="Dark theme"]').attr("disabled", this.className === "dark" ? false : true);

			if (storage_support()) {
				localStorage['theme'] = this.className;
			}
		});

		// Read from local storage if it exists and set to its value
		if (storage_support() && 'theme' in localStorage) {
			theme = localStorage['theme'];
			$('link[title="Dark theme"]').attr("disabled", theme === "dark" ? false : true);
		}

		// Save settings on page unload (to support browser stylesheet switching)
		$(window).bind("unload", function (e) {
			if (storage_support()) {
				localStorage['theme'] = $('link[title="Dark theme"]').attr("disabled") ? "" : "dark";
			}
		});
	}

	// Hide comment form. Should open on request
	$(".comment-form ul").hide();
	$(".comment-form h2").wrapInner('<a href="#comment-form" class="post-comment">');
	$(".post-comment").click(function (e) {
		$(".comment-form ul").show();
		$(".comment-form h2").html($(".comment-form h2 a").html());
	});


	// Autogrow textarea
	$(".comment-form textarea").keyup(function (e) {
		if (this.scrollHeight > this.clientHeight) {
			this.rows += 5;
		}
	});

	// Add theme switcher
	themeSwitch();
});
