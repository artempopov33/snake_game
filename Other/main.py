class Building:
    minheight = 0
    maxheight = 400

    def housea(self, maxheight=0, minheight=0):
        self.__minheight = minheight
        self.__maxheight = maxheight



    def setheight(self, maxheight, minheight):
        if self.__maxheight > 0 and self.__minheight > -10:
            self.__maxheight = maxheight
            self.__minheight = minheight

    def getheight(self):
        return self.__maxheight, self.__minheight

