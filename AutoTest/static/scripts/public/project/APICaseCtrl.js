myApp.controller('APICaseCtrl',function($scope,$http,$cookieStore,$timeout) {
    var pro_id = $cookieStore.get("currProID");
    var moduleId=0;
    $scope.List=["active"];
    $scope.varInfoShow=true;
    $scope.moduleList="";
    $scope.module={
        "module_desc": "",
        "module_id": "",
        "pro_id": pro_id,
        "module_name": ""
    }
    $timeout(function(){
        $http.post('project/module/list', {
             "pro_id": pro_id
        }).success(function (response) {
            if(response.code==1) {
                $scope.moduleList = response.data;
            }else{
                alert(response.msg);
            }
        });
        for(var i=0;i<$scope.moduleList.length;i++){
            $scope.List[i+1]="disactive"
        }
        $scope.List[0]="active"
    })

    $scope.showAll=function(){
        for(var i=0;i<$scope.moduleList.length;i++){
            $scope.List[i+1]="disactive"
        }
        $scope.List[0]="active";
    }

    $scope.active1 = function(id) {
         for(var i=0;i<$scope.moduleList.length;i++){
            $scope.List[i+1]="disactive"
         }
         $scope.List[id+1]='active';
         $scope.List[0]="disactive";
         $scope.module=$scope.moduleList[id];
    }

    $scope.addModule=function(){
        $scope.module="";
        $("#AddModule").modal();
    }

    $scope.saveModule=function(){
        if($scope.module.module_name==null){
            $scope.module.module_name="";
        }
        if($scope.module.module_desc==null){
            $scope.module.module_desc="无";
        }
        $http.post('project/module/create',{
            "pro_id":pro_id,
            "module_name":$scope.module.module_name,
            "module_desc":$scope.module.module_desc
        }).success(function (response) {
            if(response.code==1){
                $("#AddModule").modal('hide');
                $http.post('project/module/list', {
                     "pro_id": pro_id
                }).success(function (response1) {
                     if(response1.code==1) {
                         $scope.moduleList = response1.data;
                     }else{
                        alert(response1.msg);
                    }
                });
            } else{
                alert(response.msg);
            }
        });
    }

     $scope.editModule=function(id){
         $("#editModule").modal();
     }

     $scope.saveModule=function(){
        if($scope.module.module_name==null){
            $scope.module.module_name="";
        }
        if($scope.module.module_desc==null){
            $scope.module.module_desc="无";
        }
        $http.post('project/module/create',{
            "pro_id":pro_id,
            "module_name":$scope.module.module_name,
            "module_desc":$scope.module.module_desc
        }).success(function (response) {
            if(response.code==1){
                $("#AddModule").modal('hide');
                $http.post('project/module/list', {
                     "pro_id": pro_id
                }).success(function (response1) {
                     if(response1.code==1) {
                         $scope.moduleList = response1.data;
                     }else{
                        alert(response1.msg);
                    }
                });
            } else{
                alert(response.msg);
            }
        });
     }

     $scope.cfModoule=function(id){
        $("#cfModule").modal();
        moduleId=id;
    }

    $scope.delModule=function(){
        $("#cfModule").modal('hide');
        $http.post('project/module/delete',{
            "module_id":moduleId,
        }).success(function (response1) {
            if(response1.code==1){
                $http.post('project/module/list', {
                     "pro_id": pro_id
                }).success(function (response) {
                     if(response.code==1) {
                         $scope.moduleList = response.data;
                     }else{
                        alert(response.msg);
                    }
                });
            }else{
                alert(response1.msg);
            }
        });
    }
})
