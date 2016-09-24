Slot things into buckets.

### Introduction

Slotter provides a library to bucketize items into pre-defined slots

### Installation - TODO

### Basic usage examples

- Create slotter

  ```
  import slotter

  slots = slotter.create()
  ```

- Define the slots:

  ```
  slots.add(start=1, end=10)  # >= 1 and < 10

  slots.add(start=10, end=20) # >= 10 and < 20

  slots.add(start=20) # >= 10 to infinity
  ```

- Define the slots during creation itself:

  ```
  import slotter

  slots = slotter.create([(1, 10), (10, 20), (20,)])
  ```

- Add elements:

  ```
  low, high = slots.put(5) # slots and returns True

  print low
  >> 1

  print high
  >> 10

  low, high = slots.put(10)

  print low
  >> 10

  low, high = slots.put(15)

  low, high = slots.put(-1) # returns (None, None)
  ```

- Dump the slotted elements

  ```
  slots.dump()
  {
    (1,10): [5]
    (10,20): [10, 15]
  }

  slots.dump(keystrs=True)
  {
    '1-10': [5]
    '10-20': [10, 15]
  }

  slots.dump(reverse=True)

  {
    '5': (1,10),
    '10': (10, 20),
    '15': (10, 20),
    '150': (20, None),
  }
  ```
