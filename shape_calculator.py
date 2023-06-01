class Rectangle:

    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
        pass

    def __str__(self) -> str:
        return "Rectangle(width={}, height={})".format(self.width, self.height)
    
    def set_width(self, width) -> int:
        self.width = width
        pass

    def set_height(self, height) -> int:
        self.height = height
        pass

    def get_area(self) -> int:
        return self.width * self.height  

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5
    
    def get_picture(self) -> str:
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        
        picture = ''
        i = 0
        while i < self.height:
            j = 0
            while j < self.width:
                picture = picture + '*'
                j +=1
            picture = picture + '\n'
            i += 1
        return picture
    
    def get_amount_inside(self, shape) -> int:
        return (self.width//shape.width) * (self.height//shape.height)
    

class Square(Rectangle):
    
    def __init__(self, side) -> None:
        super().__init__(side, side)

    def __str__(self) -> str:
        return "Square(side={})".format(self.width)
    
    def set_side(self, side):
        super().set_width(side)
        super().set_height(side)

# rect = Rectangle(10, 5)
# print(rect.get_area())
# rect.set_height(3)
# print(rect.get_perimeter())
# print(rect)
# print(rect.get_picture())

# sq = Square(9)
# print(sq.get_area())
# sq.set_side(4)
# print(sq.get_diagonal())
# print(sq)
# print(sq.get_picture())

# rect.set_height(8)
# rect.set_width(16)
# print(rect.get_amount_inside(sq))