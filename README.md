### Introduction

Python library to slot items into pre-defined slots.

### Installation - TODO

### Examples

- ```cat sample.py```

  ```
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

  print "Has 5 been slotted"
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
  print json.dumps(s.dump(reverse=True), indent=2)
  print "=================================="
  ```

- Output

  ```
  Has 5 been slotted
  True
  ==================================
  Target slot of 5
  Target slot start - 1
  Target slot end - 10
  Target slot str representation - 1-10
  ==================================
  Target slot of 11
  Is 15 in the same target slot?
  True
  ==================================
  All slots
  [<slotter.slotter.Slot object at 0x7f6b1c4f2b50>, <slotter.slotter.Slot object at 0x7f6b1c4f2c10>]
  ==================================
  All items
  [5, 11, 15]
  ==================================
  All slot items
  {<slotter.slotter.Slot object at 0x7f6b1c4f2c10>: [11, 15], <slotter.slotter.Slot object at 0x7f6b1c4f2b50>: [5]}
  ==================================
  All item slots
  {11: <slotter.slotter.Slot object at 0x7f6b1c4f2c10>, 5: <slotter.slotter.Slot object at 0x7f6b1c4f2b50>, 15: <slotter.slotter.Slot object at 0x7f6b1c4f2c10>}
  ==================================
  Dumpable ds
  {
    "1-10": [
      5
    ],
    "10-20": [
      11,
      15
    ]
  }
  ==================================
  Dumpable ds - reverse
  {
    "11": "10-20",
    "15": "10-20",
    "5": "1-10"
  }
  ==================================
  ```
