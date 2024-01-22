class Generation:
    all_generations = []

    def __init__(self, id, numbers, binary, bits_required, x, fx, the_best_data, the_rest_data, formed_couples, chance_of_mutating, binary_formed_couples):
        self.id = id
        self.data = {
            "Numbers": numbers,
            "Binary Numbers": binary,
            "Bits Required": bits_required,
            "X": x,
            "f(x)": fx,
            "Betters": the_best_data,
            "The rest": the_rest_data,
            "Formed couples": formed_couples,
            "Chance of mutating": chance_of_mutating,
            "Binary of formed couples": binary_formed_couples,
        }


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

    def getID(self):
        return self.id
    
    def getData(self):
        return self.data