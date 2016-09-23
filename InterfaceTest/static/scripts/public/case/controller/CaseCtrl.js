//项目用例控制器
autoTest.controller("CaseCtrl",function($scope,$http,$location,$rootScope,$cookieStore,CaseModel) {
    var pro_id = $cookieStore.get("currProID")
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
    $scope.pro_model={
        currname:"",
        currdesc:"",
    }
    $scope.runCase={
        currReport:"",
        currEnv:{},
        currModel:{},
        currSuite:{},
        currDesc:"",
    }
    $scope.case={
        currName:"",
        currApi:{},
        currDesc:"",
        suite:[]
    }

    //初始化模块列表
    CaseModel.getModelList($scope,pro_id)

    //初始化接口列表
    CaseModel.getApiList($scope,pro_id)

    CaseModel.getSuiteList($scope,pro_id)

    //向下传播打开增加API的模态框
    $scope.openApiModal = function () {
        $scope.api.currmodel=$scope.modelList[0]
        $('#apiAddModal').modal('show')
    }

    $scope.saveApi = function(){
        CaseModel.saveApi($scope,pro_id)
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
    //向下传播打开增加模块的模态框
    $scope.openModelModal = function () {
        $('#modelAddModal').modal('show')
    }

    $scope.saveModel = function(){
        CaseModel.saveModel($scope,pro_id)
        $("#modelAddModal").modal("hide");
        $scope.pro_model={
            currname:"",
            currdesc:"",
        }
    }
    //向下传播打开增加模块的模态框
    $scope.openRunModal = function () {
        $scope.runCase.currModel = $scope.modelList[0]
        CaseModel.getEnvList($scope,pro_id)
        CaseModel.getSuiteList($scope,pro_id)
        $scope.runCase.currEnv = $scope.envList[0]
        $scope.runCase.currSuite =  $scope.suiteList[0]

        $('#runModal').modal('show')
    }
    //向下传播打开增加模块的模态框
    $scope.openSuiteModal = function () {
        $('#suiteModal').modal('show')
    }

    $scope.saveSuite = function(){
        CaseModel.saveSuite($scope,pro_id)
        $("#suiteModal").modal("hide");
        $scope.suite={
            currName:"",
            currDesc:"",
        }
    }
    //向下传播打开增加模块的模态框
    $scope.openCaseModal = function () {
        for(var i=0;i<$scope.suiteList.length;i++){
            $scope.case.suite[i]={
                name:$scope.suiteList[i].suite_name,
                desc:$scope.suiteList[i].suite_desc,
                suite_id:$scope.suiteList[i].id,
                checked:false
            }
        }
        $scope.case.currApi = $scope.apiList[0]
        $('#caseModal').modal('show')
    }

    $scope.checkearSuite = function (check,id) {
        $scope.case.suite[id].checked = check;
    }

    $scope.saveCase = function(){

        CaseModel.saveCaseInfo($scope,pro_id)
        $('#caseModal').modal('hide')
        $scope.case={
            currName:"",
            currApi:{},
            currDesc:"",
            suite:[]
        }
    }

    $scope.getApiCase = function (id) {
        CaseModel.getCaseOfApi($scope,id)
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

        CaseModel.saveReqParam($scope,index,id,api_id)
        $scope.editShow=false
        $scope.displayShow=true
    }

    $scope.runCaseStart = function () {
        $http.post('run/',{
            api_id:5
        })
    }
})