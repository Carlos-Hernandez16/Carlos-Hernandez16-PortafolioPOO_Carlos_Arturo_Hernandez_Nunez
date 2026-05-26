<?php
/**
* Actividad Integradora - Arreglos unidimensionales
* Materia: Programacion Orientada a Objetos (Corte 4)
* Alumno: Hernandez Nuñez Carlos Arturo
* No. Control: 252310355
* Fecha 21/05/2026
*/

// Iniciar sesión para recuperar los datos guardados por procesar.php
session_start();

// Verificar que existen datos en sesión, si no redirigir al formulario
if (!isset($_SESSION['productos']) || empty($_SESSION['productos'])) {
    header("Location: index.php");
    exit;
}

// Recuperar los datos guardados en sesion
$productosLimpios = $_SESSION['productos'];
$preciosLimpios = $_SESSION['precios'];
$total = $_SESSION['total'];
$promedio = $_SESSION['promedio'];
$productoMasCaro = $_SESSION['productoMasCaro'];
$productoMasBarato = $_SESSION['productoMasBarato'];
$precioMaximo = $_SESSION['precioMaximo'];
$precioMinimo = $_SESSION['precioMinimo'];

// Limpiar la sesión después de recuperar los datos (opcional)
// session_destroy(); // Descomentar si no se quiere reutilizar
?>

<!DOCTYPE html>
<!-- Pagina de resultados del inventario -->
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Resultados del Inventario</title>
    <!-- Se vincula la hoja de estilos externa -->
    <link rel="stylesheet" href="css/estilos.css">
</head>
<body>

    <h1>Resultados del Inventario</h1>

    <!-- Tabla con los productos ingresados -->
    <h2>Productos registrados</h2>
    <table class="tabla-resultados">
        <tr>
            <th>#</th>
            <th>Producto</th>
            <th>Precio (MXN)</th>
        </tr>
        
        <!-- Ciclo for para mostrar cada producto en una fila -->
        <?php for ($i = 0; $i < count($productosLimpios); $i++): ?>
        <tr>
            <td><?php echo $i + 1; ?></td>
            <td><?php echo $productosLimpios[$i]; ?></td>
            <td>$<?php echo number_format($preciosLimpios[$i], 2); ?></td>
        </tr>
        <?php endfor; ?>
    </table>

    <!-- Resultados destacados -->
    <div class="resultado">
        <h2>Resumen del inventario</h2>
        <p><strong>Total de la venta:</strong> $<?php echo number_format($total, 2); ?></p>
        <p><strong>Promedio de precios:</strong> $<?php echo number_format($promedio, 2); ?></p>
        <p><strong>Producto más caro:</strong> <?php echo $productoMasCaro; ?> ($<?php echo number_format($precioMaximo, 2); ?>)</p>
        <p><strong>Producto más barato:</strong> <?php echo $productoMasBarato; ?> ($<?php echo number_format($precioMinimo, 2); ?>)</p>
    </div>

    <!-- Botón para volver al formulario -->
    <a href="index.php" class="btn">Registrar nuevos productos</a>

</body>
</html>