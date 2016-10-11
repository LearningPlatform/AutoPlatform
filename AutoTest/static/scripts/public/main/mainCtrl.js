    myApp.controller('mainCtrl',function($scope,$http,$cookieStore,$timeout){
        var saveType=0;

        $scope.proList='';

        $scope.pro={
            pro_id:0,
            pro_name:'',
            pro_desc:''
        };

        $timeout(function() {
            $http.get('project/list').success(function(response){
                $scope.proList=response.data;
            })
        })

        $scope.addProject=function(){
            $scope.pro='';
            $("#myModal").modal();
        }

        $scope.recordId=function (id) {
            $cookieStore.put("currProID",id);
        };

        $cookieStore.put("activeNav",0);

        $scope.editPro=function(id){
            $http.post('project/detail',{
                "pro_id":id
            }).success(function (response){
                $scope.pro=response.data;
            });
            $("#editModal").modal();
        }

        $scope.save=function(){
            $http.post('project/create',{
                "pro_name":$scope.pro.pro_name,
                "pro_desc":$scope.pro.pro_desc
            }).success(function () {
                $("#myModal").modal('hide');
                $http.get('project/list').success(function(response){
                    $scope.proList=response.data;
                })
        });
        }

        $scope.saveEdit=function(id){
            $http.post('project/edit',{
                "pro_id":id,
                "pro_name":$scope.pro.pro_name,
                "pro_desc":$scope.pro.pro_desc
            }).success(function () {
            $http.get('project/list').success(function(response){
                $scope.proList=response.data;
            })
            $("#editModal").modal('hide');
        });
        }

        $scope.delPro=function(id){
            $http.post('project/delete',{
                "pro_id":id,
            }).success(function () {
            $http.get('project/list').success(function(response){
                $scope.proList=response.data;
            })
        });
        }
    });
