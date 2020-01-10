<template>
  <div>
    <!-- 通栏菜单 -->
    <div class="topbar hidden-sm hidden-xs">
      <div class="container">
        <div class="row">
          <div class="tb-1 col-md-2">
            <a href="#" class="text-muted">

              <span class="text"><i class=" icon-qrcode" aria-hidden="true"></i>LUCAS’HOME</span>

              <img src="../assets/img/erweima.jpg" alt="扫一扫">
            </a>
          </div>
          <div class="tb-2 col-md-5 text-center text-muted">
           <span class="number"> <i class="icon-mobile-phone"style="width:10px;"></i>134-5045-5728（服务时间：10:00-22:00）</span>
          </div>
          <div class="tb-3 col-md-2 text-center ">
            <a href="#" class="number">常见问题</a>
            <a href="#" class="number">网站登录</a>
          </div>
          <div class="tb-4 col-md-3 text-center">
            <a href="#" class="btn btn-register btn-sm btn-danger">免费注册</a>
            <a href="#" class="text-muted" data-toggle="modal" data-target=".modal"><i class="icon-user"></i>登录</a>

          </div>
        </div>
      </div>
    </div>
    <!-- /通栏菜单 -->
  </div>
</template>

<script>
</script>

<style>
	.topbar {
	  border-bottom: 1px solid #e0e0e0;
	  line-height: 40px;
    background: #00C5CD;
    font-size: 10px;
	}
.number{
  color: #1B1B1B;
  font-size: 13px;
}


	.topbar .tb-1 > a {
	  text-decoration: none;
	  position: relative;
	  z-index: 999;
	}

	.topbar .tb-1 > a > img {
	  display: none;
	}

	.topbar .tb-1:hover > a > img {
	  display: block;
	  position: absolute;
	  z-index: 1;
	  /*top: 14px;*/
	  left: 0;
    width:100px;
    height:100px;
	}

	.topbar .tb-4 > .text-muted {
	  margin-left: 15px;
	  font-size: 18px;
    font-weight: 600;
	}

	.topbar .row > div + div {
	  border-left: 1px solid #e0e0e0;
	}
  .text{
    font-size:18px;
    font-weight: 600;
    color:black;
    font-family:"estrangelo edessa";
  }
</style>
