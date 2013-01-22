import entities
import sorter
import readerN

import sys
import getopt

def main():
    #parse cmd options
        try:
            opts, args = getopt.getopt(sys.argv[1:], "h", ["help"])
        except getopt.error, msg:
            print msg
            print "for help use --help"
            sys.exit(2)
        # process options
        for o, a in opts:
            if o in ("-h", "--help"):
                print __doc__
                sys.exit(0) 

        #start
        #read data
        r = readerN.Reader('test')
        r.read()

        bus1 = entities.Bus({'route' : 43, 'seat' : 14})
        bus2 = entities.Bus({'route' : 41, 'seat' : 11})
        cards = [entities.TravelCard('london', 'oxford', bus1), 
                entities.TravelCard('minsk', 'london', bus1),
                entities.TravelCard('oxford', 'somewhere', bus1)]
        algo = sorter.Sorter()
        sortedList = algo.sort(cards)
        #for card in sortedList: 
        #    print card.message()
        

                
                        
if __name__ == "__main__":
    main()
