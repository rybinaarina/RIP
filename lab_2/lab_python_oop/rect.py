from .geom_shape import GeomShape
from .shape_color import ShapeColor


class Rect(GeomShape):
    NAME = 'Прямоугольник'

    def __init__(self, height: int, width: int, color: str):
        self._height = height
        self._width = width
        self._color = ShapeColor(color)

    def square(self) -> int:
        return self._height * self._width

    @classmethod
    def name(cls) -> str:
        return cls.NAME

    def __repr__(self):
        return f"<Shape: {self.NAME}, width: {self._width}, height: {self._height}, color: {self._color.color_ppt}, " \
               f"square: {self.square()}>"
