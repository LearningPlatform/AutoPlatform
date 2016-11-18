myApp.controller('APIDependencyCtrl',function($scope,$http,$cookieStore,$timeout) {
    var pro_id = $cookieStore.get("currProID");
    $scope.showDetail=false;
    $scope.apiDepId=0;
    $scope.apiDepList="";
    $scope.apiDep={
        "depnd_api_name": "获取uid",
        "depnd_api_protocol": "http",
        "depnd_api_desc": "测试描述",
        "depnd_api_method": "post",
        "depnd_api_type": "json",
        "depnd_api_id": 1,
        "depnd_api_url": "{{host}}/index.php?r=api/login/login",
        "depnd_api_param": "{'username': 'liujing3@supernano.com', 'pwd': '670b14728ad9902aecba32e22fa4f6bd'}",
        "pro_id": pro_id,
        "depnd_id": 0
    }

    $timeout(function(){
        $http.post("project/dapi/list",{
            "pro_id":pro_id
        }).success(function(response){
            if(response.code==1){
                $scope.apiDepList=response.data;
            }else{
                alert(response.msg)
            }
        })
    })

    $scope.addAPIDep=function(){
        $scope.apiDep={};
        $("#addapiDep").modal();
    }

    $scope.moreDetail=function(obj){
        $scope.apiDep=obj;
        $scope.apiDepList.push(obj);
        $scope.showDetail=true;

    }

    $scope.saveapiDep=function(obj){
        if(obj.depnd_api_id==null){
            $http.post("project/dapi/create",{
                "depnd_api_name": obj.depnd_api_name,
                "depnd_api_protocol": obj.depnd_api_protocol,
                "depnd_api_desc": obj.depnd_api_desc,
                "depnd_api_method": obj.depnd_api_method,
                "depnd_api_type": obj.depnd_api_type,
                "depnd_api_url": obj.depnd_api_url,
                "depnd_api_param": obj.depnd_api_param,
                "pro_id": pro_id,
                "depnd_id": obj.depnd_id
            }).success(function(response){
                if(response.code==1){
                    $http.post("project/dapi/list",{
                        "pro_id":pro_id
                    }).success(function(response1){
                        if(response1.code==1){
                            $scope.apiDepList=response1.data;
                        }else{
                            alert(response1.msg)
                        }
                    })
                }else{
                    alert(response.msg)
                }
            })
        }else{
            $http.post("project/dapi/edit",{
                "depnd_api_id": obj.depnd_api_id,
                "depnd_api_name": obj.depnd_api_name,
                "depnd_api_protocol": obj.depnd_api_protocol,
                "depnd_api_desc": obj.depnd_api_desc,
                "depnd_api_method": obj.depnd_api_method,
                "depnd_api_type": obj.depnd_api_type,
                "depnd_api_url": obj.depnd_api_url,
                "depnd_api_param": obj.depnd_api_param,
                "pro_id": pro_id,
                "depnd_id": obj.depnd_id
            }).success(function(response){
                if(response.code==0){
                    alert(response.msg)
                }
            })
        }
        $scope.edit=false;
    }

    $scope.apiDepDetail=function(obj){
        $scope.edit=false;
        $scope.apiDepId=obj.depnd_api_id;
        $scope.showDetail=!$scope.showDetail;
        $http.post("project/dapi/detail",{
            "depnd_api_id":obj.depnd_api_id
        }).success(function(response){
            if(response.code==1){
                $scope.apiDep=response.data;
            }else{
                alert(reponse.msg)
            }
        })
    }

    $scope.edit=false;
    $scope.editId=0;
    $scope.editApiDep=function(obj){
        $scope.editId=obj.depnd_api_id;
        $scope.edit=true;
        $scope.apiDepId=obj.depnd_api_id;
        $scope.showDetail=true;
        $http.post("project/dapi/detail",{
            "depnd_api_id":obj.depnd_api_id
        }).success(function(response){
            if(response.code==1){
                $scope.apiDep=response.data;
            }else{
                alert(reponse.msg)
            }
        })
    }

    var delDepID=0;
    $scope.cfdelapiDep=function(id){
        delDepID=id;
        $("#cfapiDep").modal();
    }

    $scope.delapiDep=function(){
        $("#cfapiDep").modal('hide');
        $http.post("project/dapi/delete",{
            "depnd_api_id": delDepID
        }).success(function(response){
            if(response.code==1){
                $http.post("project/dapi/list",{
                    "pro_id":pro_id
                }).success(function(response1){
                    if(response1.code==1){
                        $scope.apiDepList=response1.data;
                    }else{
                        alert(response1.msg)
                    }
                })
            }else{
                alert(response.msg)
            }
        })
    }


})
