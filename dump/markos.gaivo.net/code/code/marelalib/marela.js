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
