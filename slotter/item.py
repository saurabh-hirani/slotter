# -*- coding: utf-8 -*-
""" Item class """

from utils import SlotterException

VALID_DERIVABLES = set([str, int, float])

def get_str_value(item):
  """ Get string value """
  return len(item)

def get_int_value(item):
  """ Get int value """
  return item

def get_float_value(item):
  """ Get float value """
  return item

class Item(object):
  """ Deafult item representation """
  def __init__(self, obj=None, name=None, value=None):
    """ Create the item to store """
    self.name = None
    self.value = None
    self.slot = None
    self.obj = self

    # try to derive the name and value of the item
    if obj is not None:
      self.obj = obj
      try:
        self.name = getattr(obj, 'name')
        self.value = getattr(obj, 'value')
      except AttributeError as e:
        pass

      try:
        self.name = getattr(obj, 'get_item_name')()
        self.value = getattr(obj, 'get_item_value')()
      except AttributeError as e:
        pass

      for derivable_obj in VALID_DERIVABLES:
        if isinstance(obj, derivable_obj):
          self.name = str(obj)
          self.value = globals()['get_%s_value' % derivable_obj.__name__](obj)

    if name is not None:
      self.name = name

    if value is not None:
      self.value = value

    failed_attrs = []
    for attr in ['name', 'value']:
      if getattr(self, attr) is None:
        failed_attrs.append(attr)

    if failed_attrs:
      failed_attrs_str = ','.join(failed_attrs)
      raise SlotterException('Invalid object - %s. Failed to find - %s' %\
                             (obj, failed_attrs_str))

  def __str__(self):
    """ Print this object as string """
    return '%s-%s' % (self.name, self.value)

  def get_siblings(self):
    """ Get siblings of this object """
    if self.slot is not None:
      all_items = set(self.slot.items)
      return list(all_items - set([self]))
    return []
