<?php
/**
* Actividad Integradora - Arreglos unidimensionales
* Materia: Programacion Orientada a Objetos (Corte 4)
* Alumno: Hernandez Nuñez Carlos Arturo
* No. Control: 252310355
* Fecha 21/05/2026
*/

// Iniciar sesión para poder pasar datos a resultados.php
session_start();

// Verificar que los datos fueron enviados por método POST
if ($_SERVER["REQUEST_METHOD"] != "POST") {
    header("Location: index.php");
    exit;
}

// Obtener los arreglos desde el formulario
$productos = $_POST['productos'] ?? [];
$precios = $_POST['precios'] ?? [];

// Validar que ambos arreglos tengan la misma cantidad de elementos
if (count($productos) != count($precios) || empty($productos)) {
    die("Error: Los datos enviados son incorrectos.");
}

// Filtrar productos vacíos o precios inválidos
$datosValidos = [];
for ($i = 0; $i < count($productos); $i++) {
    // Solo se guardan productos con nombre no vacío y precio mayor a 0
    if (!empty($productos[$i]) && $precios[$i] > 0) {
        $datosValidos[] = [
            'producto' => htmlspecialchars($productos[$i]), // Previene inyección XSS
            'precio' => (float)$precios[$i]                 // Convierte a número decimal
        ];
    }
}

// Validar que haya al menos un producto válido
if (count($datosValidos) == 0) {
    die("Error: No hay productos válidos para procesar.");
}

// Extraer arreglos limpios usando array_column()
$productosLimpios = array_column($datosValidos, 'producto');
$preciosLimpios = array_column($datosValidos, 'precio');

// Calcular resultados usando funciones nativas de PHP
$total = array_sum($preciosLimpios);                        // Suma total con array_sum()
$promedio = $total / count($preciosLimpios);                // Promedio dividiendo suma entre cantidad
$precioMaximo = max($preciosLimpios);                       // Valor máximo con max()
$precioMinimo = min($preciosLimpios);                       // Valor mínimo con min()

// Encontrar los nombres del producto más caro y más barato usando array_search()
$indiceMaximo = array_search($precioMaximo, $preciosLimpios);
$indiceMinimo = array_search($precioMinimo, $preciosLimpios);
$productoMasCaro = $productosLimpios[$indiceMaximo];
$productoMasBarato = $productosLimpios[$indiceMinimo];

// Guardar todos los resultados en variables de sesión
// para que resultados.php pueda mostrarlos
$_SESSION['productos'] = $productosLimpios;
$_SESSION['precios'] = $preciosLimpios;
$_SESSION['total'] = $total;
$_SESSION['promedio'] = $promedio;
$_SESSION['precioMaximo'] = $precioMaximo;
$_SESSION['precioMinimo'] = $precioMinimo;
$_SESSION['productoMasCaro'] = $productoMasCaro;
$_SESSION['productoMasBarato'] = $productoMasBarato;

// Redirigir a la página de resultados
header("Location: resultados.php");
exit;
?>