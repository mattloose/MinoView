<template>
<div id="Temp">
<div class="container-fluid">
      <div class="page-header">
          <h2><img src="./components/LandingPageView/assets/minoTourlogotext.png" alt="minoTour-logo"><small>Local monitoring for MinKNOW</small></h2></div>
  </div>
  <div class="container">
    <div id="#app">
       <router-view :currenttime=currenttime :minIONdict=minIONdict></router-view>
    </div>
  </div>
  <div class="footer-clean">
      <footer>
          <div class="container">
              <div class="row">
                  <div class="col-md-6 col-sm-8 item">
                  Tool could break any time. Currently compatible with MinKNOW 1.4.2. If a new version of MinKNOW comes out - this probably breaks. Sorry.
                  </div>
                  <div class="col-md-3 col-sm-4 item">

                  </div>
                  <div class="col-md-3 item social">
                  <!--<a href="https://twitter.com/mattloose" target="_blank"><i class="icon ion-social-twitter"></i></a>-->
                      <p class="copyright">@mattloose 2017</p>
                  </div>
              </div>
          </div>
      </footer>
  </div>
</div>
</template>

<script>
  import store from 'renderer/vuex/store'
  export default {
    store
  }
</script>
