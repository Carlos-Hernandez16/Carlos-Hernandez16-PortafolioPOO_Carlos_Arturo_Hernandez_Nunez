"""
Proyecto: Sistema de Usuarios - ITSL
Materia: Programacion Orientada a Objetos (Corte 3)
Alumno: Hernandez Nuñez Carlos Arturo
No. Control: 252310355}
Fecha 11/05/2026
Este archivo coordina la ejecucion del sistema. Aqui implementamos la logica
de interaccion con el usuario y la demostracion de los pilares de la POO
solicitados en la practica: Herencia y Polimorfismo.
"""

from usuario import Usuario
from admin import Admin
from cliente import Cliente
from invitado import Invitado

# Estructura de datos dinamica para gestionar los objetos de forma centralizada
# Esta lista permite aplicar polimorfismo al recorrerla
lista_usuarios = []


# Auxiliares para la interfaz

def dibujar_cabecera(texto):
    """Genera un marco visual para separar las secciones en consola"""
    print("\n" + "~" * 50)
    print(f"  {texto.upper()}")
    print("~" * 50)

def esperar_usuario():
    """Mecanismo de pausa para que el usuario pueda leer los resultados"""
    input("\n[ Presiona Enter para continuar... ]")


# Logica del Sistema

def ejecutar_polimorfismo():
    """
    DEMOSTRACION DE POLIMORFISMO:
    Aqui recorremos la lista de objetos. Aunque todos son tratados como 'Usuario',
    cada uno ejecuta su propia version de 'acceso_sistema()' gracias a la 
    sobreescritura de metodos definida en las clases hijas.
    """
    dibujar_cabecera("Prueba de Polimorfismo")
    print(" Verificando accesos de seguridad segun el tipo de cuenta...\n")
    
    for u in lista_usuarios:
        print(f" > Identificando a: {u.nombre}")
        # El interprete decide en tiempo de ejecucion que metodo llamar
        u.acceso_sistema() 
        print("." * 20)
    esperar_usuario()

def ver_usuarios():
    """Muestra la informacion tecnica de cada objeto almacenado en la lista"""
    dibujar_cabecera("Lista de Usuarios Registrados")
    if not lista_usuarios:
        print(" No hay registros en la base de datos temporal.")
    
    for u in lista_usuarios:
        # Se invoca el metodo heredado de la clase base Usuario
        u.mostrar_datos()
        print("." * 30)
    esperar_usuario()

def nuevo_registro():
    """
    GESTION DINAMICA DE OBJETOS:
    Permite instanciar diferentes clases dependiendo de la necesidad,
    capturando atributos especificos como 'puntos' o 'nivel de acceso'.
    """
    dibujar_cabecera("Registrar Nuevo Usuario")
    print(" 1. Administrador | 2. Cliente | 3. Invitado")
    op = input(" Elige una opcion: ").strip()

    try:
        # Atributos compartidos por la herencia
        nom = input(" Nombre: ").strip()
        correo = input(" Email: ").strip()

        if op == "1":
            # Atributo exclusivo de la clase Admin
            lvl = int(input(" Nivel de acceso (1-5): "))
            user = Admin(nom, correo, lvl)
        elif op == "2":
            # Atributo exclusivo de la clase Cliente
            pts = int(input(" Puntos acumulados: "))
            user = Cliente(nom, correo, pts)
        elif op == "3":
            # El invitado no requiere atributos adicionales
            user = Invitado(nom, correo)
        else:
            print(" ¡Opcion no valida!")
            return

        # Guardamos el objeto en la lista para su gestion posterior
        lista_usuarios.append(user)
        print(f"\n Exito: {nom} ha sido registrado en el sistema.")

    except Exception as e:
        # Manejo basico de errores en la entrada de datos
        print(f"\n Error durante el registro: {e}")
    
    esperar_usuario()

def saludo_general():
    """Demostracion del metodo saludar() implementado como desafio"""
    dibujar_cabecera("Repartiendo saludos")
    for u in lista_usuarios:
        u.saludar()
    esperar_usuario()


# Menu Principal

def mostrar_menu():
    """Ciclo principal que mantiene la aplicacion en ejecucion"""
    while True:
        dibujar_cabecera("Menu del sistema")
        print(" 1) Ver todos los usuarios")
        print(" 2) Dar de alta a alguien")
        print(" 3) Prueba de acceso (Polimorfismo)")
        print(" 4) Mandar saludos")
        print(" 5) Salir")
        
        eleccion = input("\n ¿Que quieres hacer?: ").strip()

        if eleccion == "1": ver_usuarios()
        elif eleccion == "2": nuevo_registro()
        elif eleccion == "3": ejecutar_polimorfismo()
        elif eleccion == "4": saludo_general()
        elif eleccion == "5":
            print("\n Finalizando sesion... ¡Hasta luego!")
            break
        else:
            print(" Entrada no valida, intenta de nuevo.")


# Inicio del programa

if __name__ == "__main__":
    # REQUERIMIENTO: Cargar al menos 1 Admin, 1 Cliente y 1 Invitado
    # Aqui se demuestra el uso de constructores y super() al crear los objetos
    admin_default = Admin("Carlos Hernandez", "carlos.arturo@itsl.edu.mx", 5)
    cliente_default = Cliente("Emiliano Garcia", "emiliano.estudio@gmail.com", 150)
    invitado_default = Invitado("Anonimo_99", "visita@temp.com")

    # Agregamos los objetos iniciales a la coleccion
    lista_usuarios.extend([admin_default, cliente_default, invitado_default])

    # Portada del sistema 
    print("\n" + "#" * 50)
    print("  BIENVENIDO AL SISTEMA DE GESTION DE USUARIOS")
    print("#" * 50)
    
    mostrar_menu()