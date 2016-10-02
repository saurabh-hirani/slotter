### Introduction

Python library to slot items into pre-defined slots.

### Why?

Scratching my own itch.

Had written a function that takes a list of time ranges, a list of times (seconds) and slots them in the appropriate ranges. Abstracted that out into a module.

### An interesting use case

Talk to your monitoring setup's API. Find out how many services are in warning/critical state and for how long. Keep on collecting, slotting (use this module) and plotting this data for X hours. You get an insight into your alert response times.

e.g. X services were in WARNING state for 1-2 hours.

Watch for a blog post demoing this within a week on [my blog](http://saurabh-hirani.github.io/writing/)

### Installation - TODO

### Examples

- If you want to run all of the following examples in one shot:

  ```
  $ python sample.py
  ```

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
  s.add_slot(1,10)
  s.add_slot(10,20)
  ```

- Add items

  ```
  # Add items
  s.add_item(5)
  s.add_item(11)
  s.add_item(15)
  ```

- Check slots, items, etc.

  ```
  print s.slotted(5)
  >> True
  ```

- Find the target slot of an item:

  ```
  target_slot = s.find_slot(5)
  print str(target_slot.start)
  >> 1
  print str(target_slot.end)
  >> 10
  print str(target_slot)
  >> 1-10
  ```

  ```
  target_slot = s.find_slot(11)
  print str(target_slot.start)
  >> 10
  print str(target_slot.end)
  >> 20
  print 15 in target_slot
  >> True
  ```

- Get all slots

  ```
  print s.slots
  >> [<slotter.slotter.Slot object at 0x7f1af93a7a90>, <slotter.slotter.Slot object at 0x7f1af93a7b50>]
  ```

- Get all items

  ```
  print s.items
  >> [5, 11, 15]
  ```

- Map slots to items

  ```
  print s.slot_items
  >> {<slotter.slotter.Slot object at 0x7f1af93a7a90>: [5], <slotter.slotter.Slot object at 0x7f1af93a7b50>: [11, 15]}
  ```

- Map items to slots

  ```
  print s.item_slots
  >> {11: <slotter.slotter.Slot object at 0x7f1af93a7b50>, 5: <slotter.slotter.Slot object at 0x7f1af93a7a90>, 15: <slotter.slotter.Slot object at 0x7f1af93a7b50>}
  ```

- json dump slot_items map:

  ```
  import json
  print json.dumps(s.dump(), indent=2)
  {
    "1-10": [
        5
      ],
    "10-20": [
        11,
        15
      ]
  }
  ```

- json dump item_slots map:

  ```
  import json
  print json.dumps(s.dump(reverse=True), indent=2)
  {
    "11": "10-20",
    "15": "10-20",
    "5": "1-10"
  }
  ```
