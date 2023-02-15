import pandas as pd #importamos Pandas para leer y mostrar las tablas del csv.
import matplotlib.pyplot as plt #importamos Matplotlib para hacer los gráficos y mostrarlos.

#Leemos el csv.
df = pd.read_csv("organizations-100.csv")

#Hacemos que nos agrupe las columnas que tengan datos con el mismo valor y nos sume los valores.
datos=df.groupby("Industry").sum()
#Hacemos que nos ordene la gráfica en orden descendente.
datos=datos.sort_values("Number_of_employees", ascending=False)

#Asignamos colores para cada columna (Hay 10 industrias, 10 colores diferentes).
colores=["grey","c","yellow","b","brown","g","violet","pink","k","r"]

#Ponemos que nos haga un gráfico de barras.
#datos.index es el eje x.
#datos["Number of employees"] es el eje y.
#color=colores se utiliza para asignar los colores que hemos puesto anteriormente.
plt.bar(datos.index, datos["Number_of_employees"], color=colores)

#Ponemos un título para la gráfica.
plt.title("Número de empleados de cada industria")

#Mostramos la gráfica.
plt.show()





