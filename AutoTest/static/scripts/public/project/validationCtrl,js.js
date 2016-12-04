myApp.controller('validationCtrl',function($scope,$http,$cookieStore,$timeout) {
    var pro_id = $cookieStore.get("currProID");
    $scope.activeList2=["active","disactive"];
    $scope.checkList=[];
    $scope.check={
        "check_name": "",
        "check_id": 0,
        "pro_id": pro_id,
        "check_desc": "",
        "check_code": ""
    }

     $timeout(function(){
        $http.post("project/check/list",{
             "pro_id": pro_id
        }).success(function (response) {
             if(response.code==1) {
                 $scope.checkList=response.data;
             }else{
                alert(response.msg);
            }
        });
    })

    $scope.addCheck=function(){
        $("#addCheck").modal();
        $scope.check={};
    }

    $scope.moreCheckDetail=function(obj){
        $scope.check=obj;
        $scope.checkList.push($scope.check);
        $scope.showcheck=true;
        $scope.activeList2=["disactivec","active"];
        $scope.formation=false;
        $scope.code=true;
    }

    $scope.showcheck=false;
    $scope.checkId=0;
    $scope.checkDetail=function(id){
        $scope.showcheck=!$scope.showcheck;
        $scope.checkId=id;
        $scope.activeList2=["active","disactive"];
        $scope.formation=true;
        $scope.code=false;
        $http.post("project/check/detail",{
            "check_id":id
        }).success(function(response){
            if(response.code==1){
                $scope.check=response.data;
            }else{
                alert(response.msg);
            }
        })
    }

    $scope.active4=function(index){
        for(var i=0;i<2;i++){
            $scope.activeList2[i]="disactive";
        }
        $scope.activeList2[index]="active";
        if(index==0){
            $scope.formation=true;
            $scope.code=false;
        }else{
            $scope.formation=false;
            $scope.code=true;
        }
    }

    $scope.runResult={};
    $scope.runCheck=function(obj){
        $("#runCheck").modal();
        $http.post("project/check/run",{
            "check_name":obj.check_name,
            "check_code":obj.check_code
        }).success(function(response) {
            if(response.code==1){
                if(response.data.status == 1){
                    $scope.runResult=response.data;
                }
                else {
                    $scope.runResult = {
                        status: response.data.status,
                        output: "【异常】："+response.data.error + "【具体信息】:"+response.data.output
                    }
                }
            }else{
                alert(response.msg)
            }
        })
    }

    $scope.saveCheck=function(obj){
         if(obj.check_desc==""){
            obj.check_desc=" ";
        }
        if(obj.check_code==null){
            obj.check_code=" ";
        }
        if(obj.check_id==null){
            $http.post("project/check/run",{
                "check_name":obj.check_name,
                "check_code":obj.check_code
            }).success(function(response){
                if(response.code==1) {
                    if (response.data.status == 1) {
                        $http.post("project/check/create", {
                            "pro_id":pro_id,
                            "check_name":obj.check_name,
                            "check_code":obj.check_code,
                            "check_desc":obj.check_desc
                        }).success(function (response1) {
                            if (response1.code == 1) {
                                $http.post("project/check/list", {
                                    "pro_id": pro_id
                                }).success(function (response2) {
                                    if (response2.code == 1) {
                                        $scope.checkList = response2.data;
                                    } else {
                                        alert(response2.msg);
                                    }
                                });
                            } else {
                                alert(response1.msg)
                            }
                        })
                    } else {
                        alert("【异常】："+response.data.error + "【具体信息】:"+response.data.output)
                    }
                }
                else {
                    alert(response.msg)
                }
            })
        }else{
            $http.post("project/check/run",{
                "check_name":obj.check_name,
                "check_code":obj.check_code
            }).success(function(response){
                if(response.code==1){
                    if (response.data.status == 1) {
                        $http.post("project/check/edit", {
                            "check_id":obj.check_id,
                            "check_name":obj.check_name,
                            "check_code":obj.check_code,
                            "check_desc":obj.check_desc
                        }).success(function (response1) {
                            if (response1.code == 0) {
                                alert(response1.msg)
                            }
                        })
                    } else {
                        alert("【异常】："+response.data.error + "【具体信息】:"+response.data.output)
                    }
                }
                else {
                    alert(response.msg)
                }
            })
        }
        $scope.edit=false;
    }

    $scope.editCheck=function(id){
        $scope.editCheckId=id;
        $scope.checkId=id;
        $scope.edit=true;
        $scope.showcheck=true;
        $scope.activeList2=["active","disactive"];
        $scope.formation=true;
        $scope.code=false;
        $http.post("project/check/detail",{
            "check_id":id
        }).success(function(response){
            if(response.code==1){
                $scope.check=response.data;
            }else{
                alert(response.msg);
            }
        })
    }

    var delCheckID=0;
    $scope.cfDelCheck=function(id){
        $("#cfDelCheck").modal();
        delCheckID=id;
    }

    $scope.delCheck=function(){
        $http.post("project/check/delete",{
            "check_id":delCheckID
        }).success(function(response1){
            if(response1.code==1){
                $("#cfDelCheck").modal("hide");
                $http.post("project/check/list",{
                     "pro_id": pro_id
                }).success(function (response) {
                     if(response.code==1) {
                         $scope.checkList=response.data;
                     }else{
                        alert(response.msg);
                    }
                });
            }else{
                alert(response1.msg)
            }
        })
    }
})

