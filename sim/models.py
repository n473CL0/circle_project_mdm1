import matplotlib.pyplot as plt

class Circle:
    def __init__(self, x, y, diameter):
        self.x = x
        self.y = y
        self.radius = diameter / 2

    def area(self):
        return 3.14 * self.radius ** 2
    
    def draw(self):
        circle = plt.Circle((self.x, self.y), self.radius, facecolor='none', edgecolor='black')
        plt.gca().add_patch(circle)
    

class Sheet():
    def __init__(self, length, height):
        self.length = length
        self.height = height

    def area(self):
        return self.length * self.height

    def draw(self):
        rectangle = plt.Rectangle((0,0), self.length, self.height, fc='none', ec="black")
        plt.gca().add_patch(rectangle)


class System():
    def __init__(self, sheet, circles):
        self.sheet = sheet
        self.circles = circles

    def waste(self):
        total_area = self.sheet.area()
        used_area = sum([circle.area() for circle in self.circles])

        return (total_area - used_area) / total_area
    
    def count(self, d_1, d_2):
        r_1 = d_1 / 2
        r_2 = d_2 / 2
        return sum([c.radius == r_1 for c in self.circles]), sum([c.radius == r_2 for c in self.circles])

    def draw(self):
        plt.axes()
        self.sheet.draw()
        for circle in self.circles:
            circle.draw()
        plt.axis('scaled')
        plt.show()

    def draw_section(self, x_end):
        plt.axes()
        self.sheet.draw()
        for circle in self.circles:
            circle.draw()
            if circle.x - circle.radius > x_end:
                break
        plt.ylim(0,100)
        plt.show()

    def save_fig(self, filename):
        plt.axes()
        self.sheet.draw()
        for circle in self.circles:
            circle.draw()
        plt.axis('scaled')
        plt.savefig(filename)
        plt.clf()

    def save_fig_section(self, filename, x_end):
        plt.axes()
        for circle in self.circles:
            if circle.x > x_end:
                break
            circle.draw()
        plt.axis('scaled')
        plt.savefig(filename)
        plt.clf()