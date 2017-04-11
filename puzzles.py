from adventurelib import *
import rooms, items, sys

def reveal(puzzle, room):
    bag = room.items
    if puzzle == 'crystals':
        current_puzzle = items.crystal_puzzle
    if puzzle == 'lamp':
        current_puzzle = items.lamp
    if puzzle == 'bookshelf':
        current_puzzle = items.bookshelf
    for part in current_puzzle.parts:
        print(('%s' % part.roomdesc) + (' is %s' % part.location))
        bag.add(part)
    return

def check_solve(obj, part):
    if obj.single == part.solve_condition:
        part.solved = True
        print("You hear a click.")
    puzzle = part.puzzle_name
    for each in puzzle.parts:
        if not each.solved:
            puzzle.solved = False
            break
        else:
            puzzle.solved = True
    if puzzle.solved:
        print("""
        You Win!!

        .
        ..
        ...

        Kind of anti-climactic, huh?

        .
        ..
        ...

        Oh well.

        Bye!
        """)
        sys.exit()
