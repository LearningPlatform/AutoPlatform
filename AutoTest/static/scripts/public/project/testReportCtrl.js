myApp.controller('testReportCtrl', function ($scope, $http, $cookieStore, $timeout) {
    var pro_id = $cookieStore.get("currProID");
    $scope.wid = {}
    $scope.List = ['active'];
    $scope.reportDetal = [];
    $scope.suiteList = "";
    $scope.resultList = "";
    $scope.result = {
        "result_id": 1,
        "suite_id": 1,
        "start_time": "1478617457",
        "pass_num": 1,
        "report_name": "test",
        "end_time": "1478617457",
        "fail_num": 1,
        "pro_id": 1
    }
    $scope.allResult = [];
    $scope.api = {
        "api_param": "username,pwd",
        "api_id": 1,
        "module_id": 1,
        "pro_id": pro_id,
        "api_url": "",
        "api_method": "post",
        "api_type": "34",
        "api_protocol": "http",
        "api_name": "登录接口",
        "api_desc": "登录"
    }

    var date;
    var m;
    var s;
    $scope.timeInval = [];
    $timeout(function () {
        $scope.suite = "";
        $scope.startDate = "";
        $scope.endDate = "";
        $scope.title = "";
        $http.post('project/suite/list', {
            "pro_id": pro_id
        }).success(function (response) {
            if (response.code == 1) {
                $scope.suiteList = response.data;
            } else {
                alert(response.msg)
            }
        })
        $scope.repDetail = false;
        $scope.repList = true;
        $http.post('project/result/list', {
            "pro_id": pro_id
        }).success(function (response1) {
            if (response1.code = 1) {
                $scope.resultList = response1.data;
                for (var i = 0; i < $scope.resultList.length; i++) {
                    date = new Date(($scope.resultList[i].end_time - $scope.resultList[i].start_time) * 1000);
                    m = date.getMinutes();
                    s = date.getSeconds();
                    if (m > 0) {
                        $scope.timeInval[i] = m + "m" + s + "s";
                    } else {
                        $scope.timeInval[i] = s + "s";
                    }
                }
            } else {
                alert(response1.msg)
            }
        })
    })

    $scope.clearSelect = function () {
        $scope.suite = "";
        $scope.startDate = "";
        $scope.endDate = "";
        $scope.title = "";
    }

    $scope.showDetail = function (obj) {
        $scope.result = obj;
        $scope.repList = false;
        $scope.repDetail = true;
        $http.post('project/result/detailList', {
            "result_id": obj.result_id
        }).success(function (response) {
            if (response.code = 1) {
                $scope.allResult = response.data;
                $scope.resultStr = "";
                for (var i = 0; i < $scope.allResult.length - 1; i++) {
                    $scope.reportDetal[i] = false;
                     $scope.styleList.push($scope.tableStyle);
                }
            } else {
                alert(response.msg)
            }
        })
    }

    $scope.showReport = function (obj, index) {
        $http.post("project/api/detail", {
            "api_id": obj.api_id
        }).success(function (response) {
            if (response.code == 1) {
                $scope.api = response.data;
            } else {
                alert(response.msg);
            }
        })
        $scope.reportDetal[index] = !$scope.reportDetal[index];
    }

    $scope.returnList = function () {
        $scope.repDetail = false;
        $scope.repList = true;
        $http.post('project/result/list', {
            "pro_id": pro_id
        }).success(function (response1) {
            if (response1.code = 1) {
                $scope.resultList = response1.data;
            } else {
                alert(response.msg)
            }
        })
    }

    $scope.delReport = function (id) {
        $http.post("project/result/delete", {
            "result_id": id
        }).success(function (response) {
            if (response.code == 1) {
                $http.post('project/result/list', {
                    "pro_id": pro_id
                }).success(function (response1) {
                    if (response1.code = 1) {
                        $scope.resultList = response1.data;
                    } else {
                        alert(response1.msg)
                    }
                })
            } else {
                alert(response.msg)
            }
        })
    }

    $scope.styleList=[];
    $scope.tableStyle = {
        "background-color": "white",
        //"height": "35px"
    }

    $scope.styleChange = {
        "background-color": "#eeeeff",
        //"height": "35px"
    }

    $scope.tableGray = function (index) {
        $scope.styleList[index]=$scope.styleChange;

    }

    $scope.tableWhite = function (index) {
        $scope.styleList[index]=$scope.tableStyle;
    }

    $('.form_date').datetimepicker({
        format: 'yyyy-mm-dd',
        startDate: '1900-01-01',
        autoclose: true,
        bootcssVer: 3,
        language: 'zh_CN',
        minView: "month"
    });
})
