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
    $scope.methodType=["GET","POST","PUT","DELETE"];
    $scope.protocolType=["http"];
    //$scope.typeType=["json","raw","text"];
    $scope.typeType=["json"];
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
        api:{api_name:"",api_id:0},
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
    $scope.check1={
        "check_name": "",
        "check_id": 0,
        "pro_id": pro_id,
        "check_desc": "",
        "check_code": ""
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
        $http.post("project/dapi/list",{
            "pro_id":pro_id
        }).success(function(response){
            if(response.code==1){
                $scope.apiDepList=response.data;
                $scope.apiDep=new Object();
                $scope.apiDep.depnd_api_name="无";
                $scope.apiDep.depnd_api_id=0;
                $scope.apiDepList.unshift($scope.apiDep);
            }else{
                alert(response.msg)
            }
        })
        $http.post("project/check/list",{
            "pro_id":pro_id
        }).success(function(response){
            if(response.code==1){
                $scope.checkList=response.data;
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
        $scope.env="无";
        $scope.suite="";
    }

    $scope.report_name="";

    $scope.saveRun=function(envId,suiteId){
        if(envId==undefined){
            envId=0;
        }
        if(suiteId==undefined){
            suiteId=0;
        }
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
        if(id==""){
            id=0;
        }
        if($scope.api.api_protocol==undefined){
            $scope.api.api_protocol="http";
        }
        if($scope.api.api_method==undefined){
            $scope.api.api_method="POST";
        }
        if($scope.api.api_type==undefined){
            $scope.api.api_type="json";
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

    $scope.selected=0;
    $scope.editapi=function(id){
        $http.post('project/api/detail',{
            "api_id":id
        }).success(function(response){
            if(response.code==1){
                $scope.api=response.data;
                $scope.api.api_method=$scope.api.api_method.toLocaleUpperCase();
                $scope.selected=$scope.api.module_id;
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
        $("#AddCase").modal();
    }

     var suite_list=[];
    $scope.addSuiteList=function(index,id){
        if($scope.check[index]==true){
            suite_list[index]=id;
        }else{
            suite_list[index]="";
        }
    }

    $scope.saveCase=function(apiId,apiDepId,checkId){
        if(apiId==undefined){
            apiId=0;
        }
        if(apiDepId==undefined){
            apiDepId=0;
        }
        if(checkId==undefined){
            checkId=0;
        }
        $scope.case.check_type=checkId;
        $scope.case.depnd_api_id=apiDepId;
        $scope.case.api_id=apiId;
        for(var i=0;i<$scope.check.length;i++){
             if($scope.check[i]==true){
                $scope.suite_list.push(suite_list[i]);
            }
        }
        if($scope.case.case_name==null){
            $scope.case.case_name="";
        }
        if($scope.case.case_desc==null){
            $scope.case.case_desc="无";
        }
        $http.post('project/case/create',{
            "api_id": $scope.case.api_id,
            "pro_id": pro_id,
            "case_desc": $scope.case.case_desc,
            "case_name": $scope.case.case_name,
            "suite_list":$scope.suite_list,
            "check_type":$scope.case.check_type,
            "depnd_api_id":$scope.case.depnd_api_id
        }).success(function(response){
            if(response.code==1) {
                $http.post('project/api/caseList',{
                    "api_id":$scope.case.api_id
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

    $scope.schema="";
    $scope.active2=function(index,obj){
        for(i=0;i<3;i++){
            $scope.al[i]="disactive";
        }
        $scope.al[index]="active";
        $scope.showSelectId=index;
        $scope.showParamId=0;
        /*
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
        }*/
        $scope.str=obj.input_data;
        $scope.exp = obj.exp_data;
        $scope.schema=obj.case_schema;
        $scope.showParamId=2;
        //$scope.showParam2();
    }

    var editApiId=0;
    $scope.infoCase=function(obj){
        $scope.showinfo=!$scope.showinfo;
        $scope.showCaseID=obj.case_id;
        $scope.showCaseType=obj.case_type;
        $scope.str="";
        $scope.al=["active","disactive","disactive"];
        $scope.showSelectId=0;
        if(obj.case_type==1) {
            $http.post("project/case/detail", {
                "case_id": obj.case_id
            }).success(function (response) {
                if (response.code == 1) {
                    $scope.case = response.data;
                    $http.post('project/api/detail', {
                        "api_id": $scope.case.api_id
                    }).success(function (response) {
                        if (response.code == 1) {
                            $scope.api = response.data;
                        } else {
                            alert(response.msg);
                        }
                    })
                    if(obj.check_type==0){
                        $scope.check1.check_name="默认";
                    }else{
                        $http.post("project/check/detail", {
                            "check_id": obj.check_type
                        }).success(function (response) {
                            if (response.code == 1) {
                                $scope.check1 = response.data;
                            } else {
                                alert(response.msg);
                            }
                        })
                    }
                    $http.post("project/dapi/detail", {
                        "depnd_api_id": $scope.case.depnd_api_id
                    }).success(function (response) {
                        if (response.code == 1) {
                            $scope.depnd = response.data;
                        } else {
                            alert(response.msg);
                        }
                    })
                }
            })
        }else{
            $http.post("project/rcd_case/detail", {
                "case_id": obj.case_id
            }).success(function (response) {
                if (response.code == 1) {
                    $scope.case = response.data;
                    $http.post('project/api/detail', {
                        "api_id": $scope.case.api_id
                    }).success(function (response) {
                        if (response.code == 1) {
                            $scope.api = response.data;
                        } else {
                            alert(response.msg);
                        }
                    })
                    $http.post("project/check/detail", {
                        "check_id": obj.check_type
                    }).success(function (response) {
                        if (response.code == 1) {
                            $scope.check1 = response.data;
                        } else {
                            alert(response.msg);
                        }
                    })
                }
            })
        }
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
            for(var i=0;i<$scope.param.length-1;i++){
                $scope.str = $scope.str +'"'+ $scope.param[i]+'" :'+ $scope.canshu[i]+', ';
            }
            $scope.str = $scope.str +'"'+$scope.param[$scope.param.length-1] + '" :'+ $scope.canshu[$scope.param.length-1]+'}';
        }
        $scope.textValue=$scope.str;
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

    $scope.saveParam2=function(obj){
        //$scope.case.input_data=eval("("+$scope.case.input_data+")");
        if(obj.case_type==1){
            $http.post('project/case/edit',{
                "case_id":obj.case_id,
                "pro_id":obj.pro_id,
                "api_id":obj.api_id,
                "case_desc":obj.case_desc,
                "case_name":obj.case_name,
                "depnd_api_id":obj.depnd_api_id,
                "input_data":obj.input_data,
                "exp_data":obj.exp_data,
                "case_schema":obj.case_schema,
                "check_type":obj.check_type,
                "suite_list":obj.suite_list
            }).success(function(response){
                if(response.code==0){
                    alert(response.msg);
                }
            })
        }else{
            $http.post('project/rcd_case/edit',{
                "case_id":obj.case_id,
                "pro_id":obj.pro_id,
                "api_id":obj.api_id,
                "module_id":obj.module_id,
                "case_url": obj.case_url,
                "case_method" :obj.case_method,
                "case_protocol":obj.case_protocol,
                "case_header":obj.case_header,
                "input_data":obj.input_data,
                "exp_data": obj.exp_data,
                "check_type":obj.check_type,
                "case_name":obj.case_name,
                "case_desc":obj.case_desc,
                "depnd_api_id":obj.depnd_api_id,
                "resp_type":obj.resp_type,
                "suite_list":obj.suite_list,
                "case_schema":obj.case_schema
            }).success(function(response){
                if(response.code==0){
                    alert(response.msg);
                }
            })
        }
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

    $scope.saveExp=function(obj,data,schema){
        if(obj.case_header==""){
            obj.case_header=" ";
        }
        if(obj.case_type==1){
            $http.post('project/case/edit/resp',{
                "case_id": obj.case_id,
                 "exp_data": data,
                 "check_type": obj.case_type,
                "case_schema":schema
            }).success(function(response){
                if(response.code==0){
                    alert(response.msg)
                }
            })
        }else{
            $http.post('project/rcd_case/edit',{
                "case_id":obj.case_id,
                "pro_id":pro_id,
                "api_id":obj.api_id,
                "module_id":obj.module_id,
                "case_url": obj.case_url,
                "case_method" :obj.case_method,
                "case_protocol":obj.case_protocol,
                "case_header":obj.case_header,
                "input_data":obj.input_data,
                "exp_data": data,
                "check_type":obj.check_type,
                "case_name":obj.case_name,
                "case_desc":obj.case_desc,
                "depnd_api_id":obj.depnd_api_id,
                "resp_type":obj.resp_type,
                "suite_list":obj.suite_list,
                "case_schema":schema
            }).success(function(response){
                if(response.code==0){
                    alert(response.msg)
                }
            })
        }


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

    var suiteIndex=0;
    $scope.editCase = function (obj) {
        $scope.case=obj;
        $scope.suite_list=[];
        $("#EditCase").modal();
        $scope.selected1=$scope.case.api_id;
        $scope.selected2=$scope.case.depnd_api_id;
        $scope.selected3=$scope.case.check_type;
        if($scope.selected3==0){
            $scope.selected3="无"
        }
        for(var i=0;i<$scope.suiteList.length;i++){
            $scope.check[i]=false;
            suite_list[i]=-1;
        }
        for(var i=0;i<$scope.case.suite_list.length;i++){
            for(var j=0;j<$scope.suiteList.length;j++){
                if($scope.suiteList[j].suite_id==$scope.case.suite_list[i]){
                    $scope.check[j]=true;
                    suite_list[j]=$scope.suiteList[j].suite_id;
                }
            }
        }
    }

    $scope.saveEditCase=function(obj,apiId,depntId,checkId){
        for(var i=0;i<$scope.check.length;i++){
             if($scope.check[i]==true){
                $scope.suite_list.push(suite_list[i]);
            }
        }
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
        if(obj.case_type==1){
            $http.post('project/case/edit',{
                "case_id":obj.case_id,
                "pro_id":obj.pro_id,
                "api_id":apiId,
                "case_desc":obj.case_desc,
                "case_name":obj.case_name,
                "depnd_api_id":depntId,
                "input_data":obj.input_data,
                "exp_data":obj.exp_data,
                "case_schema":obj.case_schema,
                "check_type":checkId,
                "suite_list":obj.suite_list
            }).success(function(response){
                if(response.code==1) {
                    $http.post('project/api/caseList',{
                        "api_id":apiId
                    }).success(function(response1){
                        $scope.caseList=response1.data;
                    })
                }else{
                    alert(response.msg);
                }
            })
        }else{
            $http.post('project/rcd_case/edit',{
                "case_id":obj.case_id,
                "pro_id":obj.pro_id,
                "api_id":apiId,
                "module_id":obj.module_id,
                "case_url": obj.case_url,
                "case_method" :obj.case_method,
                "case_protocol":obj.case_protocol,
                "case_header":obj.case_header,
                "input_data":obj.input_data,
                "exp_data": obj.exp_data,
                "check_type":checkId,
                "case_name":obj.case_name,
                "case_desc":obj.case_desc,
                "depnd_api_id":depntId,
                "resp_type":obj.resp_type,
                "suite_list":obj.suite_list,
                "case_schema":obj.case_schema
            }).success(function(response){
                if(response.code==1) {
                    $http.post('project/api/caseList',{
                        "api_id":apiId
                    }).success(function(response1){
                        $scope.caseList=response1.data;
                    })
                }else{
                    alert(response.msg);
                }
            })



        }
        $("#EditCase").modal('hide');
    }

    $scope.addDepntApi = function () {
        $http.post("project/dapi/list",{
            "pro_id":pro_id
        }).success(function(response){
            if(response.code==1){
                $scope.apiDepList=response.data;
                $scope.apiDepList.unshift("无");
            }else{
                alert(response.msg)
            }
        })
        $("#cfDepnt").modal();
    }

    $scope.addDepnt = function () {
        $("#cfDepnt").modal('hide');
    }

    $scope.runCase=function(obj){
        $scope.env="";
        $("#runCase").modal();
    }

    $scope.caseResult="";
    $scope.getCaseResult=function(caseId,caseType,envId){
        $("#runCase").modal("hide");
        $http.post("project/case/runsingal",{
            "case_id":caseId,
            "case_type":1,
            "env_id":envId
        }).success(function(response){
            if(response.code==1){
                $scope.caseResult=response.data;
                $scope.caseResult.schema=JSON.stringify($scope.caseResult.schema);
                $scope.caseResult.response_body=JSON.stringify($scope.caseResult.response_body);
                if($scope.caseResult.schema_check==1){
                    $scope.caseResult.schema_check="通过";
                }else{
                    $scope.caseResult.schema_check="失败";
                }
                if($scope.caseResult.result_check==1){
                    $scope.caseResult.result_check="通过";
                }else{
                    $scope.caseResult.result_check="失败";
                }
                $("#caseResult").modal();
            }else{
                alert(response.msg)
            }
        })
    }
})
