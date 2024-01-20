class Generation:
    all_generations = []

    def __init__(self, id, numbers, binary, x, fx, the_best_data, the_rest_data, formed_couples, id_formed_couples):
        self.id = id
        self.data = {
            "Id": numbers,
            "Numbers": numbers,
            "Binary": binary,
            "X": x,
            "f(x)": fx,
            "Betters": the_best_data,
            "The rest": the_rest_data,
            "Formed couples": formed_couples,
            "Id of formed couples": id_formed_couples,
        }
        all_generations.append(generation_by_cycle)


    def __str__(self):
        return f"ID: {self.id}, Data: {self.data}"
        return f"Generation {self.id}: Betters={self.data['Betters']}, The rest={self.data['The rest']}, Formed couples={self.data['Formed couples']}, Id of formed couples={self.data['Id of formed couples']}"

    def add_number(self, new_number):
        self.data["Numbers"].append(new_number)

    def add_binary(self, new_binary):
        self.data["Binary"].append(new_binary)

    def add_x(self, new_x):
        self.data["X"].append(new_x)

    def add_formed_couple(self, new_value):
        self.data["Formed couples"].append(new_value)