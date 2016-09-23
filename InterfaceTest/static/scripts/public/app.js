var autoTest=angular.module('autoTest',['ui.router','ngCookies'])
    .config(function($stateProvider,$urlRouterProvider,$interpolateProvider) {
        $interpolateProvider.startSymbol('{$');
        $interpolateProvider.endSymbol('$}');
        $urlRouterProvider.when("","/index")
        $stateProvider
            .state('index',{
                url:'/index',
                views:{
                    '':{
                        templateUrl: '/static/view/main.html',
                        controller:'MainCtrl'
                    }
                }
            })
            .state('project',{
                url:'/project',
                views:{
                    '':{
                        templateUrl: '/static/view/project.html',
                    },
                    'topBar@project':{
                         templateUrl: '/static/view/pro_top.html',
                         controller:  'ProTopCtrl'
                    },
                    'leftBar@project':{
                         templateUrl: '/static/view/pro_nav.html',
                         controller:  'ProNavCtrl'
                    },
                }
            })
        .state('project.var',{
                url:'/var',
                views:{
                    'rightBar@project':{
                         templateUrl: '/static/view/var.html',
                    }
                }
            })
        .state('project.overview',{
                url:'/overview',
                views:{
                    'rightBar@project':{
                         templateUrl: '/static/view/overview.html',
                    }
                }
            })
        .state('project.case',{
                url:'/case',
                views:{
                    'rightBar@project':{
                         templateUrl: '/static/view/case.html',
                    }
                }
            })
    })