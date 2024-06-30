import math


class Punct:
    def __init__(self, coord_x, coord_y):
        self.x = coord_x
        self.y = coord_y

    def __str__(self):
        return str({"x=": self.x, "y=": self.y})

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        return False

    def distance(self, other)->float:
        x=(self.x-other.x)**2
        y=(self.y-other.y)**2
        distance = math.sqrt(x+y)
        return distance


class Geometric_figure(Punct):
    def __init__(self, ox, oy):
        super().__init__(ox, oy)
        self.ox = ox
        self.oy = oy

    def calc_area(self):
        pass

    def calc_perimeter(self):
        pass


class Rectangle(Geometric_figure):
    def __init__(self, ox, oy, o2x, o2y, o3x, o3y):
        super().__init__(ox, oy)
        self.ox = ox
        self.oy = oy
        self.o2x = o2x
        self.o2y = o2y
        self.o3x = o3x
        self.o3y = o3y


    def calc_area(self):
        lenght = Punct(self.ox, self. oy).distance(Punct(self.o2x, self.o2y))
        print(f"L={lenght}")
        width = Punct(self.ox, self. oy).distance(Punct(self.o3x, self.o3y))
        print(f"l={width}")
        area = lenght * width
        return area

    def calc_perimeter(self):
        lenght = Punct(self.ox, self.oy).distance(Punct(self.o2x, self.o2y))
        width = Punct(self.ox, self.oy).distance(Punct(self.o3x, self.o3y))
        perimeter = 2*(lenght+width)
        return perimeter

class Square(Rectangle):
    def __init__(self, ox, oy, o2x, o2y):
        super().__init__(ox, oy, o2x, o2y, o2x, o2y)
        self.ox = ox
        self.oy = oy
        self.o2x = o2x
        self.o2y = o2y

class Triangle(Geometric_figure):
    def __init__(self, ox, oy, o2x, o2y, o3x, o3y):
        super().__init__(ox, oy)
        self.ox = ox
        self.oy = oy
        self.o2x = o2x
        self.o2y = o2y
        self.o3x = o3x
        self.o3y = o3y

    def calc_area(self):
        l1 = Punct(self.ox, self.oy).distance(Punct(self.o2x, self.o2y))
        l2 = Punct(self.ox, self.oy).distance(Punct(self.o3x, self.o3y))
        l3 = Punct(self.o2x, self.o2y).distance(Punct(self.o3x, self.o3y))
        s = (l1+l2+l3)/2
        area = math.sqrt(s*(s-l1)*(s-l2)*(s-l3))
        return area

    def calc_perimeter(self):
        l1 = Punct(self.ox, self.oy).distance(Punct(self.o2x, self.o2y))
        l2 = Punct(self.ox, self.oy).distance(Punct(self.o3x, self.o3y))
        l3 = Punct(self.o2x, self.o2y).distance(Punct(self.o3x, self.o3y))
        perimeter = l1+l2+l3
        return perimeter

class Circle(Geometric_figure):
    def __init__(self, ox, oy, o1x, o1y):
        super().__init__(ox, oy)
        self.ox = ox
        self. oy = oy
        self. o1x = o1x
        self. o1y = o1y

    def calc_area(self):
        r = Punct(self.ox, self.oy).distance(Punct(self.o1x, self.o1y))
        area = math.pi * r * r
        return area

    def calc_perimeter(self):
        r = Punct(self.ox, self.oy).distance(Punct(self.o1x, self.o1y))
        perimeter = 2 * math.pi *r
        return perimeter




if __name__ == '__main__':
    x = Square(0,0,2,2)
    print(x.calc_area())
    print(x.calc_perimeter())
    y = Triangle(0,0,0,2,4,0)
    print(y.calc_perimeter())


#Nu stiu daca asa trebuia faacut tema, eu am construit fiecare figura geo pe baza punctelor
#In acest caz nu avea sens o clasa de triunghi dreptunghic care sa mosteneasca clasa tiunghi
#Toate merg ok pt ca le am testat, mai pot fi adaugate conditii ca punctele date sa creeze figura dorita
#exista situatia in care 2 puncte sa fie coliniare si atunci figura nu exista, dar nu am mai facut
