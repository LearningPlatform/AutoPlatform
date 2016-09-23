//平台首页控制器
autoTest.controller("proListCtrl",function($scope,$http,$rootScope,$cookies,$cookieStore){
    var delID = 0;//设置删除的id
    var saveType = 0;//确定项目是新建1还是编辑2

    $scope.pro={
        pro_id:0,
        pro_name:"",
        pro_desc:""
    };

    //默认设置项目导航id为0
    $cookieStore.put("activeNav",0);

    //获取项目列表数据
    $http.get("pro_list/").success(function(response) {
        $scope.proList=response.data;
    });

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
        $http.post("pro_get/",{
            "pro_id": id
        }).success(function(response){
            $scope.pro.pro_id = response.data.id;
            $scope.pro.pro_name = response.data.pro_name;
            $scope.pro.pro_desc = response.data.pro_desc;
        });
        $('#myModal').modal('show');
        saveType = 2;
    };

    //删除弹框，设置删除项目的id
    $scope.delProCom = function(id){
        $('#comModal').modal('show');
        delID = id;
    };

    //保存
    $scope.savePro = function(){
        $http.post("pro_save/",{
            "type":saveType,
            "pro_id": $scope.pro.pro_id,
            "pro_name": $scope.pro.pro_name,
            "pro_desc": $scope.pro.pro_desc
        }).success(function (response) {
            $scope.proList=response.data;
        });
        $('#myModal').modal('hide');
    };

    //向后台请求，删除对应id的项目
    $scope.delPro = function () {
         $http.post("pro_del/",{
            "pro_id": delID,
        }).success(function (response) {
            $scope.proList=response.data;
        });
        $('#comModal').modal('hide');
    }
});
