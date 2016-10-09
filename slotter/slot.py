# -*- coding: utf-8 -*-
""" Slot class """

from utils import SlotterException
from blist import sortedset

class Slot(object):
  """ That which contains items """
  def __init__(self, start, end, desc=None):
    if start > end or start == end:
      raise SlotterException('ERROR: Invalid start - %s, end - %s' % (start, end))

    self.start = start
    self.end = end
    self.items = sortedset(key=lambda x: x.value)

    if desc is None:
      desc = '%s-%s' % (str(self.start), str(self.end))

    self.desc = desc

  def __str__(self):
    return self.desc

  def can_accomodate(self, item):
    if item.value >= self.start and item.value < self.end:
      return True
    return False
