
# create civ class to hold game info 

class Civ():

    # starting max values
    MAX_POP = 100
    MAX_FOOD = 100
    MAX_WOOD = 100
    MAX_CLAY = 100
    MAX_STONE = 100
    MAX_GOLD = 100
    MAX_GEMS = 100

    # starting values
    STARTING_POP = 5
    STARTING_FOOD = 10
    STARTING_WOOD = 0
    STARTING_CLAY = 0
    STARTING_STONE = 0
    STARTING_GOLD = 0
    STARTING_GEMS = 0

    def __init__(self):

        self.pop = Civ.STARTING_POP
        self.food = Civ.STARTING_FOOD
        self.wood = Civ.STARTING_WOOD
        self.clay = Civ.STARTING_CLAY
        self.stone = Civ.STARTING_STONE
        self.gold = Civ.STARTING_GOLD
        self.gems = Civ.STARTING_GEMS

    def change_pop(self, change):

        self.pop += change

        if self.pop > Civ.MAX_POP:

            self.pop = Civ.MAX_POP

        return self.pop

    def change_food(self, change):

        self.food += change

        if self.food > Civ.MAX_FOOD:

            self.food = Civ.MAX_FOOD

        return self.food

    def change_wood(self, change):

        self.wood += change

        if self.wood > Civ.MAX_WOOD:

            self.wood = Civ.MAX_WOOD

        return self.wood

    def change_clay(self, change):

        self.clay += change

        if self.clay > Civ.MAX_CLAY:

            self.clay = Civ.MAX_CLAY

        return self.clay

    def change_stone(self, change):

        self.stone += change

        if self.stone > Civ.MAX_STONE:

            self.stone = Civ.MAX_STONE

        return self.stone

    def change_gold(self, change):

        self.pop += change

        if self.pop > Civ.MAX_POP:

            self.pop = Civ.MAX_POP

        return self.pop

    def change_gems(self, change):

        self.pop += change

        if self.pop > Civ.MAX_POP:

            self.pop = Civ.MAX_POP

        return self.pop

civ1 = Civ()

print("starting pop:", civ1.pop)

civ1.change_pop(25)

print("Changed pop:", civ1.pop)

civ1.change_pop(250000000)

print("Changed pop at max:", civ1.pop)