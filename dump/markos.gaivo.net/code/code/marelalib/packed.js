function MarelaRPC(){this.I="";var r=this;this.call=function(b,p,nu){var u="http://www.marela.si/as/rest/?rtype=json";var m=false;var c;if(nu)u=nu;var a=b.search(",");switch(a){case 0:alert("Syntax error: methods start with empty name");return;case-1:c=u+"&method="+b;break;default:c=u+"&methods="+b;m=true;};var s=document.createElement('script');s.type='text/javascript';var t;do{t="rpc"+Math.round(Math.random()*1000);}while(document.getElementById(t)||window["fn"+t]);s.id=t;c+="&json_func=fn"+t+"(%s)";window["fn"+t]=this._h;for(k in p){if(m&&p[k].search(".")<=0){alert("Syntax error: Malformed parameters in multi-method call");return;}
c+="&"+k+"="+p[k];}
s.src=c;document.getElementsByTagName('head')[0].appendChild(s);this.I=s.id;}
this.callback=function(d){}
this._h=function(d){var n=document.getElementById(r.I);if(n)
n.parentNode.removeChild(n);r.callback(d);try{delete windows["fn"+tmpId];}catch(e){};}}
