(function () {
	var rich = false; // Globally private variable :)

	function toggleVisible() {
		var myAnim, h, f;
		var dl = document.getElementsByTagName("dl")[0];
		if (rich) {
			if (dl.offsetHeight) {
				h = 0; f = 48;
			} else {
				h = 48; f = 0;
			}
			myAnim = new YAHOO.util.Anim(dl, { 
				    height: { from: f, to: h , unit: "em"}  
				    }, 0.6, YAHOO.util.Easing.easeOut); 
			myAnim.animate();
		} else {
			dl.className = (dl.className) ? null : "noshow";
		}
	}

	window.onload = function () {
		// Are we in rich mode?
		var el, yui = ["utilities", "animation" ];
		var scr = document.getElementsByTagName("script");
		var head = document.getElementsByTagName("head")[0];

		for(var i=0;i<scr.length;i++) {
			if (scr[i].src && scr[i].src.match("rswitch")) {
				rich = true;

				// Import YUI
				for(var j=0;j<yui.length;j++) {
					el = document.createElement("script");
					el.type = "text/javascript";
					el.src = "yui/"+yui[j]+"/"+yui[j]+".js";
					head.appendChild(el);
				}
				break;
			}
		}
		document.getElementsByTagName("input")[0].onclick = toggleVisible;
	}
})();
