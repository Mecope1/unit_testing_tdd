import pytest

from checkout_kata import checkout_kata

# First test to determine if class can be called. Is removed since later testes make it redundant.
# def test_checkout_kata():
#    co = checkout_kata()

@pytest.fixture()
def checkout():

    checkout1 = checkout_kata()
    return checkout1


# # Second test to see if method can be called. Removed because test 4 makes redundant
# def test_add_item_price(checkout):
#     checkout.add_item_price("watermelon", 1)
#
#
# # Third test. Removed because test 4 makes redundant
# def test_add_item(checkout):
#     checkout.add_item("watermelon")


# Fourth test.
def test_can_calc_total(checkout):

    checkout.add_item_price("watermelon", 1)
    checkout.add_item("watermelon")
    assert checkout.calc_total() == 1

# Fifth test.
def test_multiple_items_total(checkout):
    checkout.add_item_price("watermelon", 1)
    checkout.add_item_price("radish", 2)
    checkout.add_item("watermelon")
    checkout.add_item("radish")
    assert checkout.calc_total() == 3
