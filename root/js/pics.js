// RPC functions
function MarelaRPC() {
	this.ID = "";
	var rpc = this;

	this.call = function (method, params, newurl) {
			var url = "http://www.marela.si/as/rest/?rtype=json";
			var multi = false;
			var callURL;

			if (newurl) url = newurl;

			// Marela allows method pipelining. Check if this is happening and act
			// accordingly.
			var noMethod = method.search(",");
			switch(noMethod) {
				case 0:
					alert("Syntax error: methods start with empty name");
					return;
				case -1: // Just one method
					callURL = url + "&method="+method;
					break;
				default:
					callURL = url + "&methods="+method;
					multi = true;
			};

			var scr = document.createElement('script');
			scr.type = 'text/javascript';

			// Find non-used ID
			var tmpId;
			do {
				tmpId = "rpc"+Math.round(Math.random()*10000);
				// Check that there's no element or function using this ID
			} while (document.getElementById(tmpId) || window["fn"+tmpId]);
			scr.id = tmpId;

			// Use this ID also for callback function name
			callURL += "&json_func=fn"+tmpId+"(%s)";
			window["fn"+tmpId] = this._handle;

			for (key in params) {
				// In multi-method call check that parameters are of correct form
				if (multi && params[key].search(".")<=0) {
					alert("Syntax error: Malformed parameters in multi-method call");
					return;
				}
				callURL += "&"+key+"="+params[key];
			}
			scr.src = callURL;
			document.getElementsByTagName('head')[0].appendChild(scr);

			this.ID = scr.id;
		}

	this.callback = function (result) {}

	this._handle = function (result) {
		// We can delete superfluous script element and function
		var node = document.getElementById(rpc.ID);
		if (node)
			node.parentNode.removeChild(node);

		rpc.callback(result);

		// Some browsers (IE) don't like this
		try {
			delete windows["fn"+tmpId];
		} catch(e) {};
		}
}

// RPC handlers
function changePhoto() {
		var img = document.getElementById("rand-image");
		if (img)
			img.src = imgURL;
		else {
			window.setTimeout("changePhoto();", 100);
			return;
		}
}

function myCallback(result) {
	var photos = result["portal.getObjectsByTag"];

	if (photos.length) {
		// Pick a random photo
		var num = Math.floor(Math.random()*photos.length);
		imgURL = photos[num][2].replace("%s", "2/");
		if (!imgURL)
			imgURL = photos[0][2].replace("%s", "2/");

		changePhoto();
	}
}

var imgURL = "";
var parameters = { username : "markos",
					limit : 100,
					tag : "moja-izbira" };

a = new MarelaRPC();
a.callback = myCallback;
a.call("portal.getObjectsByTag", parameters);
