# -*- coding: utf-8 -*-
""" The main class of slotter """

class SlotterException(Exception):
  pass

class Slot(object):
  def __init__(self, start, end):
    self.start = start
    self.end = end

  def __str__(self):
    return '%s-%s' % (str(self.start), str(self.end))

  def __contains__(self, key):
    if key >= self.start and key < self.end:
      return True
    return False

  def contains(self, key):
    return key in self

class Slotter(object):
  """ Slotter class """

  def __init__(self, slots=None):
    """ Create the slots object """
    if slots is not None:
      self.slots= slots
    else:
      self.slots= []
    self.items = []
    self._str_slots = []
    self._str_items = []
    self.item_slots = {}
    self.slot_items = {}

  def add_slot(self, start, end):
    """ Define start, end for a slot """
    slot_obj = Slot(start, end)

    if str(slot_obj) in self._str_slots:
      return True

    self.slots.append(slot_obj)
    self._str_slots.append(str(self.slots[-1]))

    return True

  def __contains__(self, key):
    """ Check if value already added """
    return key in self.item_slots

  def find_slot(self, item):
    """ Find the slot to which the item belongs """
    for slot in self.slots:
      if item in slot:
        return slot
    return None

  def add_item(self, item):
    """ Slot the item """

    if str(item) in self._str_items:
      return self.item_slots[item]

    if item not in self:
      slot = self.find_slot(item)
      if slot is None:
        return None

      if slot not in self.slot_items:
        self.slot_items[slot] = item

      self.item_slots[item] = slot

    self.items.append(item)
    self._str_items.append(str(self.items[-1]))

    return self.item_slots[item]

  def slotted(self, item):
    """ Check if the number is slotted """
    return item in self.items

  def dump(self, reverse=False):
    """ Dump the slotted ds """
    ds = {}
    if not reverse:
      for slot in self.slot_items:
        print slot
        ds[str(slot)] = str(self.slot_items[slot])
      return ds

    for item in self.item_slots:
      slots = self.item_slots[item]
      ds[str(item)] = [str(s) for s in self.item_slots[item]]

    return ds
