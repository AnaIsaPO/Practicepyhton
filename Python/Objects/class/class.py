class PartyAnimal:   # This is the template for making Party Animal objects
    x = 0    # Each PrtyAnimal object has a bit of data

    def __init__(self):
        print('I am constructed')

    def party(self):    #Each PartyAnimal object has a bit of code
        self.x = self.x + 1
        print("So far", self.x)

    def __delattr__(self):
        print('I am destructed', self.x)

an = PartyAnimal() # Construct a PartyAnimal object and store in "an" variable

# Tell the "an" object to run the party() code within it
an.party()  # <- PartyAnimal.party(an)
an.party()
an.party()

an = 42
print('an contains', an)

print("Type", type(an))
print("Dir", dir(an))
