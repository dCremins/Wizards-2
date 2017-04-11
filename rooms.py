from adventurelib import *
import items

#####################
# Rooms
#####################

Room.items = Bag()
Room.lit = True

upstairs = Room("""
The room is cluttered with dirty clothes and papers.
STAIRS lead DOWN into another room of the tower.
""")
upstairs.items = Bag({items.crystal_puzzle, items.bookshelf})

downstairs = Room("""
This room is used for storage and is filled with lots of junk.
""")
downstairs.lit = False
downstairs.items = Bag({items.bCrystal, items.cat, items.lamp})
