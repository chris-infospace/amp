from flask import Flask
from flask_restful import Resource, Api
from time import sleep

app = Flask(__name__)
api = Api(app)

bingdata = {
	"top": [{
			"display_url": "www.cheaptickets.com/Flights",
			"title": "AD1 -- <strong>Airlines</strong> - Lowest Price Guaranteed | cheaptickets.com",
			"description": "Find your best deal from 450+ <strong>Airlines</strong>. Book a Flight &amp; Hotel to save more!",
			"url": "http://ccs.infospace.com/ClickHandler.ashx?encp=ld%3d20170830%26app%3d1%26c%3ddogpl.100%26s%3ddogpilesem%26rc%3ddogpl.300%26dc%3d%26euip%3d104.132.11.74%26pvaid%3de6a8799486614194bae5467d76ce1d31%26dt%3dDesktop%26fct.uid%3ddddaea275d7e4d759eb57b7755b44a37%26en%3d352GU4fR56WY6dtc5jlLFS1qfqwkvnZ3WLV07iuIzB20xQ26pTFYPQ%253d%253d%26coi%3d1493%26npp%3d0%26p%3d1%26pp%3d0%26mid%3d9%26ep%3d1%26ru%3dhttps%253a%252f%252f2359788.r.bat.bing.com%252f%253fld%253dd3Ci_8HPI2MMo8ULpA9OyXljVUCUyoVOtlwpvTwIwlHHMhHkOBtZoZBvouZOJlR7aD7PJTvXXK_POQHZM1l3omlhVsP1rzbiBlgww0patz5txLGho28o7-gRO3ymGYmLq58W3Tf7O2Ez3SB3natxl-dd0csaI%2526u%253dhttp%25253a%25252f%25252f1195.xg4ken.com%25252ftrk%25252fv1%25253fprof%25253d107%252526camp%25253d184806%252526affcode%25253dkw24897%252526kct%25253dmsn%252526kchid%25253d2359788%252526cid%25253d73461193247625%252526queryStr%25253dairlines%252526kdv%25253dc%252526criteriaid%25253dkwd-14966926842%252526adgroupid%25253d1531911971%252526campaignid%25253d51868923%252526url%25253dhttps%25253a%25252f%25252fwww.cheaptickets.com%25252fFlights%25253fsemcid%25253dcheaptickets-us.multilob.bing.gt-c-en.flight%252526kword%25253dbe.%25257cairlines%25257c.107.184806.410.24897.73461193247625.1531911971.kwd-14966926842.s%252526semdtl%25253da151868923.b11531911971.d173461193247625.e1c.f1.g1kwd-14966926842.h1e.i1.j1.k1.l1s.m1be.n1%252526epi%25253d_kenshoo_clickid_%26du%3dwww.cheaptickets.com%252fFlights%26hash%3dF29D167EBAA87DAB8D6ED835B893AACB&ap=0&cop=main-title&om_userid=WuWG1m1lIw1lbevx1l4I&om_sessionid=GMlva6OKEexxdZ4T3hX7&om_pageid=XygfQ04Q6uehLcmXWrKW&om_nextpage=true",
			"type": "ad",
			"deeplinks": [{
				"title": "Deals on 325,000 Hotels",
				"url": "http://ccs.infospace.com/ClickHandler.ashx?encp=ld%3d20170830%26app%3d1%26c%3ddogpl.100%26s%3ddogpilesem%26rc%3ddogpl.300%26dc%3d%26euip%3d104.132.11.74%26pvaid%3de6a8799486614194bae5467d76ce1d31%26dt%3dDesktop%26fct.uid%3ddddaea275d7e4d759eb57b7755b44a37%26en%3d352GU4fR56WY6dtc5jlLFS1qfqwkvnZ3WLV07iuIzB20xQ26pTFYPQ%253d%253d%26coi%3d1506%26npp%3d0%26p%3d1%26pp%3d0%26mid%3d5%26ep%3d1%26ru%3dhttps%253a%252f%252f2359788.r.bat.bing.com%252f%253fld%253dd3E9u_D_kuh0mWFYUStglnXzVUCUyMH4-llq8ORBycY5nkZAqU4vC-cGlfBx4hBoEqCaCduwEYl_p9Ts9JTKpB96cKvZQ6KL-8dNoTRggbWCshguhs2KfiTJBj8XrpORzZvxjaIzkyZMedsm7YY--fksqKuT0%2526u%253dhttp%25253a%25252f%25252f1195.xg4ken.com%25252fmedia%25252fredir.php%25253fprof%25253d%252526camp%25253d%252526affcode%25253d%252526k_inner_url_encoded%25253d0%252526cid%25253d73461193247625%25257c%25257cairlines%252526mType%25253de%252526networkType%25253dsearch%252526kdv%25253dc%252526ksl%25253d382772%252526url%25255b%25255d%25253dhttps%25253a%25252f%25252fwww.cheaptickets.com%25252fg%25252fun%25252fdeals%25253fsemcid%25253dcheaptickets-us.multilob.bing.gt-c-en.flight%252526kword%25253dbe.%25257cairlines%25257c.107.184806.410.24897.73461193247625.1531911971.kwd-14966926842.s%252526epic%25253d_kenshoo_clickid_%252526epi%25253d_kenshoo_clickid_%252526semdtl%25253da151868923.b11531911971.d173461193247625.e1c.f1.g1kwd-14966926842.h1e.i1.j1.k1.l1s.m1be.n1%26hash%3d5AD34DD20F61683C49B7F64F541E17A3&ap=0&cop=main-title&om_userid=WuWG1m1lIw1lbevx1l4I&om_sessionid=GMlva6OKEexxdZ4T3hX7&om_pageid=XygfQ04Q6uehLcmXWrKW&om_nextpage=true",
				"type": "deeplink"
			}, {
				"title": "Flights Under $199",
				"url": "http://ccs.infospace.com/ClickHandler.ashx?encp=ld%3d20170830%26app%3d1%26c%3ddogpl.100%26s%3ddogpilesem%26rc%3ddogpl.300%26dc%3d%26euip%3d104.132.11.74%26pvaid%3de6a8799486614194bae5467d76ce1d31%26dt%3dDesktop%26fct.uid%3ddddaea275d7e4d759eb57b7755b44a37%26en%3d352GU4fR56WY6dtc5jlLFS1qfqwkvnZ3WLV07iuIzB20xQ26pTFYPQ%253d%253d%26coi%3d1506%26npp%3d0%26p%3d1%26pp%3d0%26mid%3d5%26ep%3d2%26ru%3dhttps%253a%252f%252f2359788.r.bat.bing.com%252f%253fld%253dd3dXlk72wkdDe-kCUowHt8mTVUCUyXQb49ma1CWIE3BrWHLSwVCFmxQPO7NH7S6jbITJWTySR2Z0761Ehzqq7eKhf51f_G09nR9Ibkl2J4F_C6p2k2f7CuDMTzIhkzdeZO5bEBaf5jmjcYJFV2zEfKwsvuXPE%2526u%253dhttp%25253a%25252f%25252f1195.xg4ken.com%25252fmedia%25252fredir.php%25253fprof%25253d%252526camp%25253d%252526affcode%25253d%252526k_inner_url_encoded%25253d0%252526cid%25253d73461193247625%25257c%25257cairlines%252526mType%25253de%252526networkType%25253dsearch%252526kdv%25253dc%252526ksl%25253d382773%252526url%25255b%25255d%25253dhttps%25253a%25252f%25252fwww.cheaptickets.com%25252fg%25252fdd%25252fflightdeals-under199%25253fsemcid%25253dcheaptickets-us.multilob.bing.gt-c-en.flight%252526kword%25253dbe.%25257cairlines%25257c.107.184806.410.24897.73461193247625.1531911971.kwd-14966926842.s%252526epic%25253d_kenshoo_clickid_%252526epi%25253d_kenshoo_clickid_%252526semdtl%25253da151868923.b11531911971.d173461193247625.e1c.f1.g1kwd-14966926842.h1e.i1.j1.k1.l1s.m1be.n1%26hash%3dBAE69F9FBB1314BEDC3531D58FD23B70&ap=0&cop=main-title&om_userid=WuWG1m1lIw1lbevx1l4I&om_sessionid=GMlva6OKEexxdZ4T3hX7&om_pageid=XygfQ04Q6uehLcmXWrKW&om_nextpage=true",
				"type": "deeplink"
			}, {
				"title": "Secret Bargain Deals",
				"url": "http://ccs.infospace.com/ClickHandler.ashx?encp=ld%3d20170830%26app%3d1%26c%3ddogpl.100%26s%3ddogpilesem%26rc%3ddogpl.300%26dc%3d%26euip%3d104.132.11.74%26pvaid%3de6a8799486614194bae5467d76ce1d31%26dt%3dDesktop%26fct.uid%3ddddaea275d7e4d759eb57b7755b44a37%26en%3d352GU4fR56WY6dtc5jlLFS1qfqwkvnZ3WLV07iuIzB20xQ26pTFYPQ%253d%253d%26coi%3d1506%26npp%3d0%26p%3d1%26pp%3d0%26mid%3d5%26ep%3d3%26ru%3dhttps%253a%252f%252f2359788.r.bat.bing.com%252f%253fld%253dd3SDfyNlKpGq-JRxqkk4QIIzVUCUzKV3nB1_ns6rin3v278QcuP6h6mEJ8l_0DHvlcmzyb7k5UBykIpIw0IUDvE2ZWY1l4WAlVk9bUKKucR7eli6QhG0oI6Z7GlIq0XJE4ePEpFEQuMWrFTOCyMC793o93MBo%2526u%253dhttp%25253a%25252f%25252f1195.xg4ken.com%25252fmedia%25252fredir.php%25253fprof%25253d%252526camp%25253d%252526affcode%25253d%252526k_inner_url_encoded%25253d0%252526cid%25253d73461193247625%25257c%25257cairlines%252526mType%25253de%252526networkType%25253dsearch%252526kdv%25253dc%252526ksl%25253d382774%252526url%25255b%25255d%25253dhttps%25253a%25252f%25252fwww.cheaptickets.com%25252fg%25252fmb%25252ftraveldeals-secret-bargains%25253fsemcid%25253dcheaptickets-us.multilob.bing.gt-c-en.flight%252526kword%25253dbe.%25257cairlines%25257c.107.184806.410.24897.73461193247625.1531911971.kwd-14966926842.s%252526epic%25253d_kenshoo_clickid_%252526epi%25253d_kenshoo_clickid_%252526semdtl%25253da151868923.b11531911971.d173461193247625.e1c.f1.g1kwd-14966926842.h1e.i1.j1.k1.l1s.m1be.n1%26hash%3d6DDD9D30F85EE7FD63BB2E66BBF3751B&ap=0&cop=main-title&om_userid=WuWG1m1lIw1lbevx1l4I&om_sessionid=GMlva6OKEexxdZ4T3hX7&om_pageid=XygfQ04Q6uehLcmXWrKW&om_nextpage=true",
				"type": "deeplink"
			}, {
				"title": "Up to 50% off Hotels",
				"url": "http://ccs.infospace.com/ClickHandler.ashx?encp=ld%3d20170830%26app%3d1%26c%3ddogpl.100%26s%3ddogpilesem%26rc%3ddogpl.300%26dc%3d%26euip%3d104.132.11.74%26pvaid%3de6a8799486614194bae5467d76ce1d31%26dt%3dDesktop%26fct.uid%3ddddaea275d7e4d759eb57b7755b44a37%26en%3d352GU4fR56WY6dtc5jlLFS1qfqwkvnZ3WLV07iuIzB20xQ26pTFYPQ%253d%253d%26coi%3d1506%26npp%3d0%26p%3d1%26pp%3d0%26mid%3d5%26ep%3d4%26ru%3dhttps%253a%252f%252f2359788.r.bat.bing.com%252f%253fld%253dd3JmZDnB4Z-sSFy9_M_Ki82jVUCUwPcKDcU_FBLZd7a0JYTSe7CDOTOsNC0DVVAIvaeFT7FKr_KoQ8d_MyTyXohYSiyf5Z-4ZTfQFJzhJBbiCcoaQOxZKl_4jmTaQ9V4YromhB0dWRS2NukR7Qb3xB-y1NLV4%2526u%253dhttp%25253a%25252f%25252f1195.xg4ken.com%25252fmedia%25252fredir.php%25253fprof%25253d%252526camp%25253d%252526affcode%25253d%252526k_inner_url_encoded%25253d0%252526cid%25253d73461193247625%25257c%25257cairlines%252526mType%25253de%252526networkType%25253dsearch%252526kdv%25253dc%252526ksl%25253d382775%252526url%25255b%25255d%25253dhttps%25253a%25252f%25252fwww.cheaptickets.com%25252fg%25252flc%25252ftraveldeals-major-hotel-sale%25253fsemcid%25253dcheaptickets-us.multilob.bing.gt-c-en.flight%252526kword%25253dbe.%25257cairlines%25257c.107.184806.410.24897.73461193247625.1531911971.kwd-14966926842.s%252526epic%25253d_kenshoo_clickid_%252526epi%25253d_kenshoo_clickid_%252526semdtl%25253da151868923.b11531911971.d173461193247625.e1c.f1.g1kwd-14966926842.h1e.i1.j1.k1.l1s.m1be.n1%26hash%3d37B67A0189CFBA566A5BC460ABA49575&ap=0&cop=main-title&om_userid=WuWG1m1lIw1lbevx1l4I&om_sessionid=GMlva6OKEexxdZ4T3hX7&om_pageid=XygfQ04Q6uehLcmXWrKW&om_nextpage=true",
				"type": "deeplink"
			}, {
				"title": "Save Extra 16% On Hotels",
				"url": "http://ccs.infospace.com/ClickHandler.ashx?encp=ld%3d20170830%26app%3d1%26c%3ddogpl.100%26s%3ddogpilesem%26rc%3ddogpl.300%26dc%3d%26euip%3d104.132.11.74%26pvaid%3de6a8799486614194bae5467d76ce1d31%26dt%3dDesktop%26fct.uid%3ddddaea275d7e4d759eb57b7755b44a37%26en%3d352GU4fR56WY6dtc5jlLFS1qfqwkvnZ3WLV07iuIzB20xQ26pTFYPQ%253d%253d%26coi%3d1506%26npp%3d0%26p%3d1%26pp%3d0%26mid%3d5%26ep%3d5%26ru%3dhttps%253a%252f%252f2359788.r.bat.bing.com%252f%253fld%253dd3tB5RgIrnsuRAcZR4adoKPjVUCUzC5gba-AksX-ZG11Yp6hN6oIwYI2k1H6eaK_09_dW1gx0mjby7Y6iZPbaa66Q-Zg8CEquRMWeqkzu-sYO9CvsXfxflWtqqZBqSuTCUo3notCen4gV49BEZ1eXV77dMspM%2526u%253dhttp%25253a%25252f%25252f1195.xg4ken.com%25252fmedia%25252fredir.php%25253fprof%25253d%252526camp%25253d%252526affcode%25253d%252526k_inner_url_encoded%25253d0%252526cid%25253d73461193247625%25257c%25257cairlines%252526mType%25253de%252526networkType%25253dsearch%252526kdv%25253dc%252526ksl%25253d382776%252526url%25255b%25255d%25253dhttps%25253a%25252f%25252fwww.cheaptickets.com%25252fg%25252flc%25252ftraveldeals-cheapoftheweek%25253fsemcid%25253dcheaptickets-us.multilob.bing.gt-c-en.flight%252526kword%25253dbe.%25257cairlines%25257c.107.184806.410.24897.73461193247625.1531911971.kwd-14966926842.s%252526epic%25253d_kenshoo_clickid_%252526epi%25253d_kenshoo_clickid_%252526semdtl%25253da151868923.b11531911971.d173461193247625.e1c.f1.g1kwd-14966926842.h1e.i1.j1.k1.l1s.m1be.n1%26hash%3d8DD9CD0750AD8A4C1AF824B003BCE0AA&ap=0&cop=main-title&om_userid=WuWG1m1lIw1lbevx1l4I&om_sessionid=GMlva6OKEexxdZ4T3hX7&om_pageid=XygfQ04Q6uehLcmXWrKW&om_nextpage=true",
				"type": "deeplink"
			}, {
				"title": "Hotels Under $50",
				"url": "http://ccs.infospace.com/ClickHandler.ashx?encp=ld%3d20170830%26app%3d1%26c%3ddogpl.100%26s%3ddogpilesem%26rc%3ddogpl.300%26dc%3d%26euip%3d104.132.11.74%26pvaid%3de6a8799486614194bae5467d76ce1d31%26dt%3dDesktop%26fct.uid%3ddddaea275d7e4d759eb57b7755b44a37%26en%3d352GU4fR56WY6dtc5jlLFS1qfqwkvnZ3WLV07iuIzB20xQ26pTFYPQ%253d%253d%26coi%3d1506%26npp%3d0%26p%3d1%26pp%3d0%26mid%3d5%26ep%3d6%26ru%3dhttps%253a%252f%252f2359788.r.bat.bing.com%252f%253fld%253dd3Tv4BT9FO4xCPRZGEzeJG5jVUCUykXqQjQ0hKRMCgKtjuo1C4LL6owtjX5sS2gJGU-GDqXeJLEQaqoPJ9bCO0i3s_hnscavsM3DzrLrVqlVu91Hu4G5MX3Ys1oIZIJEtj2bx5EbyGfgRddr3_M8AO7XR5OU8%2526u%253dhttp%25253a%25252f%25252f1195.xg4ken.com%25252fmedia%25252fredir.php%25253fprof%25253d%252526camp%25253d%252526affcode%25253d%252526k_inner_url_encoded%25253d0%252526cid%25253d73461193247625%25257c%25257cairlines%252526mType%25253de%252526networkType%25253dsearch%252526kdv%25253dc%252526ksl%25253d382777%252526url%25255b%25255d%25253dhttps%25253a%25252f%25252fwww.cheaptickets.com%25252fg%25252fdd%25252ftraveldeals-top-hotel-deals%25253fsemcid%25253dcheaptickets-us.multilob.bing.gt-c-en.flight%252526kword%25253dbe.%25257cairlines%25257c.107.184806.410.24897.73461193247625.1531911971.kwd-14966926842.s%252526epic%25253d_kenshoo_clickid_%252526epi%25253d_kenshoo_clickid_%252526semdtl%25253da151868923.b11531911971.d173461193247625.e1c.f1.g1kwd-14966926842.h1e.i1.j1.k1.l1s.m1be.n1%26hash%3dA1C301ACC8E519A8C55379D661BCCB2F&ap=0&cop=main-title&om_userid=WuWG1m1lIw1lbevx1l4I&om_sessionid=GMlva6OKEexxdZ4T3hX7&om_pageid=XygfQ04Q6uehLcmXWrKW&om_nextpage=true",
				"type": "deeplink"
			}]
		},
		{
			"display_url": "www.expedia.com/Flights/Airline",
			"title": "AD2 -- Expedia - Cheap Plane Tickets - Fly At Incredible Prices.",
			"description": "Plan The Ultimate Trip. Fantastic Flight + Hotel Deals Are Waiting Just For You.",
			"url": "http://ccs.infospace.com/ClickHandler.ashx?encp=ld%3d20170830%26app%3d1%26c%3ddogpl.100%26s%3ddogpilesem%26rc%3ddogpl.300%26dc%3d%26euip%3d104.132.11.74%26pvaid%3de6a8799486614194bae5467d76ce1d31%26dt%3dDesktop%26fct.uid%3ddddaea275d7e4d759eb57b7755b44a37%26en%3d352GU4fR56WY6dtc5jlLFS1qfqwkvnZ3WLV07iuIzB20xQ26pTFYPQ%253d%253d%26coi%3d1493%26npp%3d0%26p%3d1%26pp%3d0%26mid%3d9%26ep%3d2%26ru%3dhttps%253a%252f%252f43070220.r.bat.bing.com%252f%253fld%253dd3Q3L8IR2I2xs2e6PVneNxdTVUCUw4V3cAv7E4TGBoGhwt6hvMHTSrLXBOL1twGvzSxOPW0dJ4BSdAzY5fJy0On9p6gSHxmu29Em96Tq_8HwEbxFmP3_5Z0O9ClXDHMsqfrjccaK8liPYde-YCj0B4OVooazE%2526u%253dhttp%25253a%25252f%25252f138.xg4ken.com%25252ftrk%25252fv1%25253fprof%25253d485%252526camp%25253d220303%252526affcode%25253dkw22938%252526kct%25253dmsn%252526kchid%25253d43070220%252526cid%25253d14388586985%252526queryStr%25253dairlines%252526kdv%25253dc%252526criteriaid%25253dkwd-29737302506%252526adgroupid%25253d5282898297%252526campaignid%25253d141944743%252526url%25253dhttps%25253a%25252f%25252fwww.expedia.com%25252fFlights%25253fsemcid%25253dus.multilob.bing.gt-c-en.flight%252526kword%25253dZzZz.4850000022938._kenshoo_clickid_%252526semdtl%25253da1141944743.b15282898297.d114388586985.e1c.f1.g1kwd-29737302506.h1e.i1.j1.k1.l1s.m1be.n1%252526msclkid%25253d%25257bmsclkid%25257d%252526utm_source%25253dbing%252526utm_medium%25253dcpc%252526utm_campaign%25253dUSA%2525253AENG%2525253A%252540%2525253AGT%2525253AGLOB%2525253AALL%2525253AE%2525253AX%2525253A%2525253A%252526utm_term%25253dairlines%252526utm_content%25253dUSA%2525253AENG%2525253A%252540%2525253AGT%2525253AGLOB%2525253AALL%2525253AXX%2525253AX%2525253AX%2525253AX%2525253AX%2525253AE%2525253AX%2525253Aairline%2525253A%26du%3dwww.expedia.com%252fFlights%252fAirline%26hash%3d005AD968DB08433EFB87FF4F0D014008&ap=0&cop=main-title&om_userid=WuWG1m1lIw1lbevx1l4I&om_sessionid=GMlva6OKEexxdZ4T3hX7&om_pageid=XygfQ04Q6uehLcmXWrKW&om_nextpage=true",
			"type": "ad",
			"deeplinks": [{
				"title": "Search Cheap Flights",
				"url": "http://ccs.infospace.com/ClickHandler.ashx?encp=ld%3d20170830%26app%3d1%26c%3ddogpl.100%26s%3ddogpilesem%26rc%3ddogpl.300%26dc%3d%26euip%3d104.132.11.74%26pvaid%3de6a8799486614194bae5467d76ce1d31%26dt%3dDesktop%26fct.uid%3ddddaea275d7e4d759eb57b7755b44a37%26en%3d352GU4fR56WY6dtc5jlLFS1qfqwkvnZ3WLV07iuIzB20xQ26pTFYPQ%253d%253d%26coi%3d1506%26npp%3d0%26p%3d1%26pp%3d0%26mid%3d5%26ep%3d1%26ru%3dhttps%253a%252f%252f43070220.r.bat.bing.com%252f%253fld%253dd3_6jYUIFb0alDKd55Cc99sDVUCUxAckCnpdeBhXgeQGaPpuUeDS2BEIRMqjB7KM9YJt2VuavhbLcKY5hBMgYF72v6vrTOEhkPVK7Kc9f1GZg0qjsQRw0Hy5XfsDxEd7onmVOH7uFI82cfkljkWcMOMmNdwTo%2526u%253dhttp%25253a%25252f%25252f138.xg4ken.com%25252fmedia%25252fredir.php%25253fprof%25253d%252526camp%25253d%252526affcode%25253d%252526k_inner_url_encoded%25253d0%252526cid%25253d14388586985%25257c%25257cairlines%252526mType%25253de%252526networkType%25253dsearch%252526kdv%25253dc%252526ksl%25253d5111243%252526url%25255b%25255d%25253dhttp%25253a%25252f%25252fwww.expedia.com%25252fFlights%25253fregionId%25253d%252526Sitelink%25253dCheap_Flights%252526semdtl%25253da1141944743.b15282898297.d114388586985.e1c.f1.g1kwd-29737302506.h1e.i1.j1.k1.l1s.m1be.n1%252526msclkid%25253d%25257bmsclkid%25257d%252526semcid%25253dus.multilob.bing.gt-c-en.flight%252526utm_source%25253dbing%252526utm_medium%25253dcpc%252526utm_campaign%25253dUSA%2525253AENG%2525253A%252540%2525253AGT%2525253AGLOB%2525253AALL%2525253AE%2525253AX%2525253A%2525253A%252526utm_term%25253dairlines%252526utm_content%25253dUSA%2525253AENG%2525253A%252540%2525253AGT%2525253AGLOB%2525253AALL%2525253AXX%2525253AX%2525253AX%2525253AX%2525253AX%2525253AE%2525253AX%2525253Aairline%2525253A%26hash%3dF894E10D4551306EEA3AF96FCC9DE0DC&ap=0&cop=main-title&om_userid=WuWG1m1lIw1lbevx1l4I&om_sessionid=GMlva6OKEexxdZ4T3hX7&om_pageid=XygfQ04Q6uehLcmXWrKW&om_nextpage=true",
				"type": "deeplink"
			}, {
				"title": "Direct Flights",
				"url": "http://ccs.infospace.com/ClickHandler.ashx?encp=ld%3d20170830%26app%3d1%26c%3ddogpl.100%26s%3ddogpilesem%26rc%3ddogpl.300%26dc%3d%26euip%3d104.132.11.74%26pvaid%3de6a8799486614194bae5467d76ce1d31%26dt%3dDesktop%26fct.uid%3ddddaea275d7e4d759eb57b7755b44a37%26en%3d352GU4fR56WY6dtc5jlLFS1qfqwkvnZ3WLV07iuIzB20xQ26pTFYPQ%253d%253d%26coi%3d1506%26npp%3d0%26p%3d1%26pp%3d0%26mid%3d5%26ep%3d2%26ru%3dhttps%253a%252f%252f43070220.r.bat.bing.com%252f%253fld%253dd37nU0jtK4XatVP2HBkDITMzVUCUx2Al8trmSBdvqe6wH3DXMIOn-OPr81-htj8fpDFABUfVmw6elr3k3Jm6NNrI80gJWoUOKfiN3_OVpAZ95KJVQm5egsUHNS9bfa_zT_arDXPJDGdb2Zq2iS1VKSwtwbaCA%2526u%253dhttp%25253a%25252f%25252f138.xg4ken.com%25252fmedia%25252fredir.php%25253fprof%25253d%252526camp%25253d%252526affcode%25253d%252526k_inner_url_encoded%25253d0%252526cid%25253d14388586985%25257c%25257cairlines%252526mType%25253de%252526networkType%25253dsearch%252526kdv%25253dc%252526ksl%25253d5111246%252526url%25255b%25255d%25253dhttp%25253a%25252f%25252fwww.expedia.com%25252fFlights%25253fregionId%25253d%252526Sitelink%25253dDirect_Flights%252526semdtl%25253da1141944743.b15282898297.d114388586985.e1c.f1.g1kwd-29737302506.h1e.i1.j1.k1.l1s.m1be.n1%252526msclkid%25253d%25257bmsclkid%25257d%252526semcid%25253dus.multilob.bing.gt-c-en.flight%252526utm_source%25253dbing%252526utm_medium%25253dcpc%252526utm_campaign%25253dUSA%2525253AENG%2525253A%252540%2525253AGT%2525253AGLOB%2525253AALL%2525253AE%2525253AX%2525253A%2525253A%252526utm_term%25253dairlines%252526utm_content%25253dUSA%2525253AENG%2525253A%252540%2525253AGT%2525253AGLOB%2525253AALL%2525253AXX%2525253AX%2525253AX%2525253AX%2525253AX%2525253AE%2525253AX%2525253Aairline%2525253A%26hash%3d50EAB4427BFE3D2CA8C9283586E972C7&ap=0&cop=main-title&om_userid=WuWG1m1lIw1lbevx1l4I&om_sessionid=GMlva6OKEexxdZ4T3hX7&om_pageid=XygfQ04Q6uehLcmXWrKW&om_nextpage=true",
				"type": "deeplink"
			}, {
				"title": "Cheap Hotels",
				"url": "http://ccs.infospace.com/ClickHandler.ashx?encp=ld%3d20170830%26app%3d1%26c%3ddogpl.100%26s%3ddogpilesem%26rc%3ddogpl.300%26dc%3d%26euip%3d104.132.11.74%26pvaid%3de6a8799486614194bae5467d76ce1d31%26dt%3dDesktop%26fct.uid%3ddddaea275d7e4d759eb57b7755b44a37%26en%3d352GU4fR56WY6dtc5jlLFS1qfqwkvnZ3WLV07iuIzB20xQ26pTFYPQ%253d%253d%26coi%3d1506%26npp%3d0%26p%3d1%26pp%3d0%26mid%3d5%26ep%3d3%26ru%3dhttps%253a%252f%252f43070220.r.bat.bing.com%252f%253fld%253dd3rUirrulkVoZ8HCgTvsTk8TVUCUzjJCdz0rF1hH58zvLGcBmPScw4OvNYAXHVuTzlcw605FevJuas2UJqA-Pt1aO7lyBfvopdebCdVahZkf60OVXVQrVZCby7gP2c_0HHLj5lRFZ-TMg9qwM9N-dwp9hq58c%2526u%253dhttp%25253a%25252f%25252f138.xg4ken.com%25252fmedia%25252fredir.php%25253fprof%25253d%252526camp%25253d%252526affcode%25253d%252526k_inner_url_encoded%25253d0%252526cid%25253d14388586985%25257c%25257cairlines%252526mType%25253de%252526networkType%25253dsearch%252526kdv%25253dc%252526ksl%25253d5111249%252526url%25255b%25255d%25253dhttp%25253a%25252f%25252fwww.expedia.com%25252fHotels%25253fregionId%25253d%252526Sitelink%25253dCheap_Hotels%252526semdtl%25253da1141944743.b15282898297.d114388586985.e1c.f1.g1kwd-29737302506.h1e.i1.j1.k1.l1s.m1be.n1%252526msclkid%25253d%25257bmsclkid%25257d%252526semcid%25253dus.multilob.bing.gt-c-en.flight%252526utm_source%25253dbing%252526utm_medium%25253dcpc%252526utm_campaign%25253dUSA%2525253AENG%2525253A%252540%2525253AGT%2525253AGLOB%2525253AALL%2525253AE%2525253AX%2525253A%2525253A%252526utm_term%25253dairlines%252526utm_content%25253dUSA%2525253AENG%2525253A%252540%2525253AGT%2525253AGLOB%2525253AALL%2525253AXX%2525253AX%2525253AX%2525253AX%2525253AX%2525253AE%2525253AX%2525253Aairline%2525253A%26hash%3d3E318D6BD927506204B11D8CEA2B6D66&ap=0&cop=main-title&om_userid=WuWG1m1lIw1lbevx1l4I&om_sessionid=GMlva6OKEexxdZ4T3hX7&om_pageid=XygfQ04Q6uehLcmXWrKW&om_nextpage=true",
				"type": "deeplink"
			}, {
				"title": "Book Flights + Hotel",
				"url": "http://ccs.infospace.com/ClickHandler.ashx?encp=ld%3d20170830%26app%3d1%26c%3ddogpl.100%26s%3ddogpilesem%26rc%3ddogpl.300%26dc%3d%26euip%3d104.132.11.74%26pvaid%3de6a8799486614194bae5467d76ce1d31%26dt%3dDesktop%26fct.uid%3ddddaea275d7e4d759eb57b7755b44a37%26en%3d352GU4fR56WY6dtc5jlLFS1qfqwkvnZ3WLV07iuIzB20xQ26pTFYPQ%253d%253d%26coi%3d1506%26npp%3d0%26p%3d1%26pp%3d0%26mid%3d5%26ep%3d4%26ru%3dhttps%253a%252f%252f43070220.r.bat.bing.com%252f%253fld%253dd3EbLv1LHMaoWWgeQIS4iYgDVUCUxDZcbJphmORuiWe2JMIx0JCvCkHyKSfNdzy7FTSKN-K5PDWQxwu6r5YW0OAoyYElxIFevM3QpXY44Gc2icT_u-SjBsD-wE1zW9aL39tmL_CVM42CXAMyXFLAzlWALz45E%2526u%253dhttp%25253a%25252f%25252f138.xg4ken.com%25252fmedia%25252fredir.php%25253fprof%25253d%252526camp%25253d%252526affcode%25253d%252526k_inner_url_encoded%25253d0%252526cid%25253d14388586985%25257c%25257cairlines%252526mType%25253de%252526networkType%25253dsearch%252526kdv%25253dc%252526ksl%25253d5111252%252526url%25255b%25255d%25253dhttp%25253a%25252f%25252fwww.expedia.com%25252fFlights%25253fregionId%25253d%252526Sitelink%25253dBook_Flights_Hotel%252526semdtl%25253da1141944743.b15282898297.d114388586985.e1c.f1.g1kwd-29737302506.h1e.i1.j1.k1.l1s.m1be.n1%252526msclkid%25253d%25257bmsclkid%25257d%252526semcid%25253dus.multilob.bing.gt-c-en.flight%252526utm_source%25253dbing%252526utm_medium%25253dcpc%252526utm_campaign%25253dUSA%2525253AENG%2525253A%252540%2525253AGT%2525253AGLOB%2525253AALL%2525253AE%2525253AX%2525253A%2525253A%252526utm_term%25253dairlines%252526utm_content%25253dUSA%2525253AENG%2525253A%252540%2525253AGT%2525253AGLOB%2525253AALL%2525253AXX%2525253AX%2525253AX%2525253AX%2525253AX%2525253AE%2525253AX%2525253Aairline%2525253A%26hash%3dE503DB09FE3D203769810B38037E8CD3&ap=0&cop=main-title&om_userid=WuWG1m1lIw1lbevx1l4I&om_sessionid=GMlva6OKEexxdZ4T3hX7&om_pageid=XygfQ04Q6uehLcmXWrKW&om_nextpage=true",
				"type": "deeplink"
			}]
		},
		{
			"display_url": "www.CheapOair.com/Big-Savings",
			"title": "AD3 -- Book Airline Tickets - Get Away this Summer! - CheapOair.com",
			"description": "Get Away this Summer! Buy Airline Tickets now at CheapOair&#174; &amp; Save Big.",
			"url": "http://ccs.infospace.com/ClickHandler.ashx?encp=ld%3d20170830%26app%3d1%26c%3ddogpl.100%26s%3ddogpilesem%26rc%3ddogpl.300%26dc%3d%26euip%3d104.132.11.74%26pvaid%3de6a8799486614194bae5467d76ce1d31%26dt%3dDesktop%26fct.uid%3ddddaea275d7e4d759eb57b7755b44a37%26en%3d352GU4fR56WY6dtc5jlLFS1qfqwkvnZ3WLV07iuIzB20xQ26pTFYPQ%253d%253d%26coi%3d1493%26npp%3d0%26p%3d1%26pp%3d0%26mid%3d9%26ep%3d3%26ru%3dhttps%253a%252f%252f13391.r.bat.bing.com%252f%253fld%253dd35Q9sez8PwcFBBtgwlOl1MDVUCUztPeBDoFoxHGVDqb7_xvE0Nkjd3AbN9mudsZErDXY3bMJLs3MpT9edPop2W0cr6dgkx9urI2Q5JKvfTjnweDebCyBLzADp1gm5Du0mj0pp4DLGtHSMUPEkJbSOnIDm54M%2526u%253dhttps%25253a%25252f%25252fwww.cheapoair.com%25252fflights%25252fbooknow%25252fcheap-flight-deals%25253ffpaffiliate%25253dMSN%252526fpsub%25253d9thapr_v1_84181360100972%252526utm_source%25253dmsn%252526utm_medium%25253dcpc%252526utm_campaign%25253dgeneric2%252526utm_term%25253dairlines%252526fpprice%25253d%252526utm_content%25253dv1%26du%3dwww.CheapOair.com%252fBig-Savings%26hash%3d61B63B8B9E65385766227713A4209A78&ap=0&cop=main-title&om_userid=WuWG1m1lIw1lbevx1l4I&om_sessionid=GMlva6OKEexxdZ4T3hX7&om_pageid=XygfQ04Q6uehLcmXWrKW&om_nextpage=true",
			"type": "ad",
			"deeplinks": [{
				"title": "One Way Flights",
				"url": "http://ccs.infospace.com/ClickHandler.ashx?encp=ld%3d20170830%26app%3d1%26c%3ddogpl.100%26s%3ddogpilesem%26rc%3ddogpl.300%26dc%3d%26euip%3d104.132.11.74%26pvaid%3de6a8799486614194bae5467d76ce1d31%26dt%3dDesktop%26fct.uid%3ddddaea275d7e4d759eb57b7755b44a37%26en%3d352GU4fR56WY6dtc5jlLFS1qfqwkvnZ3WLV07iuIzB20xQ26pTFYPQ%253d%253d%26coi%3d1506%26npp%3d0%26p%3d1%26pp%3d0%26mid%3d5%26ep%3d1%26ru%3dhttps%253a%252f%252f13391.r.bat.bing.com%252f%253fld%253dd3y4S0SaPqrz7LCl4KehOzCTVUCUxnn4YVsSKhaEh4IwywAkheO3kQBMbW9J7sN-rh1saBsNJyYLWLsKXklXMMjX-8doqYMowme2bYsWkoc9224UdcYVo_MxRCu6xtE6qjQNMAm1Zcbe08CMDlK18RQ-6Z1uI%2526u%253dwww.cheapoair.com%25252fflights%25252fbooknow%25252fcheap-one-way-flights%25253ffpaffiliate%25253dMSN%252526fpsub%25253dsloneway_gencamp1234%252526utm_source%25253dMSN%252526utm_medium%25253dcpc%252526utm_campaign%25253dGeneric2%252526utm_term%25253dairlines%252526utm_content%25253dv5%26hash%3d5A835FCD0853717D52DA277DB92FAF32&ap=0&cop=main-title&om_userid=WuWG1m1lIw1lbevx1l4I&om_sessionid=GMlva6OKEexxdZ4T3hX7&om_pageid=XygfQ04Q6uehLcmXWrKW&om_nextpage=true",
				"type": "deeplink"
			}, {
				"title": "Discount Flight Tickets",
				"url": "http://ccs.infospace.com/ClickHandler.ashx?encp=ld%3d20170830%26app%3d1%26c%3ddogpl.100%26s%3ddogpilesem%26rc%3ddogpl.300%26dc%3d%26euip%3d104.132.11.74%26pvaid%3de6a8799486614194bae5467d76ce1d31%26dt%3dDesktop%26fct.uid%3ddddaea275d7e4d759eb57b7755b44a37%26en%3d352GU4fR56WY6dtc5jlLFS1qfqwkvnZ3WLV07iuIzB20xQ26pTFYPQ%253d%253d%26coi%3d1506%26npp%3d0%26p%3d1%26pp%3d0%26mid%3d5%26ep%3d2%26ru%3dhttps%253a%252f%252f13391.r.bat.bing.com%252f%253fld%253dd3OAB3NpMd1h2B-iAjDrCWxjVUCUxResas1VWk3xlXpUBU9AG-E1JdvRvdJIxAkHZGyrxopqFIibkNlOD2RbmQu5MeMqenbdKlgr1mGOY0wUBhFeOtRqtCg5Ks91Eoi2nlwuqlGbgSioolSf3KXpNXqtlOHX8%2526u%253dhttps%25253a%25252f%25252fwww.cheapoair.com%25252fflights%25252fbooknow%25252fdiscounted-flight-tickets%25253ffpaffiliate%25253dMSN%252526fpsub%25253dslcamp_discfltstkt_v5_50236144%252526utm_source%25253dmsn%252526utm_medium%25253dcpc%252526utm_campaign%25253dgeneric2%252526utm_term%25253dairlines%252526utm_content%25253dv5%26hash%3d0A58DBC91AFB1C8C4D5FB27295D68DF5&ap=0&cop=main-title&om_userid=WuWG1m1lIw1lbevx1l4I&om_sessionid=GMlva6OKEexxdZ4T3hX7&om_pageid=XygfQ04Q6uehLcmXWrKW&om_nextpage=true",
				"type": "deeplink"
			}, {
				"title": "Family Travel Deals",
				"url": "http://ccs.infospace.com/ClickHandler.ashx?encp=ld%3d20170830%26app%3d1%26c%3ddogpl.100%26s%3ddogpilesem%26rc%3ddogpl.300%26dc%3d%26euip%3d104.132.11.74%26pvaid%3de6a8799486614194bae5467d76ce1d31%26dt%3dDesktop%26fct.uid%3ddddaea275d7e4d759eb57b7755b44a37%26en%3d352GU4fR56WY6dtc5jlLFS1qfqwkvnZ3WLV07iuIzB20xQ26pTFYPQ%253d%253d%26coi%3d1506%26npp%3d0%26p%3d1%26pp%3d0%26mid%3d5%26ep%3d3%26ru%3dhttps%253a%252f%252f13391.r.bat.bing.com%252f%253fld%253dd3I_PIeZfQuByMzeTvBlVynDVUCUyk-Ahec4kyAoeTodP5rxjfoOpgwzH25AuqBsEvtr9CZY9IniMydXiaFceFmvG468tSuUXVIWHA1WQp0xb388vWECsGXHeZZ9VPSaUYZIQhz7MjjXvjCuO615_-91sKIJQ%2526u%253dhttps%25253a%25252f%25252fwww.cheapoair.com%25252fflights%25252fbooknow%25252ffamily-travel%25253ffpaffiliate%25253dMSN%252526fpsub%25253dsl_1feb_familyGeneric-Generic2%252526utm_source%25253dmsn%252526utm_medium%25253dcpc%252526utm_campaign%25253dgeneric2%252526utm_term%25253dairlines%252526utm_content%25253dsl%26hash%3d62016BBD5F9EA559D3EC6D7075F833F2&ap=0&cop=main-title&om_userid=WuWG1m1lIw1lbevx1l4I&om_sessionid=GMlva6OKEexxdZ4T3hX7&om_pageid=XygfQ04Q6uehLcmXWrKW&om_nextpage=true",
				"type": "deeplink"
			}, {
				"title": "Seasonal Flight Deals",
				"url": "http://ccs.infospace.com/ClickHandler.ashx?encp=ld%3d20170830%26app%3d1%26c%3ddogpl.100%26s%3ddogpilesem%26rc%3ddogpl.300%26dc%3d%26euip%3d104.132.11.74%26pvaid%3de6a8799486614194bae5467d76ce1d31%26dt%3dDesktop%26fct.uid%3ddddaea275d7e4d759eb57b7755b44a37%26en%3d352GU4fR56WY6dtc5jlLFS1qfqwkvnZ3WLV07iuIzB20xQ26pTFYPQ%253d%253d%26coi%3d1506%26npp%3d0%26p%3d1%26pp%3d0%26mid%3d5%26ep%3d4%26ru%3dhttps%253a%252f%252f13391.r.bat.bing.com%252f%253fld%253dd3_bVbs4BIp54Pfqpkltq-JzVUCUzCSskE6EzvY9GglwWXNrxbMrLL3-T4HRuLHuAa-ituG1c_RHpY8ezF19j_tVm5yDNzCcsrkCUqguBNyu93dELwXwcVogkm0nEz1y0_Oi23sMoUZEscm4iFaS_1crEMTPE%2526u%253dhttps%25253a%25252f%25252fwww.cheapoair.com%25252fflights%25252fbooknow%25252fseasonal-travel-deals%25253ffpaffiliate%25253dMSN%252526fpsub%25253dsl_1feb_seasonalGeneric-Generic2%252526utm_source%25253dmsn%252526utm_medium%25253dcpc%252526utm_campaign%25253dgeneric2%252526utm_term%25253dairlines%252526utm_content%25253dsl%26hash%3d40C2B7393B419F1D34C991EE5747FA50&ap=0&cop=main-title&om_userid=WuWG1m1lIw1lbevx1l4I&om_sessionid=GMlva6OKEexxdZ4T3hX7&om_pageid=XygfQ04Q6uehLcmXWrKW&om_nextpage=true",
				"type": "deeplink"
			}]
		},
		{
			"display_url": "www.kayak.com",
			"title": "AD4 -- KAYAK&#174; Flight Search - Best Airline Deals in Seconds",
			"description": "Search Prices for Hundreds of <strong>Airlines</strong> Worldwide. Book the Cheapest Flights!",
			"url": "http://ccs.infospace.com/ClickHandler.ashx?encp=ld%3d20170830%26app%3d1%26c%3ddogpl.100%26s%3ddogpilesem%26rc%3ddogpl.300%26dc%3d%26euip%3d104.132.11.74%26pvaid%3de6a8799486614194bae5467d76ce1d31%26dt%3dDesktop%26fct.uid%3ddddaea275d7e4d759eb57b7755b44a37%26en%3d352GU4fR56WY6dtc5jlLFS1qfqwkvnZ3WLV07iuIzB20xQ26pTFYPQ%253d%253d%26coi%3d1493%26npp%3d0%26p%3d1%26pp%3d0%26mid%3d9%26ep%3d4%26ru%3dhttps%253a%252f%252f0.r.bat.bing.com%252f%253fld%253dd3bVf0SCbzfCFtihyc_dTAzzVUCUyFShnhPeDKVyejfncbFrww0AA0pEOohXaN4XEf1tnD--DdocmJ7c5mvkQnzfdz40TP9ekcXAvEUHx6BVnSbOEky7hJQPw_3Ko6pxIfQH-N6r45hL_TXZK7dZ2dPE2cH_M%2526u%253dhttps%25253a%25252f%25252fad.atdmt.com%25252fs%25252fgo%25253badv%25253d11097200781192%25253bec%25253d11097201123879%25253bc.a%25253d31260147%25253bs.a%25253dbing%25253bp.a%25253d31260147%25253bas.a%25253d2954429944%25253bc.n%25253dAir%25252520General%25252520Airlines%25252520-%25252520Exact%25253bp.n%25253dAir%25252520General%25252520Airlines%25252520-%25252520Exact%25253bas.n%25253dAirlines%25253bqpb%25253d1%25253b%25253fbidkw%25253dairlines%252526dvc%25253dc%252526h%25253dhttp%2525253A%2525252F%2525252Fwww.kayak.com%2525252Fsemi%2525252Fbingadssearch%2525252Fflight_general%2525252Fany%2525252Fen.html%2525253Fmt%25253de%252526bmt%25253dbe%252526qs%25253dairlines%252526oiid%25253d30645824917%252526cmpid%25253d31260147%252526aid%25253d2954429944%252526adid%25253d78202765370810%252526tid%25253dkwd-30645824917%252526d%25253dc%252526n%25253ds%252526utm_source%25253dbing%252526utm_medium%25253dcpc%252526utm_campaign%25253dAir%25252520General%25252520Airlines%25252520-%25252520Exact%252526utm_term%25253dairlines%252526utm_content%25253dAirlines%26du%3dwww.kayak.com%26hash%3d9259D161B18DA6EADF0985F504B9E1AD&ap=0&cop=main-title&om_userid=WuWG1m1lIw1lbevx1l4I&om_sessionid=GMlva6OKEexxdZ4T3hX7&om_pageid=XygfQ04Q6uehLcmXWrKW&om_nextpage=true",

			"type": "ad",
			"sources": [{
				"name": "Ads by bing",
				"position": 4,
				"provider": "BingAds"
			}],
			"deeplinks": [{
				"title": "Flights to New York",
				"url": "http://ccs.infospace.com/ClickHandler.ashx?encp=ld%3d20170830%26app%3d1%26c%3ddogpl.100%26s%3ddogpilesem%26rc%3ddogpl.300%26dc%3d%26euip%3d104.132.11.74%26pvaid%3de6a8799486614194bae5467d76ce1d31%26dt%3dDesktop%26fct.uid%3ddddaea275d7e4d759eb57b7755b44a37%26en%3d352GU4fR56WY6dtc5jlLFS1qfqwkvnZ3WLV07iuIzB20xQ26pTFYPQ%253d%253d%26coi%3d1506%26npp%3d0%26p%3d1%26pp%3d0%26mid%3d5%26ep%3d1%26ru%3dhttps%253a%252f%252f0.r.bat.bing.com%252f%253fld%253dd380_yq98CcmNbfmmuxvaseDVUCUxaLFxWQz0Stf4fbQKlFWqac1eUQP7VeH-Tw7CNtTLukfUkBc6QBBgAQpHkIKRpJWh_PtkoaexfWxZFmmd5ZaOVjBef1wvrpdfBcTN_QR-irhH1vC6u50GxwJYjKPHW6ns%2526u%253dwww.KAYAK.com%25252fsemi%25252fbingadssearch%25252fflight_airport_city%25252fNYC%25252fen.html%25253futm_source%25253dbing%252526utm_medium%25253dcpc%252526utm_campaign%25253dAir%25252520General%25252520Airlines%25252520-%25252520Exact%252526utm_term%25253dairlines%252526utm_content%25253dAirlines%26hash%3dF796D781FABB7F9BE459EAE83AF025A2&ap=0&cop=main-title&om_userid=WuWG1m1lIw1lbevx1l4I&om_sessionid=GMlva6OKEexxdZ4T3hX7&om_pageid=XygfQ04Q6uehLcmXWrKW&om_nextpage=true",
				"type": "deeplink",
				"sources": [{
					"name": "Ads by bing",
					"position": 1,
					"provider": "BingAds"
				}]
			}, {
				"title": "Flights to Las Vegas",
				"url": "http://ccs.infospace.com/ClickHandler.ashx?encp=ld%3d20170830%26app%3d1%26c%3ddogpl.100%26s%3ddogpilesem%26rc%3ddogpl.300%26dc%3d%26euip%3d104.132.11.74%26pvaid%3de6a8799486614194bae5467d76ce1d31%26dt%3dDesktop%26fct.uid%3ddddaea275d7e4d759eb57b7755b44a37%26en%3d352GU4fR56WY6dtc5jlLFS1qfqwkvnZ3WLV07iuIzB20xQ26pTFYPQ%253d%253d%26coi%3d1506%26npp%3d0%26p%3d1%26pp%3d0%26mid%3d5%26ep%3d2%26ru%3dhttps%253a%252f%252f0.r.bat.bing.com%252f%253fld%253dd3RJIJKWcDixy2AZ84vbpCZjVUCUxIZyBlkcPtpKzwkmjo5zawGXqNcltREqYYu-vYJ1A8BZqNvI4mqMrd9T8ZjBMjAHcXKf40GiPEi_oQDMWhVHZ_6yP7q2MdGYqEL3WO6oyIStf0HIhbOEJTb8sJxlp9W_w%2526u%253dwww.KAYAK.com%25252fsemi%25252fbingadssearch%25252fflight_airport_city%25252fLAS%25252fen.html%25253futm_source%25253dbing%252526utm_medium%25253dcpc%252526utm_campaign%25253dAir%25252520General%25252520Airlines%25252520-%25252520Exact%252526utm_term%25253dairlines%252526utm_content%25253dAirlines%26hash%3d5653F203D82ADCE8CFD7E9550839C19D&ap=0&cop=main-title&om_userid=WuWG1m1lIw1lbevx1l4I&om_sessionid=GMlva6OKEexxdZ4T3hX7&om_pageid=XygfQ04Q6uehLcmXWrKW&om_nextpage=true",
				"type": "deeplink",
				"sources": [{
					"name": "Ads by bing",
					"position": 2,
					"provider": "BingAds"
				}]
			}, {
				"title": "KAYAK Hotel Search",
				"url": "http://ccs.infospace.com/ClickHandler.ashx?encp=ld%3d20170830%26app%3d1%26c%3ddogpl.100%26s%3ddogpilesem%26rc%3ddogpl.300%26dc%3d%26euip%3d104.132.11.74%26pvaid%3de6a8799486614194bae5467d76ce1d31%26dt%3dDesktop%26fct.uid%3ddddaea275d7e4d759eb57b7755b44a37%26en%3d352GU4fR56WY6dtc5jlLFS1qfqwkvnZ3WLV07iuIzB20xQ26pTFYPQ%253d%253d%26coi%3d1506%26npp%3d0%26p%3d1%26pp%3d0%26mid%3d5%26ep%3d3%26ru%3dhttps%253a%252f%252f0.r.bat.bing.com%252f%253fld%253dd3AedS9jwHEVN9Mppq2qcqITVUCUw_VOKOXjOdqoOUqYy8gNBrgturC5jboQ0kTIdPr3mvtKRCkbrir7eIUgouFg6Zj-_rb65vGkNyHsjbbEM7uiC5zqBgtbaTFzf-oWVBIlT-2siuMs5zZt3iyXiG2EdcI6s%2526u%253dwww.KAYAK.com%25252fsemi%25252fbingadssearch%25252fhotel_general%25252fany%25252fen.html%25253futm_source%25253dbing%252526utm_medium%25253dcpc%252526utm_campaign%25253dAir%25252520General%25252520Airlines%25252520-%25252520Exact%252526utm_term%25253dairlines%252526utm_content%25253dAirlines%26hash%3d4F0E6D114996E5DB2E1684CE1F28DF23&ap=0&cop=main-title&om_userid=WuWG1m1lIw1lbevx1l4I&om_sessionid=GMlva6OKEexxdZ4T3hX7&om_pageid=XygfQ04Q6uehLcmXWrKW&om_nextpage=true",
				"type": "deeplink",
				"sources": [{
					"name": "Ads by bing",
					"position": 3,
					"provider": "BingAds"
				}]
			}, {
				"title": "Last Minute Flights",
				"url": "http://ccs.infospace.com/ClickHandler.ashx?encp=ld%3d20170830%26app%3d1%26c%3ddogpl.100%26s%3ddogpilesem%26rc%3ddogpl.300%26dc%3d%26euip%3d104.132.11.74%26pvaid%3de6a8799486614194bae5467d76ce1d31%26dt%3dDesktop%26fct.uid%3ddddaea275d7e4d759eb57b7755b44a37%26en%3d352GU4fR56WY6dtc5jlLFS1qfqwkvnZ3WLV07iuIzB20xQ26pTFYPQ%253d%253d%26coi%3d1506%26npp%3d0%26p%3d1%26pp%3d0%26mid%3d5%26ep%3d4%26ru%3dhttps%253a%252f%252f0.r.bat.bing.com%252f%253fld%253dd3rvpthOz4pDI0N7d4k0RcAzVUCUxfTAQD8x30hz_uGNRN6U6a4v8edrPxAGA2RKwPREXWUPrAIuXDxUmhfp-FZ3YYnxHHWk--07Xyma5idYsNR9QHYZO0m9s7F8fhTeUwFTRFo5oWrBqBKqfFMzLRp0gwggM%2526u%253dwww.KAYAK.com%25252fsemi%25252fbingadssearch%25252fflight_general%25252fany%25252fen.html%25253futm_source%25253dbing%252526utm_medium%25253dcpc%252526utm_campaign%25253dAir%25252520General%25252520Airlines%25252520-%25252520Exact%252526utm_term%25253dairlines%252526utm_content%25253dAirlines%26hash%3d3392E24058A73C9AC96727D79919BAB1&ap=0&cop=main-title&om_userid=WuWG1m1lIw1lbevx1l4I&om_sessionid=GMlva6OKEexxdZ4T3hX7&om_pageid=XygfQ04Q6uehLcmXWrKW&om_nextpage=true",
				"type": "deeplink",
				"sources": [{
					"name": "Ads by bing",
					"position": 4,
					"provider": "BingAds"
				}]
			}, {
				"title": "KAYAK Car Rental Search",
				"url": "http://ccs.infospace.com/ClickHandler.ashx?encp=ld%3d20170830%26app%3d1%26c%3ddogpl.100%26s%3ddogpilesem%26rc%3ddogpl.300%26dc%3d%26euip%3d104.132.11.74%26pvaid%3de6a8799486614194bae5467d76ce1d31%26dt%3dDesktop%26fct.uid%3ddddaea275d7e4d759eb57b7755b44a37%26en%3d352GU4fR56WY6dtc5jlLFS1qfqwkvnZ3WLV07iuIzB20xQ26pTFYPQ%253d%253d%26coi%3d1506%26npp%3d0%26p%3d1%26pp%3d0%26mid%3d5%26ep%3d5%26ru%3dhttps%253a%252f%252f0.r.bat.bing.com%252f%253fld%253dd3Z1uTHo86MKweBgqXGzo2XzVUCUxYGPSI-wlQr2qhtoUhgpGdOO2RifdhTn9KJOk-U8dxKdavo2xQNFFFHGqbIWyCIglFEWZ9vcfiMahqbRojKniYaxH88wr5DDtgh7lRClW2ARU33ne3K1kRa7EWJ0hpc34%2526u%253dwww.KAYAK.com%25252fsemi%25252fbingadssearch%25252fcar_general%25252fany%25252fen.html%25253futm_source%25253dbing%252526utm_medium%25253dcpc%252526utm_campaign%25253dAir%25252520General%25252520Airlines%25252520-%25252520Exact%252526utm_term%25253dairlines%252526utm_content%25253dAirlines%26hash%3dCC74B438FA94371E0C9493E4DA81398E&ap=0&cop=main-title&om_userid=WuWG1m1lIw1lbevx1l4I&om_sessionid=GMlva6OKEexxdZ4T3hX7&om_pageid=XygfQ04Q6uehLcmXWrKW&om_nextpage=true",
				"type": "deeplink",
				"sources": [{
					"name": "Ads by bing",
					"position": 5,
					"provider": "BingAds"
				}]
			}, {
				"title": "Vacation Packages",
				"url": "http://ccs.infospace.com/ClickHandler.ashx?encp=ld%3d20170830%26app%3d1%26c%3ddogpl.100%26s%3ddogpilesem%26rc%3ddogpl.300%26dc%3d%26euip%3d104.132.11.74%26pvaid%3de6a8799486614194bae5467d76ce1d31%26dt%3dDesktop%26fct.uid%3ddddaea275d7e4d759eb57b7755b44a37%26en%3d352GU4fR56WY6dtc5jlLFS1qfqwkvnZ3WLV07iuIzB20xQ26pTFYPQ%253d%253d%26coi%3d1506%26npp%3d0%26p%3d1%26pp%3d0%26mid%3d5%26ep%3d6%26ru%3dhttps%253a%252f%252f0.r.bat.bing.com%252f%253fld%253dd3e69gRwOAa_glKrEi5DmT4zVUCUxp6cE2exb1oc8rM8HYV1Gr_IELT2ExeuxPh9iYXb-yIBHtqIDfTTNwnfWsGMAUXjyiyB1wfjyydkDGYF4EUprmL9VbUFp033T37v8qy03U4QF9uq4U_R4tZBACXXUGhEE%2526u%253dwww.KAYAK.com%25252fsemi%25252fbingadssearch%25252fkpack_general%25252fany%25252fen.html%25253futm_source%25253dbing%252526utm_medium%25253dcpc%252526utm_campaign%25253dAir%25252520General%25252520Airlines%25252520-%25252520Exact%252526utm_term%25253dairlines%252526utm_content%25253dAirlines%26hash%3d8BF07DC8163F95FAE9D53C6ED7CBA8BC&ap=0&cop=main-title&om_userid=WuWG1m1lIw1lbevx1l4I&om_sessionid=GMlva6OKEexxdZ4T3hX7&om_pageid=XygfQ04Q6uehLcmXWrKW&om_nextpage=true",
				"type": "deeplink",
				"sources": [{
					"name": "Ads by bing",
					"position": 6,
					"provider": "BingAds"
				}]
			}],
			"enhanced_data": [{
				"name": "ContentSourceAdSource",
				"value": "Mainline",
				"type": "dataInfo"
			}]
		}
	],
	"bottom": [{
			"display_url": "www.cheaptickets.com/Flights",
			"title": "AD1 -- <strong>Airlines</strong> - Lowest Price Guaranteed | cheaptickets.com",
			"description": "Find your best deal from 450+ <strong>Airlines</strong>. Book a Flight &amp; Hotel to save more!",
			"url": "http://ccs.infospace.com/ClickHandler.ashx?encp=ld%3d20170830%26app%3d1%26c%3ddogpl.100%26s%3ddogpilesem%26rc%3ddogpl.300%26dc%3d%26euip%3d104.132.11.74%26pvaid%3de6a8799486614194bae5467d76ce1d31%26dt%3dDesktop%26fct.uid%3ddddaea275d7e4d759eb57b7755b44a37%26en%3d352GU4fR56WY6dtc5jlLFS1qfqwkvnZ3WLV07iuIzB20xQ26pTFYPQ%253d%253d%26coi%3d1493%26npp%3d0%26p%3d1%26pp%3d0%26mid%3d9%26ep%3d1%26ru%3dhttps%253a%252f%252f2359788.r.bat.bing.com%252f%253fld%253dd3Ci_8HPI2MMo8ULpA9OyXljVUCUyoVOtlwpvTwIwlHHMhHkOBtZoZBvouZOJlR7aD7PJTvXXK_POQHZM1l3omlhVsP1rzbiBlgww0patz5txLGho28o7-gRO3ymGYmLq58W3Tf7O2Ez3SB3natxl-dd0csaI%2526u%253dhttp%25253a%25252f%25252f1195.xg4ken.com%25252ftrk%25252fv1%25253fprof%25253d107%252526camp%25253d184806%252526affcode%25253dkw24897%252526kct%25253dmsn%252526kchid%25253d2359788%252526cid%25253d73461193247625%252526queryStr%25253dairlines%252526kdv%25253dc%252526criteriaid%25253dkwd-14966926842%252526adgroupid%25253d1531911971%252526campaignid%25253d51868923%252526url%25253dhttps%25253a%25252f%25252fwww.cheaptickets.com%25252fFlights%25253fsemcid%25253dcheaptickets-us.multilob.bing.gt-c-en.flight%252526kword%25253dbe.%25257cairlines%25257c.107.184806.410.24897.73461193247625.1531911971.kwd-14966926842.s%252526semdtl%25253da151868923.b11531911971.d173461193247625.e1c.f1.g1kwd-14966926842.h1e.i1.j1.k1.l1s.m1be.n1%252526epi%25253d_kenshoo_clickid_%26du%3dwww.cheaptickets.com%252fFlights%26hash%3dF29D167EBAA87DAB8D6ED835B893AACB&ap=0&cop=main-title&om_userid=WuWG1m1lIw1lbevx1l4I&om_sessionid=GMlva6OKEexxdZ4T3hX7&om_pageid=XygfQ04Q6uehLcmXWrKW&om_nextpage=true",
			"type": "ad",
			"deeplinks": [{
				"title": "Deals on 325,000 Hotels",
				"url": "http://ccs.infospace.com/ClickHandler.ashx?encp=ld%3d20170830%26app%3d1%26c%3ddogpl.100%26s%3ddogpilesem%26rc%3ddogpl.300%26dc%3d%26euip%3d104.132.11.74%26pvaid%3de6a8799486614194bae5467d76ce1d31%26dt%3dDesktop%26fct.uid%3ddddaea275d7e4d759eb57b7755b44a37%26en%3d352GU4fR56WY6dtc5jlLFS1qfqwkvnZ3WLV07iuIzB20xQ26pTFYPQ%253d%253d%26coi%3d1506%26npp%3d0%26p%3d1%26pp%3d0%26mid%3d5%26ep%3d1%26ru%3dhttps%253a%252f%252f2359788.r.bat.bing.com%252f%253fld%253dd3E9u_D_kuh0mWFYUStglnXzVUCUyMH4-llq8ORBycY5nkZAqU4vC-cGlfBx4hBoEqCaCduwEYl_p9Ts9JTKpB96cKvZQ6KL-8dNoTRggbWCshguhs2KfiTJBj8XrpORzZvxjaIzkyZMedsm7YY--fksqKuT0%2526u%253dhttp%25253a%25252f%25252f1195.xg4ken.com%25252fmedia%25252fredir.php%25253fprof%25253d%252526camp%25253d%252526affcode%25253d%252526k_inner_url_encoded%25253d0%252526cid%25253d73461193247625%25257c%25257cairlines%252526mType%25253de%252526networkType%25253dsearch%252526kdv%25253dc%252526ksl%25253d382772%252526url%25255b%25255d%25253dhttps%25253a%25252f%25252fwww.cheaptickets.com%25252fg%25252fun%25252fdeals%25253fsemcid%25253dcheaptickets-us.multilob.bing.gt-c-en.flight%252526kword%25253dbe.%25257cairlines%25257c.107.184806.410.24897.73461193247625.1531911971.kwd-14966926842.s%252526epic%25253d_kenshoo_clickid_%252526epi%25253d_kenshoo_clickid_%252526semdtl%25253da151868923.b11531911971.d173461193247625.e1c.f1.g1kwd-14966926842.h1e.i1.j1.k1.l1s.m1be.n1%26hash%3d5AD34DD20F61683C49B7F64F541E17A3&ap=0&cop=main-title&om_userid=WuWG1m1lIw1lbevx1l4I&om_sessionid=GMlva6OKEexxdZ4T3hX7&om_pageid=XygfQ04Q6uehLcmXWrKW&om_nextpage=true",
				"type": "deeplink"
			}, {
				"title": "Flights Under $199",
				"url": "http://ccs.infospace.com/ClickHandler.ashx?encp=ld%3d20170830%26app%3d1%26c%3ddogpl.100%26s%3ddogpilesem%26rc%3ddogpl.300%26dc%3d%26euip%3d104.132.11.74%26pvaid%3de6a8799486614194bae5467d76ce1d31%26dt%3dDesktop%26fct.uid%3ddddaea275d7e4d759eb57b7755b44a37%26en%3d352GU4fR56WY6dtc5jlLFS1qfqwkvnZ3WLV07iuIzB20xQ26pTFYPQ%253d%253d%26coi%3d1506%26npp%3d0%26p%3d1%26pp%3d0%26mid%3d5%26ep%3d2%26ru%3dhttps%253a%252f%252f2359788.r.bat.bing.com%252f%253fld%253dd3dXlk72wkdDe-kCUowHt8mTVUCUyXQb49ma1CWIE3BrWHLSwVCFmxQPO7NH7S6jbITJWTySR2Z0761Ehzqq7eKhf51f_G09nR9Ibkl2J4F_C6p2k2f7CuDMTzIhkzdeZO5bEBaf5jmjcYJFV2zEfKwsvuXPE%2526u%253dhttp%25253a%25252f%25252f1195.xg4ken.com%25252fmedia%25252fredir.php%25253fprof%25253d%252526camp%25253d%252526affcode%25253d%252526k_inner_url_encoded%25253d0%252526cid%25253d73461193247625%25257c%25257cairlines%252526mType%25253de%252526networkType%25253dsearch%252526kdv%25253dc%252526ksl%25253d382773%252526url%25255b%25255d%25253dhttps%25253a%25252f%25252fwww.cheaptickets.com%25252fg%25252fdd%25252fflightdeals-under199%25253fsemcid%25253dcheaptickets-us.multilob.bing.gt-c-en.flight%252526kword%25253dbe.%25257cairlines%25257c.107.184806.410.24897.73461193247625.1531911971.kwd-14966926842.s%252526epic%25253d_kenshoo_clickid_%252526epi%25253d_kenshoo_clickid_%252526semdtl%25253da151868923.b11531911971.d173461193247625.e1c.f1.g1kwd-14966926842.h1e.i1.j1.k1.l1s.m1be.n1%26hash%3dBAE69F9FBB1314BEDC3531D58FD23B70&ap=0&cop=main-title&om_userid=WuWG1m1lIw1lbevx1l4I&om_sessionid=GMlva6OKEexxdZ4T3hX7&om_pageid=XygfQ04Q6uehLcmXWrKW&om_nextpage=true",
				"type": "deeplink"
			}, {
				"title": "Secret Bargain Deals",
				"url": "http://ccs.infospace.com/ClickHandler.ashx?encp=ld%3d20170830%26app%3d1%26c%3ddogpl.100%26s%3ddogpilesem%26rc%3ddogpl.300%26dc%3d%26euip%3d104.132.11.74%26pvaid%3de6a8799486614194bae5467d76ce1d31%26dt%3dDesktop%26fct.uid%3ddddaea275d7e4d759eb57b7755b44a37%26en%3d352GU4fR56WY6dtc5jlLFS1qfqwkvnZ3WLV07iuIzB20xQ26pTFYPQ%253d%253d%26coi%3d1506%26npp%3d0%26p%3d1%26pp%3d0%26mid%3d5%26ep%3d3%26ru%3dhttps%253a%252f%252f2359788.r.bat.bing.com%252f%253fld%253dd3SDfyNlKpGq-JRxqkk4QIIzVUCUzKV3nB1_ns6rin3v278QcuP6h6mEJ8l_0DHvlcmzyb7k5UBykIpIw0IUDvE2ZWY1l4WAlVk9bUKKucR7eli6QhG0oI6Z7GlIq0XJE4ePEpFEQuMWrFTOCyMC793o93MBo%2526u%253dhttp%25253a%25252f%25252f1195.xg4ken.com%25252fmedia%25252fredir.php%25253fprof%25253d%252526camp%25253d%252526affcode%25253d%252526k_inner_url_encoded%25253d0%252526cid%25253d73461193247625%25257c%25257cairlines%252526mType%25253de%252526networkType%25253dsearch%252526kdv%25253dc%252526ksl%25253d382774%252526url%25255b%25255d%25253dhttps%25253a%25252f%25252fwww.cheaptickets.com%25252fg%25252fmb%25252ftraveldeals-secret-bargains%25253fsemcid%25253dcheaptickets-us.multilob.bing.gt-c-en.flight%252526kword%25253dbe.%25257cairlines%25257c.107.184806.410.24897.73461193247625.1531911971.kwd-14966926842.s%252526epic%25253d_kenshoo_clickid_%252526epi%25253d_kenshoo_clickid_%252526semdtl%25253da151868923.b11531911971.d173461193247625.e1c.f1.g1kwd-14966926842.h1e.i1.j1.k1.l1s.m1be.n1%26hash%3d6DDD9D30F85EE7FD63BB2E66BBF3751B&ap=0&cop=main-title&om_userid=WuWG1m1lIw1lbevx1l4I&om_sessionid=GMlva6OKEexxdZ4T3hX7&om_pageid=XygfQ04Q6uehLcmXWrKW&om_nextpage=true",
				"type": "deeplink"
			}, {
				"title": "Up to 50% off Hotels",
				"url": "http://ccs.infospace.com/ClickHandler.ashx?encp=ld%3d20170830%26app%3d1%26c%3ddogpl.100%26s%3ddogpilesem%26rc%3ddogpl.300%26dc%3d%26euip%3d104.132.11.74%26pvaid%3de6a8799486614194bae5467d76ce1d31%26dt%3dDesktop%26fct.uid%3ddddaea275d7e4d759eb57b7755b44a37%26en%3d352GU4fR56WY6dtc5jlLFS1qfqwkvnZ3WLV07iuIzB20xQ26pTFYPQ%253d%253d%26coi%3d1506%26npp%3d0%26p%3d1%26pp%3d0%26mid%3d5%26ep%3d4%26ru%3dhttps%253a%252f%252f2359788.r.bat.bing.com%252f%253fld%253dd3JmZDnB4Z-sSFy9_M_Ki82jVUCUwPcKDcU_FBLZd7a0JYTSe7CDOTOsNC0DVVAIvaeFT7FKr_KoQ8d_MyTyXohYSiyf5Z-4ZTfQFJzhJBbiCcoaQOxZKl_4jmTaQ9V4YromhB0dWRS2NukR7Qb3xB-y1NLV4%2526u%253dhttp%25253a%25252f%25252f1195.xg4ken.com%25252fmedia%25252fredir.php%25253fprof%25253d%252526camp%25253d%252526affcode%25253d%252526k_inner_url_encoded%25253d0%252526cid%25253d73461193247625%25257c%25257cairlines%252526mType%25253de%252526networkType%25253dsearch%252526kdv%25253dc%252526ksl%25253d382775%252526url%25255b%25255d%25253dhttps%25253a%25252f%25252fwww.cheaptickets.com%25252fg%25252flc%25252ftraveldeals-major-hotel-sale%25253fsemcid%25253dcheaptickets-us.multilob.bing.gt-c-en.flight%252526kword%25253dbe.%25257cairlines%25257c.107.184806.410.24897.73461193247625.1531911971.kwd-14966926842.s%252526epic%25253d_kenshoo_clickid_%252526epi%25253d_kenshoo_clickid_%252526semdtl%25253da151868923.b11531911971.d173461193247625.e1c.f1.g1kwd-14966926842.h1e.i1.j1.k1.l1s.m1be.n1%26hash%3d37B67A0189CFBA566A5BC460ABA49575&ap=0&cop=main-title&om_userid=WuWG1m1lIw1lbevx1l4I&om_sessionid=GMlva6OKEexxdZ4T3hX7&om_pageid=XygfQ04Q6uehLcmXWrKW&om_nextpage=true",
				"type": "deeplink"
			}, {
				"title": "Save Extra 16% On Hotels",
				"url": "http://ccs.infospace.com/ClickHandler.ashx?encp=ld%3d20170830%26app%3d1%26c%3ddogpl.100%26s%3ddogpilesem%26rc%3ddogpl.300%26dc%3d%26euip%3d104.132.11.74%26pvaid%3de6a8799486614194bae5467d76ce1d31%26dt%3dDesktop%26fct.uid%3ddddaea275d7e4d759eb57b7755b44a37%26en%3d352GU4fR56WY6dtc5jlLFS1qfqwkvnZ3WLV07iuIzB20xQ26pTFYPQ%253d%253d%26coi%3d1506%26npp%3d0%26p%3d1%26pp%3d0%26mid%3d5%26ep%3d5%26ru%3dhttps%253a%252f%252f2359788.r.bat.bing.com%252f%253fld%253dd3tB5RgIrnsuRAcZR4adoKPjVUCUzC5gba-AksX-ZG11Yp6hN6oIwYI2k1H6eaK_09_dW1gx0mjby7Y6iZPbaa66Q-Zg8CEquRMWeqkzu-sYO9CvsXfxflWtqqZBqSuTCUo3notCen4gV49BEZ1eXV77dMspM%2526u%253dhttp%25253a%25252f%25252f1195.xg4ken.com%25252fmedia%25252fredir.php%25253fprof%25253d%252526camp%25253d%252526affcode%25253d%252526k_inner_url_encoded%25253d0%252526cid%25253d73461193247625%25257c%25257cairlines%252526mType%25253de%252526networkType%25253dsearch%252526kdv%25253dc%252526ksl%25253d382776%252526url%25255b%25255d%25253dhttps%25253a%25252f%25252fwww.cheaptickets.com%25252fg%25252flc%25252ftraveldeals-cheapoftheweek%25253fsemcid%25253dcheaptickets-us.multilob.bing.gt-c-en.flight%252526kword%25253dbe.%25257cairlines%25257c.107.184806.410.24897.73461193247625.1531911971.kwd-14966926842.s%252526epic%25253d_kenshoo_clickid_%252526epi%25253d_kenshoo_clickid_%252526semdtl%25253da151868923.b11531911971.d173461193247625.e1c.f1.g1kwd-14966926842.h1e.i1.j1.k1.l1s.m1be.n1%26hash%3d8DD9CD0750AD8A4C1AF824B003BCE0AA&ap=0&cop=main-title&om_userid=WuWG1m1lIw1lbevx1l4I&om_sessionid=GMlva6OKEexxdZ4T3hX7&om_pageid=XygfQ04Q6uehLcmXWrKW&om_nextpage=true",
				"type": "deeplink"
			}, {
				"title": "Hotels Under $50",
				"url": "http://ccs.infospace.com/ClickHandler.ashx?encp=ld%3d20170830%26app%3d1%26c%3ddogpl.100%26s%3ddogpilesem%26rc%3ddogpl.300%26dc%3d%26euip%3d104.132.11.74%26pvaid%3de6a8799486614194bae5467d76ce1d31%26dt%3dDesktop%26fct.uid%3ddddaea275d7e4d759eb57b7755b44a37%26en%3d352GU4fR56WY6dtc5jlLFS1qfqwkvnZ3WLV07iuIzB20xQ26pTFYPQ%253d%253d%26coi%3d1506%26npp%3d0%26p%3d1%26pp%3d0%26mid%3d5%26ep%3d6%26ru%3dhttps%253a%252f%252f2359788.r.bat.bing.com%252f%253fld%253dd3Tv4BT9FO4xCPRZGEzeJG5jVUCUykXqQjQ0hKRMCgKtjuo1C4LL6owtjX5sS2gJGU-GDqXeJLEQaqoPJ9bCO0i3s_hnscavsM3DzrLrVqlVu91Hu4G5MX3Ys1oIZIJEtj2bx5EbyGfgRddr3_M8AO7XR5OU8%2526u%253dhttp%25253a%25252f%25252f1195.xg4ken.com%25252fmedia%25252fredir.php%25253fprof%25253d%252526camp%25253d%252526affcode%25253d%252526k_inner_url_encoded%25253d0%252526cid%25253d73461193247625%25257c%25257cairlines%252526mType%25253de%252526networkType%25253dsearch%252526kdv%25253dc%252526ksl%25253d382777%252526url%25255b%25255d%25253dhttps%25253a%25252f%25252fwww.cheaptickets.com%25252fg%25252fdd%25252ftraveldeals-top-hotel-deals%25253fsemcid%25253dcheaptickets-us.multilob.bing.gt-c-en.flight%252526kword%25253dbe.%25257cairlines%25257c.107.184806.410.24897.73461193247625.1531911971.kwd-14966926842.s%252526epic%25253d_kenshoo_clickid_%252526epi%25253d_kenshoo_clickid_%252526semdtl%25253da151868923.b11531911971.d173461193247625.e1c.f1.g1kwd-14966926842.h1e.i1.j1.k1.l1s.m1be.n1%26hash%3dA1C301ACC8E519A8C55379D661BCCB2F&ap=0&cop=main-title&om_userid=WuWG1m1lIw1lbevx1l4I&om_sessionid=GMlva6OKEexxdZ4T3hX7&om_pageid=XygfQ04Q6uehLcmXWrKW&om_nextpage=true",
				"type": "deeplink"
			}]
		},
		{
			"display_url": "www.expedia.com/Flights/Airline",
			"title": "AD2 -- Expedia - Cheap Plane Tickets - Fly At Incredible Prices.",
			"description": "Plan The Ultimate Trip. Fantastic Flight + Hotel Deals Are Waiting Just For You.",
			"url": "http://ccs.infospace.com/ClickHandler.ashx?encp=ld%3d20170830%26app%3d1%26c%3ddogpl.100%26s%3ddogpilesem%26rc%3ddogpl.300%26dc%3d%26euip%3d104.132.11.74%26pvaid%3de6a8799486614194bae5467d76ce1d31%26dt%3dDesktop%26fct.uid%3ddddaea275d7e4d759eb57b7755b44a37%26en%3d352GU4fR56WY6dtc5jlLFS1qfqwkvnZ3WLV07iuIzB20xQ26pTFYPQ%253d%253d%26coi%3d1493%26npp%3d0%26p%3d1%26pp%3d0%26mid%3d9%26ep%3d2%26ru%3dhttps%253a%252f%252f43070220.r.bat.bing.com%252f%253fld%253dd3Q3L8IR2I2xs2e6PVneNxdTVUCUw4V3cAv7E4TGBoGhwt6hvMHTSrLXBOL1twGvzSxOPW0dJ4BSdAzY5fJy0On9p6gSHxmu29Em96Tq_8HwEbxFmP3_5Z0O9ClXDHMsqfrjccaK8liPYde-YCj0B4OVooazE%2526u%253dhttp%25253a%25252f%25252f138.xg4ken.com%25252ftrk%25252fv1%25253fprof%25253d485%252526camp%25253d220303%252526affcode%25253dkw22938%252526kct%25253dmsn%252526kchid%25253d43070220%252526cid%25253d14388586985%252526queryStr%25253dairlines%252526kdv%25253dc%252526criteriaid%25253dkwd-29737302506%252526adgroupid%25253d5282898297%252526campaignid%25253d141944743%252526url%25253dhttps%25253a%25252f%25252fwww.expedia.com%25252fFlights%25253fsemcid%25253dus.multilob.bing.gt-c-en.flight%252526kword%25253dZzZz.4850000022938._kenshoo_clickid_%252526semdtl%25253da1141944743.b15282898297.d114388586985.e1c.f1.g1kwd-29737302506.h1e.i1.j1.k1.l1s.m1be.n1%252526msclkid%25253d%25257bmsclkid%25257d%252526utm_source%25253dbing%252526utm_medium%25253dcpc%252526utm_campaign%25253dUSA%2525253AENG%2525253A%252540%2525253AGT%2525253AGLOB%2525253AALL%2525253AE%2525253AX%2525253A%2525253A%252526utm_term%25253dairlines%252526utm_content%25253dUSA%2525253AENG%2525253A%252540%2525253AGT%2525253AGLOB%2525253AALL%2525253AXX%2525253AX%2525253AX%2525253AX%2525253AX%2525253AE%2525253AX%2525253Aairline%2525253A%26du%3dwww.expedia.com%252fFlights%252fAirline%26hash%3d005AD968DB08433EFB87FF4F0D014008&ap=0&cop=main-title&om_userid=WuWG1m1lIw1lbevx1l4I&om_sessionid=GMlva6OKEexxdZ4T3hX7&om_pageid=XygfQ04Q6uehLcmXWrKW&om_nextpage=true",
			"type": "ad",
			"deeplinks": [{
				"title": "Search Cheap Flights",
				"url": "http://ccs.infospace.com/ClickHandler.ashx?encp=ld%3d20170830%26app%3d1%26c%3ddogpl.100%26s%3ddogpilesem%26rc%3ddogpl.300%26dc%3d%26euip%3d104.132.11.74%26pvaid%3de6a8799486614194bae5467d76ce1d31%26dt%3dDesktop%26fct.uid%3ddddaea275d7e4d759eb57b7755b44a37%26en%3d352GU4fR56WY6dtc5jlLFS1qfqwkvnZ3WLV07iuIzB20xQ26pTFYPQ%253d%253d%26coi%3d1506%26npp%3d0%26p%3d1%26pp%3d0%26mid%3d5%26ep%3d1%26ru%3dhttps%253a%252f%252f43070220.r.bat.bing.com%252f%253fld%253dd3_6jYUIFb0alDKd55Cc99sDVUCUxAckCnpdeBhXgeQGaPpuUeDS2BEIRMqjB7KM9YJt2VuavhbLcKY5hBMgYF72v6vrTOEhkPVK7Kc9f1GZg0qjsQRw0Hy5XfsDxEd7onmVOH7uFI82cfkljkWcMOMmNdwTo%2526u%253dhttp%25253a%25252f%25252f138.xg4ken.com%25252fmedia%25252fredir.php%25253fprof%25253d%252526camp%25253d%252526affcode%25253d%252526k_inner_url_encoded%25253d0%252526cid%25253d14388586985%25257c%25257cairlines%252526mType%25253de%252526networkType%25253dsearch%252526kdv%25253dc%252526ksl%25253d5111243%252526url%25255b%25255d%25253dhttp%25253a%25252f%25252fwww.expedia.com%25252fFlights%25253fregionId%25253d%252526Sitelink%25253dCheap_Flights%252526semdtl%25253da1141944743.b15282898297.d114388586985.e1c.f1.g1kwd-29737302506.h1e.i1.j1.k1.l1s.m1be.n1%252526msclkid%25253d%25257bmsclkid%25257d%252526semcid%25253dus.multilob.bing.gt-c-en.flight%252526utm_source%25253dbing%252526utm_medium%25253dcpc%252526utm_campaign%25253dUSA%2525253AENG%2525253A%252540%2525253AGT%2525253AGLOB%2525253AALL%2525253AE%2525253AX%2525253A%2525253A%252526utm_term%25253dairlines%252526utm_content%25253dUSA%2525253AENG%2525253A%252540%2525253AGT%2525253AGLOB%2525253AALL%2525253AXX%2525253AX%2525253AX%2525253AX%2525253AX%2525253AE%2525253AX%2525253Aairline%2525253A%26hash%3dF894E10D4551306EEA3AF96FCC9DE0DC&ap=0&cop=main-title&om_userid=WuWG1m1lIw1lbevx1l4I&om_sessionid=GMlva6OKEexxdZ4T3hX7&om_pageid=XygfQ04Q6uehLcmXWrKW&om_nextpage=true",
				"type": "deeplink"
			}, {
				"title": "Direct Flights",
				"url": "http://ccs.infospace.com/ClickHandler.ashx?encp=ld%3d20170830%26app%3d1%26c%3ddogpl.100%26s%3ddogpilesem%26rc%3ddogpl.300%26dc%3d%26euip%3d104.132.11.74%26pvaid%3de6a8799486614194bae5467d76ce1d31%26dt%3dDesktop%26fct.uid%3ddddaea275d7e4d759eb57b7755b44a37%26en%3d352GU4fR56WY6dtc5jlLFS1qfqwkvnZ3WLV07iuIzB20xQ26pTFYPQ%253d%253d%26coi%3d1506%26npp%3d0%26p%3d1%26pp%3d0%26mid%3d5%26ep%3d2%26ru%3dhttps%253a%252f%252f43070220.r.bat.bing.com%252f%253fld%253dd37nU0jtK4XatVP2HBkDITMzVUCUx2Al8trmSBdvqe6wH3DXMIOn-OPr81-htj8fpDFABUfVmw6elr3k3Jm6NNrI80gJWoUOKfiN3_OVpAZ95KJVQm5egsUHNS9bfa_zT_arDXPJDGdb2Zq2iS1VKSwtwbaCA%2526u%253dhttp%25253a%25252f%25252f138.xg4ken.com%25252fmedia%25252fredir.php%25253fprof%25253d%252526camp%25253d%252526affcode%25253d%252526k_inner_url_encoded%25253d0%252526cid%25253d14388586985%25257c%25257cairlines%252526mType%25253de%252526networkType%25253dsearch%252526kdv%25253dc%252526ksl%25253d5111246%252526url%25255b%25255d%25253dhttp%25253a%25252f%25252fwww.expedia.com%25252fFlights%25253fregionId%25253d%252526Sitelink%25253dDirect_Flights%252526semdtl%25253da1141944743.b15282898297.d114388586985.e1c.f1.g1kwd-29737302506.h1e.i1.j1.k1.l1s.m1be.n1%252526msclkid%25253d%25257bmsclkid%25257d%252526semcid%25253dus.multilob.bing.gt-c-en.flight%252526utm_source%25253dbing%252526utm_medium%25253dcpc%252526utm_campaign%25253dUSA%2525253AENG%2525253A%252540%2525253AGT%2525253AGLOB%2525253AALL%2525253AE%2525253AX%2525253A%2525253A%252526utm_term%25253dairlines%252526utm_content%25253dUSA%2525253AENG%2525253A%252540%2525253AGT%2525253AGLOB%2525253AALL%2525253AXX%2525253AX%2525253AX%2525253AX%2525253AX%2525253AE%2525253AX%2525253Aairline%2525253A%26hash%3d50EAB4427BFE3D2CA8C9283586E972C7&ap=0&cop=main-title&om_userid=WuWG1m1lIw1lbevx1l4I&om_sessionid=GMlva6OKEexxdZ4T3hX7&om_pageid=XygfQ04Q6uehLcmXWrKW&om_nextpage=true",
				"type": "deeplink"
			}, {
				"title": "Cheap Hotels",
				"url": "http://ccs.infospace.com/ClickHandler.ashx?encp=ld%3d20170830%26app%3d1%26c%3ddogpl.100%26s%3ddogpilesem%26rc%3ddogpl.300%26dc%3d%26euip%3d104.132.11.74%26pvaid%3de6a8799486614194bae5467d76ce1d31%26dt%3dDesktop%26fct.uid%3ddddaea275d7e4d759eb57b7755b44a37%26en%3d352GU4fR56WY6dtc5jlLFS1qfqwkvnZ3WLV07iuIzB20xQ26pTFYPQ%253d%253d%26coi%3d1506%26npp%3d0%26p%3d1%26pp%3d0%26mid%3d5%26ep%3d3%26ru%3dhttps%253a%252f%252f43070220.r.bat.bing.com%252f%253fld%253dd3rUirrulkVoZ8HCgTvsTk8TVUCUzjJCdz0rF1hH58zvLGcBmPScw4OvNYAXHVuTzlcw605FevJuas2UJqA-Pt1aO7lyBfvopdebCdVahZkf60OVXVQrVZCby7gP2c_0HHLj5lRFZ-TMg9qwM9N-dwp9hq58c%2526u%253dhttp%25253a%25252f%25252f138.xg4ken.com%25252fmedia%25252fredir.php%25253fprof%25253d%252526camp%25253d%252526affcode%25253d%252526k_inner_url_encoded%25253d0%252526cid%25253d14388586985%25257c%25257cairlines%252526mType%25253de%252526networkType%25253dsearch%252526kdv%25253dc%252526ksl%25253d5111249%252526url%25255b%25255d%25253dhttp%25253a%25252f%25252fwww.expedia.com%25252fHotels%25253fregionId%25253d%252526Sitelink%25253dCheap_Hotels%252526semdtl%25253da1141944743.b15282898297.d114388586985.e1c.f1.g1kwd-29737302506.h1e.i1.j1.k1.l1s.m1be.n1%252526msclkid%25253d%25257bmsclkid%25257d%252526semcid%25253dus.multilob.bing.gt-c-en.flight%252526utm_source%25253dbing%252526utm_medium%25253dcpc%252526utm_campaign%25253dUSA%2525253AENG%2525253A%252540%2525253AGT%2525253AGLOB%2525253AALL%2525253AE%2525253AX%2525253A%2525253A%252526utm_term%25253dairlines%252526utm_content%25253dUSA%2525253AENG%2525253A%252540%2525253AGT%2525253AGLOB%2525253AALL%2525253AXX%2525253AX%2525253AX%2525253AX%2525253AX%2525253AE%2525253AX%2525253Aairline%2525253A%26hash%3d3E318D6BD927506204B11D8CEA2B6D66&ap=0&cop=main-title&om_userid=WuWG1m1lIw1lbevx1l4I&om_sessionid=GMlva6OKEexxdZ4T3hX7&om_pageid=XygfQ04Q6uehLcmXWrKW&om_nextpage=true",
				"type": "deeplink"
			}, {
				"title": "Book Flights + Hotel",
				"url": "http://ccs.infospace.com/ClickHandler.ashx?encp=ld%3d20170830%26app%3d1%26c%3ddogpl.100%26s%3ddogpilesem%26rc%3ddogpl.300%26dc%3d%26euip%3d104.132.11.74%26pvaid%3de6a8799486614194bae5467d76ce1d31%26dt%3dDesktop%26fct.uid%3ddddaea275d7e4d759eb57b7755b44a37%26en%3d352GU4fR56WY6dtc5jlLFS1qfqwkvnZ3WLV07iuIzB20xQ26pTFYPQ%253d%253d%26coi%3d1506%26npp%3d0%26p%3d1%26pp%3d0%26mid%3d5%26ep%3d4%26ru%3dhttps%253a%252f%252f43070220.r.bat.bing.com%252f%253fld%253dd3EbLv1LHMaoWWgeQIS4iYgDVUCUxDZcbJphmORuiWe2JMIx0JCvCkHyKSfNdzy7FTSKN-K5PDWQxwu6r5YW0OAoyYElxIFevM3QpXY44Gc2icT_u-SjBsD-wE1zW9aL39tmL_CVM42CXAMyXFLAzlWALz45E%2526u%253dhttp%25253a%25252f%25252f138.xg4ken.com%25252fmedia%25252fredir.php%25253fprof%25253d%252526camp%25253d%252526affcode%25253d%252526k_inner_url_encoded%25253d0%252526cid%25253d14388586985%25257c%25257cairlines%252526mType%25253de%252526networkType%25253dsearch%252526kdv%25253dc%252526ksl%25253d5111252%252526url%25255b%25255d%25253dhttp%25253a%25252f%25252fwww.expedia.com%25252fFlights%25253fregionId%25253d%252526Sitelink%25253dBook_Flights_Hotel%252526semdtl%25253da1141944743.b15282898297.d114388586985.e1c.f1.g1kwd-29737302506.h1e.i1.j1.k1.l1s.m1be.n1%252526msclkid%25253d%25257bmsclkid%25257d%252526semcid%25253dus.multilob.bing.gt-c-en.flight%252526utm_source%25253dbing%252526utm_medium%25253dcpc%252526utm_campaign%25253dUSA%2525253AENG%2525253A%252540%2525253AGT%2525253AGLOB%2525253AALL%2525253AE%2525253AX%2525253A%2525253A%252526utm_term%25253dairlines%252526utm_content%25253dUSA%2525253AENG%2525253A%252540%2525253AGT%2525253AGLOB%2525253AALL%2525253AXX%2525253AX%2525253AX%2525253AX%2525253AX%2525253AE%2525253AX%2525253Aairline%2525253A%26hash%3dE503DB09FE3D203769810B38037E8CD3&ap=0&cop=main-title&om_userid=WuWG1m1lIw1lbevx1l4I&om_sessionid=GMlva6OKEexxdZ4T3hX7&om_pageid=XygfQ04Q6uehLcmXWrKW&om_nextpage=true",
				"type": "deeplink"
			}]
		}
	],
	"right": [{
			"display_url": "www.cheaptickets.com/Flights",
			"title": "AD1 -- <strong>Airlines</strong> - Lowest Price Guaranteed | cheaptickets.com",
			"description": "Find your best deal from 450+ <strong>Airlines</strong>. Book a Flight &amp; Hotel to save more!",
			"url": "http://ccs.infospace.com/ClickHandler.ashx?encp=ld%3d20170830%26app%3d1%26c%3ddogpl.100%26s%3ddogpilesem%26rc%3ddogpl.300%26dc%3d%26euip%3d104.132.11.74%26pvaid%3de6a8799486614194bae5467d76ce1d31%26dt%3dDesktop%26fct.uid%3ddddaea275d7e4d759eb57b7755b44a37%26en%3d352GU4fR56WY6dtc5jlLFS1qfqwkvnZ3WLV07iuIzB20xQ26pTFYPQ%253d%253d%26coi%3d1493%26npp%3d0%26p%3d1%26pp%3d0%26mid%3d9%26ep%3d1%26ru%3dhttps%253a%252f%252f2359788.r.bat.bing.com%252f%253fld%253dd3Ci_8HPI2MMo8ULpA9OyXljVUCUyoVOtlwpvTwIwlHHMhHkOBtZoZBvouZOJlR7aD7PJTvXXK_POQHZM1l3omlhVsP1rzbiBlgww0patz5txLGho28o7-gRO3ymGYmLq58W3Tf7O2Ez3SB3natxl-dd0csaI%2526u%253dhttp%25253a%25252f%25252f1195.xg4ken.com%25252ftrk%25252fv1%25253fprof%25253d107%252526camp%25253d184806%252526affcode%25253dkw24897%252526kct%25253dmsn%252526kchid%25253d2359788%252526cid%25253d73461193247625%252526queryStr%25253dairlines%252526kdv%25253dc%252526criteriaid%25253dkwd-14966926842%252526adgroupid%25253d1531911971%252526campaignid%25253d51868923%252526url%25253dhttps%25253a%25252f%25252fwww.cheaptickets.com%25252fFlights%25253fsemcid%25253dcheaptickets-us.multilob.bing.gt-c-en.flight%252526kword%25253dbe.%25257cairlines%25257c.107.184806.410.24897.73461193247625.1531911971.kwd-14966926842.s%252526semdtl%25253da151868923.b11531911971.d173461193247625.e1c.f1.g1kwd-14966926842.h1e.i1.j1.k1.l1s.m1be.n1%252526epi%25253d_kenshoo_clickid_%26du%3dwww.cheaptickets.com%252fFlights%26hash%3dF29D167EBAA87DAB8D6ED835B893AACB&ap=0&cop=main-title&om_userid=WuWG1m1lIw1lbevx1l4I&om_sessionid=GMlva6OKEexxdZ4T3hX7&om_pageid=XygfQ04Q6uehLcmXWrKW&om_nextpage=true",
			"type": "ad",
			"deeplinks": [{
				"title": "Deals on 325,000 Hotels",
				"url": "http://ccs.infospace.com/ClickHandler.ashx?encp=ld%3d20170830%26app%3d1%26c%3ddogpl.100%26s%3ddogpilesem%26rc%3ddogpl.300%26dc%3d%26euip%3d104.132.11.74%26pvaid%3de6a8799486614194bae5467d76ce1d31%26dt%3dDesktop%26fct.uid%3ddddaea275d7e4d759eb57b7755b44a37%26en%3d352GU4fR56WY6dtc5jlLFS1qfqwkvnZ3WLV07iuIzB20xQ26pTFYPQ%253d%253d%26coi%3d1506%26npp%3d0%26p%3d1%26pp%3d0%26mid%3d5%26ep%3d1%26ru%3dhttps%253a%252f%252f2359788.r.bat.bing.com%252f%253fld%253dd3E9u_D_kuh0mWFYUStglnXzVUCUyMH4-llq8ORBycY5nkZAqU4vC-cGlfBx4hBoEqCaCduwEYl_p9Ts9JTKpB96cKvZQ6KL-8dNoTRggbWCshguhs2KfiTJBj8XrpORzZvxjaIzkyZMedsm7YY--fksqKuT0%2526u%253dhttp%25253a%25252f%25252f1195.xg4ken.com%25252fmedia%25252fredir.php%25253fprof%25253d%252526camp%25253d%252526affcode%25253d%252526k_inner_url_encoded%25253d0%252526cid%25253d73461193247625%25257c%25257cairlines%252526mType%25253de%252526networkType%25253dsearch%252526kdv%25253dc%252526ksl%25253d382772%252526url%25255b%25255d%25253dhttps%25253a%25252f%25252fwww.cheaptickets.com%25252fg%25252fun%25252fdeals%25253fsemcid%25253dcheaptickets-us.multilob.bing.gt-c-en.flight%252526kword%25253dbe.%25257cairlines%25257c.107.184806.410.24897.73461193247625.1531911971.kwd-14966926842.s%252526epic%25253d_kenshoo_clickid_%252526epi%25253d_kenshoo_clickid_%252526semdtl%25253da151868923.b11531911971.d173461193247625.e1c.f1.g1kwd-14966926842.h1e.i1.j1.k1.l1s.m1be.n1%26hash%3d5AD34DD20F61683C49B7F64F541E17A3&ap=0&cop=main-title&om_userid=WuWG1m1lIw1lbevx1l4I&om_sessionid=GMlva6OKEexxdZ4T3hX7&om_pageid=XygfQ04Q6uehLcmXWrKW&om_nextpage=true",
				"type": "deeplink"
			}, {
				"title": "Flights Under $199",
				"url": "http://ccs.infospace.com/ClickHandler.ashx?encp=ld%3d20170830%26app%3d1%26c%3ddogpl.100%26s%3ddogpilesem%26rc%3ddogpl.300%26dc%3d%26euip%3d104.132.11.74%26pvaid%3de6a8799486614194bae5467d76ce1d31%26dt%3dDesktop%26fct.uid%3ddddaea275d7e4d759eb57b7755b44a37%26en%3d352GU4fR56WY6dtc5jlLFS1qfqwkvnZ3WLV07iuIzB20xQ26pTFYPQ%253d%253d%26coi%3d1506%26npp%3d0%26p%3d1%26pp%3d0%26mid%3d5%26ep%3d2%26ru%3dhttps%253a%252f%252f2359788.r.bat.bing.com%252f%253fld%253dd3dXlk72wkdDe-kCUowHt8mTVUCUyXQb49ma1CWIE3BrWHLSwVCFmxQPO7NH7S6jbITJWTySR2Z0761Ehzqq7eKhf51f_G09nR9Ibkl2J4F_C6p2k2f7CuDMTzIhkzdeZO5bEBaf5jmjcYJFV2zEfKwsvuXPE%2526u%253dhttp%25253a%25252f%25252f1195.xg4ken.com%25252fmedia%25252fredir.php%25253fprof%25253d%252526camp%25253d%252526affcode%25253d%252526k_inner_url_encoded%25253d0%252526cid%25253d73461193247625%25257c%25257cairlines%252526mType%25253de%252526networkType%25253dsearch%252526kdv%25253dc%252526ksl%25253d382773%252526url%25255b%25255d%25253dhttps%25253a%25252f%25252fwww.cheaptickets.com%25252fg%25252fdd%25252fflightdeals-under199%25253fsemcid%25253dcheaptickets-us.multilob.bing.gt-c-en.flight%252526kword%25253dbe.%25257cairlines%25257c.107.184806.410.24897.73461193247625.1531911971.kwd-14966926842.s%252526epic%25253d_kenshoo_clickid_%252526epi%25253d_kenshoo_clickid_%252526semdtl%25253da151868923.b11531911971.d173461193247625.e1c.f1.g1kwd-14966926842.h1e.i1.j1.k1.l1s.m1be.n1%26hash%3dBAE69F9FBB1314BEDC3531D58FD23B70&ap=0&cop=main-title&om_userid=WuWG1m1lIw1lbevx1l4I&om_sessionid=GMlva6OKEexxdZ4T3hX7&om_pageid=XygfQ04Q6uehLcmXWrKW&om_nextpage=true",
				"type": "deeplink"
			}, {
				"title": "Secret Bargain Deals",
				"url": "http://ccs.infospace.com/ClickHandler.ashx?encp=ld%3d20170830%26app%3d1%26c%3ddogpl.100%26s%3ddogpilesem%26rc%3ddogpl.300%26dc%3d%26euip%3d104.132.11.74%26pvaid%3de6a8799486614194bae5467d76ce1d31%26dt%3dDesktop%26fct.uid%3ddddaea275d7e4d759eb57b7755b44a37%26en%3d352GU4fR56WY6dtc5jlLFS1qfqwkvnZ3WLV07iuIzB20xQ26pTFYPQ%253d%253d%26coi%3d1506%26npp%3d0%26p%3d1%26pp%3d0%26mid%3d5%26ep%3d3%26ru%3dhttps%253a%252f%252f2359788.r.bat.bing.com%252f%253fld%253dd3SDfyNlKpGq-JRxqkk4QIIzVUCUzKV3nB1_ns6rin3v278QcuP6h6mEJ8l_0DHvlcmzyb7k5UBykIpIw0IUDvE2ZWY1l4WAlVk9bUKKucR7eli6QhG0oI6Z7GlIq0XJE4ePEpFEQuMWrFTOCyMC793o93MBo%2526u%253dhttp%25253a%25252f%25252f1195.xg4ken.com%25252fmedia%25252fredir.php%25253fprof%25253d%252526camp%25253d%252526affcode%25253d%252526k_inner_url_encoded%25253d0%252526cid%25253d73461193247625%25257c%25257cairlines%252526mType%25253de%252526networkType%25253dsearch%252526kdv%25253dc%252526ksl%25253d382774%252526url%25255b%25255d%25253dhttps%25253a%25252f%25252fwww.cheaptickets.com%25252fg%25252fmb%25252ftraveldeals-secret-bargains%25253fsemcid%25253dcheaptickets-us.multilob.bing.gt-c-en.flight%252526kword%25253dbe.%25257cairlines%25257c.107.184806.410.24897.73461193247625.1531911971.kwd-14966926842.s%252526epic%25253d_kenshoo_clickid_%252526epi%25253d_kenshoo_clickid_%252526semdtl%25253da151868923.b11531911971.d173461193247625.e1c.f1.g1kwd-14966926842.h1e.i1.j1.k1.l1s.m1be.n1%26hash%3d6DDD9D30F85EE7FD63BB2E66BBF3751B&ap=0&cop=main-title&om_userid=WuWG1m1lIw1lbevx1l4I&om_sessionid=GMlva6OKEexxdZ4T3hX7&om_pageid=XygfQ04Q6uehLcmXWrKW&om_nextpage=true",
				"type": "deeplink"
			}, {
				"title": "Up to 50% off Hotels",
				"url": "http://ccs.infospace.com/ClickHandler.ashx?encp=ld%3d20170830%26app%3d1%26c%3ddogpl.100%26s%3ddogpilesem%26rc%3ddogpl.300%26dc%3d%26euip%3d104.132.11.74%26pvaid%3de6a8799486614194bae5467d76ce1d31%26dt%3dDesktop%26fct.uid%3ddddaea275d7e4d759eb57b7755b44a37%26en%3d352GU4fR56WY6dtc5jlLFS1qfqwkvnZ3WLV07iuIzB20xQ26pTFYPQ%253d%253d%26coi%3d1506%26npp%3d0%26p%3d1%26pp%3d0%26mid%3d5%26ep%3d4%26ru%3dhttps%253a%252f%252f2359788.r.bat.bing.com%252f%253fld%253dd3JmZDnB4Z-sSFy9_M_Ki82jVUCUwPcKDcU_FBLZd7a0JYTSe7CDOTOsNC0DVVAIvaeFT7FKr_KoQ8d_MyTyXohYSiyf5Z-4ZTfQFJzhJBbiCcoaQOxZKl_4jmTaQ9V4YromhB0dWRS2NukR7Qb3xB-y1NLV4%2526u%253dhttp%25253a%25252f%25252f1195.xg4ken.com%25252fmedia%25252fredir.php%25253fprof%25253d%252526camp%25253d%252526affcode%25253d%252526k_inner_url_encoded%25253d0%252526cid%25253d73461193247625%25257c%25257cairlines%252526mType%25253de%252526networkType%25253dsearch%252526kdv%25253dc%252526ksl%25253d382775%252526url%25255b%25255d%25253dhttps%25253a%25252f%25252fwww.cheaptickets.com%25252fg%25252flc%25252ftraveldeals-major-hotel-sale%25253fsemcid%25253dcheaptickets-us.multilob.bing.gt-c-en.flight%252526kword%25253dbe.%25257cairlines%25257c.107.184806.410.24897.73461193247625.1531911971.kwd-14966926842.s%252526epic%25253d_kenshoo_clickid_%252526epi%25253d_kenshoo_clickid_%252526semdtl%25253da151868923.b11531911971.d173461193247625.e1c.f1.g1kwd-14966926842.h1e.i1.j1.k1.l1s.m1be.n1%26hash%3d37B67A0189CFBA566A5BC460ABA49575&ap=0&cop=main-title&om_userid=WuWG1m1lIw1lbevx1l4I&om_sessionid=GMlva6OKEexxdZ4T3hX7&om_pageid=XygfQ04Q6uehLcmXWrKW&om_nextpage=true",
				"type": "deeplink"
			}, {
				"title": "Save Extra 16% On Hotels",
				"url": "http://ccs.infospace.com/ClickHandler.ashx?encp=ld%3d20170830%26app%3d1%26c%3ddogpl.100%26s%3ddogpilesem%26rc%3ddogpl.300%26dc%3d%26euip%3d104.132.11.74%26pvaid%3de6a8799486614194bae5467d76ce1d31%26dt%3dDesktop%26fct.uid%3ddddaea275d7e4d759eb57b7755b44a37%26en%3d352GU4fR56WY6dtc5jlLFS1qfqwkvnZ3WLV07iuIzB20xQ26pTFYPQ%253d%253d%26coi%3d1506%26npp%3d0%26p%3d1%26pp%3d0%26mid%3d5%26ep%3d5%26ru%3dhttps%253a%252f%252f2359788.r.bat.bing.com%252f%253fld%253dd3tB5RgIrnsuRAcZR4adoKPjVUCUzC5gba-AksX-ZG11Yp6hN6oIwYI2k1H6eaK_09_dW1gx0mjby7Y6iZPbaa66Q-Zg8CEquRMWeqkzu-sYO9CvsXfxflWtqqZBqSuTCUo3notCen4gV49BEZ1eXV77dMspM%2526u%253dhttp%25253a%25252f%25252f1195.xg4ken.com%25252fmedia%25252fredir.php%25253fprof%25253d%252526camp%25253d%252526affcode%25253d%252526k_inner_url_encoded%25253d0%252526cid%25253d73461193247625%25257c%25257cairlines%252526mType%25253de%252526networkType%25253dsearch%252526kdv%25253dc%252526ksl%25253d382776%252526url%25255b%25255d%25253dhttps%25253a%25252f%25252fwww.cheaptickets.com%25252fg%25252flc%25252ftraveldeals-cheapoftheweek%25253fsemcid%25253dcheaptickets-us.multilob.bing.gt-c-en.flight%252526kword%25253dbe.%25257cairlines%25257c.107.184806.410.24897.73461193247625.1531911971.kwd-14966926842.s%252526epic%25253d_kenshoo_clickid_%252526epi%25253d_kenshoo_clickid_%252526semdtl%25253da151868923.b11531911971.d173461193247625.e1c.f1.g1kwd-14966926842.h1e.i1.j1.k1.l1s.m1be.n1%26hash%3d8DD9CD0750AD8A4C1AF824B003BCE0AA&ap=0&cop=main-title&om_userid=WuWG1m1lIw1lbevx1l4I&om_sessionid=GMlva6OKEexxdZ4T3hX7&om_pageid=XygfQ04Q6uehLcmXWrKW&om_nextpage=true",
				"type": "deeplink"
			}, {
				"title": "Hotels Under $50",
				"url": "http://ccs.infospace.com/ClickHandler.ashx?encp=ld%3d20170830%26app%3d1%26c%3ddogpl.100%26s%3ddogpilesem%26rc%3ddogpl.300%26dc%3d%26euip%3d104.132.11.74%26pvaid%3de6a8799486614194bae5467d76ce1d31%26dt%3dDesktop%26fct.uid%3ddddaea275d7e4d759eb57b7755b44a37%26en%3d352GU4fR56WY6dtc5jlLFS1qfqwkvnZ3WLV07iuIzB20xQ26pTFYPQ%253d%253d%26coi%3d1506%26npp%3d0%26p%3d1%26pp%3d0%26mid%3d5%26ep%3d6%26ru%3dhttps%253a%252f%252f2359788.r.bat.bing.com%252f%253fld%253dd3Tv4BT9FO4xCPRZGEzeJG5jVUCUykXqQjQ0hKRMCgKtjuo1C4LL6owtjX5sS2gJGU-GDqXeJLEQaqoPJ9bCO0i3s_hnscavsM3DzrLrVqlVu91Hu4G5MX3Ys1oIZIJEtj2bx5EbyGfgRddr3_M8AO7XR5OU8%2526u%253dhttp%25253a%25252f%25252f1195.xg4ken.com%25252fmedia%25252fredir.php%25253fprof%25253d%252526camp%25253d%252526affcode%25253d%252526k_inner_url_encoded%25253d0%252526cid%25253d73461193247625%25257c%25257cairlines%252526mType%25253de%252526networkType%25253dsearch%252526kdv%25253dc%252526ksl%25253d382777%252526url%25255b%25255d%25253dhttps%25253a%25252f%25252fwww.cheaptickets.com%25252fg%25252fdd%25252ftraveldeals-top-hotel-deals%25253fsemcid%25253dcheaptickets-us.multilob.bing.gt-c-en.flight%252526kword%25253dbe.%25257cairlines%25257c.107.184806.410.24897.73461193247625.1531911971.kwd-14966926842.s%252526epic%25253d_kenshoo_clickid_%252526epi%25253d_kenshoo_clickid_%252526semdtl%25253da151868923.b11531911971.d173461193247625.e1c.f1.g1kwd-14966926842.h1e.i1.j1.k1.l1s.m1be.n1%26hash%3dA1C301ACC8E519A8C55379D661BCCB2F&ap=0&cop=main-title&om_userid=WuWG1m1lIw1lbevx1l4I&om_sessionid=GMlva6OKEexxdZ4T3hX7&om_pageid=XygfQ04Q6uehLcmXWrKW&om_nextpage=true",
				"type": "deeplink"
			}]
		},
		{
			"display_url": "www.expedia.com/Flights/Airline",
			"title": "AD2 -- Expedia - Cheap Plane Tickets - Fly At Incredible Prices.",
			"description": "Plan The Ultimate Trip. Fantastic Flight + Hotel Deals Are Waiting Just For You.",
			"url": "http://ccs.infospace.com/ClickHandler.ashx?encp=ld%3d20170830%26app%3d1%26c%3ddogpl.100%26s%3ddogpilesem%26rc%3ddogpl.300%26dc%3d%26euip%3d104.132.11.74%26pvaid%3de6a8799486614194bae5467d76ce1d31%26dt%3dDesktop%26fct.uid%3ddddaea275d7e4d759eb57b7755b44a37%26en%3d352GU4fR56WY6dtc5jlLFS1qfqwkvnZ3WLV07iuIzB20xQ26pTFYPQ%253d%253d%26coi%3d1493%26npp%3d0%26p%3d1%26pp%3d0%26mid%3d9%26ep%3d2%26ru%3dhttps%253a%252f%252f43070220.r.bat.bing.com%252f%253fld%253dd3Q3L8IR2I2xs2e6PVneNxdTVUCUw4V3cAv7E4TGBoGhwt6hvMHTSrLXBOL1twGvzSxOPW0dJ4BSdAzY5fJy0On9p6gSHxmu29Em96Tq_8HwEbxFmP3_5Z0O9ClXDHMsqfrjccaK8liPYde-YCj0B4OVooazE%2526u%253dhttp%25253a%25252f%25252f138.xg4ken.com%25252ftrk%25252fv1%25253fprof%25253d485%252526camp%25253d220303%252526affcode%25253dkw22938%252526kct%25253dmsn%252526kchid%25253d43070220%252526cid%25253d14388586985%252526queryStr%25253dairlines%252526kdv%25253dc%252526criteriaid%25253dkwd-29737302506%252526adgroupid%25253d5282898297%252526campaignid%25253d141944743%252526url%25253dhttps%25253a%25252f%25252fwww.expedia.com%25252fFlights%25253fsemcid%25253dus.multilob.bing.gt-c-en.flight%252526kword%25253dZzZz.4850000022938._kenshoo_clickid_%252526semdtl%25253da1141944743.b15282898297.d114388586985.e1c.f1.g1kwd-29737302506.h1e.i1.j1.k1.l1s.m1be.n1%252526msclkid%25253d%25257bmsclkid%25257d%252526utm_source%25253dbing%252526utm_medium%25253dcpc%252526utm_campaign%25253dUSA%2525253AENG%2525253A%252540%2525253AGT%2525253AGLOB%2525253AALL%2525253AE%2525253AX%2525253A%2525253A%252526utm_term%25253dairlines%252526utm_content%25253dUSA%2525253AENG%2525253A%252540%2525253AGT%2525253AGLOB%2525253AALL%2525253AXX%2525253AX%2525253AX%2525253AX%2525253AX%2525253AE%2525253AX%2525253Aairline%2525253A%26du%3dwww.expedia.com%252fFlights%252fAirline%26hash%3d005AD968DB08433EFB87FF4F0D014008&ap=0&cop=main-title&om_userid=WuWG1m1lIw1lbevx1l4I&om_sessionid=GMlva6OKEexxdZ4T3hX7&om_pageid=XygfQ04Q6uehLcmXWrKW&om_nextpage=true",
			"type": "ad",
			"deeplinks": [{
				"title": "Search Cheap Flights",
				"url": "http://ccs.infospace.com/ClickHandler.ashx?encp=ld%3d20170830%26app%3d1%26c%3ddogpl.100%26s%3ddogpilesem%26rc%3ddogpl.300%26dc%3d%26euip%3d104.132.11.74%26pvaid%3de6a8799486614194bae5467d76ce1d31%26dt%3dDesktop%26fct.uid%3ddddaea275d7e4d759eb57b7755b44a37%26en%3d352GU4fR56WY6dtc5jlLFS1qfqwkvnZ3WLV07iuIzB20xQ26pTFYPQ%253d%253d%26coi%3d1506%26npp%3d0%26p%3d1%26pp%3d0%26mid%3d5%26ep%3d1%26ru%3dhttps%253a%252f%252f43070220.r.bat.bing.com%252f%253fld%253dd3_6jYUIFb0alDKd55Cc99sDVUCUxAckCnpdeBhXgeQGaPpuUeDS2BEIRMqjB7KM9YJt2VuavhbLcKY5hBMgYF72v6vrTOEhkPVK7Kc9f1GZg0qjsQRw0Hy5XfsDxEd7onmVOH7uFI82cfkljkWcMOMmNdwTo%2526u%253dhttp%25253a%25252f%25252f138.xg4ken.com%25252fmedia%25252fredir.php%25253fprof%25253d%252526camp%25253d%252526affcode%25253d%252526k_inner_url_encoded%25253d0%252526cid%25253d14388586985%25257c%25257cairlines%252526mType%25253de%252526networkType%25253dsearch%252526kdv%25253dc%252526ksl%25253d5111243%252526url%25255b%25255d%25253dhttp%25253a%25252f%25252fwww.expedia.com%25252fFlights%25253fregionId%25253d%252526Sitelink%25253dCheap_Flights%252526semdtl%25253da1141944743.b15282898297.d114388586985.e1c.f1.g1kwd-29737302506.h1e.i1.j1.k1.l1s.m1be.n1%252526msclkid%25253d%25257bmsclkid%25257d%252526semcid%25253dus.multilob.bing.gt-c-en.flight%252526utm_source%25253dbing%252526utm_medium%25253dcpc%252526utm_campaign%25253dUSA%2525253AENG%2525253A%252540%2525253AGT%2525253AGLOB%2525253AALL%2525253AE%2525253AX%2525253A%2525253A%252526utm_term%25253dairlines%252526utm_content%25253dUSA%2525253AENG%2525253A%252540%2525253AGT%2525253AGLOB%2525253AALL%2525253AXX%2525253AX%2525253AX%2525253AX%2525253AX%2525253AE%2525253AX%2525253Aairline%2525253A%26hash%3dF894E10D4551306EEA3AF96FCC9DE0DC&ap=0&cop=main-title&om_userid=WuWG1m1lIw1lbevx1l4I&om_sessionid=GMlva6OKEexxdZ4T3hX7&om_pageid=XygfQ04Q6uehLcmXWrKW&om_nextpage=true",
				"type": "deeplink"
			}, {
				"title": "Direct Flights",
				"url": "http://ccs.infospace.com/ClickHandler.ashx?encp=ld%3d20170830%26app%3d1%26c%3ddogpl.100%26s%3ddogpilesem%26rc%3ddogpl.300%26dc%3d%26euip%3d104.132.11.74%26pvaid%3de6a8799486614194bae5467d76ce1d31%26dt%3dDesktop%26fct.uid%3ddddaea275d7e4d759eb57b7755b44a37%26en%3d352GU4fR56WY6dtc5jlLFS1qfqwkvnZ3WLV07iuIzB20xQ26pTFYPQ%253d%253d%26coi%3d1506%26npp%3d0%26p%3d1%26pp%3d0%26mid%3d5%26ep%3d2%26ru%3dhttps%253a%252f%252f43070220.r.bat.bing.com%252f%253fld%253dd37nU0jtK4XatVP2HBkDITMzVUCUx2Al8trmSBdvqe6wH3DXMIOn-OPr81-htj8fpDFABUfVmw6elr3k3Jm6NNrI80gJWoUOKfiN3_OVpAZ95KJVQm5egsUHNS9bfa_zT_arDXPJDGdb2Zq2iS1VKSwtwbaCA%2526u%253dhttp%25253a%25252f%25252f138.xg4ken.com%25252fmedia%25252fredir.php%25253fprof%25253d%252526camp%25253d%252526affcode%25253d%252526k_inner_url_encoded%25253d0%252526cid%25253d14388586985%25257c%25257cairlines%252526mType%25253de%252526networkType%25253dsearch%252526kdv%25253dc%252526ksl%25253d5111246%252526url%25255b%25255d%25253dhttp%25253a%25252f%25252fwww.expedia.com%25252fFlights%25253fregionId%25253d%252526Sitelink%25253dDirect_Flights%252526semdtl%25253da1141944743.b15282898297.d114388586985.e1c.f1.g1kwd-29737302506.h1e.i1.j1.k1.l1s.m1be.n1%252526msclkid%25253d%25257bmsclkid%25257d%252526semcid%25253dus.multilob.bing.gt-c-en.flight%252526utm_source%25253dbing%252526utm_medium%25253dcpc%252526utm_campaign%25253dUSA%2525253AENG%2525253A%252540%2525253AGT%2525253AGLOB%2525253AALL%2525253AE%2525253AX%2525253A%2525253A%252526utm_term%25253dairlines%252526utm_content%25253dUSA%2525253AENG%2525253A%252540%2525253AGT%2525253AGLOB%2525253AALL%2525253AXX%2525253AX%2525253AX%2525253AX%2525253AX%2525253AE%2525253AX%2525253Aairline%2525253A%26hash%3d50EAB4427BFE3D2CA8C9283586E972C7&ap=0&cop=main-title&om_userid=WuWG1m1lIw1lbevx1l4I&om_sessionid=GMlva6OKEexxdZ4T3hX7&om_pageid=XygfQ04Q6uehLcmXWrKW&om_nextpage=true",
				"type": "deeplink"
			}, {
				"title": "Cheap Hotels",
				"url": "http://ccs.infospace.com/ClickHandler.ashx?encp=ld%3d20170830%26app%3d1%26c%3ddogpl.100%26s%3ddogpilesem%26rc%3ddogpl.300%26dc%3d%26euip%3d104.132.11.74%26pvaid%3de6a8799486614194bae5467d76ce1d31%26dt%3dDesktop%26fct.uid%3ddddaea275d7e4d759eb57b7755b44a37%26en%3d352GU4fR56WY6dtc5jlLFS1qfqwkvnZ3WLV07iuIzB20xQ26pTFYPQ%253d%253d%26coi%3d1506%26npp%3d0%26p%3d1%26pp%3d0%26mid%3d5%26ep%3d3%26ru%3dhttps%253a%252f%252f43070220.r.bat.bing.com%252f%253fld%253dd3rUirrulkVoZ8HCgTvsTk8TVUCUzjJCdz0rF1hH58zvLGcBmPScw4OvNYAXHVuTzlcw605FevJuas2UJqA-Pt1aO7lyBfvopdebCdVahZkf60OVXVQrVZCby7gP2c_0HHLj5lRFZ-TMg9qwM9N-dwp9hq58c%2526u%253dhttp%25253a%25252f%25252f138.xg4ken.com%25252fmedia%25252fredir.php%25253fprof%25253d%252526camp%25253d%252526affcode%25253d%252526k_inner_url_encoded%25253d0%252526cid%25253d14388586985%25257c%25257cairlines%252526mType%25253de%252526networkType%25253dsearch%252526kdv%25253dc%252526ksl%25253d5111249%252526url%25255b%25255d%25253dhttp%25253a%25252f%25252fwww.expedia.com%25252fHotels%25253fregionId%25253d%252526Sitelink%25253dCheap_Hotels%252526semdtl%25253da1141944743.b15282898297.d114388586985.e1c.f1.g1kwd-29737302506.h1e.i1.j1.k1.l1s.m1be.n1%252526msclkid%25253d%25257bmsclkid%25257d%252526semcid%25253dus.multilob.bing.gt-c-en.flight%252526utm_source%25253dbing%252526utm_medium%25253dcpc%252526utm_campaign%25253dUSA%2525253AENG%2525253A%252540%2525253AGT%2525253AGLOB%2525253AALL%2525253AE%2525253AX%2525253A%2525253A%252526utm_term%25253dairlines%252526utm_content%25253dUSA%2525253AENG%2525253A%252540%2525253AGT%2525253AGLOB%2525253AALL%2525253AXX%2525253AX%2525253AX%2525253AX%2525253AX%2525253AE%2525253AX%2525253Aairline%2525253A%26hash%3d3E318D6BD927506204B11D8CEA2B6D66&ap=0&cop=main-title&om_userid=WuWG1m1lIw1lbevx1l4I&om_sessionid=GMlva6OKEexxdZ4T3hX7&om_pageid=XygfQ04Q6uehLcmXWrKW&om_nextpage=true",
				"type": "deeplink"
			}, {
				"title": "Book Flights + Hotel",
				"url": "http://ccs.infospace.com/ClickHandler.ashx?encp=ld%3d20170830%26app%3d1%26c%3ddogpl.100%26s%3ddogpilesem%26rc%3ddogpl.300%26dc%3d%26euip%3d104.132.11.74%26pvaid%3de6a8799486614194bae5467d76ce1d31%26dt%3dDesktop%26fct.uid%3ddddaea275d7e4d759eb57b7755b44a37%26en%3d352GU4fR56WY6dtc5jlLFS1qfqwkvnZ3WLV07iuIzB20xQ26pTFYPQ%253d%253d%26coi%3d1506%26npp%3d0%26p%3d1%26pp%3d0%26mid%3d5%26ep%3d4%26ru%3dhttps%253a%252f%252f43070220.r.bat.bing.com%252f%253fld%253dd3EbLv1LHMaoWWgeQIS4iYgDVUCUxDZcbJphmORuiWe2JMIx0JCvCkHyKSfNdzy7FTSKN-K5PDWQxwu6r5YW0OAoyYElxIFevM3QpXY44Gc2icT_u-SjBsD-wE1zW9aL39tmL_CVM42CXAMyXFLAzlWALz45E%2526u%253dhttp%25253a%25252f%25252f138.xg4ken.com%25252fmedia%25252fredir.php%25253fprof%25253d%252526camp%25253d%252526affcode%25253d%252526k_inner_url_encoded%25253d0%252526cid%25253d14388586985%25257c%25257cairlines%252526mType%25253de%252526networkType%25253dsearch%252526kdv%25253dc%252526ksl%25253d5111252%252526url%25255b%25255d%25253dhttp%25253a%25252f%25252fwww.expedia.com%25252fFlights%25253fregionId%25253d%252526Sitelink%25253dBook_Flights_Hotel%252526semdtl%25253da1141944743.b15282898297.d114388586985.e1c.f1.g1kwd-29737302506.h1e.i1.j1.k1.l1s.m1be.n1%252526msclkid%25253d%25257bmsclkid%25257d%252526semcid%25253dus.multilob.bing.gt-c-en.flight%252526utm_source%25253dbing%252526utm_medium%25253dcpc%252526utm_campaign%25253dUSA%2525253AENG%2525253A%252540%2525253AGT%2525253AGLOB%2525253AALL%2525253AE%2525253AX%2525253A%2525253A%252526utm_term%25253dairlines%252526utm_content%25253dUSA%2525253AENG%2525253A%252540%2525253AGT%2525253AGLOB%2525253AALL%2525253AXX%2525253AX%2525253AX%2525253AX%2525253AX%2525253AE%2525253AX%2525253Aairline%2525253A%26hash%3dE503DB09FE3D203769810B38037E8CD3&ap=0&cop=main-title&om_userid=WuWG1m1lIw1lbevx1l4I&om_sessionid=GMlva6OKEexxdZ4T3hX7&om_pageid=XygfQ04Q6uehLcmXWrKW&om_nextpage=true",
				"type": "deeplink"
			}]
		}
	],
	"aylf": [{
		"title": "cheap tickets flights",
		"htmlTitle": "cheap tickets flights",
		"coid": 1498,
		"type": "related",
		"sources": [{
			"name": "bing",
			"position": 1,
			"provider": "BingAds"
		}]
	}, {
		"title": "cheapoair flights",
		"htmlTitle": "cheapoair flights",
		"coid": 1498,
		"type": "related",
		"sources": [{
			"name": "bing",
			"position": 2,
			"provider": "BingAds"
		}]
	}, {
		"title": "air flight and hotel packages",
		"htmlTitle": "air flight and hotel packages",
		"coid": 1498,
		"type": "related",
		"sources": [{
			"name": "bing",
			"position": 3,
			"provider": "BingAds"
		}]
	}, {
		"title": "cheap airline tickets",
		"htmlTitle": "cheap airline tickets",
		"coid": 1498,
		"type": "related",
		"sources": [{
			"name": "bing",
			"position": 4,
			"provider": "BingAds"
		}]
	}, {
		"title": "cheap flights",
		"htmlTitle": "cheap flights",
		"coid": 1498,
		"type": "related",
		"sources": [{
			"name": "bing",
			"position": 5,
			"provider": "BingAds"
		}]
	}, {
		"title": "travelocity hotel",
		"htmlTitle": "travelocity hotel",
		"coid": 1498,
		"type": "related",
		"sources": [{
			"name": "bing",
			"position": 6,
			"provider": "BingAds"
		}]
	}, {
		"title": "orbitz flights",
		"htmlTitle": "orbitz flights",
		"coid": 1498,
		"type": "related",
		"sources": [{
			"name": "bing",
			"position": 7,
			"provider": "BingAds"
		}]
	}, {
		"title": "travelocity flights only",
		"htmlTitle": "travelocity flights only",
		"coid": 1498,
		"type": "related",
		"sources": [{
			"name": "bing",
			"position": 8,
			"provider": "BingAds"
		}]
	}],
	"main": [{
		"display_url": "www.southwest.com/",
		"title": "Southwest <strong>Airlines</strong> - Official Site",
		"description": "Official Southwest <strong>Airlines</strong> website, the only place to find Southwest <strong>Airlines</strong> fares online. Book lowest airfare deals, view flight schedules, get flight status, and ...",
		"url": "http://ccs.infospace.com/ClickHandler.ashx?encp=ld%3d20170830%26app%3d1%26c%3ddogpl.100%26s%3ddogpilesem%26rc%3ddogpl.300%26dc%3d%26euip%3d104.132.11.74%26pvaid%3de6a8799486614194bae5467d76ce1d31%26dt%3dDesktop%26fct.uid%3ddddaea275d7e4d759eb57b7755b44a37%26en%3d352GU4fR56WY6dtc5jlLFS1qfqwkvnZ3WLV07iuIzB20xQ26pTFYPQ%253d%253d%26coi%3d1494%26npp%3d0%26p%3d0%26pp%3d0%26mid%3d9%26ep%3d1%26ru%3dhttps%253a%252f%252fwww.southwest.com%252f%26du%3dhttps%253a%252f%252fwww.southwest.com%26hash%3d0E9F416F19EDAB26140C611C6349715A&ap=0&cop=main-title&om_userid=WuWG1m1lIw1lbevx1l4I&om_sessionid=GMlva6OKEexxdZ4T3hX7&om_pageid=XygfQ04Q6uehLcmXWrKW&om_nextpage=true",
		"paid": false,
		"type": "web",
		"sources": [{
			"name": "bing",
			"position": 1,
			"provider": "BingAds"
		}]
	}, {
		"display_url": "www.seatguru.com/browseairlines/browseairlines.php",
		"title": "List of All Major <strong>Airlines</strong> - SeatGuru",
		"description": "Browse all of our featured <strong>airlines</strong> to get a comprehensive look at the carrier that best suits your travel needs.",
		"url": "http://ccs.infospace.com/ClickHandler.ashx?encp=ld%3d20170830%26app%3d1%26c%3ddogpl.100%26s%3ddogpilesem%26rc%3ddogpl.300%26dc%3d%26euip%3d104.132.11.74%26pvaid%3de6a8799486614194bae5467d76ce1d31%26dt%3dDesktop%26fct.uid%3ddddaea275d7e4d759eb57b7755b44a37%26en%3d352GU4fR56WY6dtc5jlLFS1qfqwkvnZ3WLV07iuIzB20xQ26pTFYPQ%253d%253d%26coi%3d1494%26npp%3d0%26p%3d0%26pp%3d0%26mid%3d9%26ep%3d2%26ru%3dhttps%253a%252f%252fwww.seatguru.com%252fbrowseairlines%252fbrowseairlines.php%26du%3dhttps%253a%252f%252fwww.seatguru.com%252fbrowseairlines%252fbrowseairlines.php%26hash%3d24F380AC0A2B67E9E17762D3B039D179&ap=0&cop=main-title&om_userid=WuWG1m1lIw1lbevx1l4I&om_sessionid=GMlva6OKEexxdZ4T3hX7&om_pageid=XygfQ04Q6uehLcmXWrKW&om_nextpage=true",
		"paid": false,
		"type": "web",
		"sources": [{
			"name": "bing",
			"position": 2,
			"provider": "BingAds"
		}]
	}, {
		"display_url": "www.delta.com",
		"title": "Delta Air Lines - Airline Tickets and Airfare to Worldwide ...",
		"description": "Official website of Delta <strong>Airlines</strong> including trip bookings, check-in, flight status, and travel information.",
		"url": "http://ccs.infospace.com/ClickHandler.ashx?encp=ld%3d20170830%26app%3d1%26c%3ddogpl.100%26s%3ddogpilesem%26rc%3ddogpl.300%26dc%3d%26euip%3d104.132.11.74%26pvaid%3de6a8799486614194bae5467d76ce1d31%26dt%3dDesktop%26fct.uid%3ddddaea275d7e4d759eb57b7755b44a37%26en%3d352GU4fR56WY6dtc5jlLFS1qfqwkvnZ3WLV07iuIzB20xQ26pTFYPQ%253d%253d%26coi%3d1494%26npp%3d0%26p%3d0%26pp%3d0%26mid%3d9%26ep%3d3%26ru%3dhttp%253a%252f%252fwww.delta.com%252f%26du%3dwww.delta.com%26hash%3d68F3171A88529FBB451CB2774B7408C6&ap=0&cop=main-title&om_userid=WuWG1m1lIw1lbevx1l4I&om_sessionid=GMlva6OKEexxdZ4T3hX7&om_pageid=XygfQ04Q6uehLcmXWrKW&om_nextpage=true",
		"paid": false,
		"type": "web",
		"sources": [{
			"name": "bing",
			"position": 3,
			"provider": "BingAds"
		}]
	}, {
		"display_url": "en.wikipedia.org/wiki/List_of_<strong>airlines</strong>",
		"title": "Lists of <strong>airlines</strong> - Wikipedia",
		"description": "This is a list of <strong>airlines</strong>. Lists of <strong>airlines</strong> are listed alphabetically by the name of the continent from which they operate. There are lists of <strong>airlines</strong> for all of ...",
		"url": "http://ccs.infospace.com/ClickHandler.ashx?encp=ld%3d20170830%26app%3d1%26c%3ddogpl.100%26s%3ddogpilesem%26rc%3ddogpl.300%26dc%3d%26euip%3d104.132.11.74%26pvaid%3de6a8799486614194bae5467d76ce1d31%26dt%3dDesktop%26fct.uid%3ddddaea275d7e4d759eb57b7755b44a37%26en%3d352GU4fR56WY6dtc5jlLFS1qfqwkvnZ3WLV07iuIzB20xQ26pTFYPQ%253d%253d%26coi%3d1494%26npp%3d0%26p%3d0%26pp%3d0%26mid%3d9%26ep%3d4%26ru%3dhttps%253a%252f%252fen.wikipedia.org%252fwiki%252fList_of_airlines%26du%3dhttps%253a%252f%252fen.wikipedia.org%252fwiki%252fList_of_airlines%26hash%3d1B047991EB8BF7A85FACD2CF0CE41B5A&ap=0&cop=main-title&om_userid=WuWG1m1lIw1lbevx1l4I&om_sessionid=GMlva6OKEexxdZ4T3hX7&om_pageid=XygfQ04Q6uehLcmXWrKW&om_nextpage=true",
		"paid": false,
		"type": "web",
		"sources": [{
			"name": "bing",
			"position": 4,
			"provider": "BingAds"
		}]
	}, {
		"display_url": "www.allegiantair.com",
		"title": "Allegiant Air - Official Site",
		"description": "Official Allegiant website, the only place to book Allegiant’s low fares for flights to Las Vegas, Florida, and more. Find deals on vacation packages, check your ...",
		"url": "http://ccs.infospace.com/ClickHandler.ashx?encp=ld%3d20170830%26app%3d1%26c%3ddogpl.100%26s%3ddogpilesem%26rc%3ddogpl.300%26dc%3d%26euip%3d104.132.11.74%26pvaid%3de6a8799486614194bae5467d76ce1d31%26dt%3dDesktop%26fct.uid%3ddddaea275d7e4d759eb57b7755b44a37%26en%3d352GU4fR56WY6dtc5jlLFS1qfqwkvnZ3WLV07iuIzB20xQ26pTFYPQ%253d%253d%26coi%3d1494%26npp%3d0%26p%3d0%26pp%3d0%26mid%3d9%26ep%3d5%26ru%3dhttp%253a%252f%252fwww.allegiantair.com%252f%26du%3dwww.allegiantair.com%26hash%3d091651AAAC2225A8DAA5E3AF1BA934AF&ap=0&cop=main-title&om_userid=WuWG1m1lIw1lbevx1l4I&om_sessionid=GMlva6OKEexxdZ4T3hX7&om_pageid=XygfQ04Q6uehLcmXWrKW&om_nextpage=true",
		"paid": false,
		"type": "web",
		"sources": [{
			"name": "bing",
			"position": 5,
			"provider": "BingAds"
		}]
	}, {
		"display_url": "www.aa.com/",
		"title": "American <strong>Airlines</strong> - Airline tickets and cheap flights at ...",
		"description": "American <strong>Airlines</strong> has airline tickets, cheap flights, vacation packages and American <strong>Airlines</strong> AAdvantage bonus mile offers at AA.com",
		"url": "http://ccs.infospace.com/ClickHandler.ashx?encp=ld%3d20170830%26app%3d1%26c%3ddogpl.100%26s%3ddogpilesem%26rc%3ddogpl.300%26dc%3d%26euip%3d104.132.11.74%26pvaid%3de6a8799486614194bae5467d76ce1d31%26dt%3dDesktop%26fct.uid%3ddddaea275d7e4d759eb57b7755b44a37%26en%3d352GU4fR56WY6dtc5jlLFS1qfqwkvnZ3WLV07iuIzB20xQ26pTFYPQ%253d%253d%26coi%3d1494%26npp%3d0%26p%3d0%26pp%3d0%26mid%3d9%26ep%3d6%26ru%3dhttps%253a%252f%252fwww.aa.com%252fhomePage.do%26du%3dhttps%253a%252f%252fwww.aa.com%26hash%3d212FB123939F0BCF4BBA4BDC4093EB02&ap=0&cop=main-title&om_userid=WuWG1m1lIw1lbevx1l4I&om_sessionid=GMlva6OKEexxdZ4T3hX7&om_pageid=XygfQ04Q6uehLcmXWrKW&om_nextpage=true",
		"paid": false,
		"type": "web",
		"sources": [{
			"name": "bing",
			"position": 6,
			"provider": "BingAds"
		}]
	}, {
		"display_url": "en.wikipedia.org/wiki/<strong>Airlines</strong>",
		"title": "Airline - Wikipedia",
		"description": "An airline is a company that provides air transport services for traveling passengers and freight. <strong>Airlines</strong> utilize aircraft to supply these services and may form ...",
		"url": "http://ccs.infospace.com/ClickHandler.ashx?encp=ld%3d20170830%26app%3d1%26c%3ddogpl.100%26s%3ddogpilesem%26rc%3ddogpl.300%26dc%3d%26euip%3d104.132.11.74%26pvaid%3de6a8799486614194bae5467d76ce1d31%26dt%3dDesktop%26fct.uid%3ddddaea275d7e4d759eb57b7755b44a37%26en%3d352GU4fR56WY6dtc5jlLFS1qfqwkvnZ3WLV07iuIzB20xQ26pTFYPQ%253d%253d%26coi%3d1494%26npp%3d0%26p%3d0%26pp%3d0%26mid%3d9%26ep%3d7%26ru%3dhttps%253a%252f%252fen.wikipedia.org%252fwiki%252fAirlines%26du%3dhttps%253a%252f%252fen.wikipedia.org%252fwiki%252fAirlines%26hash%3dD603D85EF183BDFED99D81D7054B7FB8&ap=0&cop=main-title&om_userid=WuWG1m1lIw1lbevx1l4I&om_sessionid=GMlva6OKEexxdZ4T3hX7&om_pageid=XygfQ04Q6uehLcmXWrKW&om_nextpage=true",
		"paid": false,
		"type": "web",
		"sources": [{
			"name": "bing",
			"position": 7,
			"provider": "BingAds"
		}]
	}, {
		"display_url": "www.united.com/ual",
		"title": "United <strong>Airlines</strong> – Airline Tickets, Travel Deals and Flights",
		"description": "Find the latest travel deals on flights, hotels and rental cars. Book airline tickets and MileagePlus award tickets to worldwide destinations.",
		"url": "http://ccs.infospace.com/ClickHandler.ashx?encp=ld%3d20170830%26app%3d1%26c%3ddogpl.100%26s%3ddogpilesem%26rc%3ddogpl.300%26dc%3d%26euip%3d104.132.11.74%26pvaid%3de6a8799486614194bae5467d76ce1d31%26dt%3dDesktop%26fct.uid%3ddddaea275d7e4d759eb57b7755b44a37%26en%3d352GU4fR56WY6dtc5jlLFS1qfqwkvnZ3WLV07iuIzB20xQ26pTFYPQ%253d%253d%26coi%3d1494%26npp%3d0%26p%3d0%26pp%3d0%26mid%3d9%26ep%3d8%26ru%3dhttps%253a%252f%252fwww.united.com%252fual%252fen%252fus%252f%26du%3dhttps%253a%252f%252fwww.united.com%252fual%26hash%3dBEFE9685A57992C542264658E72058A7&ap=0&cop=main-title&om_userid=WuWG1m1lIw1lbevx1l4I&om_sessionid=GMlva6OKEexxdZ4T3hX7&om_pageid=XygfQ04Q6uehLcmXWrKW&om_nextpage=true",
		"paid": false,
		"type": "web",
		"sources": [{
			"name": "bing",
			"position": 8,
			"provider": "BingAds"
		}]
	}, {
		"display_url": "www.spirit.com",
		"title": "Spirit <strong>Airlines</strong> - Official Site",
		"description": "Spirit <strong>Airlines</strong> is the leading Ultra Low Cost Carrier in the United States, the Caribbean, the Bahamas and Latin America. Serving 39+ destinations, we liberate you ...",
		"url": "http://ccs.infospace.com/ClickHandler.ashx?encp=ld%3d20170830%26app%3d1%26c%3ddogpl.100%26s%3ddogpilesem%26rc%3ddogpl.300%26dc%3d%26euip%3d104.132.11.74%26pvaid%3de6a8799486614194bae5467d76ce1d31%26dt%3dDesktop%26fct.uid%3ddddaea275d7e4d759eb57b7755b44a37%26en%3d352GU4fR56WY6dtc5jlLFS1qfqwkvnZ3WLV07iuIzB20xQ26pTFYPQ%253d%253d%26coi%3d1494%26npp%3d0%26p%3d0%26pp%3d0%26mid%3d9%26ep%3d9%26ru%3dhttp%253a%252f%252fwww.spirit.com%252f%26du%3dwww.spirit.com%26hash%3d5AFBB9DC98A28859FEBEFC2C2069E9A7&ap=0&cop=main-title&om_userid=WuWG1m1lIw1lbevx1l4I&om_sessionid=GMlva6OKEexxdZ4T3hX7&om_pageid=XygfQ04Q6uehLcmXWrKW&om_nextpage=true",
		"paid": false,
		"type": "web",
		"sources": [{
			"name": "bing",
			"position": 9,
			"provider": "BingAds"
		}]
	}, {
		"display_url": "www.jetblue.com/",
		"title": "JetBlue - Official Site",
		"description": "JetBlue offers flights to 90+ destinations with free inflight entertainment, free brand-name snacks and drinks, lots of legroom and award-winning service.",
		"url": "http://ccs.infospace.com/ClickHandler.ashx?encp=ld%3d20170830%26app%3d1%26c%3ddogpl.100%26s%3ddogpilesem%26rc%3ddogpl.300%26dc%3d%26euip%3d104.132.11.74%26pvaid%3de6a8799486614194bae5467d76ce1d31%26dt%3dDesktop%26fct.uid%3ddddaea275d7e4d759eb57b7755b44a37%26en%3d352GU4fR56WY6dtc5jlLFS1qfqwkvnZ3WLV07iuIzB20xQ26pTFYPQ%253d%253d%26coi%3d1494%26npp%3d0%26p%3d0%26pp%3d0%26mid%3d9%26ep%3d10%26ru%3dhttps%253a%252f%252fwww.jetblue.com%252f%26du%3dhttps%253a%252f%252fwww.jetblue.com%26hash%3dCA1D6A0BC7247F18DFDDD712354D2647&ap=0&cop=main-title&om_userid=WuWG1m1lIw1lbevx1l4I&om_sessionid=GMlva6OKEexxdZ4T3hX7&om_pageid=XygfQ04Q6uehLcmXWrKW&om_nextpage=true",
		"paid": false,
		"type": "web",
		"sources": [{
			"name": "bing",
			"position": 10,
			"provider": "BingAds"
		}]
	}]
}

class GetBingData(Resource):
    def get(self):
        sleep(0.4)
        return bingdata

api.add_resource(GetBingData, '/')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
