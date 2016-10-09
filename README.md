### Introduction

Python library to slot items into pre-defined slots.

A slotter slots items.

An item can be a primitive (int, str) or an object which either has the attributes **name, value** or implements the methods **get_item_name, get_item_value**

A slot can hold one or more item. An item can belong to only one slot.

A slotter can add/remove items/slots and can also search items/slots for slots/items.

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

### Usage

  ```
  >>> import inspect, slotter.sample
  >>> slotter.sample.__file__
  # the location of the sample code
  >>> print inspect.getsource(slotter.sample.main)
  # the sample code
  >>> slotter.sample.main()
  # sample code run output
  ```

- More code in ```slotter/tests``` dir
