#Now here we can only stantiate instances. This would be cleaner.
from item import Item
from phone import Phone
from keyboard import Keyboard

item10 = Item("MyItem", 750)
# item1.name = "OtherItem"
print(item10.name)

# Encapsulation
item10.apply_increment(0.2)
print(item10.price) #900
item10.apply_discount()
print(item10.price) # 720

# Abstraction
item10 = Phone("jscPhone", 1000, 3)

item10.send_email()

# Inheritance
item1 = Phone("jscPhone", 1000, 3)
item1.send_email()

# Polymorphism
name = "Jim"
print(len(name)) #length of the string (counting characters)
some_list = ["some", "name"]
print(len(some_list)) # length of the list (counting elements)
# That's polymorphism in action, a single function does know
# how to handle different kinds of objects as expected.

# Another polymorphism in this project:
item20 = Keyboard("jscKeyboard", 1000, 3)
item20.apply_discount()
print(item20.price) # 800