function trans() {
	alert(_("Display translated string"));
}

function untrans() {
	alert(_("Display untranslated string"));
}

function init() {
	translateNodes();
}

window.onload = init;
