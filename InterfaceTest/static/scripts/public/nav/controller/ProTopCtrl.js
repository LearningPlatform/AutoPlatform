//项目顶部控制器
autoTest.controller("ProTopCtrl",function($scope,$cookieStore,NavModel){
    var pro_id = $cookieStore.get("currProID")

    $scope.pro={};

    NavModel.getPro($scope,pro_id);

});
