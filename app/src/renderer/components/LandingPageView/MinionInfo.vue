<template>
<div id='stuff'>
<p>The Current Time is: {{ currenttime }}</p>
<ul class="nav nav-tabs" role="tablist" >
    <li v-for="(key,minion) in minIONdict "><a v-bind:href="'#' + minion" role = "tab" data-toggle="tab">{{ minion }}</a></li>
</ul>

<div class="tab-content">

    <div v-for="(key,minion,index) in minIONdict " role="tabpanel" class="tab-pane" :id="minion">


    <div v-if="minIONdict[minion].detailsdata">
    <div v-if="minIONdict[minion].detailsdata.statistics">
    <YieldPlot :currenttime="currenttime" :yielddata="minIONdict[minion].yield_history"  :title="minion" ></YieldPlot>
    <HistPlot :currenttime="currenttime" :title="minion" :datain="minIONdict[minion].detailsdata.statistics.read_event_count_weighted_hist" :datain2="minIONdict[minion].detailsdata.statistics.read_event_count_weighted_hist_bin_width"></HistPlot>
    </div>
    </div>
    <div v-if="minIONdict[minion].pore_history">
    <StrandPlot :currenttime="currenttime" :title="minion" :datain2="minIONdict[minion].pore_history"></StrandPlot>
    <PercPlot :currenttime="currenttime" :title="minion" :datain2="minIONdict[minion].pore_history"></PercPlot>
    <TempPlot :currenttime="currenttime" :title="minion" :datain2="minIONdict[minion].temp_history"></TempPlot>
    <VoltPlot :currenttime="currenttime" :title="minion" :datain2="minIONdict[minion].temp_history"></VoltPlot>
    <PorePlot :currenttime="currenttime" :title="minion" :datain="minIONdict[minion].channelstuff" :datain2="minIONdict[minion].pore_history.details"></PorePlot>


    <h5><b>Messages from MinKNOW:</b></h5>
    <div class="pre-scrollable">
      <div v-for="message in key.messages" >
        <span :class="message.severity">{{message.severity}}</span>{{message.message}}<br><i>{{message.timestamp}}</i>
      </div>
    </div>
    </div>
    <div v-else> This minION is not currently active. </div>

    <!--
    <div v-for="(value2, key2) in key.livedata">
        <div v-if="key2 === 'current_script'">
            {{value2}}
            <div v-if="key.livedata.current_script.result.length>0">YAY!</div>
            <div v-else>Nay!</div>
        </div>
    </div>
    -->
    </div>

</div>
 </div>
</template>


<script>
import YieldPlot from './Plots/yieldplot.vue'
import HistPlot from './Plots/histplot.vue'
import StrandPlot from './Plots/strandplot.vue'
import PercPlot from './Plots/percplot.vue'
import TempPlot from './Plots/tempplot.vue'
import VoltPlot from './Plots/voltplot.vue'
import PorePlot from './Plots/poreplot.vue'
function reverse (value) {
  return value.split('').reverse().join('')
}
export default {
  components: {YieldPlot, HistPlot, StrandPlot, PercPlot, TempPlot, VoltPlot, PorePlot}, // , Chart, Chart2},
  data () {
    return {
    }
  },
  props: ['currenttime', 'minIONdict'],
  methods: {
    reverse
  }
}

</script>
