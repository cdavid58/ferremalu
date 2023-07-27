!function ($) {
    "use strict";

    var SweetAlert = function () {
    };

    //examples
    SweetAlert.prototype.init = function () {

        // LOGIN
        $('#validate_login_error').click(function () {
            swal(
                {
                    type: 'error',
                    title: 'Oops...',
                    text: 'Usuario o Contraseña incorrecta',
                }
            )
        });


        // INVOICE
        $('#Add_not_quanty_invoice').click(function () {
            swal(
                {
                    type: 'error',
                    title: 'Oops...',
                    text: 'No puede facturar en cero o vacio',
                    timer: 1500,
                    showConfirmButton:false
                }
            )
        });
        $('#Product_DoesNotExist').click(function () {
            swal(
                {
                    type: 'error',
                    title: 'Oops...',
                    text: 'El producto que busca no existe',
                    timer: 2000,
                    showConfirmButton:false
                }
            )
        });

        $('#Error_Invoice').click(function () {
            swal(
                {
                    type: 'error',
                    title: 'Oops...',
                    text: 'Falta indicar el cliente o ingresar un articulo para la venta',
                    timer: 2000,
                    showConfirmButton:false
                }
            )
        });

        $('#Error_Sold_Out').click(function () {
            swal(
                {
                    type: 'error',
                    title: 'Oops...',
                    text: 'Se agotaron los documentos electrónios',
                    timer: 2000,
                    showConfirmButton:false
                }
            )
        });

        $('#UPDATE_PRODUCT_ERROR').click(function () {
            swal(
                {
                    type: 'error',
                    title: 'Oops...',
                    text: 'Producto no actualizado',
                    timer: 2000,
                    showConfirmButton:false
                }
            )
        });


        $('#UPDATE_PRODUCT').click(function () {
            swal(
                {
                    type: 'success',
                    title: 'Éxito',
                    text: 'El producto fue actualizado con éxito',
                    timer: 2000,
                    showConfirmButton:false
                }
            )
        });

        $('#UPDATE_EMPLOYEE').click(function () {
            swal(
                {
                    type: 'success',
                    title: 'Éxito',
                    text: 'El empleado fue actualizado con éxito',
                    timer: 2000,
                    showConfirmButton:false
                }
            )
        });

        $('#PRODUCT_SAVE_SUCCESS').click(function () {
            swal(
                {
                    type: 'success',
                    title: 'Éxito',
                    text: 'El producto se creo con éxito',
                    timer: 2000,
                    showConfirmButton:false
                }
            )
        });
        $('#PRODUCT_SAVE_ERROR').click(function () {
            swal(
                {
                    type: 'success',
                    title: 'Éxito',
                    text: 'El producto ya existe',
                    timer: 2000,
                    showConfirmButton:false
                }
            )
        });


        // CLIENT
        $('#UPDATED_CLIENT').click(function () {
            swal(
                {
                    type: 'success',
                    title: 'Éxito',
                    text: 'Cliente actualizado con éxito',
                    timer: 2000,
                    showConfirmButton:false
                }
            )
        });


        $('#SOLD_OUT').click(function () {
            swal(
                {
                    type: 'error',
                    title: 'Oops',
                    text: 'Los cupos de empleados estan agotados, puede comprar más cupos si quiere',
                    timer: 3000,
                    showConfirmButton:false
                }
            )
        });

        $('#REGISTERED_EMPLOYEE').click(function () {
            swal(
                {
                    type: 'error',
                    title: 'Oops',
                    text: 'El empleado ya esta registrado',
                    timer: 2000,
                    showConfirmButton:false
                }
            )
        });
        $('#REGISTERED_EMPLOYEE_SUCCESSS').click(function () {
            swal(
                {
                    type: 'success',
                    title: 'Éxito',
                    text: 'El empleado se registro con éxito',
                    timer: 2000,
                    showConfirmButton:false
                }
            )
        });

        $('#DELETED_EMPLOYEE_SUCCESS').click(function () {
            swal(
                {
                    type: 'success',
                    title: 'Éxito',
                    text: 'El empleado se elimino con éxito',
                    timer: 2000,
                    showConfirmButton:false
                }
            )
        });

        $('#DELETED_EMPLOYEE_READY').click(function () {
            swal(
                {
                    type: 'error',
                    title: 'Oops',
                    text: 'El empleado ya fue eliminado',
                    timer: 2000,
                    showConfirmButton:false
                }
            )
        });


        $('#PRODUCT_DOESNOTEXIST').click(function () {
            swal(
                {
                    type: 'error',
                    title: 'Oops',
                    text: 'El producto que busca no éxite',
                    timer: 2000,
                    showConfirmButton:false
                }
            )
        });

        $('#QUANTY_DOESNOTEXIST').click(function () {
            swal(
                {
                    type: 'error',
                    title: 'Oops',
                    text: 'Tiene que agregar una cantidad distinta a cero',
                    timer: 2000,
                    showConfirmButton:false
                }
            )
        });

        $('#TAX_DOESNOTEXIST').click(function () {
            swal(
                {
                    type: 'error',
                    title: 'Oops',
                    text: 'El iva que indica no es valido',
                    timer: 2000,
                    showConfirmButton:false
                }
            )
        });

        $('#NUMBER_INVOICE_DOESNOTEXIST').click(function () {
            swal(
                {
                    type: 'error',
                    title: 'Oops',
                    text: 'Tiene que indicar el número de la factura de compra',
                    timer: 2000,
                    showConfirmButton:false
                }
            )
        });

        $('#NEGATIVE_FIRST_PRODUCT').click(function () {
            swal(
                {
                    type: 'error',
                    title: 'Oops',
                    text: 'No puede agregar una cantidad en negativo en su primera agregada',
                    timer: 2500,
                    showConfirmButton:false
                }
            )
        });


        $('#EXIST_SHOPPING').click(function () {
            swal(
                {
                    type: 'error',
                    title: 'Oops',
                    text: 'La factura ya fue ingresada al sistema, si continua la compra no sera registrada',
                    timer: 2500,
                    showConfirmButton:false
                }
            )
        });


        $('#SUCCESS_SHOPPING').click(function () {
            swal(
                {
                    type: 'success',
                    title: 'Éxito',
                    text: 'La compra se registro con éxito',
                    timer: 2000,
                    showConfirmButton:false
                }
            )
        });

        $('#ERROR_DOCUMENT_LENGTH').click(function () {
            swal(
                {
                    type: 'error',
                    title: 'Oops',
                    text: 'El documento debe tener 9 o 12 caracteres junto al digito de verificación',
                    timer: 2200,
                    showConfirmButton:false
                }
            )
        });

        $('#CLIENT_SUCCES').click(function () {
            swal(
                {
                    type: 'success',
                    title: 'Éxito',
                    text: 'El cliente fue registrado con éxito',
                    timer: 2000,
                    showConfirmButton:false
                }
            )
        });


        $('#REGISTRAMOSCLIENTE').click(function () {
            swal(
                {
                    type: 'info',
                    title: 'Información',
                    text: 'Enviando datos',
                    timer: 1500,
                    showConfirmButton:false
                }
            )
        });

        $('#CLIENTEXIST').click(function () {
            swal(
                {
                    type: 'error',
                    title: 'Oops',
                    text: 'El cliente ya existe',
                    timer: 2000,
                    showConfirmButton:false
                }
            )
        });

        $('#DOCUMENT_ERROR_XLSX').click(function () {
            swal(
                {
                    type: 'error',
                    title: 'Oops',
                    text: 'El documento tiene que ser un documento excel',
                    timer: 2000,
                    showConfirmButton:false
                }
            )
        });


        $('#OUT_STOCK').click(function () {
            swal(
                {
                    type: 'error',
                    title: 'Oops',
                    text: 'La cantidad que indico es mayor a la del stock',
                    timer: 2400,
                    showConfirmButton:false
                }
            )
        });






    },
        //init
        $.SweetAlert = new SweetAlert, $.SweetAlert.Constructor = SweetAlert
}(window.jQuery),

//initializing
    function ($) {
        "use strict";
        $.SweetAlert.init()
    }(window.jQuery);