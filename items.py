from adventurelib import *

#####################
# Items
#####################

Item.location = 'is here'
Item.desc = ''
Item.roomdesc = ''
Item.inspected = False
Item.single = ''

gCrystal = Item('sparkling', 'sparkle', 'sparkling thing', 'something sparkling', 'grey crystal', 'gray crystal')
gCrystal.location = 'in the bookshelf'
gCrystal.roomdesc = 'Something SPARKLING'
gCrystal.desc = 'A GREY CRYSTAL. Gray...?'
gCrystal.single = 'grey crystal'

bCrystal = Item('glittering', 'glitter', 'glittering thing', 'something glittering', 'blue crystal')
bCrystal.location = 'under some papers'
bCrystal.roomdesc = 'Something GLITTERING'
bCrystal.desc = 'A luminous BLUE CRYSTAL'
bCrystal.single = 'blue crystal'

rCrystal = Item('shiny', 'shining', 'shining thing', 'something shining', 'shiny thing', 'something shiny','brown crystal', 'brown crystal', 'green crystal', 'green-ish crystal', 'greenish crystal', 'brown-ish crystal', 'brownish crystal')
rCrystal.location = 'in your pocket'
rCrystal.roomdesc = 'A sparkling GREEN-ish CRYSTAL. Brownish?'
rCrystal.single = 'green-ish crystal'
rCrystal.inspected = True

yCrystal = Item('fancy', 'fancy thing', 'something fancy', 'yellow crystal')
yCrystal.location = 'in the lamp'
yCrystal.roomdesc = 'Something FANCY'
yCrystal.desc = 'An expensive looking YELLOW CRYSTAL'
yCrystal.single = 'yellow crystal'

lamp = Item('lamp', 'the lamp', 'dead lamp', 'broken lamp')
lamp.location = 'on the floor'
lamp.single = 'lamp'
lamp.desc = 'A dead LAMP'
lamp.roomdesc = 'A dead LAMP'
lamp.puzzle_name = 'lamp'
lamp.parts = Bag({yCrystal})

bookshelf = Item('bookshelf', 'the bookshelf', 'bookcase', 'the bookcase')
bookshelf.location = 'against one wall'
bookshelf.single = 'BOOKSHELF'
bookshelf.roomdesc = 'A BOOKSHELF'
bookshelf.desc = 'A stuffy old BOOKSHELF'
bookshelf.puzzle_name = 'bookshelf'
bookshelf.parts = Bag({gCrystal})

#####################
# Puzzles
#####################

crystals = Bag({bCrystal, rCrystal, yCrystal, gCrystal})

crystal_puzzle = Item('table', 'puzzle table', 'crystal table', 'crystal puzzle', 'wizard puzzle', 'wizard table', 'wizards puzzle', 'wizards table', 'wizard\'s puzzle', 'wizard\'s table')
crystal_puzzle.location = 'against the far wall'
crystal_puzzle.roomdesc = 'A TABLE'
crystal_puzzle.desc = 'The WIZARD\'S TABLE'
crystal_puzzle.puzzle_name = 'crystals'
crystal_puzzle.puzzle = 'There are FOUR SLOTS to the TOP RIGHT, TOP LEFT, BOTTOM RIGHT, and BOTTOM LEFT.'
crystal_puzzle.solved = False
crystal_puzzle.single = 'table'

crystal_puzzle_TR = Item('top right', 'top right slot', 'tr', 'tr slot')
crystal_puzzle_TR.roomdesc = 'A strange slot'
crystal_puzzle_TR.location = 'in the TOP RIGHT of the table'
crystal_puzzle_TR.items = Bag()
crystal_puzzle_TR.solved = False
crystal_puzzle_TR.inspected = True
crystal_puzzle_TR.single = 'top right slot'
crystal_puzzle_TR.puzzle_name = crystal_puzzle
crystal_puzzle_TR.solve_condition = 'yellow crystal'

crystal_puzzle_TL = Item('top left', 'top left slot', 'tl', 'tl slot')
crystal_puzzle_TL.roomdesc = 'A strange slot'
crystal_puzzle_TL.location = 'in the TOP LEFT of the table'
crystal_puzzle_TL.items = Bag()
crystal_puzzle_TL.solved = False
crystal_puzzle_TL.inspected = True
crystal_puzzle_TL.single = 'top left slot'
crystal_puzzle_TL.puzzle_name = crystal_puzzle
crystal_puzzle_TL.solve_condition = 'green-ish crystal'

crystal_puzzle_BR = Item('bottom right', 'bottom right slot', 'br', 'br slot')
crystal_puzzle_BR.roomdesc = 'A strange slot'
crystal_puzzle_BR.location = 'in the BOTTOM RIGHT of the table'
crystal_puzzle_BR.items = Bag()
crystal_puzzle_BR.solved = False
crystal_puzzle_BR.inspected = True
crystal_puzzle_BR.single = 'bottom right slot'
crystal_puzzle_BR.puzzle_name = crystal_puzzle
crystal_puzzle_BR.solve_condition = 'grey crystal'

crystal_puzzle_BL = Item('bottom left', 'bottom left slot', 'bl', 'bl slot')
crystal_puzzle_BL.roomdesc = 'A strange slot'
crystal_puzzle_BL.location = 'in the BOTTOM LEFT of the table'
crystal_puzzle_BL.items = Bag()
crystal_puzzle_BL.solved = False
crystal_puzzle_BL.inspected = True
crystal_puzzle_BL.single = 'bottom left slot'
crystal_puzzle_BL.puzzle_name = crystal_puzzle
crystal_puzzle_BL.solve_condition = 'blue crystal'

crystal_puzzle.parts = [crystal_puzzle_TR, crystal_puzzle_TL, crystal_puzzle_BR, crystal_puzzle_BL]

#####################
# Characters
#####################

cat = Item('furry', 'furry thing', 'something furry', 'arnold', 'arnold fuzzybottom', 'cat', 'fuzzybottom')
cat.location = 'curled up in an old suitcase'
cat.def_name = 'Arnold Fuzzybottom'
cat.roomdesc = 'Something FURRY'
