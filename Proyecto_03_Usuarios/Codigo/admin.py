"""
Proyecto: Sistema de Usuarios - ITSL
Materia: Programacion Orientada a Objetos (Corte 3)
Alumno: Hernandez Nuñez Carlos Arturo
No. Control: 252310355
Fecha 11/05/2026

Modulo que define la clase Admin, derivada de Usuario.
Aqui se implementa un perfil con privilegios elevados, demostrando 
como una clase hija puede extender la funcionalidad del padre.
"""

from usuario import Usuario

# La clase Admin hereda de Usuario para reutilizar nombre y email
class Admin(Usuario):
    """
    Representa a un usuario Administrador con permisos totales.
    
    Ademas de los atributos basicos, esta clase introduce el 
    'nivel_acceso' para determinar que tanto poder tiene en el sistema.
    """

    def __init__(self, nombre, email, nivel_acceso):
        """
        Constructor de Admin.
        
        Se utiliza super() para inicializar los datos en la clase base.
        Despues, establecemos el atributo propio 'nivel_acceso' que 
        caracteriza de forma unica a esta clase.
        """
        super().__init__(nombre, email)
        self.nivel_acceso = nivel_acceso

    # SOBREESCRITURA DE METODOS (POLIMORFISMO):
    # Redefinimos los metodos para que reflejen la autoridad de un Admin.

    def acceso_sistema(self):
        """
        Define el comportamiento de acceso para el perfil administrativo.
        """
        print(f"  [{self.nombre}] Acceso ADMINISTRADOR Nivel {self.nivel_acceso} concedido.")
        print("  -> Permisos: Gestion total de usuarios y configuracion de red.")

    def mostrar_datos(self):
        """
        Muestra la informacion completa del administrador.
        Invocamos super().mostrar_datos() para no tener que escribir 
        de nuevo los prints de nombre y correo.
        """
        super().mostrar_datos()
        print(f"  > Nivel de privilegio: {self.nivel_acceso} de 5")

    def saludar(self):
        """
        Implementacion personalizada del saludo para administradores.
        """
        print(f"  [Admin - {self.nombre}]: Sistema listo. Esperando comandos de gestion.")

    def __str__(self):
        """
        Representacion textual del objeto administrador.
        """
        return f"Admin: {self.nombre} | Nivel: {self.nivel_acceso}"