class Points():
    x=1; y=2
    def setCoords(self):
        print(self.__dict__)

pt = Points()
pt.x = 5
pt.y = 10
pt.setCoords()