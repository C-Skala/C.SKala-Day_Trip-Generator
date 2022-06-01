print("Hello and welcome to the wonderful world of pokemon, lets get you all set up for a fantastic journey!")

import random
places_to_visit = ["Kanto", "Jhoto", "Hoenn", "Sinnoh", "Galar"]

def region_picker(): # will pick the overall region to set the whole trip
    location_picked = False
    poke_places = random.choice(places_to_visit)
    travel_location = input('Would you like to visit the region of ' + f'{poke_places}? ' + 'Please select y/n ')
    if travel_location == 'y':
        location_picked = True
        return poke_places
    while location_picked == False:
        poke_places = random.choice(places_to_visit)
        travel_location = input('I get it, that region is not for everyone. What about ' + f'{poke_places}? ' + 'Please select y/n ')
        if travel_location == 'y':
            location_picked = True
            
            return poke_places

picked_region = region_picker()
print(picked_region)
print('Thats a great region, lets figure out the details now!')

Kanto_food = ['cubones home cooking', 'magmars BBQ', 'the snotlax buffet', 'tangelas stir fry']
Kanto_transport = ['fly by dragonite', 'teleport with abra', 'swim with lapras', 'tunnel with diglet']
kanto_entertainment = ['meet professor oak and pick a starter pokemon', 'win some cash at celedon game center', 'battle the elite four', 'catch some pokemon in the safati zone']

Jhoto_food = ['miltanks ice cream', 'shuckles seafood', 'steelixs kabobs', 'bellosems vegan specials']
Jhoto_transport = ['fly on noctowl', 'swim on Feraligatr', 'teleport with stantler', 'ride on raikou']
Jhoto_entertainment = ['pick a starter with professor elm', 'battle the elite four', 'catch a shiny red Gyrados', 'catch the unknown alphabet']

Hoenn_food = ['Ludicolos cantina', 'Crawdaunts crawfish boil', 'Spindas bar and grill', 'Hariyamas sushi hut' ]
Hoenn_transport = ['teleport with Gardevoir', 'fly with Flygon', 'float with Metagross', 'swim with Kygore']
Hoenn_entertainment = ['get a starter from Professor Birch', 'fight team Magma', 'fight team Aqua', 'fight the elite four']

Sinnoh_food = ['Munchlaxs bed and breakfast', 'carnivines not so vegan burger joint', 'cherrims fruit palace', 'bidoofs sushi on the log']
Sinnoh_transport = ['dig with garchomp', 'fly with staraptor', 'teleport with dialga', 'through dimensions with Arceus']
Sinnoh_entertainment = ['get a starter from professor rowan', 'fight the elite four', 'catch a shaymin', 'discover the secrets of the regis']

Galar_food = ['Coalossals BBQ', 'Appletons pastries', 'Cramorants catch', 'sinisteas cafe']
Galar_transport = ['Corviknight flights', 'ride on a Dubwool', 'ride on a Copperajah', 'ride on a Spectrier']
Galar_entertainment = ['Meet the champion Leon', 'go to a toxtricity concert', 'roam the wild land', 'attend the champion cup']


def entertainment_picker(destinaiton):
    if destinaiton == "Kanto": # this is where the logic will go based on Kanto selection
        
        pass

picked_entertainment = entertainment_picker(picked_region)