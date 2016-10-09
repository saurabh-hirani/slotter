# -*- coding: utf-8 -*-
""" Shared utils for Slotter """

VALID_DERIVABLES = set([str, int, float])

class SlotterException(Exception):
  pass

def derive_item_value(item):
  """ For non user defined objects find their values """
  try:
    return getattr(item, 'value')
  except AttributeError as e:
    pass

  try:
    return getattr(item, 'get_item_value')()
  except AttributeError as e:
    pass

  for derivable_obj in VALID_DERIVABLES:
    if isinstance(item, derivable_obj):
      func = 'get_%s_value' % derivable_obj.__name__
      return globals()[func](item)


  raise SlotterException('Cannot derive item value - %s' % str(item))
