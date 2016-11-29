myApp.controller('recordCtrl', function ($scope, $http, $cookieStore, $timeout) {
    var pro_id = $cookieStore.get("currProID");
    $scope.record_info={
        host:"10.170.56.122",
        port:8003,
        filter:"url"
    }
    $scope.servers_url = "";
    $scope.reqData=[];
    $scope.showiframe = false;
    var dataSocket;
    var baseUrl;
    var socketPort;

    $scope.dfRecord=function(){
        $("#recordModal").modal();
        //$scope.record_info="";
    }

    var reqURL="";
    var reqString="";
    var reqLength;
    var data;
    var reqData_str;
    $scope.initSocket=function () {
        dataSocket = new WebSocket("ws://" + baseUrl + ":" + socketPort);
        dataSocket.onmessage = function (event) {
            data = JSON.parse(event.data);
            reqData_str = JSON.stringify(data);
            if(reqData_str.indexOf($scope.record_info.filter)!=-1){
                data.content.reqHeader = JSON.stringify(data.content.reqHeader)
                $scope.reqData.push(data.content);
            }
            reqLength=$scope.reqData.length;
            for (var i=0;i<reqLength;i++){
                $scope.styleList.push($scope.tableStyle);
                reqURL="http://10.170.51.96:8002/fetchBody?id="+$scope.reqData[i].id;
                $http.jsonp(reqURL).success(function(response){
                    //response.setHeader("Access-Control-Allow-Origin", "http://127.0.0.1");
                    $scope.reqData.push(response.content);
                })
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
    }

    $scope.styleList=[];
    $scope.tableStyle = {
        "background-color": "white",
    }

    $scope.styleChange = {
        "background-color": "#eeeeff",
    }

    $scope.tableGray = function (index) {
        $scope.styleList[index]=$scope.styleChange;
    }

    $scope.tableWhite = function (index) {
        $scope.styleList[index]=$scope.tableStyle;
    }


})
