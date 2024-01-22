import sympy as sp
import random
import math
import pandas as pd
from itertools import product
from Structure.generation import Generation

my_base_dictionary = {}
base_data = {}
all_generations = []
actual_generation = "generation"
number_of_generation = 0

def receive_base_generation(data, my_dictionary):
    global my_base_dictionary, base_data
    # print("I receive this \ndata:", data, "\ndictionaty:", my_dictionary)
    my_base_dictionary = my_dictionary
    base_data = data
    form_duos("")
    create_excel()

def form_duos(data):
    print("Data length", len(data)) # Data expect an array with elements to sort as below when "base_data" is sorted
    if(len(data) == 0):
        ordened_list = sorted(base_data["Numbers"])
    else:
        ordened_list = sorted(data)
    half_length = len(ordened_list) // 2
    if(my_base_dictionary["find_x_by"] == "Minimización"):
        result = ordened_list[:half_length]
        the_rest = ordened_list[half_length:]
    else:
        result = ordened_list[half_length:]
        the_rest = ordened_list[:half_length]
    # Combinar "Better" con "The rest"
    combinations = list(product(result, the_rest))
    probabilities = [round(random.uniform(0.00, 1.00), 2) for _ in combinations]
    # Bits requeridos
    bits_required = base_data.get("Bits_required", 0)  # Puedes ajustar el valor predeterminado según sea necesario

    # Convertir números a binario con padding de ceros a la izquierda
    binary_combinations = [
        (bin(a)[2:].zfill(bits_required), bin(b)[2:].zfill(bits_required))
        for a, b in combinations
    ]
    combinations_with_probabilities = probabilities
    # combinations_with_probabilities = list(zip(probabilities, probabilities[::-1]))
    generation_at_this_moment = actual_generation+str(number_of_generation)
    generation_by_cycle = Generation(
        generation_at_this_moment,
        numbers=base_data["Numbers"],  # Agrega listas vacías para 'numbers', 'binary', 'x', 'fx' y 'formed_couples'
        binary=base_data["Binary_numbers"],
        bits_required=base_data["Bits_required"],
        x=base_data["Values_x"],
        fx=base_data["Values_f(x)"],
        the_best_data=result,
        the_rest_data=the_rest,
        formed_couples=combinations,
        chance_of_mutating=combinations_with_probabilities,
        binary_formed_couples=binary_combinations,
    )
    all_generations.append(generation_by_cycle)

    # print("All generations created:", all_generations)
    for generation in all_generations:
        print(generation)
    # I ADDED THIS, VERIFY
    combinations_with_probabilities = list(zip(probabilities, probabilities[::-1]))

    crossing(binary_combinations, combinations_with_probabilities)

def crossing(binary_combinations, combinations_with_probabilities):
    # Resultados de la cruza
    binary_combinations_crossed = []

    for i, (binary_pair, probabilities) in enumerate(zip(binary_combinations, combinations_with_probabilities)):
        print(f"\n--- Cruza para el par {i + 1} ---")

        # Realizar la cruza sin restricciones de probabilidad

        # Realizar la cruza
        num_crossover_points = random.randint(1, len(binary_pair[0]) - 1)
        crossover_points = random.sample(range(len(binary_pair[0])), num_crossover_points)
        crossover_points.sort()

        print(f"Puntos de Cruza: {crossover_points}")

        child1_binary = ''
        child2_binary = ''
        previous_crossover_point = 0

        for point in crossover_points:
            child1_binary += binary_pair[0][previous_crossover_point:point]
            child2_binary += binary_pair[1][previous_crossover_point:point]
            previous_crossover_point = point

        # Completar con el resto de los bits
        child1_binary += binary_pair[1][previous_crossover_point:]
        child2_binary += binary_pair[0][previous_crossover_point:]

        # Agregar a la lista de resultados
        binary_combinations_crossed.append((child1_binary, child2_binary))

        # Imprimir información sobre los hijos generados
        print(f"Hijos generados:")
        print(f"Child 1 Binary: {child1_binary}")
        print(f"Child 2 Binary: {child2_binary}")

    # Mostrar resultados finales
    print("\n--- Resultados finales ---")
    print("Original Binary Combinations:", binary_combinations)
    print("Binary Combinations Crossed:", binary_combinations_crossed)
    mutate(binary_combinations_crossed, [prob[0] for prob in combinations_with_probabilities])

def mutate(binary_combinations_crossed, combinations_with_probabilities):
    binary_combinations_mutated = []

    # Paso 1: Obtener los elementos de binary_combinations_crossed
    for i, (binary_crossed, probabilities) in enumerate(zip(binary_combinations_crossed, combinations_with_probabilities)):
        print(f"\n--- Mutación para el elemento {i + 1} ---")

        # Paso 2: Obtener las probabilidades de combinations_with_probabilities
        prob_mut_ind = random.uniform(0.0, 1.0)
        
        # Paso 3: Comprobación de prob_mut_ind <= my_base_dictionary["prob_mut_ind"]
        if prob_mut_ind <= combinations_with_probabilities[0]:  # Acceder al primer elemento de la tupla
            print("El elemento va a mutar.")
            mutated_binary = ''

            # Paso 4: Obtener la probabilidad de cada número del binario
            for bit in binary_crossed:
                prob_mut_bit = round(random.uniform(0.0, 1.0), 2)

                # Paso 5: Comparar prob_mut_bit <= my_base_dictionary["prob_mut_gen"]
                mutated_bit = '1' if prob_mut_bit <= probabilities[1] else '0'  # Acceder al segundo elemento de la tupla

                mutated_binary += mutated_bit

            print(f"Original Binary: {binary_crossed}")
            print(f"Mutated Binary: {mutated_binary}")
            binary_combinations_mutated.append(mutated_binary)
        else:
            # Si no muta, agregar el binario original a la lista resultante
            print("El elemento no muta.")
            binary_combinations_mutated.append(binary_crossed)

    print("\n--- Resultados finales ---")
    print("Binary Combinations Crossed:", binary_combinations_crossed)
    print("Binary Combinations Mutated:", binary_combinations_mutated)




def create_excel():
    # Crear un DataFrame de pandas a partir del diccionario base_data
    df = pd.DataFrame(base_data)
    
    # Crear un DataFrame adicional para my_base_dictionary
    dD_data = {
        'initial_people': [my_base_dictionary['initial_people']],
        'max_people': [my_base_dictionary['max_people']],
        'variable_a': [my_base_dictionary['variable_a']],
        'variable_b': [my_base_dictionary['variable_b']],
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
        df[['Id', 'Numbers', 'Binary_numbers', 'Values_x', 'Values_f(x)']].to_excel(writer, sheet_name='Sheet1', index=False)

        # Exportar el DataFrame adicional a la segunda sección
        dD.to_excel(writer, sheet_name='Sheet1', index=False, startrow=6)

        # Exportar la segunda tabla adicional a la tercera sección
        additional_data2 = {'ColX': ['a', 'b', 'c'], 'ColY': ['d', 'e', 'f']}
        additional_df2 = pd.DataFrame(additional_data2)
        additional_df2.to_excel(writer, sheet_name='Sheet1', startcol=2, startrow=12, index=False, header=['ColX', 'ColY'])

    print(f"Archivo Excel '{excel_file}' creado satisfactoriamente.")


