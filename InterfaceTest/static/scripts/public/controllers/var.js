//项目变量控制器
autoTest.controller("proVarCtrl",function($scope,$http,$cookieStore) {
    $scope.varInfoShow = true
    $scope.var={
        currVarName:"",
        currVarType:"",
        currVarValue:[{
            value:"",
            currEnv:{
                env_desc:"",
                env_name:"",
                id:"",
                pro_id:""
            }
        }],
        currVarDesc:""
    };
    $scope.showtableid2=0;
    $scope.showtable = false;
    $scope.showtable2 = false;
    $scope.showDivType = "evn";
    $scope.evnactive = 'active';
    $scope.varactive = 'disactive';
    $scope.varType=["String","Integer","Float","Boolean"];

    $http.post('env_list/',{
        "pro_id":$cookieStore.get("currProID")
    }).success(function(response){
        $scope.envList = response.data;
    });

    $scope.getEnvVar = function(id){

        if(id==$scope.showtableid){
            $scope.showtable = !$scope.showtable
        }else{

            $http.post('env_varlist/',{
                "env_id":id
            }).success(function(response){
                $scope.envVarList = response.data;
                $scope.showtable = true;
                $scope.showtableid = id;
            })
        }
    };

    $scope.getVarEnv = function(id){
        if(id==$scope.showtableid2){
            $scope.showtable2 = !$scope.showtable2
        }else{
            $http.post('var_envlist/',{
                "var_id":id
            }).success(function(response){
                $scope.varEnvList = response.data;
                $scope.showtable2 = true;
                $scope.showtableid2 = id;

            })
        }
    };

    $scope.showEvnDiv = function(){
        $scope.evnactive = 'active';
        $scope.varactive = 'disactive';
        $http.post('env_list/',{
            "pro_id":$cookieStore.get("currProID")
        }).success(function(response){
            $scope.envList = response.data;
        });
        $scope.showDivType = "evn";
    };

    $scope.showVarDiv = function(){
        $scope.evnactive = 'disactive';
        $scope.varactive = 'active';
        $http.post("var_list/",{
            "pro_id": $cookieStore.get("currProID")
        }).success(function (response) {
            $scope.varList=response.data;
            $scope.showDivType = "var";
        });
    };

    $scope.addEnv = function(){
        $scope.env={
            env_name:"",
            env_desc:""
        };
        $("#envAddModal").modal("show");
    };
    $scope.addVar = function(){
        $scope.var={
            currVarName:"",
            currVarType:"",
            currVarValue:[{
                value:"",
                currEnv:{
                    env_desc:"",
                    env_name:"",
                    id:"",
                    pro_id:""
                }
            }],
            currVarDesc:""
        };
        $('#varAddModal').modal('show');
    };
    $scope.delInfo={
        env_id:"",
        var_id:""
    };

    $scope.delEnvCom = function (env_id,$event) {
        $("#delEnvModal").modal("show");
        $scope.delInfo.env_id = env_id;
        $event.stopPropagation();
    };

    $scope.delVarCom = function (var_id,$event) {
        $("#delVarModal").modal("show");
        $scope.delInfo.var_id=var_id;
        $event.stopPropagation();

    }

    $scope.showHo = false
    $scope.showBtn = function(id){
        $scope.showID = id
        $scope.showHo=true
    }
    $scope.hideBtn = function(id){
        $scope.showID = id
        $scope.showHo=false
    }


});
//项目变量增加环境弹出框控制器
autoTest.controller("addEnvCtrl",function($scope,$http,$cookieStore){

    $scope.saveEnv = function(){
        $http.post("env_save/",{
            "pro_id": $cookieStore.get("currProID"),
            "env_name": $scope.env.env_name,
            "env_desc": $scope.env.env_desc
        }).success(function (response) {
            $scope.$parent.envList=response.data;
        });
        $("#envAddModal").modal("hide");
    };
});
//项目变量增加变量弹出框控制器
autoTest.controller("addVarCtrl",function($scope,$http,$cookieStore){
    $scope.var={
        currVarName:"",
        currVarType:"",
        currVarValue:[{
            value:"",
            currEnv:{
                env_desc:"",
                env_name:"",
                id:"",
                pro_id:""
            }
        }],
        currVarDesc:""
    };
    $scope.saveVar = function(){
        for(var i=0;i<$scope.envList.length;i++){
            $scope.var.currVarValue[i].currEnv = $scope.envList[i]
        }
        $http.post("var_save/",{
            "pro_id": $cookieStore.get("currProID"),
            "var_name": $scope.var.currVarName,
            "var_desc": $scope.var.currVarDesc,
            "var_value": $scope.var.currVarValue,
            "var_type": $scope.var.currVarType

        }).success(function (response) {
            $scope.$parent.varList=response.data;
        });
        $("#varAddModal").modal("hide");
    }
});
//项目变量删除环境弹出框控制器
autoTest.controller("delEnvCtrl",function($scope,$http,$cookieStore){

    $scope.delEnv = function () {
        $http.post("env_del/",{
            "pro_id": $cookieStore.get("currProID"),
            "env_id":$scope.delInfo.env_id
        }).success(function (response) {
            $scope.$parent.envList = response.data
        });
        $("#delEnvModal").modal("hide");

    }
});
//项目变量删除变量弹出框控制器
autoTest.controller("delVarCtrl",function($scope,$http,$cookieStore){
    $scope.delVar = function () {
        $http.post("var_del/",{
            "pro_id": $cookieStore.get("currProID"),
            "var_id": $scope.delInfo.var_id,
        }).success(function (response) {
            $scope.$parent.varList = response.data;
        });
        $("#delVarModal").modal("hide");

    }
});

