Chapter 2 Quiz

Q1:
    When creating a subclass from a class that has an init method with parameters, how do you call the parent class init method?

    Your Answer:
    def __init__ (self, other_sub_parameters):
        super().__init__(self, super_parameters)

Q2:
    T/F – In an ideal world, unit tests would be extensive enough to ensure that when they are run, every line of code of
    the class it is testing is ran.

    Your Answer:
    T

Q3:
    T/F – If we achieve that ideal world from the above question, we are guaranteed to have a bug free program.

    Your Answer:
    F
    Even if all lines are covered, all lines are tested, since we can not possibly test all values, we only proved
    when we run some of the instances of the values, we are bug free. This does not guarantee all instances.
    For example, if we input a string when the expected input is int, we have a bug.

Q4:
    What is wrong with trying to make a copy of a list like this:
    list_a = [ 1,2,3 ]
    list_b = list_a

    Your Answer:
    List b changes when list a changes, since the point to the same Python object in the storage place of the memory.
    A is the same object rather than a copy.
    we could do:
    list_a=[1,2,3]
    list_b=list_a.copy()

Q5:
    What does the AAA convention for unit tests stand for?
    
    Your Answer:
    Arrange Act and Assert


