autoTest.factory('NavModel',function($http){
    var navServices = {};

    navServices.getPro = function ($scope,id) {
        console.log(id)
        $http.post("pro_get/",{
            "pro_id": id
        }).success(function(response){
            $scope.pro = response.data;
        });
    };

    return navServices;
})