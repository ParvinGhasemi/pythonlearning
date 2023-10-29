from item import Item


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