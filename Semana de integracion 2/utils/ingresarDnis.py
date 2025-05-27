#y luego le solicite los DNI. 
#en base a ese FOR vas a sacar 2 variables, una que sea de tipo set, y otra que sea de tipo list.
def ingresar_dnis(cant_integrantes):
    dnis_list = []
    for i in range(cant_integrantes):
        dni = int(input(f"Ingrese el DNI del integrante {i + 1}: "))
        dnis_list.append(dni)
    return dnis_list