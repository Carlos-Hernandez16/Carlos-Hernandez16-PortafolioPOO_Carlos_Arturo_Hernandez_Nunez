<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Gestión de bitácoras</title>
</head>
<body>
    <div class="container">
        <h2>Gestion de bitacora diaria</h2>
        
        <!-- Bloque 1: Formulario para registrar actividades -->
        <h3>Registrar nueva actividad</h3>
        <form method="POST" action="">
            <label for="actividad">Descripcion de la actividad:</label>
            <textarea name="actividad" id="actividad" rows="3" required placeholder="Describa la actividad realizada"></textarea>
            
            <label for="responsable">Responsable:</label>
            <input type="text" name="responsable" id="responsable" required placeholder="Nombre del responsable">
            
            <label for="fecha">Fecha:</label>
            <input type="date" name="fecha" id="fecha" required>
            
            <button type="submit">Guardar actividad</button>
        </form>
        
        <?php
        /**
        * Gestión de Bitácoras en Archivos de Texto
        * Materia: Programacion Orientada a Objetos (Corte 4)
        * Alumno: Hernandez Nuñez Carlos Arturo
        * No. Control: 252310355
        * Fecha 26/05/2026
        */
        $archivo = "bitacora.txt";
        $mensaje = "";

        // Procesar el formulario cuando se envia
        if ($_SERVER["REQUEST_METHOD"] == "POST") {
            // Validar que ningun campo este vacio
            if (empty($_POST["actividad"]) || empty($_POST["responsable"]) || empty($_POST["fecha"])) {
                // Si hay error, guardar mensaje en sesion o variable
                $mensaje = "Error: Todos los campos son obligatorios.";
            } else {
                // Sanitizar los datos
                $actividad = htmlspecialchars(trim($_POST["actividad"]));
                $responsable = htmlspecialchars(trim($_POST["responsable"]));
                $fecha = htmlspecialchars(trim($_POST["fecha"]));
                
                // Formato de la actividad
                $contenido = "Fecha: " . $fecha . "\n";
                $contenido .= "Actividad: " . $actividad . "\n";
                $contenido .= "Responsable: " . $responsable . "\n";
                $contenido .= "-------------------------------\n";
                
                // Guardar en el archivo
                $resultado = file_put_contents($archivo, $contenido, FILE_APPEND | LOCK_EX);
                
                if ($resultado !== false) {
                    // INSTRUCCION CLAVE: Redirigir a la misma pagina para evitar duplicados al recargar
                    header("Location: " . $_SERVER["PHP_SELF"]);
                    exit(); // Detener la ejecucion del script
                } else {
                    $mensaje = "Error: No se pudo guardar la actividad.";
                }
            }
        }

        // Verificar si hay un mensaje pendiente (se muestra despues de la redireccion)
        if (isset($_GET["mensaje"])) {
            if ($_GET["mensaje"] == "success") {
                $mensajeMostrar = "<div class='success'>Actividad guardada correctamente.</div>";
            } elseif ($_GET["mensaje"] == "error") {
                $mensajeMostrar = "<div class='error'>Error: Todos los campos son obligatorios.</div>";
            }
        }
        ?>
        
        <hr>
        
        <!-- Bloque 2: Lectura y despliegue de la bitacora -->
        <h3>Bitacora de actividades</h3>
        
        <?php
        // Verificar si el archivo existe antes de leerlo
        if (file_exists($archivo)) {
            // Leer todo el contenido del archivo
            $contenidoBitacora = file_get_contents($archivo);
            
            if ($contenidoBitacora !== false) {
                // Dividir el contenido por el separador de actividades
                $actividades = explode("-------------------------------\n", $contenidoBitacora);
                
                echo "<div class='bitacora'>";
                echo "<ol>";
                
                $contador = 1;
                foreach ($actividades as $actividad) {
                    $actividad = trim($actividad);
                    if (!empty($actividad)) {
                        // Reemplazar saltos de linea por <br> para mostrar en HTML
                        $actividadMostrar = nl2br(htmlspecialchars($actividad));
                        echo "<li><strong>Actividad " . $contador . ":</strong><br>" . $actividadMostrar . "</li>";
                        $contador++;
                    }
                }
                
                echo "</ol>";
                echo "</div>";
                
                if ($contador == 1) {
                    echo "<p>No hay actividades registradas.</p>";
                } else {
                    echo "<p>Total de actividades: " . ($contador - 1) . "</p>";
                }
            } else {
                echo "<div class='error'>Error: No se pudo leer el archivo de bitácora.</div>";
            }
        } else {
            echo "<p>Aun no hay actividades registradas. Complete el formulario para comenzar.</p>";
        }
        ?>
    </div>
</body>
</html>