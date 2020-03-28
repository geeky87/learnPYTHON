class Point() :

    classvar = '$'

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def __init__(self,initx,inity):
        self.x = initx
        self.y = inity

    def __str__(self):
        return 'Point({},{})'.format(self.getX(),self.getY())

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def sort_priority(self):
        return self.x

class SmallPoint(Point) :



if __name__ == '__main__':
    point1 = Point(10,20)
    point2 = Point(15,25)

    print(point1.getX())
    print(point1.getY())

    point1.x = 5
    point2.x = 10

    print(point1.getX())
    print(point2.getX())

    print(point1)
    print(point1 + point2)
    print(point1 - point2)

    pointList = [point1,point2]
    print(sorted(pointList,key=lambda x: x.sort_priority()))

    print(Point.classvar)
    print(point1.classvar)
