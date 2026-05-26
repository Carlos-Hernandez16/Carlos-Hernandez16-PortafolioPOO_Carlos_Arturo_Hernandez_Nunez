<?php

require_once 'Paquete.php';
require_once 'Sensor.php';

// Instancias de Paquete
$paqueteA = new Paquete();
$paqueteB = new Paquete();

// Asignar valores a propiedades públicas
$paqueteA->codigoSeguimiento = "45624";
$paqueteA->pesoKilogramos = 5.5;
$paqueteA->esFragil = true;

// Intento de asignar propiedad privada
// $paqueteA->costoInterno = 10.0; 
// Error: No se puede acceder a una propiedad privada desde fuera de la clase.

// Instancia de Sensor
$sensor = new Sensor();
$sensor->id = 1;
$sensor->marca = "Sony";
$sensor->ultimaLectura = new DateTime();
$sensor->rangoMaximo = 100.0;

echo "<h2>Resumen de logística</h2>";

echo "Código de seguimiento: " . $paqueteA->codigoSeguimiento . "<br>";
echo "Peso: " . $paqueteA->pesoKilogramos . " kg<br>";
echo "Fragilidad: " . ($paqueteA->esFragil ? 'Si' : 'No') . "<br>";

echo "<h2>Estado del sensor</h2>";

echo "ID: " . $sensor->id . "<br>";
echo "Marca: " . $sensor->marca . "<br>";
echo "Última Lectura: " . $sensor->ultimaLectura->format('Y-m-d H:i:s') . "<br>";
echo "Rango Máximo: " . $sensor->rangoMaximo . " unidades";

?>