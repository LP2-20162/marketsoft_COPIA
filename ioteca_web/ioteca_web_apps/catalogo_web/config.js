var catalogoUrl = 'http://localhost:9000/api/catalogo/';


var config = {

    catalogoUrl: catalogoUrl,


};

app

    .value('configCatalogo', config);


app.constant('ROUTERS2', {
    "xxx": {
        "url": "/xxx",
        "templateUrl": "templates/xxx.html"
    },
    "catalogo": {
        "url": "/catalogo",
        "views": {
            "": {
                "templateUrl": "app/views/layout.html"
            },
            "aside": {
                "templateUrl": "app/views/aside.html"
            },
            "content": {
                "templateUrl": "app/views/content.html"
            }
        }
    },

    "catalogo.catalogo": {
        "url": "/catalogo",
        "template": "<div ui-view ></div>"
    },

    "catalogo.catalogo.producto": {
        "url": "/producto",
        "data": {
            "section": "Catálogo",
            "page": "producto"
        },
        "templateUrl": "ioteca_web_apps/catalogo_web/views/producto/index.html"
    },
    "catalogo.catalogo.productoNew": {
        "url": "/producto/new",
        "data": {
            "section": "Catálogo",
            "page": "Producto"
        },
        "templateUrl": "ioteca_web_apps/catalogo_web/views/producto/form.html"
    },
    "catalogo.catalogo.productoEdit": {
        "url": "/producto/:id/edit",
        "data": {
            "section": "Catálogo",
            "page": "Producto"
        },
        "templateUrl": "ioteca_web_apps/catalogo_web/views/producto/form.html"
    },

    "catalogo.catalogo.cliente": {
        "url": "/cliente",
        "data": {
            "section": "Catálogo",
            "page": "Cliente"
        },
        "templateUrl": "ioteca_web_apps/catalogo_web/views/cliente/index.html"
    },
    "catalogo.catalogo.clienteNew": {
        "url": "/cliente/new",
        "data": {
            "section": "Catálogo",
            "page": "Cliente"
        },
        "templateUrl": "ioteca_web_apps/catalogo_web/views/cliente/form.html"
    },
    "catalogo.catalogo.clienteEdit": {
        "url": "/cliente/:id/edit",
        "data": {
            "section": "Catálogo",
            "page": "Cliente"
        },
        "templateUrl": "ioteca_web_apps/catalogo_web/views/cliente/form.html"
    }

});
