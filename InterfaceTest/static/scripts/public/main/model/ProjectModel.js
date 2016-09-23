autoTest.factory('ProjectModel',function($http){
    var proServices={};

    proServices.getProList = function ($scope) {
        $http.get("pro_list/").success(function(response) {
            $scope.proList=response.data;
            console.log(response)
        });
    };
    
    proServices.addPro = function ($scope,saveType) {
        $http.post("pro_save/",{
            "type":saveType,
            "pro_id": $scope.pro.pro_id,
            "pro_name": $scope.pro.pro_name,
            "pro_desc": $scope.pro.pro_desc
        }).success(function (response) {
            $scope.proList=response.data;
        });
    };

    proServices.getPro = function ($scope,id) {
         $http.post("pro_get/",{
            "pro_id": id
        }).success(function(response){
            $scope.pro.pro_id = response.data.id;
            $scope.pro.pro_name = response.data.pro_name;
            $scope.pro.pro_desc = response.data.pro_desc;
        });
    };

    proServices.delPro = function ($scope,id) {
        console.log(id)
        $http.post("pro_del/",{
            "pro_id": id,
        }).success(function (response) {
            $scope.proList=response.data;
        });
    }
    return proServices
});
