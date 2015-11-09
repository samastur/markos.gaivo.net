(function () {
    var docCookies = {
      getItem: function (sKey) {
        return unescape(document.cookie.replace(new RegExp("(?:(?:^|.*;)\\s*" + escape(sKey).replace(/[\-\.\+\*]/g, "\\$&") + "\\s*\\=\\s*([^;]*).*$)|^.*$"), "$1")) || null;
      },
      setItem: function (sKey, sValue, vEnd, sPath, sDomain, bSecure) {
        if (!sKey || /^(?:expires|max\-age|path|domain|secure)$/i.test(sKey)) { return false; }
        var sExpires = "";
        if (vEnd) {
          switch (vEnd.constructor) {
            case Number:
              sExpires = vEnd === Infinity ? "; expires=Fri, 31 Dec 9999 23:59:59 GMT" : "; max-age=" + vEnd;
              break;
            case String:
              sExpires = "; expires=" + vEnd;
              break;
            case Date:
              sExpires = "; expires=" + vEnd.toGMTString();
              break;
          }
        }
        document.cookie = escape(sKey) + "=" + escape(sValue) + sExpires + (sDomain ? "; domain=" + sDomain : "") + (sPath ? "; path=" + sPath : "") + (bSecure ? "; secure" : "");
        return true;
      }
    };

    function load_delayed() {
        var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
        ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
        (document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(ga);
    }

    function cookie_choice() {
        if ($(this).hasClass("yes")) {
            docCookies.setItem("cookie_law", "true", Infinity);
            load_delayed();
        } else {
            docCookies.setItem("cookie_law", "false", Infinity);
        }
        $(".cookie-div").remove();
        return false;
    }

    function create_alert() {
        var en_txt = "I'd like to use cookies to collect metrics for improving this site. I can't and wouldn't want to identify you. Are you OK with that?",
            $note = null,
            note_html = '<p>'+en_txt+'</p>'+
                        '<p class="cookie-buttons"><input type="button" value="✓" class="yes">'+
                        '<input type="button" value="×" class="no"></p>';

        $note = $("<div>", {class:'cookie-div'});
        $note.html(note_html);
        $note.insertBefore(document.body.firstChild);
        $("input", $note).click(cookie_choice);
    }

    var choice = docCookies.getItem("cookie_law");
    if (choice === null) {
        create_alert();
    } else if (choice === "true") {
        load_delayed();
    }
})();
