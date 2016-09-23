//项目测试用例详情
autoTest.controller("ProNavCtrl",function($scope,$cookieStore,$timeout,NavModel){
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