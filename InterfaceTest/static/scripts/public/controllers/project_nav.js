//项目顶部控制器
autoTest.controller("proTopCtrl",function($scope,$http,$rootScope,$cookieStore){
    $scope.pro={
        pro_id:$cookieStore.get("currProID"),
        pro_name:"",
        pro_desc:""
    };
    //获取项目列表数据
    $http.post("pro_get/",{
        "pro_id": $cookieStore.get("currProID")
    }).success(function(response){
        $scope.pro.pro_id = response.data.id;
        $scope.pro.pro_name = response.data.pro_name;
        $scope.pro.pro_desc = response.data.pro_desc;
    });

});

//项目测试用例详情
autoTest.controller("navCtrl",function($scope,$http,$rootScope,$cookieStore,$timeout){
    $scope.activeList=["active","disactive","disactive","disactive","disactive","disactive","disactive","disactive","disactive"]

    $timeout(function(){
        var id = $cookieStore.get('activeNav');
        for (var i=0;i<9;i++){
            $scope.activeList[i]="disactive";
        }
        $scope.activeList[id]='active';
    });
    $scope.liactive = function(id) {
        $cookieStore.put("activeNav",id);
        for (var i=0;i<9;i++){
            $scope.activeList[i]="disactive";
        }
        $scope.activeList[id]='active';
    }
});