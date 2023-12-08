<?php

if ($_SERVER['REQUEST_METHOD'] === 'POST') {

    $name = $_POST['name'];
    $email = $_POST['email'];
    $message = $_POST['message'];
    $to = 'bonattig.sofia@gmail.com';
    $subject = 'Nuevo mensaje de contacto';
    $body = "Nombre: $name\nEmail: $email\nMensaje: $message";
    $headers = "From: $email";


    if (mail($to, $subject, $body, $headers)) {
        echo '¡Gracias por tu mensaje! Nos pondremos en contacto con vos pronto.';
    } else {
        echo 'Hubo un error al enviar el mensaje. Por favor, intentá nuevamente.';
    }
} else {
    echo 'Acceso inválido al formulario.';
}
?>