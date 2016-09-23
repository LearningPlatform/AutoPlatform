//项目用例控制器
autoTest.controller("CaseCtrl",function($scope,$http,$location,$rootScope,$cookieStore) {
    $scope.modelList = []
    $scope.apiList = []
    $scope.suiteList=[]
    $scope.caseDivShow = true
    $scope.caseShow = false
    $scope.caseBaseInfoShow = false
    $scope.caseReqInfoShow = false
    $scope.caseResInfoShow = false
    $scope.editShow=true
    $scope.displayShow=false
    $scope.reqParam=[]

    //初始化模块列表
    $http.post('model_list/',{
        pro_id: $cookieStore.get("currProID")
    }).success(function(response){
        $scope.modelList = response.data;
    })

    //初始化接口列表
    $http.post('api_listPro/',{
        pro_id: $cookieStore.get("currProID")
    }).success(function(response){
        $scope.apiList = response.data;
        for(var i=0;i<$scope.apiList.length;i++){
            $scope.apiList[i].api_param = $scope.apiList[i].api_param.split(",")
        }
    })

    $http.post('suite_list/',{
        "pro_id":$cookieStore.get("currProID")
    }).success(function(response){
        $scope.suiteList = response.data;
    });

    //向下传播打开增加API的模态框
    $scope.openApiModal = function () {
        $scope.$broadcast('openApiModal');
    }
    //向下传播打开增加模块的模态框
    $scope.openModelModal = function () {
        $scope.$broadcast('openModelModal');
    }
    //向下传播打开增加模块的模态框
    $scope.openRunModal = function () {
        $scope.$broadcast('openRunModal');
    }
    //向下传播打开增加模块的模态框
    $scope.openSuiteModal = function () {
        $scope.$broadcast('openSuiteModal');
    }
    //向下传播打开增加模块的模态框
    $scope.openCaseModal = function () {
        $scope.$broadcast('openCaseModal');
    }

    $scope.getApiCase = function (id) {
        $http.post('case_listofApi/',{
            api_id: id,
        }).success(function (response) {
            $scope.caseNameList=response.data;
        });
        $scope.caseShow = true
        $scope.caseShowID = id;
    }

    $scope.getCaseInfo = function (id,index) {
        $http.post('case_info/',{
            case_id: id
        }).success(function(response){
            $scope.caseInfo = response.data;
            $scope.caseReqInfoShow = false
            $scope.caseResInfoShow = false
            $scope.caseBaseInfoShow = true
            $scope.caseInfoShowID = id;
            if($scope.caseInfo.is_set==1){
                var i = 0
                data1 = eval('(' + $scope.caseInfo.input_data + ')')
                console.log($scope.caseInfo.input_data)
                console.log( eval('(' + $scope.caseInfo.input_data + ')'))
                for(var o in eval('(' + $scope.caseInfo.input_data + ')')){
                    var reqParamBody = {
                        name: "",
                        type: "字符串",
                        value: ""
                    }
                    reqParamBody.name = o
                    reqParamBody.value = data1[o]
                    //reqParamBody.type = typeof data1[o]
                    switch(typeof data1[o]){
                        case "string":
                            reqParamBody.type = "字符串"
                            break;
                        case "number":
                            reqParamBody.type = "数字"
                            break;
                        case "boolean":
                            reqParamBody.type = "布尔型"
                            break;
                        }
                            $scope.reqParam[i] = reqParamBody
                            i++;
                    }
                console.log($scope.reqParam)
                $scope.editShow=false
                $scope.displayShow=true
            }if($scope.caseInfo.is_set==0) {
                for (var j = 0; j < $scope.apiList[index].api_param.length; j++) {
                    var reqParamBody = {
                        name: "",
                        type: "字符串",
                        value: ""
                    }
                    reqParamBody.name = $scope.apiList[index].api_param[j]
                    $scope.reqParam[j] = reqParamBody
                }
                console.log("未设置")
            }
            console.log($scope.reqParam)
        })

    }

    $scope.showBese = function (id) {
        if(id==1){
            $scope.caseReqInfoShow = false
            $scope.caseResInfoShow = false
            $scope.caseBaseInfoShow = true
        }
        if(id==2){
            $scope.caseResInfoShow = false
            $scope.caseBaseInfoShow = false
            $scope.caseReqInfoShow = true

        }
        if(id==3){
            $scope.caseReqInfoShow = false
            $scope.caseBaseInfoShow = false
            $scope.caseResInfoShow = true
        }
    }

    $scope.disEditParam = function () {
        $scope.editShow=false
        $scope.displayShow=true
    }
    $scope.editParam = function () {
        console.log($scope.reqParam)
        $scope.displayShow=false
        $scope.editShow=true
    }
    $scope.submitParam = function (index,id,api_id) {

        $http.post('case_saveReq/',{
            case_id: id,
            api_id: api_id,
            input_data:$scope.reqParam
        }).success(function (response) {
            $scope.caseList=response.data;
        });
        $scope.editShow=false
        $scope.displayShow=true
    }

    $scope.runCaseStart = function () {
        $http.post('run/',{
            api_id:5
        })
    }
})
autoTest.controller("ApiModalCtrl",function($scope,$http,$location,$rootScope,$cookieStore) {
    $scope.method = [
        "GET","POST","DELETE","PULL"
    ];
    $scope.type = [
        "JSON","TEXT","RAW"
    ];
    $scope.protocal = [
        "HTTP"
    ];
    $scope.api={
        currname:"",
        currprotocol:"HTTP",
        currmodel:{},
        currurl:"",
        currmethod:"GET",
        currtype:"JSON",
        currparam:[],
        currdesc:""
    }
    $scope.$on('openApiModal',function(){
        $scope.api.currmodel=$scope.modelList[0]
        $('#apiAddModal').modal('show')
    })
    $scope.saveApi = function(){
        $http.post('api_save/',{
            pro_id: $cookieStore.get("currProID"),
            model_id : $scope.api.currmodel.id,
            api_name : $scope.api.currname,
            api_protocol : $scope.api.currprotocol,
            api_method :$scope.api.currmethod,
            api_url :$scope.api.currurl,
            api_type :$scope.api.currtype,
            api_desc : $scope.api.currdesc,
            api_param :$scope.api.currparam
        }).success(function (response) {
            $scope.$parent.apiList=response.data;
        });
        $('#apiAddModal').modal("hide");
        $scope.api={
            currname:"",
            currmodel:$scope.modelList[0],
            currprotocol:"HTTP",
            currurl:"",
            currmethod:"GET",
            currtype:"JSON",
            currparam:[],
            currdesc:""
        }
    }
})
autoTest.controller("ModelModalCtrl",function($scope,$http,$location,$rootScope,$cookieStore) {
    $scope.pro_model={
        currname:"",
        currdesc:"",
    }

    $scope.$on('openModelModal',function(){
        $('#modelAddModal').modal('show')
    })

    $scope.saveModel = function(){
        $http.post('model_save/',{
            pro_id: $cookieStore.get("currProID"),
            model_name:$scope.pro_model.currname,
            model_desc:$scope.pro_model.currdesc,
        }).success(function (response) {
            $scope.$parent.modelList=response.data;
        });
        $("#modelAddModal").modal("hide");
        $scope.pro_model={
            currname:"",
            currdesc:"",
        }
    }
})
autoTest.controller("RunModalCtrl",function($scope,$http,$location,$rootScope,$cookieStore) {
    $scope.runCase={
        currReport:"",
        currEnv:{},
        currModel:{},
        currSuite:{},
        currDesc:"",
    }
    $scope.envList=[]
    $scope.$on('openRunModal',function(){
        $scope.runCase.currModel = $scope.modelList[0]

        $http.post('env_list/',{
            "pro_id":$cookieStore.get("currProID")
        }).success(function(response){
            $scope.envList = response.data;
            $scope.runCase.currEnv = $scope.envList[0]
        });

        $http.post('suite_list/',{
            "pro_id":$cookieStore.get("currProID")
        }).success(function(response){
            $scope.$parent.suiteList = response.data;
            $scope.runCase.currSuite =  $scope.suiteList[0]
        });
        $('#runModal').modal('show')
    })
})
autoTest.controller("SuiteModalCtrl",function($scope,$http,$location,$rootScope,$cookieStore) {
    $scope.suite={
        currName:"",
        currDesc:"",
    }
    $scope.$on('openSuiteModal',function(){
        $('#suiteModal').modal('show')
    })

    $scope.saveSuite = function(){
        $http.post('suite_save/',{
            pro_id: $cookieStore.get("currProID"),
            suite_name:$scope.suite.currName,
            suite_desc:$scope.suite.currDesc,
        }).success(function (response) {
            $scope.$parent.suiteList=response.data;
        });
        $("#suiteModal").modal("hide");
        $scope.suite={
            currName:"",
            currDesc:"",
        }
    }
})
autoTest.controller("CaseModalCtrl",function($scope,$http,$location,$rootScope,$cookieStore) {
    $scope.case={
        currName:"",
        currApi:{},
        currDesc:"",
        suite:[]
    }

    $scope.$on('openCaseModal',function(){
        for(var i=0;i<$scope.suiteList.length;i++){
            $scope.case.suite[i]={
                name:$scope.suiteList[i].suite_name,
                desc:$scope.suiteList[i].suite_desc,
                suite_id:$scope.suiteList[i].id,
                checked:false
            }
        }
        console.log($scope.case.suite)

        $scope.case.currApi = $scope.apiList[0]
        $('#caseModal').modal('show')
    })

    $scope.checkearSuite = function (check,id) {
        $scope.case.suite[id].checked = check;
    }

    $scope.saveCase = function(){

        $http.post('case_saveInfo/',{
            case_name:$scope.case.currName,
            pro_id: $cookieStore.get("currProID"),
            suite_list:$scope.case.suite,
            api_id:$scope.case.currApi.id,
            case_desc:$scope.case.currDesc
        });
        $('#caseModal').modal('hide')
        $scope.case={
            currName:"",
            currApi:{},
            currDesc:"",
            suite:[]
        }
    }

})