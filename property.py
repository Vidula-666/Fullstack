class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    # Getter for width
    @property
    def width(self):
        return f"{self._width:.1f}cm"

    # Getter for height
    @property
    def height(self):
        return f"{self._height:.1f}cm"

    # Setter for width
    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Width must be greater than zero")

    # Setter for height
    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("Height must be greater than zero")

    # Deleter for width
    @width.deleter
    def width(self):
        del self._width
        print("Width has been deleted")

    # Deleter for height
    @height.deleter
    def height(self):
        del self._height
        print("Height has been deleted")


# -------------------------------
# Test the class
rectangle = Rectangle(3, 4)

# Set new width and height
rectangle.width = 5
rectangle.height = 6

# Get width and height (via @property)
print("Width:", rectangle.width)   # Output: Width: 5.0cm
print("Height:", rectangle.height) # Output: Height: 6.0cm

# Delete width and height using deleter
del rectangle.width
del rectangle.height

# Try accessing again (will raise error if uncommented)
# print(rectangle.width)   # AttributeError
# print(rectangle.height)  # AttributeError
 