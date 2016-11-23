myApp.controller('APICaseCtrl',function($scope,$http,$cookieStore,$timeout) {
    var pro_id = $cookieStore.get("currProID");
    var moduleId=0;
    var apiId=0;
    var caseId=0;
    $scope.showBtn=false;
    $scope.showModule=true;
    $scope.showCase=false;
    $scope.showinfo=false;
    $scope.showAPIID=0;
    $scope.showCaseID=0;
    $scope.List=["active"];
    $scope.envList="";
    $scope.suite_list=[];
    $scope.varInfoShow=true;
    $scope.moduleList="";
    $scope.module={
        "module_desc": "",
        "module_id": "",
        "pro_id": pro_id,
        "module_name": ""
    }
    $scope.suiteList="";
    $scope.suite={
        "suite_desc": "",
        "suite_id": 0,
        "pro_id": pro_id,
        "suite_name": ""
    };
    $scope.methodType=["get","post","put","detele"];
    $scope.protocolType=["http","tcp","udp"];
    $scope.typeType=["json","raw","text"];
    $scope.apiList="";
    $scope.api={
        "pro_id": pro_id,
        "api_id": 0,
        "module_id": $scope.module.module_id,
        "api_desc": "",
        "api_param": "",
        "api_url": "",
        "api_method": "",
        "api_type": "",
        "api_protocol": "",
        "api_name": ""
    };

    $scope.caseList="";
    $scope.case={
        "case_name": "",
        "input_data": "",
        "exp_data": "",
        "pro_id": pro_id,
        "module_id": 0,
        "case_desc": "",
        "check_type": 0,
        "case_id": 1,
        "api_id": 1,
        "is_set": 1,
        "depnt_api":{depnt_api_name:"",depnt_api_id:0}
    }

    $scope.report={
        "report_name": "",
        "start_time": "",
        "suite_id": 1,
        "fail_num": 1,
        "pro_id": pro_id,
        "pass_num": 1,
        "result_id": 50,
        "end_time": 1478621079
    }

    $timeout(function(){
        $http.post('project/env/list',{
            "pro_id":pro_id
        }).success(function(response){
            if(response.code==1){
                $scope.envList=response.data;
            }else{
                alert(response.msg)
            }
        })
        $scope.showAllAPI=true;
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
        $http.post('project/api/list',{
            "pro_id":pro_id
        }).success(function (response) {
            if(response.code==1){
                $scope.apiList=response.data;
            }else{
                alert(response.msg)
            }
        })
        $scope.showBtn=false;
        $scope.showBtn1=true;
        $http.post('project/suite/list', {
             "pro_id": pro_id
        }).success(function (response) {
            if(response.code==1) {
                $scope.suiteList = response.data;
            }else{
                alert(response.msg);
            }
        });
    })

    $scope.showAll=function(){
        $scope.showCase=false;
        for(var i=0;i<$scope.moduleList.length;i++){
            $scope.List[i+1]="disactive"
        }
        $scope.List[0]="active";
        $http.post('project/api/list',{
            "pro_id":pro_id
        }).success(function (response) {
            if(response.code==1){
                $scope.apiList=response.data;
            }else{
                alert(response.msg)
            }
        })
         $scope.showBtn=false;
         $scope.showBtn1=true;
         $scope.showAllAPI=true;
         $scope.showAPIInModule=false;
         $scope.showinfo=false;
    }

    $scope.active1 = function(id) {
         $scope.showCase=false;
         for(var i=0;i<$scope.moduleList.length;i++){
            $scope.List[i+1]="disactive"
         }
         $scope.List[id+1]='active';
         $scope.List[0]="disactive";
         $scope.module=$scope.moduleList[id];
         $scope.showId=$scope.module.module_id;
         $scope.showBtn=true;
         $scope.showBtn1=false;
         $scope.showAllAPI=false;
         $scope.showAPIInModule=true;
         $scope.showinfo=false;
         $http.post('project/module/apiList',{
             "module_id":$scope.module.module_id
         }).success(function(response){
             if(response.code==1){
                 $scope.apiList=response.data;
             }else{
                 alert(response.msg);
             }
         })
    }

    $scope.run=function(){
        $("#runModule").modal();
        $scope.report_name="";
    }

    $scope.report_name="";

    $scope.saveRun=function(envId,suiteId){
        $http.post('project/case/run',{
            "suite_id":suiteId,
            "pro_id":pro_id,
            "env_id":envId,
            "report_name": $scope.report_name
        }).success(function(response){
            if(response.code==1){
                $scope.report=response.data;
            }else{
                alert(response.msg)
            }
        })
       $("#runModule").modal('hide');
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

     $scope.editModule=function(){
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

    $scope.addSuite=function(){
         $scope.suite="";
        $("#AddSuite").modal();
    }

    $scope.saveSuite=function(){
        if($scope.suite.suite_name==null){
            $scope.suite.suite_name="";
        }
        if($scope.suite.suite_desc==null){
            $scope.suite.suite_desc="无";
        }
        $http.post('project/suite/create',{
            "pro_id":pro_id,
            "suite_name":$scope.suite.suite_name,
            "suite_desc":$scope.suite.suite_desc
        }).success(function (response) {
            if(response.code==1){
                $("#AddSuite").modal('hide');
                $http.post('project/suite/list', {
                     "pro_id": pro_id
                }).success(function (response1) {
                     if(response1.code==1) {
                         $scope.suiteList = response1.data;
                     }else{
                        alert(response1.msg);
                    }
                });
            } else{
                alert(response.msg);
            }
        });
    }

    $scope.addApi=function(){
        $http.post('project/module/list', {
             "pro_id": pro_id
        }).success(function (response) {
            if(response.code==1) {
                $scope.moduleList = response.data;
            }else{
                alert(response.msg);
            }
        });
        $scope.api="";
        $("#addapi").modal();
    }

    $scope.saveAPI=function(id){
        if($scope.api.api_name==null){
            $scope.api.api_name="";
        }
        if($scope.api.api_desc==null){
            $scope.api.api_desc="无";
        }
        $http.post('project/api/create',{
            "api_param": $scope.api.api_param,
            "module_id": id,
            "pro_id": pro_id,
            "api_url": $scope.api.api_url,
            "api_method": $scope.api.api_method,
            "api_type": $scope.api.api_type,
            "api_protocol": $scope.api.api_protocol,
            "api_name": $scope.api.api_name,
            "api_desc": $scope.api.api_desc
        }).success(function (response) {
            if(response.code==1){
                $("#addapi").modal('hide');
                if($scope.showAllAPI){
                    $http.post('project/api/list', {
                         "pro_id": pro_id
                    }).success(function (response1) {
                         if(response1.code==1) {
                             $scope.apiList = response1.data;
                         }else{
                            alert(response1.msg);
                        }
                    });
                }else if($scope.showAPIInModule){
                     $http.post('project/module/apiList',{
                     "module_id":$scope.showId
                     }).success(function(response2){
                         if(response2.code==1){
                             $scope.apiList=response2.data;
                         }else{
                             alert(response2.msg);
                         }
                     })
                }
            } else{
                alert(response.msg);
            }
        });
    }

    $scope.editapi=function(id){
        $http.post('project/api/detail',{
            "api_id":id
        }).success(function(response){
            if(response.code==1){
                $scope.api=response.data;
                $http.post('project/module/detail',{
                    "module_id":$scope.api.module_id
                }).success(function(response1){
                    if(response1.code==1){
                        $scope.module=response1.data;
                    }else{
                        alert(response1.msg);
                    }
                })
            }else{
                alert(response.msg);
            }
        })
        $("#editapi").modal();
    }

    $scope.saveEditAPI=function(id){
        if($scope.api.api_name==null){
            $scope.api.api_name="";
        }
        if($scope.api.api_desc==null){
            $scope.api.api_desc="无";
        }
        $http.post('project/api/edit',{
            "api_param": $scope.api.api_param,
            "module_id": id,
            "pro_id": pro_id,
            "api_id": $scope.api.api_id,
            "api_url": $scope.api.api_url,
            "api_method": $scope.api.api_method,
            "api_type": $scope.api.api_type,
            "api_protocol": $scope.api.api_protocol,
            "api_name": $scope.api.api_name,
            "api_desc": $scope.api.api_desc
        }).success(function (response) {
            if(response.code==1){
                $("#editapi").modal('hide');
                if($scope.showAllAPI){
                     $http.post('project/api/list', {
                         "pro_id": pro_id
                    }).success(function (response1) {
                         if(response1.code==1) {
                             $scope.apiList = response1.data;
                         }else{
                            alert(response1.msg);
                        }
                    });
                }else if($scope.showAPIInModule){
                     $http.post('project/module/apiList',{
                     "module_id":$scope.showId
                 }).success(function(response2){
                     if(response2.code==1){
                         $scope.apiList=response2.data;
                     }else{
                         alert(response2.msg);
                     }
                 })
                }
            }else {
                alert(response.msg);
            }
        });
    }

    $scope.cfDelapi=function(id){
        $("#cfAPI").modal();
        apiId=id;
    }

    $scope.delAPI=function(){
        $("#cfAPI").modal('hide');
        $http.post('project/api/delete',{
            "api_id":apiId,
        }).success(function (response1) {
            if(response1.code==1){
                if($scope.showAllAPI){
                    $http.post('project/api/list', {
                         "pro_id": pro_id
                    }).success(function (response1) {
                         if(response1.code==1) {
                             $scope.apiList = response1.data;
                         }else{
                            alert(response1.msg);
                        }
                    });
                }else if($scope.showAPIInModule){
                     $http.post('project/module/apiList',{
                     "module_id":$scope.showId
                     }).success(function(response2){
                         if(response2.code==1){
                             $scope.apiList=response2.data;
                         }else{
                             alert(response2.msg);
                         }
                     })
                }
            }else{
                alert(response1.msg);
            }
        });
    }

    $scope.getAPICase=function(id){
        $scope.showCase=!$scope.showCase;
        $scope.showAPIID=id;
        $http.post('project/api/caseList',{
            "api_id":id
        }).success(function(response){
            if(response.code==1){
                $scope.caseList=response.data;
            }else{
                alert(response.msg);
            }
        })
    }
    $scope.check=[];

    $scope.addCase=function(){
        $scope.case="";
        $scope.api="";
        $scope.suite_list = []
        for(var i=0;i<$scope.suiteList.length;i++){
            $scope.check[i]=false;
        }
        $http.post("project/dapi/list",{
            "pro_id":pro_id
        }).success(function(response){
            if(response.code==1){
                $scope.apiDepList=response.data;
            }else{
                alert(response.msg)
            }
        })
        $("#AddCase").modal();
    }

    $scope.addSuiteList=function(checked,id){
        if(checked==true){
            $scope.suite_list.push(id);
        }
    }

    $scope.saveCase=function(id){
        if($scope.case.case_name==null){
            $scope.case.case_name="";
        }
        if($scope.case.case_desc==null){
            $scope.case.case_desc="无";
        }
        if($scope.case.check_type==null){
            $scope.case.check_type=0;
        }
        if($scope.case.depnt_api==null){
            $scope.case.depnt_api={depnt_api_name:"",depnt_api_id:0};
        }
        console.log($scope.case.depnt_api)
        $http.post('project/case/create',{
            api_id: id,
            pro_id: pro_id,
            case_desc: $scope.case.case_desc,
            case_name: $scope.case.case_name,
            suite_list:$scope.suite_list,
            check_type:0,
            depnd_api_id:$scope.case.depnt_api.depnd_api_id
        }).success(function(response){
            if(response.code==1) {
                $http.post('project/api/caseList',{
                    "api_id":id
                }).success(function(response1){
                    $scope.caseList=response1.data;
                })
            }else{
                alert(response.msg);
            }
        })
        $("#AddCase").modal('hide');
    }

    $scope.str="";
    $scope.exp="";
    $scope.showSelectId=0;
    $scope.al=["active","disactive","disactive"];

    $scope.active2=function(index,obj){
        for(i=0;i<3;i++){
            $scope.al[i]="disactive";
        }
        $scope.al[index]="active";
        $scope.showSelectId=index;
        $scope.showParamId=0;
        if($scope.str==""){
            if(obj.is_set==1){
                $scope.str=obj.input_data.replace(/\'/ig,"\"");
            }else{
                $scope.param = $scope.api.api_param.split(',');
                $scope.str='{';
                for(var i=0;i<$scope.param.length-1;i++){
                    $scope.str = $scope.str +'"'+ $scope.param[i]+'" :"undefined", ';
                }
                $scope.str = $scope.str  +'"'+ $scope.param[$scope.param.length-1] + '" :"undefined"}';
            }
        }
        $scope.exp = obj.exp_data;
    }

    var editApiId=0;
    $scope.infoCase=function(obj){
        $scope.showinfo=!$scope.showinfo;
        $scope.showCaseID=obj.case_id;
        $scope.str="";
        editApiId=obj.api_id;
        $scope.al=["active","disactive","disactive"];
        $scope.showSelectId=0;
         $http.post('project/api/detail',{
            "api_id":editApiId
        }).success(function(response) {
            if (response.code == 1) {
                $scope.api = response.data;
            }else{
                alert(response.msg);
            }
        })
    }
    var value;
    var totalValue;
    var paramValue;
    $scope.param=[];

    $scope.canshu=[];
    var stringId;
    var textId;
    $scope.showParam1=function(){
        stringId=1;
        $scope.showParamId=1;
        if(textId==1){
            $scope.str=angular.toJson($scope.case.input_data)
            $scope.str=$scope.str.replace(/\'/ig,"\"");
        }
        value=$scope.str.replace('{','');
        value=value.replace('}','');
        totalValue=value.split(',');
        $scope.param=[];
        $scope.canshu=[];
        for(var i=0;i<totalValue.length;i++){
            totalValue[i] = totalValue[i].replace(' ','');
            paramValue=totalValue[i].split(':');
            $scope.param[i] = paramValue[0].replace(/\"/ig,"");
            $scope.canshu[i] = paramValue[paramValue.length-1].replace(' ','');
        }
    }

    $scope.showParam2=function(){
        $scope.showParamId=2;
        textId=1;
        if(stringId==1){
            $scope.str="";
            $scope.str='{'
            console.log($scope.param)
            for(var i=0;i<$scope.param.length-1;i++){
                $scope.str = $scope.str +'"'+ $scope.param[i]+'" :'+ $scope.canshu[i]+', ';
            }
            $scope.str = $scope.str +'"'+$scope.param[$scope.param.length-1] + '" :'+ $scope.canshu[$scope.param.length-1]+'}';
        }
        $scope.textValue=$scope.str;
        console.log($scope.str)
    }

    $scope.addParam1=function(){
        $scope.param.push(" ");
    }

    $scope.saveParam1=function(id){
         $scope.str='{'
         for(var i=0;i<$scope.param.length-1;i++){
             $scope.str = $scope.str +'"'+ $scope.param[i]+'" :'+ $scope.canshu[i]+', ';
         }
         $scope.str = $scope.str +'"'+$scope.param[$scope.param.length-1] + '" :'+ $scope.canshu[$scope.param.length-1]+'}';
         $scope.case.input_data=angular.fromJson($scope.str);
         $http.post('project/case/edit/req',{
             "case_id":id,
             "input_data":$scope.case.input_data,
             "depnd_api_id":0
         }).success(function(response){
             if(response.code==0){
                 alert(response.msg);
            }
        })
    }

    $scope.saveParam2=function(id,abc){
        $scope.case.input_data=angular.fromJson(abc);
        $http.post('project/case/edit/req',{
            "case_id":id,
            "input_data":$scope.case.input_data,
            "depnd_api_id":0
        }).success(function(response){
            if(response.code==0){
                alert(response.msg);
            }
        })
    }

    var delParam=0;
    var delCaseId=0;
    var index=0;

    $scope.cfDelParam=function(caseId,value){
        $("#cfParam").modal();
        delCaseId=caseId;
        delParam=value;
    }

    $scope.delParam=function(){
        index=$scope.param.indexOf(delParam);
        $scope.param.splice(index,1);
        $scope.canshu.splice(index,1)
        $scope.saveParam1(delCaseId);
        $("#cfParam").modal('hide');
    }

    $scope.saveExp=function(id,data){
        $http.post('project/case/edit/resp',{
            "case_id": id,
             "exp_data": data,
             "check_type": 0
        }).success(function(response){
            if(response.code==0){
                alert(response.msg)
            }
        })
    }

    $scope.cfDelCase=function(caseid,APIid){
        $("#cfCase").modal();
        caseId=caseid;
        apiId=APIid;
    }

    $scope.delCase=function(){
        $http.post('project/case/delete',{
            "case_id":caseId
        }).success(function(response){
            if(response.code==1){
                $("#cfCase").modal("hide");
                $http.post('project/api/caseList',{
                    "api_id":apiId
                }).success(function(response1){
                    if(response1.code==1){
                        $scope.caseList=response1.data;
                    }else{
                        alert(response1.msg);
                    }
                })
            }else{
                alert(response.msg);
            }
        })
    }

    $scope.addDepntApi = function () {
        $http.post("project/dapi/list",{
            "pro_id":pro_id
        }).success(function(response){
            if(response.code==1){
                $scope.apiDepList=response.data;
            }else{
                alert(response.msg)
            }
        })
        $("#cfDepnt").modal();
    }
    $scope.addDepnt = function () {


        $("#cfDepnt").modal('hide');
    }
})
