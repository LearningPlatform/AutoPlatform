
var myApp = angular.module('autoTest',['ui.router','ngCookies','monospaced.elastic',"chart.js"]);

myApp.config(function($stateProvider,$urlRouterProvider,$interpolateProvider) {
    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
    $urlRouterProvider.when("", "/index");
    $stateProvider
        .state('index', {
            url: '/index',
            views: {
                '': {
                    templateUrl: '/static/views/main.html',
                    controller: 'mainCtrl'
                }
            }
        })

        .state('project',{
            url:'/project',
            views:{
                '':{
                    templateUrl: '/static/views/projectIntro.html',
                    controller: 'proCtrl'
                },
                'intro@project':{
                    templateUrl: '/static/views/homepage.html',
                    controller: 'homepageCtrl'
                }
            }
        })

        .state('project.homepage',{
            url:'/homepage',
            views:{
                'intro@project':{
                    templateUrl: '/static/views/homepage.html',
                    controller: 'homepageCtrl'
                }
            }
        })

        .state('project.globalVar',{
            url:'/globalVar',
            views:{
                'intro@project':{
                    templateUrl: '/static/views/globalVar.html',
                    controller: 'globalVarCtrl'
                }
            }
        })

        .state('project.method',{
            url:'/method',
            views:{
                'intro@project':{
                    templateUrl: '/static/views/method.html',
                    controller: 'methodCtrl',
                }
            }
        })

        .state('project.validation',{
            url:'/validation',
            views:{
                'intro@project':{
                    templateUrl: '/static/views/validation.html',
                    controller: 'validationCtrl',
                }
            }
        })

        .state('project.response',{
            url:'/response',
            views:{
                'intro@project':{
                    templateUrl: '/static/views/response.html',
                    controller: 'responseCtrl',
                }
            }
        })

        .state('project.APIDependency',{
            url:'/APIDependency',
            views:{
                'intro@project':{
                    templateUrl: '/static/views/APIDependency.html',
                    controller:'APIDependencyCtrl'
                }
            }
        })

        .state('project.APICase',{
            url:'/APICase',
            views:{
                'intro@project':{
                    templateUrl: '/static/views/APICase.html',
                    controller:'APICaseCtrl'
                }
            }
        })

        .state('project.task',{
            url:'/task',
            views:{
                'intro@project':{
                    templateUrl: '/static/views/task.html',
                    controller:'taskCtrl'
                }
            }
        })

        .state('project.testReport',{
            url:'/testReport',
            views:{
                'intro@project':{
                    templateUrl: '/static/views/testReport.html',
                    controller: 'testReportCtrl'
                }
            }
        })

        .state('project.record',{
            url:'/record',
            views:{
                'intro@project':{
                    templateUrl: '/static/views/record.html',
                    controller: 'recordCtrl'
                }
            }
        })
})
