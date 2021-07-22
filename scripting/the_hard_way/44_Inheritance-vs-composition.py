# Inheritance and composition

# The basis of inheritance is that you have multiple common
# functionalities between objects from different classes 
# and because of that you create a main class that will then
# be inherited hence it becomes the parent class and the class
# that is inheriting is the child class. 
# The child class has all of the methods that come with the parent
# class but also some methods that make specialized in other
# things.

# There 3 types of relationships between parent and child classes:

# 1. Actions on the child imply an action on the parent
# 2. Actions on the child override the action on the parent
# 3. Actions on the child alter the action on the parent

#====================================================================#
        # Implicit Inheritance
#====================================================================#

class Parent():

    def implicit(self):
        print ("PARENT implicit()")

class Child(Parent):
    pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

#====================================================================#
        # Override Explicity
#====================================================================#

class Parent_override():

    def override(self):
        print ("PARENT override()")

class Child_override(Parent_override):

    def override (self):
        print ("CHILD override()")

print ()

dad = Parent_override()
son = Child_override()

dad.override()
son.override()

#====================================================================#
        # After Before or After
#====================================================================#

class Parent_after():

    def altered(self):
        print ("PARENT altered()")

class Child_after(Parent_after):

    def altered(self):
        print ("CHILD, before Parent altered()")
        super (Child_after, self).altered()
        print ("CHILD, after PARENT altered()")

print ()

dad = Parent_after()
son = Child_after()

dad.altered()
son.altered()

#====================================================================#
        # Explanaition for After Before or After
#====================================================================#

# Basically, the important bits are all in the Child class where we 
# introduce changes to the altered method. However, while we are 
# introducing changes we still want to keep the functionality of the
# parent's class method so we call it using the built in super function.

# NOTE: This way of calling super is a Python 2 standard. The Python 3 
# way is - super().method_name(arguments) or parent_class.method_name(self, arguments)

# Here is an example of how that will look like:

class Child_p3(Parent_after):

    def altered(self):
        print ("This is the Python 3 example")
        print ("CHILD, before Parent altered()")
        super().altered()
        print ("CHILD, after Parent altered()")
        Parent_after.altered(self)
        print ("CHILD, after 2nd Parent  altered()")

print ()

son_p3 = Child_p3()

son_p3.altered()

# As we can see in Python 3 the readability of the super() function
# has been improved. Most noticably when we have multiple inheritance.

#====================================================================#
        # Multiple inheritance
#====================================================================#

# Multiple inheritance is a the moment when a class needs to inherite
# from multiple Parent classes. In Python this is done like so:

# class Multiple_inherite(Parent_one, Parent_two):
#     def __init__():
#         pass

# Now knowing how overriding and inheritance work we can see why we 
# need the super method. This, however, means that we need to specify
# which parent method we want to use and thus we can use the second 
# syntax of super - parent_name.method_name(self, arguments). This 
# way we eliminate the confusion that may arise while reading the code.

#====================================================================#
        # Common use
#====================================================================#

# The most common use of super () is actually in __init__ functions.
# As the book states: "This is probably the only place where you would
# need to do some things in a child, then complete the initialization
# in the parent." Here is an example from the book:

# class Child(Parent):  
#     def __init__(self, stuff):
#         self.studd = stuff
#         super().__init__()
#         # Parent.__init__(self)

#====================================================================#
        # Composition
#====================================================================#

# Inheritanc eis something useful, but the same effect can be achieved
# in other ways. If we look closely at the ways inheritance is initiated
# we can see that in 2 out 3 cases we are writing new code, which we 
# can introduce just by using different classes. Here is the example:

class Other():

    def override(self):
        print ("OTHER override()")

    def implicit(self):
        print ("OTHER implicit()")

    def altered(self):
        print ("OTHER altered()")

class Child_other():

    def __init__(self):
        self.other = Other()

    def implicit(self):
        self.other.implicit()

    def override(self):
        print ("CHILD overide()")

    def altered(self):
        print ("CHILD, before OTHER altered()")
        self.other.altered()
        print ("CHILD, after OTHER altered()")

son = Child_other()

son.implicit()
son.override()
son.altered()

#====================================================================#
        # Inheritance vs Composition
#====================================================================#

# We see that Inheritance and Composition solve one very important 
# problem in programming - repetitive code. But when do we use which?
# Here are the 3 rules followed by the author:

# 1. Avoid multiple inheritance at all costs, as it's too complex to 
# to be useful reliably. If you're stuck with it, then be prepared to
# know the class hierarchy and spend time finding where everything is
# coming from. 

# 2. Use composition to package up code into modules that are used in 
# many different unrelated places and situations.

# 3. Use inheritance only when there are clearly related reusable pieces
# of code that fit under a single common concept or if you have to 
# because of something you're using.
