myApp.controller('recordCtrl', function ($scope, $http, $cookieStore, $timeout) {
    var pro_id = $cookieStore.get("currProID");
    $scope.record_info={
        host:"10.170.18.55",
        port:8003,
        filter:""
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
        //self.bodyCbMap = {};
        dataSocket = new WebSocket("ws://" + baseUrl + ":" + socketPort);
        dataSocket.onmessage = function (event) {
            data = JSON.parse(event.data);
            /*type = data.type;
            $scope.content = data.content;
            reqRef = data.reqRef;
            if (type == "update") {

            } else if (type == "body") {
                if (data.reqRef && self.bodyCbMap[reqRef]) {
                    self.bodyCbMap[reqRef].call(self, content);
                }
            }*/
            $scope.reqData.push(data);
        }
        //self.dataSocket = dataSocket;
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
    }

})
