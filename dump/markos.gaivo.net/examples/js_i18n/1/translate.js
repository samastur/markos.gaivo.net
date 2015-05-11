/*
 * i18n functions
 */
function stripStr(str) {
	return str.replace(/^\s*/, "").replace(/\s*$/, "");
}

// Multiline strip
function stripStrML(str) {
	// Split because m flag doesn't exist before JS1.5 and we need to
	// strip newlines anyway
	var parts = str.split('\n');
	for (var i=0; i<parts.length; i++)
		parts[i] = stripStr(parts[i]);

	// Don't join with empty strings, because it "concats" words
	return parts.join(" ");
}

// Return translation, if translation dictionary exists and has a translation.
function _(str) {
	if (i18nDict && i18nDict[str])
		return i18nDict[str];
	return str;
}
