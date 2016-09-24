#!/usr/bin/env python

import json
import slotter

# Create the slotter
s = slotter.create()

# Add slots to put items in
s.add_slot(1,10)
s.add_slot(10,20)

# Add items
s.add_item(5)
s.add_item(11)
s.add_item(15)

print "Has 5 been slotted?"
print s.slotted(5)   # has 5 been added
print "=================================="

print "Target slot of 5"
target_slot = s.find_slot(5) # in which slot has 5 been added
print "Target slot start - %s" % str(target_slot.start)
print "Target slot end - %s" % str(target_slot.end)
print "Target slot str representation - %s" % str(target_slot)
print "=================================="

print "Target slot of 11"
target_slot = s.find_slot(11) # in which slot has 5 been added
print "Is 15 in the same target slot?"
print 15 in target_slot
print "=================================="

print "All slots"
print s.slots
print "=================================="

print "All items"
print s.items
print "=================================="

print "All slot items"
print s.slot_items # return dictionary of slot -> items
print "=================================="

print "All item slots"
print s.item_slots # return dictionary of item -> slots
print "=================================="

print "Dumpable ds"
print json.dumps(s.dump(), indent=2) # return a json dumpable version of the ds
print "=================================="

print "Dumpable ds - reverse"
print json.dumps(s.dump(reverse=True), indent=2) # flip key values
print "=================================="
