<template>
<div class="container">
  <div>
  <div class="row">
      <div class="col-md-12">
    <MinionInfo :minIONdict=minIONdict :currenttime=currenttime></MinionInfo>
    <custom-message></custom-message>
    <!-- use router-link component for navigation. -->
    <!-- specify the link by passing the `to` prop. -->
    <!-- <router-link> will be rendered as an `<a>` tag by default -->
    <router-link to="/landing-page">View Real Time Data</router-link>
    <router-link to="/text-page">Help Guide</router-link>
    <router-view></router-view>
    </div>
  </div>

 </div>
</div>
</template>

<script>
  import CustomMessage from './LandingPageView/CustomMessage'
  import MinionInfo from './LandingPageView/MinionInfo'
  export default {
    components: {
      CustomMessage,
      MinionInfo
    },
    name: 'landing-page',
    props: ['currenttime', 'minIONdict', 'loading']
  }
</script>

<style scoped>

</style>
