class PartyAnimal:
    x = 0
    
    def __init__(self):  # Constructor
        print('I am constructed')
        
    def party(self):
        self.x = self.x + 1
        print('So far', self.x)
        
    def __del__(self):  # Destructor
        print('I am destructed' , self.x)
        
an = PartyAnimal()
an.party()
an.party()
an = 42
print('an contains' , an)


class PartyAnimal2:
    x = 0
    name = ""
    def __init__(self, z):
        self.name = z
        print(self.name, "constructed")
        
    def party(self):
        self.x = self.x + 1
        print(self.name, "party count", self.x)
        
s = PartyAnimal2("Sally")
s.party()  # s instance

j = PartyAnimal2("Jim")
j.party()   # j instance
j.party()  


class FootballFan(PartyAnimal2): #FootballFan extends PartyAnimals2 
    points = 0
    def touchdown(self):
        self.points = self.points + 7
        self.party()
        print(self.name, "points", self.points)
        
k = FootballFan("Kim")
k.party()
k.touchdown()