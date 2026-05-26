"""
Proyecto: Sistema de Usuarios - ITSL
Materia: Programacion Orientada a Objetos (Corte 3)
Alumno: Hernandez Nuñez Carlos Arturo
No. Control: 252310355
Fecha 11/05/2026

Modulo que define la clase Cliente, derivada de Usuario.
En este archivo vemos como extender una clase base agregando 
atributos especificos y metodos propios para una funcionalidad nueva.
"""

from usuario import Usuario

# La clase Cliente expande la funcionalidad de Usuario
class Cliente(Usuario):
    """
    Representa a un usuario estandar con sistema de fidelizacion.
    
    Ademas de heredar el nombre y el correo, esta clase gestiona 
    un contador de puntos para el usuario.
    """

    def __init__(self, nombre, email, puntos=0):
        """
        Constructor de Cliente.
        
        Usamos super() para inicializar la parte de 'Usuario' y 
        luego asignamos el atributo propio 'puntos' que solo 
        existe en esta clase hija.
        """
        super().__init__(nombre, email)
        self.puntos = puntos

    # SOBREESCRITURA DE METODOS:
    # Adaptamos el comportamiento del acceso para mostrar los puntos.
    
    def acceso_sistema(self):
        """
        Define los permisos exclusivos del perfil de cliente.
        """
        print(f"  [{self.nombre}] Acceso como CLIENTE concedido.")
        print(f"  -> Estado actual: {self.puntos} puntos disponibles para canje.")

    def mostrar_datos(self):
        """
        Extendemos el metodo mostrar_datos del padre.
        Primero llamamos al metodo de la clase base y luego 
        agregamos la informacion de los puntos.
        """
        super().mostrar_datos()
        print(f"  > Puntos: {self.puntos}")

    # METODOS PROPIOS:
    # Estos metodos no existen en la clase Usuario, son unicos de Cliente.

    def agregar_puntos(self, cantidad):
        """
        Permite incrementar el saldo de puntos del cliente.
        """
        if cantidad > 0:
            self.puntos += cantidad
            print(f"  [{self.nombre}] Se han sumado {cantidad} puntos.")
        else:
            print("  Error: La cantidad de puntos debe ser positiva.")

    def saludar(self):
        """
        Implementacion del saludo para el perfil de cliente.
        """
        print(f"  [Cliente - {self.nombre}]: Hola, ¿tienen alguna oferta especial hoy?")

    def __str__(self):
        """
        Formato de texto para identificar rapidamente al objeto cliente.
        """
        return f"Cliente: {self.nombre} | Puntos: {self.puntos}"