#!/usr/bin/python

class AbstractTransport(object):
    def message(self):
        raise NotImplementedError

class TransportFactory():
    def getTransport(self, transportParams):
        if (transportParams['type'] == Bus.typeT):
            return Bus(transportParams['params'])
        elif (transportParams['type'] == Plane.typeT):
            return Plane(transportParams['params'])

class Bus(AbstractTransport):
    typeT = 'bus'
    def __init__(self, transportParams):
        self.route = transportParams['route']
        self.seat = transportParams['seat']
    def message(self):
        return 'Route %s, seat %s' %(self.route, self.seat)

class Plane(AbstractTransport):
    typeT = 'plane'
    def __init__(self, transportParams):
        self.route = transportParams['route']
        self.gate = transportParams['gate']
        self.seat = transportParams['seat']
    def message(self):
        return 'Route %s, gate %s, seat %s' %(self.route, self.gate, self.seat)

class TravelCard:
    #card is a dictionary
    def __init__(self, card):
        self.fromP = card['from']
        self.toP = card['to']
        self.transport = TransportFactory().getTransport(card['transport'])
    def message(self):
        return 'Take %s from %s to %s. %s' % (self.transport.typeT, self.fromP, self.toP, self.transport.message())
