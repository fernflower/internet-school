import readerN
import sorter
import entities


class Manager:
    def __init__(self):
        self.sortAlgo = sorter.Sorter()

    #returns a list of TravelCards
    def readFile(self, filename):
        reader = readerN.Reader(filename)
        blocks = reader.readToDictionary()
        cards = []
        for key in blocks.keys():
            card = entities.TravelCard(blocks[key])
            cards.append(card)
        return cards

    #sorts a list of TravelCards and returns textual route representation
    def getRoute(self, cardList):
        sortedCards = self.sortAlgo.sort(cardList)
        for card in sortedCards:
            print card.message()
