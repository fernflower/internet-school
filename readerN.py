import re
'''
Input format:
    (Would have used JSON (and standard JSON parser) if hadn't had misinterpreted 'standard library usage' as 'only sys module usage')
    
    JSON-like input with several restrictions: 
    - ('{' and '}') have to be on a separate line
    - data : value pairs are separated by newlines, not commas
    - no json-list support
    
    {
        data1 : value
        data2 : 
               {
                   data3 : value
                  
               }
    }

    Typical TransportCard description: 
    {
        from : London
        to   : Boston
        transport : 
                {
                    type : plane
                    params: 
                        { 
                            seat : "14E"
                            route : "112-K"
                            gate : A
                        }
                }
    }
'''


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
        count = 1
        result = dict()
        result['block' + `count`] = self._block()
        while (self._viewNext() is not None):
            count+=1
            result['block' + `count`] = self._block()
        return result

    #BLOCK ::= '{' BLOCK '}'
    def _block(self):
        result = None
        if (self._getNext() != '{'):
            raise Exception('Block should start with a { !')
        else:
            result = self._card()
            if (self._getNext() != '}'):
                raise Exception('Block should end with a } !')
        return result

    #CARD ::= DATA (DATA)
    def _card(self):
        result = dict()
        (key, value) = self._data()
        result[key] = value
        while (self._viewNext() != '}'):
            (key, value) = self._data()
            result[key] = value
        return result
       
    #DATA ::= KEY ':' VALUE
    def _data(self):
        key = self._getNext()
        if (self._getNext() != ':'):
            raise Exception('Colon expected!')
        else:
            result = (key, self._value())
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
