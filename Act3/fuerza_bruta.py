# Info
# Autor: Juan Cataldo [jcataldoaguilera@gmail.com]
# Fecha: 2024-03-19
# RLAB-23-02-09-0044-2
#

# Librerias
from string import ascii_lowercase
from getpass import getpass

# Variables
password = [*getpass("Ingrese la contraseña: ")]
cracked = []
intentos = 0

# Loop
for y in ascii_lowercase :
    if len(password) == len(cracked) :
        break
    for z in password :
        if y == z :
            cracked.append(y)
            intentos += 1
        else :
            intentos += 1

print(f"La contraseña fue forzada en {intentos} intentos.")