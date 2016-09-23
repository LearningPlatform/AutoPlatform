autoTest.factory('CaseModel',function($http) {
    var caseServices = {}

    caseServices.getSuiteList = function ($scope,id) {
        $http.post('suite_list/',{
            "pro_id":id
        }).success(function(response){
            $scope.suiteList = response.data;
        });
    }

    caseServices.getModelList = function ($scope,id) {
        $http.post('model_list/',{
            pro_id: id
        }).success(function(response){
            $scope.modelList = response.data;
        })
    }

    caseServices.getApiList = function ($scope,id) {
        $http.post('api_listPro/',{
            pro_id: id
        }).success(function(response){
            $scope.apiList = response.data;
            for(var i=0;i<$scope.apiList.length;i++){
                $scope.apiList[i].api_param = $scope.apiList[i].api_param.split(",")
            }
        })
    }

    caseServices.getCaseOfApi = function ($scope,id) {
         $http.post('case_listofApi/',{
            api_id: id,
        }).success(function (response) {
            $scope.caseNameList=response.data;
        });
    }

    caseServices.saveReqParam = function ($scope,index,id,api_id) {
        $http.post('case_saveReq/',{
            case_id: id,
            api_id: api_id,
            input_data:$scope.reqParam
        }).success(function (response) {
            $scope.caseList=response.data;
        });
    }

    caseServices.saveApi = function ($scope,id) {
        $http.post('api_save/',{
            pro_id: id,
            model_id : $scope.api.currmodel.id,
            api_name : $scope.api.currname,
            api_protocol : $scope.api.currprotocol,
            api_method :$scope.api.currmethod,
            api_url :$scope.api.currurl,
            api_type :$scope.api.currtype,
            api_desc : $scope.api.currdesc,
            api_param :$scope.api.currparam
        }).success(function (response) {
            $scope.apiList=response.data;
        });
    }

    caseServices.saveModel = function ($scope,id) {
        $http.post('model_save/',{
            pro_id: id,
            model_name:$scope.pro_model.currname,
            model_desc:$scope.pro_model.currdesc,
        }).success(function (response) {
            $scope.modelList=response.data;
        });
    }

    caseServices.saveSuite = function ($scope,id) {
        $http.post('suite_save/',{
            pro_id: id,
            suite_name:$scope.suite.currName,
            suite_desc:$scope.suite.currDesc,
        }).success(function (response) {
            $scope.suiteList=response.data;
        });
    }

    caseServices.saveCaseInfo = function ($scope,id) {
        $http.post('case_saveInfo/',{
            case_name:$scope.case.currName,
            pro_id: id,
            suite_list:$scope.case.suite,
            api_id:$scope.case.currApi.id,
            case_desc:$scope.case.currDesc
        });
    }

    return caseServices;
})
