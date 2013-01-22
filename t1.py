import sys
import getopt

import manager


def main():
    filename = 'test'
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
        elif o in ("-f", "--file"):
            filename = a
            print filename
            

    #start
    m = manager.Manager()
    cards = m.readFile(filename)
    m.getRoute(cards)
            
                        
if __name__ == "__main__":
    main()
