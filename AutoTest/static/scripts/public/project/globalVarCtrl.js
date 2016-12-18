myApp.controller('globalVarCtrl',function($scope,$http,$cookieStore,$timeout){
    var pro_id = $cookieStore.get("currProID");
    var envId=0;
    var varId=0;
    $scope.varType=["String","Number","Array","Boolean"];
    $scope.varInfoShow=true;
    $scope.showVarCom=false;
    $scope.showVar=[];
    $scope.showEnv=[];
    $scope.envList="";
    $scope.env={
        pro_id:pro_id,
        env_id:0,
        env_name:'',
        env_desc:''
    };
    $scope.envVarList="";
    $scope.varList="";
    $scope.var={
        pro_id:pro_id,
        var_id:0,
        var_name:'',
        var_type:'',
        var_desc:'',
        value:[{
            env_id:0,
            env_name:"",
            env_desc:"",
            var_value:""
        }]
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
                for(var i=0;i<$scope.envList.length;i++){
                    $scope.showVar[i]=false;
                }
            }else{
                alert(response.msg);
            }
        });
        $http.post('project/var/list', {
             "pro_id": pro_id
        }).success(function (response) {
            if(response.code==1) {
                $scope.varList = response.data;
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
                 $scope.showVar=[];
                 for(var i=0;i<$scope.envList.length;i++){
                    $scope.showVar[i]=false;
                 }
             }else{
                alert(response.msg);
            }
         });
        $http.post('project/var/list', {
             "pro_id": pro_id
        }).success(function (response) {
            if(response.code==1) {
                $scope.varList = response.data;
                $scope.showEnv=[];
                 for(var i=0;i<$scope.varList.length;i++){
                    $scope.showEnv[i]=false;
                 }
            }else{
                alert(response.msg);
            }
        });
        $scope.showVarCom=true;
        $scope.showEnvCom=false;
    }

    $scope.showVarDiv=function(){
        //$scope.showVar=false;
        $scope.varactive="active";
        $scope.evnactive="disactive";
        $scope.showVarCom=false;
        $scope.showEnvCom=true;
        $http.post('project/var/list', {
             "pro_id": pro_id
        }).success(function (response) {
            if(response.code==1) {
                $scope.varList = response.data;
                $scope.showEnv=[];
                 for(var i=0;i<$scope.varList.length;i++){
                    $scope.showEnv[i]=false;
                 }
            }else{
                alert(response.msg);
            }
        });
        $http.post('project/env/list', {
             "pro_id": pro_id
        }).success(function (response) {
             if(response.code==1) {
                 $scope.envList = response.data;
                 $scope.showVar=[];
                 for(var i=0;i<$scope.envList.length;i++){
                    $scope.showVar[i]=false;
                 }
             }else{
                alert(response.msg);
            }
        });
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
                             $scope.showVar=[];
                             for(var i=0;i<$scope.envList.length;i++){
                                 $scope.showVar[i]=false;
                             }
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
        $("#cfModalEnv").modal();
        envId=id;
    }

    $scope.delEnv=function(){
        $("#cfModalEnv").modal('hide');
        $http.post('project/env/delete',{
            "env_id":envId,
        }).success(function (response1) {
            if(response1.code==1){
                $http.post('project/env/list', {
                     "pro_id": pro_id
                }).success(function (response) {
                     if(response.code==1) {
                         $scope.envList = response.data;
                         $scope.showVar=[];
                         for(var i=0;i<$scope.envList.length;i++){
                             $scope.showVar[i]=false;
                         }
                     }else{
                        alert(response.msg);
                    }
                });
            }else{
                alert(response1.msg);
            }
        });
    }

    $scope.getEnvVar=function(id,index){
        for(var i=0;i<$scope.showVar.length;i++){
            if(i!=index){
                $scope.showVar[i]=false;
            }
        }
        $scope.showVar[index]=!$scope.showVar[index];
        $http.post('project/env/varList',{
            "env_id":id
        }).success(function(response){
            if(response.code==1){
                $scope.envVarList=response.data;
            }else{
                alert(response.msg);
            }
        });
    }

    $scope.delVarCom=function(envId,varId){
        $http.post('project/var/detail',{
            "var_id":varId
        }).success(function (response){
            if(response.code==1){
                $scope.var=response.data;
            } else {
                alert(response.msg);
            }
        });
        for(var i=0;i<$scope.var.value.length;i++){
            if($scope.var.value[i].env_id==envId){
                $scope.var.value[i].var_value='该环境下'+$scope.var.var_name+'变量不存在';
            }
        }
        $http.post('project/var/edit',{
            "pro_id":pro_id,
            "var_id":$scope.var.var_id,
            "var_name":$scope.var.var_name,
            "var_type":$scope.var.var_type,
            "var_desc":$scope.var.var_desc,
            "value":$scope.var.value
        }).success(function (response) {
            if(response.code==1){
                $http.post('project/env/varList',{
                    "env_id":envId
                }).success(function(response){
                    if(response.code==1){
                        $scope.envVarList=response.data;
                    }else{
                        alert(response.msg);
                    }
                });
            }else{
                alert(response.msg);
            }
        });
    }

    $scope.addVar=function(){
        $scope.var={
            pro_id:pro_id,
            var_id:"",
            var_name:'',
            var_type:'无',
            var_desc:'',
            value:[{
                env_id:"",
                env_name:"",
                env_desc:"",
                var_value:""
            }]
        };
        $("#varAddModal").modal();
    }

    $scope.saveVar=function(){
        if($scope.var.var_name==null){
            $scope.var.var_name=" ";
        }
        if($scope.var.var_desc==null){
            $scope.var.var_desc="无";
        }
        if($scope.var.var_type=="无"){
            $scope.var.var_type="String";
        }
        for(var i=0;i<$scope.envList.length;i++){
            $scope.var.value[i].env_id=$scope.envList[i].env_id;
            $scope.var.value[i].env_name=$scope.envList[i].env_name;
            $scope.var.value[i].env_desc=$scope.envList[i].env_desc;
        }
        $http.post('project/var/create',{
            "pro_id":pro_id,
            "var_name":$scope.var.var_name,
            "var_type":$scope.var.var_type,
            "var_desc":$scope.var.var_desc,
            "value":$scope.var.value
        }).success(function (response) {
            if(response.code==1){
                $("#varAddModal").modal('hide');
                $http.post('project/var/list', {
                     "pro_id": pro_id
                }).success(function (response1) {
                     if(response1.code==1) {
                         $scope.varList = response1.data;
                         $scope.showEnv=[];
                         for(var i=0;i<$scope.varList.length;i++){
                            $scope.showEnv[i]=false;
                         }
                     }else{
                        alert(response1.msg);
                    }
                });
            } else{
                alert(response.msg);
            }
        });
    }

    $scope.editVar=function(id){
        $http.post('project/var/detail',{
            "var_id":id
        }).success(function (response){
            if(response.code==1){
                $scope.var=response.data;
            } else {
                alert(response.msg);
            }
        });
        $("#editvarModal").modal();
    }

    $scope.saveVarEdit=function(id){
        if($scope.var.var_desc==""){
            $scope.var.var_desc="无";
        }
        for(var i=0;i<$scope.envList.length;i++){
            $scope.var.value[i].env_id=$scope.envList[i].env_id;
            $scope.var.value[i].env_name=$scope.envList[i].env_name;
            $scope.var.value[i].env_desc=$scope.envList[i].env_desc;
        }
        $http.post('project/var/edit',{
            "pro_id":pro_id,
            "var_id":id,
            "var_name":$scope.var.var_name,
            "var_type":$scope.var.var_type,
            "var_desc":$scope.var.var_desc,
            "value":$scope.var.value
        }).success(function (response) {
            if(response.code==1){
                $("#editvarModal").modal('hide');
                $http.post('project/var/list', {
                     "pro_id": pro_id
                }).success(function (response1) {
                     if(response1.code==1) {
                         $scope.varList = response1.data;
                         $scope.showEnv=[];
                         for(var i=0;i<$scope.varList.length;i++){
                            $scope.showEnv[i]=false;
                         }
                     }else{
                        alert(response1.msg);
                    }
                });
            } else{
                alert(response.msg);
            }
        });
    }

    $scope.getVarEnv=function(id,index){
        for(var i=0;i<$scope.showEnv.length;i++){
            if(i!=index){
                $scope.showEnv[i]=false;
            }
        }
        $scope.showEnv[index]=!$scope.showEnv[index];
        $http.post('project/var/detail',{
            "var_id":id
        }).success(function(response){
            if(response.code==1){
                $scope.var=response.data;
            }else{
                alert(response.msg);
            }
        });
    }

    $scope.delEnvCom=function(varId,envId){
        for(var i=0;i<$scope.var.value.length;i++){
            if($scope.var.value[i].env_id==envId){
                $scope.var.value[i].var_value='该环境下'+$scope.var.var_name+'变量不存在';
            }
        }
        $http.post('project/var/edit',{
            "pro_id":pro_id,
            "var_id":$scope.var.var_id,
            "var_name":$scope.var.var_name,
            "var_type":$scope.var.var_type,
            "var_desc":$scope.var.var_desc,
            "value":$scope.var.value
        }).success(function (response) {
            if(response.code==0){
                alert(response.msg);
            }
        });
    }

    $scope.cfDelVar=function(id){
        $("#cfModalVar").modal();
        varId=id;
    }

    $scope.delVar=function(){
        $("#cfModalVar").modal('hide');
        $http.post('project/var/delete',{
            "var_id":varId,
        }).success(function (response1) {
            if(response1.code==1){
                $http.post('project/var/list', {
                     "pro_id": pro_id
                }).success(function (response) {
                     if(response.code==1) {
                         $scope.varList = response.data;
                         $scope.showEnv=[];
                         for(var i=0;i<$scope.varList.length;i++){
                            $scope.showEnv[i]=false;
                         }
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
