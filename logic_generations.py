import sympy as sp
import random
import math
import pandas as pd
from Structure.generation import Generation

my_base_dictionary = {}
base_data = {}
all_generations = []

def receive_base_generation(data, my_dictionary):
    global my_base_dictionary, base_data
    print("I receive this \ndata:", data, "\ndictionaty:", my_dictionary)
    my_base_dictionary = my_dictionary
    base_data = data
    form_duos("", 0)
    create_excel()

def form_duos(data, generation_id):
    print("Data length", len(data)) # Data expect an array with elements to sort as below when "base_data" is sorted
    # temp_key_value = {}
    # for i, j in zip(base_data["Id"], base_data["Numero"]):
    #     temp_key_value[i] = j
    # print("temp_key_value:", temp_key_value)
    if(len(data) == 0):
        ordened_list = sorted(base_data["Numero"])
    else:
        ordened_list = sorted(data)
    half_length = len(ordened_list) // 2
    if(my_base_dictionary["find_x_by"] == "Minimización"):
        result = ordened_list[:half_length]
        the_rest = ordened_list[half_length:]
    else:
        result = ordened_list[half_length:]
        the_rest = ordened_list[:half_length]
    print("Betters by", my_base_dictionary["find_x_by"], ":", result)
    print("The rest by", my_base_dictionary["find_x_by"], ":", the_rest)
    generation_at_this_moment = "generation0"
    generation_by_cycle = Generation(
        generation_at_this_moment,
        numbers=[],  # Agrega listas vacías para 'numbers', 'binary', 'x', 'fx' y 'formed_couples'
        binary=[],
        x=[],
        fx=[],
        the_best_data=result,
        the_rest_data=the_rest,
        formed_couples=[],
        id_formed_couples=[]
    )
    all_generations.append(generation_by_cycle)
    print("All generations created:", all_generations)
    for generation in all_generations:
        print(generation)
def create_excel():
    # Crear un DataFrame de pandas a partir del diccionario base_data
    df = pd.DataFrame(base_data)
    
    # Crear un DataFrame adicional para my_base_dictionary
    dD_data = {
        'initial_people': [my_base_dictionary['initial_people']],
        'max_people': [my_base_dictionary['max_people']],
        'variable_a': [my_base_dictionary['variable_a']],
        'variable_b': [my_base_dictionary['variable_b']],
        'prob_of_crossing': [my_base_dictionary['prob_of_crossing']],
        'prob_mut_ind': [my_base_dictionary['prob_mut_ind']],
        'prob_mut_gen': [my_base_dictionary['prob_mut_gen']],
        'function_entry': [my_base_dictionary['function_entry']],
        'delta_x': [my_base_dictionary['delta_x']],
        'find_x_by': [my_base_dictionary['find_x_by']],
        'iterator_entry': [my_base_dictionary['iterator_entry']],
        'range': [my_base_dictionary['range']],
        'jump_numbers': [my_base_dictionary['jump_numbers']],
        'points_numbers': [my_base_dictionary['points_numbers']],
        'bits_required': [my_base_dictionary['bits_required']]
    }
    dD = pd.DataFrame(dD_data)
    
    # Especificar el nombre del archivo Excel
    excel_file = "generations.xlsx"

    # Crear un escritor Excel
    with pd.ExcelWriter(excel_file, engine='xlsxwriter') as writer:
        # Exportar el DataFrame original a la primera sección
        df[['Id', 'Numero', 'Binario', 'X', 'f(x)']].to_excel(writer, sheet_name='Sheet1', index=False)

        # Exportar el DataFrame adicional a la segunda sección
        dD.to_excel(writer, sheet_name='Sheet1', index=False, startrow=6)

        # Exportar la segunda tabla adicional a la tercera sección
        additional_data2 = {'ColX': ['a', 'b', 'c'], 'ColY': ['d', 'e', 'f']}
        additional_df2 = pd.DataFrame(additional_data2)
        additional_df2.to_excel(writer, sheet_name='Sheet1', startcol=2, startrow=12, index=False, header=['ColX', 'ColY'])

    print(f"Archivo Excel '{excel_file}' creado satisfactoriamente.")


