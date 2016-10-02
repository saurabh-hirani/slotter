import itertools
import pytest
import slotter
from slotter.slotter import SlotterException, Slot

@pytest.fixture(scope='session')
def slotter_obj():
  """ Return basic slotter object """
  return slotter.Slotter()

def test_create(slotter_obj):
  """ Test slotter creation """
  assert isinstance(slotter_obj, slotter.Slotter)

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
  slot1 = slotter_obj.add_item('five', 5)
  assert slot1

  slotter_obj.add_item('four', 4)

  slot2 = slotter_obj.add_item('fifteen', 15)
  assert slot2

  slot = slotter_obj.add_item('neg1', -1)
  assert slot is False

  items = slotter_obj.get_items()
  assert items == [('four', 4), ('five', 5), ('fifteen', 15)]

  items = slotter_obj.get_items(slot1)
  assert items == [('four', 4), ('five', 5)]

  items = slotter_obj.get_items(start=1, end=10)
  assert items == [('four', 4), ('five', 5)]

def test_remove_item(slotter_obj):
  """ Test adding item to a slot """
  slot = slotter_obj.add_item('nineteen', 19)
  assert slot
  removed = slotter_obj.remove_item('nineteen', 19)
  assert removed

  slot = slotter_obj.add_item('four', 4)
  assert slot
  removed = slotter_obj.remove_item('four', 4)
  assert removed

def test_get_slots(slotter_obj):
  """ Test getting an item's slot """
  all_slots = slotter_obj.get_slots()
  assert [str(x) for x in all_slots] == ['1-10', '10-20', 'third']

  slot = slotter_obj.get_slots('fifteen', 15)
  assert slot.start == 10
  assert slot.end == 20

  slot = slotter_obj.get_slots('thousand', 1000)
  assert slot == []

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

  obj.add_slot(1,10)

  obj.add_item('five', 5)
  assert len(obj.item_slots.keys()) == 1

  obj.add_item('five', 5)
  assert len(obj.item_slots.keys()) == 1

def test_dump(slotter_obj):
  """ Test dumping slotter object """
  output = slotter_obj.dump()
  assert '1-10' in output.keys()
  assert '10-20' in output.keys()
  assert 'third' in output.keys()

  assert ('five', 5) in list(itertools.chain(*output.values()))
  assert ('fifteen', 15) in list(itertools.chain(*output.values()))

  output = slotter_obj.dump(reverse=True)
  assert "('five', 5)" in output.keys()
  assert "('fifteen', 15)" in output.keys()
  assert '1-10' in output.values()
  assert '10-20' in output.values()
