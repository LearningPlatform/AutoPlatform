myApp.controller('APICaseCtrl',function($scope,$http,$cookieStore,$timeout) {
    var pro_id = $cookieStore.get("currProID");
    var moduleId=0;
    var apiId=0;
    $scope.showBtn=false;
    $scope.showModule=true;
    $scope.showCase=false;
    $scope.showAPIID=0;
    $scope.List=["active"];
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
        "is_set": 1
    }
    $timeout(function(){
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
    })

    $scope.showAll=function(){
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
    }

    $scope.active1 = function(id) {
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
         $http.post('project/module/apiList',{
             "module_id":$scope.module.module_id
         }).success(function(response){
             if(response.code==1){
                 $scope.apiList=response.data;
                 console.log($scope.apiListInModelu)
             }else{
                 alert(response.msg);
             }
         })
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
                         console.log($scope.suiteList);
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
                 console.log($scope.caseList)
            }else{
                alert($scope.msg);
            }
        })
    }

    $scope.addCase=function(){
        $("#AddCase").modal();
    }

})
