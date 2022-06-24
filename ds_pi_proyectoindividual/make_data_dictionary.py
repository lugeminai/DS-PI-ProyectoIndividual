
import pandas as pd
class create_datadic:
    # clase que brinda las funciones para crear un diccionario de dataos a un dataset
    def __init__(self):
        return None
    
    def make_my_data_dictionary(self, df):
            ''''''
            col_ = df.columns
            df_DataDict = {}

            for col in col_:
                    df_DataDict[col] = {
                                'Tipo de Dato': str(df.dtypes[col]),
                                'Length': len(df[col]),
                                'Cantidad de nulos': sum(df[col].isna()),
                                'Size(Memory)': df.memory_usage()[col],
                                'Definicion': str('')
                                    }

            df_DD = pd.DataFrame(df_DataDict)

            return df_DD

    def define_data_meaning(self, df_data_dictionary):
        '''Proporcione rápidamente información sobre el significado de cada columna y transpóngala a un diccionario utilizable'''

        col_ = df_data_dictionary.columns
        d = 'Definition'

        for col in col_:
            df_data_dictionary[col][d] = input('Proporciona una definicion de dato para: {}'.format(col))

        df_data_dictionary = df_data_dictionary.transpose()

        return df_data_dictionary

    def update_dd_definition(self, df_data_dictionary, attribute):
        try:
            df_dd = df_data_dictionary.transpose()
            df_dd[attribute]['Definition'] = input('Proporciona una definicion de dato para: {}'.format(attribute))
            df_dd = df_dd.transpose()
            return df_dd
        except:
            print('Lo sentimos, existe un error. Revisa la definicion del dato y vuelve a intentar')
