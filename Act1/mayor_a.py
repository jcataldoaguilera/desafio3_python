# Info
# Autor: Juan Cataldo [jcataldoaguilera@gmail.com]
# Fecha: 2024-03-19
# RLAB-23-02-09-0044-2
#

# Balances del año anterior
ventas = {
"Enero": 15000,
"Febrero": 22000,
"Marzo": 12000,
"Abril": 17000,
"Mayo": 81000,
"Junio": 13000,
"Julio": 21000,
"Agosto": 41200,
"Septiembre": 25000,
"Octubre": 21500,
"Noviembre": 91000,
"Diciembre": 21000,
}

# Librerias
from sys import argv

# Variables
i = int(argv[1])
filtro = {}

# Loop
for k,v in ventas.items() :
    if v > i :
        salida = {k:v}
        filtro.update(salida)

# Resultado
print(filtro)