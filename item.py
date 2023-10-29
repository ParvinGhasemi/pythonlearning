import csv

class Item:
  pay_rate = 0.8 # regarding 20% discount
  all = []

  def __init__(self, name: str, price: float, quantity = 0):
    assert price >= 0, f"Price {price} for {name} should be greater than or equal to zaro."
    assert quantity >= 0, f"Quantity {quantity} for {name} should be greater than or equal to zero."
    self.__name = name
    self.__price = price
    self.quantity = quantity
    Item.all.append(self)


  @property
  def price(self):
    return self.__price

  def apply_discount(self):
    self.__price = self.__price * self.pay_rate

  def apply_increment(self, increment_value):
    self.__price = self.__price * (1 + increment_value)

  @property
  def name(self):
    return self.__name

  @name.setter
  def name(self, value):
    if len(value) > 10:
      raise Exception("The name is too long - it should be less than 10 characters.")
    else:
      self.__name = value 

  def calculate_total_price(self):
    return self.__price * self.quantity


  @classmethod
  def instantiate_from_csv(cls): 
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

  def __connect_to_smtp_server(self, smtp_server):
    pass

  def __prepare_email_body(self):
    return f"""
    Hello someone,
    We have {self.name} {self.quantity} times.
    """

  def __send(self):
    pass
  
  def send_email(self):
    self.__connect_to_smtp_server('')
    self.__prepare_email_body()
    self.__send()

