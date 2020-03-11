class Point() :
    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def __init__(self,initx,inity):
        self.x = initx
        self.y = inity


if __name__ == '__main__':
    point1 = Point(10,20)
    point2 = Point(15,25)

    print(point1.getX())
    print(point1.getY())

    point1.x = 5
    point2.x = 10

    print(point1.getX())
    print(point2.getX())
