import csv #imports this library to deal with csv files 

class Item:
  pay_rate = 0.8 # regarding 20% discount
  all = []

  def __init__(self, name: str, price: float, quantity = 0):
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

  # To read the data from CSV files, and instantiate the instances in a generic way
  @classmethod
  def instantiate_from_csv(cls):
  # In each method we design, we need to receive at least one parameter that will be passed as the instance itself.
  # The problem here is we are not going to have any instances on our hand to call this method from the instance, 
  # because this method is actually designed for instantiating the object itself. Therefore, this method can't be called from an instance.
  # To solve this: convert this method to a class method. A class method is a method that could be accessed from the class level only. (Item.{methodName})
  # Since it's a class method, then we use the declarator: @classmethod and instead of (self) we have: (cls) -> cls stands for class 
    with open('items.csv', 'r') as f: # Now we use a context manager to read the csv file, and since they're located in the same location we just say the filename and with persission'r' because we're just going to read this
      reader = csv.DictReader(f) # Converts it to a python dictionary and pass in the content of the file
      items = list(reader) # Converts it to a list

    # To instantiate:    
    for item in items:
      Item(
        name = item.get('name'), # type: ignore
        price = float(item.get('price')), # type: ignore
        quantity = int(item.get('quantity')), # type: ignore
      )
  
  # If you look after at the color of the received parameter ('self') below after typing @staticmethod, turned into a color that we're familiar with because that's like a regular parameter that wereceive.
  # It means that the static methods are never sending (in the background) the instance as a first argument and that's unlike the class method.
  # The class method sending the class reference as a first argument and that's why we had to receive the cls.
  # But with static methods we never send the object as the first argument. that is why we should relate to the static method like a regular function that just receives parameters like we are familiar with isolated functions
  @staticmethod
  def is_integer(num):
    # We'll count out the decimals that are point zero; e.g. 5.0
    #tance do What isinses, is to check if the received parameter is an instance of a float or an integer.
    if isinstance(num, float):
      return num.is_integer
    elif isinstance(num, int):
      return True
    else:
      return False

  def __repr__(self):
    return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"


# How to access a static method
"""
print(Item.is_integer(1000.0))

Item.instantiate_from_csv()
print(Item.all)
"""

class Phone(Item):
  """
  Using inheritence, we don't what code duplication. that's why we need to use the super function in the child class.
  Super function will allow us to havr the attributes access from the parent classes. and therefore, we will be able to fully
  implement the best practices in inheritence. by calling the super() we have access to all the attributes and methods in the parent class.
  """
  def __init__(self, name: str, price: float, quantity = 0, broken_phones=0):
    super().__init__(
      name, price, quantity
    )
    assert broken_phones >= 0, f"Broken phones {broken_phones} for {name} should be greater than or equal to zero."
    self.broken_phones = broken_phones

# If we have some broken phones, then we can't use the Item class. so we need a separate class that can inherit from the item class, but also has an option for
# calculating broken phones, if there are any.
phone1 = Phone("jscPhonev10", 500, 5, 1)
print(phone1.calculate_total_price())
phone2 = Phone("jscPhonev20", 700, 5, 2)
print(phone2.calculate_total_price())

print(Item.all)
print(Phone.all)
