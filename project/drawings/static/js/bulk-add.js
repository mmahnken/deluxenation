angular.module("bulkAdd", [])

    .controller('AddController', function ($scope, $http) {

        $scope.groups = [];
        $scope.notebooks = [];
        $scope.drawings = [];

        $http.get("/nb/all?format=json").then(function (response) {
                    $scope.notebooks = JSON.parse(response.data.data);
        });

        $http.get("/groups/all?format=json").then(function (response) {
                    $scope.groups = JSON.parse(response.data.data);
        });

        $scope.test = function(){
          $scope.drawings.push($scope.notebook);
        };



        $scope.handleDirectoryChoice = function (e){
            for (var i=0; i<e.files.length; i++) {
                var f = e.files[i];
                var drawing = {
                    data: URL.createObjectURL(f),
                    fileObj: f
                };
                $scope.drawings.push(drawing);
                $scope.$apply();
            }
        };


        //
        // $scope.stockPrice = Math.random() * 1000;
        //
        // $scope.buy = function(nshares) {
        //     $scope.message = nshares + " shares bought!";
        //     $timeout(function () {
        //         $scope.message = "";
        //     }, 1500);
        // };
    })

    .config(function($interpolateProvider) {
                $interpolateProvider.startSymbol('{[{');
                $interpolateProvider.endSymbol('}]}');
    });
