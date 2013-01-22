import re

class Reader:
    def __init__(self, filename):
        self.f = open(filename, 'r')
        self.words = self._tokenize(self.f.readlines())
        self.i = iter(self.words)
        self.currWord = None
        self.nextWord = self.i.next()

    def _tokenize(self, inputLines):
        result = []
        for line in inputLines:
            s = map (lambda x: x.strip(), re.split('(:)', line))
            result.extend(s)
        return [x for x in result if x != '']

    def _getNext(self):
        try:
            if (self.i is not None):
                self.currWord = self.nextWord
                self.nextWord = self.i.next()
        except StopIteration:
            print "NO MORE!"
            self.nextWord = None
            self.i = None
            return self.currWord
        return self.currWord

    def _viewNext(self):
        if (self.i is None):
            return None
        return self.nextWord
    
    #BLOCKS ::= BLOCK (BLOCK)
    def _blocks(self):
        print "enter blocks"
        count = 1
        result = dict()
        result['block' + `count`] = self._block()
        while (self._viewNext() is not None):
            count+=1
            result['block' + `count`] = self._block()
        print "exit blocks"
        return result

    #BLOCK ::= '{' BLOCK '}'
    def _block(self):
        print "enter block"
        result = None
        if (self._getNext() != '{'):
            raise Exception('Block should start with a { !')
        else:
            result = self._card()
            if (self._getNext() != '}'):
                raise Exception('Block should end with a } !')
        print "exit block : " + repr(result)
        return result

    #CARD ::= DATA (DATA)
    def _card(self):
        print "enter card"
        result = dict()
        (key, value) = self._data()
        result[key] = value
        #result.append(self._data())
        while (self._viewNext() != '}'):
            (key, value) = self._data()
            result[key] = value
            #result.append(self._data())
        print "exit card: " + repr(result)
        return result
       
    #DATA ::= KEY ':' VALUE
    def _data(self):
        print "enter data"
        key = self._getNext()
        if (self._getNext() != ':'):
            raise Exception('Colon expected!')
        else:
            result = (key, self._value())
            print "exit data: " + repr(result)
            return result
           
    #VALUE ::= string | BLOCK
    def _value(self):
        if (self._viewNext() == '{'):
            #another block
            return self._block()
        else:
            return self._getNext()

    def readToDictionary(self):
        try:
            result = self._blocks()
            return result
        except Exception as e: 
            print "Exception occured : " + e
