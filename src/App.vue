
<template>
  <div id="app">
    <!-- 路由出口，路由匹配的组件将渲染在这里 -->

   <navgation />

    <login/>
    <search/>
     <daohang/>
     <secondnav/>
     <lunbo/>
     <cebiannav/>
  <router-view/>
  <div class="swiper-scrollbar"></div>
  </div>
</template>

<script>
//import NavBottom from './components/NavBottom'
import navgation from './components/navgation';
import login from './components/login';
import search from './components/search';
import daohang from './components/daohang';
import secondnav from './components/secondnav';//引入组件
import lunbo from './components/lunbo';
import cebiannav from './components/cebiannav';
//Vue.prototype.$http = axios;
import axios from 'axios';



export default {
  data () {
    return {

      items: []
    }
  },

  methods:{ //方法
    getData:function(){
      axios.get("api/list").then(res=>{
        console.log(res);
        if(res.status =='200'){
          this.items = res.data;
        }
      },(error)=>{
        console.log(error)
      })
    }
  },
  mounted:function(){    //生命周期
    this.getData();
  },
  components: {
    //NavBottom,
    navgation,
    daohang,
    login,
    secondnav,
    search,
    lunbo,
    cebiannav
  }
}

</script>

<style>
@import './assets/css/index.css'

</style>
