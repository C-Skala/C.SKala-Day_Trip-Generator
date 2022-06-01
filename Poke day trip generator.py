print("Hello and welcome to the wonderful world of pokemon, lets get you all set up for a fantastic journey!")

import random
places_to_visit = ["Kanto", "Jhoto", "Hoenn", "Sinnoh", "Aloha", "Galar"]

def destination_picker():
    location_picked = False
    poke_places = random.choice(places_to_visit)
    travel_location = input('Would you like to visit the region of ' + f'{poke_places}? ' + 'Please select y/n ')
    if travel_location == 'y':
        location_picked = True
        print('Thats a great region, lets figure out the details now!')
        return poke_places
    while location_picked == False:
        poke_places = random.choice(places_to_visit)
        travel_location = input('I get it, that region is not for everyone. What about ' + f'{poke_places}? ' + 'Please select y/n ')
        if travel_location == 'y':
            location_picked = True
            print('Thats a great region, lets figure out the details now!')
            return poke_places

picked_destination = destination_picker()
print(picked_destination)

Kato_food = ['']

def entertainment_picker(destinaiton):
    if destinaiton == "Kanto":
        # this is where the logic will go based on Kanto selection
        pass

picked_entertainment = entertainment_picker(picked_destination)