'use strict'

//TODO -  update this path to your basepyramid application
require('../basepyramid/basepyramid/static/scripts/app.js');

var appt = angular.module("myModule");

//this code will override the controller myController2 in the base pyramid application
//in a similar way code can be extended with another controller, directive, ...
appt.controller("myController2", function ($scope) {
    var employee = {
        firstName : "Anna",
        lastName : "Smith Davidov",
        gender : "Female"
    };
    $scope.employee2 = employee;
});