import pandas as pd
from pathlib import Path

ds_path= Path("ds_pi_proyectoindividual/Datasets")       #Nombre de la carpeta donde se encuentran los archivos de los Datasets


def leerCSV_y_concatClient_o_Sucur(archivo):
    df_list= []
    for file in ds_path.glob(f'{archivo}*.csv'):
        print(file)
        df = pd.read_csv(file, delimiter = ';', decimal=",", encoding = "utf-8")
        df_list.append(df)
    return pd.concat((df_list), ignore_index=True, sort=False)

def leerCSV_y_concat(archivo):
    df_list= []
    for file in ds_path.glob(f'{archivo}*.csv'):
        print(file)
        df = pd.read_csv(file, delimiter = ',',  encoding = "utf-8")
        df_list.append(df)
    return pd.concat((df_list), ignore_index=True, sort=False)

def leerCSV_y_concatProveedor(archivo):
    df_list= []
    for file in ds_path.glob(f'{archivo}*.csv'):
        print(file)
        df = pd.read_csv(file, delimiter = ',',  encoding = "latin-1")
        df_list.append(df)
    return pd.concat((df_list), ignore_index=True, sort=False)

def leerXLSX_y_concatCanalVenta(archivo):
    df_list= []
    for file in ds_path.glob(f'{archivo}*.xlsx'):
        print(file)
        df = pd.read_excel(file)
        df_list.append(df)
    return pd.concat((df_list), ignore_index=True, sort=False)