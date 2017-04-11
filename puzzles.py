from adventurelib import *
import rooms, items

def reveal(puzzle, room):
    if not isinstance(puzzle, Item):
        return
    else:
        print("puzzle time!")
        if puzzle == 'crystals':
            puzzle_parts = crystal_puzzle.parts
        for part in puzzle_parts:
            room.items.add(part)
