from pathlib import Path
import pandas as pd

def leer_excel(anio):
    if(anio == 2025): 
        return (leer_2025())

    else: 
        return (pd.DataFrame())

def leer_2025():
    ARCHIVO = 'epi_2025.xlsx' # Dataset
    DIRECTORIO = Path.cwd().parent / "data" / "raw" / ARCHIVO

    return (pd.read_excel(DIRECTORIO))
