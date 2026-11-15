// Light/dark switch, following
// https://lea.verou.me/blog/2026/dark-mode-toggles/
//
// Pages follow the OS colour scheme. The switch highlights the theme on
// screen; choosing the other one stores it as an override ("light" or "dark"
// in localStorage.theme) if it differs from the OS preference, or removes the
// override if it matches, so the page follows the OS again. An override is
// never dropped just because the OS later switches to the same scheme.
//
// The override lives in <meta name="color-scheme">, which home.css maps to the
// light or dark colours; head.html applies a stored one before the first paint.
(function () {
	var meta = document.querySelector('meta[name="color-scheme"]'),
		group = document.querySelector('.theme-switch'),
		buttons = group.querySelectorAll('button'),
		system = matchMedia('(prefers-color-scheme: dark)');

	function valid(theme) {
		return theme === 'light' || theme === 'dark' ? theme : null;
	}
	function systemTheme() {
		return system.matches ? 'dark' : 'light';
	}
	function shownTheme() {
		return valid(meta.content) || systemTheme();
	}

	function update() {
		var shown = shownTheme(), os = systemTheme(), i, button;
		for (i = 0; i < buttons.length; i++) {
			button = buttons[i];
			button.setAttribute('aria-pressed', button.value === shown);
			button.title = button.getAttribute('aria-label') +
				(button.value === os ? ' (system default)' : '');
		}
	}
	function apply(theme) {
		meta.content = valid(theme) || 'light dark';
		update();
	}

	group.addEventListener('click', function (e) {
		var button = e.target.closest('button'),
			to = button && button.value,
			override = to === systemTheme() ? null : to;
		if (!to || to === shownTheme()) {
			return;
		}
		try {
			if (override) {
				localStorage.setItem('theme', override);
			} else {
				localStorage.removeItem('theme');
			}
		} catch (err) {
			// Storage blocked: switch this page anyway.
		}
		apply(override);
	});
	// Keep other open tabs in sync, and the highlight in sync with the OS.
	addEventListener('storage', function (e) {
		if (e.key === 'theme' || e.key === null) {
			apply(e.newValue);
		}
	});
	system.addEventListener('change', update);

	update();
	group.hidden = false;
})();
