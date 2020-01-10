<template>
    <div class="container-fluid bg">
      <div class="row">
        <div class="col-md-3">
         <img src="../assets/img/1.jpg" class="img-thumbnail photo1">
        </div>
        <div class="col-md-6">
             <form class=" form-inline row search"action="#"  role="form">
              <div class="input-group input-group-lg  col-lg-10">
               <input type="text"placeholder="请输入你要搜索的商品" class="form-control input-lg" >
               <button type="submit" class="btn-default btn btn-info ">搜索</button>
              </div>
             </form>
             <div>
               <ul class="row low_text">
                  <li class="col-sm-2"><a href="#">广州恒大</a></li>
                  <li class="col-sm-2"><a href="#">林俊杰</a></li>
                  <li class="col-sm-2"><a href="#">一淘限时抢</a></li>
                  <li class="col-sm-3"><a href="#">天猫双十一狂欢节</a></li>
                  <li class="col-sm-2"><a href="#">周杰伦</a></li>
               </ul>
             </div>
        </div>
        <div class="col-md-3">
          <img src="../assets/img/2.jpg" class="img-thumbnail photo2">
        </div>
      </div>
    </div>
</template>

<script>
</script>

<style>
	.bg{
		background:paleturquoise;
	}
.search{
  display: flex;
  justify-content: center;
  margin-top:40px;
}
.phpto1{
  margin-left:50px;
  height: 65px;
  }
.phpto2{
  margin-right:50px;
  height: 65px;
  }
  .low_text{
   display: flex;
   margin-left: 60px;

  }
  .low_text a{
    font-size: 20px;
    color: red;

  }
</style>
