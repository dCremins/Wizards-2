from adventurelib import *

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

ghost = Item('ghost', 'blink')
ghost.def_name = "Blink"
ghost.roomdesc = 'A ghost'
