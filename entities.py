#!/usr/bin/python

class AbstractTransport(object):
    def message(self):
        raise NotImplementedError

class Bus(AbstractTransport):
    typeT = 'bus'
#transportParams is a dictionary
    def __init__(self, transportParams):
        self.transportParams = transportParams
    def message(self):
        return 'Route %s, seat %s' %(self.transportParams['route'], self.transportParams['seat'])

class TravelCard:
    def __init__(self, fromP, toP, transport):
        self.fromP = fromP
        self.toP = toP
        self.transport = transport
    def message(self):
        return 'Take %s from %s to %s. %s' % (self.transport.typeT, self.fromP, self.toP, self.transport.message())
