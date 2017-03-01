<template>
	<div></div>
</template>

<script>
var Highcharts = require('highcharts')
export default {
  name: 'YieldPlot',
  props: {
    currenttime: '',
    title: {
      type: String,
      required: false
    },
    yielddata: {}
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
        type: 'spline',
        zoomType: 'x',
        height: 350,
        backgroundColor: null
      },
      credits: {
        enabled: false
      },
      title: {
        text: 'Yield Over Time ' + this.title,
        x: -20 // center
      },
      xAxis: {
        type: 'datetime',
        tickPixelInterval: 150
      },
      yAxis: {
        title: {
          text: 'Cumulative Events'
        },
        plotLines: [{
          value: 0,
          width: 1,
          color: '#808080'
        }],
        min: 0
      },
      series: [{
        name: 'Event Counts',
        data: ''
      }]
    }
    )
    this.$nextTick(function () {
      this.target.series[0].setData(this.yielddata)
      // console.log(this)
      var self = this
      setInterval(function () {
        self.target.series[0].setData(this.yielddata)
        self.target.redraw()
        // console.log(this)
      }.bind(self), 5000)
    })
  },
  beforeDestroy: function () {
    this.target.destroy()
  }
}
</script>
