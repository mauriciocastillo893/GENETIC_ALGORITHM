import sympy as sp
import random
import math
import pandas as pd

generations = []
my_base_dictionary = {}
base_data = {}

def receive_base_generation(data, my_dictionary):
    global my_base_dictionary, base_data
    print("I recive this \ndata:", data, "\ndictionaty:", my_dictionary)
    my_base_dictionary = my_dictionary
    base_data = data
    form_duos()
    # create_excel()

def form_duos():
    ordened_list = sorted(base_data["Numero"])
    half_length = len(ordened_list) // 2
    if(my_base_dictionary["iterator_entry"] == "Minimización"):
        result = ordened_list[:half_length]
    else:
        result = ordened_list[half_length:]
    print("Betters by", my_base_dictionary["iterator_entry"], ":", result)

def create_excel():
    # Crear un DataFrame de pandas a partir del diccionario
    df = pd.DataFrame(base_data)
    # Especificar el nombre del archivo Excel
    excel_file = "generations.xlsx"

    # Crear un escritor Excel
    with pd.ExcelWriter(excel_file, engine='xlsxwriter') as writer:
        # Exportar el DataFrame original a la primera sección
        df[['Id', 'Numero', 'Binario', 'X', 'f(x)']].to_excel(writer, sheet_name='Sheet1', index=False)

        # Exportar la primera tabla adicional a la segunda sección
        additional_data1 = {'ColA': [7, 8, 9], 'ColB': [10, 11, 12]}
        additional_df1 = pd.DataFrame(additional_data1)
        additional_df1.to_excel(writer, sheet_name='Sheet1', startcol=1, startrow=6, index=False, header=['ColA', 'ColB'])

        # Exportar la segunda tabla adicional a la tercera sección
        additional_data2 = {'ColX': ['a', 'b', 'c'], 'ColY': ['d', 'e', 'f']}
        additional_df2 = pd.DataFrame(additional_data2)
        additional_df2.to_excel(writer, sheet_name='Sheet1', startcol=2, startrow=12, index=False, header=['ColX', 'ColY'])
    print(f"Archivo Excel '{excel_file}' creado satisfactoriamente.")