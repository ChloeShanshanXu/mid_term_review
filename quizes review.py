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