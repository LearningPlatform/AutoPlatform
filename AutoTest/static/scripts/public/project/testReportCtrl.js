myApp.controller('testReportCtrl',function($scope,$http,$cookieStore,$timeout) {
    var pro_id = $cookieStore.get("currProID");
    $scope.List=['active'];
    $scope.resultList="";
    $scope.result={
        "result_id": 1,
        "suite_id": 1,
        "start_time": "1478617457",
        "pass_num": 1,
        "report_name": "test",
        "end_time": "1478617457",
        "fail_num": 1,
        "pro_id": 1
    }
    $scope.allResult=[];

     $timeout(function(){
         $http.post('project/result/list',{
             "pro_id":pro_id
         }).success(function(response1){
             if(response1.code=1){
                 $scope.resultList=response1.data;
                 $scope.result=$scope.resultList[0];
                 $http.post('project/result/detailList',{
                     "result_id":$scope.result.result_id
                 }).success(function(response){
                     if(response.code=1){
                         $scope.allResult=response.data;
                         $scope.resultStr="";
                         if($scope.allResult.length>1){
                             for(var i=0; i<$scope.allResult.length-1;i++){
                                 var str= angular.toJson($scope.allResult[i]);
                                 $scope.resultStr = $scope.resultStr + str + " ";
                             }
                             str= angular.toJson($scope.allResult[$scope.allResult.length-1]);
                             $scope.resultStr=$scope.resultStr+str;
                         }else{
                             str= angular.toJson($scope.allResult[$scope.allResult.length-1]);
                             $scope.resultStr=$scope.resultStr+str;
                         }
                     }else{
                         alert(response1.msg)
                     }
                 })



             }else{
                 alert(response.msg)
             }
         })
     })

    $scope.active=function(id,obj){
        $scope.result=$scope.resultList[id];
        for(var i=0;i<$scope.resultList.length;i++){
            $scope.List[i]="disactive";
        }
        $scope.List[id]="active";
        $http.post('project/result/detailList',{
            "result_id":obj.result_id
        }).success(function(response){
            if(response.code=1){
                $scope.allResult=response.data;
                $scope.resultStr="";
                if($scope.allResult.length>1){
                    for(var i=0; i<$scope.allResult.length-1;i++){
                        var str= angular.toJson($scope.allResult[i]);
                        $scope.resultStr = $scope.resultStr + str + " ";
                    }
                    str= angular.toJson($scope.allResult[$scope.allResult.length-1]);
                    $scope.resultStr=$scope.resultStr+str;
                }else{
                    str= angular.toJson($scope.allResult[$scope.allResult.length-1]);
                    $scope.resultStr=$scope.resultStr+str;
                }
            }else{
                alert(response.msg)
            }
        })

    }

})
