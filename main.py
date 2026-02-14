import matplotlib.pyplot as plt

class Figure:
    def __init__(self, color):
        self.color = color

class Quadrilateral(Figure):
    def __init__(self, width, height, color):
        super().__init__(color)
        self.width = width
        self.height = height

class Circle(Figure):
    def __init__(self, radius, color):
        super().__init__(color)
        self.radius = radius
    
    def increase_radius(self, r):
        self.radius + r
        return self.radius
    
    def draw_circle(self):
        plt.gca().add_patch(plt.Circle((0,0), radius=self.radius, fc=self.color))
        plt.axis('scaled')
        plt.show()

class Rectangle(Quadrilateral):
    def __init__(self, width, height, color):
        super().__init__(width=width, height=height, color=color)
    
    def draw_rectangle(self):
        plt.gca().add_patch(plt.Rectangle((0,0), width=self.width, height=self.height, fc=self.color))
        plt.axis('scaled')
        plt.show()
    

   
import matplotlib
matplotlib.use('TkAgg')
myCircle = Circle(10, 'red')
myCircle.draw_circle()

mySquare = Rectangle(10,10, 'blue')
mySquare.draw_rectangle()