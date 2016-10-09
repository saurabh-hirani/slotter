import string
import itertools
import pytest
import slotter

from slotter.slotter import Slotter
from slotter.utils import SlotterException
from slotter.slot import Slot
from slotter.item import Item

class SampleItemClass1(object):
  """ A sample item class """
  def __init__(self, name, value):
    self.name = name
    self.value = value

class SampleItemClass2(object):
  """ A sample item class """
  def __init__(self, name, value):
    self.new_name = name
    self.new_value = value

  def get_item_name(self):
    """ Return item name """
    return self.new_name

  def get_item_value(self):
    """ Return item name """
    return self.new_value

def test_item_object():
  item1 = Item(name='this', value=10)
  assert item1.name == 'this'
  assert item1.value == 10

  obj = SampleItemClass1('this', 10)
  item2 = Item(obj=obj)
  assert item2.name == 'this'
  assert item2.value == 10
  assert item2.obj == obj

  obj = SampleItemClass2('this', 10)
  item3 = Item(obj=obj)
  assert item3.name == 'this'
  assert item3.value == 10
  assert item3.obj == obj

  item4 = Item(10)
  assert str(item4) == '10-10'

  item5 = Item(string.ascii_lowercase[:5])
  assert str(item5) == 'abcde-5'

@pytest.fixture(scope='session')
def slotter_obj():
  """ Return basic slotter object """
  return Slotter()

def test_create(slotter_obj):
  """ Test slotter creation """
  assert isinstance(slotter_obj, Slotter)

def test_create_slot(slotter_obj):
  """ Test slotter slot creation """
  with pytest.raises(SlotterException):
    slot_obj = slotter_obj.create_slot(100, 10)

  with pytest.raises(SlotterException):
    slot_obj = slotter_obj.create_slot(1, 1)

  slot_obj = slotter_obj.create_slot(100, 200)
  assert slot_obj.start == 100
  assert slot_obj.end == 200

def test_add_slot(slotter_obj):
  """ Test slot creation """
  slot_obj = slotter_obj.add_slot(20, 30, 'third')
  assert slot_obj

  slot_obj = slotter_obj.add_slot(10, 20)
  assert slot_obj

  slot_obj = slotter_obj.add_slot(1, 10)
  assert slot_obj

def test_remove_slot(slotter_obj):
  """ Test slot removal """
  slot_obj = slotter_obj.add_slot(30, 40)
  assert slot_obj

  removed = slotter_obj.remove_slot(slot_obj)
  assert removed

  removed = slotter_obj.remove_slot(Slot(100,200))
  assert removed is False

def test_add_item(slotter_obj):
  """ Test adding item to a slot """
  item1 = slotter_obj.add_item(string.ascii_lowercase[:5])
  assert item1
  assert [] == [str(x) for x in item1.get_siblings()]

  item2 = slotter_obj.add_item(string.ascii_lowercase[:4])

  item3 = slotter_obj.add_item(string.ascii_lowercase[:15])
  assert item3

  assert ['abcde-5'] == [str(x) for x in item2.get_siblings()]
  assert ['abcd-4'] == [str(x) for x in item1.get_siblings()]

  item4 = slotter_obj.add_item(-1)
  assert item4 is False

  items = slotter_obj.get_items()

  assert ['abcd', 'abcde', 'abcdefghijklmno'] == [i.name for i in items]
  assert [4, 5, 15] == [i.value for i in items]

  items = slotter_obj.get_items(start=1, end=10)
  assert ['abcd', 'abcde'] == [i.name for i in items]

def test_remove_item(slotter_obj):
  """ Test adding item to a slot """
  item = slotter_obj.add_item(string.ascii_lowercase[:19])
  assert item

  removed = slotter_obj.remove_item(item=item)
  assert removed

  item = slotter_obj.add_item(string.ascii_lowercase[:4])

  removed = slotter_obj.remove_item(name='abcd', value=4)
  assert removed

  removed = slotter_obj.remove_item(name='abcdx', value=4)
  assert not removed

def test_get_slot(slotter_obj):
  """ Test getting an item's slot """
  all_slots = slotter_obj.slots
  assert [str(x) for x in all_slots] == ['1-10', '10-20', 'third']

  slot = slotter_obj.get_slot(string.ascii_lowercase[:15])
  assert slot.start == 10
  assert slot.end == 20

  slot = slotter_obj.get_slot('thousand')
  assert slot == None

def test_duplicate_slots():
  """ Test adding same slot twice """
  obj = slotter.Slotter()

  obj.add_slot(1,10)
  assert len(obj.slots) == 1

  obj.add_slot(1,10)
  assert len(obj.slots) == 1

def test_duplicate_items():
  """ Test adding same item twice """
  obj = slotter.Slotter()

  slot_obj = obj.add_slot(1,10)

  item = obj.add_item('five')
  assert item.slot == slot_obj
  assert len(obj.item_slots.keys()) == 1

  obj.add_item('five')
  assert len(obj.item_slots.keys()) == 1

def test_dump(slotter_obj):
  """ Test dumping slotter object """
  output = slotter_obj.dump()
  assert '1-10' in output.keys()
  assert '10-20' in output.keys()
  assert 'third' in output.keys()

  assert (string.ascii_lowercase[:5], 5) in list(itertools.chain(*output.values()))
  assert (string.ascii_lowercase[:15], 15) in list(itertools.chain(*output.values()))

  output = slotter_obj.dump(reverse=True)
  assert (string.ascii_lowercase[:5], 5)  in output.keys()
  assert (string.ascii_lowercase[:15], 15)  in output.keys()
  assert '1-10' in output.values()
  assert '10-20' in output.values()
