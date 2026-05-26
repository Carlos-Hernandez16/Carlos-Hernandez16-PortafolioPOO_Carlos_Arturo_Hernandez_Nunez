"""
Proyecto: Sistema de Usuarios - ITSL
Materia: Programacion Orientada a Objetos (Corte 3)
Alumno: Hernandez Nuñez Carlos Arturo
No. Control: 252310355
Fecha 11/05/2026

Modulo que define la clase Invitado, derivada de Usuario.
En este archivo se aplica la herencia para crear un perfil con
permisos restringidos dentro del sistema.
"""

from usuario import Usuario

# La clase Invitado hereda de Usuario, obteniendo sus atributos y metodos
class Invitado(Usuario):
    """
    Representa a un usuario sin cuenta registrada.
    
    No agrega atributos nuevos, pero es fundamental para demostrar 
    como una clase hija puede comportarse de forma distinta a la 
    clase padre mediante la sobreescritura.
    """

    def __init__(self, nombre, email):
        """
        Constructor de Invitado.
        
        Aqui usamos super() para enviar el nombre y el correo a la
        clase base Usuario. Esto evita duplicar la logica de 
        inicializacion y validacion que ya existe en el padre.
        """
        super().__init__(nombre, email)

    # SOBREESCRITURA DE METODOS:
    # Redefinimos acceso_sistema para que el comportamiento sea 
    # especifico para los invitados, cumpliendo con el polimorfismo.
    
    def acceso_sistema(self):
        """
        Define el nivel de acceso minimo para este tipo de objeto.
        """
        print(f"  [{self.nombre}] Acceso como INVITADO detectado.")
        print("  -> Aviso: Solo puedes ver contenido publico sin cuenta activa.")

    def saludar(self):
        """
        Personalizacion del saludo para el perfil de invitado.
        """
        print(f"  [Invitado - {self.nombre}]: Hola, solo estoy explorando la plataforma.")

    def __str__(self):
        """
        Representacion simplificada del objeto en formato de texto.
        """
        return f"Invitado: {self.nombre}"