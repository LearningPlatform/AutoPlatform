 myApp.controller('proCtrl',function($scope,$http,$cookieStore,$timeout){
     var pro_id = $cookieStore.get("currProID");
     $scope.activeList=["active","disactive","disactive","disactive","disactive","disactive","disactive","disactive","disactive"];

    $scope.pro={};

     $timeout(function() {
         $http.post('project/detail', {
             "pro_id": pro_id
         }).success(function (response) {
             $scope.pro = response.data;
         });
         for (var i=0;i<9;i++){
             $scope.activeList[i]="disactive";
         }
         $scope.activeList[0]='active';
     })

     $scope.active = function(id) {
         for (var i=0;i<9;i++){
             $scope.activeList[i]="disactive";
         }
         $scope.activeList[id]='active';
     }
 })

