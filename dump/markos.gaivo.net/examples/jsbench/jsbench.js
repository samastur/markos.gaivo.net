var req;
var JS = 0;
var start;
var end;
var data;

// developer.apple script. Good enough for this.
function loadXMLDoc(url) {
    var server = document.location.protocol+"//"+document.location.host;
    req = false;
    // branch for native XMLHttpRequest object
    if(window.XMLHttpRequest) {
        try {
                        req = new XMLHttpRequest();
        } catch(e) {
                        req = false;
        }
    // branch for IE/Windows ActiveX version
    } else if(window.ActiveXObject) {
        try {
                req = new ActiveXObject("Msxml2.XMLHTTP");
        } catch(e) {
                try {
                        req = new ActiveXObject("Microsoft.XMLHTTP");
                } catch(e) {
                        req = false;
                }
                }
    }
        if(req) {
                req.onreadystatechange = processReqChange;
                start = new Date();
                req.open("GET", server+url, true);
                req.send("");
        }
}

function processReqChange() {
    // only if req shows "loaded"
    if (req.readyState == 4) {
        // only if "OK"
        if (req.status == 200) {
            // ...processing statements go here...
            if (!JS) {
                JS = 1;
                // Time JS
                eval("data = "+req.responseText);
                document.getElementById("js").innerHTML = data["id34"][1];
                end = new Date();

                document.getElementById("jstime").innerHTML = end.getTime() - start.getTime();
                loadXMLDoc("/examples/jsbench/xmlsample.xml");
            }
            else {
		var data = null;
		data = req.responseXML.getElementsByTagName("dataset")[0];
                document.getElementById("xml").innerHTML = data.childNodes[34].getAttribute("str");
                end = new Date();

                document.getElementById("xmltime").innerHTML = end.getTime() - start.getTime();
            }
        } else {
            alert("There was a problem retrieving the XML data:\n" +
                req.statusText);
        }
    }
}

function init() {
	loadXMLDoc("/examples/jsbench/jssample.raw");
}

window.onload = init;
