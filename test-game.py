from adventurelib import *
import rooms, items

#####################
# Player
#####################

inventory = Bag()

#####################
# Base Commands
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

#####################
# Character Commands
#####################

@when('talk PERSON')
@when('talk to PERSON')
@when('speak PERSON')
@when('speak to PERSON')
def chit_chat(person):
    char = current_room.items.find(person)
    conversation = {}
    if not char:
        print("Who is that?")
    elif not hasattr(char, 'def_name'):
        print("You talk to the %s but no one responds. You feel a little silly." % char)
    else:
        if char == items.ghost:
            print("You talk to the ghost.")
            conversation = {'Sup?': {'B': 'Not Much', 'C': 'I\'m looking for crystals', 'D': 'Holy shit! You can talk!?'},
                'B': 'Right....So, did you like, need something?',
                'C': 'Did you try the bookcase?',
                'D': 'What? Did you hit your head or something?',
                'What? Did you hit your head or something?': {'F': 'Yes', 'G': 'No!', 'H': 'Do you like cheese?'},
                'F': 'Cool....So, did you like, need something?',
                'G': 'Cool....So, did you like, need something?',
                'H': 'Cool....So, did you like, need something?',
                'Cool....So, did you like, need something?': {'C': 'I\'m Looking for crystals', 'J': "No"},
                'J': 'Ok. Bye then.',
                'Did you try the bookcase?': {'L': 'I already found that', 'M': 'Thanks!'},
                'L': 'Did you try the bookcase?',
                'M': 'Ok. Bye then.'}
            talk(conversation, list(conversation.keys())[0], conversation[list(conversation.keys())[-1]])

def talk(convo, start, end):
    done = False
    if start not in convo:
        print("what?")
        done = True
    else:
        print("""
        """)
        print('"' + (list(convo.keys())[0]) + '"')

    while not done:
        for node in convo[start]:
            if convo[start][node]:
                desc = ': ' + convo[start][node]
            else:
                desc = ''
            print(("[%s]" % node) + desc)
        print("""
        """)
        try:
            start = input('>>').strip()
        except EOFError:
            print()
            break

        if not start:
            continue
        if start.lower() == 'quit' or start.lower() == 'q':
            print("You awkwardly leave the conversation.")
            break
        elif convo[start.upper()] == end:
            print('"' + (convo[start.upper()]) + '"')
            done = True
        else:
            print('"' + (convo[start.upper()]) + '"')
            start = convo[start.upper()]

    print("""
    """)
    look()








#####################
# Dialogue Tree
#####################


#####################
# Navigation Commands
#####################

current_room = rooms.upstairs

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


@when('go upstairs')
@when('up')
def climb_stairs():
    global current_room

    if current_room is not rooms.downstairs:
        print("You're already upstairs.")
        return

    current_room = rooms.downstairs

    print("You climb the stairs.")

    look()

@when('go downstairs')
@when('down')
def down_stairs():
    global current_room

    if current_room is not rooms.upstairs:
        print("You're already downstairs.")
        return

    current_room = rooms.downstairs

    print("You walk down the stairs.")
    look()




















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
