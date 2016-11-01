app
// =========================================================================
// Show View and Delete Autor 
// =========================================================================
    .controller("ClienteCtrl", function($scope, $state, $stateParams, catalogoService, $window, $mdDialog, $log, toastr) {
    //Valores iniciales
    $scope.fields = 'nombre';
    var params = {};
    $scope.lista = [];
    $scope.cliente = {};

    $scope.list = function(params) {
        $scope.isLoading = true;
        catalogoService.Cliente.query(params, function(r) {
            $scope.lista = r.results;
            $scope.options = r.options;
            $scope.isLoading = false;
        }, function(err) {
            $log.log("Error in list:" + JSON.stringify(err));
            toastr.error(err.data.results.detail, err.status + ' ' + err.statusText);
        });
    };
    $scope.list(params);

    $scope.buscar = function() {
        params.page = 1;
        params.fields = $scope.fields;
        params.query = $scope.query;
        $scope.list(params);
    };

    $scope.onReorder = function(order) { //TODO
        $log.log('Order: ' + order);
    };

    $scope.delete = function(d) {
        if ($window.confirm("Seguro?")) {
            catalogoService.Cliente.delete({ id: d.id }, function(r) {
                $log.log("Se eliminó cliente:" + JSON.stringify(d));
                toastr.success('Se eliminó cliente ' + d.nombre, 'Cliente');
                $scope.list(params);
            }, function(err) {
                $log.log("Error in delete:" + JSON.stringify(err));
                toastr.error(err.data.detail, err.status + ' ' + err.statusText);
            });
        }
    };

})

// =========================================================================
// Create and Update Autor
// =========================================================================
.controller("AutorSaveCtrl", function($scope, $state, $stateParams, clienteService, $window, $mdDialog, $log, toastr) {
    //Valores iniciales
    $scope.cliente = {};

    $scope.sel = function() {
        catalogoService.ACliente.get({ id: $stateParams.id }, function(r) {
            $scope.Cliente = r;
        }, function(err) {
            $log.log("Error in get:" + JSON.stringify(err));
            toastr.error(err.data.detail, err.status + ' ' + err.statusText);
        });
    };
    if ($stateParams.id) {
        $scope.sel();
    }

    $scope.save = function() {
        if ($scope.cliente.id) {
            catalogoService.Cliente.update({ id: $scope.cliente.id }, $scope.cliente, function(r) {
                $log.log("r: " + JSON.stringify(r));
                toastr.success('Se editó cliente ' + r.nombre, 'Cliente');
                $state.go('catalogo.catalogo.cliente');
            }, function(err) {
                $log.log("Error in update:" + JSON.stringify(err));
                toastr.error(err.data.detail, err.status + ' ' + err.statusText);
            });
        } else {
            catalogoService.Cliente.save($scope.cliente, function(r) {
                $log.log("r: " + JSON.stringify(r));
                toastr.success('Se insertó cliente ' + r.nombre, 'Clienter');
                $state.go('catalogo.catalogo.cliente');
            }, function(err) {
                $log.log("Error in save:" + JSON.stringify(err));
                toastr.error(err.data.detail, err.status + ' ' + err.statusText);
            });
        }
    };

    $scope.cancel = function() {
        $state.go('catalogo.catalogo.cliente');


        
    };
});
