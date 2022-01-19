class Display:

    def __init__(self, id: int, matrix_type: str, diagonal: float):
        self.id = id
        self.matrix_type = matrix_type
        self.diagonal = diagonal

    def __str__(self):
        return "Processor with id: " + str(self.id) + "; matrix_type: " + self.matrix_type + "; diagonal: " + str(
            self.diagonal)

    def __repr__(self) -> str:
        return self.__str__()

    def values(self):
        return self.matrix_type, self.diagonal


class PC:

    def __init__(self, id: int, name: str, price: int, disp_id: int):
        self.id = id
        self.name = name
        self.price = price
        self.disp_id = disp_id

    def __str__(self):
        return "PC with id: " + str(self.id) + "; name: " + self.name + "; price: " + str(
            self.price) + "; disp_id: " + str(self.disp_id)

    def __repr__(self) -> str:
        return self.__str__()

    def values(self):
        return self.name, self.price


class PC_Display:
    def __init__(self, disp_id: int, pc_id: int):
        self.disp_id = disp_id
        self.pc_id = pc_id

    def __repr__(self) -> str:
        return self.__str__()

    def values(self):
        return self.disp_id, self.pc_id
