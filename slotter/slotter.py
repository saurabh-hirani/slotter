# -*- coding: utf-8 -*-
""" The main class of slotter """

from blist import sortedset
from slot import Slot
from item import Item
import utils

class Slotter(object):
  """ Slotter class """

  def __init__(self, slots=None):
    """ Create the slots object """
    self.slots = sortedset(key=lambda x: x.start + x.end)
    if slots is not None:
      for slot in slots:
        self.slots.add(slot)
    self.verbose = False

    self.slot_items = {}
    self.item_slots = {}

    # prevent duplicate slots and items by remembering their string rep
    self._str_slots = {}
    self._str_items = {}

    self.items = sortedset(key = lambda x: x.value)

  def create_slot(self, start, end, desc=None):
    """ Just create a slot object - don't add it """
    return Slot(start, end, desc)

  def create_item(self, item):
    """ Just create a item object - don't slot it """
    return Item(item)

  def add_slot(self, start, end, desc=None):
    """ Define start, end for a slot """
    slot_obj = self.create_slot(start, end, desc)

    if str(slot_obj) in self._str_slots:
      return self._str_slots[str(slot_obj)]

    self.slots.add(slot_obj)
    self._str_slots[str(slot_obj)] = slot_obj

    return slot_obj

  def remove_slot(self, slot_obj):
    """ Define start, end for a slot """
    if slot_obj not in self.slots:
      return False
    for item in slot_obj.items:
      self.remove_item(item)
    self.slots.remove(slot_obj)
    del self._str_slots[str(slot_obj)]
    return True

  def _find_slot(self, item):
    """ Find the slot to which the item belongs """
    for slot in self.slots:
      if slot.can_accomodate(item):
        return slot
    return None

  def _find_item_by_name_value(self, name, value):
    """ Find item by its name and value """
    key = '%s-%s' % (str(name), str(value))
    if key in self._str_items:
      item = self._str_items[key]
      return item
    return None

  def add_item(self, item):
    """ Slot the item """
    if not isinstance(item, Item):
      item = self.create_item(item)

    if str(item) in self._str_items:
      return self._str_items[str(item)]

    slot = self._find_slot(item)
    if slot is None:
      if self.verbose:
        print 'ERROR: Did not find a slot - existing slots - %s' % self.dump().keys()
      return False

    if slot not in self.slot_items:
      self.slot_items[slot] = sortedset(key=lambda x: x.value)

    self.items.add(item)
    slot.items.add(item)
    self._str_items[str(item)] = item

    self.slot_items[slot].add(item)
    self.item_slots[item] = slot

    item.slot = slot

    return item

  def remove_item(self, item=None, name=None, value=None):
    """ Remove the slotted item """
    if item is None and name is not None and value is not None:
      item = self._find_item_by_name_value(name, value)

    if item is None or item not in self.item_slots:
      return False

    slot = self.item_slots[item]

    slot.items.remove(item)
    self.slot_items[slot].remove(item)
    del self._str_items[str(item)]

    self.items.remove(item)
    del self.item_slots[item]

    return True

  def dump(self, reverse=False):
    """ Dump the slotted ds """
    ds = {}
    if not reverse:
      for slot in self.slots:
        str_slot = str(slot)
        if str_slot not in ds:
          ds[str_slot] = []
        if slot in self.slot_items:
          items = self.slot_items[slot]
          for item in items:
            ds[str_slot].append((item.name, item.value))
      return ds

    for item in self.item_slots.keys():
      ds[str(item)] = str(self.item_slots[item])

    return ds

  def get_slot(self, item=None, name=None, value=None):
    """ Get slots """
    if item is None and name is not None and value is not None:
      item = self._find_item_by_name_value(name, value)
    if not isinstance(item, Item):
      item = self.create_item(item)
    if item is None:
      return None
    if str(item) in self._str_items:
      return self.item_slots[self._str_items[str(item)]]
    return None

  def get_items(self, slot=None, start=None, end=None):
    """ Get slot items """
    if slot is None and start is None and end is None:
      return list(self.items)

    if slot is not None:
      if slot in self.slot_items:
        return list(self.slot_items[slot])
    else:
      if start is not None and end is not None:
        key = '%s-%s' % (str(start), str(end))
        if key in self._str_slots:
          slot = self._str_slots[key]
          return list(self.slot_items[slot])

    return []
