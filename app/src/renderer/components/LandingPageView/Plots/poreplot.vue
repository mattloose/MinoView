<template>
	<div><div>
</template>

<script>
var Highcharts = require('highcharts')
function parseporehist (descriptions, counts) {
  var results = []
  // var colors = []
  // var categories = []
  // var datam = []
  var colorlookup = []
  for (var thing in descriptions) {
    if (descriptions.hasOwnProperty(thing)) {
      if (descriptions[thing].hasOwnProperty('style')) {
        colorlookup[descriptions[thing]['name']] = descriptions[thing]['style']['colour']
      }
    }
  }

  for (var pore in counts) {
    results.push({'name': pore, 'color': '#' + colorlookup[pore], 'data': counts[pore]}) // ,'color':'#121212']})
  }
  return results
}
export default {
  name: 'PorePlot',
  props: {
    title: {
      type: String,
      required: false
    },
    datain: {},
    datain2: {}
    // target: {}
  },
  data: function () {
    return {
      target: undefined
    }
  },
  mounted: function () {
    this.target = Highcharts.chart(this.$el, {
      chart: {
        type: 'area',
        // zoomType: 'x',
        height: 350,
        backgroundColor: null,
        animation: false
      },
      credits: {
        enabled: false
      },
      title: {
        text: 'Pore States'
      },
      xAxis: {
        type: 'datetime'
        // tickPixelInterval: 150
      },
      yAxis: {
        endOnTick: false,
        title: {
          text: 'Channel Classifications'
        }
      },
      legend: {
        enabled: true
      },
      plotOptions: {
        area: {
          stacking: 'percent'
        },
        series: {
          showInNavigator: true,
          dataLabels: {
            enabled: false,
            formatter: function () {
              return this.y
            }
          }
        } // ,
        // series: []
      }
    }
    )
    this.$nextTick(function () {
      var returndata = parseporehist(this.datain, this.datain2)
      while (this.target.series.length > 0) {
        this.target.series[0].remove(true)
      }
      for (var i = 0; i < returndata.length; i++) {
        this.target.addSeries(returndata[i])
      }
      // console.log(this)
      var self = this
      setInterval(function () {
        var returndata = parseporehist(this.datain, this.datain2)
        while (self.target.series.length > 0) {
          self.target.series[0].remove(true)
        }
        for (var i = 0; i < returndata.length; i++) {
          self.target.addSeries(returndata[i])
        }
      }.bind(self), 15000)
    })
  },
  beforeDestroy: function () {
    this.target.destroy()
  }
}
</script>
