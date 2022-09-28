JSDATA = """
var data = {{ "search": {{ "currentPage": 1, "ids": [{FLAT_IDS}], "regionId": 105, "isOnMap": false, "userId": null, "parameters": {{ "section": "arenda", "category": "kvartiry", "regionAlias": "nur-sultan", "das[_sys.hasphoto]": "1", "das[price][to]": "10000", "das[rent.period]": "1" }}, "nbTotal": "1 497" }}, "category": {{ "id": 2, "hasPrice": true, "name": "rent.flat", "sectionName": "rent", "categoryName": "flat", "defaultCurrency": 2 }}, "svgIconsUrl": "//krisha.kz/static/frontend/svg/sprite-icons.73833fc512.svg", "svgLandingUrl": "//krisha.kz/static/frontend/svg/sprite-landing.49c562a566.svg", "app": "Frontend", "baseHostname": "krisha.kz", "mobileHostname": "m.krisha.kz", "cookieDomain": ".krisha.kz", "isRemoteResourcesEnabled": true, "isDebug": false, "isWebView": false, "route": "advert:search", "controller": "a", "action": "search", "ab": [], "user": {{ "email": null, "typeAlias": null, "isGuest": true, "isOwner": false, "isPro": false, "isSpecialist": false, "isCompany": false, "isBuilderOrComplex": false, "isBuilder": false, "isComplex": false, "isStatusVerified": false, "id": null, "globalId": null, "name": null, "identificationInfo": null, "accountFill": null, "locale": "", "xdmAssetUrl": "https://id.kolesa.kz/authToken.js" }}, "photoHost": "photos-kr.kcdn.kz", "views": {{ "host": "http://views:8080", "location": "ms/views" }}, "centrifuge": {{ "url": "wss://ws.krisha.kz/v2/connection/websocket" }}, "config": {{ "isProduction": true, "sentry": {{ "isEnabled": true, "blackList": "closest, window.Ya.adfoxCode, adFoxAdaptive, NS_ERROR_STORAGE_IOERR, enterprise" }}, "bucky": {{ "host": "/ms/rum", "aggregationInterval": 100, "sample": 10 }}, "photosCDN": {{ "cookieName": "kr_cdn_host", "defaultHost": "photos-kr.kcdn.kz" }}, "staticLink": "//krisha.kz/static/frontend", "nps": {{ "url": "/ms/nps" }}, "region": {{ "autocompleteUrl": "/region/ajaxAutocomplete", "parentChainUrl": "/region/ajaxParentChain" }} }}, "appUrl": "https://app.krisha.kz", "appToken": "RBHaZuZT7wV2gBXImVOzTdkoRA0FzN1z%2B5MSCDglBO%2BFWDoC8bMcDjAKc1vj8Oao4UTGratFFEled6Xs1oqByi3%2FU1Q%2Fb8MTxWu%2Fm7XDFU%2BpZq%2FhPc4jje1FjFbCyNJ7AvgLKz9snN12qCUNfjxOJm410mVkhOouyHObnBHf%2BtAG1V%2BNF4AtyL8x1aMdn%2BpcY6WFjBppcTaH3gAt3dMf%2B0LsFBrx4a%2BgErP6yaLzMwA%3D" }};
"""

TEMPLATE ="""
<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8" />
    <meta http-equiv="x-ua-compatible" content="ie=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <base href="https://krisha.kz" />
    <title>Снять квартиру 🏘 посуточно в вашем городе – объявления на Крыше</title>
    <meta name="description"
        content="На «Крыше» можно ⭐ снять или сдать квартиру ⭐ посуточно в вашем городе. Актуальные объявления об аренде квартир в вашем городе. Размещайте объявления!" />
    <link rel="alternate"
        href="https://krisha.kz/arenda/kvartiry/nur-sultan/?das%5B_sys.hasphoto%5D=1&das%5Bprice%5D%5Bto%5D=10000&das%5Brent.period%5D=1"
        hreflang="ru" />
    <link rel="alternate"
        href="https://krisha.kz/kz/arenda/kvartiry/nur-sultan/?das%5B_sys.hasphoto%5D=1&das%5Bprice%5D%5Bto%5D=10000&das%5Brent.period%5D=1"
        hreflang="kz" />
    <link rel="canonical" href="https://krisha.kz/arenda/kvartiry/nur-sultan/?das[rent.period]=1" />
    <link
        href="https://m.krisha.kz/arenda/kvartiry/nur-sultan/?das%5B_sys.hasphoto%5D=1&amp;das%5Bprice%5D%5Bto%5D=10000&amp;das%5Brent.period%5D=1"
        media="only screen and (max-width: 640px)" rel="alternate" />
    <link rel="icon" type="image/png" href="//krisha.kz/static/frontend/favicons/favicon-64x64.png" sizes="64x64">
    <link rel="icon" type="image/png" href="//krisha.kz/static/frontend/favicons/favicon-32x32.png" sizes="32x32">
    <link rel="icon" type="image/png" href="//krisha.kz/static/frontend/favicons/favicon-16x16.png" sizes="16x16">
    <link rel="icon" type="image/x-icon" href="//krisha.kz/static/frontend/favicons/favicon.ico">

    <link rel="apple-touch-icon" sizes="57x57" href="//krisha.kz/static/frontend/favicons/apple-touch-icon-57x57.png">
    <link rel="apple-touch-icon" sizes="76x76" href="//krisha.kz/static/frontend/favicons/apple-touch-icon-76x76.png">
    <link rel="apple-touch-icon" sizes="120x120"
        href="//krisha.kz/static/frontend/favicons/apple-touch-icon-120x120.png">
    <link rel="apple-touch-icon" sizes="152x152"
        href="//krisha.kz/static/frontend/favicons/apple-touch-icon-152x152.png">
    <link rel="apple-touch-icon" sizes="180x180" href="//krisha.kz/static/frontend/favicons/apple-touch-icon.png">
    <link rel="icon" type="image/png" href="//krisha.kz/static/frontend/favicons/android-chrome-192x192.png"
        sizes="192x192">

    <link rel="manifest" href="//krisha.kz/static/frontend/manifest.json">
    <meta name="msapplication-config" content="//krisha.kz/static/frontend/browserconfig.xml" />
    <meta name="apple-mobile-web-app-title" content="Krisha.kz">
    <meta name="application-name" content="Krisha.kz">
    <meta name="theme-color" content="#ffdd61">
    <meta name="og:title" content="Снять квартиру 🏘 посуточно в вашем городе – объявления на Крыше" />
    <meta name="og:url" content="https://krisha.kz/arenda/kvartiry/nur-sultan/?das[rent.period]=1" />
    <meta name="og:image" content="//krisha.kz/static/frontend/images/og-logo.png" />
    <meta name="og:site_name" content="Krisha.kz" />
    <meta name="yandex-verification" content="f4a558e742872677" />
    <meta property="fb:pages" content="453858631376956" />
    <script type="application/ld+json">
        {{
            "@context": "http://schema.org",
            "@type": ["Apartment", "Product"],
            "name": "Снять квартиру 🏘 посуточно в вашем городе – объявления на Крыше",
            "description": "На «Крыше» можно ⭐ снять или сдать квартиру ⭐ посуточно в вашем городе. Актуальные объявления об аренде квартир в вашем городе. Размещайте объявления!"
                        ,
            "offers": {{
                "@type": "AggregateOffer",
                "offerCount": "1497",
                "highPrice": "10000",
                "lowPrice": "1000",
                "priceCurrency": "KZT"
            }}
                    }}
    </script>
    <script id="jsdata">
        {JSDATA}
    </script>

    <link rel="preload" href="//krisha.kz/static/frontend/fonts/OpenSans-Regular.woff2" as="font" type="font/woff2"
        crossorigin="anonymous">
    <link rel="preload" href="//krisha.kz/static/frontend/fonts/OpenSans-Semibold.woff2" as="font" type="font/woff2"
        crossorigin="anonymous">



    <link rel="stylesheet" type="text/css" href="//krisha.kz/static/frontend/css/main-common.f5acc58e9f.css" />


    <script type="application/javascript">var YaDirectParams = {{
            stat_id: 5,
            ad_format: "direct",
            font_size: 1,
            type: "oldHorizontal",
            limit: 1,
            title_font_size: 3,
            links_underline: true,
            site_bg_color: "FFF2CF",
            bg_color: "FFF2CF",
            title_color: "996633",
            url_color: "0066CC",
            text_color: "996633",
            hover_color: "FF0000",
            favicon: true,
            no_sitelinks: true
        }};
        ;
        var googletag = googletag || {{}};
        googletag.cmd = googletag.cmd || [];
        googletag.cmd.push(function () {{
            googletag.defineSlot('/21685517069/Krisha_Homepage_Top_new', [[970, 90], [900, 90], [980, 90], [728, 90]], 'div-gpt-ad-1536297276650-0').addService(googletag.pubads());
            googletag.defineSlot('/21685517069/Krisha_Search_Leaderboard_new', [[468, 60], [550, 80], [728, 90]], 'div-gpt-ad-1536300331333-0').addService(googletag.pubads());
            googletag.defineSlot('/21685517069/Krisha_Search_Right_new', [[240, 400], [300, 250]], 'div-gpt-ad-1536300503358-0').addService(googletag.pubads());
            googletag.defineSlot('/21685517069/Krisha_Search_Right2_new', [[300, 250], [240, 400]], 'div-gpt-ad-1536300745208-0').addService(googletag.pubads());
            googletag.defineSlot('/21685517069/Krisha_Search_Leaderboard2_new', [[550, 80], [468, 60], [728, 90]], 'div-gpt-ad-1536300838629-0').addService(googletag.pubads());
            googletag.defineSlot('/47763208/krisha_icon_search', [[310, 87]], 'div-gpt-ad-1498821549802-0').addService(googletag.pubads());
            googletag.defineSlot('/47763208/krisha_icon_search', [[310, 87]], 'div-gpt-ad-1498476236129-0').addService(googletag.pubads());
            googletag.defineSlot('/47763208/krisha_icon_search', [[310, 87]], 'div-gpt-ad-1498476581453-0').addService(googletag.pubads());
            googletag.defineSlot('/47763208/krisha_icon_search', [[310, 87]], 'div-gpt-ad-1498476634002-0').addService(googletag.pubads());
            googletag.defineSlot('/47763208/krisha_icon_search', [[310, 87]], 'div-gpt-ad-1498540120368-0').addService(googletag.pubads());
            googletag.defineSlot('/47763208/krisha_icon_search', [[310, 87]], 'div-gpt-ad-1498540148673-0').addService(googletag.pubads());
            googletag.defineSlot('/47763208/krisha_icon_search', [[310, 87]], 'div-gpt-ad-1498540179932-0').addService(googletag.pubads());
            googletag.defineSlot('/47763208/krisha_icon_search', [[310, 87]], 'div-gpt-ad-1498540200272-0').addService(googletag.pubads());
            googletag.defineSlot('/47763208/krisha_ns_search_2', [[550, 150]], 'div-gpt-ad-1516786457462-0').addService(googletag.pubads());

            googletag.pubads().collapseEmptyDivs();
            googletag.pubads().setTargeting('kr_category', 'Аренда');
            googletag.pubads().setTargeting('kr_type', 'Квартиры');
            googletag.pubads().setTargeting('kr_city', 'Астана');
            googletag.pubads().setTargeting('kr_price', '0-18000000');

            googletag.enableServices();
        }});
        function adFoxAdaptive(data) {{
            var params = {{
                ownerId: 260188,
                containerId: data.id,
                params: {{
                    pp: data.pp || '',
                    ps: data.ps || '',
                    p1: data.p1 || '',
                    p2: data.p2 || '',
                    puid1: '',
                    puid2: '',
                    puid3: ''
                }}
            }};

            var devices = ['desktop', 'tablet', 'phone'];
            var deviceOptions = {{
                tabletWidth: 830,
                phoneWidth: 480,
                isAutoReloads: false
            }};

            if (window.Ya && window.Ya.adfoxCode) {{
                window.Ya.adfoxCode.createAdaptive(params, devices, deviceOptions);
            }} else {{
                window.addEventListener('DOMContentLoaded', function () {{
                    if (window.Ya && window.Ya.adfoxCode) {{
                        window.Ya.adfoxCode.createAdaptive(params, devices, deviceOptions);
                    }}
                }});
            }}
        }}</script>
    <script src="https://yastatic.net/pcode/adfox/loader.js" crossorigin="anonymous" defer></script>
    <script src="https://an.yandex.ru/system/widget.js" async></script>

    <script
        type="text/javascript">window.digitalData = {{ "version": "1.1.2", "website": {{ "type": "desktop", "section": "krisha", "language": "ru", "currency": "KZT", "environment": "production" }}, "page": {{ "type": "search", "category": "Search Listing", "referrer": "" }}, "user": {{ "isLoggedIn": false, "isReturning": false, "email": "", "experimentId": "" }}, "listing": {{ "section": "rent", "category_string": "flat", "category": ["rent", "flat"], "categoryId": 2, "currentPage": 1, "resultCount": 1497, "pagesCount": 75, "sortBy": "по умолчанию", "query": null, "listName": "search", "layout": "list", "listId": "main", "filters": [{{ "region": "KZ-AKM", "city": "nur-sultan" }}] }} }};</script>
    <script type="text/javascript">
        (function (h, d) {{ d = d || "cdn.segmentstream.com"; var a = window.segmentstream = window.segmentstream || []; window.ddListener = window.ddListener || []; var b = window.digitalData = window.digitalData || {{}}; b.events = b.events || []; b.changes = b.changes || []; if (!a.initialize) if (a.invoked) window.console && console.error && console.error("SegmentStream snippet included twice."); else {{ a.invoked = !0; a.methods = "initialize addIntegration persist unpersist on once off getConsent setConsent".split(" "); a.factory = function (k) {{ return function () {{ var c = Array.prototype.slice.call(arguments); c.unshift(k); a.push(c); return a }} }}; for (b = 0; b < a.methods.length; b++) {{ var f = a.methods[b]; a[f] = a.factory(f) }} a.load = function (a) {{ var c = document.createElement("script"); c.type = "text/javascript"; c.charset = "utf-8"; c.async = !0; c.src = a; a = document.getElementsByTagName("script")[0]; a.parentNode.insertBefore(c, a) }}; a.loadProject = function (b) {{ var c = window.location.search; if (0 <= c.indexOf("segmentstream_test_mode=1")) try {{ var e = !0; window.localStorage.setItem("_segmentstream_test_mode", "1") }} catch (g) {{ }} else if (0 <= c.indexOf("segmentstream_test_mode=0")) try {{ e = !1, window.localStorage.removeItem("_segmentstream_test_mode") }} catch (g) {{ }} else try {{ e = "1" === window.localStorage.getItem("_segmentstream_test_mode") }} catch (g) {{ }} e ? a.load(window.SEGMENTSTREAM_TESTMODE_INIT_URL || "https://api.segmentstream.com/v1/project/" + b + ".js") : a.load(window.SEGMENTSTREAM_INIT_URL || "https://" + d + "/project/" + b + ".js") }}; a.CDN_DOMAIN = d; a.SNIPPET_VERSION = "2.0.0"; a.loadProject(h) }} }})("17dd2b97-af09-4af6-9ad0-ad31a2713544");
    </script>

    <script type='text/javascript'>
        (function (i, s, o, g, r, a, m) {{
            i['GoogleAnalyticsObject'] = r;
            i[r] = i[r] || function () {{
                (i[r].q = i[r].q || []).push(arguments)
            }}, i[r].l = 1 * new Date();
            a = s.createElement(o),
                m = s.getElementsByTagName(o)[0];
            a.async = 1;
            a.src = g;
            m.parentNode.insertBefore(a, m)
        }})(window, document, 'script', 'https://www.google-analytics.com/analytics.js', 'ga');

        ga('create', 'UA-20095530-1', 'krisha.kz');
        ga('require', 'GTM-PM9LL5D');

        var utmcampaign, utmsource, utmcontent;

        var OpenStatParser = {{
            _params: {{}},
            _parsed: false,
            _decode64: function (data) {{
                if (typeof window['atob'] === 'function') {{
                    return atob(data);
                }}

                var b64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=";
                var o1, o2, o3, h1, h2, h3, h4, bits, i = 0,
                    ac = 0,
                    dec = "",
                    tmp_arr = [];

                if (!data) {{
                    return data;
                }}

                data += '';

                do {{
                    h1 = b64.indexOf(data.charAt(i++));
                    h2 = b64.indexOf(data.charAt(i++));
                    h3 = b64.indexOf(data.charAt(i++));
                    h4 = b64.indexOf(data.charAt(i++));

                    bits = h1 << 18 | h2 << 12 | h3 << 6 | h4;

                    o1 = bits >> 16 & 0xff;
                    o2 = bits >> 8 & 0xff;
                    o3 = bits & 0xff;

                    if (h3 == 64) {{
                        tmp_arr[ac++] = String.fromCharCode(o1);
                    }} else if (h4 == 64) {{
                        tmp_arr[ac++] = String.fromCharCode(o1, o2);
                    }} else {{
                        tmp_arr[ac++] = String.fromCharCode(o1, o2, o3);
                    }}
                }} while (i < data.length);

                dec = tmp_arr.join('');

                return dec;
            }},
            _parse: function () {{
                var prmstr = window.location.search.substr(1);
                var prmarr = prmstr.split('&');
                this._params = {{}};

                for (var i = 0; i < prmarr.length; i++) {{
                    var tmparr = prmarr[i].split('=');
                    this._params[tmparr[0]] = tmparr[1];
                }}

                this._parsed = true;
            }},
            hasMarker: function () {{
                if (!this._parsed) {{
                    this._parse();
                }}
                return (typeof this._params['_openstat'] !== 'undefined') ? true : false;
            }},
            buildCampaignParams: function () {{
                if (!this.hasMarker()) {{
                    return false;
                }}

                var
                    openstat = this._decode64(this._params['_openstat']),
                    statarr = openstat.split(';');

                utmcampaign = statarr[3];
                utmsource = statarr[0];
                utmcontent = statarr[2];
            }}
        }};

        if (OpenStatParser.hasMarker()) {{
            var campaignParams = OpenStatParser.buildCampaignParams();

            if (campaignParams !== false) {{
                ga('set', {{
                    'campaignName': utmcampaign,
                    'campaignSource': utmsource,
                    'campaignMedium': 'cpc',
                    'campaignContent': utmcontent
                }});
            }}
        }}

        var advertPrice = '';

        // отправляем цену внутри объявления при первичном collect
        if ((window.data.route === 'a:show' || window.data.route === 'advert:show') && advertPrice) {{
            ga('set', 'metric1', advertPrice);
        }}

        if (digitalData.website && digitalData.website.type) {{
            ga('set', 'dimension8', digitalData.website.type);
        }}

        ga('require', 'displayfeatures');
        ga('send', 'pageview');
    </script>
    <script type="text/javascript" src="//static.criteo.net/js/ld/ld.js" async="true"></script>
    <script type="text/javascript">
        window.criteo_q = window.criteo_q || [];
    </script>
    <script>
        /**
         * Собирает ошибки по фоткам с хранилиша Крыши в window.photoLoadErrors
         */
        (function () {{
            window.photoLoadErrors = [];

            var KRISHA_IMAGE_PATTERN = 'photos-kr';
            var onError = function (e) {{
                var element = e.target;

                if (
                    (element.src && element.src.match(KRISHA_IMAGE_PATTERN)) ||
                    (element.srcset && element.srcset.match(KRISHA_IMAGE_PATTERN))
                ) {{
                    window.photoLoadErrors.push(element);
                }}
            }};

            // useCapture: true - чтобы сработал "захват" события сверху-вниз
            document.addEventListener('error', onError, true);
        }})();
    </script>
</head>

<body class="a-search-page favorites-not-updated">
    <script>
        (function () {{
            var isSvgSupported = document.implementation.hasFeature("http://www.w3.org/TR/SVG11/feature#Image", "1.1"),
                hasLocalStorage;

            try {{
                hasLocalStorage = 'localStorage' in window && window.localStorage !== null;
            }} catch (e) {{
                hasLocalStorage = false;
            }}

            function insertSvg(data) {{
                var div = document.createElement("div");

                div.className = 'svg-container';
                div.innerHTML = data;
                document.body.insertBefore(div, document.body.childNodes[0]);
            }}

            function getSvgSprite(name, url) {{
                var cacheKey = name,
                    urlKey = name + 'Url',
                    svgRequest,
                    cachedSvg;

                cachedSvg = hasLocalStorage ? localStorage.getItem(cacheKey) : null;

                if (cachedSvg && localStorage.getItem(urlKey) === url) {{
                    insertSvg(cachedSvg);
                }} else {{
                    svgRequest = new XMLHttpRequest();

                    svgRequest.open("GET", url, true);
                    svgRequest.send();
                    svgRequest.onload = function () {{
                        insertSvg(svgRequest.responseText);

                        if (hasLocalStorage) {{
                            localStorage.setItem(cacheKey, svgRequest.responseText);
                            localStorage.setItem(urlKey, url);
                        }}
                    }};
                }}
            }}

            if (isSvgSupported) {{
                if (window.data.svgIconsUrl) getSvgSprite('svgCache', window.data.svgIconsUrl);
                if (window.data.svgLandingUrl) getSvgSprite('svgLandingCache', window.data.svgLandingUrl);
            }}
        }})();
    </script>
    <div class="topb">
        <div class="common-b vip ddl_campaign" id="vip" data-campaign-id="vip">
            <div id='div-gpt-ad-1536297276650-0'>
                <script type="text/javascript">
                    googletag.cmd.push(function () {{

                        googletag.display('div-gpt-ad-1536297276650-0');
                    }});
                </script>
            </div>
            <div id='ya-vip'></div>
        </div>
    </div>
    <header class="header-public">
        <div class="primary-navbar-container">
            <div class="global-alert-container">
                <div class="global-alert-wrap">
                </div>
            </div>
            <div class="container header-wrap">
                <nav class="site-switcher">
                    <div class="main-header-logo">
                        <div class="main-header-logo__img"><svg role="img" class="icon icon-svg icon-logo-x3">
                                <use xlink:href="#icon-logo-x3"></use>
                            </svg></div>

                        <div class="main-header-logo__links">
                            <a class="main-header-logo__kolesa" href="https://kolesa.kz" data-toggle="tooltip"
                                data-placement="bottom" title="Автомобили"></a>

                            <div class="main-header-logo__krisha" data-toggle="tooltip" data-placement="bottom"
                                title="Недвижимость"></div>

                            <a class="main-header-logo__market"
                                href="https://market.kz/?utm_source=krisha.kz&utm_medium=link&utm_campaign=top_menu"
                                data-toggle="tooltip" data-placement="bottom" title="Товары и услуги"></a>
                        </div>
                    </div>
                </nav>

                <ul class="navbar-menu">
                    <li>
                        <div id="header-lang"></div>
                    </li>
                    <li class="favorites-link-item">
                        <a href="/favorites/advert/">Избранное</a>
                        <span class="navbar-badge fav-nb-value"></span>
                    </li>
                    <li class="registration-link-item">
                        <a href="/passport/register">Регистрация</a>
                    </li>
                    <li class="cabinet-link-item">
                        <a href="/my" class="cabinet-link">Личный кабинет</a>
                    </li>
                </ul>
            </div>
        </div>

        <div class="container">
            <div class="secondary-navbar ">
                <div class="logo-container">
                    <a href="/" class="logo">
                        <svg role="img" class="icon icon-svg icon-logo">
                            <use xlink:href="#icon-logo"></use>
                        </svg>
                    </a>
                </div>

                <nav class="main-menu">
                    <ul>
                        <li>
                            <a href="/prodazha/">
                                Продажа

                            </a>
                        </li>
                        <li class="is-active">
                            <a href="/arenda/">
                                Аренда

                            </a>
                        </li>
                        <li>
                            <a href="/valuation/">
                                Оценка

                                <span class="navbar-badge navbar-badge-active">New</span>
                            </a>
                        </li>
                        <li>
                            <a href="/pro/">
                                Компании и специалисты

                            </a>
                        </li>
                        <li>
                            <a href="/complex/search/">
                                Новостройки

                            </a>
                        </li>
                        <li>
                            <a href="/content/">
                                Новости

                            </a>
                        </li>
                        <li>
                            <a href="/guide/">
                                Крыша Гид

                            </a>
                        </li>
                    </ul>
                </nav>

                <div class="a-new-block">
                    <a href="/a/new?redirect=1" class="btn btn-default ">
                        Подать объявление
                    </a>
                    <div class="text-help">383 468 уже на сайте</div>
                </div>
            </div>

            <div class="category-navbar">
                <nav class="submenu submenu-one-row clearfix">
                    <ul>
                        <li class="submenu-item is-active">
                            <a href="/arenda/kvartiry/" class="link submenu-link">Квартиры</a>
                        </li>
                        <li class="submenu-item">
                            <a href="/arenda/doma/" class="link submenu-link">Дома</a>
                        </li>
                        <li class="submenu-item">
                            <a href="/arenda/komnaty/" class="link submenu-link">Комнаты</a>
                        </li>
                        <li class="submenu-item">
                            <a href="/arenda/dachi/" class="link submenu-link">Дачи</a>
                        </li>
                        <li class="submenu-item">
                            <a href="/arenda/ofisa/" class="link submenu-link">Офисы</a>
                        </li>
                        <li class="submenu-item">
                            <a href="/arenda/pomeshhenija/" class="link submenu-link">Помещения</a>
                        </li>
                        <li class="submenu-item">
                            <a href="/arenda/zdanija/" class="link submenu-link">Здания</a>
                        </li>
                        <li class="submenu-item">
                            <a href="/arenda/magazina/" class="link submenu-link">Магазины и бутики</a>
                        </li>
                        <li class="submenu-item">
                            <a href="/arenda/prombazy/" class="link submenu-link">Промбазы, склады, заводы</a>
                        </li>
                        <li class="submenu-item">
                            <a href="/arenda/prochej-nedvizhimosti/" class="link submenu-link">Прочая недвижимость</a>
                        </li>
                        <li class="submenu-item">
                            <a href="/arenda/vozmu-v-arendu/" class="link submenu-link">Возьму в аренду</a>
                        </li>
                    </ul>
                </nav>
            </div>
        </div>
    </header>
    <main class="container">
        <section class="a-search-form-container">

            <form action="/arenda/kvartiry/" method="get" class="form a-search-form form-horizontal" id="a-search-form">


                <div class="search-section section-separator-search-simple" style="">
                    <div class="section-content">


                        <div class="col-xs-4 col-sm-4 is-hidden">
                            <div class="element-group element-group-parameter-map.bounds is-horizontal element-group-x">

                                <div class="form-group">
                                    <div class="col-xs-8 col-sm-8 group-container">
                                        <div class="group-elements ">



                                            <input type="hidden" id="bounds" name="bounds" />






                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>




                        <div class="col-xs-4 col-sm-4 is-hidden">
                            <div class="element-group element-group-parameter-map.areas is-horizontal element-group-x">

                                <div class="form-group">
                                    <label class="col-xs-4 col-sm-4 control-label group-label" for="areas">
                                        Выделенные области на карте
                                    </label>
                                    <div class="col-xs-8 col-sm-8 group-container">
                                        <div class="group-elements ">



                                            <input type="hidden" id="areas" name="areas" />






                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>




                        <div class="col-xs-4 col-sm-4 simple-first-group">
                            <div
                                class="element-group element-group-parameter-live.rooms element-group-with-label is-horizontal element-group-x">

                                <div class="form-group">
                                    <label class="col-xs-4 col-sm-4 control-label group-label" for="das[live.rooms]">
                                        Квартиры
                                    </label>
                                    <div class="col-xs-8 col-sm-8 group-container">
                                        <div class="group-elements ">





                                            <div class="group-element field-container has-no-label"
                                                data-field="das[live.rooms]">








                                                <div class="element-select">


                                                    <div is-button-select='1'
                                                        class='btn-group is-button-select field-container muted-select'
                                                        data-toggle='buttons' template='button-select.twig'
                                                        additionalText='- комн.' max='1000' min='0'
                                                        id='das[live.rooms]'>
                                                        <label class="btn btn-primary btn-sm-custom das[live.rooms]-1">
                                                            <input type="checkbox" name="das[live.rooms]"
                                                                autocomplete="off" value="1"> 1
                                                        </label>
                                                        <label class="btn btn-primary btn-sm-custom das[live.rooms]-2">
                                                            <input type="checkbox" name="das[live.rooms]"
                                                                autocomplete="off" value="2"> 2
                                                        </label>
                                                        <label class="btn btn-primary btn-sm-custom das[live.rooms]-3">
                                                            <input type="checkbox" name="das[live.rooms]"
                                                                autocomplete="off" value="3"> 3
                                                        </label>
                                                        <label class="btn btn-primary btn-sm-custom das[live.rooms]-4">
                                                            <input type="checkbox" name="das[live.rooms]"
                                                                autocomplete="off" value="4"> 4
                                                        </label>
                                                        <label
                                                            class="btn btn-primary btn-sm-custom das[live.rooms]-5.100">
                                                            <input type="checkbox" name="das[live.rooms]"
                                                                autocomplete="off" value="5.100"> 5+
                                                        </label>
                                                    </div>
                                                    <span class="additional-text">- комн.</span>
                                                </div>




                                            </div>




                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>




                        <div class="col-xs-4 col-sm-4 simple-region">
                            <div class="element-group element-group-parameter-map.geo_id is-horizontal element-group-x">

                                <div class="form-group">
                                    <div class="col-xs-8 col-sm-8 group-container">
                                        <div class="group-elements ">





                                            <div class="group-element field-container has-no-label"
                                                data-field="regionAlias">









                                                <div class="element-region-dropdown dropdown"
                                                    data-url="/region/ajaxGetChildren/" data-allowed-ids="">
                                                    <a id="regionAlias-selected-value" href="#" data-toggle="dropdown"
                                                        class="dropdown-selected-text dropdown-toggle-link">
                                                        <span class="region-dropdown-label"
                                                            data-label="Регион">Астана</span>
                                                        <span class="dropdown-caret caret"></span>
                                                        <div class="triangle-with-shadow"></div>
                                                    </a>
                                                    <input type="hidden" name="regionAlias" id="regionAlias"
                                                        value="nur-sultan" class="region-value-hidden" data-id="105"
                                                        data-alias="nur-sultan">
                                                    <div class="dropdown-menu">
                                                        <a class="link region-dropdown-action region-dropdown-action-cancel"
                                                            href="#" title="Отмена">
                                                            <svg role="img" class="icon icon-svg icon-cross">
                                                                <use xlink:href="#icon-cross"></use>
                                                            </svg>
                                                        </a>
                                                        <div class="element-region-dropdown-inner"
                                                            data-url="/region/ajaxGetChildren/">
                                                            <div class="kr-autocomplete"></div>

                                                            <div class="element-region-dropdown-selects">
                                                                <div class="leveled-select is-visible">
                                                                    <select size="20" data-level="2" min='0'
                                                                        id='regionAlias' asPlaceholder=''>
                                                                        <option class="" value=""
                                                                            data-name="Весь Казахстан"
                                                                            data-label="Весь Казахстан" data-lon="0"
                                                                            data-lat="0" data-zoom="0" data-alias=""
                                                                            data-id="" data-has-complexes="0"
                                                                            data-has-children="0" data-type="">
                                                                            Весь Казахстан
                                                                        </option>
                                                                        <option class="is-big-city" value="105"
                                                                            data-name="Астана" data-label="Астана"
                                                                            data-lon="71.4314" data-lat="51.1583"
                                                                            data-zoom="11" data-alias="nur-sultan"
                                                                            data-id="105" data-has-complexes="1"
                                                                            data-has-children="1" data-type="city"
                                                                            selected>
                                                                            Астана
                                                                        </option>
                                                                        <option class="is-big-city" value="2"
                                                                            data-name="Алматы" data-label="Алматы"
                                                                            data-lon="76.9129" data-lat="43.2859"
                                                                            data-zoom="11" data-alias="almaty"
                                                                            data-id="2" data-has-complexes="1"
                                                                            data-has-children="1" data-type="city">
                                                                            Алматы
                                                                        </option>
                                                                        <option class="is-big-city" value="278"
                                                                            data-name="Шымкент" data-label="Шымкент"
                                                                            data-lon="69.6207" data-lat="42.3174"
                                                                            data-zoom="11" data-alias="shymkent"
                                                                            data-id="278" data-has-complexes="1"
                                                                            data-has-children="1" data-type="city">
                                                                            Шымкент
                                                                        </option>
                                                                        <option class="" value="3729"
                                                                            data-name="Абайская обл."
                                                                            data-label="Абайская обл." data-lon="0"
                                                                            data-lat="0" data-zoom="0"
                                                                            data-alias="abay-oblast" data-id="3729"
                                                                            data-has-complexes="1" data-has-children="1"
                                                                            data-type="region">
                                                                            Абайская обл.
                                                                        </option>
                                                                        <option class="" value="112"
                                                                            data-name="Акмолинская обл."
                                                                            data-label="Акмолинская обл."
                                                                            data-lon="70.0004" data-lat="52.1358"
                                                                            data-zoom="6"
                                                                            data-alias="akmolinskaja-oblast"
                                                                            data-id="112" data-has-complexes="1"
                                                                            data-has-children="1" data-type="region">
                                                                            Акмолинская обл.
                                                                        </option>
                                                                        <option class="" value="124"
                                                                            data-name="Актюбинская обл."
                                                                            data-label="Актюбинская обл."
                                                                            data-lon="57.2893" data-lat="49.1891"
                                                                            data-zoom="7"
                                                                            data-alias="aktjubinskaja-oblast"
                                                                            data-id="124" data-has-complexes="1"
                                                                            data-has-children="1" data-type="region">
                                                                            Актюбинская обл.
                                                                        </option>
                                                                        <option class="" value="132"
                                                                            data-name="Алматинская обл."
                                                                            data-label="Алматинская обл."
                                                                            data-lon="77.3393" data-lat="45.2151"
                                                                            data-zoom="6"
                                                                            data-alias="almatinskaja-oblast"
                                                                            data-id="132" data-has-complexes="1"
                                                                            data-has-children="1" data-type="region">
                                                                            Алматинская обл.
                                                                        </option>
                                                                        <option class="" value="213"
                                                                            data-name="Атырауская обл."
                                                                            data-label="Атырауская обл."
                                                                            data-lon="52.5799" data-lat="47.3865"
                                                                            data-zoom="7"
                                                                            data-alias="atyrauskaja-oblast"
                                                                            data-id="213" data-has-complexes="1"
                                                                            data-has-children="1" data-type="region">
                                                                            Атырауская обл.
                                                                        </option>
                                                                        <option class="" value="216"
                                                                            data-name="Восточно-Казахстанская обл."
                                                                            data-label="Восточно-Казахстанская обл."
                                                                            data-lon="81.2285" data-lat="48.8247"
                                                                            data-zoom="6"
                                                                            data-alias="vostochno-kazahstanskaja-oblast"
                                                                            data-id="216" data-has-complexes="1"
                                                                            data-has-children="1" data-type="region">
                                                                            Восточно-Казахстанская обл.
                                                                        </option>
                                                                        <option class="" value="227"
                                                                            data-name="Жамбылская обл."
                                                                            data-label="Жамбылская обл."
                                                                            data-lon="72.0988" data-lat="44.2558"
                                                                            data-zoom="6"
                                                                            data-alias="zhambylskaja-oblast"
                                                                            data-id="227" data-has-complexes="1"
                                                                            data-has-children="1" data-type="region">
                                                                            Жамбылская обл.
                                                                        </option>
                                                                        <option class="" value="3731"
                                                                            data-name="Жетысуская обл."
                                                                            data-label="Жетысуская обл." data-lon="0"
                                                                            data-lat="0" data-zoom="0"
                                                                            data-alias="jetisyskaya-oblast"
                                                                            data-id="3731" data-has-complexes="1"
                                                                            data-has-children="1" data-type="region">
                                                                            Жетысуская обл.
                                                                        </option>
                                                                        <option class="" value="232"
                                                                            data-name="Западно-Казахстанская обл."
                                                                            data-label="Западно-Казахстанская обл."
                                                                            data-lon="50.5107" data-lat="49.989"
                                                                            data-zoom="7"
                                                                            data-alias="zapadno-kazahstanskaja-oblast"
                                                                            data-id="232" data-has-complexes="1"
                                                                            data-has-children="1" data-type="region">
                                                                            Западно-Казахстанская обл.
                                                                        </option>
                                                                        <option class="" value="235"
                                                                            data-name="Карагандинская обл."
                                                                            data-label="Карагандинская обл."
                                                                            data-lon="73.7798" data-lat="49.5734"
                                                                            data-zoom="6"
                                                                            data-alias="karagandinskaja-oblast"
                                                                            data-id="235" data-has-complexes="1"
                                                                            data-has-children="1" data-type="region">
                                                                            Карагандинская обл.
                                                                        </option>
                                                                        <option class="" value="247"
                                                                            data-name="Костанайская обл."
                                                                            data-label="Костанайская обл."
                                                                            data-lon="63.9799" data-lat="51.4697"
                                                                            data-zoom="6"
                                                                            data-alias="kostanajskaja-oblast"
                                                                            data-id="247" data-has-complexes="1"
                                                                            data-has-children="1" data-type="region">
                                                                            Костанайская обл.
                                                                        </option>
                                                                        <option class="" value="253"
                                                                            data-name="Кызылординская обл."
                                                                            data-label="Кызылординская обл."
                                                                            data-lon="63.2988" data-lat="45.3425"
                                                                            data-zoom="6"
                                                                            data-alias="kyzylordinskaja-oblast"
                                                                            data-id="253" data-has-complexes="1"
                                                                            data-has-children="1" data-type="region">
                                                                            Кызылординская обл.
                                                                        </option>
                                                                        <option class="" value="257"
                                                                            data-name="Мангистауская обл."
                                                                            data-label="Мангистауская обл."
                                                                            data-lon="53.7627" data-lat="44.2648"
                                                                            data-zoom="6"
                                                                            data-alias="mangistauskaja-oblast"
                                                                            data-id="257" data-has-complexes="1"
                                                                            data-has-children="1" data-type="region">
                                                                            Мангистауская обл.
                                                                        </option>
                                                                        <option class="" value="260"
                                                                            data-name="Павлодарская обл."
                                                                            data-label="Павлодарская обл."
                                                                            data-lon="76.7461" data-lat="52.0809"
                                                                            data-zoom="6"
                                                                            data-alias="pavlodarskaja-oblast"
                                                                            data-id="260" data-has-complexes="1"
                                                                            data-has-children="1" data-type="region">
                                                                            Павлодарская обл.
                                                                        </option>
                                                                        <option class="" value="264"
                                                                            data-name="Северо-Казахстанская обл."
                                                                            data-label="Северо-Казахстанская обл."
                                                                            data-lon="68.6491" data-lat="54.4275"
                                                                            data-zoom="7"
                                                                            data-alias="severo-kazahstanskaja-oblast"
                                                                            data-id="264" data-has-complexes="1"
                                                                            data-has-children="1" data-type="region">
                                                                            Северо-Казахстанская обл.
                                                                        </option>
                                                                        <option class="" value="270"
                                                                            data-name="Туркестанская обл."
                                                                            data-label="Туркестанская обл."
                                                                            data-lon="78.4223" data-lat="44.9498"
                                                                            data-zoom="11"
                                                                            data-alias="juzhno-kazahstanskaja-oblast"
                                                                            data-id="270" data-has-complexes="1"
                                                                            data-has-children="1" data-type="region">
                                                                            Туркестанская обл.
                                                                        </option>
                                                                        <option class="" value="3727"
                                                                            data-name="Улытауская обл."
                                                                            data-label="Улытауская обл." data-lon="0"
                                                                            data-lat="0" data-zoom="0"
                                                                            data-alias="ulitayskay-oblast"
                                                                            data-id="3727" data-has-complexes="1"
                                                                            data-has-children="1" data-type="region">
                                                                            Улытауская обл.
                                                                        </option>
                                                                        <option class="" value="zn"
                                                                            data-name="Зарубежная недвижимость"
                                                                            data-label="Зарубежная недвижимость"
                                                                            data-lon="-18.71915" data-lat="37.44986"
                                                                            data-zoom="3" data-alias="zn" data-id="zn"
                                                                            data-has-complexes="1" data-has-children="1"
                                                                            data-type="">
                                                                            Зарубежная недвижимость
                                                                        </option>
                                                                    </select>

                                                                    <a class="btn btn-primary region-dropdown-action region-dropdown-action-apply"
                                                                        href="#">
                                                                        Выбрать
                                                                    </a>
                                                                </div>
                                                                <div class="leveled-select is-visible">
                                                                    <select size="20" data-level="3" min='0'
                                                                        id='regionAlias' asPlaceholder=''>
                                                                        <option class="" value="105" data-name="Астана"
                                                                            data-label="Все районы" data-lon="71.4314"
                                                                            data-lat="51.1583" data-zoom="11"
                                                                            data-alias="nur-sultan" data-id="105"
                                                                            data-has-complexes="1" data-has-children="0"
                                                                            data-type="city">
                                                                            Все районы
                                                                        </option>
                                                                        <option class="" value="106"
                                                                            data-name="Алматы р-н"
                                                                            data-label="Алматы р-н" data-lon="71.51"
                                                                            data-lat="51.1328" data-zoom="12"
                                                                            data-alias="astana-almatinskij"
                                                                            data-id="106" data-has-complexes="0"
                                                                            data-has-children="0" data-type="district">
                                                                            Алматы р-н
                                                                        </option>
                                                                        <option class="" value="291"
                                                                            data-name="Есильский р-н"
                                                                            data-label="Есильский р-н"
                                                                            data-lon="71.3665" data-lat="51.1227"
                                                                            data-zoom="12" data-alias="astana-esilskij"
                                                                            data-id="291" data-has-complexes="0"
                                                                            data-has-children="1" data-type="district">
                                                                            Есильский р-н
                                                                        </option>
                                                                        <option class="" value="2637"
                                                                            data-name="р-н Байконур"
                                                                            data-label="р-н Байконур" data-lon="71.4686"
                                                                            data-lat="51.2338" data-zoom="11"
                                                                            data-alias="r-n-bajkonur" data-id="2637"
                                                                            data-has-complexes="0" data-has-children="0"
                                                                            data-type="district">
                                                                            р-н Байконур
                                                                        </option>
                                                                        <option class="" value="107"
                                                                            data-name="Сарыарка р-н"
                                                                            data-label="Сарыарка р-н" data-lon="71.3869"
                                                                            data-lat="51.2063" data-zoom="12"
                                                                            data-alias="astana-saryarkinskij"
                                                                            data-id="107" data-has-complexes="0"
                                                                            data-has-children="0" data-type="district">
                                                                            Сарыарка р-н
                                                                        </option>
                                                                    </select>

                                                                    <a class="btn btn-primary region-dropdown-action region-dropdown-action-apply"
                                                                        href="#">
                                                                        Выбрать
                                                                    </a>
                                                                </div>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>





                                            </div>




                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>




                        <div class="col-xs-4 col-sm-4 simple-price">
                            <div
                                class="element-group element-group-price element-group-with-label is-horizontal element-group-x-x">

                                <div class="form-group">
                                    <label class="col-xs-4 col-sm-4 control-label group-label" for="">
                                        Цена
                                    </label>
                                    <div class="col-xs-8 col-sm-8 group-container">
                                        <div class="group-elements has-suffix">





                                            <div class="group-element field-container has-no-label"
                                                data-field="das[price][from]">





                                                <input type="tel" placeholder='От' suffix='-' max='150000000000' min='1'
                                                    id='das[price][from]' name='das[price][from]' value=''>




                                            </div>








                                            <div class="group-element field-container has-no-label"
                                                data-field="das[price][to]">





                                                <input type="tel" placeholder='До' max='150000000000' min='1'
                                                    id='das[price][to]' name='das[price][to]' value=''>




                                            </div>




                                            <div class="group-suffix">тг</div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>




                        <div class="col-xs-3 col-sm-3 simple-photo-wrapper-mini">
                            <div class="element-group element-group-parameter-_sys.hasphoto is-horizontal ">

                                <div class="form-group">
                                    <div class="col-xs-8 col-sm-8 group-container">
                                        <div class="group-elements ">





                                            <div class="group-element field-container has-no-label"
                                                data-field="das[_sys.hasphoto]">





                                                <div class="checkbox-custom ">
                                                    <input type="checkbox" id="das[_sys.hasphoto]-checkbox-0"
                                                        name="das[_sys.hasphoto]" value="1" />
                                                    <label for="das[_sys.hasphoto]-checkbox-0">
                                                        <svg role="img" class="icon icon-svg icon-checkbox">
                                                            <use xlink:href="#icon-checkbox"></use>
                                                        </svg>
                                                        <svg role="img" class="icon icon-svg icon-checkbox-checked">
                                                            <use xlink:href="#icon-checkbox-checked"></use>
                                                        </svg>
                                                        есть фото
                                                    </label>
                                                </div>




                                            </div>








                                            <div class="group-element field-container has-no-label"
                                                data-field="das[who]">





                                                <div class="checkbox-custom ">
                                                    <input type="checkbox" id="das[who]-checkbox-0" name="das[who]"
                                                        value="1" />
                                                    <label for="das[who]-checkbox-0">
                                                        <svg role="img" class="icon icon-svg icon-checkbox">
                                                            <use xlink:href="#icon-checkbox"></use>
                                                        </svg>
                                                        <svg role="img" class="icon icon-svg icon-checkbox-checked">
                                                            <use xlink:href="#icon-checkbox-checked"></use>
                                                        </svg>
                                                        от хозяев
                                                    </label>
                                                </div>




                                            </div>




                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>


                    </div>
                </div>

                <div class="search-section section-separator-search-middle" style="">
                    <div class="section-content">


                        <div class="col-xs-4 col-sm-4">
                            <div
                                class="element-group element-group-parameter-rent.period is-horizontal element-group-x">

                                <div class="form-group">
                                    <label class="col-xs-4 col-sm-4 control-label group-label" for="das[rent.period]">
                                        На какой срок
                                    </label>
                                    <div class="col-xs-8 col-sm-8 group-container">
                                        <div class="group-elements ">





                                            <div class="group-element field-container has-no-label"
                                                data-field="das[rent.period]">








                                                <div class="element-select">


                                                    <select name="das[rent.period]" id="das[rent.period]"
                                                        multiple='multiple' class='is-multiple muted-select' min='0'
                                                        id='das[rent.period]'>
                                                        <option value="">На любой срок</option>
                                                        <option value="4"
                                                            data-extra='{{"val_kk":"\u0441\u0430\u0493\u0430\u0442\u044b\u043d\u0430"}}'>
                                                            по часам</option>
                                                        <option value="1"
                                                            data-extra='{{"val_kk":"\u0442\u04d9\u0443\u043b\u0456\u0433\u0456\u043d\u0435"}}'>
                                                            посуточно</option>
                                                        <option value="2"
                                                            data-extra='{{"val_kk":"\u04b1\u0437\u0430\u049b \u0443\u0430\u049b\u044b\u0442\u049b\u0430"}}'>
                                                            на длительный срок</option>
                                                    </select>
                                                    <svg role="img" class="icon icon-svg icon-arrow-down">
                                                        <use xlink:href="#icon-arrow-down"></use>
                                                    </svg>
                                                </div>



                                            </div>




                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>




                        <div class="col-xs-4 col-sm-4">
                            <div
                                class="element-group element-group-floor element-group-with-label is-horizontal element-group-x-x">

                                <div class="form-group">
                                    <label class="col-xs-4 col-sm-4 control-label group-label" for="">
                                        Этаж
                                    </label>
                                    <div class="col-xs-8 col-sm-8 group-container">
                                        <div class="group-elements ">





                                            <div class="group-element field-container has-label"
                                                data-field="das[flat.floor][from]">





                                                <input type="number" id="das[flat.floor][from]"
                                                    name="das[flat.floor][from]" placeholder="От" max="500" min="0" />




                                            </div>








                                            <div class="group-element field-container has-label"
                                                data-field="das[flat.floor][to]">





                                                <input type="number" id="das[flat.floor][to]" name="das[flat.floor][to]"
                                                    placeholder="До" max="500" min="0" />




                                            </div>




                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>




                        <div class="col-xs-4 col-sm-4">
                            <div
                                class="element-group element-group-parameter-live.furniture is-horizontal element-group-x">

                                <div class="form-group">
                                    <label class="col-xs-4 col-sm-4 control-label group-label"
                                        for="das[live.furniture]">
                                        Квартира меблирована
                                    </label>
                                    <div class="col-xs-8 col-sm-8 group-container">
                                        <div class="group-elements ">





                                            <div class="group-element field-container has-label"
                                                data-field="das[live.furniture]">








                                                <div class="element-select">


                                                    <select name="das[live.furniture]" id="das[live.furniture]"
                                                        multiple='multiple' class='is-multiple muted-select' min='0'
                                                        id='das[live.furniture]'>
                                                        <option value="">Не важно</option>
                                                        <option value="1"
                                                            data-extra='{{"val_kk":"\u0442\u043e\u043b\u044b\u049b"}}'>
                                                            полностью</option>
                                                        <option value="2"
                                                            data-extra='{{"val_kk":"\u0456\u0448\u0456\u043d\u0430\u0440\u0430"}}'>
                                                            частично</option>
                                                        <option value="3" data-extra='{{"val_kk":"\u0431\u043e\u0441"}}'>
                                                            без мебели</option>
                                                    </select>
                                                    <svg role="img" class="icon icon-svg icon-arrow-down">
                                                        <use xlink:href="#icon-arrow-down"></use>
                                                    </svg>
                                                </div>



                                            </div>




                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>




                        <div class="col-xs-4 col-sm-4">
                            <div
                                class="element-group element-group-parameter-flat.building is-horizontal element-group-x">

                                <div class="form-group">
                                    <label class="col-xs-4 col-sm-4 control-label group-label" for="das[flat.building]">
                                        Тип дома
                                    </label>
                                    <div class="col-xs-8 col-sm-8 group-container">
                                        <div class="group-elements ">





                                            <div class="group-element field-container has-label"
                                                data-field="das[flat.building]">








                                                <div class="element-select">


                                                    <select name="das[flat.building]" id="das[flat.building]"
                                                        multiple='multiple' class='is-multiple muted-select' min='0'
                                                        id='das[flat.building]'>
                                                        <option value="">Не важно</option>
                                                        <option value="1"
                                                            data-extra='{{"val_kk":"\u043a\u0456\u0440\u043f\u0456\u0448"}}'>
                                                            кирпичный</option>
                                                        <option value="2"
                                                            data-extra='{{"val_kk":"\u043f\u0430\u043d\u0435\u043b\u044c\u0434\u0456\u043a"}}'>
                                                            панельный</option>
                                                        <option value="3"
                                                            data-extra='{{"val_kk":"\u043c\u043e\u043d\u043e\u043b\u0438\u0442\u0442\u0456"}}'>
                                                            монолитный</option>
                                                        <option value="0"
                                                            data-extra='{{"val_kk":"\u0431\u0430\u0441\u049b\u0430"}}'>
                                                            иное</option>
                                                    </select>
                                                    <svg role="img" class="icon icon-svg icon-arrow-down">
                                                        <use xlink:href="#icon-arrow-down"></use>
                                                    </svg>
                                                </div>



                                            </div>




                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>




                        <div class="col-xs-4 col-sm-4 has-change-wrapper-large">
                            <div
                                class="element-group element-group-parameter-floor_not_last is-horizontal element-group-x">

                                <div class="form-group">
                                    <div class="col-xs-8 col-sm-8 group-container">
                                        <div class="group-elements ">





                                            <div class="group-element field-container has-no-label"
                                                data-field="das[floor_not_last]">





                                                <div class="checkbox-custom ">
                                                    <input type="checkbox" id="das[floor_not_last]-checkbox-0"
                                                        name="das[floor_not_last]" value="1" />
                                                    <label for="das[floor_not_last]-checkbox-0">
                                                        <svg role="img" class="icon icon-svg icon-checkbox">
                                                            <use xlink:href="#icon-checkbox"></use>
                                                        </svg>
                                                        <svg role="img" class="icon icon-svg icon-checkbox-checked">
                                                            <use xlink:href="#icon-checkbox-checked"></use>
                                                        </svg>
                                                        Не последний этаж
                                                    </label>
                                                </div>




                                            </div>




                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>




                        <div class="col-xs-4 col-sm-4">
                            <div class="element-group element-group-parameter-inet.type is-horizontal element-group-x">

                                <div class="form-group">
                                    <label class="col-xs-4 col-sm-4 control-label group-label" for="das[inet.type]">
                                        Интернет
                                    </label>
                                    <div class="col-xs-8 col-sm-8 group-container">
                                        <div class="group-elements ">





                                            <div class="group-element field-container has-label"
                                                data-field="das[inet.type]">








                                                <div class="element-select">


                                                    <select name="das[inet.type]" id="das[inet.type]"
                                                        multiple='multiple' class='is-multiple muted-select' min='0'
                                                        id='das[inet.type]'>
                                                        <option value="">Не важно</option>
                                                        <option value="1" data-extra='{{"val_kk":"ADSL"}}'>ADSL</option>
                                                        <option value="2"
                                                            data-extra='{{"val_kk":"TV \u043a\u0430\u0431\u0435\u043b\u0456 \u0430\u0440\u049b\u044b\u043b\u044b"}}'>
                                                            через TV кабель</option>
                                                        <option value="3"
                                                            data-extra='{{"val_kk":"\u0441\u044b\u043c\u0434\u044b"}}'>
                                                            проводной</option>
                                                        <option value="4"
                                                            data-extra='{{"val_kk":"\u043e\u043f\u0442\u0438\u043a\u0430"}}'>
                                                            оптика</option>
                                                    </select>
                                                    <svg role="img" class="icon icon-svg icon-arrow-down">
                                                        <use xlink:href="#icon-arrow-down"></use>
                                                    </svg>
                                                </div>



                                            </div>




                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>




                        <div class="col-xs-4 col-sm-4">
                            <div
                                class="element-group element-group-parameter-house.complex_name is-horizontal element-group-x">

                                <div class="form-group">
                                    <label class="col-xs-4 col-sm-4 control-label group-label" for="das[map.complex]">
                                        Жилой комплекс
                                    </label>
                                    <div class="col-xs-8 col-sm-8 group-container">
                                        <div class="group-elements ">





                                            <div class="map-complex-container group-element field-container has-label"
                                                data-field="das[map.complex]">





                                                <div class="selectbox element-selectbox" data-for="das[map.complex]">
                                                    <div class="selectbox-select">
                                                        <input type="hidden" class=" selected-value-holder"
                                                            name="das[map.complex]" id="das[map.complex]" value="">
                                                        <div class="text"></div>
                                                        <svg role="img" class="icon icon-svg icon-arrow-down">
                                                            <use xlink:href="#icon-arrow-down"></use>
                                                        </svg>
                                                    </div>
                                                    <ul class="selectbox-options">
                                                        <li class="system search">
                                                            <input type="text" autocomplete="off"
                                                                placeholder="Поиск…" />
                                                            <div class="not-found">Совпадений не найдено</div>
                                                        </li>
                                                    </ul>
                                                </div>




                                            </div>




                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>




                        <div class="col-xs-4 col-sm-4 has-change-wrapper-large">
                            <div
                                class="element-group element-group-parameter-floor_not_first is-horizontal element-group-x">

                                <div class="form-group">
                                    <div class="col-xs-8 col-sm-8 group-container">
                                        <div class="group-elements ">





                                            <div class="group-element field-container has-no-label"
                                                data-field="das[floor_not_first]">





                                                <div class="checkbox-custom ">
                                                    <input type="checkbox" id="das[floor_not_first]-checkbox-0"
                                                        name="das[floor_not_first]" value="1" />
                                                    <label for="das[floor_not_first]-checkbox-0">
                                                        <svg role="img" class="icon icon-svg icon-checkbox">
                                                            <use xlink:href="#icon-checkbox"></use>
                                                        </svg>
                                                        <svg role="img" class="icon icon-svg icon-checkbox-checked">
                                                            <use xlink:href="#icon-checkbox-checked"></use>
                                                        </svg>
                                                        Не первый этаж
                                                    </label>
                                                </div>




                                            </div>




                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>




                        <div class="col-xs-4 col-sm-4">
                            <div
                                class="element-group element-group-parameter-flat.toilet is-horizontal element-group-separator">

                                <div class="form-group">
                                    <label class="col-xs-4 col-sm-4 control-label group-label" for="das[flat.toilet]">
                                        Санузел
                                    </label>
                                    <div class="col-xs-8 col-sm-8 group-container">
                                        <div class="group-elements ">





                                            <div class="group-element field-container has-label"
                                                data-field="das[flat.toilet]">








                                                <div class="element-select">


                                                    <select name="das[flat.toilet]" id="das[flat.toilet]"
                                                        multiple='multiple' class='is-multiple muted-select' min='0'
                                                        id='das[flat.toilet]'>
                                                        <option value="">Не важно</option>
                                                        <option value="1"
                                                            data-extra='{{"val_kk":"\u0431\u04e9\u043b\u0435\u043a"}}'>
                                                            раздельный</option>
                                                        <option value="2"
                                                            data-extra='{{"val_kk":"\u0431\u0456\u0440\u0456\u043a\u0442\u0456\u0440\u0456\u043b\u0433\u0435\u043d"}}'>
                                                            совмещенный</option>
                                                        <option value="3"
                                                            data-extra='{{"val_kk":"2 \u0441\/\u0442 \u0436\u04d9\u043d\u0435 \u043e\u0434\u0430\u043d \u043a\u04e9\u043f"}}'>
                                                            2 с/у и более</option>
                                                        <option value="4" data-extra='{{"val_kk":"\u0436\u043e\u049b"}}'>
                                                            нет</option>
                                                    </select>
                                                    <svg role="img" class="icon icon-svg icon-arrow-down">
                                                        <use xlink:href="#icon-arrow-down"></use>
                                                    </svg>
                                                </div>



                                            </div>




                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>




                        <div class="col-xs-4 col-sm-4">
                            <div
                                class="element-group element-group-live-square-total element-group-with-label is-horizontal element-group-x-x">

                                <div class="form-group">
                                    <label class="col-xs-4 col-sm-4 control-label group-label" for="">
                                        Общая площадь
                                    </label>
                                    <div class="col-xs-8 col-sm-8 group-container">
                                        <div class="group-elements has-suffix">





                                            <div class="group-element field-container has-label"
                                                data-field="das[live.square][from]">





                                                <input type="number" id="das[live.square][from]"
                                                    name="das[live.square][from]" placeholder="От" max="100000"
                                                    min="1" />




                                            </div>








                                            <div class="group-element field-container has-label"
                                                data-field="das[live.square][to]">





                                                <input type="number" id="das[live.square][to]"
                                                    name="das[live.square][to]" placeholder="До" max="100000" min="1" />




                                            </div>




                                            <div class="group-suffix">м²</div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>




                        <div class="col-xs-4 col-sm-4">
                            <div
                                class="element-group element-group-parameter-flat.renovation is-horizontal element-group-x">

                                <div class="form-group">
                                    <label class="col-xs-4 col-sm-4 control-label group-label"
                                        for="das[flat.renovation]">
                                        Состояние
                                    </label>
                                    <div class="col-xs-8 col-sm-8 group-container">
                                        <div class="group-elements ">





                                            <div class="group-element field-container has-label"
                                                data-field="das[flat.renovation]">








                                                <div class="element-select">


                                                    <select name="das[flat.renovation]" id="das[flat.renovation]"
                                                        multiple='multiple' class='is-multiple muted-select' min='0'
                                                        id='das[flat.renovation]'>
                                                        <option value="">Не важно</option>
                                                        <option value="1"
                                                            data-extra='{{"val_kk":"\u0436\u0430\u049b\u0441\u044b"}}'>
                                                            хорошее</option>
                                                        <option value="2"
                                                            data-extra='{{"val_kk":"\u043e\u0440\u0442\u0430\u0448\u0430"}}'>
                                                            среднее</option>
                                                        <option value="4"
                                                            data-extra='{{"val_kk":"\u0436\u04e9\u043d\u0434\u0435\u0443 \u0436\u04af\u0440\u0433\u0456\u0437\u0443 \u049b\u0430\u0436\u0435\u0442"}}'>
                                                            требует ремонта</option>
                                                        <option value="5"
                                                            data-extra='{{"val_kk":"\u0435\u0440\u043a\u0456\u043d \u0436\u043e\u0441\u043f\u0430\u0440\u043b\u0430\u043d\u0493\u0430\u043d"}}'>
                                                            свободная планировка</option>
                                                        <option value="6"
                                                            data-extra='{{"val_kk":"\u0431\u0430\u0441\u0442\u0430\u043f\u049b\u044b \u04d9\u0440\u043b\u0435\u043d\u0433\u0435\u043d"}}'>
                                                            черновая отделка</option>
                                                    </select>
                                                    <svg role="img" class="icon icon-svg icon-arrow-down">
                                                        <use xlink:href="#icon-arrow-down"></use>
                                                    </svg>
                                                </div>



                                            </div>




                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>


                    </div>
                </div>

                <div class="search-section section-separator-search-advanced" style="display:none;">
                    <div class="section-content">


                        <div class="col-xs-4 col-sm-4">
                            <div
                                class="element-group element-group-square-living element-group-with-label is-horizontal element-group-x-x">

                                <div class="form-group">
                                    <label class="col-xs-4 col-sm-4 control-label group-label" for="">
                                        Жилая площадь
                                    </label>
                                    <div class="col-xs-8 col-sm-8 group-container">
                                        <div class="group-elements has-suffix">





                                            <div class="group-element field-container has-label"
                                                data-field="das[live.square_l][from]">





                                                <input type="number" id="das[live.square_l][from]"
                                                    name="das[live.square_l][from]" placeholder="От" max="100000"
                                                    min="0" />




                                            </div>








                                            <div class="group-element field-container has-label"
                                                data-field="das[live.square_l][to]">





                                                <input type="number" id="das[live.square_l][to]"
                                                    name="das[live.square_l][to]" placeholder="До" max="100000"
                                                    min="0" />




                                            </div>




                                            <div class="group-suffix">м²</div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>




                        <div class="col-xs-4 col-sm-4 big-label">
                            <div
                                class="element-group element-group-parameter-flat.priv_dorm is-horizontal element-group-x">

                                <div class="form-group">
                                    <label class="col-xs-4 col-sm-4 control-label group-label"
                                        for="das[flat.priv_dorm]">
                                        Бывшее общежитие
                                    </label>
                                    <div class="col-xs-8 col-sm-8 group-container">
                                        <div class="group-elements ">





                                            <div class="radio-layout-x-x-x group-element field-container has-no-label"
                                                data-field="das[flat.priv_dorm]">








                                                <div class="element-select">


                                                    <select name="das[flat.priv_dorm]" id="das[flat.priv_dorm]" min='0'
                                                        id='das[flat.priv_dorm]' class='form-control muted-select'>
                                                        <option value="">Не важно</option>
                                                        <option value="1" data-extra='{{"val_kk":"\u0438\u04d9"}}'>да
                                                        </option>
                                                        <option value="2" data-extra='{{"val_kk":"\u0436\u043e\u049b"}}'>
                                                            нет</option>
                                                    </select>
                                                    <svg role="img" class="icon icon-svg icon-arrow-down">
                                                        <use xlink:href="#icon-arrow-down"></use>
                                                    </svg>
                                                </div>



                                            </div>




                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>




                        <div class="col-xs-8 col-sm-8">
                            <div
                                class="element-group element-group-square-kitchen element-group-with-label is-horizontal element-group-separator element-group-x-x">

                                <div class="form-group">
                                    <label class="col-xs-4 col-sm-4 control-label group-label" for="">
                                        Площадь кухни
                                    </label>
                                    <div class="col-xs-8 col-sm-8 group-container">
                                        <div class="group-elements has-suffix">





                                            <div class="group-element field-container has-label"
                                                data-field="das[live.square_k][from]">





                                                <input type="number" id="das[live.square_k][from]"
                                                    name="das[live.square_k][from]" placeholder="От" max="1000"
                                                    min="0" />




                                            </div>








                                            <div class="group-element field-container has-label"
                                                data-field="das[live.square_k][to]">





                                                <input type="number" id="das[live.square_k][to]"
                                                    name="das[live.square_k][to]" placeholder="До" max="1000" min="0" />




                                            </div>




                                            <div class="group-suffix">м²</div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>




                        <div class="col-xs-8 col-sm-8">
                            <div
                                class="element-group element-group-parameter-text element-group-with-label is-horizontal search-text">

                                <div class="form-group">
                                    <label class="col-xs-4 col-sm-4 control-label group-label" for="_txt_">
                                        Поиск по тексту
                                    </label>
                                    <div class="col-xs-8 col-sm-8 group-container">
                                        <div class="group-elements ">





                                            <div class="group-element field-container has-label" data-field="_txt_">





                                                <input type="text" id="_txt_" name="_txt_" />




                                            </div>




                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>


                    </div>
                </div>

                <input type="hidden" name="zoom" value="" />
                <input type="hidden" name="lat" value="" />
                <input type="hidden" name="lon" value="" />
                <input type="hidden" name="sort_by" value="" />

                <div class="submit-wrapper">
                    <div class="row">
                        <div class="col-xs-3 col-sm-4 search-form-bottom-left">
                            <a href="#" class="search-extra-settings">
                                <i class="fi-settings"></i>
                                <span class="on">Ещё настройки</span>
                                <span class="off">Скрыть настройки</span>
                            </a>
                            <a href="#" class="form-reset no-link-border">
                                <i class="fi-close-big"></i>
                                <span class="link">
                                    Очистить всё
                                </span>
                            </a>
                        </div>
                        <div class="col-xs-5 col-sm-4 search-form-bottom-middle">
                            <div class="btn-submit-wrapper">
                                <button type="submit" class="btn-submit search-btn-main">
                                    Показать результаты
                                    <span class="gray nb-total"></span>
                                </button>
                            </div>
                        </div>
                        <div class="col-xs-3 col-sm-4 search-form-bottom-right">
                            <div class="search-view-toggle-container">
                                <a class="search-btn-main link-show-as-list is-active"
                                    href="/arenda/kvartiry/nur-sultan/?das[_sys.hasphoto]=1&das[price][to]=10000&das[rent.period]=1">
                                    <svg role="img" class="icon icon-svg icon-list-simple">
                                        <use xlink:href="#icon-list-simple"></use>
                                    </svg>
                                    Списком
                                </a>
                                <a class="search-btn-main link-show-on-map"
                                    href="/map/arenda/kvartiry/nur-sultan/?das[_sys.hasphoto]=1&das[price][to]=10000&das[rent.period]=1">
                                    <svg role="img" class="icon icon-svg icon-map-geolocation">
                                        <use xlink:href="#icon-map-geolocation"></use>
                                    </svg>
                                    На карте
                                </a>
                            </div>
                        </div>
                    </div>
                </div>
            </form>

            <div class="tooltip-overlay">
                <div class="tooltip-overlay__img"><svg role="img" class="icon icon-svg icon-vector-stroke">
                        <use xlink:href="#icon-vector-stroke"></use>
                    </svg></div>
                <div class="tooltip-overlay__title-block">
                    <div class="tooltip-overlay__title">
                        Первичное жильё
                    </div>
                    <div class="tooltip-overlay__description">
                        Ищите проверенные объявления от застройщиков.
                    </div>
                </div>
            </div>
        </section>

        <section itemscope itemtype="https://schema.org/BreadcrumbList" class="breadcrumbs breadcrumbs-top ">
            <div itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
                <a itemscope itemtype="https://schema.org/WebPage" itemprop="item" itemid="/" href="/"><span
                        itemprop="name">Крыша</span></a>
                <meta itemprop="position" content="1">
            </div>
            /
            <div itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
                <a itemscope itemtype="https://schema.org/WebPage" itemprop="item" itemid="/arenda/kvartiry/"
                    href="/arenda/kvartiry/"><span itemprop="name">Аренда квартир</span></a>
                <meta itemprop="position" content="2">
            </div>
        </section>


        <section class="a-search-container main-cols-container">
            <div class="main-col">
                <div class="search-top-min-h">
                    <div class="common-b 10 ddl_campaign" id="10" data-campaign-id="10">
                        <div id='div-gpt-ad-1536300331333-0'>
                            <script type="text/javascript">
                                googletag.cmd.push(function () {{

                                    googletag.display('div-gpt-ad-1536300331333-0');
                                }});
                            </script>
                        </div>
                        <div id='ya-10'></div>
                    </div>
                </div>


                <div class="page-title">
                    <h1> Аренда квартиры посуточно в вашем городе</h1>
                </div>
                <div class="a-search-subtitle search-results-nb">

                    Найдено <span>1 497</span> объявлений


                </div>

                <div class="a-search-options-container clearfix has-sort-filter">
                    <div class="a-search-options">
                        <div class="sort-filter">
                            <span class="sort-option-label">Сначала:</span>
                            <div class="sort-option-selector is-active search-tab-active" data-value="add_date-desc">
                                <a href="#"
                                    data-href="/arenda/kvartiry/nur-sultan/?das[_sys.hasphoto]=1&amp;das[price][to]=10000&amp;das[rent.period]=1"
                                    class="link se-link sort-option-link">новые объявления</a>
                            </div>
                            <div class="sort-option-selector" data-value="price-asc">
                                <a href="#"
                                    data-href="/arenda/kvartiry/nur-sultan/?das[_sys.hasphoto]=1&amp;das[price][to]=10000&amp;das[rent.period]=1&amp;sort_by=price-asc"
                                    class="link se-link sort-option-link">дешевые</a>
                            </div>
                            <div class="sort-option-selector" data-value="price-desc">
                                <a href="#"
                                    data-href="/arenda/kvartiry/nur-sultan/?das[_sys.hasphoto]=1&amp;das[price][to]=10000&amp;das[rent.period]=1&amp;sort_by=price-desc"
                                    class="link se-link sort-option-link">дорогие</a>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="a-add-to-category">
                    <svg role="img" class="icon icon-svg icon-add-a">
                        <use xlink:href="#icon-add-a"></use>
                    </svg>
                    <a href="/a/new/?cat=rent.flat&redirect=1" class="link">Подать объявление</a><br><span>в этот
                        раздел</span>
                </div>
                <section class="a-list a-search-list a-list-with-favs">
                    {FLAT_LIST}
                </section>
                <div class="new-b-place">
                    <script type="application/javascript">
        < !--
        if (top.location.hostname != self.location.hostname) {{
                            self.location = 'http://' + top.location.hostname + self.location.pathname + self.location.search;
                        }}
        //-->
                    </script>
                    <script type="text/javascript" charset="utf-8">
                        (function (G, o, O, g, L, e) {{
                            G[g] = G[g] || function () {{
                                (G[g]['q'] = G[g]['q'] || []).push(
                                    arguments)
                            }}, G[g]['t'] = 1 * new Date; L = o.createElement(O), e = o.getElementsByTagName(
                                O)[0]; L.async = 1; L.src = '//www.google.com/adsense/search/async-ads.js';
                            e.parentNode.insertBefore(L, e)
                        }})(window, document, 'script', '_googCsa');
                    </script>

                    <div id="zh-container"></div>

                    <script type="text/javascript" charset="utf-8">
                        var pageOptions = {{
                            'pubId': 'pub-5830422643177092',
                            'query': 'Аренда квартиры посуточно в вашем городе',
                            'hl': 'ru',
                            'linkTarget': '_blank',
                            'channel': '8541758322',
                            'adPage': 1
                        }};

                        var adblock1 = {{
                            'container': 'zh-container',
                            'fontFamily': 'Open Sans',
                            'fontSizeTitle': 15,
                            'fontSizeDescription': 12,
                            'fontSizeDomainLink': 12,
                            'colorTitleLink': '#0066CC',
                            'colorText': '#333333',
                            'noTitleUnderline': false,
                            'detailedAttribution': false,
                            'siteLinks': false
                        }};

                        _googCsa('ads', pageOptions, adblock1);

                    </script>
                </div>
                <nav class="paginator">

                    <a class="paginator__btn paginator__btn--active"
                        href="/arenda/kvartiry/nur-sultan/?das[_sys.hasphoto]=1&amp;das[price][to]=10000&amp;das[rent.period]=1"
                        data-page="1">
                        1
                    </a>
                    <a class="paginator__btn "
                        href="/arenda/kvartiry/nur-sultan/?das[_sys.hasphoto]=1&amp;das[price][to]=10000&amp;das[rent.period]=1&amp;page=2"
                        data-page="2">
                        2
                    </a>
                    <a class="paginator__btn "
                        href="/arenda/kvartiry/nur-sultan/?das[_sys.hasphoto]=1&amp;das[price][to]=10000&amp;das[rent.period]=1&amp;page=3"
                        data-page="3">
                        3
                    </a>
                    <a class="paginator__btn "
                        href="/arenda/kvartiry/nur-sultan/?das[_sys.hasphoto]=1&amp;das[price][to]=10000&amp;das[rent.period]=1&amp;page=4"
                        data-page="4">
                        4
                    </a>
                    <a class="paginator__btn "
                        href="/arenda/kvartiry/nur-sultan/?das[_sys.hasphoto]=1&amp;das[price][to]=10000&amp;das[rent.period]=1&amp;page=5"
                        data-page="5">
                        5
                    </a>
                    <a class="paginator__btn "
                        href="/arenda/kvartiry/nur-sultan/?das[_sys.hasphoto]=1&amp;das[price][to]=10000&amp;das[rent.period]=1&amp;page=6"
                        data-page="6">
                        6
                    </a>
                    <a class="paginator__btn "
                        href="/arenda/kvartiry/nur-sultan/?das[_sys.hasphoto]=1&amp;das[price][to]=10000&amp;das[rent.period]=1&amp;page=7"
                        data-page="7">
                        7
                    </a>
                    <a class="paginator__btn "
                        href="/arenda/kvartiry/nur-sultan/?das[_sys.hasphoto]=1&amp;das[price][to]=10000&amp;das[rent.period]=1&amp;page=8"
                        data-page="8">
                        8
                    </a>
                    <span class="paginator__btn">...</span>
                    <a class="paginator__btn "
                        href="/arenda/kvartiry/nur-sultan/?das[_sys.hasphoto]=1&amp;das[price][to]=10000&amp;das[rent.period]=1&amp;page=75"
                        data-page="75">
                        75
                    </a>

                    <a class="paginator__btn paginator__btn--next"
                        href="/arenda/kvartiry/nur-sultan/?das[_sys.hasphoto]=1&amp;das[price][to]=10000&amp;das[rent.period]=1&amp;page=2"
                        data-page="2">
                        <div class="paginator__btn-text">Дальше</div>

                        <span class="fi-arrow-small-right"></span>
                    </a>
                </nav>

                <div class="common-b 13 ddl_campaign" id="13" data-campaign-id="13">
                    <div id='div-gpt-ad-1536300838629-0'>
                        <script type="text/javascript">
                            googletag.cmd.push(function () {{

                                googletag.display('div-gpt-ad-1536300838629-0');
                            }});
                        </script>
                    </div>
                    <div id='ya-13'></div>
                </div>
                <section itemscope itemtype="https://schema.org/BreadcrumbList" class="breadcrumbs breadcrumbs-bottom ">
                    <div itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
                        <a itemscope itemtype="https://schema.org/WebPage" itemprop="item" itemid="/" href="/"><span
                                itemprop="name">Недвижимость в Казахстане</span></a>
                        <meta itemprop="position" content="1">
                    </div>
                    /
                    <div itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
                        <a itemscope itemtype="https://schema.org/WebPage" itemprop="item" itemid="/arenda/"
                            href="/arenda/"><span itemprop="name">Аренда недвижимости</span></a>
                        <meta itemprop="position" content="2">
                    </div>
                    /
                    <div itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
                        <a itemscope itemtype="https://schema.org/WebPage" itemprop="item" itemid="/catalog/nur-sultan/"
                            href="/catalog/nur-sultan/"><span itemprop="name">Недвижимость в Астане</span></a>
                        <meta itemprop="position" content="3">
                    </div>
                    /
                    <div itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
                        <a itemscope itemtype="https://schema.org/WebPage" itemprop="item" itemid="/arenda/kvartiry/"
                            href="/arenda/kvartiry/"><span itemprop="name">Объявления аренды квартир</span></a>
                        <meta itemprop="position" content="4">
                    </div>
                    /
                    <div itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
                        <a itemscope itemtype="https://schema.org/WebPage" itemprop="item"
                            itemid="/arenda/kvartiry/nur-sultan/?das[rent.period]=1"
                            href="/arenda/kvartiry/nur-sultan/?das[rent.period]=1"><span
                                itemprop="name">Посуточно</span></a>
                        <meta itemprop="position" content="5">
                    </div>
                </section>

            </div>

            <aside class="right-col">
                <div class="common-b krisha_icon_search_1 ddl_campaign" id="krisha_icon_search_1"
                    data-campaign-id="krisha_icon_search_1">
                    <div id='div-gpt-ad-1498821549802-0'>
                        <script type="text/javascript">
                            googletag.cmd.push(function () {{

                                googletag.display('div-gpt-ad-1498821549802-0');
                            }});
                        </script>
                    </div>
                    <div id='ya-krisha_icon_search_1'></div>
                </div>
                <div class="common-b krisha_icon_search_2 ddl_campaign" id="krisha_icon_search_2"
                    data-campaign-id="krisha_icon_search_2">
                    <div id='div-gpt-ad-1498476236129-0'>
                        <script type="text/javascript">
                            googletag.cmd.push(function () {{

                                googletag.display('div-gpt-ad-1498476236129-0');
                            }});
                        </script>
                    </div>
                    <div id='ya-krisha_icon_search_2'></div>
                </div>
                <div class="common-b krisha_icon_search_3 ddl_campaign" id="krisha_icon_search_3"
                    data-campaign-id="krisha_icon_search_3">
                    <div id='div-gpt-ad-1498476581453-0'>
                        <script type="text/javascript">
                            googletag.cmd.push(function () {{

                                googletag.display('div-gpt-ad-1498476581453-0');
                            }});
                        </script>
                    </div>
                    <div id='ya-krisha_icon_search_3'></div>
                </div>
                <div class="common-b krisha_icon_search_4 ddl_campaign" id="krisha_icon_search_4"
                    data-campaign-id="krisha_icon_search_4">
                    <div id='div-gpt-ad-1498476634002-0'>
                        <script type="text/javascript">
                            googletag.cmd.push(function () {{

                                googletag.display('div-gpt-ad-1498476634002-0');
                            }});
                        </script>
                    </div>
                    <div id='ya-krisha_icon_search_4'></div>
                </div>
                <div class="common-b krisha_icon_search_5 ddl_campaign" id="krisha_icon_search_5"
                    data-campaign-id="krisha_icon_search_5">
                    <div id='div-gpt-ad-1498540120368-0'>
                        <script type="text/javascript">
                            googletag.cmd.push(function () {{

                                googletag.display('div-gpt-ad-1498540120368-0');
                            }});
                        </script>
                    </div>
                    <div id='ya-krisha_icon_search_5'></div>
                </div>
                <div class="common-b krisha_icon_search_6 ddl_campaign" id="krisha_icon_search_6"
                    data-campaign-id="krisha_icon_search_6">
                    <div id='div-gpt-ad-1498540148673-0'>
                        <script type="text/javascript">
                            googletag.cmd.push(function () {{

                                googletag.display('div-gpt-ad-1498540148673-0');
                            }});
                        </script>
                    </div>
                    <div id='ya-krisha_icon_search_6'></div>
                </div>
                <div class="common-b krisha_icon_search_7 ddl_campaign" id="krisha_icon_search_7"
                    data-campaign-id="krisha_icon_search_7">
                    <div id='div-gpt-ad-1498540179932-0'>
                        <script type="text/javascript">
                            googletag.cmd.push(function () {{

                                googletag.display('div-gpt-ad-1498540179932-0');
                            }});
                        </script>
                    </div>
                    <div id='ya-krisha_icon_search_7'></div>
                </div>
                <div class="common-b krisha_icon_search_8 ddl_campaign" id="krisha_icon_search_8"
                    data-campaign-id="krisha_icon_search_8">
                    <div id='div-gpt-ad-1498540200272-0'>
                        <script type="text/javascript">
                            googletag.cmd.push(function () {{

                                googletag.display('div-gpt-ad-1498540200272-0');
                            }});
                        </script>
                    </div>
                    <div id='ya-krisha_icon_search_8'></div>
                </div>
                <div class="board">
                    <div class="common-b 11 ddl_campaign" id="11" data-campaign-id="11">
                        <div id='div-gpt-ad-1536300503358-0'>
                            <script type="text/javascript">
                                googletag.cmd.push(function () {{

                                    googletag.display('div-gpt-ad-1536300503358-0');
                                }});
                            </script>
                        </div>
                        <div id='ya-11'></div>
                    </div>
                </div>


                <div class="hot-aside-title">Горячие предложения в Астане</div>
                <div class="hot-a-wrap" title="В горячих с 18:35:10">
                    <div class="hot-a-photo">
                        <a href="/a/show/679129323" class="tm-click-sidebar-hot-adv">


                            <picture class=" is-moderated has-photo" title="" data-photo-id="1" data-name="1"
                                data-full-src="https://photos-kr.kcdn.kz/webp/cb/cb64d4f6-64ee-4d29-a0a0-8ca16e6c17cc/1-full.jpg">

                                <source
                                    srcset="https://photos-kr.kcdn.kz/webp/cb/cb64d4f6-64ee-4d29-a0a0-8ca16e6c17cc/1-60x45.webp 1x, https://photos-kr.kcdn.kz/webp/cb/cb64d4f6-64ee-4d29-a0a0-8ca16e6c17cc/1-120x90.webp 1.5x, https://photos-kr.kcdn.kz/webp/cb/cb64d4f6-64ee-4d29-a0a0-8ca16e6c17cc/1-120x90.webp 2x"
                                    type="image/webp">
                                <source
                                    srcset="https://photos-kr.kcdn.kz/webp/cb/cb64d4f6-64ee-4d29-a0a0-8ca16e6c17cc/1-60x45.jpg 1x, https://photos-kr.kcdn.kz/webp/cb/cb64d4f6-64ee-4d29-a0a0-8ca16e6c17cc/1-120x90.jpg 1.5x, https://photos-kr.kcdn.kz/webp/cb/cb64d4f6-64ee-4d29-a0a0-8ca16e6c17cc/1-120x90.jpg 2x"
                                    type="image/jpeg">

                                <img alt="3-комнатная квартира, 120 м², 6/11 этаж на длительный срок, Есенберлина 7/1 — Біржан Сал- Есенберлина за 400 000 〒 в Астане, Сарыарка р-н"
                                    title="Аренда квартир в Астане: 3-комнатная квартира, 120 м², 6/11 этаж на длительный срок, Есенберлина 7/1 — Біржан Сал- Есенберлина за 400 000 〒"
                                    src="https://photos-kr.kcdn.kz/webp/cb/cb64d4f6-64ee-4d29-a0a0-8ca16e6c17cc/1-60x45.jpg"
                                    srcset="https://photos-kr.kcdn.kz/webp/cb/cb64d4f6-64ee-4d29-a0a0-8ca16e6c17cc/1-60x45.jpg 1x, https://photos-kr.kcdn.kz/webp/cb/cb64d4f6-64ee-4d29-a0a0-8ca16e6c17cc/1-120x90.jpg 1.5x, https://photos-kr.kcdn.kz/webp/cb/cb64d4f6-64ee-4d29-a0a0-8ca16e6c17cc/1-120x90.jpg 2x"
                                    loading="lazy" />
                            </picture>
                        </a>
                    </div>
                    <div class="hot-a-info">
                        <a href="/a/show/679129323" class="tm-click-sidebar-hot-adv">
                            3-комнатная квартира, 120 м², 6/11 этаж на длительный срок
                        </a>
                        &nbsp;<b>за</b>
                        <br>
                        <b class="price">400&nbsp;000&nbsp;<span class="currency-sign offer__currency">〒</span></b>
                        <div>Есенберлина-Біржан Сал- Есенберлина</div>
                    </div>
                </div>

                <div class="hot-a-wrap" title="В горячих с 18:30:14">
                    <div class="hot-a-photo">
                        <a href="/a/show/678673735" class="tm-click-sidebar-hot-adv">


                            <picture class=" is-moderated has-photo" title="" data-photo-id="1" data-name="1"
                                data-full-src="https://photos-kr.kcdn.kz/webp/e9/e9b606b0-4e09-4008-b40e-6d565b0e829d/1-full.jpg">

                                <source
                                    srcset="https://photos-kr.kcdn.kz/webp/e9/e9b606b0-4e09-4008-b40e-6d565b0e829d/1-60x45.webp 1x, https://photos-kr.kcdn.kz/webp/e9/e9b606b0-4e09-4008-b40e-6d565b0e829d/1-120x90.webp 1.5x, https://photos-kr.kcdn.kz/webp/e9/e9b606b0-4e09-4008-b40e-6d565b0e829d/1-120x90.webp 2x"
                                    type="image/webp">
                                <source
                                    srcset="https://photos-kr.kcdn.kz/webp/e9/e9b606b0-4e09-4008-b40e-6d565b0e829d/1-60x45.jpg 1x, https://photos-kr.kcdn.kz/webp/e9/e9b606b0-4e09-4008-b40e-6d565b0e829d/1-120x90.jpg 1.5x, https://photos-kr.kcdn.kz/webp/e9/e9b606b0-4e09-4008-b40e-6d565b0e829d/1-120x90.jpg 2x"
                                    type="image/jpeg">

                                <img alt="2-комнатная квартира, 120 м², 16/20 этаж на длительный срок, Калдаякова 1 за 550 000 〒 в Астане, Алматы р-н"
                                    title="Аренда квартир в Астане: 2-комнатная квартира, 120 м², 16/20 этаж на длительный срок, Калдаякова 1 за 550 000 〒"
                                    src="https://photos-kr.kcdn.kz/webp/e9/e9b606b0-4e09-4008-b40e-6d565b0e829d/1-60x45.jpg"
                                    srcset="https://photos-kr.kcdn.kz/webp/e9/e9b606b0-4e09-4008-b40e-6d565b0e829d/1-60x45.jpg 1x, https://photos-kr.kcdn.kz/webp/e9/e9b606b0-4e09-4008-b40e-6d565b0e829d/1-120x90.jpg 1.5x, https://photos-kr.kcdn.kz/webp/e9/e9b606b0-4e09-4008-b40e-6d565b0e829d/1-120x90.jpg 2x"
                                    loading="lazy" />
                            </picture>
                        </a>
                    </div>
                    <div class="hot-a-info">
                        <a href="/a/show/678673735" class="tm-click-sidebar-hot-adv">
                            2-комнатная квартира, 120 м², 16/20 этаж на длительный срок
                        </a>
                        &nbsp;<b>за</b>
                        <br>
                        <b class="price">550&nbsp;000&nbsp;<span class="currency-sign offer__currency">〒</span></b>
                        <div>Калдаякова</div>
                    </div>
                </div>

                <div class="hot-a-wrap" title="В горячих с 18:25:13">
                    <div class="hot-a-photo">
                        <a href="/a/show/677714801" class="tm-click-sidebar-hot-adv">


                            <picture class=" is-moderated has-photo" title="" data-photo-id="1" data-name="1"
                                data-full-src="https://photos-kr.kcdn.kz/webp/da/da6a6b40-28d8-42f6-9916-d13756463ad1/1-full.jpg">

                                <source
                                    srcset="https://photos-kr.kcdn.kz/webp/da/da6a6b40-28d8-42f6-9916-d13756463ad1/1-60x45.webp 1x, https://photos-kr.kcdn.kz/webp/da/da6a6b40-28d8-42f6-9916-d13756463ad1/1-120x90.webp 1.5x, https://photos-kr.kcdn.kz/webp/da/da6a6b40-28d8-42f6-9916-d13756463ad1/1-120x90.webp 2x"
                                    type="image/webp">
                                <source
                                    srcset="https://photos-kr.kcdn.kz/webp/da/da6a6b40-28d8-42f6-9916-d13756463ad1/1-60x45.jpg 1x, https://photos-kr.kcdn.kz/webp/da/da6a6b40-28d8-42f6-9916-d13756463ad1/1-120x90.jpg 1.5x, https://photos-kr.kcdn.kz/webp/da/da6a6b40-28d8-42f6-9916-d13756463ad1/1-120x90.jpg 2x"
                                    type="image/jpeg">

                                <img alt="2-комнатная квартира, 60 м², 2/17 этаж посуточно, Сыганак 11 за 30 000 〒 в Астане, Есильский р-н"
                                    title="Аренда квартир в Астане: 2-комнатная квартира, 60 м², 2/17 этаж посуточно, Сыганак 11 за 30 000 〒"
                                    src="https://photos-kr.kcdn.kz/webp/da/da6a6b40-28d8-42f6-9916-d13756463ad1/1-60x45.jpg"
                                    srcset="https://photos-kr.kcdn.kz/webp/da/da6a6b40-28d8-42f6-9916-d13756463ad1/1-60x45.jpg 1x, https://photos-kr.kcdn.kz/webp/da/da6a6b40-28d8-42f6-9916-d13756463ad1/1-120x90.jpg 1.5x, https://photos-kr.kcdn.kz/webp/da/da6a6b40-28d8-42f6-9916-d13756463ad1/1-120x90.jpg 2x"
                                    loading="lazy" />
                            </picture>
                        </a>
                    </div>
                    <div class="hot-a-info">
                        <a href="/a/show/677714801" class="tm-click-sidebar-hot-adv">
                            2-комнатная квартира, 60 м², 2/17 этаж посуточно
                        </a>
                        &nbsp;<b>за</b>
                        <br>
                        <b class="price">30&nbsp;000&nbsp;<span class="currency-sign offer__currency">〒</span></b>
                        <div>Сыганак</div>
                    </div>
                </div>

                <div class="hot-a-wrap" title="В горячих с 18:25:13">
                    <div class="hot-a-photo">
                        <a href="/a/show/679091680" class="tm-click-sidebar-hot-adv">


                            <picture class=" is-moderated has-photo" title="" data-photo-id="1" data-name="1"
                                data-full-src="https://photos-kr.kcdn.kz/webp/49/492d734e-a1c7-4288-9f81-c2733d4abb9f/1-full.jpg">

                                <source
                                    srcset="https://photos-kr.kcdn.kz/webp/49/492d734e-a1c7-4288-9f81-c2733d4abb9f/1-60x45.webp 1x, https://photos-kr.kcdn.kz/webp/49/492d734e-a1c7-4288-9f81-c2733d4abb9f/1-120x90.webp 1.5x, https://photos-kr.kcdn.kz/webp/49/492d734e-a1c7-4288-9f81-c2733d4abb9f/1-120x90.webp 2x"
                                    type="image/webp">
                                <source
                                    srcset="https://photos-kr.kcdn.kz/webp/49/492d734e-a1c7-4288-9f81-c2733d4abb9f/1-60x45.jpg 1x, https://photos-kr.kcdn.kz/webp/49/492d734e-a1c7-4288-9f81-c2733d4abb9f/1-120x90.jpg 1.5x, https://photos-kr.kcdn.kz/webp/49/492d734e-a1c7-4288-9f81-c2733d4abb9f/1-120x90.jpg 2x"
                                    type="image/jpeg">

                                <img alt="1-комнатная квартира, 30 м², 2/16 этаж на длительный срок, проспект Тлендиева 15/4 за 200 000 〒 в Астане, Сарыарка р-н"
                                    title="Аренда квартир в Астане: 1-комнатная квартира, 30 м², 2/16 этаж на длительный срок, проспект Тлендиева 15/4 за 200 000 〒"
                                    src="https://photos-kr.kcdn.kz/webp/49/492d734e-a1c7-4288-9f81-c2733d4abb9f/1-60x45.jpg"
                                    srcset="https://photos-kr.kcdn.kz/webp/49/492d734e-a1c7-4288-9f81-c2733d4abb9f/1-60x45.jpg 1x, https://photos-kr.kcdn.kz/webp/49/492d734e-a1c7-4288-9f81-c2733d4abb9f/1-120x90.jpg 1.5x, https://photos-kr.kcdn.kz/webp/49/492d734e-a1c7-4288-9f81-c2733d4abb9f/1-120x90.jpg 2x"
                                    loading="lazy" />
                            </picture>
                        </a>
                    </div>
                    <div class="hot-a-info">
                        <a href="/a/show/679091680" class="tm-click-sidebar-hot-adv">
                            1-комнатная квартира, 30 м², 2/16 этаж на длительный срок
                        </a>
                        &nbsp;<b>за</b>
                        <br>
                        <b class="price">200&nbsp;000&nbsp;<span class="currency-sign offer__currency">〒</span></b>
                        <div>проспект Тлендиева</div>
                    </div>
                </div>

                <div class="hot-a-wrap" title="В горячих с 18:24:58">
                    <div class="hot-a-photo">
                        <a href="/a/show/678000912" class="tm-click-sidebar-hot-adv">


                            <picture class=" is-moderated has-photo" title="" data-photo-id="1" data-name="1"
                                data-full-src="https://photos-kr.kcdn.kz/webp/39/39b3fe48-44ac-4f2a-b271-4a67db5f25e2/1-full.jpg">

                                <source
                                    srcset="https://photos-kr.kcdn.kz/webp/39/39b3fe48-44ac-4f2a-b271-4a67db5f25e2/1-60x45.webp 1x, https://photos-kr.kcdn.kz/webp/39/39b3fe48-44ac-4f2a-b271-4a67db5f25e2/1-120x90.webp 1.5x, https://photos-kr.kcdn.kz/webp/39/39b3fe48-44ac-4f2a-b271-4a67db5f25e2/1-120x90.webp 2x"
                                    type="image/webp">
                                <source
                                    srcset="https://photos-kr.kcdn.kz/webp/39/39b3fe48-44ac-4f2a-b271-4a67db5f25e2/1-60x45.jpg 1x, https://photos-kr.kcdn.kz/webp/39/39b3fe48-44ac-4f2a-b271-4a67db5f25e2/1-120x90.jpg 1.5x, https://photos-kr.kcdn.kz/webp/39/39b3fe48-44ac-4f2a-b271-4a67db5f25e2/1-120x90.jpg 2x"
                                    type="image/jpeg">

                                <img alt="4-комнатная квартира, 120 м², 9/21 этаж на длительный срок, Кабанбай батыра 43В за 600 000 〒 в Астане"
                                    title="Аренда квартир в Астане: 4-комнатная квартира, 120 м², 9/21 этаж на длительный срок, Кабанбай батыра 43В за 600 000 〒"
                                    src="https://photos-kr.kcdn.kz/webp/39/39b3fe48-44ac-4f2a-b271-4a67db5f25e2/1-60x45.jpg"
                                    srcset="https://photos-kr.kcdn.kz/webp/39/39b3fe48-44ac-4f2a-b271-4a67db5f25e2/1-60x45.jpg 1x, https://photos-kr.kcdn.kz/webp/39/39b3fe48-44ac-4f2a-b271-4a67db5f25e2/1-120x90.jpg 1.5x, https://photos-kr.kcdn.kz/webp/39/39b3fe48-44ac-4f2a-b271-4a67db5f25e2/1-120x90.jpg 2x"
                                    loading="lazy" />
                            </picture>
                        </a>
                    </div>
                    <div class="hot-a-info">
                        <a href="/a/show/678000912" class="tm-click-sidebar-hot-adv">
                            4-комнатная квартира, 120 м², 9/21 этаж на длительный срок
                        </a>
                        &nbsp;<b>за</b>
                        <br>
                        <b class="price">600&nbsp;000&nbsp;<span class="currency-sign offer__currency">〒</span></b>
                        <div>Кабанбай батыра</div>
                    </div>
                </div>

                <div class="hot-a-wrap" title="В горячих с 18:20:15">
                    <div class="hot-a-photo">
                        <a href="/a/show/679046690" class="tm-click-sidebar-hot-adv">


                            <picture class=" is-moderated has-photo" title="" data-photo-id="1" data-name="1"
                                data-full-src="https://photos-kr.kcdn.kz/webp/b7/b794ff46-e3e8-4c20-8b78-32dde02946ca/1-full.jpg">

                                <source
                                    srcset="https://photos-kr.kcdn.kz/webp/b7/b794ff46-e3e8-4c20-8b78-32dde02946ca/1-60x45.webp 1x, https://photos-kr.kcdn.kz/webp/b7/b794ff46-e3e8-4c20-8b78-32dde02946ca/1-120x90.webp 1.5x, https://photos-kr.kcdn.kz/webp/b7/b794ff46-e3e8-4c20-8b78-32dde02946ca/1-120x90.webp 2x"
                                    type="image/webp">
                                <source
                                    srcset="https://photos-kr.kcdn.kz/webp/b7/b794ff46-e3e8-4c20-8b78-32dde02946ca/1-60x45.jpg 1x, https://photos-kr.kcdn.kz/webp/b7/b794ff46-e3e8-4c20-8b78-32dde02946ca/1-120x90.jpg 1.5x, https://photos-kr.kcdn.kz/webp/b7/b794ff46-e3e8-4c20-8b78-32dde02946ca/1-120x90.jpg 2x"
                                    type="image/jpeg">

                                <img alt="1-комнатная квартира, 41 м², 14/16 этаж на длительный срок, Туркестан 10 — Байтерек, ботанический сад за 270 000 〒 в Астане, Есильский р-н"
                                    title="Аренда квартир в Астане: 1-комнатная квартира, 41 м², 14/16 этаж на длительный срок, Туркестан 10 — Байтерек, ботанический сад за 270 000 〒"
                                    src="https://photos-kr.kcdn.kz/webp/b7/b794ff46-e3e8-4c20-8b78-32dde02946ca/1-60x45.jpg"
                                    srcset="https://photos-kr.kcdn.kz/webp/b7/b794ff46-e3e8-4c20-8b78-32dde02946ca/1-60x45.jpg 1x, https://photos-kr.kcdn.kz/webp/b7/b794ff46-e3e8-4c20-8b78-32dde02946ca/1-120x90.jpg 1.5x, https://photos-kr.kcdn.kz/webp/b7/b794ff46-e3e8-4c20-8b78-32dde02946ca/1-120x90.jpg 2x"
                                    loading="lazy" />
                            </picture>
                        </a>
                    </div>
                    <div class="hot-a-info">
                        <a href="/a/show/679046690" class="tm-click-sidebar-hot-adv">
                            1-комнатная квартира, 41 м², 14/16 этаж на длительный срок
                        </a>
                        &nbsp;<b>за</b>
                        <br>
                        <b class="price">270&nbsp;000&nbsp;<span class="currency-sign offer__currency">〒</span></b>
                        <div>Туркестан-Байтерек, ботанический сад</div>
                    </div>
                </div>

                <div class="hot-a-wrap" title="В горячих с 18:18:18">
                    <div class="hot-a-photo">
                        <a href="/a/show/679186392" class="tm-click-sidebar-hot-adv">


                            <picture class=" is-moderated has-photo" title="" data-photo-id="1" data-name="1"
                                data-full-src="https://photos-kr.kcdn.kz/webp/9e/9e0e0f38-ebdb-4cb9-8d37-7f4c1b05235b/1-full.jpg">

                                <source
                                    srcset="https://photos-kr.kcdn.kz/webp/9e/9e0e0f38-ebdb-4cb9-8d37-7f4c1b05235b/1-60x45.webp 1x, https://photos-kr.kcdn.kz/webp/9e/9e0e0f38-ebdb-4cb9-8d37-7f4c1b05235b/1-120x90.webp 1.5x, https://photos-kr.kcdn.kz/webp/9e/9e0e0f38-ebdb-4cb9-8d37-7f4c1b05235b/1-120x90.webp 2x"
                                    type="image/webp">
                                <source
                                    srcset="https://photos-kr.kcdn.kz/webp/9e/9e0e0f38-ebdb-4cb9-8d37-7f4c1b05235b/1-60x45.jpg 1x, https://photos-kr.kcdn.kz/webp/9e/9e0e0f38-ebdb-4cb9-8d37-7f4c1b05235b/1-120x90.jpg 1.5x, https://photos-kr.kcdn.kz/webp/9e/9e0e0f38-ebdb-4cb9-8d37-7f4c1b05235b/1-120x90.jpg 2x"
                                    type="image/jpeg">

                                <img alt="2-комнатная квартира, 65 м², 10/10 этаж на длительный срок, Сыганак 18/1 — Туркестан за 350 000 〒 в Астане, Есильский р-н"
                                    title="Аренда квартир в Астане: 2-комнатная квартира, 65 м², 10/10 этаж на длительный срок, Сыганак 18/1 — Туркестан за 350 000 〒"
                                    src="https://photos-kr.kcdn.kz/webp/9e/9e0e0f38-ebdb-4cb9-8d37-7f4c1b05235b/1-60x45.jpg"
                                    srcset="https://photos-kr.kcdn.kz/webp/9e/9e0e0f38-ebdb-4cb9-8d37-7f4c1b05235b/1-60x45.jpg 1x, https://photos-kr.kcdn.kz/webp/9e/9e0e0f38-ebdb-4cb9-8d37-7f4c1b05235b/1-120x90.jpg 1.5x, https://photos-kr.kcdn.kz/webp/9e/9e0e0f38-ebdb-4cb9-8d37-7f4c1b05235b/1-120x90.jpg 2x"
                                    loading="lazy" />
                            </picture>
                        </a>
                    </div>
                    <div class="hot-a-info">
                        <a href="/a/show/679186392" class="tm-click-sidebar-hot-adv">
                            2-комнатная квартира, 65 м², 10/10 этаж на длительный срок
                        </a>
                        &nbsp;<b>за</b>
                        <br>
                        <b class="price">350&nbsp;000&nbsp;<span class="currency-sign offer__currency">〒</span></b>
                        <div>Сыганак-Туркестан</div>
                    </div>
                </div>

                <div class="hot-a-wrap" title="В горячих с 18:10:52">
                    <div class="hot-a-photo">
                        <a href="/a/show/679165077" class="tm-click-sidebar-hot-adv">


                            <picture class=" is-moderated has-photo" title="" data-photo-id="1" data-name="1"
                                data-full-src="https://photos-kr.kcdn.kz/webp/c7/c7323d52-fd9f-467f-adaa-7be26d4edcc2/1-full.jpg">

                                <source
                                    srcset="https://photos-kr.kcdn.kz/webp/c7/c7323d52-fd9f-467f-adaa-7be26d4edcc2/1-60x45.webp 1x, https://photos-kr.kcdn.kz/webp/c7/c7323d52-fd9f-467f-adaa-7be26d4edcc2/1-120x90.webp 1.5x, https://photos-kr.kcdn.kz/webp/c7/c7323d52-fd9f-467f-adaa-7be26d4edcc2/1-120x90.webp 2x"
                                    type="image/webp">
                                <source
                                    srcset="https://photos-kr.kcdn.kz/webp/c7/c7323d52-fd9f-467f-adaa-7be26d4edcc2/1-60x45.jpg 1x, https://photos-kr.kcdn.kz/webp/c7/c7323d52-fd9f-467f-adaa-7be26d4edcc2/1-120x90.jpg 1.5x, https://photos-kr.kcdn.kz/webp/c7/c7323d52-fd9f-467f-adaa-7be26d4edcc2/1-120x90.jpg 2x"
                                    type="image/jpeg">

                                <img alt="2-комнатная квартира, 55 м², 5/9 этаж на длительный срок, Сыганак 16 — Е-12 за 250 000 〒 в Астане, Есильский р-н"
                                    title="Аренда квартир в Астане: 2-комнатная квартира, 55 м², 5/9 этаж на длительный срок, Сыганак 16 — Е-12 за 250 000 〒"
                                    src="https://photos-kr.kcdn.kz/webp/c7/c7323d52-fd9f-467f-adaa-7be26d4edcc2/1-60x45.jpg"
                                    srcset="https://photos-kr.kcdn.kz/webp/c7/c7323d52-fd9f-467f-adaa-7be26d4edcc2/1-60x45.jpg 1x, https://photos-kr.kcdn.kz/webp/c7/c7323d52-fd9f-467f-adaa-7be26d4edcc2/1-120x90.jpg 1.5x, https://photos-kr.kcdn.kz/webp/c7/c7323d52-fd9f-467f-adaa-7be26d4edcc2/1-120x90.jpg 2x"
                                    loading="lazy" />
                            </picture>
                        </a>
                    </div>
                    <div class="hot-a-info">
                        <a href="/a/show/679165077" class="tm-click-sidebar-hot-adv">
                            2-комнатная квартира, 55 м², 5/9 этаж на длительный срок
                        </a>
                        &nbsp;<b>за</b>
                        <br>
                        <b class="price">250&nbsp;000&nbsp;<span class="currency-sign offer__currency">〒</span></b>
                        <div>Сыганак-Е-12</div>
                    </div>
                </div>

                <div class="br-sticky-wrapper">
                    <div class="br-sticky">
                        <div class="board">
                            <div class="common-b 12 ddl_campaign" id="12" data-campaign-id="12">
                                <div id='div-gpt-ad-1536300745208-0'>
                                    <script type="text/javascript">
                                        googletag.cmd.push(function () {{

                                            googletag.display('div-gpt-ad-1536300745208-0');
                                        }});
                                    </script>
                                </div>
                                <div id='ya-12'></div>
                            </div>
                        </div>
                        <div class="hot-a-wrap" title="В горячих с 18:08:30">
                            <div class="hot-a-photo">
                                <a href="/a/show/679157903" class="tm-click-sidebar-hot-adv">


                                    <picture class=" is-moderated has-photo" title="" data-photo-id="9" data-name="9"
                                        data-full-src="https://photos-kr.kcdn.kz/webp/5a/5a67a899-ec5d-4f69-af66-550a3545c164/9-full.jpg">

                                        <source
                                            srcset="https://photos-kr.kcdn.kz/webp/5a/5a67a899-ec5d-4f69-af66-550a3545c164/9-60x45.webp 1x, https://photos-kr.kcdn.kz/webp/5a/5a67a899-ec5d-4f69-af66-550a3545c164/9-120x90.webp 1.5x, https://photos-kr.kcdn.kz/webp/5a/5a67a899-ec5d-4f69-af66-550a3545c164/9-120x90.webp 2x"
                                            type="image/webp">
                                        <source
                                            srcset="https://photos-kr.kcdn.kz/webp/5a/5a67a899-ec5d-4f69-af66-550a3545c164/9-60x45.jpg 1x, https://photos-kr.kcdn.kz/webp/5a/5a67a899-ec5d-4f69-af66-550a3545c164/9-120x90.jpg 1.5x, https://photos-kr.kcdn.kz/webp/5a/5a67a899-ec5d-4f69-af66-550a3545c164/9-120x90.jpg 2x"
                                            type="image/jpeg">

                                        <img alt="1-комнатная квартира, 40 м², 5/10 этаж на длительный срок, Улы Дала 3/5 за 285 000 〒 в Астане, Есильский р-н"
                                            title="Аренда квартир в Астане: 1-комнатная квартира, 40 м², 5/10 этаж на длительный срок, Улы Дала 3/5 за 285 000 〒"
                                            src="https://photos-kr.kcdn.kz/webp/5a/5a67a899-ec5d-4f69-af66-550a3545c164/9-60x45.jpg"
                                            srcset="https://photos-kr.kcdn.kz/webp/5a/5a67a899-ec5d-4f69-af66-550a3545c164/9-60x45.jpg 1x, https://photos-kr.kcdn.kz/webp/5a/5a67a899-ec5d-4f69-af66-550a3545c164/9-120x90.jpg 1.5x, https://photos-kr.kcdn.kz/webp/5a/5a67a899-ec5d-4f69-af66-550a3545c164/9-120x90.jpg 2x"
                                            loading="lazy" />
                                    </picture>
                                </a>
                            </div>
                            <div class="hot-a-info">
                                <a href="/a/show/679157903" class="tm-click-sidebar-hot-adv">
                                    1-комнатная квартира, 40 м², 5/10 этаж на длительный срок
                                </a>
                                &nbsp;<b>за</b>
                                <br>
                                <b class="price">285&nbsp;000&nbsp;<span
                                        class="currency-sign offer__currency">〒</span></b>
                                <div>Улы Дала</div>
                            </div>
                        </div>

                        <div class="hot-a-wrap" title="В горячих с 18:08:04">
                            <div class="hot-a-photo">
                                <a href="/a/show/679176303" class="tm-click-sidebar-hot-adv">


                                    <picture class=" is-not-moderated" title="" data-photo-id="" data-name=""
                                        data-full-src="">

                                        <source
                                            srcset="//krisha.kz/static/frontend/images/nophoto/60x45.png 1x, //krisha.kz/static/frontend/images/nophoto/120x90.png 1.5x, //krisha.kz/static/frontend/images/nophoto/120x90.png 2x"
                                            type="image/webp">
                                        <source
                                            srcset="//krisha.kz/static/frontend/images/nophoto/60x45.png 1x, //krisha.kz/static/frontend/images/nophoto/120x90.png 1.5x, //krisha.kz/static/frontend/images/nophoto/120x90.png 2x"
                                            type="image/jpeg">

                                        <img alt="" title="" src="//krisha.kz/static/frontend/images/nophoto/60x45.png"
                                            srcset="//krisha.kz/static/frontend/images/nophoto/60x45.png 1x, //krisha.kz/static/frontend/images/nophoto/120x90.png 1.5x, //krisha.kz/static/frontend/images/nophoto/120x90.png 2x"
                                            loading="lazy" />
                                    </picture>
                                </a>
                            </div>
                            <div class="hot-a-info">
                                <a href="/a/show/679176303" class="tm-click-sidebar-hot-adv">
                                    1-комнатная квартира, 30 м², 3/9 этаж на длительный срок
                                </a>
                                &nbsp;<b>за</b>
                                <br>
                                <b class="price">300&nbsp;000&nbsp;<span
                                        class="currency-sign offer__currency">〒</span></b>
                                <div>Сатпаева</div>
                            </div>
                        </div>

                        <div class="hot-a-wrap" title="В горячих с 18:06:34">
                            <div class="hot-a-photo">
                                <a href="/a/show/679147273" class="tm-click-sidebar-hot-adv">


                                    <picture class=" is-moderated has-photo" title="" data-photo-id="1" data-name="1"
                                        data-full-src="https://photos-kr.kcdn.kz/webp/17/17c2cdda-9187-4339-8f32-5c0b35589cef/1-full.jpg">

                                        <source
                                            srcset="https://photos-kr.kcdn.kz/webp/17/17c2cdda-9187-4339-8f32-5c0b35589cef/1-60x45.webp 1x, https://photos-kr.kcdn.kz/webp/17/17c2cdda-9187-4339-8f32-5c0b35589cef/1-120x90.webp 1.5x, https://photos-kr.kcdn.kz/webp/17/17c2cdda-9187-4339-8f32-5c0b35589cef/1-120x90.webp 2x"
                                            type="image/webp">
                                        <source
                                            srcset="https://photos-kr.kcdn.kz/webp/17/17c2cdda-9187-4339-8f32-5c0b35589cef/1-60x45.jpg 1x, https://photos-kr.kcdn.kz/webp/17/17c2cdda-9187-4339-8f32-5c0b35589cef/1-120x90.jpg 1.5x, https://photos-kr.kcdn.kz/webp/17/17c2cdda-9187-4339-8f32-5c0b35589cef/1-120x90.jpg 2x"
                                            type="image/jpeg">

                                        <img alt="1-комнатная квартира, 37 м², 16/24 этаж на длительный срок, Қабанбай батыр 48/7 за 300 000 〒 в Астане, Есильский р-н"
                                            title="Аренда квартир в Астане: 1-комнатная квартира, 37 м², 16/24 этаж на длительный срок, Қабанбай батыр 48/7 за 300 000 〒"
                                            src="https://photos-kr.kcdn.kz/webp/17/17c2cdda-9187-4339-8f32-5c0b35589cef/1-60x45.jpg"
                                            srcset="https://photos-kr.kcdn.kz/webp/17/17c2cdda-9187-4339-8f32-5c0b35589cef/1-60x45.jpg 1x, https://photos-kr.kcdn.kz/webp/17/17c2cdda-9187-4339-8f32-5c0b35589cef/1-120x90.jpg 1.5x, https://photos-kr.kcdn.kz/webp/17/17c2cdda-9187-4339-8f32-5c0b35589cef/1-120x90.jpg 2x"
                                            loading="lazy" />
                                    </picture>
                                </a>
                            </div>
                            <div class="hot-a-info">
                                <a href="/a/show/679147273" class="tm-click-sidebar-hot-adv">
                                    1-комнатная квартира, 37 м², 16/24 этаж на длительный срок
                                </a>
                                &nbsp;<b>за</b>
                                <br>
                                <b class="price">300&nbsp;000&nbsp;<span
                                        class="currency-sign offer__currency">〒</span></b>
                                <div>Қабанбай батыр</div>
                            </div>
                        </div>

                        <div class="hot-a-wrap" title="В горячих с 17:59:34">
                            <div class="hot-a-photo">
                                <a href="/a/show/679121731" class="tm-click-sidebar-hot-adv">


                                    <picture class=" is-moderated has-photo" title="" data-photo-id="1" data-name="1"
                                        data-full-src="https://photos-kr.kcdn.kz/webp/b1/b1fde7db-3180-431e-8c25-3f8785aa7eea/1-full.jpg">

                                        <source
                                            srcset="https://photos-kr.kcdn.kz/webp/b1/b1fde7db-3180-431e-8c25-3f8785aa7eea/1-60x45.webp 1x, https://photos-kr.kcdn.kz/webp/b1/b1fde7db-3180-431e-8c25-3f8785aa7eea/1-120x90.webp 1.5x, https://photos-kr.kcdn.kz/webp/b1/b1fde7db-3180-431e-8c25-3f8785aa7eea/1-120x90.webp 2x"
                                            type="image/webp">
                                        <source
                                            srcset="https://photos-kr.kcdn.kz/webp/b1/b1fde7db-3180-431e-8c25-3f8785aa7eea/1-60x45.jpg 1x, https://photos-kr.kcdn.kz/webp/b1/b1fde7db-3180-431e-8c25-3f8785aa7eea/1-120x90.jpg 1.5x, https://photos-kr.kcdn.kz/webp/b1/b1fde7db-3180-431e-8c25-3f8785aa7eea/1-120x90.jpg 2x"
                                            type="image/jpeg">

                                        <img alt="3-комнатная квартира, 126 м², 22/42 этаж на длительный срок, Достык 5/1 за 500 000 〒 в Астане, Есильский р-н"
                                            title="Аренда квартир в Астане: 3-комнатная квартира, 126 м², 22/42 этаж на длительный срок, Достык 5/1 за 500 000 〒"
                                            src="https://photos-kr.kcdn.kz/webp/b1/b1fde7db-3180-431e-8c25-3f8785aa7eea/1-60x45.jpg"
                                            srcset="https://photos-kr.kcdn.kz/webp/b1/b1fde7db-3180-431e-8c25-3f8785aa7eea/1-60x45.jpg 1x, https://photos-kr.kcdn.kz/webp/b1/b1fde7db-3180-431e-8c25-3f8785aa7eea/1-120x90.jpg 1.5x, https://photos-kr.kcdn.kz/webp/b1/b1fde7db-3180-431e-8c25-3f8785aa7eea/1-120x90.jpg 2x"
                                            loading="lazy" />
                                    </picture>
                                </a>
                            </div>
                            <div class="hot-a-info">
                                <a href="/a/show/679121731" class="tm-click-sidebar-hot-adv">
                                    3-комнатная квартира, 126 м², 22/42 этаж на длительный срок
                                </a>
                                &nbsp;<b>за</b>
                                <br>
                                <b class="price">500&nbsp;000&nbsp;<span
                                        class="currency-sign offer__currency">〒</span></b>
                                <div>Достык</div>
                            </div>
                        </div>

                        <div class="hot-a-wrap" title="В горячих с 17:58:14">
                            <div class="hot-a-photo">
                                <a href="/a/show/679185890" class="tm-click-sidebar-hot-adv">


                                    <picture class=" is-moderated has-photo" title="" data-photo-id="1" data-name="1"
                                        data-full-src="https://photos-kr.kcdn.kz/webp/57/5708ab75-7af0-4468-86dc-b4ca9c5da793/1-full.jpg">

                                        <source
                                            srcset="https://photos-kr.kcdn.kz/webp/57/5708ab75-7af0-4468-86dc-b4ca9c5da793/1-60x45.webp 1x, https://photos-kr.kcdn.kz/webp/57/5708ab75-7af0-4468-86dc-b4ca9c5da793/1-120x90.webp 1.5x, https://photos-kr.kcdn.kz/webp/57/5708ab75-7af0-4468-86dc-b4ca9c5da793/1-120x90.webp 2x"
                                            type="image/webp">
                                        <source
                                            srcset="https://photos-kr.kcdn.kz/webp/57/5708ab75-7af0-4468-86dc-b4ca9c5da793/1-60x45.jpg 1x, https://photos-kr.kcdn.kz/webp/57/5708ab75-7af0-4468-86dc-b4ca9c5da793/1-120x90.jpg 1.5x, https://photos-kr.kcdn.kz/webp/57/5708ab75-7af0-4468-86dc-b4ca9c5da793/1-120x90.jpg 2x"
                                            type="image/jpeg">

                                        <img alt="2-комнатная квартира, 57 м², 8/8 этаж посуточно, Фариза Онгарсынова — Фариза Онгарсынова за 35 000 〒 в Астане, Есильский р-н"
                                            title="Аренда квартир в Астане: 2-комнатная квартира, 57 м², 8/8 этаж посуточно, Фариза Онгарсынова — Фариза Онгарсынова за 35 000 〒"
                                            src="https://photos-kr.kcdn.kz/webp/57/5708ab75-7af0-4468-86dc-b4ca9c5da793/1-60x45.jpg"
                                            srcset="https://photos-kr.kcdn.kz/webp/57/5708ab75-7af0-4468-86dc-b4ca9c5da793/1-60x45.jpg 1x, https://photos-kr.kcdn.kz/webp/57/5708ab75-7af0-4468-86dc-b4ca9c5da793/1-120x90.jpg 1.5x, https://photos-kr.kcdn.kz/webp/57/5708ab75-7af0-4468-86dc-b4ca9c5da793/1-120x90.jpg 2x"
                                            loading="lazy" />
                                    </picture>
                                </a>
                            </div>
                            <div class="hot-a-info">
                                <a href="/a/show/679185890" class="tm-click-sidebar-hot-adv">
                                    2-комнатная квартира, 57 м², 8/8 этаж посуточно
                                </a>
                                &nbsp;<b>за</b>
                                <br>
                                <b class="price">35&nbsp;000&nbsp;<span
                                        class="currency-sign offer__currency">〒</span></b>
                                <div>Фариза Онгарсынова-Фариза Онгарсынова</div>
                            </div>
                        </div>

                        <div class="hot-a-wrap" title="В горячих с 17:57:54">
                            <div class="hot-a-photo">
                                <a href="/a/show/679158269" class="tm-click-sidebar-hot-adv">


                                    <picture class=" is-moderated has-photo" title="" data-photo-id="1" data-name="1"
                                        data-full-src="https://photos-kr.kcdn.kz/webp/ab/ab4d2e45-d1e2-42e3-99e8-36d4b56f8083/1-full.jpg">

                                        <source
                                            srcset="https://photos-kr.kcdn.kz/webp/ab/ab4d2e45-d1e2-42e3-99e8-36d4b56f8083/1-60x45.webp 1x, https://photos-kr.kcdn.kz/webp/ab/ab4d2e45-d1e2-42e3-99e8-36d4b56f8083/1-120x90.webp 1.5x, https://photos-kr.kcdn.kz/webp/ab/ab4d2e45-d1e2-42e3-99e8-36d4b56f8083/1-120x90.webp 2x"
                                            type="image/webp">
                                        <source
                                            srcset="https://photos-kr.kcdn.kz/webp/ab/ab4d2e45-d1e2-42e3-99e8-36d4b56f8083/1-60x45.jpg 1x, https://photos-kr.kcdn.kz/webp/ab/ab4d2e45-d1e2-42e3-99e8-36d4b56f8083/1-120x90.jpg 1.5x, https://photos-kr.kcdn.kz/webp/ab/ab4d2e45-d1e2-42e3-99e8-36d4b56f8083/1-120x90.jpg 2x"
                                            type="image/jpeg">

                                        <img alt="3-комнатная квартира, 85 м², 6/8 этаж посуточно, 37-я за 65 000 〒 в Астане, Есильский р-н"
                                            title="Аренда квартир в Астане: 3-комнатная квартира, 85 м², 6/8 этаж посуточно, 37-я за 65 000 〒"
                                            src="https://photos-kr.kcdn.kz/webp/ab/ab4d2e45-d1e2-42e3-99e8-36d4b56f8083/1-60x45.jpg"
                                            srcset="https://photos-kr.kcdn.kz/webp/ab/ab4d2e45-d1e2-42e3-99e8-36d4b56f8083/1-60x45.jpg 1x, https://photos-kr.kcdn.kz/webp/ab/ab4d2e45-d1e2-42e3-99e8-36d4b56f8083/1-120x90.jpg 1.5x, https://photos-kr.kcdn.kz/webp/ab/ab4d2e45-d1e2-42e3-99e8-36d4b56f8083/1-120x90.jpg 2x"
                                            loading="lazy" />
                                    </picture>
                                </a>
                            </div>
                            <div class="hot-a-info">
                                <a href="/a/show/679158269" class="tm-click-sidebar-hot-adv">
                                    3-комнатная квартира, 85 м², 6/8 этаж посуточно
                                </a>
                                &nbsp;<b>за</b>
                                <br>
                                <b class="price">65&nbsp;000&nbsp;<span
                                        class="currency-sign offer__currency">〒</span></b>
                                <div>37-я</div>
                            </div>
                        </div>

                        <div class="hot-a-wrap" title="В горячих с 17:55:12">
                            <div class="hot-a-photo">
                                <a href="/a/show/663937319" class="tm-click-sidebar-hot-adv">


                                    <picture class=" is-moderated has-photo" title="" data-photo-id="48" data-name="48"
                                        data-full-src="https://photos-kr.kcdn.kz/webp/52/52a73ccf-c88f-491f-b311-f2486db28aed/48-full.jpg">

                                        <source
                                            srcset="https://photos-kr.kcdn.kz/webp/52/52a73ccf-c88f-491f-b311-f2486db28aed/48-60x45.webp 1x, https://photos-kr.kcdn.kz/webp/52/52a73ccf-c88f-491f-b311-f2486db28aed/48-120x90.webp 1.5x, https://photos-kr.kcdn.kz/webp/52/52a73ccf-c88f-491f-b311-f2486db28aed/48-120x90.webp 2x"
                                            type="image/webp">
                                        <source
                                            srcset="https://photos-kr.kcdn.kz/webp/52/52a73ccf-c88f-491f-b311-f2486db28aed/48-60x45.jpg 1x, https://photos-kr.kcdn.kz/webp/52/52a73ccf-c88f-491f-b311-f2486db28aed/48-120x90.jpg 1.5x, https://photos-kr.kcdn.kz/webp/52/52a73ccf-c88f-491f-b311-f2486db28aed/48-120x90.jpg 2x"
                                            type="image/jpeg">

                                        <img alt="1-комнатная квартира, 36 м², 7/9 этаж посуточно, Ильяс Омаров 27 — Кайыма Мухамедханова за 15 000 〒 в Астане, Есильский р-н"
                                            title="Аренда квартир в Астане: 1-комнатная квартира, 36 м², 7/9 этаж посуточно, Ильяс Омаров 27 — Кайыма Мухамедханова за 15 000 〒"
                                            src="https://photos-kr.kcdn.kz/webp/52/52a73ccf-c88f-491f-b311-f2486db28aed/48-60x45.jpg"
                                            srcset="https://photos-kr.kcdn.kz/webp/52/52a73ccf-c88f-491f-b311-f2486db28aed/48-60x45.jpg 1x, https://photos-kr.kcdn.kz/webp/52/52a73ccf-c88f-491f-b311-f2486db28aed/48-120x90.jpg 1.5x, https://photos-kr.kcdn.kz/webp/52/52a73ccf-c88f-491f-b311-f2486db28aed/48-120x90.jpg 2x"
                                            loading="lazy" />
                                    </picture>
                                </a>
                            </div>
                            <div class="hot-a-info">
                                <a href="/a/show/663937319" class="tm-click-sidebar-hot-adv">
                                    1-комнатная квартира, 36 м², 7/9 этаж посуточно
                                </a>
                                &nbsp;<b>за</b>
                                <br>
                                <b class="price">15&nbsp;000&nbsp;<span
                                        class="currency-sign offer__currency">〒</span></b>
                                <div>Ильяс Омаров-Кайыма Мухамедханова</div>
                            </div>
                        </div>

                        <div class="hot-a-wrap" title="В горячих с 17:55:05">
                            <div class="hot-a-photo">
                                <a href="/a/show/674436285" class="tm-click-sidebar-hot-adv">


                                    <picture class=" is-moderated has-photo" title="" data-photo-id="1" data-name="1"
                                        data-full-src="https://photos-kr.kcdn.kz/webp/21/2161faec-297a-4b86-8b6a-4fd98267a78b/1-full.jpg">

                                        <source
                                            srcset="https://photos-kr.kcdn.kz/webp/21/2161faec-297a-4b86-8b6a-4fd98267a78b/1-60x45.webp 1x, https://photos-kr.kcdn.kz/webp/21/2161faec-297a-4b86-8b6a-4fd98267a78b/1-120x90.webp 1.5x, https://photos-kr.kcdn.kz/webp/21/2161faec-297a-4b86-8b6a-4fd98267a78b/1-120x90.webp 2x"
                                            type="image/webp">
                                        <source
                                            srcset="https://photos-kr.kcdn.kz/webp/21/2161faec-297a-4b86-8b6a-4fd98267a78b/1-60x45.jpg 1x, https://photos-kr.kcdn.kz/webp/21/2161faec-297a-4b86-8b6a-4fd98267a78b/1-120x90.jpg 1.5x, https://photos-kr.kcdn.kz/webp/21/2161faec-297a-4b86-8b6a-4fd98267a78b/1-120x90.jpg 2x"
                                            type="image/jpeg">

                                        <img alt="4-комнатная квартира, 115 м², 4/9 этаж на длительный срок, Тыныбаева 4 за 650 000 〒 в Астане"
                                            title="Аренда квартир в Астане: 4-комнатная квартира, 115 м², 4/9 этаж на длительный срок, Тыныбаева 4 за 650 000 〒"
                                            src="https://photos-kr.kcdn.kz/webp/21/2161faec-297a-4b86-8b6a-4fd98267a78b/1-60x45.jpg"
                                            srcset="https://photos-kr.kcdn.kz/webp/21/2161faec-297a-4b86-8b6a-4fd98267a78b/1-60x45.jpg 1x, https://photos-kr.kcdn.kz/webp/21/2161faec-297a-4b86-8b6a-4fd98267a78b/1-120x90.jpg 1.5x, https://photos-kr.kcdn.kz/webp/21/2161faec-297a-4b86-8b6a-4fd98267a78b/1-120x90.jpg 2x"
                                            loading="lazy" />
                                    </picture>
                                </a>
                            </div>
                            <div class="hot-a-info">
                                <a href="/a/show/674436285" class="tm-click-sidebar-hot-adv">
                                    4-комнатная квартира, 115 м², 4/9 этаж на длительный срок
                                </a>
                                &nbsp;<b>за</b>
                                <br>
                                <b class="price">650&nbsp;000&nbsp;<span
                                        class="currency-sign offer__currency">〒</span></b>
                                <div>Тыныбаева</div>
                            </div>
                        </div>

                        <div class="hot-a-wrap" title="В горячих с 17:52:34">
                            <div class="hot-a-photo">
                                <a href="/a/show/667590192" class="tm-click-sidebar-hot-adv">


                                    <picture class=" is-moderated has-photo" title="" data-photo-id="32" data-name="32"
                                        data-full-src="https://photos-kr.kcdn.kz/webp/df/df9d30f5-a8b9-4cc1-8f85-5c55376ba87f/32-full.jpg">

                                        <source
                                            srcset="https://photos-kr.kcdn.kz/webp/df/df9d30f5-a8b9-4cc1-8f85-5c55376ba87f/32-60x45.webp 1x, https://photos-kr.kcdn.kz/webp/df/df9d30f5-a8b9-4cc1-8f85-5c55376ba87f/32-120x90.webp 1.5x, https://photos-kr.kcdn.kz/webp/df/df9d30f5-a8b9-4cc1-8f85-5c55376ba87f/32-120x90.webp 2x"
                                            type="image/webp">
                                        <source
                                            srcset="https://photos-kr.kcdn.kz/webp/df/df9d30f5-a8b9-4cc1-8f85-5c55376ba87f/32-60x45.jpg 1x, https://photos-kr.kcdn.kz/webp/df/df9d30f5-a8b9-4cc1-8f85-5c55376ba87f/32-120x90.jpg 1.5x, https://photos-kr.kcdn.kz/webp/df/df9d30f5-a8b9-4cc1-8f85-5c55376ba87f/32-120x90.jpg 2x"
                                            type="image/jpeg">

                                        <img alt="1-комнатная квартира, 50 м², 11/14 этаж посуточно, Кабанбай батыра за 40 000 〒 в Астане, Есильский р-н"
                                            title="Аренда квартир в Астане: 1-комнатная квартира, 50 м², 11/14 этаж посуточно, Кабанбай батыра за 40 000 〒"
                                            src="https://photos-kr.kcdn.kz/webp/df/df9d30f5-a8b9-4cc1-8f85-5c55376ba87f/32-60x45.jpg"
                                            srcset="https://photos-kr.kcdn.kz/webp/df/df9d30f5-a8b9-4cc1-8f85-5c55376ba87f/32-60x45.jpg 1x, https://photos-kr.kcdn.kz/webp/df/df9d30f5-a8b9-4cc1-8f85-5c55376ba87f/32-120x90.jpg 1.5x, https://photos-kr.kcdn.kz/webp/df/df9d30f5-a8b9-4cc1-8f85-5c55376ba87f/32-120x90.jpg 2x"
                                            loading="lazy" />
                                    </picture>
                                </a>
                            </div>
                            <div class="hot-a-info">
                                <a href="/a/show/667590192" class="tm-click-sidebar-hot-adv">
                                    1-комнатная квартира, 50 м², 11/14 этаж посуточно
                                </a>
                                &nbsp;<b>за</b>
                                <br>
                                <b class="price">40&nbsp;000&nbsp;<span
                                        class="currency-sign offer__currency">〒</span></b>
                                <div>Кабанбай батыра</div>
                            </div>
                        </div>

                        <div class="hot-a-wrap" title="В горячих с 17:50:14">
                            <div class="hot-a-photo">
                                <a href="/a/show/676048150" class="tm-click-sidebar-hot-adv">


                                    <picture class=" is-moderated has-photo" title="" data-photo-id="6" data-name="6"
                                        data-full-src="https://photos-kr.kcdn.kz/webp/69/69c3188a-a9b8-480e-b648-0394102c2e5b/6-full.jpg">

                                        <source
                                            srcset="https://photos-kr.kcdn.kz/webp/69/69c3188a-a9b8-480e-b648-0394102c2e5b/6-60x45.webp 1x, https://photos-kr.kcdn.kz/webp/69/69c3188a-a9b8-480e-b648-0394102c2e5b/6-120x90.webp 1.5x, https://photos-kr.kcdn.kz/webp/69/69c3188a-a9b8-480e-b648-0394102c2e5b/6-120x90.webp 2x"
                                            type="image/webp">
                                        <source
                                            srcset="https://photos-kr.kcdn.kz/webp/69/69c3188a-a9b8-480e-b648-0394102c2e5b/6-60x45.jpg 1x, https://photos-kr.kcdn.kz/webp/69/69c3188a-a9b8-480e-b648-0394102c2e5b/6-120x90.jpg 1.5x, https://photos-kr.kcdn.kz/webp/69/69c3188a-a9b8-480e-b648-0394102c2e5b/6-120x90.jpg 2x"
                                            type="image/jpeg">

                                        <img alt="2-комнатная квартира, 66.8 м², 4/12 этаж посуточно, Сейфуллина 33 за 40 000 〒 в Астане, Алматы р-н"
                                            title="Аренда квартир в Астане: 2-комнатная квартира, 66.8 м², 4/12 этаж посуточно, Сейфуллина 33 за 40 000 〒"
                                            src="https://photos-kr.kcdn.kz/webp/69/69c3188a-a9b8-480e-b648-0394102c2e5b/6-60x45.jpg"
                                            srcset="https://photos-kr.kcdn.kz/webp/69/69c3188a-a9b8-480e-b648-0394102c2e5b/6-60x45.jpg 1x, https://photos-kr.kcdn.kz/webp/69/69c3188a-a9b8-480e-b648-0394102c2e5b/6-120x90.jpg 1.5x, https://photos-kr.kcdn.kz/webp/69/69c3188a-a9b8-480e-b648-0394102c2e5b/6-120x90.jpg 2x"
                                            loading="lazy" />
                                    </picture>
                                </a>
                            </div>
                            <div class="hot-a-info">
                                <a href="/a/show/676048150" class="tm-click-sidebar-hot-adv">
                                    2-комнатная квартира, 66.8 м², 4/12 этаж посуточно
                                </a>
                                &nbsp;<b>за</b>
                                <br>
                                <b class="price">40&nbsp;000&nbsp;<span
                                        class="currency-sign offer__currency">〒</span></b>
                                <div>Сейфуллина</div>
                            </div>
                        </div>

                        <div class="hot-a-wrap" title="В горячих с 17:48:11">
                            <div class="hot-a-photo">
                                <a href="/a/show/679176204" class="tm-click-sidebar-hot-adv">


                                    <picture class=" is-moderated has-photo" title="" data-photo-id="1" data-name="1"
                                        data-full-src="https://photos-kr.kcdn.kz/webp/7c/7c25d969-735d-401d-9b9a-b99b2c8358ea/1-full.jpg">

                                        <source
                                            srcset="https://photos-kr.kcdn.kz/webp/7c/7c25d969-735d-401d-9b9a-b99b2c8358ea/1-60x45.webp 1x, https://photos-kr.kcdn.kz/webp/7c/7c25d969-735d-401d-9b9a-b99b2c8358ea/1-120x90.webp 1.5x, https://photos-kr.kcdn.kz/webp/7c/7c25d969-735d-401d-9b9a-b99b2c8358ea/1-120x90.webp 2x"
                                            type="image/webp">
                                        <source
                                            srcset="https://photos-kr.kcdn.kz/webp/7c/7c25d969-735d-401d-9b9a-b99b2c8358ea/1-60x45.jpg 1x, https://photos-kr.kcdn.kz/webp/7c/7c25d969-735d-401d-9b9a-b99b2c8358ea/1-120x90.jpg 1.5x, https://photos-kr.kcdn.kz/webp/7c/7c25d969-735d-401d-9b9a-b99b2c8358ea/1-120x90.jpg 2x"
                                            type="image/jpeg">

                                        <img alt="4-комнатная квартира, 160 м², 3/9 этаж на длительный срок, Сауран — Достык за 600 000 〒 в Астане, Есильский р-н"
                                            title="Аренда квартир в Астане: 4-комнатная квартира, 160 м², 3/9 этаж на длительный срок, Сауран — Достык за 600 000 〒"
                                            src="https://photos-kr.kcdn.kz/webp/7c/7c25d969-735d-401d-9b9a-b99b2c8358ea/1-60x45.jpg"
                                            srcset="https://photos-kr.kcdn.kz/webp/7c/7c25d969-735d-401d-9b9a-b99b2c8358ea/1-60x45.jpg 1x, https://photos-kr.kcdn.kz/webp/7c/7c25d969-735d-401d-9b9a-b99b2c8358ea/1-120x90.jpg 1.5x, https://photos-kr.kcdn.kz/webp/7c/7c25d969-735d-401d-9b9a-b99b2c8358ea/1-120x90.jpg 2x"
                                            loading="lazy" />
                                    </picture>
                                </a>
                            </div>
                            <div class="hot-a-info">
                                <a href="/a/show/679176204" class="tm-click-sidebar-hot-adv">
                                    4-комнатная квартира, 160 м², 3/9 этаж на длительный срок
                                </a>
                                &nbsp;<b>за</b>
                                <br>
                                <b class="price">600&nbsp;000&nbsp;<span
                                        class="currency-sign offer__currency">〒</span></b>
                                <div>Сауран-Достык</div>
                            </div>
                        </div>

                        <div class="hot-a-wrap" title="В горячих с 17:47:04">
                            <div class="hot-a-photo">
                                <a href="/a/show/679071341" class="tm-click-sidebar-hot-adv">


                                    <picture class=" is-moderated has-photo" title="" data-photo-id="1" data-name="1"
                                        data-full-src="https://photos-kr.kcdn.kz/webp/6b/6ba93998-0cef-4a26-a84c-f1708d577cf5/1-full.jpg">

                                        <source
                                            srcset="https://photos-kr.kcdn.kz/webp/6b/6ba93998-0cef-4a26-a84c-f1708d577cf5/1-60x45.webp 1x, https://photos-kr.kcdn.kz/webp/6b/6ba93998-0cef-4a26-a84c-f1708d577cf5/1-120x90.webp 1.5x, https://photos-kr.kcdn.kz/webp/6b/6ba93998-0cef-4a26-a84c-f1708d577cf5/1-120x90.webp 2x"
                                            type="image/webp">
                                        <source
                                            srcset="https://photos-kr.kcdn.kz/webp/6b/6ba93998-0cef-4a26-a84c-f1708d577cf5/1-60x45.jpg 1x, https://photos-kr.kcdn.kz/webp/6b/6ba93998-0cef-4a26-a84c-f1708d577cf5/1-120x90.jpg 1.5x, https://photos-kr.kcdn.kz/webp/6b/6ba93998-0cef-4a26-a84c-f1708d577cf5/1-120x90.jpg 2x"
                                            type="image/jpeg">

                                        <img alt="1-комнатная квартира, 35 м², 3/5 этаж на длительный срок, Акбугы 5 за 130 000 〒 в Астане, Сарыарка р-н"
                                            title="Аренда квартир в Астане: 1-комнатная квартира, 35 м², 3/5 этаж на длительный срок, Акбугы 5 за 130 000 〒"
                                            src="https://photos-kr.kcdn.kz/webp/6b/6ba93998-0cef-4a26-a84c-f1708d577cf5/1-60x45.jpg"
                                            srcset="https://photos-kr.kcdn.kz/webp/6b/6ba93998-0cef-4a26-a84c-f1708d577cf5/1-60x45.jpg 1x, https://photos-kr.kcdn.kz/webp/6b/6ba93998-0cef-4a26-a84c-f1708d577cf5/1-120x90.jpg 1.5x, https://photos-kr.kcdn.kz/webp/6b/6ba93998-0cef-4a26-a84c-f1708d577cf5/1-120x90.jpg 2x"
                                            loading="lazy" />
                                    </picture>
                                </a>
                            </div>
                            <div class="hot-a-info">
                                <a href="/a/show/679071341" class="tm-click-sidebar-hot-adv">
                                    1-комнатная квартира, 35 м², 3/5 этаж на длительный срок
                                </a>
                                &nbsp;<b>за</b>
                                <br>
                                <b class="price">130&nbsp;000&nbsp;<span
                                        class="currency-sign offer__currency">〒</span></b>
                                <div>Акбугы</div>
                            </div>
                        </div>

                        <div class="cross-links">
                            <ul class="crosslinks crosslinks-block-1">
                                <li class="">
                                    <a href="/arenda/kvartiry/?das[live.rooms]=1">Аренда 1-комнатных квартир</a>
                                </li>
                                <li class="">
                                    <a href="/arenda/kvartiry/?das[live.rooms]=2">Аренда 2-комнатных квартир</a>
                                </li>
                                <li class="">
                                    <a href="/arenda/kvartiry/?das[live.rooms]=3">Аренда 3-комнатных квартир</a>
                                </li>
                                <li class="">
                                    <a href="/arenda/kvartiry/?das[live.rooms]=4">Аренда 4-комнатных квартир</a>
                                </li>
                                <li class="">
                                    <a href="/arenda/kvartiry/?das[live.rooms]=5">Аренда 5-комнатных квартир</a>
                                </li>
                                <li class="">
                                    <a href="/arenda/kvartiry/nur-sultan/?das[live.furniture]=1">Полностью квартиры</a>
                                </li>
                                <li class="">
                                    <a href="/arenda/kvartiry/nur-sultan/?das[live.furniture]=2">Частично квартиры</a>
                                </li>
                            </ul>
                            <ul class="crosslinks crosslinks-block-2">
                                <li class="">
                                    <a href="/arenda/kvartiry/nur-sultan/?das[live.rooms]=1">Аренда 1-комнатных квартир
                                        в вашем городе</a>
                                </li>
                                <li class="">
                                    <a href="/arenda/kvartiry/nur-sultan/?das[live.rooms]=2">Аренда 2-комнатных квартир
                                        в вашем городе</a>
                                </li>
                                <li class="">
                                    <a href="/arenda/kvartiry/nur-sultan/?das[live.rooms]=3">Аренда 3-комнатных квартир
                                        в вашем городе</a>
                                </li>
                                <li class="">
                                    <a href="/arenda/kvartiry/nur-sultan/?das[live.rooms]=4">Аренда 4-комнатных квартир
                                        в вашем городе</a>
                                </li>
                                <li class="">
                                    <a href="/arenda/kvartiry/nur-sultan/?das[live.rooms]=5">Аренда 5-комнатных квартир
                                        в вашем городе</a>
                                </li>
                                <li class="">
                                    <a href="/arenda/kvartiry/nur-sultan/?das[live.rooms]=1&amp;das[rent.period]=2">1-комнатные
                                        квартиры на длительный срок</a>
                                </li>
                                <li class="">
                                    <a href="/arenda/kvartiry/nur-sultan/?das[live.rooms]=1&amp;das[rent.period]=1">1-комнатные
                                        квартиры посуточно</a>
                                </li>
                                <li class="">
                                    <a href="/arenda/kvartiry/nur-sultan/?das[live.rooms]=1&amp;das[rent.period]=4">1-комнатные
                                        квартиры по часам</a>
                                </li>
                                <li class="">
                                    <a href="/arenda/kvartiry/nur-sultan/?das[live.rooms]=2&amp;das[rent.period]=2">2-комнатные
                                        квартиры на длительный срок</a>
                                </li>
                                <li class="">
                                    <a href="/arenda/kvartiry/nur-sultan/?das[live.rooms]=2&amp;das[rent.period]=1">2-комнатные
                                        квартиры посуточно</a>
                                </li>
                                <li class="crosslink-toggle-btn">
                                    <a href="#" class="link dotted" data-show-text="Показать все"
                                        data-hide-text="Скрыть">Показать все</a>
                                </li>
                                <li class="crosslink-hidden">
                                    <a href="/arenda/kvartiry/nur-sultan/?das[live.rooms]=2&amp;das[rent.period]=4">2-комнатные
                                        квартиры по часам</a>
                                </li>
                                <li class="crosslink-hidden">
                                    <a href="/arenda/kvartiry/nur-sultan/?das[live.rooms]=3&amp;das[rent.period]=2">3-комнатные
                                        квартиры на длительный срок</a>
                                </li>
                                <li class="crosslink-hidden">
                                    <a href="/arenda/kvartiry/nur-sultan/?das[live.rooms]=3&amp;das[rent.period]=1">3-комнатные
                                        квартиры посуточно</a>
                                </li>
                                <li class="crosslink-hidden">
                                    <a href="/arenda/kvartiry/nur-sultan/?das[live.rooms]=3&amp;das[rent.period]=4">3-комнатные
                                        квартиры по часам</a>
                                </li>
                                <li class="crosslink-hidden">
                                    <a href="/arenda/kvartiry/nur-sultan/?das[live.rooms]=4&amp;das[rent.period]=2">4-комнатные
                                        квартиры на длительный срок</a>
                                </li>
                                <li class="crosslink-hidden">
                                    <a href="/arenda/kvartiry/nur-sultan/?das[live.rooms]=4&amp;das[rent.period]=1">4-комнатные
                                        квартиры посуточно</a>
                                </li>
                                <li class="crosslink-hidden">
                                    <a href="/arenda/kvartiry/nur-sultan/?das[live.rooms]=5&amp;das[rent.period]=2">5-комнатные
                                        квартиры на длительный срок</a>
                                </li>
                            </ul>
                            <ul class="crosslinks crosslinks-block-3">
                                <li class="">
                                    <a href="/arenda/kvartiry/nur-sultan/?das[live.rooms]=1&amp;das[who]=1">1-комнатные
                                        квартиры без посредников</a>
                                </li>
                                <li class="">
                                    <a href="/arenda/kvartiry/nur-sultan/?das[live.rooms]=2&amp;das[who]=1">2-комнатные
                                        квартиры без посредников</a>
                                </li>
                                <li class="">
                                    <a href="/arenda/kvartiry/nur-sultan/?das[live.rooms]=3&amp;das[who]=1">3-комнатные
                                        квартиры без посредников</a>
                                </li>
                                <li class="">
                                    <a href="/arenda/kvartiry/nur-sultan/?das[live.rooms]=4&amp;das[who]=1">4-комнатные
                                        квартиры без посредников</a>
                                </li>
                            </ul>
                            <ul class="crosslinks crosslinks-block-4">
                                <li class="">
                                    <a href="/arenda/kvartiry/aksaj/">Аренда квартиры в Аксае</a>
                                </li>
                                <li class="">
                                    <a href="/arenda/kvartiry/aktau/">Аренда квартиры в Актау</a>
                                </li>
                                <li class="">
                                    <a href="/arenda/kvartiry/aktobe/">Аренда квартиры в Актобе</a>
                                </li>
                                <li class="">
                                    <a href="/arenda/kvartiry/almaty/">Аренда квартиры в Алматы</a>
                                </li>
                                <li class="">
                                    <a href="/arenda/kvartiry/atyrau/">Аренда квартиры в Атырау</a>
                                </li>
                                <li class="">
                                    <a href="/arenda/kvartiry/bajkonur/">Аренда квартиры в Байконуре</a>
                                </li>
                                <li class="">
                                    <a href="/arenda/kvartiry/balhash/">Аренда квартиры в Балхаше</a>
                                </li>
                                <li class="">
                                    <a href="/arenda/kvartiry/zhezkazgan/">Аренда квартиры в Жезказгане</a>
                                </li>
                                <li class="">
                                    <a href="/arenda/kvartiry/karaganda/">Аренда квартиры в Караганде</a>
                                </li>
                                <li class="">
                                    <a href="/arenda/kvartiry/kaskelen/">Аренда квартиры в Каскелене</a>
                                </li>
                                <li class="crosslink-toggle-btn">
                                    <a href="#" class="link dotted" data-show-text="Показать все"
                                        data-hide-text="Скрыть">Показать все</a>
                                </li>
                                <li class="crosslink-hidden">
                                    <a href="/arenda/kvartiry/kokshetau/">Аренда квартиры в Кокшетау</a>
                                </li>
                                <li class="crosslink-hidden">
                                    <a href="/arenda/kvartiry/konaev/">Аренда квартиры в Конаеве (Капчагай)</a>
                                </li>
                                <li class="crosslink-hidden">
                                    <a href="/arenda/kvartiry/kostanaj/">Аренда квартиры в Костанае</a>
                                </li>
                                <li class="crosslink-hidden">
                                    <a href="/arenda/kvartiry/kulsary/">Аренда квартиры в Кульсары</a>
                                </li>
                                <li class="crosslink-hidden">
                                    <a href="/arenda/kvartiry/kyzylorda/">Аренда квартиры в Кызылорда</a>
                                </li>
                                <li class="crosslink-hidden">
                                    <a href="/arenda/kvartiry/lisakovsk/">Аренда квартиры в Лисаковске</a>
                                </li>
                                <li class="crosslink-hidden">
                                    <a href="/arenda/kvartiry/nur-sultan/">Аренда квартиры в Нур-Султане (Астане)</a>
                                </li>
                                <li class="crosslink-hidden">
                                    <a href="/arenda/kvartiry/pavlodar/">Аренда квартиры в Павлодаре</a>
                                </li>
                                <li class="crosslink-hidden">
                                    <a href="/arenda/kvartiry/petropavlovsk/">Аренда квартиры в Петропавловске</a>
                                </li>
                                <li class="crosslink-hidden">
                                    <a href="/arenda/kvartiry/ridder/">Аренда квартиры в Риддере</a>
                                </li>
                                <li class="crosslink-hidden">
                                    <a href="/arenda/kvartiry/rudnyj/">Аренда квартиры в Рудном</a>
                                </li>
                                <li class="crosslink-hidden">
                                    <a href="/arenda/kvartiry/semej/">Аренда квартиры в Семее</a>
                                </li>
                                <li class="crosslink-hidden">
                                    <a href="/arenda/kvartiry/talgar/">Аренда квартиры в Талгаре</a>
                                </li>
                                <li class="crosslink-hidden">
                                    <a href="/arenda/kvartiry/taldykorgan/">Аренда квартиры в Талдыкоргане</a>
                                </li>
                                <li class="crosslink-hidden">
                                    <a href="/arenda/kvartiry/taraz/">Аренда квартиры в Таразе</a>
                                </li>
                                <li class="crosslink-hidden">
                                    <a href="/arenda/kvartiry/temirtau/">Аренда квартиры в Темиртау</a>
                                </li>
                                <li class="crosslink-hidden">
                                    <a href="/arenda/kvartiry/turkestan/">Аренда квартиры в Туркестане</a>
                                </li>
                                <li class="crosslink-hidden">
                                    <a href="/arenda/kvartiry/uralsk/">Аренда квартиры в Уральске</a>
                                </li>
                                <li class="crosslink-hidden">
                                    <a href="/arenda/kvartiry/ust-kamenogorsk/">Аренда квартиры в Усть-Каменогорске</a>
                                </li>
                                <li class="crosslink-hidden">
                                    <a href="/arenda/kvartiry/shahtinsk/">Аренда квартиры в Шахтинске</a>
                                </li>
                                <li class="crosslink-hidden">
                                    <a href="/arenda/kvartiry/shymkent/">Аренда квартиры в Шымкенте</a>
                                </li>
                                <li class="crosslink-hidden">
                                    <a href="/arenda/kvartiry/shhuchinsk/">Аренда квартиры в Щучинске</a>
                                </li>
                                <li class="crosslink-hidden">
                                    <a href="/arenda/kvartiry/ekibastuz/">Аренда квартиры в Экибастузе</a>
                                </li>
                                <li class="crosslink-hidden">
                                    <a href="/arenda/kvartiry/aksaj/">Аренда квартиры в Аксае</a>
                                </li>
                                <li class="crosslink-hidden">
                                    <a href="/arenda/kvartiry/aktau/">Аренда квартиры в Актау</a>
                                </li>
                                <li class="crosslink-hidden">
                                    <a href="/arenda/kvartiry/aktobe/">Аренда квартиры в Актобе</a>
                                </li>
                                <li class="crosslink-hidden">
                                    <a href="/arenda/kvartiry/almaty/">Аренда квартиры в Алматы</a>
                                </li>
                                <li class="crosslink-hidden">
                                    <a href="/arenda/kvartiry/atyrau/">Аренда квартиры в Атырау</a>
                                </li>
                                <li class="crosslink-hidden">
                                    <a href="/arenda/kvartiry/bajkonur/">Аренда квартиры в Байконуре</a>
                                </li>
                                <li class="crosslink-hidden">
                                    <a href="/arenda/kvartiry/balhash/">Аренда квартиры в Балхаше</a>
                                </li>
                                <li class="crosslink-hidden">
                                    <a href="/arenda/kvartiry/zhezkazgan/">Аренда квартиры в Жезказгане</a>
                                </li>
                                <li class="crosslink-hidden">
                                    <a href="/arenda/kvartiry/karaganda/">Аренда квартиры в Караганде</a>
                                </li>
                                <li class="crosslink-hidden">
                                    <a href="/arenda/kvartiry/kaskelen/">Аренда квартиры в Каскелене</a>
                                </li>
                                <li class="crosslink-hidden">
                                    <a href="/arenda/kvartiry/kokshetau/">Аренда квартиры в Кокшетау</a>
                                </li>
                                <li class="crosslink-hidden">
                                    <a href="/arenda/kvartiry/konaev/">Аренда квартиры в Конаеве (Капчагай)</a>
                                </li>
                                <li class="crosslink-hidden">
                                    <a href="/arenda/kvartiry/kostanaj/">Аренда квартиры в Костанае</a>
                                </li>
                                <li class="crosslink-hidden">
                                    <a href="/arenda/kvartiry/kulsary/">Аренда квартиры в Кульсары</a>
                                </li>
                                <li class="crosslink-hidden">
                                    <a href="/arenda/kvartiry/kyzylorda/">Аренда квартиры в Кызылорда</a>
                                </li>
                                <li class="crosslink-hidden">
                                    <a href="/arenda/kvartiry/lisakovsk/">Аренда квартиры в Лисаковске</a>
                                </li>
                                <li class="crosslink-hidden">
                                    <a href="/arenda/kvartiry/nur-sultan/">Аренда квартиры в Нур-Султане (Астане)</a>
                                </li>
                                <li class="crosslink-hidden">
                                    <a href="/arenda/kvartiry/pavlodar/">Аренда квартиры в Павлодаре</a>
                                </li>
                                <li class="crosslink-hidden">
                                    <a href="/arenda/kvartiry/petropavlovsk/">Аренда квартиры в Петропавловске</a>
                                </li>
                                <li class="crosslink-hidden">
                                    <a href="/arenda/kvartiry/ridder/">Аренда квартиры в Риддере</a>
                                </li>
                                <li class="crosslink-hidden">
                                    <a href="/arenda/kvartiry/rudnyj/">Аренда квартиры в Рудном</a>
                                </li>
                                <li class="crosslink-hidden">
                                    <a href="/arenda/kvartiry/semej/">Аренда квартиры в Семее</a>
                                </li>
                                <li class="crosslink-hidden">
                                    <a href="/arenda/kvartiry/talgar/">Аренда квартиры в Талгаре</a>
                                </li>
                                <li class="crosslink-hidden">
                                    <a href="/arenda/kvartiry/taldykorgan/">Аренда квартиры в Талдыкоргане</a>
                                </li>
                                <li class="crosslink-hidden">
                                    <a href="/arenda/kvartiry/taraz/">Аренда квартиры в Таразе</a>
                                </li>
                                <li class="crosslink-hidden">
                                    <a href="/arenda/kvartiry/temirtau/">Аренда квартиры в Темиртау</a>
                                </li>
                                <li class="crosslink-hidden">
                                    <a href="/arenda/kvartiry/turkestan/">Аренда квартиры в Туркестане</a>
                                </li>
                                <li class="crosslink-hidden">
                                    <a href="/arenda/kvartiry/uralsk/">Аренда квартиры в Уральске</a>
                                </li>
                                <li class="crosslink-hidden">
                                    <a href="/arenda/kvartiry/ust-kamenogorsk/">Аренда квартиры в Усть-Каменогорске</a>
                                </li>
                                <li class="crosslink-hidden">
                                    <a href="/arenda/kvartiry/shahtinsk/">Аренда квартиры в Шахтинске</a>
                                </li>
                                <li class="crosslink-hidden">
                                    <a href="/arenda/kvartiry/shymkent/">Аренда квартиры в Шымкенте</a>
                                </li>
                                <li class="crosslink-hidden">
                                    <a href="/arenda/kvartiry/shhuchinsk/">Аренда квартиры в Щучинске</a>
                                </li>
                                <li class="crosslink-hidden">
                                    <a href="/arenda/kvartiry/ekibastuz/">Аренда квартиры в Экибастузе</a>
                                </li>
                            </ul>
                            <ul class="crosslinks crosslinks-block-5">
                                <li class="">
                                    <a href="/arenda/kvartiry/nur-sultan/?das[flat.renovation]=2">В среднем
                                        состоянии</a>
                                </li>
                                <li class="">
                                    <a href="/arenda/kvartiry/nur-sultan/?das[flat.renovation]=1">В хорошем
                                        состоянии</a>
                                </li>
                                <li class="">
                                    <a href="/arenda/kvartiry/nur-sultan/?das[flat.renovation]=5">Свободная
                                        планировка</a>
                                </li>
                                <li class="">
                                    <a href="/arenda/kvartiry/nur-sultan/?das[flat.toilet]=3">Квартиры с двумя и более
                                        санузлами</a>
                                </li>
                                <li class="">
                                    <a href="/arenda/kvartiry/nur-sultan/?das[inet.type]=1">C интернетом</a>
                                </li>
                                <li class="">
                                    <a href="/arenda/kvartiry/nur-sultan/?das[live.furniture]=3">Без мебели</a>
                                </li>
                                <li class="">
                                    <a href="/arenda/kvartiry/nur-sultan/?das[flat.priv_dorm]=1">В приватизированном
                                        общежитии</a>
                                </li>
                                <li class="">
                                    <a href="/arenda/kvartiry/nur-sultan/?das[flat.building]=1">В кирпичном доме</a>
                                </li>
                                <li class="">
                                    <a href="/arenda/kvartiry/nur-sultan/?das[flat.building]=3">В монолитном доме</a>
                                </li>
                                <li class="">
                                    <a href="/arenda/kvartiry/nur-sultan/?das[flat.building]=2">В панельном доме</a>
                                </li>
                                <li class="crosslink-toggle-btn">
                                    <a href="#" class="link dotted" data-show-text="Показать все"
                                        data-hide-text="Скрыть">Показать все</a>
                                </li>
                                <li class="crosslink-hidden">
                                    <a href="/arenda/kvartiry/nur-sultan/">C телефоном</a>
                                </li>
                            </ul>

                        </div>
                    </div>
                </div>

            </aside>
        </section>
    </main>

    <footer class="container footer">
        <div class="footer-row">
            <div class="col-xs-2 col-sm-2 first-side">
                <span class="gray">&copy; 2006 &mdash; 2022 &laquo;Крыша&raquo;</span>
                <a href="/content/special/agreement">Пользовательское соглашение</a>
                <a href="/sitemap" title="Основная карта сайта">Карта сайта</a>
                <a class="rules-link" href="/content/special/info/regulations"
                    title="Правила размещения объявлений">Правила размещения объявлений</a>
            </div>

            <div class="col-xs-5 col-sm-5">
                <div class="row">
                    <div class="col-xs-5 col-sm-6 col-sm-offset-1 second-side">
                        Информация <a href="/content/special/info/site">о сайте</a> и <a
                            href="/content/special/info/paper">газете</a>
                        <br>
                        <br>
                        <a href=/content/special/write-us/message>
                            Написать в службу заботы
                        </a>

                        <a class="job-link" target="_blank" href="http://job.kolesa.kz">Работа в &laquo;Колёса Крыша
                            Маркет&raquo;</a>

                        <div class="footer-social">
                            <span class="gray">Следите за нашими новостями</span>

                            <div class="social-links">
                                <a href="https://www.facebook.com/krisha.kz" rel="nofollow" target="_blank"
                                    title="Крыша в Facebook">
                                    <span class="fi-soc-facebook"></span>
                                </a>
                                <a href="https://www.youtube.com/channel/UCwRTPCE3dGzd6w3BKSQRPxQ" rel="nofollow"
                                    target="_blank" title="Крыша в Youtube">
                                    <span class="fi-soc-youtube"></span>
                                </a>
                                <a href="https://www.instagram.com/krisha.kz" rel="nofollow" target="_blank"
                                    title="Крыша в Instagram">
                                    <span class="fi-soc-instagram"></span>
                                </a>
                                <a href="https://vk.com/krishakz" rel="nofollow" target="_blank"
                                    title="Крыша вКонтакте">
                                    <span class="fi-soc-vk"></span>
                                </a>
                            </div>
                        </div>
                    </div>
                    <div class="col-xs-5 col-sm-5 third-side">
                        <a href="/favorites/advert/" class="selected-a-favorites fav-nb-text">У вас нет выбранных
                            объявлений</a>
                        <a href="/my" class="cabinet-link"><span class="fi-person"></span>Личный кабинет</a>
                        <a href="/a/new" class="a-new-link"><span class="fi-plus"></span>Подать объявление</a>
                    </div>
                </div>
            </div>

            <div class="col-xs-5 col-sm-5 fourth-side">
                <div class="mobile-applications-link">
                    <div class="clearfix">
                        <div class="mobile-text">
                            <a href="/promo/mobile">Приложения для Android и iOS</a>
                            <br>
                            <a
                                href="https://m.krisha.kz/arenda/kvartiry/nur-sultan/?das%5B_sys.hasphoto%5D=1&amp;das%5Bprice%5D%5Bto%5D=10000&amp;das%5Brent.period%5D=1">Мобильная
                                версия сайта</a>
                        </div>
                    </div>
                    <a target="_blank" href="//special.kolesa.group/reklama/krisha" class="for-a-sers">Рекламодателям
                        посвящается</a>
                </div>
            </div>
        </div>
    </footer>

    <div id="right-bottom-notice" class="right-bottom-notice">
        <div id="push-notification-block"></div>


        <div id="nps-container"></div>
    </div>



    <noscript>
        <iframe src="//www.googletagmanager.com/ns.html?id=GTM-WQVJLC" height="0" width="0"
            style="display:none;visibility:hidden"></iframe>
    </noscript> <noscript>
        <img src="https://mc.yandex.ru/watch/10575199?ut=noindex" style="position:absolute; left:-9999px;" alt="" />
        <img src="https://mc.yandex.ru/watch/51631367?ut=noindex" style="position:absolute; left:-9999px;" alt="" />
    </noscript>
    <script type="text/javascript" src="https://pay.krisha.kz/static/js/gateway/common/iframe-loader.js?v1"></script>

    <script type="text/javascript" src="//krisha.kz/static/frontend/js/lang/ru.2cb3c548e1.js"></script>

    <script type="text/javascript" src="//krisha.kz/static/frontend/js/main-old-browser.ec9ee7b9d1.js"></script>
    <script type="text/javascript" src="//krisha.kz/static/frontend/js/main-runtime.e0b9cb3ec7.js"></script>
    <script type="text/javascript" src="//krisha.kz/static/frontend/js/main-vendor.3d0e85222a.js"></script>
    <script type="text/javascript" src="//krisha.kz/static/frontend/js/main-common.f5924b9ec4.js"></script>

    <script type="text/javascript" src="//krisha.kz/static/frontend/js/main-a-search-list.b3805df612.js"></script>


    <script type="text/javascript">
        (function (d, w, c) {{
            (w[c] = w[c] || []).push(function () {{
                try {{
                    w.yaCounter10575199 = new Ya.Metrika({{
                        id: 10575199,
                        clickmap: true,
                        trackLinks: true,
                        accurateTrackBounce: true,
                        webvisor: true,
                        trackHash: true,
                        triggerEvent: true,
                        ut: "noindex"
                    }});
                }} catch (e) {{ }}

                try {{
                    w.yaCounter51631367 = new Ya.Metrika({{
                        id: 51631367,
                        clickmap: true,
                        trackLinks: true,
                        accurateTrackBounce: true,
                        webvisor: false,
                        trackHash: true,
                        triggerEvent: true,
                        ut: "noindex"
                    }});
                }} catch (e) {{ }}
            }});

            var n = d.getElementsByTagName("script")[0],
                s = d.createElement("script"),
                f = function () {{ n.parentNode.insertBefore(s, n); }};
            s.type = "text/javascript";
            s.async = true;
            s.src = "https://mc.yandex.ru/metrika/watch.js";

            if (w.opera == "[object Opera]") {{
                d.addEventListener("DOMContentLoaded", f, false);
            }} else {{ f(); }}
        }})(document, window, "yandex_metrika_callbacks");
    </script>
    <script type='text/javascript'>
        var googletag = googletag || {{}};
        googletag.cmd = googletag.cmd || [];
        (function () {{
            var gads = document.createElement('script');
            gads.async = true;
            gads.type = 'text/javascript';
            var useSSL = 'https:' == document.location.protocol;
            gads.src = (useSSL ? 'https:' : 'http:') +
                '//www.googletagservices.com/tag/js/gpt.js';
            var node = document.getElementsByTagName('script')[0];
            node.parentNode.insertBefore(gads, node);
        }})();
        /**
         * Получает высоту скрытого элемента
         *
         * @param el - нужный нам элемент
         * @returns {{number}} высота элемента
         * @see {{@link https://stackoverflow.com/a/29047232}}
         */
        var getHeight = function (el) {{
            var elStyle = window.getComputedStyle(el),
                elDisplay = elStyle.display,
                elPosition = elStyle.position,
                elVisibility = elStyle.visibility,
                elMaxHeight = elStyle.maxHeight.replace('px', '').replace('%', ''),
                wantedHeight = 0;

            if (elDisplay !== 'none' && elMaxHeight !== '0') {{
                return el.offsetHeight;
            }}

            el.style.position = 'absolute';
            el.style.visibility = 'hidden';
            el.style.display = 'block';

            wantedHeight = el.offsetHeight;

            el.style.display = elDisplay;
            el.style.position = elPosition;
            el.style.visibility = elVisibility;

            return wantedHeight;
        }};

        googletag.cmd.push(function () {{
            var
                iterations = 0,
                interval = window.setInterval(function () {{
                    var elements = document.body.querySelectorAll('.common-b');
                    var el;

                    if (elements.length < 1 || ++iterations > 20) {{
                        window.clearInterval(interval);
                    }}

                    for (var i = 0; i < elements.length; i++) {{
                        el = elements[i];

                        if (el.classList.contains('b') || el.classList.contains('c') || el.classList.contains('e')) {{
                            const hiddenYaAdvert = document.querySelector('yatag');

                            if (hiddenYaAdvert && window.getComputedStyle(hiddenYaAdvert).display === "none") {{
                                hiddenYaAdvert.style.display = 'block';
                            }} else if (hiddenYaAdvert && window.getComputedStyle(hiddenYaAdvert).visibility === "hidden") {{
                                hiddenYaAdvert.style.visibility = 'visible';
                            }}

                            // хардкодим стили по совету яндекса
                            const backgroundYaAdvert = el.querySelector('yatag a[style*="background"]');

                            if (backgroundYaAdvert) {{
                                backgroundYaAdvert.style.width = '280px';
                                backgroundYaAdvert.style.maxWidth = '280px';
                            }}

                            const pixelYaAdvert = el.querySelector('yatag[style*="728px"]');

                            if (pixelYaAdvert) {{
                                pixelYaAdvert.style.width = '100%';
                                pixelYaAdvert.style.maxWidth = '100%';
                            }}
                        }}

                        const advertHeight = getHeight(el);

                        if (advertHeight > 0) {{
                            el.style.visibility = 'visible';
                            el.classList.add('loaded');
                        }}
                    }}
                }}, 500);
        }});

        googletag.cmd.push(function () {{
            googletag.pubads().setTargeting('kr_category', 'Аренда');
            googletag.pubads().setTargeting('kr_type', 'Квартиры');
            googletag.pubads().setTargeting('kr_city', 'Астана');
            googletag.pubads().setTargeting('kr_price', '0-18000000');
        }});
    </script>
    <!-- Google Tag Manager -->
    <script>
        function initGtm(w, d, s, l, i) {{
            w[l] = w[l] || [];
            w[l].push(
                {{ 'gtm.start': new Date().getTime(), event: 'gtm.js' }}
            );
            var f = d.getElementsByTagName(s)[0],
                j = d.createElement(s), dl = l != 'dataLayer' ? '&l=' + l : '';
            j.async = true;
            j.src =
                '//www.googletagmanager.com/gtm.js?id=' + i + dl;
            f.parentNode.insertBefore(j, f);
        }}

        window.onload = function () {{
            initGtm(window, document, 'script', 'dataLayer', 'GTM-WQVJLC');
        }};
    </script>
    <!-- End Google Tag Manager -->

    <script type="text/javascript" src="//www.googleadservices.com/pagead/conversion.js"></script>
    <script type="text/javascript">
        try {{
            (function () {{
                var prefix = "", hash = "Osxx1D3Ci1PSRxbmdEFU", rtbhTags = [];
                rtbhTags.push("pr_" + hash + "");
                var key = "__rtbhouse.lid", lid = window.localStorage.getItem(key);
                if (!lid) {{
                    lid = ""; var pool = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
                    for (var i = 0; i < 20; i++) lid += pool.charAt(Math.floor(Math.random() * pool.length));
                    window.localStorage.setItem(key, lid);
                }}
                rtbhTags.push("pr_" + hash + "_lid_" + lid);
                var ifr = document.createElement("iframe"),
                    sr = encodeURIComponent(document.referrer ? document.referrer : ""),
                    su = encodeURIComponent(document.location.href ? document.location.href : ""),
                    ifrSrc = "https://" + prefix + "creativecdn.com/tags?type=iframe", tmstmp = encodeURIComponent("" + Date.now());
                for (var i = 0; i < rtbhTags.length; i++) {{ ifrSrc += "&id=" + encodeURIComponent(rtbhTags[i]); }}
                ifrSrc += "&su=" + su + "&sr=" + sr + "&ts=" + tmstmp;
                ifr.setAttribute("src", ifrSrc); ifr.setAttribute("width", "1");
                ifr.setAttribute("height", "1"); ifr.setAttribute("scrolling", "no");
                ifr.setAttribute("frameBorder", "0"); ifr.setAttribute("style", "display:none");
                ifr.setAttribute("referrerpolicy", "no-referrer-when-downgrade");
                if (document.body) {{ document.body.appendChild(ifr); }}
                else {{ window.addEventListener('DOMContentLoaded', function () {{ document.body.appendChild(ifr); }}); }}
            }})();
        }} catch (e) {{ }}
    </script>

    <script type="text/javascript" async="async" src="//krisha.kz/cdn.js"></script>
</body>

</html>
"""