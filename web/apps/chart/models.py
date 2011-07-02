# coding: UTF-8

from django.db import models

class Chart(models.Model):
    title = models.CharField(max_length=255)
    sparkblocks = models.CharField(max_length=30, unique=True)
    tweet = models.CharField(max_length=140)
    source_url = models.URLField()
    source_title = models.CharField(max_length=255)
    source_detail = models.TextField()
    chart_creator = models.CharField(max_length=100)
    chart_creator_avatar = models.URLField()
    chart_creator_detail = models.TextField()
    disqus_identifier = models.TextField(max_length=20)
    chart_data = models.TextField()
    chart_settings = models.TextField()

    def __unicode__(self):
        return self.title

def init():
    c = Chart(
        title='US Taxes as Percentage of Personal Income',
        sparkblocks='▃▃▃▅▆▆▆▆▅▇▆▅▁',
        tweet=r'US Taxes as Percentage of Percentage Income, 1929-2009: d4t4.org/▁▂▆▆▆▇▇▇▇▇▅ low 1.4% high 14.4%',
        source_url='http://www.bea.gov/iTable/index_nipa.cfm',
        source_title='US Bureau of Economic Analysis',
        source_detail="""Tax data is from <a href="http://www.bea.gov/national/nipaweb/TableView.asp?SelectedTable=89&Freq=Year&FirstYear=1&LastYear=2100" target="_blank">Table 3.4, Personal Current Tax Receipts</a>, last Revised on August 05, 2010. The breakdown of state and local tax is into Income, Property, Motor vehicle, and “other”, mainly hunting and fishing licences; not state and then local.
            <p>
            Personal income is from <a target="_blank" href="http://www.bea.gov/national/nipaweb/TableView.asp?SelectedTable=58&Freq=Year&FirstYear=1&LastYear=2100">Table 2.1. Personal Income and Its Disposition</a>, last Revised on May 26, 2011 - Next Release Date June 24, 2011. It doesn’t give federal vs. state/local breakdown, but does give the total amount which agrees with that computed from Table 3.4, though it includes data for 2010 which is not in the latest Table 3.4 data.
            <p>
            Data was downloaded on June 22, 2011 into this <a target="_blank" href="https://spreadsheets.google.com/spreadsheet/ccc?key=0AkpTmG7ijJvXdEVCMkRULUEya2VJbnM0ci1DbTZ3WUE&hl=en_US">Google spreadsheet</a> and then posted here.""",
      chart_creator="Andrew Neitsch",
      chart_creator_avatar="http://www.gravatar.com/avatar/dc87?d=identicon",
      chart_creator_detail="""2 charts posted<br>
            3 articles on the web include Andrew's charts <br>
            5 likes from 2 people <br>
            10 comments written <br>
            15 people follow Andrew <br>
            Andrew follows 8 people <br>
            <br>
            Andrew joined The Data Collective on June 18, 2011.""",
      disqus_identifier='taxpercent',
      chart_data="""1929,1.41,0.71,2.12
1930,1.31,0.66,1.97
1931,0.77,0.77,1.53
1932,0.60,0.80,1.40
1933,0.85,0.85,1.71
1934,0.93,0.74,1.68
1935,1.00,0.83,1.82
1936,1.02,0.87,1.90
1937,1.75,0.81,2.56
1938,1.75,0.88,2.63
1939,1.23,0.82,2.06
1940,1.28,0.89,2.17
1941,1.67,0.73,2.40
1942,3.40,0.57,3.97
1943,10.52,0.53,11.05
1944,10.18,0.48,10.66
1945,10.84,0.47,11.31
1946,9.18,0.50,9.69
1947,9.85,0.52,10.37
1948,8.63,0.52,9.16
1949,7.44,0.68,8.12
1950,7.60,0.66,8.26
1951,9.85,0.66,10.51
1952,10.97,0.65,11.63
1953,10.73,0.65,11.38
1954,9.55,0.71,10.26
1955,9.65,0.76,10.41
1956,9.99,0.80,10.78
1957,10.04,0.81,10.85
1958,9.62,0.84,10.46
1959,9.81,0.97,10.78
1960,10.16,1.02,11.18
1961,9.96,1.07,11.03
1962,10.19,1.10,11.28
1963,10.24,1.13,11.37
1964,8.94,1.19,10.13
1965,9.20,1.19,10.39
1966,9.71,1.29,11.00
1967,9.94,1.33,11.26
1968,10.73,1.49,12.22
1969,11.78,1.64,13.43
1970,10.60,1.69,12.29
1971,9.50,1.76,11.26
1972,10.36,2.11,12.46
1973,9.87,2.05,11.92
1974,10.35,2.00,12.35
1975,9.04,2.02,11.06
1976,9.57,2.11,11.68
1977,9.94,2.17,12.10
1978,10.28,2.21,12.49
1979,10.91,2.14,13.04
1980,10.86,2.12,12.99
1981,11.25,2.11,13.37
1982,10.66,2.14,12.80
1983,9.69,2.24,11.93
1984,9.22,2.32,11.55
1985,9.61,2.33,11.94
1986,9.47,2.36,11.83
1987,10.00,2.46,12.46
1988,9.52,2.41,11.93
1989,9.91,2.51,12.42
1990,9.70,2.53,12.23
1991,9.17,2.49,11.66
1992,8.89,2.53,11.42
1993,9.08,2.53,11.61
1994,9.23,2.52,11.75
1995,9.45,2.55,12.00
1996,10.06,2.56,12.62
1997,10.63,2.60,13.23
1998,10.97,2.67,13.64
1999,11.29,2.71,14.00
2000,11.63,2.77,14.40
2001,11.16,2.74,13.90
2002,9.15,2.45,11.59
2003,8.26,2.41,10.67
2004,8.04,2.50,10.54
2005,8.89,2.64,11.53
2006,9.32,2.68,12.00
2007,9.78,2.71,12.50
2008,8.90,2.71,11.61
2009,7.00,2.36,9.36""",
        chart_settings="""<settings>
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
</settings>""")
    c.save()
