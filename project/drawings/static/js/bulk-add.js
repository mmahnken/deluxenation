angular.module("bulkAdd", [])

    .controller('AddController', function ($scope, $http) {

        $scope.groups = [];
        $scope.globalGroups = {};
        $scope.notebooks = [];
        $scope.drawings = [];

        $http.get("/nb/all?format=json").then(function (response) {
                    $scope.notebooks = JSON.parse(response.data.data);
        });

        $http.get("/groups/all?format=json").then(function (response) {
                    $scope.groups = JSON.parse(response.data.data);
        });




        $scope.handleDirectoryChoice = function (e){
            for (var i=0; i<e.files.length; i++) {
                var f = e.files[i];
                var title = f.name.split('.').slice(0, -1).join(' ');
                var drawing = {
                    data: URL.createObjectURL(f),
                    fileObj: f,
                    groups: {},
                    shouldSave: true,
                    title: title,
                    favorite: false,
                };
                $scope.drawings.push(drawing);
                $scope.$apply();
            }
        };

        $scope.updateNotebook = function (el){
            el.d.notebook = el.notebook;
        };

        $scope.updateAllNotebooks = function (el){

            for (var i=0; i < $scope.drawings.length; i++) {
                var d = $scope.drawings[i];
                d.notebook = el.globalNotebook;
            }
        };


        $scope.updateAllGroups = function (el){
            for (var i=0; i < $scope.drawings.length; i++) {
                var d = $scope.drawings[i];
                d.groups[el.group.pk] = $scope.globalGroups[el.group.pk];
            }
        };
    })

    .config(function($interpolateProvider) {
                $interpolateProvider.startSymbol('{[{');
                $interpolateProvider.endSymbol('}]}');
    });
