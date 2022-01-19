from .rect import Rect


class Square(Rect):
    NAME = 'Квадрат'

    def __init__(self, side: int, color: str):
        super().__init__(side, side, color)
        self._side = side

    @classmethod
    def name(cls) -> str:
        return cls.NAME

    def __repr__(self):
        return f"<Shape: {self.NAME}, side: {self._side}, color: {self._color.color_ppt}, square: {self.square()}>"
