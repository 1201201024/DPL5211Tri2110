def triangle(width, length):
    tri = width * length / 2
    return tri


def rectangle(width, length):
    rect = width * length
    return rect


def main():
    i = 0
    while(i < 2):
        width = float(input("Enter width  : "))
        length = float(input("Enter length : "))
        rect = rectangle(width, length)
        tri = triangle(width, length)
        print("Rectangle area : {:.2f}".format(rect))
        print("Triangle area  : {:.2f}".format(tri))
        i += 1


main()