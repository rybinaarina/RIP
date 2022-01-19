class ShapeColor:
    def __init__(self, color: str):
        self._color = color

    @property
    def color_ppt(self) -> str:
        return self._color

    @color_ppt.setter
    def color_ppt(self, val: str) -> None:
        self._color = val
