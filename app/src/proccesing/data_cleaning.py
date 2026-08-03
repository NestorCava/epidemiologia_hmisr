from datetime import datetime
from pathlib import Path
import os

import pandas as pd


def cleaning_2025() -> pd.DataFrame:

    # IMPORTACION DE DATOS DEL 2025

    ANIO = "2025"  # Año bajo estudio
    ARCHIVO = "epi_2025.xlsx"  # Dataset
    DIRECTORIO = Path(__file__).resolve().parent.parent / "data" / "raw" / ARCHIVO

    # Para CSV
    # df = pd.read_csv(file_path)

    # Para Excel (XLSX)
    df = pd.read_excel(DIRECTORIO)

    # Eliminación de las columnas SEXO, LOCALIDAD, CONSULTA Y MÉDICO
    df.drop(columns=["SEXO", "LOCALIDAD", "CONSULTA", "MÉDICO"], inplace=True)

    # CAMBIO DEL FORMATO DE LA FECHA, SE LE AGREGA EL AÑO Y SE CAMBIA EL TIPO DE DATO

    # Esto es para el dataset del 2025 en donde:
    standardize_dates(ANIO, df)

    # ELIMINACIÓN DE LA COLUMNA DEL MES POR CONSIDERARSE REDUNDANTE
    df.drop(columns=["MES"], inplace=True)

    # AGREGAMOS UNA COLUMNA PARA IDENTIFICAR EL AÑO EPIDEMIOLÓGICO
    inser_epi_year(1, ANIO, df)

    # AGREGAMOS COLUMNA PARA IDENTIFICAR EL DÍA DE LA SEMANA
    insert_day(2, df)

    return df


def standardize_dates(
    epi_year: str | None = None, df: pd.DataFrame | None = None
) -> pd.DataFrame:

    # Si no se envía nada, se inicializa el DataFrame vacío de forma segura
    if df is None:
        df = pd.DataFrame()
        return df

    # Inicializo el año epidemiológico en el año actual
    if epi_year is None:
        epi_year = str(datetime.now().year)

    #  * Si SEMEPI = 1 y MES = DICIEMBRE => AÑO = 2024
    #  * Si SEMEPI = 53 y MES = ENERO => AÑO = 2026
    #  * Para el resto de los casos AÑO = 2025

    for i in range(len(df["FECHA"])):
        dia = df["FECHA"][i].split("/")[1]
        mes = df["FECHA"][i].split("/")[0]
        fecha = ""

        if mes == "12" and df["SEMEPI"][i] == 1:
            fecha = dia + "/" + mes + "/" + str(int(epi_year) - 1)

        elif mes == "01" and df["SEMEPI"][i] == 53:
            fecha = dia + "/" + mes + "/" + str(int(epi_year) + 1)

        else:
            fecha = dia + "/" + mes + "/" + epi_year

        df.at[i, "FECHA"] = fecha

    df["FECHA"] = pd.to_datetime(df["FECHA"], format="%d/%m/%Y")

    return df


def insert_day(loc: int = 2, df: pd.DataFrame | None = None) -> pd.DataFrame:

    # Si no se envía nada, se inicializa el DataFrame vacío de forma segura
    if df is None:
        df = pd.DataFrame()
        return df

    df.insert(loc=loc, column="DIA", value=df["FECHA"].dt.day_name())

    df["DIA"] = df["DIA"].replace(
        {
            "Sunday": "DOMINGO",
            "Monday": "LUNES",
            "Tuesday": "MARTES",
            "Wednesday": "MIERCOLES",
            "Thursday": "JUEVES",
            "Friday": "VIERNES",
            "Saturday": "SABADO",
        }
    )

    return df


def inser_epi_year(
    loc: int = 1, epi_year: str | None = None, df: pd.DataFrame | None = None
) -> pd.DataFrame:

    # Si no se envía nada, se inicializa el DataFrame vacío de forma segura
    if df is None:
        df = pd.DataFrame()
        return df

    # Inicializo el año epidemiológico en el año actual
    if epi_year is None:
        epi_year = str(datetime.now().year)

    df.insert(loc=loc, column="ANIOEPI", value=epi_year)

    return df


def save_epi_year(df: pd.DataFrame | None = None) -> bool:
    # Si no se envía nada, se inicializa el DataFrame vacío de forma segura
    if df is None:
        return False

    # Define el nombre del archivo
    ARCHIVO = "epi_2025.csv"  # Dataset
    DIRECTORIO = Path(__file__).resolve().parent.parent / "data" / "processed" / ARCHIVO
    # archivo = 'datos.csv'

    # Comprueba si el archivo ya existe
    archivo_existe = os.path.exists(DIRECTORIO)

    # Guarda o agrega datos
    df.to_csv(DIRECTORIO, mode='a', index=False, header=not archivo_existe, encoding='utf-8')
    
    return True
