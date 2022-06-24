import pandas as pd
import numpy as np
class NormalizadorDataFrame:
    def __init__(self):
        return None

    def eliminar_columnas_vacias(self, df_entrada:pd.DataFrame): 
        df = df_entrada.copy()
        for c in df:
            esta_vacia = df[c].isnull().sum() == df.shape[0]
            if esta_vacia:
                df.drop(columns=c,inplace=True)
        
        return df
        

    def upper_strings(self, df_entrada:pd.DataFrame):
        df = df_entrada.copy()
        for i in df:
            if df[i].dtype == 'O':
                df[i] = df[i].str.upper()
        
        return df
        
    def llenar_nulos(self,df_entrada:pd.DataFrame):
        df = df_entrada.copy()
        for i in df:
            if df[i].dtype == 'O':
                df[i] = df[i].fillna('Sin datos')
            else:
                df[i] = df[i].fillna(0)
        
        return df

    def eliminar_duplicados(self,df_entrada:pd.DataFrame):
        df = df_entrada.copy()
        for i in df:
            df[i].drop_duplicates(inplace=True)
        
        return df

    def corregir_geolocalizacion(self, df_entrada:pd.DataFrame):
        df = df_entrada.copy()
        if 'X' in df and 'Y' in df:
            df['X'][df.X > 0] = df['X'][df.X > 0] * -1      # las latitudes y longitudes deben ser valores negativos
            df['Y'][df.Y > 0] = df['Y'][df.Y > 0] * -1
        
        return df

    def agregar_rango_etario(self, df_entrada:pd.DataFrame):
        df = df_entrada.copy()
        if 'Edad' in df:
            df['Rango_Etario'] = '-'
            df['Rango_Etario'][df.Edad <= 30] = '1_Hasta 30 años'
            df['Rango_Etario'][(df.Edad <= 40) & (df.Rango_Etario == '-')] = '2_De 31 a 40 años'
            df['Rango_Etario'][(df.Edad <= 50) & (df.Rango_Etario == '-')] = '3_De 41 a 50 años'
            df['Rango_Etario'][(df.Edad <= 60) & (df.Rango_Etario == '-')] = '4_De 51 a 60 años'
            df['Rango_Etario'][(df.Edad > 60) & (df.Rango_Etario == '-')] = '5_Desde 60 años'
        
        return df

    def eliminar_columnas(self,df_entrada:pd.DataFrame,columns:list):
        df = df_entrada.copy()
        df.drop(columns=columns,inplace=True)
        
        return df

    def parsear_fecha(self,df_entrada:pd.DataFrame, columna:str):
        df = df_entrada.copy()
        df[columna] = pd.to_datetime(df[columna])
        
        return df

    def renombrar_columnas(self,df_entrada:pd.DataFrame,diccionario:dict):
        df = df_entrada.copy()
        df.rename(columns=diccionario,inplace=True)
        return df
    
    def lev(self,s, t, ratio_calc = False):
        """levenshtein_ratio_and_distance:
            Calculates levenshtein distance between two strings.
            If ratio_calc = True, the function computes the
            levenshtein distance ratio of similarity between two strings
            For all i and j, distance[i,j] will contain the Levenshtein
            distance between the first i characters of s and the
            first j characters of t
        """
            # Initialize matrix of zeros
        rows = len(s)+1
        cols = len(t)+1
        distance = np.zeros((rows,cols),dtype = int)

        # Populate matrix of zeros with the indeces of each character of both strings
        for i in range(1, rows):
            for k in range(1,cols):
                distance[i][0] = i
                distance[0][k] = k

        # Iterate over the matrix to compute the cost of deletions,insertions and/or substitutions    
        for col in range(1, cols):
            for row in range(1, rows):
                if s[row-1] == t[col-1]:
                    cost = 0 # If the characters are the same in the two strings in a given position [i,j] then the cost is 0
                else:
                    # In order to align the results with those of the Python Levenshtein package, if we choose to calculate the ratio
                    # the cost of a substitution is 2. If we calculate just distance, then the cost of a substitution is 1.
                    if ratio_calc == True:
                        cost = 2
                    else:
                        cost = 1
                distance[row][col] = min(distance[row-1][col] + 1,      # Cost of deletions
                                    distance[row][col-1] + 1,          # Cost of insertions
                                    distance[row-1][col-1] + cost)     # Cost of substitutions
        if ratio_calc == True:
            # Computation of the Levenshtein Distance Ratio
            Ratio = ((len(s)+len(t)) - distance[row][col]) / (len(s)+len(t))
            return Ratio
        else:
            # print(distance) # Uncomment if you want to see the matrix showing how the algorithm computes the cost of deletions,
            # insertions and/or substitutions
            # This is the minimum number of edits needed to convert string a to string b
            return "The strings are {} edits away".format(distance[row][col])
        
    def normalizar_localidades(self, df_entrada:pd.DataFrame):

        localidades_nombres = ['Capi Fed','Capital Federal','Ciudad De Buenos Aires','Mendoza','San Carlos De Bariloche','San Miguel De Tucuman','Cordoba','Rosario'
                                ,'Mar Del Plata','La Plata','Quilmes','Avellaneda','Lanus','San Justo',
                                'Castelar','Moron','Caseros','Martinez','Vicente Lopez']
        for i in df_entrada:
            if i == "Localidad":
                for l in localidades_nombres:
                    c=0
                    cv=df_entrada[i]
                    for n in cv:
                        ratio = self.lev(n,l,ratio_calc=True)
                        if (ratio > 0.69) or (n in ["CABA","Cdad De Buenos Aires","Capital","Capital Federal"]):
                            cv[c] = l
                        else:
                            pass         
                        c = c + 1