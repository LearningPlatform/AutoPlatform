myApp.controller('recordCtrl', function ($scope, $http, $cookieStore,$sce,$timeout) {
    var pro_id = $cookieStore.get("currProID");
    $scope.rcdCase={
        "case_id":"",
        "pro_id":pro_id,
        "api_id":"",
        "module_id":"",
        "case_url": "",
        "case_method" :"",
        "case_protocol":"",
        "case_header":"",
        "input_data":"",
        "exp_data": "",
        "check_type":"",
        "case_name":"",
        "case_desc":"",
        "depnd_api_id":"",
        "resp_type":"",
        "suite_list":""
    }
    $scope.record_info = {
        host: "10.170.55.129",
        port: 8003,
        filter: "url"
    }
    $scope.servers_url = "";
    $scope.reqData = [{}];
    $scope.showiframe = false;
    var dataSocket;
    var baseUrl;
    var socketPort;

    $scope.dfRecord = function () {
        $("#recordModal").modal();
        //$scope.record_info="";
    }

    var reqURL = "";
    var reqString = "";
    var reqLength;
    var data;
    var reqData_str;
    var anyproxy_id_list = [];
    var temp;

    $timeout(function(){
        $scope.undisabled=false;
        $scope.undisabledId=-1;
        $scope.typeType=["json","raw","text"];
        $http.post('project/api/list',{
            "pro_id":pro_id
        }).success(function (response) {
            if(response.code==1){
                $scope.apiList=response.data;
            }else{
                alert(response.msg)
            }
        })
        $http.post('project/suite/list', {
             "pro_id": pro_id
        }).success(function (response) {
            if(response.code==1) {
                $scope.suiteList = response.data;
            }else{
                alert(response.msg);
            }
        });
        $http.post("project/dapi/list",{
            "pro_id":pro_id
        }).success(function(response){
            if(response.code==1){
                $scope.apiDepList=response.data;
            }else{
                alert(response.msg)
            }
        })
        $http.post('project/module/list', {
             "pro_id": pro_id
        }).success(function (response) {
            if(response.code==1) {
                $scope.moduleList = response.data;
            }else{
                alert(response.msg);
            }
        });
        $http.post("project/check/list",{
            "pro_id":pro_id
        }).success(function(response){
            if(response.code==1){
                $scope.checkList=response.data;
            }else{
                alert(response.msg)
            }
        })
    })

    $scope.initSocket = function () {
        dataSocket = new WebSocket("ws://" + baseUrl + ":" + socketPort);
        dataSocket.onmessage = function (event) {
            data = JSON.parse(event.data);
            reqData_str = JSON.stringify(data);

            if (reqData_str.indexOf($scope.record_info.filter) != -1) {
                data.content.reqHeader = JSON.stringify(data.content.reqHeader);
                temp = data.content;
                if (anyproxy_id_list.indexOf(data.content.id) != -1) {
                    $scope.reqData[anyproxy_id_list.indexOf(data.content.id)] = temp;
                } else {
                    anyproxy_id_list.push(data.content.id)
                    $scope.reqData.push(temp);
                }
            }
        }
    }

    $scope.startRecord = function () {
        baseUrl = $scope.record_info.host;
        socketPort = $scope.record_info.port;
        $scope.initSocket();
        $("#recordModal").modal('hide');
        $scope.servers_url = $sce.trustAsResourceUrl("http://" + $scope.record_info.host + ":" + "8002/");
        $scope.showiframe = true;
        window.frames["Iframe1"];
    }

    $scope.stopRecord = function () {
        dataSocket.close();
    }

    $scope.idList=[];
    $scope.objList=[];
    $scope.setRecord = function () {
        var temp_resp = "";
        $scope.reqData.forEach(function(value,index){
            value.sex='male';
            $http.post("project/record/reqdetail", {
                host: $scope.record_info.host,
                port: 8002,
                req_id: value.id
            }).success(function (response) {
                if (typeof(response.content) != "undefined") {
                    value.resBody=response.content;
                }
            })
        });
        for (var i=0;i<$scope.reqData.length;i++){
            $scope.idList[i]=-1;
            $scope.objList[i]=new Object();
        }
        $scope.showiframe = false;
        $scope.showtable = true;
    }

    $scope.styleList = [];
    $scope.tableStyle = {
        "background-color": "white",
    }
    $scope.styleChange = {
        "background-color": "#eeeeff",
    }
    $scope.tableGray = function (index) {
        $scope.styleList[index] = $scope.styleChange;
    }
    $scope.tableWhite = function (index) {
        $scope.styleList[index] = $scope.tableStyle;
    }

    var suite_list=[];
    $scope.addSuiteList=function(index,id){
        if($scope.check[index]==true){
            suite_list[index]=id;
        }else{
            suite_list[index]="";
        }
    }

    var RecordId;
    $scope.cfRecord=function(index){
        $("#cfRecord").modal();
        RecordId=index;
    }

    $scope.delRecord=function(){
        $scope.idList.splice(RecordId, 1);
        $scope.objList.splice(RecordId, 1);
        $scope.reqData.splice(RecordId, 1);
        $("#cfRecord").modal('');
    }

    var editId;
    $scope.check=[];
    $scope.editRecord=function(id){
        editId=id;
        $("#editRecord").modal();
        if($scope.idList[id]==-1){
            $scope.req_data=$scope.reqData[id];
            $scope.rcdCase.case_url=$scope.req_data.host+$scope.req_data.path;
            $scope.rcdCase.case_method=$scope.req_data.method;
            $scope.rcdCase.case_protocol=$scope.req_data.protocol;
            $scope.rcdCase.case_header=$scope.req_data.reqHeader;
            $scope.rcdCase.input_data=$scope.req_data.reqBody;
            $scope.rcdCase.exp_data=$scope.req_data.resBody;
            $scope.suite_list = [];
            for(var i=0;i<$scope.suiteList.length;i++){
                $scope.check[i]=false;
            }
        }else{
            $scope.rcdCase=$scope.objList[id];
            $scope.selected1=$scope.rcdCase.api_id;
            $scope.selected2=$scope.rcdCase.depnd_api_id;
            $scope.selected3=$scope.rcdCase.module_id;
        }
    }

    var num;
    $scope.saveEditRecord=function(apiId,apiDepId,moduleId){
        $scope.rcdCase.pro_id=pro_id;
        $scope.rcdCase.api_id=apiId;
        $scope.rcdCase.module_id=moduleId;
        $scope.rcdCase.depnd_api_id=apiDepId;
        $scope.rcdCase.suite_list=suite_list;
        if($scope.rcdCase.case_id==""){
            $http.post('project/rcd_case/create',{
                "pro_id":$scope.rcdCase.pro_id,
                "api_id":$scope.rcdCase.api_id,
                "module_id":$scope.rcdCase.module_id,
                "case_url": $scope.rcdCase.case_url,
                "case_method" :$scope.rcdCase.case_method,
                "case_protocol":$scope.rcdCase.case_protocol,
                "case_header":$scope.rcdCase.case_header,
                "input_data":$scope.rcdCase.input_data,
                "exp_data": $scope.rcdCase.exp_data,
                "check_type":$scope.rcdCase.check_type,
                "case_name":$scope.rcdCase.case_name,
                "case_desc":$scope.rcdCase.case_desc,
                "depnd_api_id":$scope.rcdCase.depnd_api_id,
                "resp_type":$scope.rcdCase.resp_type,
                "suite_list":$scope.rcdCase.suite_list
            }).success(function(response){
                if(response.code==1){
                    num=$scope.rcdCase.case_url.indexOf('/');
                    $scope.req_data.host=$scope.rcdCase.case_url.slice(0,num-1);
                    $scope.req_data.path=$scope.rcdCase.case_url.slice(num,-1);
                    $scope.req_data.method=$scope.rcdCase.case_method;
                    $scope.req_data.protocol=$scope.rcdCase.case_protocol;
                    $scope.req_data.reqHeader=$scope.rcdCase.case_header;
                    $scope.req_data.reqBody=$scope.rcdCase.input_data;
                    $scope.req_data.resBody=$scope.rcdCase.exp_data;
                    $scope.rcdCase.case_id=response.data.case_id;
                    $scope.idList[editId]=$scope.rcdCase.case_id;
                    $scope.objList[editId]=$scope.rcdCase;
                    $("#editRecord").modal('hide');
                    $scope.undisabled=true;
                    $scope.undisabledId=editId;
                }else{
                    alert(response.msg);
                }
            })
        }else{
            $http.post('project/rcd_case/edit',{
                "case_id":$scope.rcdCase.case_id,
                "pro_id":$scope.rcdCase.pro_id,
                "api_id":$scope.rcdCase.api_id,
                "module_id":$scope.rcdCase.module_id,
                "case_url": $scope.rcdCase.case_url,
                "case_method" :$scope.rcdCase.case_method,
                "case_protocol":$scope.rcdCase.case_protocol,
                "case_header":$scope.rcdCase.case_header,
                "input_data":$scope.rcdCase.input_data,
                "exp_data": $scope.rcdCase.exp_data,
                "check_type":$scope.rcdCase.check_type,
                "case_name":$scope.rcdCase.case_name,
                "case_desc":$scope.rcdCase.case_desc,
                "depnd_api_id":$scope.rcdCase.depnd_api_id,
                "resp_type":$scope.rcdCase.resp_type,
                "suite_list":$scope.rcdCase.suite_list
            }).success(function(response){
                if(response.code==1){
                    num=$scope.rcdCase.case_url.indexOf('/');
                    $scope.req_data.host=$scope.rcdCase.case_url.slice(0,num-1);
                    $scope.req_data.path=$scope.rcdCase.case_url.slice(num,-1);
                    $scope.req_data.method=$scope.rcdCase.case_method;
                    $scope.req_data.protocol=$scope.rcdCase.case_protocol;
                    $scope.req_data.reqHeader=$scope.rcdCase.case_header;
                    $scope.req_data.reqBody=$scope.rcdCase.input_data;
                    $scope.req_data.resBody=$scope.rcdCase.exp_data;
                    $scope.objList[editId]=$scope.rcdCase;
                    $("#editRecord").modal('hide');
                }else{
                    alert(response.msg)
                }
            })
        }
    }

    $scope.runRecord=function(obj){
        $("#runRecord").modal();
    }

    $scope.getRecordResult=function(caseId,caseType,envId){
        $("#runRecord").modal("hide");
        $http.post("project/case/runsingal",{
            "case_id":caseId,
            "case_type":2,
            "env_id":envId
        }).success(function(response){
            if(response.code==1){
                $scope.rcdResult=response.data;
                $scope.rcdResult.schema=JSON.stringify($scope.rcdResult.schema);
                $scope.rcdResult.response_body=JSON.stringify($scope.rcdResult.response_body);
                if($scope.rcdResult.schema_check==1){
                    $scope.rcdResult.schema_check="通过";
                }else{
                    $scope.rcdResult.schema_check="失败";
                }
                if($scope.rcdResult.result_check==1){
                    $scope.rcdResult.result_check="通过";
                }else{
                    $scope.rcdResult.result_check="失败";
                }
                $("#recordResult").modal();
            }else{
                alert(response.msg)
            }
        })
    }
})
