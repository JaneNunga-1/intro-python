class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return round(22 / 7 * (self.radius ** 2), 3)

    def perimeter(self):
        return round(2 * 22 / 7 * self.radius, 3)

    def show_details(self):
        print("Circle's perimeter", self.perimeter())
        print("Circle's area", self.area())


c1 = Circle(5)
c1.show_details()
c2 = Circle(10)
c2.show_details()

my_circles = [c1, c2]

print(my_circles[0].area())
