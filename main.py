#Now here we can only stantiate instances. This would be cleaner.
from item import Item
#Here we won't import phone, since we want to keep things simple.

"""
Item.instantiate_from_csv()
print(Item.all)
"""

# look at this example about overriding:
item1 = Item("MyItem", 750)
item1.name = "OtherItem"
print(item1.name)

# But what if we want to restrict the user to change the name attribute one it's been set up at initialization?
# This is a good approach for critical attributes => we create read only attributes. means it can only be set once.
# to declare a read only attribute, we use th @property decorator
print(item1.read_only_name)

