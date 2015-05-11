var intl;
var _;

function trans() {
	alert(_("Display translated string"));
}

function untrans() {
	alert(_("Display untranslated string"));
}

function init() {
	intl = new i18n(i18nDict);
	intl.translateNodes();
	_ = function (str) { return intl.translate(str); };
}

window.onload = init;
