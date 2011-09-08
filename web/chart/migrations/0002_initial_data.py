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
  data: [0.080182811,0.183145123,0.201670697,0.233401056,0.273745546,0.338090167,0.36733985,0.356876221,0.418586195,0.452378335,0.501633235,0.487443968,0.476004883,0.495874639,0.520831391,0.540559038,0.548463052,0.554153228,0.536681167,0.535720213,0.564720522,0.588385694,0.607693514,0.639838748,0.734543574,0.948704127,1.081651767,1.154291028,1.143956416,1.159123093,1.162194297,1.139564831,1.122152726,1.145830972,1.174877154,1.286610216,1.365651222,1.445893503,1.45431588,1.405711166,1.300243304,1.324402993,1.408805701,1.749298817]
					},
                                        {
						name: "State and Local",
						data: [0.085349752,0.194185488,0.187568696,0.190664364,0.235702591,0.256096912,0.304241053,0.324842654,0.31987996,0.368626733,0.33079031,0.372794444,0.372595693,0.375720084,0.412868979,0.428716259,0.4355158,0.443574945,0.435948511,0.434935388,0.452814959,0.474429947,0.472221787,0.490244614,0.535362469,0.606859031,0.624141084,0.681108078,0.753154463,0.794593173,0.779117178,0.790832173,0.800262694,0.815671139,0.839699543,0.894411931,0.966677316,0.972367866,0.999373936,1.043568015,0.991996358,1.000700479,0.979110731,0.899193994]
					},
                                        {
						name: "Total",
						data: [0.165532563,0.37733061,0.389239393,0.424065421,0.509457768,0.594187078,0.671580903,0.681718874,0.738466155,0.821005068,0.832423545,0.860238412,0.848600575,0.871594723,0.933700369,0.969275297,0.983978852,0.997725344,0.972629678,0.970655602,1.017535481,1.062815641,1.079915301,1.130083362,1.269904319,1.555563158,1.705791274,1.835397606,1.897110879,1.953716266,1.941311475,1.930397004,1.92241542,1.961502112,2.014575692,2.181022146,2.332328538,2.418261369,2.453689816,2.449279181,2.292239661,2.325103472,2.387916432,2.648492811]
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
