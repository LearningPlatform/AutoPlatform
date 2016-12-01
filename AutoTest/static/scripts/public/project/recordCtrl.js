myApp.controller('recordCtrl', function ($scope, $http, $cookieStore,$sce) {
        var pro_id = $cookieStore.get("currProID");
        $scope.record_info = {
            host: "192.168.36.32",
            port: 8003,
            filter: "supernano"
        }
        $scope.servers_url = "";
        $scope.reqData = [{}];
        $scope.showiframe = false;
        var dataSocket;
        var baseUrl;
        var socketPort;

        $scope.dfRecord = function () {
            $("#recordModal").modal();
            //$scope.record_info="";
        }

        var reqURL = "";
        var reqString = "";
        var reqLength;
        var data;
        var reqData_str;
        var anyproxy_id_list = [];
        var temp;
        $scope.initSocket = function () {
            dataSocket = new WebSocket("ws://" + baseUrl + ":" + socketPort);
            dataSocket.onmessage = function (event) {
                data = JSON.parse(event.data);
                reqData_str = JSON.stringify(data);

                if (reqData_str.indexOf($scope.record_info.filter) != -1) {
                    data.content.reqHeader = JSON.stringify(data.content.reqHeader);
                    temp = data.content;
                    if (anyproxy_id_list.indexOf(data.content.id) != -1) {
                        $scope.reqData[anyproxy_id_list.indexOf(data.content.id)] = temp;
                    } else {
                        anyproxy_id_list.push(data.content.id)
                        $scope.reqData.push(temp);
                    }
                }
            }
        }

        $scope.startRecord = function () {
            baseUrl = $scope.record_info.host;
            socketPort = $scope.record_info.port;
            $scope.initSocket();
            $("#recordModal").modal('hide');
            $scope.servers_url = $sce.trustAsResourceUrl("http://" + $scope.record_info.host + ":" + "8002/");
            $scope.showiframe = true;
            window.frames["Iframe1"];
        }

        $scope.stopRecord = function () {
            dataSocket.close();
        }

        $scope.setRecord = function () {
            var temp_resp = "";
            $scope.reqData.forEach(function(value,index){
                value.sex='male';
                $http.post("project/record/reqdetail", {
                    host: $scope.record_info.host,
                    port: 8002,
                    req_id: value.id
                }).success(function (response) {
                    if (typeof(response.content) != "undefined") {
                        value.resBody=response.content;
                    }
                })
            });
            $scope.showiframe = false;
            $scope.showtable = true;
        }

        $scope.styleList = [];
        $scope.tableStyle = {
            "background-color": "white",
        }
        $scope.styleChange = {
            "background-color": "#eeeeff",
        }
        $scope.tableGray = function (index) {
            $scope.styleList[index] = $scope.styleChange;
        }
        $scope.tableWhite = function (index) {
            $scope.styleList[index] = $scope.tableStyle;
        }
    }
)
