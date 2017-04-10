from adventurelib import *


#####################
# Player
#####################

inventory = Bag()

#####################
# Items
#####################
Item.location = 'is here'
Item.desc = ''
Item.roomdesc = ''
Item.inspected = False

gCrystal = Item('grey crystal', 'gray crystal')

bCrystal = Item('glitters', 'glitter', 'glittering thing', 'something glittering', 'blue crystal')
bCrystal.location = 'from under some papers'
bCrystal.desc = 'A luminous BLUE CRYSTAL'
bCrystal.roomdesc = 'Something GLITTERS'

rCrystal = Item('brown crystal')

yCrystal = Item('yellow crystal')

#####################
# Characters
#####################

cat = Item('furry', 'furry thing', 'something furry', 'arnold', 'arnold fuzzybottom', 'cat', 'fuzzybottom')
cat.location = 'is curled up in an old suitcase'
cat.def_name = 'Arnold Fuzzybottom'
cat.roomdesc = 'Something FURRY'

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
        if current_room.items:
            for i in current_room.items:
                print(('%s ' % i.roomdesc)+ ('%s ' % i.location))

@when('look ITEM')
@when('look at ITEM')
def look_at(item):
    obj = inventory.find(item)
    rm = current_room.items.find(item)

    if rm:
        if not rm.inspected:
            rm.inspected = True
            if hasattr(rm, 'def_name'):
                rm.roomdesc = rm.def_name
            else:
                rm.roomdesc = rm.desc
        if hasattr(rm, 'def_name'):
            print("It's %s." % rm.def_name)
        else:
            print("It's " + ("%s." % rm.roomdesc.lower()))
    elif obj:
        print("It's " + ("%s." % rm.roomdesc.lower()) + ". You put it back in your bag")
    else:
        print("What %s?" % item)

@when('take ITEM')
def take(item):
    obj = current_room.items.find(item)
    if obj:
        if not obj.inspected:
            print("Shouldn't you look at that first? What if it bites!")
        elif hasattr(obj, 'def_name'):
            print("I don't think they'd like that.")
        else:
            say('You pick up ' + ("%s." % obj.roomdesc.lower()))
            obj = current_room.items.take(item)
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

    print("You climb the stairs.")

    look()

@when('go downstairs')
@when('down')
def down_stairs():
    global current_room

    if current_room is not upstairs:
        print("You're already downstairs.")
        return

    current_room = downstairs

    print("You walk down the stairs.")
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
