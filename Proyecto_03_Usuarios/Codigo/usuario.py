"""
Proyecto: Sistema de Usuarios - ITSL
Materia: Programacion Orientada a Objetos (Corte 3)
Alumno: Hernandez Nuñez Carlos Arturo
No. Control: 252310355
Fecha 11/05/2026

Modulo que define la clase base Usuario.
Proporciona la estructura fundamental y las validaciones basicas que 
utilizaran todos los tipos de usuarios en el sistema.
"""

import re

class Usuario:
    """
    Clase base que representa un usuario generico del sistema.
    
    Esta clase funciona como una plantilla. Define los atributos comunes 
    (nombre y email) que seran heredados por Admin, Cliente e Invitado.
    """

    def __init__(self, nombre, email):
        """
        Constructor de la clase Usuario.
        
        Al instanciar cualquier objeto hijo, este codigo se ejecuta para 
        asegurar que el nombre y el correo se guarden correctamente.
        """
        self.nombre = nombre
        # Aplicamos la validacion de email antes de asignar el valor
        self.email = self._validar_email(email)

    # VALIDACION CON EXPRESIONES REGULARES (DESAFIO):
    # Este es un metodo interno para asegurar que el correo sea real.

    def _validar_email(self, email):
        """
        Verifica que el correo tenga un formato correcto (ejemplo@dominio.com).
        """
        patron = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
        if not re.match(patron, email):
            # Si el formato esta mal, lanzamos un error para detener el programa
            raise ValueError(f"Formato de correo no valido: {email}")
        return email

    # METODOS BASE:
    # Estos metodos pueden ser usados tal cual por los hijos o sobreescritos.

    def mostrar_datos(self):
        """
        Muestra la informacion basica en consola.
        Este metodo es llamado por super() desde las clases hijas.
        """
        print(f"  > Nombre: {self.nombre}")
        print(f"  > Email:  {self.email}")
        print(f"  > Rol:    {type(self).__name__}")

    def acceso_sistema(self):
        """
        Metodo destinado al polimorfismo.
        Aqui se define el comportamiento por defecto si una clase hija
        no llegara a sobreescribir sus permisos.
        """
        print(f"  [{self.nombre}] Acceso general: Permisos base activados.")

    def saludar(self):
        """
        Metodo de saludo personalizado (Desafio de la practica).
        """
        print(f"  ¡Hola! Soy {self.nombre} y mi contacto es {self.email}.")

    def __str__(self):
        """
        Define como se ve el objeto si lo imprimimos directamente.
        """
        return f"Usuario: {self.nombre} | {self.email}"