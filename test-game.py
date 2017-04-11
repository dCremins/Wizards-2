from adventurelib import *
from puzzles import reveal
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
                print(('%s' % i.roomdesc) + ' is ' + ('%s' % i.location))

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
            if hasattr(rm, 'puzzle_name'):
                print("it's a puzzle!")
                reveal(rm.puzzle_name, current_room)
        if hasattr(rm, 'def_name'):
            print("It's %s." % rm.def_name)
        else:
            print("It's " + ("%s." % rm.roomdesc.lower()))
        if hasattr(rm, 'puzzle'):
            print(rm.puzzle)
    elif obj:
        print("It's " + ("%s." % rm.roomdesc.lower()) + ". You put it back in your bag")
    else:
        print("What %s?" % item)
    print("""
    """)
    look()

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

@when('put THING in PLACE', action='in')
@when('put THING on PLACE', action='on')
@when('use THING in PLACE', action='in')
@when('use THING on PLACE', action='on')
def put(thing, place, action):
    obj = inventory.take(thing)
    if not obj:
        say('You do not have a %s.' % thing)
    if not hasattr(place, 'items'):
        print("I don't see a %s anywhere." % place)
    elif not isinstance(place.items, Bag):
        print("Those things don't go together")
        inventory.add(thing)
    elif place.items.get_random() is not None:
        print("There is already something here.")
        inventory.add(thing)
    else:
        print(("You put the %s" % thing) + (" %s the" % action) + (place))
        place.add(thing)



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
    # Not in the room
    if not char:
        print("Who is that?")
    # Not Character
    elif not hasattr(char, 'def_name'):
        print("You talk to the %s but no one responds. You feel a little silly." % char)
    # Character
    else:
        # If you haven't investigated it already
        # count this as investigating it
        if not char.inspected:
            if not char.inspected:
                char.inspected = True
                char.roomdesc = char.def_name
                print("It's %s." % char.roomdesc)
                print("You approach %s." % char.roomdesc)

        if char == items.cat:
            conversation = {'Sup?': {'B': 'Not Much', 'C': 'I\'m looking for crystals', 'D': 'Holy shit! You can talk!?'},
                'B': 'Right....So, did you like, need something?',
                'C': 'RND',
                'D': 'What? Did you hit your head or something?',
                'What? Did you hit your head or something?': {'F': 'Yes', 'G': 'No!', 'H': 'Do you like cheese?'},
                'F': 'Right....So, did you like, need something?',
                'G': 'Right....So, did you like, need something?',
                'H': 'Right....So, did you like, need something?',
                'Right....So, did you like, need something?': {'C': 'I\'m Looking for crystals', 'J': "No"},
                'J': 'Ok. Bye then.',
                'RND': {'1': 'I already found that', '0': 'Thanks'},
                '1': 'RND',
                '0': 'Ok. Bye then.'}
            talk(conversation, list(conversation.keys())[0], conversation[list(conversation.keys())[-1]])



#####################
# Dialogue Tree
#####################

def talk(convo, choice, end):
    done = False
    if choice not in convo:
        print("what?")
        done = True
    else:
        # print Arnold's first response
        print("""
        """)
        print('"' + (list(convo.keys())[0]) + '"')

    while not done:
        # randomly choose a crystal location
        rnd_loc = items.crystals.take_random()
        # print choices based on Arnold's response
        for node in convo[choice]:
            if convo[choice][node]:
                desc = ': ' + convo[choice][node]
            else:
                desc = ''
            print(("[%s]" % node) + desc)
        print("""
        """)
        # set choice qual to user input
        try:
            hold = input('>>').strip()
            if not hold.upper() in convo[choice]:
                print("what?")
                continue
            else:
                choice = hold
        except EOFError:
            print()
            break

        # if input is quit, exit conversation
        if choice.lower() == 'quit' or choice.lower() == 'q':
            print("You awkwardly leave the conversation.")
            break
        # if input doesn't exist
        if choice.upper() not in convo:
            print("huh?")
        # if input triggers Arnold's end response
        elif convo[choice.upper()] == end:
            print('"' + (convo[choice.upper()]) + '"')
            done = True
        # if input triggers random location response
        elif convo[choice.upper()] == 'RND':
            if not rnd_loc:
                print("Well I got nothing man.")
                del convo["RND"]["1"]
                #del convo["1"]
            else:
                print("Did you look %s?" % rnd_loc.location)
            choice = convo[choice.upper()]
        # print Arnold's response
        # then change choice to Arnold's response
        # and return to the top of the while loop
        else:
            print('"' + (convo[choice.upper()]) + '"')
            choice = convo[choice.upper()]

    print("""
    """)
    look()

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
    current_room = rooms.upstairs
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
