# Why do we use OOP?
Let's go through it with an example:
A store management system that we develop and make it more complicated by every step!
First: tracking the items we have in the store at the moment.

## __init__ method (constructor):
We don't have a set of rules for the attributes that you want to pass in, in order to instanciate an instance successfully.
it means as in the previous section, we hardcoded the attributes for each item: item1.name, item1.price, etc.
it could've been nicer if we declare in the class to have a successful instance, attributes must be passed, otherwise instance can't be created successfully.
we will learn here about that, using the __init__ method, which is called a 'constructor'
Basically, it's a method with a unique name that you need to call it the way it is intentionally, in order to use its special features.
to see what exactly happens in the background:
When you create an instance of a class, python executes this double underscore init function (the constructor) automatically.
it means that after declaring the class, python will run throught he instanctation line, and then it's going to call the actions that are inside this constructor method.

## static method:
Static method should do some work for you that has some logical connections to a class. For example if you want to check if a number is an integer or a float,
then this is a good candidate for creating a static method. because this has some connection to the class that we work with. So it makes sense to check if a price of an item has a decimal point and by saying has a decimal point, I count those out that are point zero.
Static in class methods could look very alike to you. But we will explain the main differences

## static methods vs class methods:
When do we use a static method? a static method should do something that has a relationship with the class, but not something that must be unique per instance.

when a class method? it's created for instantiating instances from some structured data that you own. it also should do something that has a relationship with the class,
but usually those are used to manipulate different structures of data to instantiate objects, like we have done in csv.

main difference between class and static methods are that static methods don't pass the object reference as the first argument


## the @property decorator
if we want an attribute to be read only and can only be set once (at the initialization) and we won't be able to change it later. (for the example, you can take a look at the item.py class.)


## Attribute vs Property
what is the difference between attribute and property?
Attributes and properties are both used to store data in Python. However, there are some key differences between the two.

Attributes are simply variables that are associated with an object. They can be accessed and modified directly.

Properties are special attributes that have getter, setter, and deleter methods associated with them. These methods can be used to control how the property is accessed and modified.

For example, consider the following class:

```
class MyClass:
    name = "My Class"
```
The name variable is an attribute of the MyClass class. It can be accessed and modified directly, as shown in the following code:

```
my_class = MyClass()

# Access the attribute
print(my_class.name)

# Modify the attribute
my_class.name = "New Name"

# Access the attribute again
print(my_class.name)
```

Output:
```
My Class
New Name
```

Now, consider the following class:
```
class MyClass:
  def __init__(self, name):
    self._name = name


  @property
  def name(self):
    return self._name

  @name.setter
  def name(self, value):
    self._name = value
```

The name property is a special attribute that has getter, setter, and deleter methods associated with it. The getter method is used to get the value of the property, and the setter method is used to set the value of the property.
To access the name property, we use the dot notation, just like we would with an attribute. However, the getter method will be called behind the scenes when we access the property.

To modify the name property, we also use the dot notation, but the setter method will be called behind the scenes when we assign a new value to the property.
Here is an example of how to use the name property:

```
my_class = MyClass("My Class")

# Access the property
print(my_class.name)

# Modify the property
my_class.name = "New Name"

# Access the property again
print(my_class.name)
```

Output:
```
My Class
New Name
```

As you can see, the name property behaves just like an attribute. However, the getter and setter methods give us more control over how the property is accessed and modified.
Here are some of the benefits of using properties:

* Properties can be used to validate data before it is assigned to an object.
* Properties can be used to cache data, which can improve performance.
* Properties can be used to implement different levels of access control.

In general, it is a good practice to use properties instead of attributes whenever possible. This will make your code more robust and maintainable.

# The 4 important key principles in OOP:
OOP comes with 4 key principles that you should be aware of, to be able to design large applications, so that it's easier to maintain.

## 1. Encapsulation
Encapsulation refers to a mechanism of restricting the direct access of our attributes in a program. (like what we did in the example with name in the item class: restricting the ability to access and modify the name with some conditions)

## 2. Abstraction
It's a concept of OOP that only shows the necessary attributes and hides the unnecessary information. So it is basically hiding the unnecessary information from the user. (look at send_email method in the item.py).
We set other methods as private and then have them all as part of the send_email(), which is public and can be accessed out of the class. This way, the unnecessary information has been hidden from the user. In python we make methods and attributes private by adding double underscores (__) before the name.


## 3. Inheritance
Inheritance is a mechanism that allows us to reuse code across our classes. like when we had the Phone class (the child class) to inherit from the Item class (parent class or super class). This means we can declare/set attributes and methods in the parent class, and inherit from that, so that we don't repeat the code in each child class.
One important thing is that each parent class can have many child classes, but each child class can only have one parent class.


## 4. Polymorphism
Refers to a single type entity to represent different types in different scenarios. polymorphism literally means many forms; so applying it in programming is the ability to have different scenarios, when we call the exact same entity. An entity could be a function that we just call. It isn't something that is specifically applied to how you create your classes. Polymorphism is something that refers globally to your entire project. (To see examples, take a look at the polymorphism.py)


**Source**:
- [realpython](realpython.com/python-property/)
- [freecodecamp.org](https://www.youtube.com/@freecodecamp)