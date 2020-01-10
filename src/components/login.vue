<template>
  <!-- 登录对话框 -->
  <div class="modal fade">
    <div class="modal-dialog modal-md">
      <div class="modal-content">
        <div class="modal-header">
          <h4 class="modal-title">请登录</h4>
          <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">×</span></button>
        </div>
        <div class="modal-body">
          <form class="form-horizontal" action="#">
            <div class="form-group row">
              <label for="inputEmail3" class="col-sm-2 control-label text-muted">账号</label>
              <div class="col-sm-10">
                <input type="tel" class="form-control" id="inputEmail3" placeholder="请输入你的手机号">
              </div>
            </div>
            <div class="form-group row">
              <label for="inputPassword3" class="col-sm-2 control-label">密码</label>
              <div class="col-sm-10">
                <input type="password" class="form-control" id="inputPassword3" placeholder="请输入你的密码">
              </div>
            </div>
            <div class="form-group row location">

              <div class="col-sm-offset-2 col-sm-6 position">
                <div class="checkbox">
                  <label>
                    <input type="checkbox">记住密码
                  </label>
                </div>
                <button type="submit" class="btn btn-block btn-danger text-center">登录</button>
              </div>

            </div>

          </form>
        </div>

      </div>
    </div>
  </div>
  <!-- /登录对话框 -->
</template>

<script>
</script>

<style>
  .modal-title {
    float: left;

  }
.location{
  display: flex;
  justify-content: center;
}
</style>
