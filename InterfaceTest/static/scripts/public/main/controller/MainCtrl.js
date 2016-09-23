autoTest.controller("MainCtrl",function($scope,$cookieStore,ProjectModel) {
    var saveType = 0;//确定项目是新建1还是编辑2
    var delID = 0;//设置删除的id
    $scope.pro={
        pro_id:0,
        pro_name:"",
        pro_desc:""
    };
    ProjectModel.getProList($scope);

    //默认设置项目导航id为0
    $cookieStore.put("activeNav",0);

    //将进入的项目存入cookie
    $scope.recodeId=function (id) {
        $cookieStore.put("currProID",id);
    };

    //添加项目弹窗，并且设置为保存的类型为1
    $scope.addPro = function(){
        $scope.pro={};
        $('#myModal').modal('show');
        saveType = 1;
    };

     //编辑弹框，通过id获取项目的信息，并且赋给$scope，以便填充至弹框。
    //设置保存类型为编辑2
    $scope.editPro = function(id){
        ProjectModel.getPro($scope,id)
        $('#myModal').modal('show');
        saveType = 2;
    };

    //保存
    $scope.savePro = function(){
        ProjectModel.addPro($scope,saveType)
        $('#myModal').modal('hide');
    }

     //删除弹框，设置删除项目的id
    $scope.delProCom = function(id){
        $('#comModal').modal('show');
        delID = id;
    };

    //向后台请求，删除对应id的项目
    $scope.delPro = function () {
         ProjectModel.delPro($scope,delID)
        $('#comModal').modal('hide');
    }

});
