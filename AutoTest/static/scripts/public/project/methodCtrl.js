myApp.controller('methodCtrl',function($scope,$http,$cookieStore,$timeout) {
    var pro_id = $cookieStore.get("currProID");
    $scope.activeList1=["active","disactive"];
    $scope.funcList="";
    $scope.func={
        "func_desc": "hwbchjdcgxd",
          "pro_id": pro_id,
          "func_code": "wkcjkdwhwjkh",
          "func_name": "test",
          "func_id": 2
    }

    $timeout(function(){
        $http.post("project/func/list",{
             "pro_id": pro_id
        }).success(function (response) {
             if(response.code==1) {
                 $scope.funcList=response.data;
                 console.log($scope.funcList)
             }else{
                alert(response.msg);
            }
        });
    })

    $scope.addFunc=function(){
        $("#addFunc").modal();
        $scope.func={};
    }

    $scope.moreFuncDetail=function(obj){
        $scope.func=obj;
        $scope.funcList.push($scope.func);
        console.log($scope.funcList)
        $scope.showfunc=true;
        $scope.activeList1=["disactive","active"];
        $scope.formation=false;
        $scope.code=true;
    }

    $scope.showfunc=false;
    $scope.funcId=0;
    $scope.funcDetail=function(id){
        $scope.showfunc=!$scope.showfunc;
        $scope.funcId=id;
        $scope.activeList1=["active","disactive"];
        $scope.formation=true;
        $scope.code=false;
        $http.post("project/func/detail",{
            "func_id":id
        }).success(function(response){
            if(response.code==1){
                $scope.func=response.data;
            }else{
                alert(response.msg);
            }
        })
    }

    $scope.active3=function(index){
        for(var i=0;i<2;i++){
            $scope.activeList1[i]="disactive";
        }
        $scope.activeList1[index]="active";
        if(index==0){
            $scope.formation=true;
            $scope.code=false;
        }else{
            $scope.formation=false;
            $scope.code=true;
        }
    }

    $scope.saveFunc=function(obj){
        if(obj.func_id==null){
            $http.post("project/func/create",{
                "pro_id":pro_id,
                "func_name":obj.func_name,
                "func_code":obj.func_code,
                "func_desc":obj.func_desc
            }).success(function(response1){
                if(response1.code==1){
                    $http.post("project/func/list",{
                         "pro_id": pro_id
                    }).success(function (response) {
                         if(response.code==1) {
                             $scope.funcList=response.data;
                             console.log($scope.funcList)
                         }else{
                            alert(response.msg);
                        }
                    });
                }else{
                    alert(response1.msg)
                }
            })
        }else{
            $http.post("project/func/edit",{
                "func_id":obj.func_id,
                "func_name":obj.func_name,
                "func_code":obj.func_code,
                "func_desc":obj.func_desc,
            }).success(function(response){
                if(response.code==0){
                    alert(response.msg)
                }
            })
        }
        $scope.edit=false;
    }

    $scope.editFunc=function(id){
        $scope.editFuncId=id;
        $scope.funcId=id;
        $scope.edit=true;
        $scope.showfunc=true;
        $scope.activeList1=["active","disactive"];
        $scope.formation=true;
        $scope.code=false;
        $http.post("project/func/detail",{
            "func_id":id
        }).success(function(response){
            if(response.code==1){
                $scope.func=response.data;
            }else{
                alert(response.msg);
            }
        })
    }

    var delFuncID=0;
    $scope.cfDelFunc=function(id){
        $("#cfDelFunc").modal();
        delFuncID=id;
    }

    $scope.delFunc=function(){
        $http.post("project/func/delete",{
            "func_id":delFuncID
        }).success(function(response1){
            if(response1.code==1){
                $("#cfDelFunc").modal("hide");
                $http.post("project/func/list",{
                     "pro_id": pro_id
                }).success(function (response) {
                     if(response.code==1) {
                         $scope.funcList=response.data;
                         console.log($scope.funcList)
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
