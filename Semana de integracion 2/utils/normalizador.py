def limpiar_y_convertir(cadena):
    # Reemplazamos . y - por comas para unificar
    cadena = cadena.replace('.', ',').replace('-', ',')
    # Dividimos por comas y convertimos a enteros
    return {int(num) for num in cadena.split(',') if num.strip().isdigit()}
