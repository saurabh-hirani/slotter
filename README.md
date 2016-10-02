### Introduction

Python library to slot items into pre-defined slots.

### Why?

Scratching my own itch.

Had written a function that takes a list of time ranges, a list of times (seconds) and slots them in the appropriate ranges. Abstracted that out into a module.

### An interesting use case

Talk to your monitoring setup's API. Find out how many services are in warning/critical state and for how long. Keep on collecting, slotting (use this module) and plotting this data for X hours. You get an insight into your alert response times.

e.g. X services were in WARNING state for 1-2 hours.

[This](http://saurabh-hirani.github.io/writing/2016/10/03/sla-metrics) blog post describes the above scenario and links to the graphite plugin which does the deed.

### Installation

* stable release: ```pip install slotter```
* Install the ongoing development package:

  ```
  git clone https://github.com/saurabh-hirani/slotter
  cd slotter
  sudo ./install.sh
  ```
* Remove files installed by ```./install.sh```

  ```
  sudo ./uninstall.sh
  ```

### Examples

- Import the slotter module

  ```
  import slotter
  ```

- Create that which will slot items

  ```
  s = slotter.create()
  ```

- Add slots which will hold items

  ```
  s.add_slot(1, 10)
  >>> <slotter.slotter.Slot at 0x0>

  # adding same slot is idempotent
  s.add_slot(1, 10)
  >>> <slotter.slotter.Slot at 0x0>

  s.add_slot(10, 20)
  >>> <slotter.slotter.Slot at 0x2>

  # an optional description to label the slots
  slot = s.add_slot(20, 30, 'twenty-to-thirty')
  >>> <slotter.slotter.Slot at 0x3>

  slot.start
  >>> 20

  slot.end
  >>> 30
  ```

- Dump the empty slot objects. Returns a sorted list. Slots are sorted on the sum of start + end i.e. slot(1, 10) <  slot(10, 20)

  ```
  s.get_slots()
  >>> [<slotter.slotter.Slot object at 0x0>, <slotter.slotter.Slot object at 0x1>, <slotter.slotter.Slot at 0x2>]
  ```

- Dump in human readable form (if you fancy json dumps)

  ```
  s.dump()
  >>> {'1-10': [], '10-20': [], 'twenty-to-thirty': []} # printed 'twenty-to-thirty' because we labelled (20, 30) range explicitly
  ```

- Add items. Item are in the format - (item_name, its_slot_value). Slots chosen as per item_value >= slot.start and item_value < slot.end. Output is the slot in which items are added.

  ```
  s.add_item('item1', 5)
  >>> <slotter.slotter.Slot object at 0x1>

  s.add_item('item2', 20)
  >>> <slotter.slotter.Slot object at 0x3>

  slot = s.add_item('item3', 11)
  >>> <slotter.slotter.Slot object at 0x2>

  # add same item again is idempotent
  slot = s.add_item('item3', 11)
  >>> <slotter.slotter.Slot object at 0x2>

  # 0x2 == slot with range (10,20) - not explicitly labelled => label == 'start-end'
  str(slot)
  >>> '10-20'
  ```

- Get slots containing an item:

  ```
  s.get_slots()
  >>> [<slotter.slotter.Slot object at 0x1>, <slotter.slotter.Slot object at 0x0>, <slotter.slotter.Slot at 0x2>]

  s.get_slots('item1', 5)
  >>> <slotter.slotter.Slot object at 0x1>

  str(s.get_slots('item1', 5))
  >>> '1-10'

  str(s.get_slots('item2', 20))
  >>> 'twenty-to-thirty'
  ```

- Get all the slotted items. Returns a sorted list. Items are sorted on the basis of their values i.e. ('item5', 10) < ('item4', 50)

  ```
  # get all items
  s.get_items()
  >>> [('item1', 5), ('item3', 11), ('item2', 20)]

  # get items in a specific range
  s.get_items(start=1, end=10)
  >>> [('item1', 5)]

  # can also pass in a slot object
  s.get_items(s.slots()[0])
  >>> [('item3', 11)]
  ```

- Map slots to items

  ```
  s.slot_items
  >>> {<slotter.slotter.Slot at 0x1>: sortedset([('item3', 11)]),
  >>>  <slotter.slotter.Slot at 0x0>: sortedset([('item1', 5)]),
  >>>  <slotter.slotter.Slot at 0x2>: sortedset([('item2', 20)])}
  ```

- Dump slot_items in human readable form

  ```
  s.dump()
  >>> {'1-10': [('item1', 5)],
       '10-20': [('item3', 11)],
       'twenty-to-thirty': [('item2', 20)]}
  ```

- Map items to slots

  ```
  s.item_slots
  >>> {('item1', 5): <slotter.slotter.Slot at 0x7fb7805c2c90>,
       ('item2', 20): <slotter.slotter.Slot at 0x7fb7805c2d90>,
       ('item3', 11): <slotter.slotter.Slot at 0x7fb7805c2c50>}
  ```

- Dump item_slots in human readable form

  ```
  s.dump(reverse=True)
  >>> {"('item1', 5)": '1-10',
   "('item2', 20)": 'twenty-to-thirty',
   "('item3', 11)": '10-20'}
  ```

- 'Tie it all together' use case - Find the no. of items beyond a particular slot.

  ```
  import slotter

  s = slotter.create()

  s.add_slot(30, 60, '30-60 minutes')

  s.add_slot(10, 30, '10-30 minutes')

  s.add_slot(60, 90, '60-90 minutes')

  s.add_slot(1, 10, '1-10 minutes')

  s.add_item('item1', 23)

  s.add_item('item2', 10)

  s.add_item('item3', 15)

  s.add_item('item4', 71)

  s.add_item('item5', 54)

  s.add_item('item6', 19)

  s.add_item('item7', 44)

  print [str(x) for x in s.get_slots()]
  >>> ['1-10 minutes', '10-30 minutes', '30-60 minutes', '60-90 minutes']

  print [x for x in s.get_items()]
  >>> [('item2', 10), ('item3', 15), ('item6', 19), ('item1', 23), ('item7', 44), ('item5', 54), ('item4', 71)]

  all_slots = s.get_slots()

  target_slot = s.get_slots('item2', 10)

  target_slot_idx = all_slots.index(target_slot)

  print [s.get_items(x) for x in all_slots[target_slot_idx + 1:]]
  >>> [[('item7', 44), ('item5', 54)], [('item4', 71)]]

  print [len(s.get_items(x)) for x in all_slots[target_slot_idx + 1:]]
  >>> [2, 1]

  print sum((len(s.get_items(x)) for x in all_slots[target_slot_idx + 1:]))
  >>> 3
  ```

- See more code examples in the ```slotter/tests/``` directory
