<template>
<div class="lunbo">
  <div class="carousel" @mouseenter="enter" @mouseleave="leave">
    <transition-group
            tag="ul"
            name="image"
            enter-active-class="animated lightSpeedIn"
            leave-active-class="animated lightSpeedOut"
    >
        <li v-for='(item,index) in items' :key='item.id' v-show="index === mark"
   >
            <a href="javascript:;">
                <img :src="item.img">
            </a>
        </li>
    </transition-group>
    <div class="bullet">
        <span v-for="(item,index) in items.length" :class="{'active':index === mark}"
         @click="change(index)" :key="index"></span>
    </div>
    <div class="switch">
        <span class="prev" @click="prev">&lt;</span>
        <span class="next" @click="next">&gt;</span>
    </div>
  </div>
</div>
</template>

<script>

  import axios from 'axios';


  export default {
    data() {
      return {
        mark:0,
        items:[],
        time:null
      }
    },

    methods: { //方法
      getData:function(){
        axios.get("api/list").then(res=>{
          console.log(res);
          if(res.status =='200'){
            this.items = res.data;
            console.log( this.items)
          }
        },(error)=>{
          console.log(error)
        })
      },
      //轮播图
      change(i){
              this.mark = i;
          },
          prev(){
              this.mark--;
              if(this.mark === -1){
                  this.mark = 3;
                  return
              }
          },
          next(){
              this.mark++;
              if(this.mark === 4){
                  this.mark = 0;
                  return
              }
          },
          autoPlay(){
              this.mark++;
              if(this.mark === 4){
                  this.mark = 0;
                  return
              }
          },
          play(){
              this.time = setInterval(this.autoPlay,3000);
          },
          enter(){
              console.log('enter')
              clearInterval(this.time);
          },
          leave(){
              console.log('leave')
              this.play();
          },
          created(){
              this.play()
          }
      },
      mounted:function(){    //生命周期
        this.getData();
      }
     }
  </script>

<style>
  .lunbo{
    margin-top:-600px;

  }
  li{
      list-style: none;
      }
      .carousel{
          width: 900px;
          height: 600px;
          overflow: hidden;
          margin: 13px 420px;
          position: relative;
      }
      .carousel ul{
          width: 100%;
          height: 100%;
      }
      .carousel ul li{
          position: absolute;
      }
      .carousel ul li a img{
          width: 900px;
          height: 600px;
		     border-radius: 10px;
      }
      .bullet{
          position: absolute;
          font-size: 0;
          bottom: 20px;
          left: 50%;
          margin-left: -42px;
      }
      .bullet span{
  display: inline-block;
  width: 10px;
  height: 10px;
  background-color: #ffffff;
  margin-left: 15px;
  border-radius: 10px;
      }
      .bullet span:first-child{
          margin-left: 0;
      }
      .switch{

      }
      .switch span{
  position: absolute;
  width: 50px;
  height: 50px;
  line-height: 50px;
  text-align: center;
  background-color: rgba(0,0,0,.1);
  font-size: 20px;
  color: #ffffff;
  top: 50%;
  margin-top: -25px;
  cursor: pointer;
  font-family: "宋体";
      }
  	.switch span:hover{

  background-color: rgba(0,0,0,.5);

      }
      .prev{
          left: 0;
      }
      .next{
          right: 0;
      }
      .active{
          background-color: red !important;
      }

      .swipe_title {
          position: absolute;
          line-height: 60px;
          height: 60px;
          width: 76%;
          z-index: 20;
          text-align: left;
          color: white;
          font-size: 18px;
          margin-left: 10px;
          bottom: 0;
          overflow: hidden;
          text-overflow:ellipsis;
          white-space:nowrap
      }


</style>
