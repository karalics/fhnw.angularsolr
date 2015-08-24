var app = angular.module("firstApp", ["solr", "ui.bootstrap"]);

app.controller("MainCtrl", ["$scope", "$location",  function($scope, $location){

  $scope.params= $location.search();
}]);

  app.directive("resultDocument", function() {
    return {
      restrict: "E",
      scope :{
        doc : "=record",
      },
      templateUrl:"++resource++fhnw.angularsolr.views/my_result_document.html",
    }
  });
