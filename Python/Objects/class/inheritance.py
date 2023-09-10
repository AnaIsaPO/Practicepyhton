class PartyAnimal:   # This is the template for making PartyAnimal objects
    x = 0    # Each PrtyAnimal object has a bit of data
    name = ""

    def __init__(self, z):
        self.name = z
        print(self.name, 'constructed') #Consrtructors can have additional parameters

    def party(self):    #Each PartyAnimal object has a bit of code
        self.x = self.x + 1
        print(self.name, "party count", self.x)

class FootballFan(PartyAnimal): #Footbal is a class which extends PartyAnimal. It has all the capabilities of PartyAnimal and more
    points = 0
    def touchdown(self):
        self.points = self.points + 7
        self.party()
        print(self.name, "points", self.points)

s = PartyAnimal("Sally")
s.party()

j = FootballFan("Jim")
j.party()
j.touchdown()