print("Actividad 9 Clase Humano")
print("Francisco Luévano Mat: 22308051281074")
# Zona de class
class Humano1074:
    # Zona de atributos dentro de la clase
    edad=0
    estatura=""
    colorojos=""
    fecha_nac=""
    hijos=""
    peso=""
    #Zona de Funciones dentro de la clase
    def correr1074(self,n):
        print(f"{n} corre")
    def comer1074(self,n):
        print(f"{n} come")
    def dormir1074(self,n):
        print(f"{n} duerme")
    def trabajar1074(self,n):
        print(f"{n} trabaja")
    def leer1074(self,n):
        print(f"{n} lee")
    def conducir1074(self,n):
        print(f"{n} conduce")
        
    #Zona de creación de objetos
francisco=Humano1074()
perla=Humano1074()
# Zona de uso de objetos
print("---Resultados para Francisco---")
francisco.edad=17
francisco.estatura="178cm"
francisco.colorojos="Café"
francisco.fecha_nac="17/08/07"
francisco.hijos="Ninguno"
francisco.peso="83kg"

print(f"Edad: {francisco.edad}")
print(f"Estatura: {francisco.estatura}")
print(f"Color de ojos: {francisco.colorojos}")
print(f"Fecha de nacimiento: {francisco.fecha_nac}")
print(f"Hijos: {francisco.hijos}")
print(f"Peso: {francisco.peso}")

francisco.correr1074("Francisco")
francisco.comer1074("Francisco")
francisco.dormir1074("Francisco")
francisco.trabajar1074("Francisco")
francisco.leer1074("Francisco")
francisco.conducir1074("Francisco")

print("---Resultados para Perla---")
perla.edad=42
perla.estatura="160cm"
perla.colorojos="Negro"
perla.fecha_nac="07/04/91"
perla.hijos="Tres"
perla.peso="83kg"

print(f"Edad: {perla.edad}")
print(f"Estatura: {perla.estatura}")
print(f"Color de ojos: {perla.colorojos}")
print(f"Fecha de nacimiento: {perla.fecha_nac}")
print(f"Hijos: {perla.hijos}")
print(f"Peso: {perla.peso}")

perla.correr1074("Perla")
perla.comer1074("Perla")
perla.dormir1074("Perla")
perla.trabajar1074("Perla")
perla.leer1074("Perla")
perla.conducir1074("Perla")
perla.correr1074("Perla")