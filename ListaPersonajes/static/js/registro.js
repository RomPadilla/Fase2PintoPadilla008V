function bloquear() {
	if($('#random').prop('checked')) {
		$("#subida" ).prop( "disabled", true );
		$('.upload' ).hide();
	}
	else {
		$("#subida" ).prop( "disabled", false );
		$('.upload' ).show();
	}
}

function chequearAvatar() {
        var archivo = $("#subida").val();
        var extimagen = (archivo.substring(archivo.lastIndexOf(".")).toLowerCase());
        if(extimagen != ".jpg" && extimagen != ".png")
			{
				alert("El archivo de tipo " + extimagen + "no es válido");
				return false;
			}
		else
			{
				return true;
			}
		
}

var patronnomape = "^[a-zA-Z]{1,16}$";
var patronemail = "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+.[a-zA-Z]{2,4}$";
var patronnum = "^[0-9]{9}$"
var patroncon = "^[a-zA-Z0-9._%+-]{8,16}$"
 
function chequearentrada(id, patron) {
	if ($(id).val().match(patron)){
		$(id).css('background-color', 'white');
		return true;
	}
	else{
		$(id).css('background-color', 'red');
		return false;
	}

}

function validarform(){
	if($('#random').prop('checked')) {
		if (chequearentrada("#nombre",patronnomape) && chequearentrada("#ape",patronnomape) &&
		chequearentrada("#email",patronemail) && chequearentrada("#num",patronnum) &&
		chequearentrada("#usuario",patronnomape) && chequearentrada("#pw",patroncon)){
			$("#formulario").submit();
		
		}
		else{
			alert("Hay errores en el formulario");
		}

	}
	else {
		if (chequearentrada("#nombre",patronnomape) && chequearentrada("#ape",patronnomape) &&
		chequearentrada("#email",patronemail) && chequearentrada("#num",patronnum) &&
		chequearentrada("#usuario",patronnomape) && chequearentrada("#pw",patroncon) && chequearAvatar()){
			$("#formulario").submit();
		}
		else{
			alert("Hay errores en el formulario");
		}
	}

}