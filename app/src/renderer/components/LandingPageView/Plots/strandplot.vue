<template>
	<div><div>
</template>

<script>
var Highcharts = require('highcharts')
export default {
  name: 'YieldPlot',
  props: {
    title: {
      type: String,
      required: false
    },
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
        type: 'spline',
        zoomType: 'x',
        height: 350,
        backgroundColor: null
      },
      credits: {
        enabled: false
      },
      title: {
        text: 'In Strand Counts ' + this.title,
        x: -20 // center
      },
      xAxis: {
        type: 'datetime',
        tickPixelInterval: 150
      },
      yAxis: {
        title: {
          text: 'Number of Pores In Strand/Single'
        },
        plotLines: [{
          value: 0,
          width: 1,
          color: '#808080'
        }],
        min: 0
      },
      series: [
        {
          name: 'In Strand',
          data: []
        },
        {
          name: 'Single Pore',
          data: []
        }
      ]
    }
    )
    this.$nextTick(function () {
      this.target.series[0].setData(this.datain2['strand'])
      this.target.series[1].setData(this.datain2['single'])
      // console.log(this)
      var self = this
      setInterval(function () {
        self.target.series[0].setData(this.datain2['strand'])
        self.target.series[1].setData(this.datain2['single'])
        // console.log(this)
      }.bind(self), 5000)
    })
  },
  beforeDestroy: function () {
    this.target.destroy()
  }
}
</script>
