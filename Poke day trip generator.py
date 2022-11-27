from cProfile import run
from multiprocessing.pool import RUN
from optparse import TitledHelpFormatter
import random
from tkinter import Y

places_to_visit = ["Kanto", "Jhoto", "Hoenn", "Sinnoh", "Galar"]

Kanto_food = ['Cubones home cooking', 'Magmars BBQ', 'The Snorlax buffet', 'Tangelas stir fry']
Kanto_transport = ['fly with Dragonite', 'teleport with Abra', 'swim with Lapras', 'tunnel with Diglet']
kanto_entertainment = ['meet professor Oak and pick a starter pokemon', 'win some cash at Celedon game center', 'battle the elite four', 'catch some pokemon in the Safari Zone']

Jhoto_food = ['Miltanks ice cream', 'Shuckles seafood', 'Steelixs kabobs', 'Bellosems vegan specials']
Jhoto_transport = ['fly on Noctowl', 'swim on Feraligatr', 'teleport with Stantler', 'ride on Raikou']
Jhoto_entertainment = ['pick a starter with professor Elm', 'battle the elite four', 'catch a shiny red Gyrados', 'catch the Unknown alphabet']

Hoenn_food = ['Ludicolos cantina', 'Crawdaunts crawfish boil', 'Spindas bar and grill', 'Hariyamas sushi hut' ]
Hoenn_transport = ['teleport with Gardevoir', 'fly with Flygon', 'float with Metagross', 'swim with Kygore']
Hoenn_entertainment = ['get a starter from Professor Birch', 'fight team Magma', 'fight team Aqua', 'fight the elite four']

Sinnoh_food = ['Munchlaxs bed and breakfast', 'Carnivines not so vegan burger joint', 'Cherrims fruit palace', 'Bidoofs sushi on the log']
Sinnoh_transport = ['dig with Garchomp', 'fly with Staraptor', 'teleport with Dialga', 'through dimensions with Arceus']
Sinnoh_entertainment = ['get a starter from professor Rowan', 'fight the elite four', 'catch a Shaymin', 'discover the secrets of the Regis']

Galar_food = ['Coalossals BBQ', 'Appletons pastries', 'Cramorants catch', 'sinisteas cafe']
Galar_transport = ['Corviknight flights', 'ride on a Dubwool', 'ride on a Copperajah', 'ride on a Spectrier']
Galar_entertainment = ['Meet the champion Leon', 'go to a toxtricity concert', 'roam the wild land', 'attend the champion cup']

print("Hello and welcome to the wonderful world of Pokemon, lets get you all set up for a fantastic journey!")
print("")

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
print("")
print(picked_region)
print('Thats a great region, lets figure out the details now!')
print("")




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

    elif destinaiton == "Jhoto": 
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

    elif destinaiton == "Hoenn": 
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
    
    elif destinaiton == "Sinnoh": 
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

    elif destinaiton == "Galar": 
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
print("")
print(picked_food)
print('Great Choice, they really do have the best food in the region!')
print("")


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

    elif destinaiton == "Jhoto": 
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

    elif destinaiton == "Hoenn": 
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
    
    elif destinaiton == "Sinnoh": 
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

    elif destinaiton == "Galar": 
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
print("")
print (picked_travel)
print ('Great Choice, that truly is the only way to get around!')
print("")

def entertainment_picker(destinaiton): # this is where the logic for the entertainment will go based on region selection
    if destinaiton == "Kanto": 
        entertainment_picked = False
        poke_entertainment_kanto = random.choice(kanto_entertainment)
        entertainment_choice = input('Now lets see what we will do for fun. How does ' + f'{poke_entertainment_kanto} sound? ' + 'Please select y/n ')
        if entertainment_choice == 'y':
            entertainment_picked = True
            return poke_entertainment_kanto

        while entertainment_picked == False:
            poke_entertainment_kanto = random.choice(kanto_entertainment)
            entertainment_choice = input('Youre right thats too boring. What about ' + f'{poke_entertainment_kanto}? ' + 'Please select y/n ')
            if entertainment_choice == 'y':
                entertainment_picked = True
                return poke_entertainment_kanto
    
    elif destinaiton == "Jhoto": 
        entertainment_picked = False
        poke_entertainment_Jhoto = random.choice(Jhoto_entertainment)
        entertainment_choice = input('Now lets see what we will do for fun. How does ' + f'{poke_entertainment_Jhoto} sound? ' + 'Please select y/n ')
        if entertainment_choice == 'y':
            entertainment_picked = True
            return poke_entertainment_Jhoto

        while entertainment_picked == False:
            poke_entertainment_Jhoto = random.choice(Jhoto_entertainment)
            entertainment_choice = input('Youre right thats too boring. What about ' + f'{poke_entertainment_Jhoto}? ' + 'Please select y/n ')
            if entertainment_choice == 'y':
                entertainment_picked = True
                return poke_entertainment_Jhoto
    
    elif destinaiton == "Hoenn": 
        entertainment_picked = False
        poke_entertainment_Hoenn = random.choice(Hoenn_entertainment)
        entertainment_choice = input('Now lets see what we will do for fun. How does ' + f'{poke_entertainment_Hoenn} sound? ' + 'Please select y/n ')
        if entertainment_choice == 'y':
            entertainment_picked = True
            return poke_entertainment_Hoenn

        while entertainment_picked == False:
            poke_entertainment_Hoenn = random.choice(Hoenn_entertainment)
            entertainment_choice = input('Youre right thats too boring. What about ' + f'{poke_entertainment_Hoenn}? ' + 'Please select y/n ')
            if entertainment_choice == 'y':
                entertainment_picked = True
                return poke_entertainment_Hoenn
    
    elif destinaiton == "Sinnoh": 
        entertainment_picked = False
        poke_entertainment_Sinnoh = random.choice(Sinnoh_entertainment)
        entertainment_choice = input('Now lets see what we will do for fun. How does ' + f'{poke_entertainment_Sinnoh} sound? ' + 'Please select y/n ')
        if entertainment_choice == 'y':
            entertainment_picked = True
            return poke_entertainment_Sinnoh

        while entertainment_picked == False:
            poke_entertainment_Sinnoh = random.choice(Sinnoh_entertainment)
            entertainment_choice = input('Youre right thats too boring. What about ' + f'{poke_entertainment_Sinnoh}? ' + 'Please select y/n ')
            if entertainment_choice == 'y':
                entertainment_picked = True
                return poke_entertainment_Sinnoh
    
    elif destinaiton == "Galar": 
        entertainment_picked = False
        poke_entertainment_Galar = random.choice(Galar_entertainment)
        entertainment_choice = input('Now lets see what we will do for fun. How does ' + f'{poke_entertainment_Galar} sound? ' + 'Please select y/n ')
        if entertainment_choice == 'y':
            entertainment_picked = True
            return poke_entertainment_Galar

        while entertainment_picked == False:
            poke_entertainment_Galar = random.choice(Galar_entertainment)
            entertainment_choice = input('Youre right thats too boring. What about ' + f'{poke_entertainment_Galar}? ' + 'Please select y/n ')
            if entertainment_choice == 'y':
                entertainment_picked = True
                return poke_entertainment_Galar

picked_entertianment = entertainment_picker(picked_region)
print("")
print (picked_entertianment)
print ('Great Choice, I hear thats only availabe to do for a short time!')
print("")

print('Now that we have all of our choices lets review')
print("")

poke_dictionary = {
    'region': picked_region,
    'food' : picked_food,
    'transportation': picked_travel,
    'entertainment': picked_entertianment,
}

print(poke_dictionary)
#print('region: '+ f'{picked_region}')
#print('food: '+f'{picked_food}')
#print('transportation: '+ f'{picked_travel}')
#print('entertainment: '+ f'{picked_entertianment}')
print("")

confirm_trip = False
while confirm_trip == False:
    confirm_input = input('is this acceptable? please enter y/n ')
    print("")
    if confirm_input == 'y':
        print('Great! you will be traveling to the ' + f'{picked_region} region. '+'While there you will dine at '+f'{picked_food}. ' + 'You will travel with ' + f'{picked_travel}. ' + 'Finally you will have the form of entertainment of ' + f'{picked_entertianment}. '+ 'We hope you enjoy your trip and come back to use us again!')
        confirm_trip = True        
    elif confirm_input == 'n': # If no they will be prompted to answer all the questions again to make sure they are happy with their choice.
        print('Not a problem lets reselct your trip.')
        print("")
        picked_region = region_picker()
        print("")
        picked_food = food_picker(picked_region)
        print("")
        picked_travel = travel_picker(picked_region)
        print("")
        picked_entertianment = entertainment_picker(picked_region)
        print("")
        print('Now that we have all of our choices lets review')
        print("")
        print('region: '+ f'{picked_region}')
        print('food: '+f'{picked_food}')
        print('transportation: '+ f'{picked_travel}')
        print('entertainment: '+ f'{picked_entertianment}')
        print("")