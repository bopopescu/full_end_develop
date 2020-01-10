<template>
  <div>
  <!-- 导航 -->
  <header class="header">
    <div class="container clearfix">
      <div class="fl left">
        <!-- <a href="javascript:void(0)"><img src="../assets/img/logo.png" alt="" class="img1" /></a>
        <a href="javascript:void(0)"><img src="../assets/img/logo2.jpg" alt="" class="img2" /></a> -->
      </div>
      <div class="fr nav">
        <ul class="navbar_nav" data-in="fadeInDown" data-out="fadeOutUp">
          <li class="active">
            <a href="javascript:void(0)"style=" background-color: #00EEEE;"><i class="icon-home"></i>首页</a>
          </li> 
          <li class="dropdown">
            <a href="javascript:void(0)">
             每日爆品
            </a>
            <div class="dropdown_menu">
              <a href="#">满200立减100</a>
              <a href="#">秒杀</a>
              <a href="#">Plus会员</a>
            </div>
          </li>
          <li class="dropdown">
            <a href="javascript:void(0)">直营</a>
            <div class="dropdown_menu">
              <a href="#">生鲜</a>
              <a href="#">日用百货</a>
              <a href="#">玩具</a>
            </div>
          </li>
          <li>
            <a href="javascript:void(0)">金融</a>
          </li>
          <li>
            <a href="javascript:void(0)">关于我们</a>
          </li>
          <li>
            <a href="javascript:void(0)">联系合作</a>
          </li>
        </ul>
      </div>
      <a href="javascript:void(0)" id="navToggle">
        <span></span>
      </a>
    </div>
  </header>
  <!--移动端的导航-->
  <!-- <div class="m_nav">
    <div class="top clearfix">
      <img src="image/closed.png" alt="" class="closed" />
    </div>
    <div class="logo">
      <img src="image/logo2.jpg" alt="" />
    </div>
    <ul class="ul" data-in="fadeInDown" data-out="fadeOutUp">
      <li class="active">
        <a href="javascript:void(0)">首页</a>
      </li>
      <li class="dropdown">
        <a href="javascript:void(0)">
          业务体系
        </a>
        <div class="dropdown_menu">
          <a href="#">Custom Menu</a>
          <a href="#">Custom Menu</a>
          <a href="#">Custom Menu</a>
        </div>
      </li>
      <li class="dropdown">
        <a href="javascript:void(0)">直营园</a>
        <div class="dropdown_menu">
          <a href="#">Custom Menu</a>
          <a href="#">Custom Menu</a>
          <a href="#">Custom Menu</a>
        </div>
      </li>
      <li>
        <a href="javascript:void(0)">行知资讯</a>
      </li>
      <li>
        <a href="javascript:void(0)">关于我们</a>
      </li>
      <li>
        <a href="javascript:void(0)">联系合作</a>
      </li>
    </ul>
  </div>
  <div class="banner">
    <img src="image/aa.jpg">
  </div>
  <div class="box" style="height: 1000px;">
    <h3 style="text-align: center; color: aliceblue">调整浏览器宽度大小查看效果</h3>
  </div> -->
  </div>
</template>


<script type="text/javascript">
  $(function() {
    //超过一定高度导航添加类名
    var nav = $("header"); //得到导航对象
    var win = $(window); //得到窗口对象
    var sc = $(document); //得到document文档对象。
    win.scroll(function() {
      if (sc.scrollTop() >= 100) {
        nav.addClass("on");
      } else {
        nav.removeClass("on");
      }
    })

    //移动端展开nav
    $('#navToggle').on('click', function() {
      $('.m_nav').addClass('open');
    })
    //关闭nav
    $('.m_nav .top .closed').on('click', function() {
      $('.m_nav').removeClass('open');
    })

    //二级导航  移动端
    $(".m_nav .ul li").click(function() {
      $(this).children("div.dropdown_menu").slideToggle('slow')
      $(this).siblings('li').children('.dropdown_menu').slideUp('slow');
    });

  })
</script>
<style>
  @import './assets/css/head.css',
  @import './assets/css/reset.css',
  @import './assets/css/animate.css',
  @import './assets/css/swiper.min.css'

</style>
