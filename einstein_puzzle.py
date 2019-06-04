""" Program to find the answer for the Einstein's IQ Puzzle, as it is called
    By João Ricardo de Souza, June 3rd 2019 """

import itertools


class House:
    """ Create the House Class """
    def __init__(self, position):
        self.position = position
        self.color = None
        self.nationality = None
        self.drink = None
        self.cigar = None
        self.animal = None

    def get_info(self):
        return [
            self.color,
            self.nationality,
            self.drink,
            self.cigar,
            self.animal
        ]


""" Create the 15 conditions """


def condition_1(houselist):
    """ The norwegian lives in the first house """
    for i in range(5):
        if houselist[i].position == 1 and houselist[i].nationality == 'norwegian':
            return True
    return False


def condition_2(houselist):
    """ The english lives in the red house """
    for i in range(5):
        if houselist[i].nationality == 'english' and houselist[i].color == 'red':
            return True
    return False


def condition_3(houselist):
    """ The swedish has dogs """
    for i in range(5):
        if houselist[i].nationality == 'swedish' and houselist[i].animal == 'dog':
            return True
    return False


def condition_4(houselist):
    """ The danish drinks tea """
    for i in range(5):
        if houselist[i].nationality == 'danish' and houselist[i].drink == 'tea':
            return True
    return False


def condition_5(houselist):
    """ The green house is at the left of the white house """
    for i in range(5):
        try:
            if ((houselist[i].color == 'green' and houselist[i+1].color == 'white') or
                    (houselist[i].color == 'white' and houselist[i+1].color == 'green')):
                return True
        except IndexError:
            continue
    return False


def condition_6(houselist):
    """ The man who lives in the green house drinks coffee """
    for i in range(5):
        if houselist[i].color == 'green' and houselist[i].drink == 'coffee':
            return True
    return False


def condition_7(houselist):
    """ The man who smokes Pall Mall has a bird """
    for i in range(5):
        if houselist[i].cigar == 'pall mall' and houselist[i].animal == 'bird':
            return True
    return False


def condition_8(houselist):
    """ The man who lives in the yellow house smokes Dunhill """
    for i in range(5):
        if houselist[i].color == 'yellow' and houselist[i].cigar == 'dunhill':
            return True
    return False


def condition_9(houselist):
    """ The man who lives in the house of the middle drinks milk """
    for i in range(5):
        if houselist[i].position == 3 and houselist[i].drink == 'milk':
            return True
    return False


def condition_10(houselist):
    """ The man who smokes Blends is a neighbour of the man who has a cat """
    for i in range(5):
        try:
            if ((houselist[i].cigar == 'blends' and (houselist[i+1].animal == 'cat' or houselist[i-1].animal == 'cat'))
                    or (houselist[i].animal == 'cat' and (houselist[i+1].cigar == 'blends' or
                                                          houselist[i-1].cigar == 'blends'))):
                return True
        except IndexError:
            continue
    return False


def condition_11(houselist):
    """ The man who has a horse is a neighbour of the man who smokes Dunhill """
    for i in range(5):
        try:
            if ((houselist[i].cigar == 'dunhill' and (houselist[i+1].animal == 'horse' or
                                                      houselist[i-1].animal == 'horse')) or
                    (houselist[i].animal == 'horse' and (houselist[i+1].cigar == 'dunhill' or
                                                         houselist[i-1].cigar == 'dunhill'))):
                return True
        except IndexError:
            continue
    return False


def condition_12(houselist):
    """ The man who smokes BlueMaster drinks beer """
    for i in range(5):
        if houselist[i].cigar == 'bluemaster' and houselist[i].drink == 'beer':
            return True
    return False


def condition_13(houselist):
    """ The german smokes Prince """
    for i in range(5):
        if houselist[i].nationality == 'german' and houselist[i].cigar == 'prince':
            return True
    return False


def condition_14(houselist):
    """ The norwegian is a neighbour of the blue house """
    for i in range(5):
        try:
            if ((houselist[i].nationality == 'norwegian' and (houselist[i+1].color == 'blue' or
                                                              houselist[i-1].color == 'blue')) or
                    (houselist[i].color == 'blue' and (houselist[i+1].nationality == 'norwegian' or
                                                       houselist[i-1].nationality == 'norwegian'))):
                return True
        except IndexError:
            continue
    return False


def condition_15(houselist):
    """ The man who smokes Blends is a neighbour of the man who drinks water """
    for i in range(5):
        try:
            if ((houselist[i].cigar == 'blends' and (houselist[i+1].drink == 'water' or
                                                     houselist[i-1].drink == 'water')) or
                    (houselist[i].drink == 'water' and (houselist[i+1].cigar == 'blends' or
                                                        houselist[i-1].cigar == 'blends'))):
                return True
        except IndexError:
            continue
    return False


def check_conditions(ls):
    """ Check if all the conditions are True """
    if (
        condition_1(ls) and
        condition_2(ls) and
        condition_3(ls) and
        condition_4(ls) and
        condition_5(ls) and
        condition_6(ls) and
        condition_7(ls) and
        condition_8(ls) and
        condition_9(ls) and
        condition_10(ls) and
        condition_11(ls) and
        condition_12(ls) and
        condition_13(ls) and
        condition_14(ls) and
        condition_15(ls)
    ):
        return True
    else:
        return False


def houses_get_info(ls):
    """ Create a list with all the house's informations """
    informations = []
    for house in ls:
        informations.append(house.get_info())
    return informations


""" Create variables for all attributes containing all possibilities """
colors = ['yellow', 'red', 'blue', 'white', 'green']
nationalities = ['german', 'norwegian', 'swedish', 'danish', 'english']
drinks = ['water', 'milk', 'tea', 'beer', 'coffee']
cigars = ['dunhill', 'bluemaster', 'prince', 'pall mall', 'blends']
animals = ['dog', 'cat', 'bird', 'horse', 'fish']


""" Instantiate the 5 houses and join them in an iterable list """
house1 = House(1)
house2 = House(2)
house3 = House(3)
house4 = House(4)
house5 = House(5)
houses_list = [house1, house2, house3, house4, house5]

# This might be it, but it will take 6.9 hours to make approximately 24883200000 iterations...
# So I guess I will never know =)

success = []
iterations = 0

""" Iterate through all permutations possible and find the sequence for which all conditions are True """
for colors_list in itertools.permutations(colors, 5):
    for t in range(5):
        houses_list[t].color = colors_list[t]
    for nationalities_list in itertools.permutations(nationalities, 5):
        for u in range(5):
            houses_list[u].nationality = nationalities_list[u]
        for drinks_list in itertools.permutations(drinks, 5):
            for v in range(5):
                houses_list[v].drink = drinks_list[v]
            for cigars_list in itertools.permutations(cigars, 5):
                for w in range(5):
                    houses_list[w].cigar = cigars_list[w]
                for animals_list in itertools.permutations(animals, 5):
                    for x in range(5):
                        houses_list[x].animal = animals_list[x]
                    if check_conditions(houses_list):
                        success.append(houses_get_info(houses_list))
                    # Count the iterations for visualization purposes
                    iterations += 1
                    print(iterations)

print(len(success))
for answer in success:
    print(answer)

# CORRECT ANSWERS:

# house1.color = 'yellow'
# house1.nationality = 'norwegian'
# house1.drink = 'water'
# house1.cigar = 'dunhill'
# house1.animal = 'cat'
#
# house2.color = 'blue'
# house2.nationality = 'danish'
# house2.drink = 'tea'
# house2.cigar = 'blends'
# house2.animal = 'horse'
#
# house3.color = 'red'
# house3.nationality = 'english'
# house3.drink = 'milk'
# house3.cigar = 'pall mall'
# house3.animal = 'bird'
#
# house4.color = 'green'
# house4.nationality = 'german'
# house4.drink = 'coffee'
# house4.cigar = 'prince'
# house4.animal = 'fish'
#
# house5.color = 'white'
# house5.nationality = 'swedish'
# house5.drink = 'beer'
# house5.cigar = 'bluemaster'
# house5.animal = 'dog'
#
# print(check_conditions(houses_list))
