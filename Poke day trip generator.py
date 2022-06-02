from optparse import TitledHelpFormatter
import random

places_to_visit = ["Kanto", "Jhoto", "Hoenn", "Sinnoh", "Galar"]

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

print("Hello and welcome to the wonderful world of pokemon, lets get you all set up for a fantastic journey!")

def region_picker(): # This will pick the overall region to set the whole trip
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




def food_picker(destinaiton): # this is where the logic for the food will go based on region selection
    if destinaiton == "Kanto": 
        food_picked = False
        poke_food_kanto = random.choice(Kanto_food)
        food_location = input('Now lets pick a place to eat for the day. Would you like to try ' + f'{poke_food_kanto}? ' + 'Please select y/n ')
        if food_location == 'y':
            food_picked = True
            return poke_food_kanto

        while food_picked == False:
            poke_food_kanto = random.choice(Kanto_food)
            food_location = input('I get it, that place is not for everyone. What about ' + f'{poke_food_kanto}? ' + 'Please select y/n ')
            if food_location == 'y':
                food_picked = True
                return poke_food_kanto

    if destinaiton == "Jhoto": 
        food_picked = False
        poke_food_Jhoto = random.choice(Jhoto_food)
        food_location = input('Now lets pick a place to eat for the day. Would you like to try ' + f'{poke_food_Jhoto}? ' + 'Please select y/n ')
        if food_location == 'y':
            food_picked = True
            return poke_food_Jhoto

        while food_picked == False:
            poke_food_Jhoto = random.choice(Jhoto_food)
            food_location = input('I get it, that place is not for everyone. What about ' + f'{poke_food_Jhoto}? ' + 'Please select y/n ')
            if food_location == 'y':
                food_picked = True
                return poke_food_Jhoto

    if destinaiton == "Hoenn": 
        food_picked = False
        poke_food_Hoenn = random.choice(Hoenn_food)
        food_location = input('Now lets pick a place to eat for the day. Would you like to try ' + f'{poke_food_Hoenn}? ' + 'Please select y/n ')
        if food_location == 'y':
            food_picked = True
            return poke_food_Hoenn

        while food_picked == False:
            poke_food_Hoenn = random.choice(Hoenn_food)
            food_location = input('I get it, that place is not for everyone. What about ' + f'{poke_food_Hoenn}? ' + 'Please select y/n ')
            if food_location == 'y':
                food_picked = True
                return poke_food_Hoenn
    
    if destinaiton == "Sinnoh": 
        food_picked = False
        poke_food_Sinnoh = random.choice(Sinnoh_food)
        food_location = input('Now lets pick a place to eat for the day. Would you like to try ' + f'{poke_food_Sinnoh}? ' + 'Please select y/n ')
        if food_location == 'y':
            food_picked = True
            return poke_food_Sinnoh

        while food_picked == False:
            poke_food_Sinnoh = random.choice(Sinnoh_food)
            food_location = input('I get it, that place is not for everyone. What about ' + f'{poke_food_Sinnoh}? ' + 'Please select y/n ')
            if food_location == 'y':
                food_picked = True
                return poke_food_Sinnoh

    if destinaiton == "Galar": 
        food_picked = False
        poke_food_Galar = random.choice(Galar_food)
        food_location = input('Now lets pick a place to eat for the day. Would you like to try ' + f'{poke_food_Galar}? ' + 'Please select y/n ')
        if food_location == 'y':
            food_picked = True
            return poke_food_Galar

        while food_picked == False:
            poke_food_Galar = random.choice(Galar_food)
            food_location = input('I get it, that place is not for everyone. What about ' + f'{poke_food_Galar}? ' + 'Please select y/n ')
            if food_location == 'y':
                food_picked = True
                return poke_food_Galar
    

picked_food = food_picker(picked_region)
print(picked_food)
print('Great Choice, they really do have the best rood in the region!')


def travel_picker(destinaiton): # this is where the logic for the travel will go based on region selection
    if destinaiton == "Kanto": 
        travel_picked = False
        poke_travel_kanto = random.choice(Kanto_transport)
        travel_choice = input('Now lets see how we will get around. Would you like to try ' + f'{poke_travel_kanto}? ' + 'Please select y/n ')
        if travel_choice == 'y':
            travel_picked = True
            return poke_travel_kanto

        while travel_picked == False:
            poke_travel_kanto = random.choice(Kanto_transport)
            travel_choice = input('I get it, that meathod isnt for everyone. What about ' + f'{poke_travel_kanto}? ' + 'Please select y/n ')
            if travel_choice == 'y':
                travel_picked = True
                return poke_travel_kanto

    if destinaiton == "Jhoto": 
        travel_picked = False
        poke_travel_Jhoto = random.choice(Jhoto_transport)
        travel_choice = input('Now lets see how we will get around. Would you like to try ' + f'{poke_travel_Jhoto}? ' + 'Please select y/n ')
        if travel_choice == 'y':
            travel_picked = True
            return poke_travel_Jhoto

        while travel_picked == False:
            poke_travel_Jhoto = random.choice(Jhoto_transport)
            travel_choice = input('I get it, that meathod isnt for everyone. What about ' + f'{poke_travel_Jhoto}? ' + 'Please select y/n ')
            if travel_choice == 'y':
                travel_picked = True
                return poke_travel_Jhoto

    if destinaiton == "Hoenn": 
        travel_picked = False
        poke_travel_Hoenn = random.choice(Hoenn_transport)
        travel_choice = input('Now lets see how we will get around. Would you like to try ' + f'{poke_travel_Hoenn}? ' + 'Please select y/n ')
        if travel_choice == 'y':
            travel_picked = True
            return poke_travel_Hoenn

        while travel_picked == False:
            poke_travel_Hoenn = random.choice(Hoenn_transport)
            travel_choice = input('I get it, that meathod isnt for everyone. What about ' + f'{poke_travel_Hoenn}? ' + 'Please select y/n ')
            if travel_choice == 'y':
                travel_picked = True
                return poke_travel_Hoenn
    
    if destinaiton == "Sinnoh": 
        travel_picked = False
        poke_travel_Sinnoh = random.choice(Sinnoh_transport)
        travel_choice = input('Now lets see how we will get around. Would you like to try ' + f'{poke_travel_Sinnoh}? ' + 'Please select y/n ')
        if travel_choice == 'y':
            travel_picked = True
            return poke_travel_Sinnoh

        while travel_picked == False:
            poke_travel_Sinnoh = random.choice(Sinnoh_transport)
            travel_choice = input('I get it, that meathod isnt for everyone. What about ' + f'{poke_travel_Sinnoh}? ' + 'Please select y/n ')
            if travel_choice == 'y':
                travel_picked = True
                return poke_travel_Sinnoh

    if destinaiton == "Galar": 
        travel_picked = False
        poke_travel_Galar = random.choice(Galar_transport)
        travel_choice = input('Now lets see how we will get around. Would you like to try ' + f'{poke_travel_Galar}? ' + 'Please select y/n ')
        if travel_choice == 'y':
            travel_picked = True
            return poke_travel_Galar

        while travel_picked == False:
            poke_travel_Galar = random.choice(Galar_transport)
            travel_choice = input('I get it, that meathod isnt for everyone. What about ' + f'{poke_travel_Galar}? ' + 'Please select y/n ')
            if travel_choice == 'y':
                travel_picked = True
                return poke_travel_Galar
    

picked_travel = travel_picker(picked_region)
print (picked_travel)
print ('Great Choice, that truly is the only way to get around!')

def entertainment_picker(destinaiton): # this is where the logic for the entertainment will go based on region selection
    if destinaiton == "Kanto": 
        entertainment_picked = False
        poke_entertainment_kanto = random.choice(kanto_entertainment)
        entertainment_choice = input('Now lets see what we will do for fun. How does ' + f'{poke_entertainment_kanto} sound? ' + 'Please select y/n ')
        if entertainment_choice == 'y':
            entertainment_picked = True
            return poke_entertainment_kanto

        while entertainment_picked == False:
            poke_entertainment_kanto = random.choice(Kanto_transport)
            entertainment_choice = input('Youre right thats too boring. What about ' + f'{poke_entertainment_kanto}? ' + 'Please select y/n ')
            if entertainment_choice == 'y':
                entertainment_picked = True
                return poke_entertainment_kanto
    if destinaiton == "Jhoto": 
        entertainment_picked = False
        poke_entertainment_Jhoto = random.choice(Jhoto_entertainment)
        entertainment_choice = input('Now lets see what we will do for fun. How does ' + f'{poke_entertainment_Jhoto} sound? ' + 'Please select y/n ')
        if entertainment_choice == 'y':
            entertainment_picked = True
            return poke_entertainment_Jhoto

        while entertainment_picked == False:
            poke_entertainment_Jhoto = random.choice(Jhoto_transport)
            entertainment_choice = input('Youre right thats too boring. What about ' + f'{poke_entertainment_Jhoto}? ' + 'Please select y/n ')
            if entertainment_choice == 'y':
                entertainment_picked = True
                return poke_entertainment_Jhoto
    if destinaiton == "Hoenn": 
        entertainment_picked = False
        poke_entertainment_Hoenn = random.choice(Hoenn_entertainment)
        entertainment_choice = input('Now lets see what we will do for fun. How does ' + f'{poke_entertainment_Hoenn} sound? ' + 'Please select y/n ')
        if entertainment_choice == 'y':
            entertainment_picked = True
            return poke_entertainment_Hoenn

        while entertainment_picked == False:
            poke_entertainment_Hoenn = random.choice(Hoenn_transport)
            entertainment_choice = input('Youre right thats too boring. What about ' + f'{poke_entertainment_Hoenn}? ' + 'Please select y/n ')
            if entertainment_choice == 'y':
                entertainment_picked = True
                return poke_entertainment_Hoenn
    if destinaiton == "Sinnoh": 
        entertainment_picked = False
        poke_entertainment_Sinnoh = random.choice(Sinnoh_entertainment)
        entertainment_choice = input('Now lets see what we will do for fun. How does ' + f'{poke_entertainment_Sinnoh} sound? ' + 'Please select y/n ')
        if entertainment_choice == 'y':
            entertainment_picked = True
            return poke_entertainment_Sinnoh

        while entertainment_picked == False:
            poke_entertainment_Sinnoh = random.choice(Sinnoh_transport)
            entertainment_choice = input('Youre right thats too boring. What about ' + f'{poke_entertainment_Sinnoh}? ' + 'Please select y/n ')
            if entertainment_choice == 'y':
                entertainment_picked = True
                return poke_entertainment_Sinnoh
    if destinaiton == "Galar": 
        entertainment_picked = False
        poke_entertainment_Galar = random.choice(Galar_entertainment)
        entertainment_choice = input('Now lets see what we will do for fun. How does ' + f'{poke_entertainment_Galar} sound? ' + 'Please select y/n ')
        if entertainment_choice == 'y':
            entertainment_picked = True
            return poke_entertainment_Galar

        while entertainment_picked == False:
            poke_entertainment_Galar = random.choice(Galar_transport)
            entertainment_choice = input('Youre right thats too boring. What about ' + f'{poke_entertainment_Galar}? ' + 'Please select y/n ')
            if entertainment_choice == 'y':
                entertainment_picked = True
                return poke_entertainment_Galar

picked_entertianment = entertainment_picker(picked_region)
print (picked_entertianment)
print ('Great Choice, I hear thats only availabe to do for a short time!')

print('Now that we have all of our choices lets review')

