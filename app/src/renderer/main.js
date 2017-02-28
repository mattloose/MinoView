import Vue from 'vue'
import Electron from 'vue-electron'
import Resource from 'vue-resource'
import Router from 'vue-router'

import App from './App'
import routes from './routes'

// import 'jquery/dist/jquery.min.js'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap/dist/js/bootstrap.min.js'

Vue.use(Electron)
Vue.use(Resource)
Vue.use(Router)
Vue.config.debug = true

const router = new Router({
  scrollBehavior: () => ({ y: 0 }),
  routes
})

/* eslint-disable no-new */
let vm = new Vue({
  router,
  data: {
    loading: false,
    currenttime: 'Data Connection Establishing',
    minIONdict: {}
  },
  ...App
}).$mount('#app')

const zerorpc = require('zerorpc')
let client = new zerorpc.Client()

client.connect('tcp://127.0.0.1:4242')

client.invoke('echo', 'server ready', (error, res) => {
  if (error || res !== 'server ready') {
    console.error(error)
  } else {
    console.log('server is ready')
  }
})

// let currenttime = document.querySelector('#currenttime')
function gettimefromserver () {
  // your other code here
  client.invoke('sendtime', 'stuff', function (error, res) {
    if (error) {
      console.log(error)
    } else {
      // console.log(res)
      // console.log(vm.currenttime)
      vm.currenttime = res
    }
  })
  setTimeout(gettimefromserver, 1000)
}
gettimefromserver()

function getjsonfromserver () {
  vm.loading = true
  client.invoke('fetchminIONdict', function (error, res) {
    if (error) {
      console.log(error)
    } else {
      // console.log(JSON.parse(res))
      vm.minIONdict = JSON.parse(res)
      vm.loading = false
    }
  })
  setTimeout(getjsonfromserver, 1000)
}
getjsonfromserver()
