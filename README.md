### Introduction

Python library to slot items into pre-defined slots.

A slotter slots items.

An item can be a primitive (int, str) or an object which either has the attributes **name, value** or implements the methods **get_item_name, get_item_value**

A slot has a start and an end value e.g start=1 end=10 for holding items >= 1 and < 10. It can hold one or more items. An item can belong to only one slot.

A slotter can add/remove items/slots and can also search items/slots for slots/items.

### Play me a sample run / Slot Terminator, Pacific Rim and Transformers

<a href='https://asciinema.org/a/8mm8f0qqurk4rqt90drkpvp1b?autoplay=1' target='_blank'><img src='https://asciinema.org/a/8mm8f0qqurk4rqt90drkpvp1b.png'></a>

### Why?

Scratching my own itch.

Had written a function that takes a list of time ranges, a list of times (seconds) and slots them in the appropriate ranges. Abstracted that out into a module.

### An interesting use case

Talk to your monitoring setup's API. Find out how many services are in warning/critical state and for how long. Keep on collecting, slotting (use this module) and plotting this data for X hours. You get an insight into your alert response times.

e.g. X services were in WARNING state for 1-2 hours.

[This](http://saurabh-hirani.github.io/writing/2016/10/03/sla-metrics) blog post describes the above scenario and links to the graphite plugin which does the deed.

### Installation

* To install a stable release:

  ```pip install slotter```

* To install the development package:

  ```
  git clone https://github.com/saurabh-hirani/slotter
  pip install -r requirements.txt
  cd slotter
  sudo ./install.sh
  ```
* Remove files installed by ```./install.sh```

  ```
  sudo ./uninstall.sh
  ```

### Usage

* Sample code present in [sample.py](https://github.com/saurabh-hirani/slotter/blob/master/slotter/sample.py)

* If you have ```slotter``` installed:

  ```
  >>> import inspect, slotter.sample
  >>> print inspect.getsource(slotter.sample.main)
  # the sample code
  >>> slotter.sample.main()
  # sample code run output
  ```

* Tests cover a lot of sample code - [test_slotter.py](https://github.com/saurabh-hirani/slotter/blob/master/slotter/tests/test_slotter.py)
