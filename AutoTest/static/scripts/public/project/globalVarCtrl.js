myApp.controller('globalVarCtrl',function($scope,$http,$cookieStore,$timeout){
    var pro_id = $cookieStore.get("currProID");
    $scope.varInfoShow=true;
    $scope.showVarCom=false;
    $scope.showVar=false;
    $scope.envList="";
    $scope.env={
        pro_id:pro_id,
        id:0,
        env_name:'',
        env_desc:''
    };

    $scope.var={
        pro_id:pro_id,
        var_id:0,
        var_name:'',
        var_desc:''
    };


    $timeout(function() {
        $scope.evnactive="active";
        $scope.varactive="disactive";
        $scope.showVarCom=true;
        $scope.showEnvCom=false;
        $http.post('project/env/list', {
             "pro_id": pro_id
        }).success(function (response) {
            if(response.code==1) {
                $scope.envList = response.data;
            }else{
                alert(response.msg);
            }
        });
    })

    $scope.showEvnDiv=function(){
        $scope.evnactive="active";
        $scope.varactive="disactive";
         $http.post('project/env/list', {
             "pro_id": pro_id
         }).success(function (response) {
             if(response.code==1) {
                 $scope.envList = response.data;
             }else{
                alert(response.msg);
            }
         });
        $scope.showVarCom=true;
        $scope.showEnvCom=false;
    }

    $scope.showVarDiv=function(){
        $scope.varactive="active";
        $scope.evnactive="disactive";
        $scope.showVarCom=false;
        $scope.showEnvCom=true;
    }

    $scope.addEnv=function(){
        $scope.env="";
        $("#envAddModal").modal();
    }

    $scope.saveEnv=function(){
        if($scope.env.env_name==null){
                $scope.env.env_name="";
            }
            if($scope.env.env_desc==null){
                $scope.env.env_desc="无";
            }
            $http.post('project/env/create',{
                "pro_id":pro_id,
                "env_name":$scope.env.env_name,
                "env_desc":$scope.env.env_desc
            }).success(function (response) {
                if(response.code==1){
                    $("#envAddModal").modal('hide');
                    $http.post('project/env/list', {
                         "pro_id": pro_id
                    }).success(function (response1) {
                         if(response1.code==1) {
                             $scope.envList = response1.data;
                         }else{
                            alert(response1.msg);
                        }
                    });
                } else{
                    alert(response.msg);
                }
        });
    }

    $scope.editEnv=function(id){
        $http.post('project/env/detail',{
            "env_id":id
        }).success(function (response){
            if(response.code==1){
                $scope.env=response.data;
            } else {
                alert(response.msg);
            }
        });
        $("#editEnvModal").modal();
    }

    $scope.saveEnvEdit=function(id){
            console.log(id)
            if($scope.env.env_desc==""){
                $scope.env.env_desc="无";
            }
            $http.post('project/env/edit',{
                "env_id":id,
                "env_name":$scope.env.env_name,
                "env_desc":$scope.env.env_desc
            }).success(function (response) {
             if(response.code==1){
                    $("#editEnvModal").modal('hide');
                    $http.post('project/env/list', {
                         "pro_id": pro_id
                    }).success(function (response1) {
                        if(response1.code==1) {
                            $scope.envList = response1.data;
                        }else{
                            alert(response1.msg);
                        }
                    });
                } else{
                    alert(response.msg);
                }
        });
        }

    $scope.cfDel=function(id){
        $("#cfModal").modal();
        $http.post('project/env/detail',{
            "env_id":id
        }).success(function (response){
            $scope.env=response.data;
        });
    }

    $scope.delEnv=function(id){
        $("#cfModal").modal('hide');
        $http.post('project/env/delete',{
            "env_id":id,
        }).success(function (response1) {
            if(response1.code==1){
                $http.get('project/list').success(function(response){
                    $scope.proList=response.data;
                })
            }else{
                alert(response1.msg);
            }
        });
    }

    $scope.addVar=function(){
        $scope.var="";
        $("#varAddModal").modal();

    }

})
