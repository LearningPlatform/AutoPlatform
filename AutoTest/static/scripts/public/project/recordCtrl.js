myApp.controller('recordCtrl', function ($scope, $http, $cookieStore, $timeout) {
    var pro_id = $cookieStore.get("currProID");
    var dataSocket;
    $scope.record_info={
        host:"192.168.1.102",
        port:8003,
        filter:""
    }
    $scope.servers_url = ""
    $scope.reqData=[]
    $scope.showiframe = false

    $scope.dfRecord=function(){
        $("#recordModal").modal();
    }

    $scope.startRecord = function () {
        var baseUrl = $scope.record_info.host,
            socketPort = $scope.record_info.port;

        function initSocket() {
            self.bodyCbMap = {};
            dataSocket = new WebSocket("ws://" + baseUrl + ":" + socketPort);
            dataSocket.onmessage = function (event) {
                data = JSON.parse(event.data),
                        type = data.type,
                        content = data.content,
                        reqRef = data.reqRef;
                if (type == "update") {

                } else if (type == "body") {

                    if (data.reqRef && self.bodyCbMap[reqRef]) {
                        self.bodyCbMap[reqRef].call(self, content);
                    }
                }
                $scope.reqData.push(data);
                console.log($scope.reqData)
            }
            self.dataSocket = dataSocket;

        }

        initSocket();
        $("#recordModal").modal('hide');
        $scope.servers_url = "http://" + $scope.record_info.host+":"+"8002/"
        $("iframe").attr("src",$scope.servers_url);

    }

    $scope.stopRecord = function () {
        dataSocket.close()
    }

    $scope.showRecord = function () {

        $scope.showtable = false
        $scope.showiframe = true
    }

    $scope.setRecord = function () {
        $scope.showiframe = false
        $scope.showtable = true
    }

})
