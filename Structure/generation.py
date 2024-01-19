class Generation:
    def __init__(self, id, numbers, binary, x, fx, formed_couples):
        self.id = id
        self.data = {
            "Id": numbers,
            "Numbers": numbers,
            "Binary": binary,
            "X": x,
            "f(x)": fx,
            "Formed couples": formed_couples,
        }