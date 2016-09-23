//项目变量控制器
autoTest.controller("ProVarCtrl",function($scope,$http,$cookieStore,VarModel) {
    var pro_id = $cookieStore.get("currProID")
    $scope.varInfoShow = true
    $scope.envVarList = []
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

    VarModel.getEnvList($scope,pro_id)

    $scope.getEnvVar = function(id){
        if(id==$scope.showtableid){
            $scope.showtable = !$scope.showtable
        }else{
            VarModel.getVarOfEnv($scope,id)
        }
    };

    $scope.getVarEnv = function(id){
        if(id==$scope.showtableid2){
            $scope.showtable2 = !$scope.showtable2
        }else{
            VarModel.getEnvOfVar($scope,id)
        }
    };

    $scope.showEvnDiv = function(){
        $scope.evnactive = 'active';
        $scope.varactive = 'disactive';
        VarModel.getEnvList($scope,pro_id)
        $scope.showDivType = "evn";
    };

    $scope.showVarDiv = function(){
        $scope.evnactive = 'disactive';
        $scope.varactive = 'active';
        VarModel.getVarList($scope,pro_id)
        $scope.showDivType = "var";
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

    $scope.delEnvCom = function (env_id) {
        $("#delEnvModal").modal("show");
        $scope.delInfo.env_id = env_id;
    };

    $scope.delVarCom = function (var_id) {
        $("#delVarModal").modal("show");
        $scope.delInfo.var_id=var_id;

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

    $scope.saveEnv = function(){
        VarModel.saveEvn($scope,pro_id)
        $("#envAddModal").modal("hide");
    };

    $scope.saveVar = function(){
        for(var i=0;i<$scope.envList.length;i++){
            $scope.var.currVarValue[i].currEnv = $scope.envList[i]
        }
        VarModel.saveVar($scope,pro_id)
        $("#varAddModal").modal("hide");
    }

    $scope.delEnv = function () {
        VarModel.delEnv($scope,pro_id)
        $("#delEnvModal").modal("hide");
    }

    $scope.delVar = function () {
        VarModel.delVar($scope,pro_id)
        $("#delVarModal").modal("hide");

    }

});
