import pytest
import slotter
from slotter.slotter import SlotterException

@pytest.fixture(scope='session')
def slotter_obj():
  """ Return basic slotter object """
  return slotter.Slotter()

def test_create(slotter_obj):
  assert isinstance(slotter_obj, slotter.Slotter)

def test_numerical_slots(slotter_obj):
  added = slotter_obj.add_slot(1, 10)
  assert added
  assert slotter_obj.slots[0].start == 1
  assert slotter_obj.slots[0].end == 10
  assert str(slotter_obj.slots[0]) == '1-10'

  added = slotter_obj.add_slot(10, 20)
  assert added
  assert slotter_obj.slots[1].start == 10
  assert slotter_obj.slots[1].end == 20
  assert str(slotter_obj.slots[1]) == '10-20'

def test_add_item(slotter_obj):
  slot = slotter_obj.add_item(12)
  assert 12 in slot

  slot = slotter_obj.add_item(-1)
  assert slot is None

def test_duplicate_slots():
  obj = slotter.Slotter()

  obj.add_slot(1,10)
  assert len(obj.slots) == 1

  obj.add_slot(1,10)
  assert len(obj.slots) == 1

def test_duplicate_items():
  obj = slotter.Slotter()

  obj.add_slot(1,10)

  obj.add_item(5)
  assert len(obj.items) == 1

  obj.add_item(5)
  assert len(obj.items) == 1

def test_slotted(slotter_obj):
  assert slotter_obj.slotted(12)
  assert not slotter_obj.slotted(11)
