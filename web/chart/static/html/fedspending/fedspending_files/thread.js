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

    /* */ jsonData = {"reactions": [], "reactions_limit": 10, "ordered_highlighted": [], "posts": {"255161706": {"edited": false, "author_is_moderator": false, "from_request_user": null, "up_voted": false, "ip": "65.36.74.214", "last_modified_date": null, "dislikes": 0, "has_replies": false, "vote": false, "votable": true, "last_modified_by": null, "real_date": "2011-07-17_14:40:29", "date": "1 month ago", "message": "Look at the Clinton years vs. the Bush years.", "approved": true, "is_last_child": false, "can_edit": false, "can_reply": true, "likes": 0, "user_voted": null, "num_replies": 0, "down_voted": false, "is_first_child": false, "has_been_anonymized": false, "highlighted": false, "parent_post_id": null, "depth": 0, "points": 0, "user_key": "99b583d1b3c4bd6a268ba70b96a0aa10", "author_is_creator": false, "email": "cmrmarti@gmail.com", "killed": false, "is_realtime": false}}, "ordered_posts": [255161706], "realtime_enabled": false, "ready": true, "mediaembed": [], "has_more_reactions": false, "realtime_paused": true, "integration": {"receiver_url": "", "hide_user_votes": false, "reply_position": false, "disqus_logo": false}, "highlighted": {}, "reactions_start": 0, "media_url": "http://mediacdn.disqus.com/1315852078", "users": {"99b583d1b3c4bd6a268ba70b96a0aa10": {"username": "Cmrmarti", "tumblr": "", "about": "", "display_name": "Cmrmarti", "url": "http://disqus.com/guest/99b583d1b3c4bd6a268ba70b96a0aa10/", "registered": false, "remote_id": null, "linkedin": "", "blog": "", "remote_domain": "", "points": null, "facebook": "", "avatar": "http://mediacdn.disqus.com/1315852078/images/noavatar32.png", "delicious": "", "is_remote": false, "verified": false, "flickr": "", "twitter": "", "remote_domain_name": ""}}, "messagesx": {"count": 0, "unread": []}, "thread": {"voters_count": 0, "offset_posts": 0, "slug": "spending_is_bad_but_it8217s_not_that_bad", "paginate": false, "num_pages": 1, "days_alive": 0, "moderate_none": false, "voters": {}, "total_posts": 1, "realtime_paused": true, "queued": false, "pagination_type": "append", "user_vote": null, "likes": 2, "num_posts": 1, "closed": false, "per_page": 0, "id": 359488105, "killed": false, "moderate_all": false}, "forum": {"use_media": true, "avatar_size": 32, "apiKey": "I0Vki4XxlKRUt8RkLnBssey0NhsZRp41pVW8tDkbdbQjn7iE5l3LeD65YDgCbGSR", "comment_max_words": 0, "mobile_theme_disabled": false, "is_early_adopter": false, "login_buttons_enabled": true, "streaming_realtime": false, "reply_position": false, "id": 805154, "default_avatar_url": "http://mediacdn.disqus.com/1315852078/images/noavatar32.png", "template": {"mobile": {"url": "http://mediacdn.disqus.com/1315852078/build/themes/newmobile.js", "css": "http://mediacdn.disqus.com/1315852078/build/themes/newmobile.css"}, "url": "http://mediacdn.disqus.com/1315852078/build/themes/t_b3e3e393c77e35a4a3f3cbd1e429b5dc.js?1", "api": "1.1", "name": "Houdini", "css": "http://mediacdn.disqus.com/1315852078/build/themes/t_b3e3e393c77e35a4a3f3cbd1e429b5dc.css?1"}, "max_depth": 0, "lastUpdate": "", "use_old_templates": false, "linkbacks_enabled": true, "allow_anon_votes": true, "revert_new_login_flow": false, "stylesUrl": "http://mediacdn.disqus.com/uploads/styles/80/5154/datacollective.css", "show_avatar": true, "reactions_enabled": true, "disqus_auth_disabled": false, "name": "The Data Collective", "language": "en", "mentions_enabled": false, "url": "datacollective", "allow_anon_post": true, "thread_votes_disabled": false, "hasCustomStyles": false, "moderate_all": false}, "settings": {"realtimeHost": "qq.disqus.com", "uploads_url": "http://media.disqus.com/uploads", "ssl_media_url": "https://securecdn.disqus.com/1315852078", "realtime_url": "http://rt.disqus.com/forums/realtime-cached.js", "facebook_app_id": "52254943976", "minify_js": true, "recaptcha_public_key": "6LdKMrwSAAAAAPPLVhQE9LPRW4LUSZb810_iaa8u", "read_only": false, "facebook_api_key": "4aaa6c7038653ad2e4dbeba175a679ba", "realtimePort": "80", "debug": false, "disqus_url": "http://disqus.com", "media_url": "http://mediacdn.disqus.com/1315852078"}, "ranks": {}, "request": {"sort": 4, "is_authenticated": true, "user_type": "verified", "subscribe_on_post": null, "missing_perm": null, "user_id": 158291, "remote_domain_name": "", "remote_domain": "", "is_verified": true, "email": "dsjoerg@gmail.com", "profile_url": "", "username": "dsjoerg", "is_global_moderator": false, "sharing": {"twitter": {"auto": false, "enabled": true}, "facebook": {"auto": false, "enabled": false}, "yahoo": {"auto": false, "enabled": false}}, "timestamp": "2011-09-13_14:33:38", "is_moderator": true, "likes_count": 5, "forum": "datacollective", "is_initial_load": true, "display_username": "dsjoerg", "points": 5, "comments_count": 22, "moderator_can_edit": true, "is_remote": false, "userkey": "dsjoerg", "page": 1}, "context": {"use_twitter_signin": true, "use_fb_connect": true, "show_reply": true, "active_switches": ["bespin", "community_icon", "embedapi", "google_auth", "mentions", "new_facebook_auth", "realtime_cached", "ssl", "static_reply_frame", "static_styles", "statsd_created", "upload_media", "use_rs_paginator_60m"], "sigma_chance": 10, "use_google_signin": false, "switches": {"olark_admin_addons": true, "listactivity_replies": true, "olark_addons": true, "upload_media": true, "vip_read_slave": true, "embedapi": true, "ssl": true, "html_email": true, "moderate_ascending": true, "community_icon": true, "send_to_impermium": true, "olark_admin_packages": true, "static_styles": true, "stats": true, "google_auth": true, "listactivity_replies_30d": true, "statsd.timings": true, "realtime_cached": true, "statsd_created": true, "bespin": true, "olark_support": true, "use_rs_paginator_60m": true, "mentions": true, "olark_install": true, "new_facebook_auth": true, "limit_get_posts_days_30d": true, "compare_spam": true, "static_reply_frame": true}, "forum_facebook_key": "", "use_yahoo": true, "subscribed": false, "active_gargoyle_switches": ["compare_spam", "html_email", "limit_get_posts_days_30d", "listactivity_replies", "listactivity_replies_30d", "moderate_ascending", "olark_addons", "olark_admin_addons", "olark_admin_packages", "olark_install", "olark_support", "send_to_impermium", "stats", "statsd.timings", "vip_read_slave"], "realtime_speed": 15000, "use_openid": true}}; /* */
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
    login: 'http://disqus.com/profile/login/',
    logout: 'http://disqus.com/logout/',
    upload_remove: 'http://datacollective.disqus.com/thread/spending_is_bad_but_it8217s_not_that_bad/async_media_remove/',
    request_user_profile: 'http://disqus.com/dsjoerg/',
    request_user_avatar: 'http://mediacdn.disqus.com/uploads/users/15/8291/avatar92.jpg?1315516997',
    verify_email: 'http://disqus.com/verify/',
    remote_settings: 'http://datacollective.disqus.com/_auth/embed/remote_settings/',
    embed_thread: 'http://datacollective.disqus.com/thread.js',
    embed_vote: 'http://datacollective.disqus.com/vote.js',
    embed_thread_vote: 'http://datacollective.disqus.com/thread_vote.js',
    embed_thread_share: 'http://datacollective.disqus.com/thread_share.js',
    embed_queueurl: 'http://datacollective.disqus.com/queueurl.js',
    embed_hidereaction: 'http://datacollective.disqus.com/hidereaction.js',
    embed_more_reactions: 'http://datacollective.disqus.com/more_reactions.js',
    embed_subscribe: 'http://datacollective.disqus.com/subscribe.js',
    embed_highlight: 'http://datacollective.disqus.com/highlight.js',
    embed_block: 'http://datacollective.disqus.com/block.js',
    update_moderate_all: 'http://datacollective.disqus.com/update_moderate_all.js',
    update_days_alive: 'http://datacollective.disqus.com/update_days_alive.js',
    show_user_votes: 'http://datacollective.disqus.com/show_user_votes.js',
    forum_view: 'http://datacollective.disqus.com/spending_is_bad_but_it8217s_not_that_bad',
    cnn_saml_try: 'http://disqus.com/saml/cnn/try/',
    realtime: DISQUS.jsonData.settings.realtime_url,
    thread_view: 'http://datacollective.disqus.com/thread/spending_is_bad_but_it8217s_not_that_bad/',
    twitter_connect: DISQUS.jsonData.settings.disqus_url + '/_ax/twitter/begin/',
    yahoo_connect: DISQUS.jsonData.settings.disqus_url + '/_ax/yahoo/begin/',
    openid_connect: DISQUS.jsonData.settings.disqus_url + '/_ax/openid/begin/',
    googleConnect: DISQUS.jsonData.settings.disqus_url + '/_ax/google/begin/',
    community: 'http://datacollective.disqus.com/community.html',
    admin: 'http://datacollective.disqus.com/admin/moderate/',
    moderate: 'http://datacollective.disqus.com/admin/moderate/',
    moderate_threads: 'http://datacollective.disqus.com/admin/moderate-threads/',
    settings: 'http://datacollective.disqus.com/admin/settings/',
    unmerged_profiles: 'http://disqus.com/embed/profile/unmerged_profiles/',

    channels: {
        def:      'http://disqus.com/default.html', /* default channel */
        auth:     'https://secure.disqus.com/embed/login.html',
        tweetbox: 'http://disqus.com/forums/integrations/twitter/tweetbox.html?f=datacollective',
        edit:     'http://datacollective.disqus.com/embed/editcomment.html',

        
        
        reply:    'http://mediacdn.disqus.com/1315852078/build/system/reply.html',
        upload:   'http://mediacdn.disqus.com/1315852078/build/system/upload.html',
        sso:      'http://mediacdn.disqus.com/1315852078/build/system/sso.html',
        facebook: 'http://mediacdn.disqus.com/1315852078/build/system/facebook.html'
        
        
    }
};
