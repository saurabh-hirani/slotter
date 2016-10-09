import json
import string
import slotter 

class SampleItemClass():
  def __init__(self, n, v):
    self.name = n
    self.value = v

def main():
  print "--------------------------"
  print "Create slotter"
  s = slotter.Slotter()
  print 'slotter_obj=%s' % s
  print "--------------------------"

  print "--------------------------"
  print "Create slots"
  s1 = s.add_slot(1, 10)
  print 's1.start=%d, s1.end=%d' % (s1.start, s1.end)
  s2 = s.add_slot(10, 20)
  print 's2.start=%d, s2.end=%d' % (s2.start, s2.end)
  print "--------------------------"

  print "--------------------------"
  print "Create items"
  # For strings - item.name == string name, item.value == string length
  item1 = s.create_item('item1')
  print 'item1.name=%s, item1.value=%d, item=%s' % (item1.name, item1.value, str(item1))
  item2 = s.create_item(string.ascii_lowercase[:15])
  print 'item2.name=%s, item2.value=%d, item=%s' % (item2.name, item2.value, str(item2))
  item3 = s.create_item(SampleItemClass('item3', 8))
  print 'item3.name=%s, item3.value=%d, item3.obj=%s' % (item3.name, item3.value, item3.obj)
  print "--------------------------"

  print "--------------------------"
  print "Add items to slots"
  s.add_item(item1)
  print 'item1.slot=%s' % item1.slot
  s.add_item(item2)
  print 'item2.slot=%s' % item2.slot
  s.add_item(item3)
  print 'item3.slot=%s' % item3.slot
  item4 = s.add_item('item4')
  print 'item4.name=%s, item4.value=%d, item=%s' % (item4.name, item4.value, str(item4))
  print 'item4.slot=%s' % item3.slot
  print 'item4.siblings=%s' % ([str(x) for x in item4.get_siblings()])
  item5 = s.add_item(11)
  print 'item5.name=%s, item5.value=%d, item=%s' % (item5.name, item5.value, str(item5))
  print 'item5.slot=%s' % item5.slot
  print 'item5.siblings=%s' % ([str(x) for x in item5.get_siblings()])
  print "--------------------------"

  print "--------------------------"
  print "Add an invalid item - i.e. one which doesn't fit in any slots"
  invalid_item = string.ascii_lowercase[:30]
  print 's.add_item(%s) = %s' % (invalid_item, s.add_item(invalid_item))
  print "--------------------------"

  print "--------------------------"
  print "Get all slots"
  print 'slots=%s' % s.slots
  print "--------------------------"

  print "--------------------------"
  print "Get all items"
  print 'items=%s' % s.items
  print "--------------------------"

  print "--------------------------"
  print "Get items of a particular slot"
  s1 = s.slots[0]
  print 's1.items=%s' % s1.items
  print "Get information about a specific item in that slot"
  i1 = s1.items[0]
  print "s1.first_item.name=%s, s1.first_item.value=%d" % (i1.name, i1.value)
  print "--------------------------"

  print "--------------------------"
  print "slot -> item mapping"
  print s.slot_items
  print "--------------------------"

  print "--------------------------"
  print "item -> slot mapping"
  print s.item_slots
  print "--------------------------"

  print "--------------------------"
  print "Dumpable slot -> item mapping"
  print json.dumps(s.dump(), indent=2)
  print "--------------------------"

  print "--------------------------"
  print "Dumpable item -> slot mapping"
  print json.dumps(s.dump(reverse=True), indent=2)
  print "--------------------------"

  print "--------------------------"
  print "Get slot of a particular item"
  s1 = s.get_slot(item1)
  print 'item1.slot.start=%d, item1.slot.end=%d' % (s1.start, s1.end)
  print "--------------------------"

  print "--------------------------"
  print "Remove an item object"
  print "before - s1.items=%s" % (s1.items)
  s.remove_item(item1)
  print "after - s1.items=%s" % (s1.items)
  print "Add item1 back"
  s.add_item(item1)
  print 'item1.slot=%s' % item1.slot
  print "--------------------------"

  print "--------------------------"
  print "Remove an item by name and value"
  print "before - s1.items=%s" % (s1.items)
  s.remove_item(name='item1', value=5)
  print "after - s1.items=%s" % (s1.items)
  print "--------------------------"

if __name__ == '__main__':
  main()
