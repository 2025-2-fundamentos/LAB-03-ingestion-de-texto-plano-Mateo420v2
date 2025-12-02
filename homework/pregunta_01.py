import pandas as pd

"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel


def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


    """

    with open("files/input/clusters_report.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
    
    columns = ["cluster", "cantidad_de_palabras_clave", "porcentaje_de_palabras_clave", "principales_palabras_clave"]
    

    data = []
    current_row = None  
    cluster_counter = 1 
    

    for line in lines[4:]:
        if line.strip():  
            if line[:4].strip().isdigit():
                if current_row:  
                    data.append(current_row)
                cluster = cluster_counter
                cluster_counter += 1  
                cantidad = int(line[5:18].strip())
                porcentaje = float(line[19:33].strip().replace(",", ".").replace("%", ""))
                palabras_clave = line[34:].strip()
                current_row = [cluster, cantidad, porcentaje, palabras_clave]
            else:
               
                if current_row:
                    current_row[-1] += " " + line.strip()


    if current_row:
        data.append(current_row)
    df = pd.DataFrame(data, columns=columns)
    df["principales_palabras_clave"] = (
        df["principales_palabras_clave"]
        .str.replace("\s+", " ", regex=True)
        .str.replace(", ", ",")
        .str.replace(",", ", ")
        .str.strip()
        .str.rstrip(".")
    )
    
    return df

if __name__ == "__main__":
    resultado = pregunta_01()
    output_file = "output.txt"
    resultado.to_csv(output_file, sep="\t", index=False)
