from adventurelib import *


#####################
# Player
#####################

inventory = Bag()

#####################
# Items
#####################

gCrystal = Item('grey crystal', 'gray crystal')
bCrystal = Item('blue crystal', 'glitter', 'glittering thing', 'something glittering')
rCrystal = Item('brown crystal')
yCrystal = Item('yellow crystal')

#####################
# Characters
#####################

cat = Item('a cat', 'furry thing', 'something furry')
cat.def_name = 'Arnold Fuzzybottom'

#####################
# Rooms
#####################

Room.items = Bag()
Room.lit = True

upstairs = Room("""
The room is cluttered with dirty clothes and papers.
There is a BOOKCASE against one wall.
There is a TABLE on the far wall between two windows.
STAIRS lead DOWN into another room of the tower.
""")

downstairs = Room("""
This room is used for storage and is filled with lots of junk.
Something FURRY is curled up in an old suitcase.
Something GLITTERS from under some papers.
""")
downstairs.lit = False
downstairs.items = Bag({bCrystal, cat})

current_room = upstairs

#####################
# Commands
#####################

@when('look')
def look():
    if not current_room.lit:
        print("It's too dark for you to see anything.")
    else:
        print(current_room)

@when('look ITEM')
@when('look at ITEM')
def look_at(item):
    obj = inventory.find(item)
    rm = current_room.items.find(item)
    if obj:
        print("It's a %s. You put it back in your bag" % obj)
    elif rm:
        print("It's a %s." % rm)

@when('take ITEM')
def take(item):
    obj = current_room.items.take(item)
    if obj:
        say('You pick up the %s.' % obj)
        inventory.add(obj)
    else:
        say('There is no %s here.' % item)

@when('drop THING')
def drop(thing):
    obj = inventory.take(thing)
    if not obj:
        say('You do not have a %s.' % thing)
    else:
        say('You drop the %s.' % obj)
        current_room.items.add(obj)

@when('inventory')
@when('i')
def show_inventory():
    say('You have:')
    for thing in inventory:
        say(thing)

@when('go upstairs')
@when('up')
def climb_stairs():
    global current_room

    if current_room is not downstairs:
        print("You're already upstairs.")
        return

    current_room = downstairs

    print("""You climb the stairs.
    """)

    look()

@when('go downstairs')
@when('down')
def down_stairs():
    global current_room

    if current_room is not upstairs:
        print("You're already downstairs.")
        return

    current_room = downstairs

    print("""You walk down the stairs.
    """)

    look()

@when('turn on lights')
@when('turn on light')
@when('turn lights on')
@when('turn light on')
def clap_on():
    global current_room

    if not current_room.lit:
        print("You turn on the lights.")
        current_room.lit = True
        look()
    else:
        print("The lights are already on.")

@when('turn off lights')
@when('turn off light')
@when('turn lights off')
@when('turn light off')
def clap_off():
    global current_room

    if current_room.lit:
        print("You turn off the lights.")
        current_room.lit = False
        look()
    else:
        print("The lights are already off.")

































#####################
# Start the Game
#####################

print("""
*********************************
========     Wizards!     =======

A Python Game by Devin Cremins
*********************************


You wake up in the top room of a Wizard's tower.
You must have fallen asleep here again.

""")

look()

start()
