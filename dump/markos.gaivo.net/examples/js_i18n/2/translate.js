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
	// And strip again
	return stripStr(parts.join(" "));
}

// Return translation, if translation dictionary exists and has a translation.
function _(str) {
	if (i18nDict && i18nDict[str])
		return i18nDict[str];
	return str;
}

// Change to entity representation non-ASCII characters
function toEntity(str) {
	var newstr = "";
	for (var i=0;i<str.length; i++)
		if (str.charCodeAt(i) > 128)
			newstr += "&#"+str.charCodeAt(i)+";";
		else
			newstr += str[i];
	return newstr;
}

function translateNodes() {
	var nodes = document.getElementsByTagName("*");
	for (var i=0;i<nodes.length;i++)
		if (nodes[i].className.match("i18n")) {
			var orig = stripStrML(nodes[i].innerHTML);
			var transl = _(orig);

			// If translation not found, try again with
			// entity representation
			if (transl == orig) transl = _(toEntity(orig));
			nodes[i].innerHTML = transl;
		}
}
