import math

def distancia_euclidiana(x_1=0.0, y_1=0.0, x_2=0.0, y_2=0.0):
  distancia = math.sqrt(((x_2-x_1)**2)+((y_2-y_1)**2))
  return distancia

x_1 = float(input("Ingresa x1: "))
y_1 = float(input("Ingresa y1: "))
x_2 = float(input("Ingresa x2: "))
y_2 = float(input("Ingresa y2: "))

d = distancia_euclidiana(x_1, y_1, x_2, y_2)

print("La distancia es", d)
