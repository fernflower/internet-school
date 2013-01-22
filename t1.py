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
        blocks = r.readToDictionary()
        print repr(blocks)
        cards = []

        for key in blocks.keys():
            card = entities.TravelCard(blocks[key])
            cards.append(card)
            print card.message()
            

        

                
                        
if __name__ == "__main__":
    main()
