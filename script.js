var app = angular.module("mainapp", []); 
app.controller("maincontroller", function($scope,$http) {
  $scope.flag = false
    $scope.submit = function(){
      if ($scope.num>=325 || $scope.num<=0){
        alert("Oops! number limit exceeded");

      }
      else
      {
        $scope.flag = true
        $http({
        method: "GET",
        url: "https://ttt--assignment.herokuapp.com/tp?num="+$scope.num,
        dataType: 'json',
        crossDomain: true,
        headers: {
            'Content-Type': 'application/json'
        }
    }).then(function successCallback(response) {
      
   $scope.data1 = response.data;
   $scope.n = 1
  
  }, function errorCallback(response) {
    alert("Sorry couldn't connect!");
  
  });
      }

    	
  };
});
