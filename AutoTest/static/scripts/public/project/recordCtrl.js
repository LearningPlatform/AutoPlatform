myApp.controller('recordCtrl', function ($scope, $http, $cookieStore, $timeout) {
    var pro_id = $cookieStore.get("currProID");
    $scope.record_info={
        host:"192.168.36.32",
        port:8003,
        filter:"supernano"
    }
    $scope.servers_url = "";
    $scope.reqData=[];
    $scope.showiframe = false;
    var dataSocket;
    var baseUrl;
    var socketPort;

    $scope.dfRecord=function(){
        $("#recordModal").modal();
    }

    $scope.initSocket=function () {
        dataSocket = new WebSocket("ws://" + baseUrl + ":" + socketPort);
        dataSocket.onmessage = function (event) {
            data = JSON.parse(event.data);
            reqData_str = JSON.stringify(data);
            if(reqData_str.indexOf($scope.record_info.filter)!=-1){
                data.content.reqHeader = JSON.stringify(data.content.reqHeader)
                $scope.reqData.push(data);
            }
        }
    }

    $scope.startRecord = function () {
        baseUrl = $scope.record_info.host;
        socketPort = $scope.record_info.port;
        $scope.initSocket();
        $("#recordModal").modal('hide');
        $scope.servers_url = "http://" + $scope.record_info.host+":"+"8002/";

        $("iframe").attr("src",$scope.servers_url);
    }

    $scope.stopRecord = function () {
        dataSocket.close();
    }

    $scope.showRecord = function () {
        $scope.showtable = false;
        $scope.showiframe = true;
    }

    $scope.setRecord = function () {
        $scope.showiframe = false;
        $scope.showtable = true;
        console.log($scope.reqData)
    }

})
