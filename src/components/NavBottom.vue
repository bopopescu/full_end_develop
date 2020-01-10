<template>
  <div class="nav-bottom">
      <router-link to="/home">
        <i class="iconfont iconiconfontzhizuobiaozhun023101"></i>
        <label>首页</label>
      </router-link>
      <router-link to="/find">
        <i class="iconfont iconfaxian3"></i>
        <label>推荐</label>
      </router-link>
      <router-link to="/order">
        <i class="iconfont icondingdan"></i>
        <label>订单</label>
      </router-link>
      <router-link to="/my">
        <i class="iconfont iconwo1"></i>
        <label>我的</label>
      </router-link>
  </div>
</template>

<script>
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
    }
  }
</script>
<style scoped>
.active {
    color:red;
}
</style>
