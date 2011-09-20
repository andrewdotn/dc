var DISQUS=function(e,h){var j=e.document,q=0,p=j.getElementsByTagName("head")[0]||j.getElementsByTagName("body")[0],m={running:!1,timer:null,queue:[]},n={"0.0":{},"1.0":{}},s=[],b={config:{},blocks:{theme:{},defaults:{}},status:null,settings:{store_:{},schema_:{"disqus.version":{type:"str"},"disqus.domain":{type:"str"},"disqus.debug":{type:"bool"},"disqus.minified":{type:"bool"},"disqus.readonly":{type:"bool"},"disqus.recaptcha.key":{type:"str"},"disqus.facebook.appId":{type:"str"},"disqus.facebook.apiKey":{type:"str"},
"disqus.urls.main":{type:"str"},"disqus.urls.media":{type:"str"},"disqus.urls.sslMedia":{type:"str"},"disqus.urls.realtime":{type:"str"},"disqus.urls.uploads":{type:"str"},"disqus.urls.unmerged":{type:"str"}}}};b.settings.store_={"disqus.recaptcha.key":"6LdKMrwSAAAAAPPLVhQE9LPRW4LUSZb810_iaa8u","disqus.urls.media":"http://mediacdn.disqus.com/1316454436","disqus.urls.main":"http://disqus.com","disqus.urls.uploads":"http://media.disqus.com/uploads","disqus.urls.realtime":"http://rt.disqus.com/forums/realtime-cached.js",
"disqus.urls.unmerged":"http://disqus.com/embed/profile/unmerged_profiles/","disqus.urls.sslMedia":"https://securecdn.disqus.com/1316454436","disqus.domain":"disqus.com","disqus.version":"1316454436","disqus.debug":!1,"disqus.minified":!0};b.settings.add=function(d,c,a){b.assert(b.settings.schema_[d]==null||a,"Unsafe attempt to update settings schema.");b.assert(c.type!=null,"Missing required property 'key'.");b.settings.schema_[d]=c;return b.settings};b.settings.get=function(d,c){var a=b.settings.schema_[d];
b.assert(a!=null,"Undefined key '"+d+"'.");var i=b.settings.store_[d];if(i==null)return c;if(a.values&&!a.values.length){var f={};b.each(a.values,function(a,d){f[a]=d});return f[i]}return i};b.settings.set=function(d,c){var a=b.settings.schema_[d],i;b.assert(a!=null,"Undefined key '"+d+"'.");i=function(a){for(var d=0,b;b=a[d];d++){if(b=="str"&&typeof c=="string")return!0;if(b=="bool"&&typeof c=="boolean")return!0;if(b=="int"&&typeof c=="number")return!0;if(b=="obj"&&typeof c=="object")return!0}return!1}(typeof a.type==
"string"?[a.type]:a.type);b.assert(i,"Invalid type for rule '"+d+"'.");a.values&&b.assert(b.contains(a.values,c),"Value is not acceptable.");a.rule&&b.assert(a.rule(c,d),"Value didn't pass schema's rule.");b.settings.store_[d]=a.values&&!a.values.length?a.values[c]:c};b.each=function(d,c){var a=d.length,b=Array.prototype.forEach;if(isNaN(a))for(var f in d)d.hasOwnProperty(f)&&c(d[f],f,d);else if(b)b.call(d,c);else for(b=0;b<a;b++)c(d[b],b,d)};b.isBrowser=function(d){var b=e.navigator.userAgent,a=
/(iPhone|Android|iPod|iPad|webOS|Mobile Safari|Windows Phone)/i;switch(d){case "ie":return/msie/i.test(b)&&!/opera/i.test(b);case "ie6":return!e.XMLHttpRequest;case "ie7":return/msie/i.test(b)&&!/opera/i.test(b)&&parseInt(/MSIE\s(\d+\.\d+)/.exec(b)[1],10)==7;case "webkit":return~b.indexOf("AppleWebKit/");case "opera":return!(!e.opera||!e.opera.buildNumber);case "gecko":return~b.indexOf("Gecko/");case "mobile":return a.test(b);case "quirks":return j.compatMode==="BackCompat";default:return!1}};b.AssertionError=
function(b){this.message=b};b.AssertionError.prototype.toString=function(){return"Assertion Error: "+(this.message||"[no message]")};b.assert=function(d,c){if(!d)throw new b.AssertionError(c);};b.api=function(d,c){var a=b.comm&&b.comm.Default.recover();if(a){if(!c.type)c.type="GET";if(!c.success)c.success=function(){};if(!c.failure)c.failure=function(){};if(!c.data)c.data={};a.api(d,c.data,c.type,c.success,c.failure)}else b.once("loader.onDefaultChannelReady",function(){b.api(d,c)})};b.each(["bind",
"once","unbind","unbindAll","trigger"],function(d){b[d]=function(c,a){var i;c&&(c=c.replace(".","_"));switch(d){case "bind":b.bean.add(b,c,a);break;case "once":i=function(){b.unbind(c,i);a.apply(this,arguments)};b.bind(c,i);break;case "unbind":b.bean.remove(b,c,a);break;case "unbindAll":b.bean.remove(b,c);break;case "trigger":b.bean.fire(b,c,[a])}}});b.contains=function(b,c){if(b.length){for(var a=0,i=b.length;a<i;a++)if(b[a]==c)return!0;return!1}for(a in b)if(b.hasOwnProperty(a)&&a==c)return!0;return!1};
b.defer=function(d,c){function a(){var a=m.queue;if(a.length===0)m.running=!1,clearInterval(m.timer);try{for(var d=0,c;c=a[d];d++)c[0]()&&(a.splice(d--,1),c[1]())}catch(e){if(!(e instanceof b.AssertionError))throw e;}}m.queue.push([d,c]);a();if(!m.running)m.running=!0,m.timer=setInterval(a,100)};b.define=function(d,c){for(var a=d.split("."),i=a.shift(),f=b,e=c.call({overwrites:function(a){a.__overwrites__=!0;return a}});i;)f=f[i]?f[i]:f[i]={},i=a.shift();b.each(e,function(a,d){!e.__overwrites__&&
!b.reset_&&b.assert(f[d]==null,"Unsafe attempt to redefine existing module.");f[d]=a;s.push(function(){delete f[d]})})};b.cleanup=function(){for(var b=0;b<s.length;b++)s[b]()};b.empty=function(b){for(var c in b)if(b.hasOwnProperty(c))return!1;return!0};b.extend=function(){var d,c;arguments.length<=1?(d=b,c=[arguments[0]||{}]):(d=arguments[0]||{},c=Array.prototype.slice.call(arguments,1));b.each(c,function(a){b.each(a,function(a,b){d[b]=a})});return d};b.getGuid=function(){return q++};b.partial=function(){var b=
arguments[0],c=Array.prototype.slice.call(arguments,1);return function(){for(var a=Array.prototype.slice.call(arguments),i=[],e=0,j=c.length;e<j;e++)i.push(c[e]===h?a.shift():c[e]);for(;a.length>0;)i.push(a.shift());return b.apply(this,i)}};b.serializeArgs=function(d){var c=[];b.each(d,function(a,b){a!==h&&c.push(b+(a!==null?"="+encodeURIComponent(a):""))});return c.join("&")};b.serialize=function(d,c,a){c&&(d+=~d.indexOf("?")?d.charAt(d.length-1)=="&"?"":"&":"?",d+=b.serializeArgs(c));if(a)return c=
{},c[(new Date).getTime()]=null,b.serialize(d,c);c=d.length;return d.charAt(c-1)=="&"?d.slice(0,c-1):d};b.sdk=function(d){function c(a){return function(){function c(j){a!=j.name||d!=j.version||(j.func.apply({},e),b.unbind("loader.onSDKMethodReady",c))}var e=Array.prototype.slice.call(arguments);b.bind("loader.onSDKMethodReady",c)}}var a=n[d||"1.0"];b.assert(a!==h,"version is not supported.");if(!b.empty(a))return a;a=b.settings.get("disqus.debug")?"/js/src/sdk/":"/build/system/sdk/";b.require(b.settings.get("disqus.urls.media")+
a+d+".js");return{getThread:c("getThread"),getSession:c("getSession")}};b.sdk.add=function(d,c,a){b.assert(n[c]!==h,"version is not supported.");n[c][d]=a;b.trigger("loader.onSDKMethodReady",{name:d,version:c,func:a})};b.useSSL=function(d){var c,a,i;if(e.location.href.match(/^https/))if(d){c=["disqus_url","realtime_url","uploads_url"];for(i=0;a=c[i];i++)d[a]=d[a].replace(/^http/,"https");d.media_url=d.ssl_media_url}else{c=["disqus.urls.main","disqus.urls.realtime","disqus.urls.uploads"];for(i=0;a=
c[i];i++)b.settings.set(a,b.settings.get(a).replace(/^http/,"https"));b.settings.set("disqus.urls.media",b.settings.get("disqus.urls.sslMedia"))}};b.useSSL();b.ready=function(d){function c(){var a=b.settings.get("disqus.urls.media"),d=a+"/js/src/embed/",c=a+"/build/system/",e=b.settings.get("disqus.debug"),j=b.settings.get("disqus.urls.media"),h;b.status="loading";e?(h=a+"/styles/dtpl/defaults.css",a=[d+"dtpl.js",d+"actions.js",d+"validators.js",d+"utils.js",d+"nodes.js",d+"sandbox.js",d+"tooltip.js",
d+"comm.js",d+"ui.js",d+"sso.js",d+"compat.js",d+"facebook.js",c+"defaults.js",a+"/js/src/lib/easyxdm.js",a+"/js/src/json.js",a+"/js/src/sdk/1.0.js"],b.config.includeStacktrace&&a.push(j+"/js/src/lib/stacktrace.js")):(h=c+"/defaults.css",a=[c+"disqus.js"]);b.requireStylesheet(h);b.requireSet(a,e,function(){b.status="ready";b.trigger("loader.onFilesReady")})}if(b.status=="ready")d();else b.once("loader.onFilesReady",function(){d()});b.status===null&&c()};b.require=function(d,c,a,e,f){function h(a){if(a.type==
"load"||/^(complete|loaded)$/.test(a.target.readyState))e(),q&&clearTimeout(q),b.bean.remove(a.target,n,h)}var m=j.createElement("script"),n=m.addEventListener?"load":"readystatechange",q=null;m.src=b.serialize(d,c,a);m.async=!0;m.charset="UTF-8";e&&b.bean.add(m,n,h);f&&(q=setTimeout(function(){f()},2E4));p.appendChild(m);return b};b.requireSet=function(d,c,a){var e=d.length;b.each(d,function(d){b.require(d,{},c,function(){--e===0&&a()})})};b.requireStylesheet=function(d,c,a){var e=j.createElement("link");
e.rel="stylesheet";e.type="text/css";e.href=b.serialize(d,c,a);p.appendChild(e);return b};b.injectCss=function(b){var c=j.createElement("style");c.setAttribute("type","text/css");b=b.replace(/\}/g,"}\n");e.location.href.match(/^https/)&&(b=b.replace(/http:\/\//g,"https://"));c.styleSheet?c.styleSheet.cssText=b:c.appendChild(j.createTextNode(b));p.appendChild(c)};b.addBlocks=function(d,c){if(c)return function(){var a=b.blocks;b.blocks={};c();b.blocks=b.extend(a,{theme:b.blocks})}();var a={Builder:b.strings.Builder,
renderBlock:b.renderBlock,each:b.each,extend:b.extend,blocks:b.blocks[d||"defaults"],interpolate:b.strings.interpolate};return function(b){b(a)}};b.renderBlock=function(d,c){var a=d;typeof d==="string"&&(a=b.getBlock(d));if(a===h)throw"Block "+d+" was not found!";return b.sandbox.wrap(d,a,c)};b.getBlock=function(d){return b.blocks.theme[d]||b.blocks.defaults[d]};b.window={getSize:function(){return typeof e.innerWidth=="number"?[e.innerWidth,e.innerHeight]:j.documentElement?[j.documentElement.clientWidth||
j.body.clientWidth,j.documentElement.clientHeight||j.body.clientHeight]:[-1,-1]},getScrollPosition:function(){var b=j.documentElement;return b&&(b.scrollTop||b.scrollWidth)?[b.scrollWidth,b.scrollTop||j.body.scrollTop]:[j.body.scrollWidth,j.body.scrollTop]}};var v={};b.strings={translations:{},setGlobalContext:function(d){b.extend(v,d)},get:function(d){return b.strings.translations[d]||d},interpolate:function(b,c){var a=[c||{},v];return b.replace(/%\(\w+\)s/g,function(b){a:{for(var b=b.slice(2,-2),
c=0,d=a.length;c<d;c++)if(a[c][b]!==h){b=a[c][b].toString();break a}throw"Key "+b+" not found in context";}return b})},pluralize:function(b,c,a){return b!=1?a||"s":c||""},trim:function(b){for(var b=b.replace(/^\s\s*/,""),c=/\s/,a=b.length;c.test(b.charAt(--a)););return b.slice(0,a+1)},capitalize:function(b){return b.charAt(0).toUpperCase()+b.slice(1)},isUTF8:function(b){for(var c=0,a=b.length;c<a;c++)if(b.charCodeAt(c)>256)return!0;return!1}};var t=function(){this.value=(this.ie=b.isBrowser("ie"))?
[]:""};b.strings.Builder=t;t.prototype={put:function(b){this.ie?this.value.push(b):this.value+=b},compile:function(){if(this.ie)this.value=this.value.join("");return this.value}};return b}(this);
(function(e){function h(a){a=a.relatedTarget;if(!a)return a===null;var b;if(b=a!=this)if(b=a.prefix!="xul")if(b=!/document/.test(this.toString())){var c;a:for(a=a.parentNode;a!==null;){if(a==this){c=!0;break a}a=a.parentNode}b=!c}return b}var j=1,q={},p={},m=/over|out/,n=/[^\.]*(?=\..*)\.|.*/,s=/\..*/,b=((e.document||{}).documentElement||{}).addEventListener,v=b?"addEventListener":"attachEvent",t=function(a,b){return a.__uid=b||a.__uid||j++},d=function(a){a=t(a);return q[a]=q[a]||{}},c=b?function(a,
b,c,d){a[d?"addEventListener":"removeEventListener"](b,c,!1)}:function(a,b,c,d,g){g&&d&&(a["_on"+g]=a["_on"+g]||0);a[d?"attachEvent":"detachEvent"]("on"+b,c)},a=function(a,b,c){return function(d){d=l(d||((this.ownerDocument||this.document||this).parentWindow||e).event);return b.apply(a,[d].concat(c))}},i=function(a,c,d,g,k){return function(e){if(g?g.apply(this,arguments):b||e&&e.propertyName=="_on"+d||!e)c.apply(a,Array.prototype.slice.call(arguments,e?0:1).concat(k))}},f=function(g,k,e,l){var r=
k.replace(s,""),f=d(g),f=f[r]||(f[r]={}),j=e,k=t(e,k.replace(n,""));if(f[k])return g;var h=B[r];h&&(e=h.condition?i(g,e,r,h.condition):e,r=h.base||r);e=(h=o[r])?a(g,e,l):i(g,e,r,!1,l);h=b||h;if(r=="unload")var m=e,e=function(){u(g,r,e)&&m()};g[v]&&c(g,h?r:"propertychange",e,!0,!h&&r);f[k]=e;e.__uid=k;e.__originalFn=j;return r=="unload"?g:p[t(g)]=g},u=function(a,g,k){var r;var e,l,f=d(a),h=g.replace(s,"");if(!f||!f[h])return a;r=(g=g.replace(n,""))?g.split("."):[k.__uid],g=r;for(l=g.length;l--;)e=
g[l],k=f[h][e],delete f[h][e],a[v]&&(h=B[h]?B[h].base:h,e=b||o[h],c(a,e?h:"propertychange",k,!1,!e&&h));return a},z=function(a,b,c){return function(d){for(var g=typeof a=="string"?c(a,this):a,k=d.target;k&&k!=this;k=k.parentNode)for(var e=g.length;e--;)if(g[e]==k)return b.apply(k,arguments)}},A=function(a,b,c,d,g){if(typeof b=="object"&&!c)for(var k in b)b.hasOwnProperty(k)&&A(a,k,b[k]);else{k=typeof c=="string";for(var e=(k?c:b).split(" "),c=k?z(b,d,g):c,l=e.length;l--;)f(a,e[l],c,Array.prototype.slice.call(arguments,
k?4:3))}return a},w=function(a,b,c){var g,k,e,l=typeof b=="string",h=l&&b.replace(n,""),f=u,i=d(a);if(l&&/\s/.test(b)){b=b.split(" ");for(e=b.length-1;w(a,b[e])&&e--;);return a}k=l?b.replace(s,""):b;if(!i||l&&!i[k]){if(i&&h)for(g in i)if(i.hasOwnProperty(g))for(e in i[g])i[g].hasOwnProperty(e)&&e===h&&f(a,[g,h].join("."));return a}if(typeof c=="function")f(a,k,c);else if(h)f(a,b);else for(g in f=k?f:w,b=l&&k,k=k?c||i[k]||k:i,k)k.hasOwnProperty(g)&&(f(a,b||g,k[g]),delete k[g]);return a},k=b?function(a,
b,c){evt=document.createEvent(a?"HTMLEvents":"UIEvents");evt[a?"initEvent":"initUIEvent"](b,!0,!0,e,1);c.dispatchEvent(evt)}:function(a,b,c){a?c.fireEvent("on"+b,document.createEventObject()):c["_on"+b]++},g=function(a,b,c){var k=d(b),e;t(a);k=c?k[c]:k;for(e in k)k.hasOwnProperty(e)&&(c?A:g)(a,c||b,c?k[e].__originalFn:e);return a},l=function(a){var b={};if(!a)return b;var c=a.type,k=a.target||a.srcElement;b.preventDefault=l.preventDefault(a);b.stopPropagation=l.stopPropagation(a);b.target=k&&k.nodeType==
3?k.parentNode:k;if(~c.indexOf("key"))b.keyCode=a.which||a.keyCode;else if(/click|mouse|menu/i.test(c)){b.rightClick=a.which==3||a.button==2;b.pos={x:0,y:0};if(a.pageX||a.pageY)b.clientX=a.pageX,b.clientY=a.pageY;else if(a.clientX||a.clientY)b.clientX=a.clientX+document.body.scrollLeft+document.documentElement.scrollLeft,b.clientY=a.clientY+document.body.scrollTop+document.documentElement.scrollTop;m.test(c)&&(b.relatedTarget=a.relatedTarget||a[(c=="mouseover"?"from":"to")+"Element"])}for(var g in a)g in
b||(b[g]=a[g]);return b};l.preventDefault=function(a){return function(){a.preventDefault?a.preventDefault():a.returnValue=!1}};l.stopPropagation=function(a){return function(){a.stopPropagation?a.stopPropagation():a.cancelBubble=!0}};var o={click:1,dblclick:1,mouseup:1,mousedown:1,contextmenu:1,mousewheel:1,DOMMouseScroll:1,mouseover:1,mouseout:1,mousemove:1,selectstart:1,selectend:1,keydown:1,keypress:1,keyup:1,orientationchange:1,touchstart:1,touchmove:1,touchend:1,touchcancel:1,gesturestart:1,gesturechange:1,
gestureend:1,focus:1,blur:1,change:1,reset:1,select:1,submit:1,load:1,unload:1,beforeunload:1,resize:1,move:1,DOMContentLoaded:1,readystatechange:1,error:1,abort:1,scroll:1},B={mouseenter:{base:"mouseover",condition:h},mouseleave:{base:"mouseout",condition:h},mousewheel:{base:/Firefox/.test(navigator.userAgent)?"DOMMouseScroll":"mousewheel"}},C={add:A,remove:w,clone:g,fire:function(a,b,c){var g,e,l=b.split(" ");for(e=l.length;e--;){var b=l[e].replace(s,""),h=o[b],f=l[e].replace(n,""),i=d(a)[b];if(f){f=
f.split(".");for(g=f.length;g--;)i&&i[f[g]]&&i[f[g]].apply(a,[!1].concat(c))}else if(!c&&a[v])k(h,b,a);else for(g in i)i.hasOwnProperty(g)&&i[g].apply(a,[!1].concat(c))}return a}};e.attachEvent&&A(e,"unload",function(){for(var a in p)if(p.hasOwnProperty(a)){var b=w(p[a]).__uid;b&&(delete p[b],delete q[b])}e.CollectGarbage&&CollectGarbage()});var D=e.bean;C.noConflict=function(){e.bean=D;return this};typeof module!=="undefined"&&module.exports?module.exports=C:e.bean=C})(this);
(function(e,h){function j(){this.c={}}function q(a){z=[];c=0;for(w=a.length;c<w;c++)z[c]=a[c];return z}function p(a){for(;a=a.previousSibling;)if(a.nodeType==1)break;return a}function m(a,b,k,e,l,f,h,i,j,o,m){var x,n;if(b&&this.tagName.toLowerCase()!==b)return!1;if(k&&(x=k.match(B))&&x[1]!==this.id)return!1;if(k&&(g=k.match(C)))for(c=g.length;c--;)if(a=g[c].slice(1),!(E.g(a)||E.s(a,RegExp("(^|\\s+)"+a+"(\\s+|$)"))).test(this.className))return!1;if(j&&d.pseudos[j]&&!d.pseudos[j](this,m))return!1;if(e&&
!h)for(n in u=this.attributes,u)if(Object.prototype.hasOwnProperty.call(u,n)&&(u[n].name||n)==l)return this;if(e&&!s(f,this.getAttribute(l)||"",h))return!1;return this}function n(a){return H.g(a)||H.s(a,a.replace(P,"\\$1"))}function s(a,b,c){switch(a){case "=":return b==c;case "^=":return b.match(y.g("^="+c)||y.s("^="+c,RegExp("^"+n(c))));case "$=":return b.match(y.g("$="+c)||y.s("$="+c,RegExp(n(c)+"$")));case "*=":return b.match(y.g(c)||y.s(c,RegExp(n(c))));case "~=":return b.match(y.g("~="+c)||
y.s("~="+c,RegExp("(?:^|\\s+)"+n(c)+"(?:\\s+|$)")));case "|=":return b.match(y.g("|="+c)||y.s("|="+c,RegExp("^"+n(c)+"(-|$)")))}return 0}function b(a){var b=[],c=[],g,d=0,e,l,f,i,j,o=I.g(a)||I.s(a,a.split(O)),a=a.match(N),o=o.slice(0);if(!o.length)return b;l=o.pop();i=o.length&&(g=o[o.length-1].match(D))?h.getElementById(g[1]):h;if(!i)return b;j=l.match(G);e=a&&/^[+~]$/.test(a[a.length-1])?function(a){for(;i=i.nextSibling;)i.nodeType==1&&(j[1]?j[1]==i.tagName.toLowerCase():1)&&a.push(i);return a}([]):
i.getElementsByTagName(j[1]||"*");g=0;for(l=e.length;g<l;g++)if(f=m.apply(e[g],j))b[d++]=f;if(!o.length)return b;d=0;l=b.length;for(e=0;d<l;d++){f=b[d];for(g=o.length;g--;)for(;f=Q[a[g]](f,b[d]);)if(k=m.apply(f,o[g].match(G)))break;k&&(c[e++]=b[d])}return c}function v(a,b,c){c=typeof b=="string"?c(b)[0]:b||h;if(a===window||a&&a.nodeType&&(a.nodeType==1||a.nodeType==9))return!b||a!==window&&c&&c.nodeType&&(c.nodeType==1||c.nodeType==9)&&J(a,c)?[a]:[];if(a&&typeof a==="object"&&isFinite(a.length))return q(a);
if(f=a.match(D))return(A=h.getElementById(f[1]))?[A]:[];if(f=a.match(x))return q(c.getElementsByTagName(f[1]));return!1}function t(a){var b=[],c,g;c=0;a:for(;c<a.length;c++){for(g=0;g<b.length;g++)if(b[g]==a[c])continue a;b[b.length]=a[c]}return b}function d(a,b){var c=typeof b=="string"?d(b)[0]:b||h;if(!c||!a)return[];if(f=v(a,b,d))return f;return R(a,c)}var c,a,i,f,u,z,A,w,k,g,l,o=h.documentElement,B=/#([\w\-]+)/,C=/\.[\w\-]+/g,D=/^#([\w\-]+$)/,K=/^\.([\w\-]+)$/,x=/^([\w\-]+)$/,L=/^([\w]+)?\.([\w\-]+)$/,
M=/\s*([\s\+\~>])\s*/g,r=/[\s\>\+\~]/,F=/(?![\s\w\-\/\?\&\=\:\.\(\)\!,@#%<>\{\}\$\*\^'"]*\])/,N=RegExp("("+r.source+")"+F.source,"g"),O=RegExp(r.source+F.source),P=/([.*+?\^=!:${}()|\[\]\/\\])/g,G=RegExp(/^([a-z0-9]+)?(?:([\.\#]+[\w\-\.#]+)?)/.source+"("+/\[([\w\-]+)(?:([\|\^\$\*\~]?\=)['"]?([ \w\-\/\?\&\=\:\.\(\)\!,@#%<>\{\}\$\*\^]+)["']?)?\]/.source+")?("+/:([\w\-]+)(\(['"]?(\w+)['"]?\))?/.source+")?"),Q={" ":function(a){return a&&a!==o&&a.parentNode},">":function(a,b){return a&&a.parentNode==b.parentNode&&
a.parentNode},"~":function(a){return a&&a.previousSibling},"+":function(a,b,c,g){if(!a)return!1;c=p(a);g=p(b);return c&&g&&c==g&&c}};j.prototype={g:function(a){return this.c[a]||void 0},s:function(a,b){return this.c[a]=b}};var E=new j,H=new j,y=new j,I=new j,J="compareDocumentPosition"in o?function(a,b){return(b.compareDocumentPosition(a)&16)==16}:"contains"in o?function(a,b){b=b==h||b==window?o:b;return b!==a&&b.contains(a)}:function(a,b){for(;a=a.parentNode;)if(a===b)return 1;return 0},R=h.querySelector&&
h.querySelectorAll?function(a,b){if(b.getElementsByClassName&&(f=a.match(K)))return q(b.getElementsByClassName(f[1]));return q(b.querySelectorAll(a))}:function(c,g){var c=c.replace(M,"$1"),k=[],d,e=[],j;if(f=c.match(L)){l=g.getElementsByTagName(f[1]||"*");z=E.g(f[2])||E.s(f[2],RegExp("(^|\\s+)"+f[2]+"(\\s+|$)"));j=0;i=l.length;for(a=0;j<i;j++)z.test(l[j].className)&&(k[a++]=l[j]);return k}j=0;l=c.split(",");for(i=l.length;j<i;j++)e[j]=b(l[j]);j=0;for(i=e.length;j<i&&(d=e[j]);j++){var o=d;if(g!==h){o=
[];a=0;for(f=d.length;a<f&&(element=d[a]);a++)J(element,g)&&o.push(element)}k=k.concat(o)}return t(k)};d.uniq=t;d.pseudos={};var S=e.qwery;d.noConflict=function(){e.qwery=S;return this};e.qwery=d})(this,document);
(function(){DISQUS.extend({bean:bean.noConflict(),qwery:qwery.noConflict(),throttle:function(e,h,j,q){var p=(new Date).getTime();DISQUS.bean.add(e,h,function(e){var h=(new Date).getTime();h-p>=q&&(p=h,j(e))})},debounce:function(e,h,j,q){var p;DISQUS.bean.add(e,h,function(e){p&&clearTimeout(p);p=setTimeout(function(){j(e)},q)})}})})();DISQUS.modules={};DISQUS.addJob=DISQUS.defer;DISQUS.getResourceURL=DISQUS.serialize;
DISQUS.lang={contains:DISQUS.contains,forEach:DISQUS.each,extend:DISQUS.extend,trim:DISQUS.strings.trim,partial:DISQUS.partial};DISQUS.events={add:DISQUS.bean.add,remove:DISQUS.bean.remove,debounce:DISQUS.debounce};DISQUS.browser={ie:DISQUS.isBrowser("ie"),ie6:DISQUS.isBrowser("ie6"),ie7:DISQUS.isBrowser("ie7"),webkit:DISQUS.isBrowser("webkit"),opera:DISQUS.isBrowser("opera"),gecko:DISQUS.isBrowser("gecko"),mobile:DISQUS.isBrowser("mobile"),quirks:DISQUS.isBrowser("quirks")};
(function(e){function h(a,b){return a.hasAttribute?a.hasAttribute(b):a.getAttribute(b)!==null}function j(){for(var a=0,b=f.length;a<b;a++)if(h(f[a],"name")&&f[a].getAttribute("name")=="generator"&&h(f[a],"content")&&f[a].getAttribute("content")=="blogger")return!0;a=c.getElementById("Attribution1");if(a!==null&&a.innerHTML.indexOf("http://www.blogger.com")>0)return!0}function q(){var a;if(j()){a=c.getElementsByTagName("A");for(var b=0,d=a.length;b<d;b++)if(!h(a[b],"src")&&h(a[b],"name")&&parseInt(a[b].getAttribute("name"),
10)&&a[b].innerHTML==="")return a[b].getAttribute("name")}return null}function p(a){var b=0,c=0;if(!a.offsetParent)return[0,0];do b+=a.offsetLeft,c+=a.offsetTop,a=a.offsetParent;while(a);return[b,c]}function m(b){var c=a.window.getScrollPosition()[1],d=c+a.window.getSize()[1];return b>=c&&b<=d}function n(b){if(!(typeof i!="function"&&typeof b!="function")){var c={preData:"loader.onReady",preInit:"loader.onDataReady",onInit:"loader.onLibraryReady",afterRender:"loader.onTemplateReady",onReady:"thread.onReady",
onPaginate:"thread.onPaginate",onNewComment:"comment.onCreate",preReset:"thread.beforeReset"};a.config.callbacks={};a.config.page={};a.each(c,function(b,c){a.config.callbacks[c]=[]});try{(b||i).call(a.config)}catch(d){}a.each(a.config.callbacks,function(b,d){b.length!==0&&a.each(b,function(b){a.bind(c[d],b)})});a.config.callbacks=c}}function s(){var b={url:"thread.url",title:"thread.title",slug:"thread.slug",category_id:"thread.category",identifier:"thread.identifier",remote_auth_s3:"request.sso.data",
author_s3:"thread.author.sig",api_key:"forum.apiKey"};a.each({disqus_domain:"disqus.domain",disqus_category_id:"thread.category",disqus_thread_slug:"thread.slug",disqus_title:"thread.title",disqus_url:"thread.url",disqus_identifier:"thread.identifier",disqus_per_page:"thread.postsPerPage",disqus_require_moderation_s:"thread.moderatePosts",disqus_skip_auth:"thread.skipAuthRequest",disqus_def_email:"thread.defaults.email",disqus_def_name:"thread.defaults.name",disqus_default_text:"thread.defaults.placeholder",
disqus_shortname:"forum.shortname",disqus_facebook_key:"forum.facebook.key",disqus_custom_strings:"ui.translations",disqus_container_id:"ui.container",DsqLocal:"legacy.trackbacks",disqus_remote_auth_s2:"legacy.sso.data",disqus_author_s2:"legacy.thread.author.sig"},function(b,c){e[c]!=null&&a.settings.set(b,e[c])});if(e.disqus_sort!=null)a.settings.store_["thread.sort"]=e.disqus_sort;e.disqus_developer!=null&&a.settings.set("disqus.developer",!!e.disqus_developer);a.config&&a.config.page&&(a.config.page.remote_auth_s3!=
null&&a.settings.set("request.sso.data",a.config.page.remote_auth_s3),a.config.page.api_key!=null&&a.settings.set("forum.apiKey",a.config.page.api_key),a.each(b,function(b,c){a.config.page[c]!=null&&a.settings.set(b,a.config.page[c])}))}function b(){var b=e.location.hash,d=a.settings.get,f=d("legacy.trackbacks",{});a.extend(a.config,{container_id:d("ui.container","disqus_thread"),trackback_url:f.trackback_url||null,trackbacks:f.trackbacks||null,absorbStyles:!1});a.config.page={url:d("thread.url",
e.location.href),title:d("thread.title",""),slug:d("thread.slug"),sort:d("thread.sort",""),per_page:d("thread.postsPerPage",null),category_id:d("thread.category",""),developer:+d("disqus.developer",0),identifier:d("thread.identifier",""),require_mod_s:d("thread.moderatePosts"),remote_auth_s3:d("request.sso.data"),author_s3:d("thread.author.sig"),api_key:d("forum.apiKey"),disqus_version:d("disqus.version"),remote_auth_s2:d("legacy.sso.data"),author_s2:d("legacy.thread.author.sig")};var f=c.getElementById(a.config.container_id),
h=p(f)[1];if(f&&m(h))a.config.page.lazy="0";if(j())a.config.page.blogger_id=q(),a.config.page.url=a.config.page.url.replace(/\?.*$/,"");if(b&&(b=b.match(/comment\-([0-9]+)/)))a.config.page.anchor_post_id=b[1];var i=e.disqus_callback;typeof i=="function"&&a.bind("thread.onReady",function(){i(e.disqus_callback_params||null)});a.config.custom_strings=d("ui.translations",{});a.extend(a.config,{domain:d("disqus.domain"),shortname:d("forum.shortname")||a.getShortname(),facebook_key:d("forum.facebook.key",
null),def_name:d("thread.defaults.name"),def_email:d("thread.defaults.email"),def_text:d("thread.defaults.placeholder",""),skip_auth:d("thread.skipAuthRequest",!1)});d=a.config.shortname+"."+a.config.domain+"/thread.js";a.config.json_url=e.location.href.match(/^https/)?"https://"+d:"http://"+d}function v(){function b(a,c,d,e,g,k){return'<img width="'+a+'" height="'+c+'" alt="'+e+'" src="data:image/'+d+";base64,"+g+'"'+(k?'style="'+k+'"':"")+"/>"}a.jsonData={ready:!1};a.require(a.config.json_url,a.config.page,
!0,null,function(){e.innerHTML='There was a problem loading Disqus. For more information, please visit <a href="http://status.disqus.com">status.disqus.com</a>.'});var d=a.qwery("#dsq-content")[0]||c.createElement("div");d.id="dsq-content";d.style.display="none";var e=a.qwery("#dsq-content-stub")[0]||c.createElement("div");e.id="dsq-content-stub";e.innerHTML=a.browser.ie6?"...":b(71,17,"png","DISQUS",z.join(""))+b(16,11,"gif","...",A.join(""),"margin:0 0 3px 5px");var f=a.qwery("#"+a.config.container_id)[0];
f.appendChild(d);f.appendChild(e);a.ready(function(){a.initThread(function(){e.style.display="none"})})}function t(b){var d=c.getElementById("dsq-content"),f=a.settings.get("disqus.urls.media"),h=f+"/build/system/",i=f+"/build/lang/",j=a.jsonData.forum.template.css,m=a.jsonData.forum.template.url,n=a.jsonData.context.switches,x=a.settings.get("disqus.debug");(function(){var b=a.jsonData;a.strings.setGlobalContext({profile_url:b.urls.request_user_profile,disqus_url:a.settings.get("disqus.urls.main"),
media_url:a.settings.get("disqus.urls.media"),forum_name:b.forum.name,request_username:b.request.username,request_display_username:b.request.display_username})})();a.trigger("loader.onDataReady");if(a.browser.mobile&&!a.jsonData.forum.mobile_theme_disabled)j=a.jsonData.forum.template.mobile.css,m=a.jsonData.forum.template.mobile.url;else if(a.config.template)j=a.config.template.css,m=a.config.template.js;!e.disqus_no_style&&j&&a.requireStylesheet(j,{},x);j=a.jsonData.forum.stylesUrl;if(!a.jsonData.context.switches.static_styles||
x)j="http://"+a.config.domain+"/forums/"+a.config.shortname+"/styles.css";a.jsonData.forum.hasCustomStyles&&a.requireStylesheet(j,{u:a.jsonData.forum.lastUpdate});m=[m];n.new_toolbar&&(m.push(h+"/defaults.toolbar.js"),a.requireStylesheet(x?f+"/styles/dtpl/defaults.toolbar.css":h+"/defaults.toolbar.css",{},x));f=e.location.search;~f.indexOf("fbc_channel=1")?a.require("http://static.ak.connect.facebook.com/js/api_lib/v0.4/FeatureLoader.js.php"):~f.indexOf("fb_xd_fragment")?a.require("http://connect.facebook.net/en_US/all.js"):
(a.config.language?a.config.language!="en"&&m.push(i+a.config.language+".js"):a.jsonData.forum.language!="en"&&m.push(i+a.jsonData.forum.language+".js"),a.comm.Default.create(function(){a.trigger("loader.onDefaultChannelReady")}).setApiKey(a.jsonData.forum.apiKey),a.requireSet(m,x,function(){a.config.custom_strings&&a.lang.extend(a.strings.translations,a.config.custom_strings);if(a.config.def_text==="")a.config.def_text=a.strings.get("Type your comment here.");a.registerActions();a.trigger("loader.onActionsReady");
a.nodes.addClass(d,"clearfix");var c=d.parentNode;c.removeChild(d);d.innerHTML=a.renderBlock("thread");c.appendChild(d);a.trigger("loader.onLibraryReady");a.dtpl.actions.fire("thread.initialize");a.trigger("loader.onTemplateReady");a.bean.add(d,"click change",function(b){for(var c=b.target,e;c!=d;){if(e=a.dtpl.getAction(c,b)){b.preventDefault();e();break}c=c.parentNode}});a.nodes.container=a.nodes.get("#dsq-content");d.style.display="block";b();a.config.page.anchor_post_id&&a.nodes.scrollTo("#dsq-comment-"+
a.config.page.anchor_post_id);a.dtpl.actions.fire("thread.ready")}))}function d(a){return Date.UTC(a.getUTCFullYear(),a.getUTCMonth(),a.getUTCDate(),a.getUTCHours(),a.getUTCMinutes(),a.getUTCSeconds(),a.getUTCMilliseconds())}var c=e.document,a=e.DISQUS,i=e.disqus_config;a.qwery("head")[0]||a.qwery("#disqus_thread");var f=a.qwery("meta"),u=!1,z=["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","TkSuQmCC"],A=["R0lGODlhEAALAPQAAP///z2LqeLt8dvp7u7090GNqz2LqV+fuJ/F1IW2ycrf51aatHWs","waXJ14i4ys3h6FmctUCMqniuw+vz9eHs8fb5+meku+Tu8vT4+cfd5bbT3tbm7PH2+AAA","AAAAAAAAACH/C05FVFNDQVBFMi4wAwEAAAAh/hpDcmVhdGVkIHdpdGggYWpheGxvYWQu","aW5mbwAh+QQJCwAAACwAAAAAEAALAAAFLSAgjmRpnqSgCuLKAq5AEIM4zDVw03ve27if","DgfkEYe04kDIDC5zrtYKRa2WQgAh+QQJCwAAACwAAAAAEAALAAAFJGBhGAVgnqhpHIeR",
"vsDawqns0qeN5+y967tYLyicBYE7EYkYAgAh+QQJCwAAACwAAAAAEAALAAAFNiAgjoth","LOOIJAkiGgxjpGKiKMkbz7SN6zIawJcDwIK9W/HISxGBzdHTuBNOmcJVCyoUlk7CEAAh","+QQJCwAAACwAAAAAEAALAAAFNSAgjqQIRRFUAo3jNGIkSdHqPI8Tz3V55zuaDacDyIQ+","YrBH+hWPzJFzOQQaeavWi7oqnVIhACH5BAkLAAAALAAAAAAQAAsAAAUyICCOZGme1rJY","5kRRk7hI0mJSVUXJtF3iOl7tltsBZsNfUegjAY3I5sgFY55KqdX1GgIAIfkECQsAAAAs","AAAAABAACwAABTcgII5kaZ4kcV2EqLJipmnZhWGXaOOitm2aXQ4g7P2Ct2ER4AMul00k","j5g0Al8tADY2y6C+4FIIACH5BAkLAAAALAAAAAAQAAsAAAUvICCOZGme5ERRk6iy7qpy","HCVStA3gNa/7txxwlwv2isSacYUc+l4tADQGQ1mvpBAAIfkECQsAAAAsAAAAABAACwAA",
"BS8gII5kaZ7kRFGTqLLuqnIcJVK0DeA1r/u3HHCXC/aKxJpxhRz6Xi0ANAZDWa+kEAA7","AAAAAAAAAAAA"];a.settings.add("disqus.developer",{type:"bool"}).add("thread.category",{type:["str","int"]}).add("thread.slug",{type:"str"}).add("thread.title",{type:"str"}).add("thread.url",{type:"str"}).add("thread.identifier",{type:["str","int"]}).add("thread.postsPerPage",{type:["str","int"]}).add("thread.moderatePosts",{type:"str",values:["all","none","anon"]}).add("thread.skipAuthRequest",{type:"bool"}).add("thread.sort",
{type:"str",values:{oldest:1,newest:2,best:3,hot:4,highlighted:5}}).add("thread.defaults.name",{type:"str"}).add("thread.defaults.email",{type:"str"}).add("thread.defaults.placeholder",{type:"str"}).add("thread.author.sig",{type:"str"}).add("forum.shortname",{type:"str"}).add("forum.apiKey",{type:"str"}).add("forum.facebook.key",{type:"str"}).add("ui.translations",{type:"obj"}).add("ui.container",{type:"str"}).add("request.sso.data",{type:"str"}).add("legacy.trackbacks",{type:"obj"}).add("legacy.thread.author.sig",
{type:"str"}).add("legacy.sso.data",{type:"str"}).add("realtime.host",{type:"str"}).add("realtime.port",{type:"int"});a.extend({cache:{postboxBusy:{},buttonsToRestore:[],popupProfileCache:{},popupStatusCache:{},toggledReplies:{},postSharing:{},realtime:{interval:null,ongoing_request:null,prev_script:null,last_checked:null,newPosts:[]}},states:{edit:{},realtime:!1,useLoginWindow:!1,loginDisabled:!1,metaViewport:function(){for(var a=0,b=f.length;a<b;a++)if(f[a].getAttribute("name")=="viewport")return!0;
return!1}()},curPageId:"dsq-comments",frames:{},config:{template:null},jsonData:null,isReady:!1,getShortname:function(){function a(b){var b=b.getAttribute?b.getAttribute("src"):b.src,c=[/https?:\/\/(www\.)?disqus\.com\/forums\/([\w_\-]+)/i,/https?:\/\/(www\.)?([\w_\-]+)\.disqus\.com/i,/https?:\/\/(www\.)?dev\.disqus\.org\/forums\/([\w_\-]+)/i,/https?:\/\/(www\.)?([\w_\-]+)\.dev\.disqus\.org/i],d=c.length;if(!b||b.substring(b.length-8)!="embed.js")return null;for(var e=0;e<d;e++){var g=b.match(c[e]);
if(g&&g.length&&g.length==3)return g[2]}return null}for(var b=c.getElementsByTagName("script"),d=b.length-1;d>=0;d--){var e=a(b[d]);if(e!==null)return e}return null},callback:function(b){var c=arguments.length>1?Array.prototype.slice.call(arguments,1):[];a.trigger(b,{args:c})},reset:function(c){var d=a.nodes.get("#"+a.config.container_id),c=c||{};a.comm.reset();a.jsonData=null;a.sandbox.invalidateGlobals();a.status=null;a.config.page={};d.innerHTML="";a.trigger("thread.beforeReset");a.unbindAll();
a.cleanup();c.reload&&(n(c.config),s(),b(),v())},updatePost:function(b,c){var d=a.jsonData.posts[b]||{};if(c)c.id=b,a.jsonData.posts[b]=a.extend(d,c),a.trigger("data.onPostUpdate",{id:b,data:c})},reload:function(b){a.require(a.config.json_url,a.config.page,!0,function(){u=!0;typeof b=="function"&&b()})},redraw:function(b){if(u||b)a.sandbox.invalidateGlobals(),b=a.nodes.get("#dsq-content"),b.innerHTML=a.renderBlock("thread"),a.frames=[],a.dtpl.actions.fire("thread.initialize"),u=!1},initThread:function(b){function d(a){var b=
e.onload;e.onload=typeof e.onload!="function"?a:function(){b&&b();a()}}function f(){var b,d;if(a.isReady){if(i&&clearInterval(i),c.getElementById(a.settings.get("ui.container")),b=c.getElementsByTagName("iframe"),d=c.getElementById("dsq-content"))for(var g=0,k=b.length;g<k;g++)b[g].style.width=d.offsetWidth}else i||(i=e.setInterval(f,500))}var h,i;a.browser.ie&&a.config.frame_theme!=="cnn2"&&d(f);a.trigger("loader.onReady");h=c.getElementById("dsq-content")||c.createElement("div");h.id="dsq-content";
h.style.display="none";c.getElementById(a.config.container_id).appendChild(h);a.container=c.getElementById("dsq-content");try{a.browser.ie6&&c.execCommand("BackgroundImageCache",!1,!0)}catch(j){}a.config.page.lazy="0";var m=a.partial(t,b),n=a.partial(a.require,a.config.json_url,a.config.page,!0,m);if(a.jsonData==null)return void n();a.defer(function(){var b=a.jsonData;return b&&(b.ready||b.lazy)},function(){if(a.jsonData.ready)return void m();a.once("disqus.viewed",function(){n()})})}});n();s();b();
v();(function(){function b(){d&&m(f)&&a.trigger("disqus.viewed")}var d=c.getElementById(a.config.container_id),f=p(d)[1];b();a.events.debounce(e,"scroll",b,250)})();a.bind("thread.onReady",function(){function b(){f&&m(f)&&a.trigger("comments.reply.viewed");h&&m(h)&&a.trigger("comments.viewed")}var d=c.getElementById("dsq-reply")||c.getElementById("dsq-new-post"),f=d?a.nodes.getPosition(d)[1]+d.offsetHeight:null,d=c.getElementById("dsq-comments"),h=a.nodes.getPosition(d)[1]+d.offsetHeight;b();a.events.debounce(e,
"scroll",b,250)});var w=d(new Date);a.bind("thread.onReady",function(){var b=a.comm.Default.recover(),c=d(new Date);b.log("load:start",w);b.log("load:length",c-w);try{e.jQuery?b.log("jslib","jquery:"+jQuery().jquery):e.jQuery&&jQuery.ui?b.log("jslib","jqueryui:"+jQuery.ui.version):e.Prototype?b.log("jslib","prototype:"+Prototype.Version):e.dojo?b.log("jslib","dojo:"+dojo.version.toString()):e.MooTools?b.log("jslib","mootools:"+MooTools.version):e.Ext?b.log("jslib","ext:"+Ext.version):e.YUI?b.log("jslib",
"yui:"+YUI.version):b.log("jslib","none")}catch(f){b.log("jslib","error")}b.flushLog(null)});a.bind("loader.onTemplateReady",function(){var b=a.comm.Default.recover(),c=a.jsonData;c.context.switches.sigma&&b.enable(c.context.sigma_chance);b.log("hit",1);c.forum.id&&b.addMeta("info:forum_id",c.forum.id);c.thread.id&&b.addMeta("info:thread_id",c.thread.id);c.request.user_type&&b.addMeta("info:user_type",c.request.user_type);c.request.user_id&&b.addMeta("info:user_id",c.request.user_id)});a.once("comments.viewed",
function(){a.comm.Default.recover().log("viewed:comments",1)});a.once("comments.reply.viewed",function(){a.comm.Default.recover().log("viewed:comment_box",1)})})(this);
