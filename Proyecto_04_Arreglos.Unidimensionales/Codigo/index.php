<!DOCTYPE html>
<!-- Actividad Integradora - Arreglos unidimensionales -->
<!-- Materia: Programacion Orientada a Objetos (Corte 4) -->
<!-- Alumno: Hernandez Nuñez Carlos Arturo -->
<!-- No. Control: 252310355 -->
<!-- Fecha 21/05/2026 -->
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Inventario de Tienda</title>
    <!-- Se vincula la hoja de estilos externa -->
    <link rel="stylesheet" href="css/estilos.css">
</head>
<body>
    <h1>Gestión de Inventario</h1>
    <p>Ingrese los datos de al menos 5 productos:</p>
    <!-- Formulario que envía los datos por método POST a procesar.php -->
    <form action="procesar.php" method="POST">
        <!-- Tabla para organizar los campos de entrada -->
        <table>
            <!-- Fila de encabezados -->
            <tr>
                <th>Producto</th>
                <th>Precio (MXN)</th>
            </tr> 
            <!-- Ciclo for para generar 5 filas de productos -->
            <?php for ($i = 1; $i <= 5; $i++): ?>
            <tr>
                <!-- Campo de texto para el nombre del producto -->
                <td><input type="text" name="productos[]" placeholder="Producto <?php echo $i; ?>" required></td>
                
                <!-- Campo numérico para el precio, con step 0.01 para permitir centavos -->
                <td><input type="number" name="precios[]" step="0.01" min="0" placeholder="0.00" required></td>
            </tr>
            <?php endfor; ?>
        </table>  
        <br>
        <!-- Botón para enviar el formulario -->
        <input type="submit" value="Procesar Inventario">
    </form>
</body>
</html>
