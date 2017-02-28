<template>
  <div>
    <!--<img src="./LandingPageView/assets/minoTourlogotext.png" alt="minoTour-logo">-->
    <h2>Limited Documentation Will Be Here.</h2>
    <current-page></current-page>
    <custom-message></custom-message>
    <div id="version"></div>
    <br>
    <div id="currenttime"></div>
    <!-- use router-link component for navigation. -->
    <!-- specify the link by passing the `to` prop. -->
    <!-- <router-link> will be rendered as an `<a>` tag by default -->
    <router-link to="/landing-page">View Real Time Data</router-link>
    <router-link to="/text-page">Help Guide</router-link>
    <router-view></router-view>
  </div>
</template>

<script>
  import CurrentPage from './LandingPageView/CurrentPage'
  import CustomMessage from './LandingPageView/CustomMessage'
  export default {
    components: {
      CurrentPage,
      CustomMessage
    },
    name: 'text-page'
  }
</script>

<style scoped>
  img {
    margin-top: -25px;
    width: 450px;
  }
</style>
