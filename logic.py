import sympy as sp
import random
import math
import logic_generations

my_dictionary = {}
generations = {}

def reception_of_values(initial_people, max_people, variable_a, variable_b, prob_mut_ind, prob_mut_gen, function_entry, delta_x, find_x_entry, iterator_entry):
    set_dictionary(initial_people, max_people, variable_a, variable_b, prob_mut_ind, prob_mut_gen, function_entry, delta_x, find_x_entry, iterator_entry)

def set_dictionary(initial_people, max_people, variable_a, variable_b, prob_mut_ind, prob_mut_gen, function_entry, delta_x, find_x_entry, iterator_entry):
    initial_people_value = initial_people.get()
    max_people_value = max_people.get()
    variable_a_value = variable_a.get()
    variable_b_value = variable_b.get()
    prob_mut_ind_value = prob_mut_ind.get()
    prob_mut_gen_value = prob_mut_gen.get()
    function_value = function_entry.get()
    delta_x_value = delta_x.get()
    find_x_entry_value = find_x_entry.get()
    iterator_value = iterator_entry.get()
    
    if (initial_people_value == '' or max_people_value == '' or
            variable_a_value == '' or variable_b_value == '' or
            prob_mut_ind_value == '' or
            prob_mut_gen_value == '' or function_value == '' or delta_x_value == '' or
            find_x_entry_value == '' or iterator_value == ''):
        print("Todos los campos deben ser diferentes de vacío. Por favor, complete todos los campos correctamente.")
        return
    else:
        my_dictionary["initial_people"] = initial_people_value
        my_dictionary["max_people"] = max_people_value
        my_dictionary["variable_a"] = variable_a_value
        my_dictionary["variable_b"] = variable_b_value
        my_dictionary["prob_mut_ind"] = prob_mut_ind_value
        my_dictionary["prob_mut_gen"] = prob_mut_gen_value
        my_dictionary["function_entry"] = function_value
        my_dictionary["delta_x"] = delta_x_value
        my_dictionary["find_x_by"] = find_x_entry_value
        my_dictionary["iterator_entry"] = iterator_value
        process_data()
        # print("My dictionary", my_dictionary)

def process_data():
    calculate_range(my_dictionary["variable_a"], my_dictionary["variable_b"])
    generate_base_generation()
    # print_values()

def print_values():
    print(f"""Entered Values: 
    Poblacion inicial: {my_dictionary["initial_people"] or 4}, 
    Poblacion maxima: {my_dictionary["max_people"] or 8}, 
    Punto A: {my_dictionary["variable_a"] or 3}, 
    Punto B: {my_dictionary["variable_b"] or 5},
    Prob. de mut. ind: {my_dictionary["prob_mut_ind"] or 0.25},
    Prob. de mut. gen: {my_dictionary["prob_mut_gen"] or 0.35},
    f(x): {my_dictionary["function_entry"] or "x^2"},
    Resolución: {my_dictionary["delta_x"] or 0.06},
    Encontrar (x) por: {my_dictionary["find_x_by"] or 'Minimización'},
    Iteraciones: {my_dictionary["iterator_entry"] or 10},
    """)

def calculate_range(variable_a, variable_b):
    my_dictionary["range"] = float(variable_b) - float(variable_a)
    # print("Range:", float(variable_b) - float(variable_a))

def generate_base_generation():
    generate_jumps()
    generate_points()
    generate_bits()
    a = float(my_dictionary.get("variable_a"))
    delta_x = float(my_dictionary.get("delta_x", 0.06))
    my_dictionary["delta_x"] = delta_x
    amount_of_numbers = int(my_dictionary.get("initial_people"))
    funcion_y_str = my_dictionary.get("function_entry", "x")
    try:
        funcion_y_sympy = sp.sympify(funcion_y_str)
    except sp.SympifyError:
        print("Error al convertir la función a un formato válido")
        return

    # Generar números aleatorios y convertirlos a binario
    bits_required = int(my_dictionary["bits_required"])
    max_value = 2 ** bits_required - 1  # Max value for the specified number of bits
    random_numbers = [random.randint(1, max_value) for _ in range(amount_of_numbers)]
    binary_numbers = [format(num, f"0{bits_required}b") for num in random_numbers]
    # Generar valores de x
    values_x = generate_x(a, delta_x, random_numbers)

    # Aplicar la función y a los valores de x
    values_y = apply_function_y(funcion_y_sympy, values_x)

    # Construir el diccionario final
    data = {
        "Id": list(range(1, amount_of_numbers + 1)),
        "Numbers": random_numbers,
        "Binary_numbers": binary_numbers,
        "Values_x": values_x,
        "Values_f(x)": values_y,
        "Bits_required": bits_required
    }

    # print("Data generated:", data)
    logic_generations.receive_base_generation(data, my_dictionary)

def generate_jumps():
    range_data = float(my_dictionary["range"])
    delta_x_data = float(my_dictionary["delta_x"])
    result = range_data/delta_x_data
    # print("Jump numbers:", round(result, 4))
    my_dictionary["jump_numbers"] = round(result, 4)

def generate_points():
    points_data_pre = float(my_dictionary["jump_numbers"])
    points_data = points_data_pre + 1
    # print("Point numbers:", round(points_data, 4))
    my_dictionary["points_numbers"] = round(points_data, 4)

def generate_bits():
    points_data = float(my_dictionary["points_numbers"])
    bits_required = math.ceil(math.log2(points_data))
    my_dictionary["bits_required"] = bits_required
    # print("Bits required:", bits_required)

def generate_x(a, delta_x, random_numbers):
    return [round(a + i * delta_x, 4) for i in random_numbers]

def apply_function_y(funcion_y, values_x):
    return [round(funcion_y.subs('x', x), 4) for x in values_x]
