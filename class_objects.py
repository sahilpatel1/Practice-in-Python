class Beach:
    
    def __init__(self, location, water_color, temperature):
        #instance variables
        self.location = location
        self.water_color = water_color 
        self.temperature = temperature
        self.heat_rating = "hot" if temperature > 80 else "cool"
        self.parts = ['water', 'sand']

    def add_part(self, part):
        self.parts.append(part)

def main():
    cape_code_beach = Beach("Cape Cod", "dark blue", 70)
    cancun_beach = Beach("Cancun", "crystal blue", 90)
    cape_code_beach.add_part("rock")
    la_beach = Beach("LA","turquoise", 85)
    italy_beach = Beach("Italy", "blue", 82)
    hot_not_rocky = []
    for beach in [cape_code_beach, cancun_beach, la_beach, italy_beach]:
        print("Beach ", beach.location, " temperature : ", beach.temperature, " which is ", beach.heat_rating)
        if("rock" in beach.parts):
            print("Item rock is included in this ", beach.location)
    for beach in [cape_code_beach, cancun_beach, la_beach, italy_beach]:
        if(beach.heat_rating == "hot" and "rock" not in beach.parts):
            hot_not_rocky.append(beach)

    return hot_not_rocky


if __name__ == "__main__":
    beaches = main()
    print([beach.location for beach in beaches])