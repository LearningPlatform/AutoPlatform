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
     })

     $timeout(function(){
         var nav_id = $cookieStore.get('activeNav');
         for (var i=0;i<9;i++){
             $scope.activeList[i]="disactive";
         }
         $scope.activeList[nav_id]='active';
     });

     $scope.active = function(id) {
         $cookieStore.put("activeNav",id);
         for (var i=0;i<9;i++){
             $scope.activeList[i]="disactive";
         }
         $scope.activeList[id]='active';
     }
 })

