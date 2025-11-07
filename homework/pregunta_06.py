"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """

    ruta = "files/input/data.csv"
    stats = {}
    with open(ruta, "r", encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")
            if not line:
                continue
            parts = line.split("\t")
            if len(parts) < 5:
                continue
            dict_field = parts[4]
            for pair in dict_field.split(","):
                if not pair:
                    continue
                if ":" not in pair:
                    continue
                key, val_str = pair.split(":", 1)
                key = key.strip()
                try:
                    val = int(val_str.strip())
                except ValueError:
                    continue
                if key in stats:
                    cur_min, cur_max = stats[key]
                    if val < cur_min:
                        cur_min = val
                    if val > cur_max:
                        cur_max = val
                    stats[key] = (cur_min, cur_max)
                else:
                    stats[key] = (val, val)
    return [(k, stats[k][0], stats[k][1]) for k in sorted(stats.keys())]