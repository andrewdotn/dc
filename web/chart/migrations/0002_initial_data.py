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
            'tweet': ('django.db.models.fields.CharField', [], {'max_length': '140'})
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
 "chart_settings": r"""<settings>
<skip_rows>0</skip_rows>
<csv_separator>,</csv_separator>
<legend>
<align>right</align>
</legend>
<hide_bullets_count>18</hide_bullets_count>
<data_type>csv</data_type>
<plot_area>
<margins><left>50</left><right>40</right><top>55</top><bottom>30</bottom></margins>
</plot_area>
<grid><x><alpha>5</alpha><approx_count>8</approx_count></x>
    <y_left><alpha>5</alpha></y_left>
</grid>
<axes><x><width>1</width><color>cccccc</color></x><y_left><width>1</width><color>cccccc</color></y_left></axes>
<scroller>
<enabled>0</enabled>
</scroller>
<indicator>
<color>0D8ECF</color>
<x_balloon_text_color>FFFFFF</x_balloon_text_color>
<line_alpha>50</line_alpha>
<selection_color>0D8ECF</selection_color>
<selection_alpha>20</selection_alpha>
</indicator>
<zoom_out_button><text_color_hover>FF0F00</text_color_hover></zoom_out_button>
<help><button><color>FCD202</color><text_color>000000</text_color><text_color_hover>FF0F00</text_color_hover></button>
    <balloon><color>FCD202</color><text_color>000000</text_color></balloon>
</help>
<graphs>
<graph gid='0'>
<title>Federal</title>
<color>B8460D</color><color_hover>FF0F00</color_hover>
<fill_alpha>10</fill_alpha>
</graph>
<graph gid='1'>
<title>State and Local</title>
<color>FFD135</color><color_hover>FF0F00</color_hover>
<line_width>1</line_width>
<fill_alpha>10</fill_alpha>
<bullet>round</bullet>
</graph>
<graph gid='2'>
<title>Total</title>
<color>0F543D</color><color_hover>FF0F00</color_hover>
<line_width>2</line_width>
<fill_alpha>10</fill_alpha>
<bullet>round</bullet>
</graph>
</graphs>
</settings>"""},
{ "title": "DonorsChoose.org Project Completion Rate vs Project Size",
 "sparkblocks": "▇▆▅▅▃▃▃▃▂▁",
 "tweet": "tweet",
 "source_url": "http://blog.datacollective.org/?page_id=61",
 "source_title": "Hacking Education Data Analysis Submission: Tips For Success, By the Numbers",
 "source_detail": "Let’s take the ~300,000 projects posted on DonorsChoose.org, sort them by the project cost and divide them into 10 equally-sized groups of about 30,000 projects each.  Then for each group, let’s plot its average project size and the % of projects in that group that were completed.",
 "chart_creator": "David Joerg",
 "chart_creator_avatar": "http://a3.twimg.com/profile_images/1392074933/dj7_bigger.png",
 "chart_creator_detail": "Banned from Ogame until 2033.",
 "disqus_identifier": "donorschoose_completion_vs_size",
 "chart_data": r"""165.14,0.90
233.00,0.79
297.28,0.74
365.11,0.70
430.58,0.65
497.22,0.64
555.07,0.61
652.44,0.57
866.08,0.51
1877.03,0.43""",
 "chart_settings": r"""<settings>
<skip_rows>0</skip_rows>
<csv_separator>,</csv_separator>
<legend>
<align>right</align>
</legend>
<hide_bullets_count>18</hide_bullets_count>
<data_type>csv</data_type>
<plot_area>
<margins><left>50</left><right>40</right><top>55</top><bottom>30</bottom></margins>
</plot_area>
<grid><x><alpha>5</alpha><approx_count>8</approx_count></x>
    <y_left><alpha>5</alpha></y_left>
</grid>
<axes><x><width>1</width><color>cccccc</color></x><y_left><width>1</width><color>cccccc</color></y_left></axes>
<scroller>
<enabled>0</enabled>
</scroller>
<indicator>
<color>0D8ECF</color>
<x_balloon_text_color>FFFFFF</x_balloon_text_color>
<line_alpha>50</line_alpha>
<selection_color>0D8ECF</selection_color>
<selection_alpha>20</selection_alpha>
</indicator>
<zoom_out_button><text_color_hover>FF0F00</text_color_hover></zoom_out_button>
<help><button><color>FCD202</color><text_color>000000</text_color><text_color_hover>FF0F00</text_color_hover></button>
    <balloon><color>FCD202</color><text_color>000000</text_color></balloon>
</help>
<graphs>
<graph gid='0'>
<title>Federal</title>
<color>B8460D</color><color_hover>FF0F00</color_hover>
<fill_alpha>10</fill_alpha>
</graph>
</graphs>
</settings>"""},
{ "title": "United States Consumer Price Index",
 "sparkblocks": "▁▁▁▁▁▁▂▃▅▇",
 "tweet": "US Consumer Price Index 1774-2010",
 "source_url": "http://www.measuringworth.com/datasets/uscpi/",
 "source_title": "MeasuringWorth.com The Annual Consumer Price Index for the United States, 1774 -2010",
 "source_detail": "For further discussion of the limitations of the CPI, and for detailed exposition of development of this CPI series, please read <a target=\"_blank\" href=\"http://www.measuringworth.com/docs/cpistudyrev.pdf\">What Was the Consumer Price Index Then? A Data Study (349K PDF)</a>.",
 "chart_creator": "David Joerg",
 "chart_creator_avatar": "http://a3.twimg.com/profile_images/1392074933/dj7_bigger.png",
 "chart_creator_detail": "David Joerg",
 "disqus_identifier": "mw_inflation",
 "chart_data": r"""1774,7.82
1775,7.41
1776,8.46
1777,10.31
1778,13.38
1779,11.84
1780,13.29
1781,10.72
1782,11.76
1783,10.31
1784,9.91
1785,9.43
1786,9.19
1787,9.02
1788,8.62
1789,8.54
1790,8.86
1791,9.1
1792,9.27
1793,9.59
1794,10.64
1795,12.17
1796,12.81
1797,12.33
1798,11.92
1799,11.92
1800,12.17
1801,12.33
1802,10.39
1803,10.96
1804,11.44
1805,11.36
1806,11.84
1807,11.2
1808,12.17
1809,11.92
1810,11.92
1811,12.73
1812,12.89
1813,15.47
1814,17
1815,14.91
1816,13.62
1817,12.89
1818,12.33
1819,12.33
1820,11.36
1821,10.96
1822,11.36
1823,10.15
1824,9.35
1825,9.59
1826,9.59
1827,9.67
1828,9.19
1829,9.02
1830,8.94
1831,8.38
1832,8.3
1833,8.14
1834,8.3
1835,8.54
1836,9.02
1837,9.27
1838,9.02
1839,9.02
1840,8.38
1841,8.46
1842,7.9
1843,7.17
1844,7.25
1845,7.33
1846,7.41
1847,7.98
1848,7.65
1849,7.41
1850,7.57
1851,7.41
1852,7.49
1853,7.49
1854,8.14
1855,8.38
1856,8.22
1857,8.46
1858,7.98
1859,8.06
1860,8.06
1861,8.54
1862,9.75
1863,12.17
1864,15.23
1865,15.79
1866,15.39
1867,14.34
1868,13.78
1869,13.21
1870,12.65
1871,11.84
1872,11.84
1873,11.6
1874,11.04
1875,10.64
1876,10.39
1877,10.15
1878,9.67
1879,9.67
1880,9.91
1881,9.91
1882,9.91
1883,9.71
1884,9.51
1885,9.32
1886,9.12
1887,9.22
1888,9.22
1889,8.92
1890,8.82
1891,8.82
1892,8.82
1893,8.72
1894,8.34
1895,8.14
1896,8.14
1897,8.04
1898,8.04
1899,8.04
1900,8.14
1901,8.24
1902,8.34
1903,8.53
1904,8.63
1905,8.53
1906,8.72
1907,9.11
1908,8.92
1909,8.82
1910,9.21
1911,9.21
1912,9.4
1913,9.6
1914,9.69
1915,9.74
1916,10.64
1917,12.82
1918,15.06
1919,17.3
1920,20.04
1921,17.9
1922,16.77
1923,17.07
1924,17.1
1925,17.53
1926,17.7
1927,17.37
1928,17.13
1929,17.13
1930,16.7
1931,15.23
1932,13.66
1933,12.96
1934,13.39
1935,13.73
1936,13.86
1937,14.36
1938,14.09
1939,13.89
1940,14.03
1941,14.73
1942,16.3
1943,17.3
1944,17.6
1945,18
1946,19.54
1947,22.34
1948,24.08
1949,23.85
1950,24.08
1951,25.98
1952,26.55
1953,26.75
1954,26.88
1955,26.78
1956,27.18
1957,28.15
1958,28.92
1959,29.16
1960,29.62
1961,29.92
1962,30.26
1963,30.62
1964,31.03
1965,31.56
1966,32.46
1967,33.4
1968,34.8
1969,36.67
1970,38.84
1971,40.51
1972,41.85
1973,44.45
1974,49.33
1975,53.84
1976,56.94
1977,60.61
1978,65.22
1979,72.57
1980,82.38
1981,90.93
1982,96.5
1983,99.6
1984,103.9
1985,107.6
1986,109.6
1987,113.6
1988,118.3
1989,124
1990,130.7
1991,136.2
1992,140.3
1993,144.5
1994,148.2
1995,152.4
1996,156.9
1997,160.5
1998,163
1999,166.6
2000,172.2
2001,177.1
2002,179.9
2003,184
2004,188.9
2005,195.3
2006,201.6
2007,207.34
2008,215.3
2009,214.54
2010,218.06""",
 "chart_settings": r"""<settings>
<skip_rows>0</skip_rows>
<csv_separator>,</csv_separator>
<legend>
<align>right</align>
</legend>
<hide_bullets_count>18</hide_bullets_count>
<data_type>csv</data_type>
<plot_area>
<margins><left>50</left><right>40</right><top>55</top><bottom>30</bottom></margins>
</plot_area>
<grid><x><alpha>5</alpha><approx_count>8</approx_count></x>
    <y_left><alpha>5</alpha></y_left>
</grid>
<axes><x><width>1</width><color>cccccc</color></x><y_left><width>1</width><color>cccccc</color></y_left></axes>
<scroller>
<enabled>0</enabled>
</scroller>
<indicator>
<color>0D8ECF</color>
<x_balloon_text_color>FFFFFF</x_balloon_text_color>
<line_alpha>50</line_alpha>
<selection_color>0D8ECF</selection_color>
<selection_alpha>20</selection_alpha>
</indicator>
<zoom_out_button><text_color_hover>FF0F00</text_color_hover></zoom_out_button>
<help><button><color>FCD202</color><text_color>000000</text_color><text_color_hover>FF0F00</text_color_hover></button>
    <balloon><color>FCD202</color><text_color>000000</text_color></balloon>
</help>
<graphs>
<graph gid='0'>
<title>Federal</title>
<color>B8460D</color><color_hover>FF0F00</color_hover>
<fill_alpha>10</fill_alpha>
</graph>
</graphs>
</settings>"""}
]
