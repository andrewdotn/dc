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
            'xls_url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['chart']

CHART_DATA = [{
 "title": "US Taxes as Percentage of Personal Income",
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
 "sparkblocks": "▇▆▅▅▃▃▃▃▂▁",
 "tweet": "tweet",
 "source_url": "http://blog.datacollective.org/?page_id=61",
 "source_title": "Hacking Education Data Analysis Submission: Tips For Success, By the Numbers",
 "source_detail": "Let’s take the ~300,000 projects posted on DonorsChoose.org, sort them by the project cost and divide them into 10 equally-sized groups of about 30,000 projects each.  Then for each group, let’s plot its average project size and the % of projects in that group that were completed.",
 "csv_url": "csv",
 "xls_url": "xls",
 "chart_creator": "David Joerg",
 "chart_creator_avatar": "http://a3.twimg.com/profile_images/1392074933/dj7_bigger.png",
 "chart_creator_detail": "Banned from Ogame until 2033.",
 "disqus_identifier": "donorschoose_completion_vs_size",
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
 "sparkblocks": "▁▁▁▁▁▁▂▃▅▇",
 "tweet": "US Consumer Price Index 1774-2010",
 "source_url": "http://www.measuringworth.com/datasets/uscpi/",
 "source_title": "MeasuringWorth.com The Annual Consumer Price Index for the United States, 1774 -2010",
 "source_detail": "For further discussion of the limitations of the CPI, and for detailed exposition of development of this CPI series, please read <a target=\"_blank\" href=\"http://www.measuringworth.com/docs/cpistudyrev.pdf\">What Was the Consumer Price Index Then? A Data Study (349K PDF)</a>.",
 "csv_url": "csv",
 "xls_url": "xls",
 "chart_creator": "David Joerg",
 "chart_creator_avatar": "http://a3.twimg.com/profile_images/1392074933/dj7_bigger.png",
 "chart_creator_detail": "David Joerg",
 "disqus_identifier": "mw_inflation",
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
"""}
]
