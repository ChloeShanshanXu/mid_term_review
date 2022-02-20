Chapter 4 Quiz

Q1:
    What two things must you be able to identify if a problem has the potential to be solvable via recursion?

    Your Answer:
    If the problem can be divided into smaller workable pieces and solve individually, repetitively.
    Especially when they are complex and have a lot of possible branches.

Q2:
    If the answer is False, please correct the statement to make it true.
    T/F - A recursive solution can only have a single base case.

    Your Answer:
    F
    A recursive solution may have one or more base cases.

Q3:
    Describe a problem that is easily solved with recursion and why recursion is a good approach for the solution
    instead of an iterative approach.

    Your Answer:
    A good example would be search for something through some kind of file system - start from root folder search
    all the files it. If not there, search through every folder inside, search inside those folders through every
    file to get the target. If not, dive into all folders inside again.
    Recursion is easier than iteration in this case, because we can search different paths without having to check
    every possible instance.

Q4:
    Write a recursive function(s) that will accept a list and reverse the list ( without creating/returning a new list )

    Your Answer:
    def rev(list, front=0, back=-1):
        if front < alen(list)/2:
            list[front], list[back] = list[back], list[front]
            front += 1
            back -= 1
            rev(list)
