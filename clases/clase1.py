class Persona:
    def __init__(self, nombre, edad, cedula):
        self.nombre = nombre  # nombre es público
        self.__edad = edad    # edad es privado
        self.__cedula = cedula  # cedula es privado

    def obtener_edad(self):
        return self.__edad

    def obtener_cedula(self):
        return self.__cedula

    def establecer_edad(self, nueva_edad):
        self.__edad = nueva_edad

    def establecer_cedula(self, nueva_cedula):
        self.__cedula = nueva_cedula


# Ejemplo de uso:
persona1 = Persona("Juan", 30, "123456789")
print("Nombre:", persona1.nombre)  # nombre es accesible directamente
print("Edad:", persona1.obtener_edad())  # Accediendo a través de método
print("Cédula:", persona1.obtener_cedula())  # Accediendo a través de método

# Intentar acceder a cedula directamente dará un error
# print(persona1.__cedula)  # Esto dará un error

#get
#set



class Persona_con_get_y_set:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, nueva_edad):
        self.__edad = nueva_edad

# Uso de la clase Persona
persona = Persona_con_get_y_set("Juan", 30)
print(persona.nombre)  # Imprime "Juan"
print(persona.edad)    # Imprime 30

persona.nombre = "Carlos"  # Establece el nombre a "Carlos"
print(persona.nombre)      # Imprime "Carlos"

persona.edad = 25  # Establece la edad a 25
print(persona.edad)  # Imprime 25
