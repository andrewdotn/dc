(function() {
  if (typeof(DATACOLLECTIVE) === 'undefined') {
    DATACOLLECTIVE = { easyXDM: easyXDM.noConflict("DATACOLLECTIVE") };
  }

  new DATACOLLECTIVE.easyXDM.Socket({
    remote: "{{chart_url}}",
    container: document.getElementById("datacollective-chart-{{chart.id}}"),
    props: { style: { width: "630px", height: "400px" } },
    onMessage: function(message, origin) {
      this.container.getElementsByTagName("iframe")[0].style.height = message + "px";
    }
  });
})();