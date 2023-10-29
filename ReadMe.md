# Why use OOP?
Let's go through it with an example:
A store management system that we develop and make it more complicated by every step!
First: tracking the items we have in the store at the moment.

## __inti__ method:
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

