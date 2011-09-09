
//
// supportsVml and supportsSVG thanks to http://stackoverflow.com/questions/654112/how-do-you-detect-support-for-vml-or-svg-in-a-browser
//

function supportsVml() {
    if (typeof supportsVml.supported == "undefined") {
        var a = document.body.appendChild(document.createElement('div'));
        a.innerHTML = '<v:shape id="vml_flag1" adj="1" />';
        var b = a.firstChild;
        b.style.behavior = "url(#default#VML)";
        supportsVml.supported = b ? typeof b.adj == "object": true;
        a.parentNode.removeChild(a);
    }
    return supportsVml.supported
}

function supportsSVG() {
  return document.implementation.hasFeature("http://www.w3.org/TR/SVG11/feature#BasicStructure", "1.1")
}

// Highcharts/Raphael can work on devices that have SVG or VML
// on other devices (such as all android 2.X devices), we must
// fall back to a static image.

      if (supportsSVG() || supportsVml()) {
        document.write('<div id="chartdiv" style="margin:0px auto; max-width:600px; padding:8px; background-color:#ffffff; border:1px solid #aaaaaa "> </div>');      
      } else {
        document.write('<img src="/static/images/medicaid.png" alt="Chart: Spending on Medicaid as a Percentage of Gross Domestic Product, 1966-2009"/>')
      }


			var chart;
			$(document).ready(function() {
				chart = new Highcharts.Chart({
                                        credits: {
                                          text: 'Sources: Centers for Medicare and Medicaid Services, Bureau of Economic Analysis.  For complete source data, click here.',
			                  style: { width: '300px', textAlign: 'left', textAnchor: 'begin' },
                                          position: { y: -20 },
                                          href: 'http://localhost:8001/chart/medicaid_vs_gdp'

                                        },
                                        exporting: {
                                          enabled: false
                                        },
					chart: {
						renderTo: 'chartdiv', 
						defaultSeriesType: 'line',
                                                spacingBottom: 40,
                                                width:600
					},
                                        legend: {
                                                verticalAlign: 'bottom',
                                                align: 'center',
                                                layout: 'horizontal'
                                        },
					title: {
						text: 'Spending on Medicaid as a Percentage',
                                                style: { fontSize: '18px', color: '#000000' },
					},
					subtitle: {
						text: 'of Gross Domestic Product, 1966-2009',
                                                style: { fontSize: '18px', color: '#000000' },
                                                y: 40
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
					series: [
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

                                        ]
				});

                });
