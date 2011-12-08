{{easyxdm|safe}}

DATACOLLECTIVE = { easyXDM: easyXDM.noConflict("DATACOLLECTIVE") };

new DATACOLLECTIVE.easyXDM.Socket({
  remote: "{{chart_url}}",
  container: document.getElementById("datacollective-chart-{{chart.id}}"),
  props: { style: { width: "{% if width %}{{ width }}{% else %}{% if chart.chart_width %}{{chart.chart_width}}{% else %}630{% endif %}{% endif %}px", height: "400px" } },
  onMessage: function(message, origin) {
    this.container.getElementsByTagName("iframe")[0].style.height = parseInt(message) + "px";
  }
});
