
var myApp = angular.module('autoTest',['ui.router','ngCookies']);

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
                }
            }
        })

        .state('project.validation',{
            url:'/validation',
            views:{
                'intro@project':{
                    templateUrl: '/static/views/validation.html',
                }
            }
        })

        .state('project.response',{
            url:'/response',
            views:{
                'intro@project':{
                    templateUrl: '/static/views/response.html',
                }
            }
        })

        .state('project.APIDependency',{
            url:'/APIDependency',
            views:{
                'intro@project':{
                    templateUrl: '/static/views/APIDependency.html',
                }
            }
        })

        .state('project.APICase',{
            url:'/APICase',
            views:{
                'intro@project':{
                    templateUrl: '/static/views/APICase.html',
                }
            }
        })

        .state('project.task',{
            url:'/task',
            views:{
                'intro@project':{
                    templateUrl: '/static/views/task.html',
                }
            }
        })

        .state('project.testReport',{
            url:'/testReport',
            views:{
                'intro@project':{
                    templateUrl: '/static/views/testReport.html',
                }
            }
        })
})
