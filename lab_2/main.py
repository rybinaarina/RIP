import numpy as np

from lab_python_oop.circle import Circle
from lab_python_oop.rect import Rect
from lab_python_oop.square import Square

N = 3


def main():
    print(Rect(N, N, 'blue'))
    print(Circle(N, 'green'))
    print(Square(N, 'red'))
    print(np.empty(N))


if __name__ == '__main__':
    main()
