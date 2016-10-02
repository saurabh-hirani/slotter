# -*- coding: utf-8 -*-
""" The main class of slotter """

from blist import sortedset

class SlotterException(Exception):
  pass

class Slot(object):
  """ That which contains items """
  def __init__(self, start, end, desc=None):
    if start > end or start == end:
      raise SlotterException('ERROR: Invalid start - %s, end - %s' % (start, end))

    self.start = start
    self.end = end
    if desc is None:
      desc = '%s-%s' % (str(self.start), str(self.end))
    self.desc = desc

  def __str__(self):
    return self.desc

  def can_accomodate(self, item):
    if item >= self.start and item < self.end:
      return True
    return False

class Slotter(object):
  """ Slotter class """

  def __init__(self, slots=None):
    """ Create the slots object """
    if slots is not None:
      self.slots = sortedset(slots)
    else:
      self.slots = sortedset()
    self._str_slots = {}
    self.items = sortedset()
    self.item_slots = {}
    self.slot_items = {}

  def create_slot(self, start, end, desc=None):
    """ Just create a slot object - don't add it """
    return Slot(start, end, desc)

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
    self.slots.remove(slot_obj)
    del self._str_slots[str(slot_obj)]
    return True

  def _find_slot(self, item):
    """ Find the slot to which the item belongs """
    for slot in self.slots:
      if slot.can_accomodate(item):
        return slot
    return None

  def add_item(self, item):
    """ Slot the item """

    if item in self.item_slots:
      return self.item_slots[item]

    slot = self._find_slot(item)
    if slot is None:
      return False

    if slot not in self.slot_items:
      self.slot_items[slot] = sortedset()

    self.slot_items[slot].add(item)
    self.item_slots[item] = slot
    self.items.add(item)

    return self.item_slots[item]

  def remove_item(self, item):
    """ Remove the slotted item """
    if item not in self.item_slots:
      return False
    self.slot_items[self.item_slots[item]].remove(item)
    self.items.remove(item)
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
          ds[str_slot].extend(self.slot_items[slot])
      return ds

    for item in self.item_slots.keys():
      ds[str(item)] = str(self.item_slots[item])

    return ds

  def get_slots(self, item=None):
    """ Get the slot of an item """
    if item is None:
      return list(self.slots)
    if item in self.item_slots:
      return self.item_slots[item]
    return []

  def get_items(self, slot=None, start=None, end=None):
    """ Get all items """
    if slot is None and start is None and end is None:
      return list(self.items)

    if slot is not None:
      return list(self.slot_items[slot])
    else:
      if start is not None and end is not None:
        key = '%s-%s' % (str(start), str(end))
        return list(self.slot_items[self._str_slots[key]])
    return []
