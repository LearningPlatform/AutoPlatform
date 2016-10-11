
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
                    templateUrl: '/static/views/project.html',
                    controller: 'proCtrl'
                }
            }
        })

        .state('project.intro',{
            url:'/introduce',
            views:{
                'des@project':{
                    templateUrl: '/static/views/introduce.html',
                }
            }
        })

        .state('project.var',{
            url:'/var',
            views:{
                'des@project':{
                     templateUrl: '/static/views/var.html',
                     controller: 'proVarCtrl'
                }
            }
        })

        .state('project.method',{
            url:'/method',
            views:{
                'des@project':{
                     templateUrl: '/static/views/method.html',
                     controller: 'proMethodCtrl'
                }
            }
        })

        .state('project.validation',{
            url:'/validation',
            views:{
                'des@project':{
                     templateUrl: '/static/views/validation.html',
                     controller: 'proValidationCtrl'
                }
            }
        })

})
