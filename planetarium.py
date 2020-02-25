from Planet import Planet

class Planetarium(object):
    def __init__(self):
        self.create()

    def __str__(self):
        return '[' + ', '.join(str(planet) for planet in self.planet) + ']'

    def create(self):
        self.planet = []
        for i in range(4):
            for j in range(0,4):
                self.planet.append(Planet(i,j))

Planetarium.py
    
