class Pixel:
    """
    _x - x coordinate
    _y - y coordinate
    _red - a value between 0 and 255
    _green - a value between 0 and 255
    _blue - a value between 0 and 255
    """
    def __init__(self, _x=0, _y=0, _red=0, _green=0, _blue=0):
        self._x = _x
        self._y = _y
        self._red = _red
        self._green = _green
        self._blue = _blue

    def set_coords(self, x, y):
        self._x = x
        self._y = y

    def set_grayscale(self):
        gray = int((self._red + self._green + self._blue) / 3)
        self._red = gray
        self._green = gray
        self._blue = gray

    def print_pixel_info(self):
        print(f"X: {self._x}, Y: {self._y}, Color: ({self._red}, {self._green}, {self._blue})", end="")
        if self._red == 0 and self._green == 0 and self._blue > 50:
            print(" Blue")
        if self._red == 0 and self._blue == 0 and self._green > 50:
            print(" Green")
        if self._blue == 0 and self._green == 0 and self._red > 50:
            print(" Red")


def main():
    my_pixel = Pixel(5, 6, 250)
    my_pixel.print_pixel_info()
    my_pixel.set_grayscale()
    my_pixel.print_pixel_info()


if __name__ == '__main__':
    main()
