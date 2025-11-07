"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    archivo = "files/input/data.csv"
    resultado = {}
    with open(archivo, "r", encoding="utf-8") as f:
        for linea in f:
            linea = linea.strip()
            if not linea:
                continue
            columnas = linea.split("\t")
            clave = columnas[0]

            # la columna 5 contiene pares clave:valor separados por comas
            # sumar solo los valores numericos y agregarlos por clave
            col5 = columnas[4]
            suma_fila = 0
            for par in col5.split(','):
                if not par:
                    continue
                partes = par.split(':')
                if len(partes) != 2:
                    continue
                try:
                    valor = int(partes[1])
                except ValueError:
                    # si no es entero, ignora
                    continue
                suma_fila += valor

            resultado[clave] = resultado.get(clave, 0) + suma_fila
    return resultado


