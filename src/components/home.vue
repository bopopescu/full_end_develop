<template>
   <div class="shop">
      <div class="index-main">
         <ul>
            <li class="lists" v-for="(item,index) in items" :key="index">
                <router-link :to="'/detail/'+item.id">
                  <img :src="item.img" >
                </router-link>
                <label>

                    <b >{{item.name}}</b>

                </label>
                   <label>
                      <span class="price-text">原价:￥{{item.price}}</span>
                      <b class="discount">折扣价:￥{{item.discount}}</b>

				            </label>

            </li>
        </ul>
    </div>
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
<style>
  .shop{
    background: #00C5CD;
  }
</style>
