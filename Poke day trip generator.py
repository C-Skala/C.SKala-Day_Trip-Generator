print("Hello and welcome to the wonderful world of pokemon, lets get you all set up for a fantastic journey!")

import random
places_to_visit = ["Kanto", "Jhoto", "Hoenn", "Sinnoh", "Aloha", "Galar"]

def region_picker():
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

Kanto_food = ['']
Kanto_transport = ['']
kanto_entertainment = ['']

Jhoto_food = ['']
Jhoto_transport = ['']
Jhoto_entertainment = ['']

Hoenn_food = ['']
Hoenn_transport = ['']
Hoenn_entertainment = ['']

Sinnoh_food = ['']
Sinnoh_transport = ['']
Sinnoh_entertainment = ['']

Aloha_food = ['']
Aloha_transport = ['']
Aloha_entertainment = ['']

Galar_food = ['']
Galar_transport = ['']
Galar_entertainment = ['']


def entertainment_picker(destinaiton):
    if destinaiton == "Kanto":
        # this is where the logic will go based on Kanto selection
        pass

picked_entertainment = entertainment_picker(picked_destination)