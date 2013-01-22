#!/usr/bin/python

class smart_dict(dict):
    def __missing__(self, key):
        return None

class RouteError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class Sorter:
    def __init__(self):
        pass

    def _fillRouteTable(self, cardList):
        self.table = {card.fromP:None for card in cardList}
        self.objects = {card.fromP:card for card in cardList}
        start = {card.fromP:None for card in cardList}
        #fill hashtable from -> to
        for card in cardList:
            if (self.table[card.fromP] is None):
                self.table[card.fromP] = card.toP
                start[card.toP] = 0
            else:
                print 'value of ' + card.fromP + ' is: ' + `self.table[card.fromP]`
                raise RouteError('Multiple routes from ' + `self.table[card.fromP]`)
        print self.table
        #find start
        for key in self.table.keys():
            if (start[key] is None):
                self.start = key
                break

    def sort(self, cardList):
        try:
            self._fillRouteTable(cardList)
            sortedList = list()
            nextPoint = self.start
            while nextPoint in self.table:
                #endPoint can be not in dict. keys
                    sortedList.append(self.objects[nextPoint])
                    nextPoint = self.table[nextPoint]
            if (len(sortedList) != len(self.table.keys())):
                raise RouteError('Not all travel nodes are connected!')
        except RouteError as e:
            print 'An exception occured, value: ', e.value
        return sortedList

