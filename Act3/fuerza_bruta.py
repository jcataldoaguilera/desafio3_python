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
intentos = 0
print(password)

# Loop
for i in ascii_lowercase :
    if i in password :
        print(i)
        intentos += 1

print(f"La contraseña fue forzada en {intentos} intentos.")
# print([*password])