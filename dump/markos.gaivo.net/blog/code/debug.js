(function () {
	var debug = false,
		debuglevel = 2,
		debugcount = 15,
		debugmsg = [];

	function _displayDebug () {
		alert(debugmsg.join("\n"));
	}

	function formatText() {
		// Mimics Firebug 1.05 handling of console functions
		var txt = [], l = arguments.length;
		var arg = arguments; // Needed because of scope in replace function later on

		for(var i=0;i<l;i++) {
			txt.push( (typeof arguments[i] == "string") ?
				arguments[i].replace(/(%[sdifo])/g, function(m, value){return arg[++i];})
				: arguments[i] );
		}
		return txt.join(" ");
	}

	function onJSError(msg, url, line) {
		if (msg) {
			debugmsg.push(formatText("JS Error: %s (%s) on line %d", msg, url, line));
		}
		window.console.debugEnd();
	}

	function debugInit(dbg, dbglevel, dbgcount) {
		var names = ["error", "warn", "info", "debug", "log", "assert", "dir", "dirxml",
			"group", "groupEnd", "time", "timeEnd", "count", "trace", "profile", "profileEnd"];
		var i = ((!window.console || !console.firebug) && !dbg) ? 0 : dbglevel;

		for (var j=0; j < names.length; ++j)
			// Remove logging functions below requested level
			window.console[names[j]] = (j < i ) ?
					function(prefix) {
						return function () {
							var txt = formatText.apply(this, arguments);
							debugmsg.push(prefix.toUpperCase()+": "+txt);

							// Delete any superflous lines (debugcount)
							delete debugmsg[debugmsg.length-dbgcount-1];
						}
					}(names[j]) : function() {};
	}

	document.location.search.slice(1).replace(/([^=&]+)=([^&]*)/g, function(m, key, value){
		var v = parseInt(value, 10);
		if (key === "dbg") debug = (value === "false") ? false : true;
		else if (key == "dbglevel") debuglevel = (v < 6) ? v : 5; // Also takes care of not-numbers
		else if (key == "dbgcount") debugcount = v || debugcount;
	});

	if (!window.console || !console.firebug || !debug) {
		window.console = {};
	}
	window.console.on = debug || false;

	window.console.debugStart = function (callback, options) {
		var dbglevel = debuglevel, dbgcount = debugcount;
		var opt = options;

		window.console.on = true;
		if (callback instanceof Function) {
			window.console.debugDisplay = callback;
		} else if (callback instanceof Object) {
			// Callback is an object that isn't a function => assume proper object
			opt = callback;
		}
		if (opt instanceof Object) {
			dbglevel = opt["level"] || debuglevel;
			dbgcount = opt["count"] || debugcount;
			window.console.debugDisplay = opt["callback"] || window.console.debugDisplay;
		}
		debugInit(true, dbglevel, dbgcount);
	}

	window.console.debugEnd = function () {
		var sl = debugmsg.length-debugcount;

		// Turn debugging off
		window.console.on = false;
		debugInit(false);

		// Cut off any empty elements at the front
		debugmsg = debugmsg.slice((sl>=0) ? sl : 0);

		if (window.console.debugDisplay)
			return window.console.debugDisplay(debugmsg);
		else
			_displayDebug();
	}

	window.onerror = onJSError;

	debugInit(debug, debuglevel, debugcount);
})();
