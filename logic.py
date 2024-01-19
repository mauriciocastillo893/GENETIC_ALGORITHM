import sympy as sp
import random
import math

my_dictionary = {}
generations = {}

def reception_of_values(initial_people, max_people, variable_a, variable_b, prob_of_crossing, prob_mut_ind, prob_mut_gen, function_entry, delta_x, iterator_entry):
    set_dictionary(initial_people, max_people, variable_a, variable_b, prob_of_crossing, prob_mut_ind, prob_mut_gen, function_entry, delta_x, iterator_entry)

def set_dictionary(initial_people, max_people, variable_a, variable_b, prob_of_crossing, prob_mut_ind, prob_mut_gen, function_entry, delta_x, iterator_entry):
    initial_people_value = initial_people.get()
    max_people_value = max_people.get()
    variable_a_value = variable_a.get()
    variable_b_value = variable_b.get()
    prob_of_crossing_value = prob_of_crossing.get()
    prob_mut_ind_value = prob_mut_ind.get()
    prob_mut_gen_value = prob_mut_gen.get()
    function_value = function_entry.get()
    delta_x_value = delta_x.get()
    iterator_value = iterator_entry.get()
    
    if (initial_people_value == '' or max_people_value == '' or
            variable_a_value == '' or variable_b_value == '' or
            prob_of_crossing_value == '' or prob_mut_ind_value == '' or
            prob_mut_gen_value == '' or function_value == '' or delta_x_value == '' or
            iterator_value == ''):
        print("Todos los campos deben ser diferentes de vacío. Por favor, complete todos los campos correctamente.")
        return
    else:
        my_dictionary["initial_people"] = initial_people_value
        my_dictionary["max_people"] = max_people_value
        my_dictionary["variable_a"] = variable_a_value
        my_dictionary["variable_b"] = variable_b_value
        my_dictionary["prob_of_crossing"] = prob_of_crossing_value
        my_dictionary["prob_mut_ind"] = prob_mut_ind_value
        my_dictionary["prob_mut_gen"] = prob_mut_gen_value
        my_dictionary["function_entry"] = function_value
        my_dictionary["delta_x"] = delta_x_value
        my_dictionary["iterator_entry"] = iterator_value
        process_data()
        print("My dictionary", my_dictionary)

def process_data():
    calculate_range(my_dictionary["variable_a"], my_dictionary["variable_b"])
    generate_first_generation()
    # print_values()

def print_values():
    print(f"""Entered Values: 
    Poblacion inicial: {my_dictionary["initial_people"] or 4}, 
    Poblacion maxima: {my_dictionary["max_people"] or 8}, 
    Punto A: {my_dictionary["variable_a"] or 3}, 
    Punto B: {my_dictionary["variable_b"] or 5},
    Prob. de cruza: {my_dictionary["prob_of_crossing"] or 0.75},
    Prob. de mut. ind: {my_dictionary["prob_mut_ind"] or 0.25},
    Prob. de mut. gen: {my_dictionary["prob_mut_gen"] or 0.35},
    f(x): {my_dictionary["function_entry"] or "x^2"},
    Resolución: {my_dictionary["delta_x"] or 0.06},
    Iteraciones: {my_dictionary["iterator_entry"] or 10},
    """)

def calculate_range(variable_a, variable_b):
    my_dictionary["range"] = float(variable_b) - float(variable_a)
    print("Range:", float(variable_b) - float(variable_a))

def generate_first_generation():
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
    numeros_aleatorios = [random.randint(1, max_value) for _ in range(amount_of_numbers)]
    numeros_binarios = [format(num, f"0{bits_required}b") for num in numeros_aleatorios]
    print("Numeros aleatorios:", numeros_aleatorios)
    # Generar valores de x
    valores_x = generar_x(a, delta_x, numeros_aleatorios)

    # Aplicar la función y a los valores de x
    valores_y = aplicar_funcion_y(funcion_y_sympy, valores_x)

    # Construir el diccionario final
    data = {
        "Id": list(range(1, amount_of_numbers + 1)),
        "Numero": numeros_aleatorios,
        "Binario": numeros_binarios,
        "X": valores_x,
        "f(x)": valores_y
    }

    print("Data generated:", data)

def generate_jumps():
    range_data = float(my_dictionary["range"])
    delta_x_data = float(my_dictionary["delta_x"])
    result = range_data/delta_x_data
    print("Jump numbers:", result)
    my_dictionary["jump_numbers"] = result

def generate_points():
    points_data_pre = float(my_dictionary["jump_numbers"])
    points_data = points_data_pre + 1
    print("Point numbers:", points_data)
    my_dictionary["points_numbers"] = points_data

def generate_bits():
    points_data = float(my_dictionary["points_numbers"])
    bits_required = math.ceil(math.log2(points_data))
    my_dictionary["bits_required"] = bits_required
    print("Bits required:", bits_required)

def generar_x(a, delta_x, cantidad):
    print("a:", a, "delta_x:", delta_x, "cantidad:", cantidad)
    return [round(a + i * delta_x, 4) for i in cantidad]

def aplicar_funcion_y(funcion_y, x_valores):
    return [round(funcion_y.subs('x', x), 4) for x in x_valores]

def evaluate_expresion(expresion, valor_x):
    x = sp.symbols('x')
    try:
        resultado = sp.sympify(expresion).subs(x, valor_x)
        print("Resultado de f(x): ", resultado)
    except (sp.SympifyError, TypeError):
        return "Error al evaluar la expresión"
