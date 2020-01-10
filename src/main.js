// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import axios from 'axios'
import $ from 'jquery'
import 'swiper/css/swiper.css'
import Swiper from 'swiper';
import './assets/font/iconfont.css'
import './assets/css/head.css'
import './assets/css/reset.css'
import './assets/css/animate.css'
import './assets/css/swiper.min.css'
import './assets/css/main.css'
import './assets/js/web.js'
import './assets/js/mfb.js'
import './assets/js/vue.min.js'
import './assets/css/mfb.css'
import './assets/css/style.css'
import './assets/css/animate.min.css'
import './assets/css/font-awesome.min.css'
import './assets/js/jquery-1.10.2.js'
import './assets/js/jquery-1.11.0.min.js'
import '../node_modules/bootstrap/dist/css/bootstrap.min.css'
import '../node_modules/bootstrap/dist/js/bootstrap.min.js'

Vue.config.productionTip = false
Vue.prototype.$http = axios;
/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
