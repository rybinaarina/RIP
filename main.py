from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
import arrow


def main():
    r = Rectangle("синего", 17, 17)
    c = Circle("зеленого", 17)
    s = Square("красного", 17)

    utc_time = arrow.utcnow()
    print('Время (UTC): ',utc_time)
    print(r)
    print(c)
    print(s)

if __name__ == "__main__":
    main()
