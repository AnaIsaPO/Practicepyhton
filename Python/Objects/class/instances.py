#Two independet instances

class PartyAnimal:   # This is the template for making Party Animal objects
    x = 0    # Each PrtyAnimal object has a bit of data
    name = ""

    def __init__(self, z):
        self.name = z
        print(self.name, 'constructed') #Consrtructors can have additional parameters

    def party(self):    #Each PartyAnimal object has a bit of code
        self.x = self.x + 1
        print(self.name, "party count", self.x)


s = PartyAnimal("Sally") # Construct a PartyAnimal object and store in variable

# Tell the "an" object to run the party() code within it
s.party()  # <- PartyAnimal.party(an)

j = PartyAnimal("Jim")
j.party()
s.party()
