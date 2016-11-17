myApp.controller('testReportCtrl',function($scope,$http,$cookieStore,$timeout) {
    var pro_id = $cookieStore.get("currProID");
    $scope.List=['active'];
    $scope.reportDetal=[];
    $scope.suiteList="";
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
    $scope.api={
        "api_param": "username,pwd",
        "api_id": 1,
        "module_id": 1,
        "pro_id": pro_id,
        "api_url": "{host}/login",
        "api_method": "post",
        "api_type": "34",
        "api_protocol": "http",
        "api_name": "登录接口",
        "api_desc": "登录"
    }

     $timeout(function(){
         $http.post('project/suite/list',{
             "pro_id":pro_id
         }).success(function(response){
             if(response.code==1){
                 $scope.suiteList=response.data;
             }else{
                 alert(response.msg)
             }
         })
         $scope.repDetail=false;
         $scope.repList=true;
         $http.post('project/result/list',{
             "pro_id":pro_id
         }).success(function(response1){
             if(response1.code=1){
                 $scope.resultList=response1.data;
             }else{
                 alert(response.msg)
             }
         })
     })

    $scope.showDetail=function(obj){
        console.log(obj.result_id)
        $scope.result=obj;
        $scope.repList=false;
        $scope.repDetail=true;
        $http.post('project/result/detailList',{
             "result_id":obj.result_id
        }).success(function(response){
             if(response.code=1){
                 $scope.allResult=response.data;
                 $scope.resultStr="";
                 for(var i=0; i<$scope.allResult.length-1;i++){
                     $scope.reportDetal[i]=false;
                 }
             }else{
                 alert(response1.msg)
             }
        })
    }

    $scope.showReport=function(obj,index){
        $http.post("project/api/detail",{
            "api_id":obj.api_id
        }).success(function(response){
            if(response.code==1){
                $scope.api=response.data;
            }else{
                alert(response.msg);
            }
        })
        $scope.reportDetal[index]=!$scope.reportDetal[index];
    }

    $scope.returnList=function(){
         $scope.repDetail=false;
         $scope.repList=true;
         $http.post('project/result/list',{
             "pro_id":pro_id
         }).success(function(response1){
             if(response1.code=1){
                 $scope.resultList=response1.data;
             }else{
                 alert(response.msg)
             }
         })
    }

    /*
    $scope.inquiry=function(str){
        for (var i=0; i<$scope.resultList.length;i++){
            if($scope.resultList[i].report_name==str){
                $scope.result=$scope.resultList[i];
            }
            break;
        }
        console.log($scope.result)
        $http.post('project/result/detailList',{
            "result_id":$scope.result.result_id
        }).success(function(response){
            if(response.code=1){
                $scope.allResult=response.data;
                console.log($scope.allResult)
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
    }*/

})
