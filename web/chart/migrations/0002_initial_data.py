# encoding: utf-8
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        for d in CHART_DATA:
            chart = orm.Chart(**d)
            chart.save()

    def backwards(self, orm):
        pass

    models = {
        'chart.chart': {
            'Meta': {'object_name': 'Chart'},
            'chart_creator': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'chart_creator_avatar': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'chart_creator_detail': ('django.db.models.fields.TextField', [], {}),
            'chart_data': ('django.db.models.fields.TextField', [], {}),
            'chart_settings': ('django.db.models.fields.TextField', [], {}),
            'disqus_identifier': ('django.db.models.fields.TextField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'source_detail': ('django.db.models.fields.TextField', [], {}),
            'source_title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'source_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'sparkblocks': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'tweet': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'csv_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'xls_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'html_below_title': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'y_axis_description': ('django.db.models.fields.TextField', [], {'max_length': '255', 'null': 'True'})
        }
    }

    complete_apps = ['chart']

CHART_DATA = [{
 "title": "US Taxes as Percentage of Personal Income",
  "y_axis_description": "",
 "sparkblocks": "▃▃▃▅▆▆▆▆▅▇▆▅▁",
 "tweet": "US Taxes as Percentage of Percentage Income, 1929-2009: d4t4.org/▁▂▆▆▆▇▇▇▇▇▅ low 1.4% high 14.4%",
 "source_url": "http://www.bea.gov/iTable/index_nipa.cfm",
 "source_title": "US Bureau of Economic Analysis",
 "source_detail": r"""Tax data is from <a href="http://www.bea.gov/national/nipaweb/TableView.asp?SelectedTable=89&Freq=Year&FirstYear=1&LastYear=2100" target="_blank">Table 3.4, Personal Current Tax Receipts</a>, last Revised on August 05, 2010. The breakdown of state and local tax is into Income, Property, Motor vehicle, and “other”, mainly hunting and fishing licences; not state and then local.
            <p>
            Personal income is from <a target="_blank" href="http://www.bea.gov/national/nipaweb/TableView.asp?SelectedTable=58&Freq=Year&FirstYear=1&LastYear=2100">Table 2.1. Personal Income and Its Disposition</a>, last Revised on May 26, 2011 - Next Release Date June 24, 2011. It doesn’t give federal vs. state/local breakdown, but does give the total amount which agrees with that computed from Table 3.4, though it includes data for 2010 which is not in the latest Table 3.4 data.
            <p>
            Data was downloaded on June 22, 2011 into this <a target="_blank" href="https://spreadsheets.google.com/spreadsheet/ccc?key=0AkpTmG7ijJvXdEVCMkRULUEya2VJbnM0ci1DbTZ3WUE&hl=en_US">Google spreadsheet</a> and then posted here.""",
 "csv_url": "/static/files/taxpercent.csv",
 "xls_url": "xls",
 "short_name": "taxpercent",
 "chart_creator": "Andrew Neitsch",
 "chart_creator_avatar": "http://www.gravatar.com/avatar/dc87?d=identicon",
 "chart_creator_detail": r"""2 charts posted<br>
            3 articles on the web include Andrew's charts <br>
            5 likes from 2 people <br>
            10 comments written <br>
            15 people follow Andrew <br>
            Andrew follows 8 people <br>
            <br>
            Andrew joined The Data Collective on June 18, 2011.""",
 "disqus_identifier": "taxpercent",
 "chart_data": r"""
{
  name: "Federal",
  data: [0.014134276,0.013140604,0.007668712,0.006012024,0.008547009,0.009310987,0.009950249,0.010204082,0.01754386,0.01754386,0.012345679,0.012755102,0.016666667,0.034035656,0.105193951,0.101807229,0.108391608,0.091825308,0.09848088,0.086313782,0.074396135,0.076015727,0.098487786,0.109738372,0.107302023,0.095480802,0.096518987,0.099852725,0.10041841,0.096232041,0.098139179,0.101628981,0.099580224,0.101884312,0.102398332,0.08944196,0.091989199,0.097052004,0.099367382,0.107348602,0.117820892,0.106010017,0.09500609,0.103566391,0.098694282,0.103459557,0.090418758,0.095748288,0.099356815,0.102847498,0.109055596,0.10862481,0.112535337,0.106621368,0.096944651,0.09220227,0.0960906,0.09469697,0.100015289,0.09519758,0.099067471,0.096993831,0.091682401,0.088867279,0.090785007,0.092343569,0.094470158,0.100628072,0.106303655,0.109655301,0.112883653,0.116316564,0.111647698,0.091455944,0.082554035,0.080425069,0.088871723,0.093174537,0.097848442,0.088999362,0.070037536]
					},
                                        {
						name: "State and Local",
						data: [0.007067138,0.006570302,0.007668712,0.008016032,0.008547009,0.00744879,0.008291874,0.008746356,0.008097166,0.00877193,0.008230453,0.008928571,0.007291667,0.005672609,0.005259698,0.004819277,0.004662005,0.005039194,0.005238345,0.005245589,0.006763285,0.00655308,0.006591702,0.006540698,0.006513541,0.007135576,0.007594937,0.007952872,0.008089261,0.008403361,0.009686464,0.010211524,0.010727612,0.010955302,0.011261731,0.011860782,0.011881188,0.012918185,0.013269557,0.014893916,0.0164461,0.016932984,0.017606024,0.021055813,0.020531292,0.020037622,0.020151322,0.021089035,0.021684533,0.022050417,0.021364409,0.021247013,0.021143941,0.021360416,0.022390082,0.023249411,0.023279092,0.023593074,0.024615228,0.02413027,0.025145365,0.025295562,0.02490311,0.025302489,0.025340781,0.025192347,0.025496299,0.025593179,0.0259974,0.02673612,0.02711483,0.027653808,0.027354699,0.024480966,0.024120024,0.025017107,0.026387816,0.026845697,0.027123226,0.027067815,0.02359773]
					},
                                        {
						name: "Total",
						data: [0.021201413,0.019710907,0.015337423,0.014028056,0.017094017,0.016759777,0.018242123,0.018950437,0.025641026,0.026315789,0.020576132,0.021683673,0.023958333,0.039708266,0.110453649,0.106626506,0.113053613,0.096864502,0.103719225,0.091559371,0.08115942,0.082568807,0.105079488,0.11627907,0.113815564,0.102616378,0.104113924,0.107805596,0.108507671,0.104635403,0.107825644,0.111840506,0.110307836,0.112839614,0.113660063,0.101302742,0.103870387,0.109970189,0.112636939,0.122242518,0.134266992,0.122943,0.112612114,0.124622204,0.119225574,0.123497178,0.11057008,0.116837323,0.121041348,0.124897915,0.130420005,0.129871823,0.133679278,0.127981784,0.119334733,0.115451681,0.119369691,0.118290043,0.124630517,0.11932785,0.124212836,0.122289393,0.116585511,0.114169768,0.116125788,0.117535916,0.119966456,0.126221251,0.132301056,0.136391421,0.139998483,0.143970372,0.139002398,0.11593691,0.10667406,0.105442177,0.115259539,0.120020234,0.124971668,0.116067177,0.093635266]
					},
""",
 "chart_settings": r"""
					title: {
						text: ''
					},
					xAxis: {
						labels: {
							formatter: function() {
								return this.value; // clean, unformatted number for year
							}
						}							
					},
					yAxis: {
			                        min: 0,
						title: {
							text: '% of Personal Income'
						},
						labels: {
							formatter: function() {
								return this.value*100.0 +'%';
							}
						}
					},
					tooltip: {
						formatter: function() {
							return this.series.name +' Taxes were <b>'+
								Highcharts.numberFormat(this.y * 100.0, 1) +'%</b><br/>of Personal Income in '+ this.x;
						}
					},
					plotOptions: {
						line: {
							pointStart: 1929,
							marker: {
								enabled: false,
								symbol: 'circle',
								states: {
									hover: {
										enabled: true
									}
								}
							}
						}
					},
"""},
{ "title": "DonorsChoose.org Project Completion Rate vs Project Size",
  "y_axis_description": "",
 "sparkblocks": "▇▆▅▅▃▃▃▃▂▁",
 "tweet": "tweet",
 "source_url": "http://blog.datacollective.org/?page_id=61",
 "source_title": "Hacking Education Data Analysis Submission: Tips For Success, By the Numbers",
 "source_detail": "Let’s take the ~300,000 projects posted on DonorsChoose.org, sort them by the project cost and divide them into 10 equally-sized groups of about 30,000 projects each.  Then for each group, let’s plot its average project size and the % of projects in that group that were completed.",
 "csv_url": "csv",
 "xls_url": "xls",
 "short_name": "dc_completion_vs_size",
 "chart_creator": "David Joerg",
 "chart_creator_avatar": "http://a3.twimg.com/profile_images/1392074933/dj7_bigger.png",
 "chart_creator_detail": """
Data Collective co-founder.<br>
Interested in: how numbers explain the world, coding awesomeness, fun things, unicode abuse.  In real life: <a href="http://about.me/dsjoerg">http://about.me/dsjoerg</a>.
""",
 "disqus_identifier": "dc_completion_vs_size",
 "chart_data": r"""
{
  name: "Completion Rate",
  data: [[165.14,0.90],
         [233.00,0.79],
         [297.28,0.74],
         [365.11,0.70],
         [430.58,0.65],
         [497.22,0.64],
         [555.07,0.61],
         [652.44,0.57],
         [866.08,0.51],
         [1877.03,0.43]]
}
""",
 "chart_settings": r"""
					title: { text: '' },
					xAxis: { title: { text: 'Project Size' } },
                                        yAxis: { title: { text: 'Completion Rate' } },
                                        legend: { enabled: false },
"""},
{ "title": "United States Consumer Price Index",
  "y_axis_description": "",
 "sparkblocks": "▁▁▁▁▁▁▂▃▅▇",
 "tweet": "US Consumer Price Index 1774-2010",
 "source_url": "http://www.measuringworth.com/datasets/uscpi/",
 "source_title": "MeasuringWorth.com The Annual Consumer Price Index for the United States, 1774 -2010",
 "source_detail": "For further discussion of the limitations of the CPI, and for detailed exposition of development of this CPI series, please read <a target=\"_blank\" href=\"http://www.measuringworth.com/docs/cpistudyrev.pdf\">What Was the Consumer Price Index Then? A Data Study (349K PDF)</a>.",
 "csv_url": "csv",
 "xls_url": "xls",
 "short_name": "us_cpi",
 "chart_creator": "David Joerg",
 "chart_creator_avatar": "http://a3.twimg.com/profile_images/1392074933/dj7_bigger.png",
 "chart_creator_detail": "David Joerg",
 "disqus_identifier": "mw_us_cpi",
 "chart_data": r"""
{
  name: "CPI",
  data: [ 7.82, 7.41, 8.46, 10.31, 13.38, 11.84, 13.29, 10.72, 11.76, 10.31, 9.91, 9.43, 9.19, 9.02, 8.62, 8.54, 8.86, 9.1, 9.27, 9.59, 10.64, 12.17, 12.81, 12.33, 11.92, 11.92, 12.17, 12.33, 10.39, 10.96, 11.44, 11.36, 11.84, 11.2, 12.17, 11.92, 11.92, 12.73, 12.89, 15.47, 17., 14.91, 13.62, 12.89, 12.33, 12.33, 11.36, 10.96, 11.36, 10.15, 9.35, 9.59, 9.59, 9.67, 9.19, 9.02, 8.94, 8.38, 8.3, 8.14, 8.3, 8.54, 9.02, 9.27, 9.02, 9.02, 8.38, 8.46, 7.9, 7.17, 7.25, 7.33, 7.41, 7.98, 7.65, 7.41, 7.57, 7.41, 7.49, 7.49, 8.14, 8.38, 8.22, 8.46, 7.98, 8.06, 8.06, 8.54, 9.75, 12.17, 15.23, 15.79, 15.39, 14.34, 13.78, 13.21, 12.65, 11.84, 11.84, 11.6, 11.04, 10.64, 10.39, 10.15, 9.67, 9.67, 9.91, 9.91, 9.91, 9.71, 9.51, 9.32, 9.12, 9.22, 9.22, 8.92, 8.82, 8.82, 8.82, 8.72, 8.34, 8.14, 8.14, 8.04, 8.04, 8.04, 8.14, 8.24, 8.34, 8.53, 8.63, 8.53, 8.72, 9.11, 8.92, 8.82, 9.21, 9.21, 9.4, 9.6, 9.69, 9.74, 10.64, 12.82, 15.06, 17.3, 20.04, 17.9, 16.77, 17.07, 17.1, 17.53, 17.7, 17.37, 17.13, 17.13, 16.7, 15.23, 13.66, 12.96, 13.39, 13.73, 13.86, 14.36, 14.09, 13.89, 14.03, 14.73, 16.3, 17.3, 17.6, 18., 19.54, 22.34, 24.08, 23.85, 24.08, 25.98, 26.55, 26.75, 26.88, 26.78, 27.18, 28.15, 28.92, 29.16, 29.62, 29.92, 30.26, 30.62, 31.03, 31.56, 32.46, 33.4, 34.8, 36.67, 38.84, 40.51, 41.85, 44.45, 49.33, 53.84, 56.94, 60.61, 65.22, 72.57, 82.38, 90.93, 96.5, 99.6, 103.9, 107.6, 109.6, 113.6, 118.3, 124., 130.7, 136.2, 140.3, 144.5, 148.2, 152.4, 156.9, 160.5, 163., 166.6, 172.2, 177.1, 179.9, 184., 188.9, 195.3, 201.6, 207.34, 215.3, 214.54, 218.06 ]
}
""",
 "chart_settings": r"""
					title: { text: '' },
                                          // clean, unformatted number for year
					xAxis: { labels: { formatter: function() { return this.value; } } },
                                        yAxis: { min: 0, title: { text: 'US CPI' } },
                                        legend: { enabled: false },
                                        plotOptions: { line: { pointStart: 1774, marker: { enabled: false } } },
"""},
{ "title": "Spending on Medicaid as a Percentage of Gross Domestic Product, 1966-2009",
  "y_axis_description": "",
 "sparkblocks": "▁▂▂▃▃▅▆▇▇",
 "tweet": "Medicaid spending vs GDP 1966-2009",
 "source_url": "(deprecated field)",
 "source_title": "data from Centers for Medicare and Medicaid Services and Bureau of Economic Analysis",
 "source_detail": """
<a href="http://www.cms.gov/NationalHealthExpendData/downloads/nhe2009.zip" target="_blank">Medicaid spending data</a> comes from <a href="http://www.cms.gov/NationalHealthExpendData/02_NationalHealthAccountsHistorical.asp" target="_blank">this page</a> at the website of the Centers for Medicare and Medicaid Services,
which is part of the US Department of Health and Human Services.</p>
<p><a href="http://bea.gov/national/xls/gdplev.xls" target="_blank">GDP data</a> comes from <a href="http://bea.gov/national/index.htm#gdp" target="_blank">this page</a> at the website of the Bureau of Economic Analysis, which is part of the US Department of Commerce.</p>
<p>Data was downloaded on March 16, 2011 into this <a target="_blank" href="https://spreadsheets1.google.com/spreadsheet/ccc?hl=en&key=t9I-YHnO6bEza7hsE7bU5jQ&hl=en#gid=2">Google spreadsheet</a> and then posted here.</p>
""",
 "csv_url": "/static/files/medicaid.csv",
 "xls_url": "xls",
 "short_name": "medicaid_vs_gdp",
 "chart_creator": "David Joerg",
 "chart_creator_avatar": "http://a3.twimg.com/profile_images/1392074933/dj7_bigger.png",
 "chart_creator_detail": """
2 charts posted<br>
3 articles on the web include David's charts <br>
5 likes from 2 people <br>
10 comments written <br>
15 people follow David <br>
David follows 8 people <br>
""",
 "disqus_identifier": "medicaid",
 "chart_data": r"""
                                        {
						name: 'Federal',
						data: [0.080182811,0.183145123,0.201670697,0.233401056,0.273745546,0.338090167,0.36733985,0.356876221,0.418586195,0.452378335,0.501633235,0.487443968,0.476004883,0.495874639,0.520831391,0.540559038,0.548463052,0.554153228,0.536681167,0.535720213,0.564720522,0.588385694,0.607693514,0.639838748,0.734543574,0.948704127,1.081651767,1.154291028,1.143956416,1.159123093,1.162194297,1.139564831,1.122152726,1.145830972,1.174877154,1.286610216,1.365651222,1.445893503,1.45431588,1.405711166,1.300243304,1.324402993,1.408805701,1.749298817]
					},
                                        {
						name: 'State and Local',
						data: [0.085349752,0.194185488,0.187568696,0.190664364,0.235702591,0.256096912,0.304241053,0.324842654,0.31987996,0.368626733,0.33079031,0.372794444,0.372595693,0.375720084,0.412868979,0.428716259,0.4355158,0.443574945,0.435948511,0.434935388,0.452814959,0.474429947,0.472221787,0.490244614,0.535362469,0.606859031,0.624141084,0.681108078,0.753154463,0.794593173,0.779117178,0.790832173,0.800262694,0.815671139,0.839699543,0.894411931,0.966677316,0.972367866,0.999373936,1.043568015,0.991996358,1.000700479,0.979110731,0.899193994]
					},
                                        {
						name: 'Total',
						data: [0.165532563,0.37733061,0.389239393,0.424065421,0.509457768,0.594187078,0.671580903,0.681718874,0.738466155,0.821005068,0.832423545,0.860238412,0.848600575,0.871594723,0.933700369,0.969275297,0.983978852,0.997725344,0.972629678,0.970655602,1.017535481,1.062815641,1.079915301,1.130083362,1.269904319,1.555563158,1.705791274,1.835397606,1.897110879,1.953716266,1.941311475,1.930397004,1.92241542,1.961502112,2.014575692,2.181022146,2.332328538,2.418261369,2.453689816,2.449279181,2.292239661,2.325103472,2.387916432,2.648492811]
					},
""",
 "chart_settings": r"""
					title: {
						text: ''
					},
					xAxis: {
						labels: {
							formatter: function() {
								return this.value; // clean, unformatted number for year
							}
						}							
					},
					yAxis: {
			                        min: 0,
						title: {
							text: 'Medicaid Spending, % GDP'
						},
						labels: {
							formatter: function() {
								return this.value +'%';
							}
						}
					},
					tooltip: {
						formatter: function() {
							return this.series.name +' spending was <b>'+
								Highcharts.numberFormat(this.y, 1) +'%</b><br/>of GDP in '+ this.x;
						}
					},
					plotOptions: {
						line: {
							pointStart: 1966,
							marker: {
								enabled: false,
								symbol: 'circle',
								states: {
									hover: {
										enabled: true
									}
								}
							}
						}
					},
"""},
{ "title": "Federal Spending Did Not Grow Ten Times Faster Than Personal Income",
  "html_below_title": "What really happened: both total federal spending and total personal income grew at <i>similar</i> rates until 2009, when the recession caused personal income to shrink, while federal spending grew sharply.  The Heritage Foundation's <a target='_blank' href='http://www.heritage.org/budgetchartbook/charts/2011/growth-federal-spending-600.jpg'>chart</a> makes a misleading comparison by showing median household income, which ignores the growing <i>number</i> of households that have shared the Federal spending burden.",
  "y_axis_description": "PERCENT CHANGE OF INFLATION-ADJUSTED DOLLARS",
 "sparkblocks": "▁▂▂▃▃▅▆▇▇▇",
 "tweet": "US Federal Spending vs Total Personal Income",
 "source_url": "(deprecated field)",
 "source_title": "Office of Management and Budget, Bureau of Economic Analysis and Bureau of Labor Statistics",
 "source_detail": """
<a href="http://www.whitehouse.gov/sites/default/files/omb/budget/fy2012/assets/hist01z1.xls" target="_blank">Federal spending data</a> comes from <a href="http://www.whitehouse.gov/omb/budget/Historicals" target="_blank">this page</a> at the website of the Offices of Management and Budget,
which is part of the US Executive Branch.</p>
<p>
Total personal income is from <a target="_blank" href="http://www.bea.gov/national/nipaweb/TableView.asp?SelectedTable=58&Freq=Year&FirstYear=1&LastYear=2100">Table 2.1. Personal Income and Its Disposition</a> at the website of the Bureau of Economic Analysis, which is part of the US Department of Commerce.</p>
<p>Inflation data comes from <a target="_blank" href="http://data.bls.gov/timeseries/CUUR0000SA0?from_year=0">this page</a> at the Bureau of Labor and Statistics which is part of the US Department of Labor.
</p>
<p>Data was downloaded on July 15, 2011 into this <a target="_blank" href="https://spreadsheets.google.com/spreadsheet/ccc?key=0AtrXvCHP3uxcdFFQOW43WGM5Q2k0TGtMclo5bzR0ZGc&hl=en_US">Google spreadsheet</a> and then posted here.
""",
 "csv_url": "csv",
 "xls_url": "xls",
 "short_name": "fedspending_vs_income",
 "chart_creator": "David Joerg",
 "chart_creator_avatar": "http://a3.twimg.com/profile_images/1392074933/dj7_bigger.png",
 "chart_creator_detail": """
2 charts posted<br>
3 articles on the web include David's charts <br>
5 likes from 2 people <br>
10 comments written <br>
15 people follow David <br>
David follows 8 people <br>
""",
 "disqus_identifier": "fedspending",
 "chart_data": r"""
                                        {
						name: 'Total Federal Spending',
						data: [0.02024847,0.084386671,0.114351232,0.116759721,0.232391247,0.291931289,0.351490601,0.41809864,0.425765583,0.467501971,0.506187206,0.527888493,0.596916752,0.615028417,0.733048595,0.745847686,0.744417547,0.777428758,0.824731012,0.900175572,0.900777218,0.932771418,0.909521686,0.931704932,0.948410546,0.952658029,0.94431571,0.975619212,1.00122464,1.047575515,1.055440809,1.193738133,1.296638725,1.39192261,1.504403985,1.586807773,1.604491184,1.729945275,2.218795894,2.081639342]
					},
                                        {
						name: 'Total Personal Income',
						data: [0.022797628,0.088602659,0.17502175,0.182690034,0.154909494,0.195544733,0.257865674,0.32463172,0.359183314,0.333424173,0.337902251,0.322522338,0.36064197,0.445987015,0.493973368,0.520051668,0.590762782,0.648417198,0.696365674,0.714800701,0.684959082,0.745331043,0.760047719,0.811267754,0.859656313,0.924334167,0.983390503,1.099061555,1.170300064,1.285639969,1.286783894,1.305957888,1.326466878,1.418577399,1.478517333,1.561326366,1.652697485,1.646060186,1.599115964,1.60877277]
					},
""",
 "chart_settings": r"""
					title: {
						text: ''
					},
                                        legend: { enabled: false },
                                        labels: {
                                                items: [
                                                  {
                                                   html: "Total Federal Spending",
                                                   style: { left: "170px", top: "200px" }
                                                  },
                                                  {
                                                   html: "Total Personal Income",
                                                   style: { left: "245px", top: "275px" }
                                                  },
                                                  {
                                                   html: "",
                                                   style: { left: "10px", top: "10px", width: "400px", fontFamily:"OpenSansBold", fontSize:"16px", backgroundColor:"white" }
//                                                   style: { left: "10px", top: "10px", width: "400px", fontFamily:"OpenSansBold", fontSize:"20px" }
                                                  },
                                                ],
                                                style: { fontFamily:"ChunkFiveRegular" }
                                        },
					xAxis: {
						labels: {
							formatter: function() {
								return this.value; // clean, unformatted number for year
							},
                                                        style: { fontFamily:"ChunkFiveRegular" }
						},
                                                tickPixelInterval: 100
					},
					yAxis: {
			                        min: 0,
						title: {
							text: ''
						},
						labels: {
							formatter: function() {
								return this.value*100.0 +'%';
							},
                                                        style: { fontFamily:"ChunkFiveRegular" }
						}
					},
					tooltip: {
						formatter: function() {
							return this.series.name +' was<b>'+
								Highcharts.numberFormat(this.y*100.0, 1) +'%</b> higher in '+ this.x +' than in 1970, in inflation-adjusted dollars';
						},
                                                style: { fontFamily:"Georgia" }
					},
					plotOptions: {
						line: {
							pointStart: 1971,
                                                        lineWidth: 5,
							marker: {
								enabled: false,
								symbol: 'circle',
								states: {
									hover: {
										enabled: true
									}
								}
							}
						}
					},
"""}
]
