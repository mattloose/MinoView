<template>
	<div></div>
</template>

<script>
var Highcharts = require('highcharts')
require('highcharts/modules/exporting')(Highcharts)
require('highcharts-export-csv')(Highcharts)
function tohistogram (readeventcountweightedhist, readeventcountweightedhistbinwidth) {
  var results = []
  var categories = []
  for (var i = 0; i < readeventcountweightedhist.length; i++) {
    var category = String((i) * readeventcountweightedhistbinwidth) + '-' + String((i + 1) * readeventcountweightedhistbinwidth) + ' bp'
    categories.push(category)
    // console.log(categories)
    results.push({ 'name': category, 'y': readeventcountweightedhist[i] })
  }
  return [results, categories]
}
export default {
  name: 'HistPlot',
  props: {
    currenttime: '',
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
    this.chart = Highcharts.chart(this.$el, {
      chart: {
        type: 'column',
        zoomType: 'x',
        height: 350,
        backgroundColor: null
      },
      credits: {
        enabled: false
      },
      title: {
        text: 'Read Length Histogram ' + this.title,
        x: -20 // center
      },
      xAxis: {
        categories: []
      },
      yAxis: {
        title: {
          text: 'Total Event Length'
        },
        plotLines: [{
          value: 0,
          width: 1,
          color: '#808080'
        }],
        min: 0
      },
      series: [{
        name: 'Read Histogram',
        data: ''
      }]
    }
    )
    this.$nextTick(function () {
      var returndata = tohistogram(this.datain, parseInt(this.datain2))
      this.chart.series[0].setData(returndata[0])
      this.chart.xAxis[0].setCategories(returndata[1])
      // this.chart.series[0].setData(this.datain2)
      // console.log(this)
      var self = this
      setInterval(function () {
        var returndata = tohistogram(this.datain, parseInt(this.datain2))
        this.chart.series[0].setData(returndata[0])
        this.chart.xAxis[0].setCategories(returndata[1])
        // console.log(this)
      }.bind(self), 5000)
    })
  },
  beforeDestroy: function () {
    this.chart.destroy()
  }
}
</script>
