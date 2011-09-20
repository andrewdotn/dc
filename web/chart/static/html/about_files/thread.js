/*jslint evil:true */
/**
 * Dynamic thread loader
 *
 * 
 * 
 * 
 * 
 * 
*/

// 
var DISQUS;
if (!DISQUS || typeof DISQUS == 'function') {
    throw "DISQUS object is not initialized";
}
// 

// json_data and default_json django template variables will close
// and re-open javascript comment tags

(function () {
    var jsonData, cookieMessages, session, key;

    /* */ jsonData = {"reactions": [], "reactions_limit": 10, "ordered_highlighted": [], "posts": {}, "ordered_posts": [], "realtime_enabled": false, "ready": true, "mediaembed": [], "has_more_reactions": false, "realtime_paused": true, "integration": {"receiver_url": null, "hide_user_votes": false, "reply_position": true, "disqus_logo": false}, "highlighted": {}, "reactions_start": 0, "media_url": "https://securecdn.disqus.com/1316454436", "users": {}, "messagesx": {"count": 0, "unread": []}, "thread": {"voters_count": 0, "offset_posts": 0, "slug": "thread_06", "paginate": false, "num_pages": 1, "days_alive": 0, "moderate_none": false, "voters": {}, "total_posts": 0, "realtime_paused": true, "queued": false, "pagination_type": "append", "user_vote": null, "likes": 0, "num_posts": 0, "closed": false, "per_page": 0, "id": 412478771, "killed": false, "moderate_all": false}, "forum": {"use_media": true, "avatar_size": 32, "apiKey": "4eVeUHY7WEteiVxMAOGyeNYdWihrTIdC3BibuZWKlLZFn3k86QN1d5VfhbHpohs1", "features": {}, "use_old_templates": false, "comment_max_words": 0, "mobile_theme_disabled": false, "linkbacks_enabled": true, "is_early_adopter": false, "allow_anon_votes": true, "revert_new_login_flow": false, "stylesUrl": "http://mediacdn.disqus.com/uploads/styles/87/7834/d4t4.css", "login_buttons_enabled": true, "streaming_realtime": false, "show_avatar": true, "reactions_enabled": true, "reply_position": true, "id": 877834, "name": "d4t4.org", "language": "en", "mentions_enabled": false, "url": "d4t4", "allow_anon_post": true, "disqus_auth_disabled": false, "thread_votes_disabled": false, "default_avatar_url": "https://securecdn.disqus.com/1316454436/images/noavatar32.png", "ranks_enabled": false, "template": {"mobile": {"url": "https://securecdn.disqus.com/1316454436/build/themes/newmobile.js", "css": "https://securecdn.disqus.com/1316454436/build/themes/newmobile.css"}, "url": "https://securecdn.disqus.com/1316454436/build/themes/t_c4ca4238a0b923820dcc509a6f75849b.js?1", "api": "1.0", "name": "Narcissus", "css": "https://securecdn.disqus.com/1316454436/build/themes/t_c4ca4238a0b923820dcc509a6f75849b.css?1"}, "hasCustomStyles": false, "max_depth": 0, "lastUpdate": 1309146841, "moderate_all": false}, "settings": {"realtimeHost": "qq.disqus.com", "uploads_url": "http://media.disqus.com/uploads", "ssl_media_url": "https://securecdn.disqus.com/1316454436", "realtime_url": "http://rt.disqus.com/forums/realtime-cached.js", "facebook_app_id": "52254943976", "minify_js": true, "recaptcha_public_key": "6LdKMrwSAAAAAPPLVhQE9LPRW4LUSZb810_iaa8u", "read_only": false, "facebook_api_key": "4aaa6c7038653ad2e4dbeba175a679ba", "realtimePort": "80", "debug": false, "disqus_url": "http://disqus.com", "media_url": "https://securecdn.disqus.com/1316454436"}, "ranks": {}, "request": {"sort": 4, "is_authenticated": true, "user_type": "verified", "subscribe_on_post": null, "missing_perm": null, "user_id": 158291, "remote_domain_name": "", "remote_domain": "", "is_verified": true, "email": "dsjoerg@gmail.com", "profile_url": "", "username": "dsjoerg", "is_global_moderator": false, "sharing": {"twitter": {"auto": false, "enabled": true}, "facebook": {"auto": false, "enabled": false}, "yahoo": {"auto": false, "enabled": false}}, "timestamp": "2011-09-20_14:49:35", "is_moderator": true, "likes_count": 5, "forum": "d4t4", "is_initial_load": true, "display_username": "dsjoerg", "points": 5, "comments_count": 22, "moderator_can_edit": true, "is_remote": false, "userkey": "dsjoerg", "page": 1}, "context": {"use_twitter_signin": true, "use_fb_connect": true, "show_reply": true, "active_switches": ["bespin", "community_icon", "embedapi", "google_auth", "mentions", "new_facebook_auth", "realtime_cached", "ssl", "static_reply_frame", "static_styles", "statsd_created", "upload_media", "use_rs_paginator_60m"], "sigma_chance": 10, "use_google_signin": false, "switches": {"olark_admin_addons": true, "listactivity_replies": true, "use_impermium": true, "olark_addons": true, "upload_media": true, "vip_read_slave": true, "embedapi": true, "ssl": true, "html_email": true, "moderate_ascending": true, "community_icon": true, "send_to_impermium": true, "olark_admin_packages": true, "static_styles": true, "train_impermium": true, "stats": true, "google_auth": true, "listactivity_replies_30d": true, "statsd.timings": true, "realtime_cached": true, "statsd_created": true, "bespin": true, "olark_support": true, "use_rs_paginator_60m": true, "mentions": true, "olark_install": true, "new_facebook_auth": true, "limit_get_posts_days_30d": true, "compare_spam": true, "static_reply_frame": true}, "forum_facebook_key": "", "use_yahoo": true, "subscribed": false, "active_gargoyle_switches": ["compare_spam", "html_email", "limit_get_posts_days_30d", "listactivity_replies", "listactivity_replies_30d", "moderate_ascending", "olark_addons", "olark_admin_addons", "olark_admin_packages", "olark_install", "olark_support", "send_to_impermium", "stats", "statsd.timings", "train_impermium", "use_impermium", "vip_read_slave"], "realtime_speed": 15000, "use_openid": true}}; /* */
    /* */ cookieMessages = {"user_created": null, "post_has_profile": null, "post_twitter": null, "post_not_approved": null}; session = {"url": null, "name": null, "email": null}; /* */

    DISQUS.jsonData = jsonData;
    DISQUS.jsonData.cookie_messages = cookieMessages;
    DISQUS.jsonData.session = session;

    if (DISQUS.useSSL) {
        DISQUS.useSSL(DISQUS.jsonData.settings);
    }

    // The mappings below are for backwards compatibility--before we port all the code that
    // accesses jsonData.settings to DISQUS.settings

    var mappings = {
        debug:                'disqus.debug',
        minify_js:            'disqus.minified',
        read_only:            'disqus.readonly',
        recaptcha_public_key: 'disqus.recaptcha.key',
        facebook_app_id:      'disqus.facebook.appId',
        facebook_api_key:     'disqus.facebook.apiKey'
    };

    var urlMappings = {
        disqus_url:    'disqus.urls.main',
        media_url:     'disqus.urls.media',
        ssl_media_url: 'disqus.urls.sslMedia',
        realtime_url:  'disqus.urls.realtime',
        uploads_url:   'disqus.urls.uploads'
    };

    if (DISQUS.jsonData.context.switches.realtime_setting_change) {
        urlMappings.realtimeHost = 'realtime.host';
        urlMappings.realtimePort = 'realtime.port';
    }
    for (key in mappings) {
        if (mappings.hasOwnProperty(key)) {
            DISQUS.settings.set(mappings[key], DISQUS.jsonData.settings[key]);
        }
    }

    for (key in urlMappings) {
        if (urlMappings.hasOwnProperty(key)) {
            DISQUS.jsonData.settings[key] = DISQUS.settings.get(urlMappings[key]);
        }
    }
}());

DISQUS.jsonData.context.csrf_token = '2c363eb300475618523059ead4a30a55';

DISQUS.jsonData.urls = {
    login: '//disqus.com/profile/login/',
    logout: '//disqus.com/logout/',
    upload_remove: '//d4t4.disqus.com/thread/thread_06/async_media_remove/',
    request_user_profile: '//disqus.com/dsjoerg/',
    request_user_avatar: 'https://securecdn.disqus.com/uploads/users/15/8291/avatar92.jpg?1315516997',
    verify_email: '//disqus.com/verify/',
    remote_settings: '//d4t4.disqus.com/_auth/embed/remote_settings/',
    embed_thread: '//d4t4.disqus.com/thread.js',
    embed_vote: '//d4t4.disqus.com/vote.js',
    embed_thread_vote: '//d4t4.disqus.com/thread_vote.js',
    embed_thread_share: '//d4t4.disqus.com/thread_share.js',
    embed_queueurl: '//d4t4.disqus.com/queueurl.js',
    embed_hidereaction: '//d4t4.disqus.com/hidereaction.js',
    embed_more_reactions: '//d4t4.disqus.com/more_reactions.js',
    embed_subscribe: '//d4t4.disqus.com/subscribe.js',
    embed_highlight: '//d4t4.disqus.com/highlight.js',
    embed_block: '//d4t4.disqus.com/block.js',
    update_moderate_all: '//d4t4.disqus.com/update_moderate_all.js',
    update_days_alive: '//d4t4.disqus.com/update_days_alive.js',
    show_user_votes: '//d4t4.disqus.com/show_user_votes.js',
    forum_view: '//d4t4.disqus.com/thread_06',
    cnn_saml_try: '//disqus.com/saml/cnn/try/',
    realtime: DISQUS.jsonData.settings.realtime_url,
    thread_view: '//d4t4.disqus.com/thread/thread_06/',
    twitter_connect: DISQUS.jsonData.settings.disqus_url + '/_ax/twitter/begin/',
    yahoo_connect: DISQUS.jsonData.settings.disqus_url + '/_ax/yahoo/begin/',
    openid_connect: DISQUS.jsonData.settings.disqus_url + '/_ax/openid/begin/',
    googleConnect: DISQUS.jsonData.settings.disqus_url + '/_ax/google/begin/',
    community: '//d4t4.disqus.com/community.html',
    admin: '//d4t4.disqus.com/admin/moderate/',
    moderate: '//d4t4.disqus.com/admin/moderate/',
    moderate_threads: '//d4t4.disqus.com/admin/moderate-threads/',
    settings: '//d4t4.disqus.com/admin/settings/',
    unmerged_profiles: 'http://disqus.com/embed/profile/unmerged_profiles/',

    channels: {
        def:      'http://disqus.com/default.html', /* default channel */
        auth:     'https://secure.disqus.com/embed/login.html',
        tweetbox: 'http://disqus.com/forums/integrations/twitter/tweetbox.html?f=d4t4',
        edit:     '//d4t4.disqus.com/embed/editcomment.html',

        
        
        reply:    'https://securecdn.disqus.com/1316454436/build/system/reply_ssl.html',
        upload:   'https://securecdn.disqus.com/1316454436/build/system/upload_ssl.html',
        sso:      'https://securecdn.disqus.com/1316454436/build/system/sso_ssl.html',
        facebook: 'https://securecdn.disqus.com/1316454436/build/system/facebook_ssl.html'
        
        
    }
};
