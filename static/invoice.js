$(document).ready(function(){
	$(".save_invoice_local").click(function(){
		const invoice = new Object()
		let consecutive = $("#consecutive").text()

		var filas = $(".father").find("tr");
        var resultado = "";
        let subtotal_row_table_invoice = 0
		let tax_row_table_invoice = 0
		invoice.products = []

        for(i=0; i<filas.length; i++){
            var celdas = $(filas[i]).find("td");
        	subtotal_row_table_invoice += parseFloat($(celdas[9]).text())
        	tax_row_table_invoice += parseFloat($(celdas[6]).text())
        	invoice.products.push(
        		{
        			'consecutive':consecutive,
					'type' : 2,
					'payment_form' : 1,
					'cancelled' : true,
					'employee' : 14,
					'client' : 31,
					'company' : 26,
					'date' : '2023-03-01',
					'date_expired' : '2023-03-01',
					'time' : '21:45',
        			"CODIGO" : $(celdas[1]).text().trim(),
        			"DESCRIPCION" : $(celdas[2]).text().trim(),
        			"CANTIDAD" : $(celdas[3]).text().replace('-','').replace('+','').trim(),
        			"VAL. UNIT" : $(celdas[4]).text().trim(),
        			"IVA" : $(celdas[5]).text().trim(),
        			"VAL. IVA" : $(celdas[6]).text().trim(),
        			"DESC." : $(celdas[7]).text().trim(),
        			"VAL. DESC." : $(celdas[8]).text().trim(),
        			"SUBTOTAL" : $(celdas[9]).text().trim(),
        			"TIPO DE VENTA" : $(celdas[10]).text().trim(),
        		}
        	)
        }

        localStorage.setItem('invoice_'+consecutive,JSON.stringify(invoice))
        Clean()
        CalculateTotalsInvoice()
	})

	$(".send_invoice_localstorage").click(function(){
		__data = JSON.parse(localStorage.getItem('invoice'))
		let exist = false
		for(i = 0; i < localStorage.length; i++ ){
			if(localStorage.key(i).includes('invoice')){
				exist = true
				__data = JSON.parse(localStorage.getItem(localStorage.key(i)))
				var settings = {
				  "url": "https://apiferre.pythonanywhere.com/invoice_fe/CREATE_INVOICE/",
				  "method": "POST",
				  "timeout": 0,
				  "headers": {
				    "Content-Type": "application/json"
				  },
				  "data": JSON.stringify(__data['products']),
				};

				$.ajax(settings).done(function (response) {
				  console.log(response);
				  for(i = 0; i < localStorage.length; i++ ){
					if(localStorage.key(i).includes('invoice')){
					  localStorage.removeItem(localStorage.key(i));
					  $.gritter.add({
		                    title: 'EXITO',
		                    text: "La Factura que estaba guardada fue registrada con exito."
		               });
					}
				  }
				});

			}
		}
		if(!exist){
			$.gritter.add({
                title: 'Oops!',
                text: "No tiene facturas pendientes"
            });
		}

	})
})