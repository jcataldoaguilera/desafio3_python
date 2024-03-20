# Info
# Autor: Juan Cataldo [jcataldoaguilera@gmail.com]
# Fecha: 2024-03-19
# RLAB-23-02-09-0044-2
#

# Programa
if input("¿Responde a estímulos? (S/N): ").lower() == "s" :
    print("+ Valorar la necesidad de llevarlo al hospital más cercano +")
else :
    print("Abrir la vía Aerea")
    if input("¿Respira?: (S/N) ").lower() == "s" :
        print("+ Permitirle posición de suficiente ventilación +")
    else :
        print("Administrar 5 Ventilaciones y llamar a la Ambulancia")
        amb = "n"
        while amb == "n" :
            if input("¿Signos de Vida?: (S/N) ").lower() == "s" :
                print("Reevaluar a la espera de la ambulancia")
            else :
                print("Administrar compresiones toraxicas hasta que llegue la ambulancia")
            amb = input("¿Llegó la ambulancia?: (S/N)").lower()