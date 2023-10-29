# The first and simplest example for keeping track of items in a store
"""
item1 = 'Phone'
item1_price = 100
item1_quantity = 5
item1_price_total = item1_price * item1_quantity

print(type(item1)) #str
print(type(item1_price)) #int
print(type(item1_quantity)) #int
print(type(item1_price_total)) #int
"""

# Now we instantiate the Item() class and assign attributes to instances
"""
class Item:
  pass

item1 = Item()
item1.name = "Phone"
item1.price = 100
item1.quantity = 5

print(type(item1)) #Item
print(type(item1.name)) #str
print(type(item1.price)) #int
print(type(item1.quantity)) #int
"""

# Now to understand how to create methods and execute them on out instances
"""
class Item:
  def calculate_total_price(self, price, quantity):
    return price * quantity

item1 = Item()
item1.name = "Phone"
item1.price = 100
item1.quantity = 5
print(item1.calculate_total_price(item1.price, item1.quantity))

item2 = Item()
item2.name = "Laptop"
item2.price = 1000
item2.quantity = 3
print(item2.calculate_total_price(item2.price, item2.quantity))
"""

# We don't have a set of rules for the attributes that you want to pass in, in order to instanciate an instance successfully.
# It means as in the previous section, we hardcoded the attributes for each item: item1.name, item1.price, etc.
# It could've been nicer if we declare in the class to have a successful instance, attributes must be passed, otherwise instance can't be created successfully.
# We will learn here about that, using the __init__ method, which is called a 'constructor'
"""
class Item:
  def __init__(self, name, price, quantity):
    self.name = name
    self.price = price
    self.quantity = quantity
  def calculate_total_price(self, price, quantity):
    return price * quantity

item1 = Item("Phone", 100, 5)
total_price = item1.calculate_total_price(item1.price, item1.quantity)

item2 = Item("Laptop", 1000, 3)
item2.calculate_total_price(item2.price, item2.quantity)

print(item1.name)
print(item2.name)
print(item1.price)
print(item2.price)
print(item1.quantity)
print(item2.quantity)
"""

# To define the mandatory and non-mandatory parameters in the constructor
"""
class Item:
  def __init__(self, name, price, quantity=0 ):
    self.name = name
    self.price = price
    self.quantity = quantity

  def calculate_total_price(self):
    return self.price * self.quantity


item1 = Item("Phone", 100, 3)
item2 = Item("Laptop", 1000)

#You can add some more attributes to the specific instantiations, and not to all
item2.has_numpad = False

print(f"Total price for {item1.name} is", item1.calculate_total_price())
print(f"Total price for {item2.name} is", item2.calculate_total_price())
"""

# How to define data type that each value can take? e.g. price can only get integers.
# Data Type Validation

# One way is by using typings in the parameters that you declare inside the init method (the constructor)
"""
class Item:
  def __init__(self, name: str, price: float, quantity=0):
    #if you want to set conditions (e.g. price can't be negative) you can use assert statement 
    # you can also add your own Error messages
    assert price >= 0, f"Price {price} for {name} should be greater than or equal to zaro."
    assert quantity >= 0, f"Quantity {quantity} for {name} should be greater than or equal to zero."
    self.name = name
    self.price = price
    self.quantity = quantity

  def calculate_total_price(self):
    return self.price * self.quantity

    
item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)

print(f"Total price for {item1.name} is", item1.calculate_total_price())
print(f"Total price for {item2.name} is", item2.calculate_total_price())
"""

# How to creat a variable as global (or across all the instances)?
# e.g. when you want to create a sale for your shop and apply some discount for each one of the items
# These are called class attributes (the attributes we were working with till now, were 'instance attributes')
# Class attributes belong to the class itself but can be accessed also from the instance level
"""
class Item:
  pay_rate = 0.8 # if 20% discount is applied

  def __init__(self, name: str, price: float, quantity=0):
    assert price >= 0, f"Price {price} for {name} should be greater than or equal to zaro."
    assert quantity >= 0, f"Quantity {quantity} for {name} should be greater than or equal to zero."
    self.name = name
    self.price = price
    self.quantity = quantity

  def calculate_total_price(self):
    return self.price * self.quantity

    
item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)

# Here we try to access to the reference of the class itself, so we won't create an instance: item();
# But instead we will bring in the reference to the class level itself. To access this attribute:
print(Item.pay_rate)
#how to access a class attribute in an instance level:
print(item1.pay_rate)
print(item2.pay_rate)
# There's a built-in magic attribute(not a magic method!) that you can see all the attrubytes that are belonging to that specific object.
print(Item.__dict__) # All the attributes for the Class level
print(item1.__dict__) # All the attributes for the instance level
"""

# How to apply the discount on the price via a method:
"""
class Item:
  pay_rate = 0.8 # if 20% discount is applied

  def __init__(self, name: str, price: float, quantity=0):
    assert price >= 0, f"Price {price} for {name} should be greater than or equal to zaro."
    assert quantity >= 0, f"Quantity {quantity} for {name} should be greater than or equal to zero."
    self.name = name
    self.price = price
    self.quantity = quantity

  def calculate_total_price(self):
    return self.price * self.quantity
  
  def apply_discount(self):
    self.price = self.price * Item.pay_rate # we can't just say pay_rate, we need to say it's at class level item


item1 = Item("Phone", 100, 1)
item1.apply_discount()
print(item1.price) # it will print 80, because of the 20% discount
"""


# Now we want to apply a different discount just for one item. when we do so, it won't work, because in the apply_discount we have Item.pay_rate
# If we want it to work when we change it at the instance level, to work and have a different discount, we should say: self.pay_rate
"""
class Item:
  pay_rate = 0.8 # if 20% discount is applied

  def __init__(self, name: str, price: float, quantity=0):
    assert price >= 0, f"Price {price} for {name} should be greater than or equal to zaro."
    assert quantity >= 0, f"Quantity {quantity} for {name} should be greater than or equal to zero."
    self.name = name
    self.price = price
    self.quantity = quantity

  def calculate_total_price(self):
    return self.price * self.quantity
  
  def apply_discount(self):
    self.price = self.price * self.pay_rate # we can't just say pay_rate, we need to say it's at class level item


item1 = Item("Phone", 100, 1)
item1.apply_discount()
print(item1.price) # it will print 80, because of the 20% discount

item2 = Item("Laptop", 1000, 3)
item2.pay_rate = 0.7
item2.apply_discount()
print(item2.price) # it'll print: 700
"""

# When shop gets bigger, there will be more items. We need to have a list to access all the items that we have.
# We can create a class attribute to achieve this and add all instances of the class to that list.
"""
class Item:
  pay_rate = 0.8 # regarding 20% discount
  all = []

  def __init__(self, name: str, price: float, quantity: 0):
    assert price >= 0, f"Price {price} for {name} should be greater than or equal to zaro."
    assert quantity >= 0, f"Quantity {quantity} for {name} should be greater than or equal to zero."
    self.name = name
    self.price = price
    self.quantity = quantity
    Item.all.append(self) # 'self' is the instance itself everytime that it's being created. and we add it in the constructor, because we know when we create an instance, the constructor is automatically called.

  def calculate_total_price(self):
    return self.price * self.quantity
  
  def apply_discount(self):
    self.price = self.price * self.pay_rate

  def __repr__(self): # A magic method that represents your object. in this example we want to return a string.
    return f"Item('{self.name}', {self.price}, {self.quantity})"

item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 50)

print(Item.all) # The result will have 5 elements, since we have 5 items till now.
# It'll print the references, but we need to see the objects. so That's why we use the '__repr__' magic method.

# To do something only with one attribute of all your instances (e.g. print only names)
for instance in Item.all:
  print(instance.name)
"""


"""
class Item:
  pay_rate = 0.8 # regarding 20% discount
  all = []

  def __init__(self, name: str, price: float, quantity: 0):
    assert price >= 0, f"Price {price} for {name} should be greater than or equal to zaro."
    assert quantity >= 0, f"Quantity {quantity} for {name} should be greater than or equal to zero."
    self.name = name
    self.price = price
    self.quantity = quantity
    Item.all.append(self)

  def calculate_total_price(self):
    return self.price * self.quantity
  
  def apply_discount(self):
    self.price = self.price * self.pay_rate

  def __repr__(self):
    return f"Item('{self.name}', {self.price}, {self.quantity})"

item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

print(Item.all)
"""

# The problem is that we are keeping the data as code by instantiating those 5 items.
# If we want to add more features, it'd be hard, since the code and the data are in the same file.
# We can create a database, but for now we are keeping it simple and use CSV. it allows the data to be saved in a table structured format.