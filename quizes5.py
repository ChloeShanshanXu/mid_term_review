Chapter 5 Quiz

Q1:
    Why is the amortized average time for adding to an array based list O(1) and not O(n)?

    Your Answer:
    There are basically 2 circumstances:
    1). When storage for new value is sufficient, adding one value to the array based list is just one operation -
    add the value, this is O(1).
    2). When there is an overflow current available space, we need to allocate to a larger space, move everything there
    and this is an O(n) operation. However, we only face this scenario every time all the available space all taken - which
    is once every n times, so, to find the amortized rate, O(n * (1/n) ) = O(1).
    With (1) and (2) said, amortized average time is O(1).

Q2；
    In English, what does the Insert method do when inserting a value in the middle of a list?

    Your Answer:
    The "insert" method do 3 things: 1) check if insert valid in the list. 2) set given value to given index if valid.
    3) shift the value at the given index position and everything that is after the index originally to its index+1 position.

Q3:
    In English, what does the remove method do?

    Your Answer:
    The "remove" method in array based list also do 3 things: 1) search for the value provided in the list
    2) delete the first matching value found 3) move everything after the value up by one position

Q4:
    How
does
an
array
based
list
deliver
O(1)
time
operation
speed
when
accessing
any
element
at
a
given
index?

Your
Answer:
In
array
based
lists, objects
are
stored in continuous
memory
location.The
address
of
the
object
needed is the
known
base
address + given
index.Therefore, it is accessible in one
operation.

Q5:
Why is it
important
that
an
array
based
list
has
a
contiguous
block
of
memory
for storing values?

Your Answer:
    When
we
set
the
array
based
list
at
a
contiguous
block, the
elements
are
adjacent
to
each
other, the
address
calculation
of
the
elements
become
easy and fast.
