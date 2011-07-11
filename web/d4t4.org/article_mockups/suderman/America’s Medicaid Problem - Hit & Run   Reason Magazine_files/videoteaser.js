function onYouTubePlayerReady(playerid) {
	onYouTubePlayerReady.player = document.getElementById(playerid);
	if (onYouTubePlayerReady.loadurl) {
		onYouTubePlayerReady.player.loadVideoByUrl(onYouTubePlayerReady.loadurl, 0);
	}
}
onYouTubePlayerReady.player = null;
onYouTubePlayerReady.loadurl = null;
(function(){
	var videoteaser = $('div.videoteaser');
	var player = videoteaser.children('div.player');
	var overlay = videoteaser.children('div.overlay');
	var adselector = 'div.section.ads, div.col2 div.feature, div.logooverlay > div.header, div.google-ad, div.col2 object, div.col2 embed';
	function createplayer(url){
		onYouTubePlayerReady.player=false;
		var playerid = 'videoteaserplayer';
		var youtubeplayerurl = url+((url.indexOf('?')!==-1)?'&':'?')+'enablejsapi=1&version=3&fs=1&autoplay=1&color1=F3F3F3&color2=E6E6E6&playerapiid='+playerid;
		var youtubeswfargs = {
			allowscriptaccess: 'always',
			allowfullscreen: 'true'
		};
		swfobject.embedSWF(youtubeplayerurl, playerid, '640', '390', '8', '', {}, youtubeswfargs, {});
	}
	
	function YT_loadVideoByUrl(url) {
		if (onYouTubePlayerReady.player===null) { // not created
			createplayer(url);
		} else if (onYouTubePlayerReady.player===false) { // created but not ready
			onYouTubePlayerReady.loadurl = url;
		} else if (onYouTubePlayerReady.player) { // ready
			onYouTubePlayerReady.player.loadVideoByUrl(url, 0);
		}
	}
	
	function playvideo(e) {
		e.preventDefault();
		var vurl = this.title;
		var lurl = this.href;
		var title = $(this).find('span.description span').text();
		var play = function(){
			$(adselector).css('visibility','hidden');
			YT_loadVideoByUrl(vurl);
			updatesharinglinks(lurl, title);
		};
		if (player.is(':hidden')) {
			overlay.show();
			player.fadeIn('fast', play);
		} else {
			play();
		}
	}
	function closevideo(e) {
		e.preventDefault();
		if (onYouTubePlayerReady.player) {
			onYouTubePlayerReady.player.stopVideo();
		}
		player.fadeOut('fast', function(){
			$(adselector).css('visibility','visible');
			overlay.hide();
		});
	}
	
	var re_nofb = /\bnofb=1\b/;
	function updatesharinglinks(url, title) {
		title = 'reason.tv: '+title;
		var sharinglinks = {
			facebook : {
				'_src' : 'http://www.facebook.com/plugins/like.php',
				layout : 'standard',
				show_faces : 'false',
				width : '375',
				height : '23',
				action : 'like',
				colorscheme : 'light',
				href : url
			},
			twitter : {
				'_src' : 'http://platform.twitter.com/widgets/tweet_button.html',
				url : url,
				text : title
			},
			stumble : {
				'_href' : 'http://www.stumbleupon.com/submit',
				url : url,
				title : title
			},
			digg : {
				'_href' : 'http://digg.com/submit',
				phase : '2',
				url : url,
				title : title
			},
			reddit : {
				'_href' : 'http://reddit.com/submit',
				url : url,
				title : title
			}
		};
		
		var socials = player.find('div.social');
		var k, v, pk, pv, slink, attrname, attrval, baseurl, params, i;
		for (k in sharinglinks) {
			slink = socials.find('.'+k);
			if (slink.length) {
				v = sharinglinks[k];
				attrname = attrval = baseurl = '';
				params = {};
				for (pk in v) {
					pv = v[pk];
					if (pk.substr(0,1)==='_') {
						attrname = pk.substr(1);
						baseurl = pv;
					} else {
						params[pk] = pv;
					}
				}
				attrval = constructurl(baseurl, params);
			}
			if (slink.is('li')) {
				slink = slink.children();
			}
			var noiframe = re_nofb.test(document.cookie);
			for (i=0; i < slink.length; i+=1) {
				if (noiframe && attrname==='src') continue;
				slink.get(i)[attrname] = attrval;
			}
		}
	}
	
	function constructurl(url, params) {
		var finalurl = encodeURI(url);
		var qparams = [];
		var k;
		for (k in params) {
			qparams.push(encodeURIComponent(k)+'='+encodeURIComponent(params[k]));
		}
		qparams.sort();
		if (qparams.length) {
			finalurl += '?'+qparams.join('&');
		}
		return finalurl;
	}
	videoteaser.find('> div.videoteaser-container a').click(playvideo);
	videoteaser.find('div.close, div.closetext').add(overlay).click(closevideo);
	$(document).bind('keyup', function(e){
		if (e.which===27 && player.is(':visible')) {
			closevideo(e);
		}
	});
})();
