<template>
	<div></div>
</template>

<script>
var Highcharts = require('highcharts')
export default {
  name: 'TempPlot',
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
        text: 'Temperature Over Time'
      },
      xAxis: {
        type: 'datetime',
        tickPixelInterval: 150
      },
      yAxis: {
        title: {
          text: 'Temperature Celcius'
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
          name: 'Asic Temperature',
          data: []
        },
        {
          name: 'Heat Sink Temperature',
          data: []
        }
      ]
    }
    )
    this.$nextTick(function () {
      this.target.series[0].setData(this.datain2['asictemp'])
      this.target.series[1].setData(this.datain2['heatsinktemp'])
      // console.log(this)
      var self = this
      setInterval(function () {
        self.target.series[0].setData(this.datain2['asictemp'])
        self.target.series[1].setData(this.datain2['heatsinktemp'])
        // console.log(this)
      }.bind(self), 5000)
    })
  },
  beforeDestroy: function () {
    this.target.destroy()
  }
}
</script>
