# Activity: Currency Exchange Emulator
# Your task for this activity is to complete the necessary magic methods to allow the provided code to function. We will first walk through what a magic method is, and then walk through the specific magic methods that you need to add to your code.

# Step 1: Understanding Magic Methods
# Magic methods are a special piece of Python programming. They are specific to Object Oriented Programming in Python, meaning that they can only be implemented in, and will only work in, classes.

# They allow actions to be performed on class instance objects that are otherwise impossible, such as printing and comparing.

# Magic methods will always take the __<>__() form. For example, in the following code snippet the __str__() magic method is defined for the Car class.

# undefinedClick here to copy
# We have already seen and worked with one magic method: the __init__(self,...) function. This is a magic method! We have already discussed some of its special features, but for this conversation, it is important that it gets called behind the scenes without us needing to call it explicitly.

# Magic methods are never called directly. They are always called behind the scenes when specific events trigger them.

# Magic Methods Example
# Source: Python Docs

# There are many magic methods that can be implemented for any class we write. Some of them, such as those shown here, are implemented by default. However, they can also be overwritten, such as in our example of the __str__() function in the Car class, shown above. Remember, overwriting a function means that the function may already exist, but we write over what is there by re-defining the function.

# Whenever we create a new class, Python creates a __str__() function for us by default. The default implementation is often not very useful, since it only prints out the address in memory of our object. By overwriting the __str__() function, we make our class more usable.

# Magic methods help our classes to be more useful. They enable us to use some common functions, such as print() and len() . They also allow us to perform comparisons, such as <, >, <=, >=, and == .

# To use these operators, the following shorthand guide may be useful:

# undefinedClick here to copy
# By default, comparisons including instances of any user-defined classes are based on the address where the objects are stored. This is rarely desired behavior. Instead, by implementing the comparison magic methods shown above, the program writer can control how their objects interact with other objects.

# For example, consider the following code:

# undefinedClick here to copy
# Note: Each of the comparison methods MUST return a Boolean, or True/False, value. It is assumed that the 'other' will be another object of the same class, but sometimes including a check for that and throwing an error otherwise is a good idea. (In our example, if we had tried to compare 'car1 == 3', we would get an error rather than a 'False'.

# undefinedClick here to copy
# The __repr__(self) and __str__(self) functions should almost always both be implemented and should both return identical strings.

# These functions must return strings. It is best practice to have the same strings returned for each method. The syntactical difference between these two methods may be unclear at the start. That is okay, just make sure that both get implemented and return the same string.

# See the following code for an example:

# undefinedClick here to copy
# In conclusion, magic methods are special methods that can be defined on custom classes that are designed to help certain operations be easier. Every magic method has its own pre-defined behavior and expected return value. Care should be taken to make sure that vital requirements and assumptions about parameters and return values are not broken.

# Step 2: Creating a Currency Exchange Emulator
# To better understand magic methods and how they are used, we will be creating a Currency Exchange Emulator.

# We will be using the following Replit for this part of class: https://replit.com/@SD-Team/Python-1044#main.py

# If you try to run the Replit before making any changes, you will get an error. This is intentional - the test code at the bottom of the Replit is using operators that will only be defined for the class after you have implemented them.

# To get started, simply fork the Replit to your own account!

# 1. Getting Started
# First, let's explore the code we already have. We have provided you with a base Currency class that contains a class dictionary called currencies , which contains some currency exchange rates, using USD as a base value. Feel free to update this table if you desire. Note that doing so will change the expected output of the program.

# We have also provided you with the class constructor and a changeTo() function for converting between currencies. Feel free to play with these elements.

# 2. Building Magic Methods
# Your task for this activity is to complete the necessary magic methods to allow the provided code to function. The first three have been outlined in the Replit for you, the others you will need to add manually from scratch. For the pre-defined functions, make sure to remove the 'pass' statement before coding the desired return values, or they may not work. These methods are:

# __repr__(self) - This method returns the string to be printed. This should be the value rounded to two digits, accompanied by its acronym.
# __str__(self) - This method returns the same value as __repr__(self) .
# __add__(self,other) - Defines the '+' operator. If other is a Currency object, the currency values are added, and the result will be the unit of self. If other is an int or a float, it will be treated as a USD value.
# __iadd__(self,other) - This is the same as (calls) __add__(self,other) .
# __radd__(self,other) - This method is similar to __add__(self,other), but occurs when an int or float tries to add a Currency object. (Treat the int/float as having a USD value.)
# __sub__(self,other) - All __sub__(self,other) type functions are parallel to __add__(self,other) type functions.
# __isub__(self,other)
# __rsub__(self,other)
# 3. Testing Your Currency Class
# After you have defined your magic methods, test your Currency class by running the given code (the code included with the Replit). It should run with no errors if you have implemented all of the magic methods correctly.

# In case you changed it, the test code is:

# undefinedClick here to copy
# Your output should be:

# undefinedClick here to copy
# Remember, if you changed the values of the currency exchange rates, this output will also be different.

class Currency:

  currencies =  {'CHF': 0.930023, #swiss franc 
                 'CAD': 1.264553, #canadian dollar
                 'GBP': 0.737414, #british pound
                 'JPY': 111.019919, #japanese yen
                 'EUR': 0.862361, #euro
                 'USD': 1.0} #us dollar
      
  def __init__(self, value, unit="USD"):
    self.value = value
    self.unit = unit

  def __str__(self):
    return f"{round(self.value,2)} {self.unit}"

  def __repr__(self):
    return f"{round(self.value,2)} {self.unit}"

  def changeTo(self, new_unit):
    """
      An Currency object is transformed from the unit "self.unit" to "new_unit"
    """
    self.value = (self.value / Currency.currencies[self.unit] * Currency.currencies[new_unit])
    self.unit = new_unit
      
  def __add__(self, other):
    """
      Defines the '+' operator.
      If other is a Currency object the currency values 
      are added and the result will be the unit of 
      self. If other is an int or a float, other will
      be treated as a USD value. 
    """
    if type(other) == int or type(other) == float:
      x = (other * Currency.currencies[self.unit])
    else:
      x = (other.value / Currency.currencies[other.unit] * Currency.currencies[self.unit]) 
    return Currency(x + self.value, self.unit)


  def __iadd__(self, other):
    """
      Similar to __add__
    """
    return Currency.__add__(self,other)

  def __radd__(self, other):
    res = self + other
    if self.unit != "USD":
      res.changeTo("USD")
    return res

  def __sub__(self, other):
    """
      Defines the '+' operator.
      If other is a Currency object the currency values 
      are subtracted and the result will be the unit of 
      self. If other is an int or a float, other will
      be treated as a USD value. 
    """
    if type(other) == int or type(other) == float:
      x = (other * Currency.currencies[self.unit])
    else:
      x = (other.value / Currency.currencies[other.unit] * Currency.currencies[self.unit]) 
    return Currency(self.value - x, self.unit)


  def __isub__(self, other):
    """
      Similar to __sub__
    """
    return Currency.__sub__(self,other)

  def __rsub__(self, other):
    res = other - self.value
    res = Currency(res,self.unit)
    if self.unit != "USD":
      res.changeTo("USD")
    return res

v1 = Currency(23.43, "EUR")
v2 = Currency(19.97, "USD")
print(v1 + v2)
print(v2 + v1)
print(v1 + 3) # an int or a float is considered to be a USD value
print(3 + v1)
print(v1 - 3) # an int or a float is considered to be a USD value
print(30 - v2) 