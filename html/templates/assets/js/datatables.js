  
$(document).ready(function() {
    $('#example').DataTable( {
    	"pageLength": 20,
    	//"paging":   false,
    	//"ordering": false,
        "info":     false,
        dom: 'Bfrtip',
        buttons: [
            //'copyHtml5',
            //'excelHtml5',
            //'csvHtml5',
            //'pdfHtml5'
        ]
    } );
} );