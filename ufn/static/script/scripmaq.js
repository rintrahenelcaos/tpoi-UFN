
function FuncionResponsiveNavbar() {
    var x = document.getElementById("minavbar");
    if (x.className === "navbar_lista_links") {
      x.className += " responsive";
    } else {
      x.className = "navbar_lista_links";
    }
}

function FuncionMuestraNoticias() {
  var x = document.getElementById("deslizador_id");
  if (x.className === "deslizador") {
    x.className += " mas_noticias";
  } else {
    x.className = "deslizador";
  }
}

function CambioTramite(evt, TramiteActivo ){
  var i, contenido_pestania, pestania_link;

  contenido_pestania = document.getElementsByClassName("contenido_pestania");
  for (i = 0; i < contenido_pestania.length; i++) {
    contenido_pestania[i].style.display = "none";
  } 

  pestania_link = document.getElementsByClassName("pestania_link");
  for (i = 0; i < pestania_link.length; i++) {
    pestania_link[i].className = pestania_link[i].className.replace("active", "");
  }

  document.getElementById(TramiteActivo).style.display = "block";
  evt.currentTarget.className += " active";
}







function validarPreinscripcion() {
  let apellido = document.forms["pre-inscripcion_form"]["apellido"].value;
  let nombre = document.forms["pre-inscripcion_form"]["nombre"].value;
  let dni = document.forms["pre-inscripcion_form"]["dni"].value;
  let cuil = document.forms["pre-inscripcion_form"]["cuil"].value;
  let email = document.forms["pre-inscripcion_form"]["email"].value;
  let genero = document.forms["pre-inscripcion_form"]["genero"].value;
  let alumno_existente = document.forms["pre-inscripcion_form"]["alumno_existente"].value;
  let id_curso = document.forms["pre-inscripcion_form"]["id_curso"].value;

  if (apellido=="" || nombre=="" || dni=="" || cuil=="" || email=="" || genero=="" || alumno_existente=="" || id_curso=="") {
    alert("Todos los campos son obligatorios")
  } 
  

}

function validarSolicituTit() {
  let apellido = document.forms["soltit_form"]["apellido"].value;
  let nombre = document.forms["soltit_form"]["nombre"].value;
  let dni = document.forms["soltit_form"]["dni"].value;
  let matricula = document.forms["soltit_form"]["matricula"].value;
  let id_curso = document.forms["soltit_form"]["id_curso"].value;
  let comision = document.forms["soltit_form"]["comision"].value;
  

  if (apellido=="" || nombre=="" || dni=="" || matricula=="" || id_curso=="" || comision=="" ) {
    alert("Todos los campos son obligatorios")
  } 
  

}

function validarPagoMatricula() {
  let apellido = document.forms["pago_matricula_form"]["apellido"].value;
  let nombre = document.forms["pago_matricula_form"]["nombre"].value;
  let matricula = document.forms["pago_matricula_form"]["matricula"].value;
  let comprobante = document.forms["pago_matricula_form"]["comprobante"].value;
  
  

  if (apellido=="" || nombre=="" || matricula=="" || comprobante=="" ) {
    alert("Todos los campos son obligatorios")
  } 
  

}

function validarSeguimiento() {
  let apellido = document.forms["seguimiento_form"]["apellido"].value;
  let nombre = document.forms["seguimiento_form"]["nombre"].value;
  let cod_tramite = document.forms["seguimiento_form"]["cod_tramite"].value;
  
  
  

  if (apellido=="" || nombre=="" || cod_tramite==""  ) {
    alert("Todos los campos son obligatorios")
  } 
  

}