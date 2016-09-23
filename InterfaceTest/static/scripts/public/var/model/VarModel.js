autoTest.factory('VarModel',function($http){
    var varServices = {};

    varServices.getEnvList = function ($scope,id) {
        $http.post('env_list/',{
            "pro_id":id
        }).success(function(response){
            $scope.envList = response.data;
        });
    };

    varServices.getVarList = function ($scope,id) {
        $http.post("var_list/",{
            "pro_id": id
        }).success(function (response) {
            $scope.varList=response.data;
        });
    };

    varServices.getVarOfEnv = function ($scope,id) {
        $http.post('env_varlist/',{
            "env_id":id
        }).success(function(response){
            $scope.envVarList = response.data;
            $scope.showtable = true;
            $scope.showtableid = id;
        })
    }

    varServices.getEnvOfVar = function ($scope,id) {
        $http.post('var_envlist/',{
            "var_id":id
        }).success(function(response){
            $scope.varEnvList = response.data;
            $scope.showtable2 = true;
            $scope.showtableid2 = id;

        })
    }

    varServices.saveEvn = function ($scope,id) {
        $http.post("env_save/",{
            "pro_id": id,
            "env_name": $scope.env.env_name,
            "env_desc": $scope.env.env_desc
        }).success(function (response) {
            $scope.envList=response.data;
        });
    }

    varServices.saveVar = function ($scope,id) {
        $http.post("var_save/",{
            "pro_id": id,
            "var_name": $scope.var.currVarName,
            "var_desc": $scope.var.currVarDesc,
            "var_value": $scope.var.currVarValue,
            "var_type": $scope.var.currVarType
        }).success(function (response) {
            $scope.varList=response.data;
        });
    }

    varServices.delEnv  = function ($scope,id) {
        $http.post("env_del/",{
            "pro_id": id,
            "env_id":$scope.delInfo.env_id
        }).success(function (response) {
            $scope.envList = response.data
        });
    }

    varServices.delVar = function($scope,id){
        $http.post("var_del/",{
            "pro_id": id,
            "var_id": $scope.delInfo.var_id,
        }).success(function (response) {
            $scope.varList = response.data;
        });
    }

    return varServices;
})
