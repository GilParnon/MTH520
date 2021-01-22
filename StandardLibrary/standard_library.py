# standard_library.py
"""Python Essentials: The Standard Library.
<Gil Parnon>
<Math 520>
<1/22/2020>
"""
import calculator as clc
from itertools import combinations

    
# Problem 1
def prob1(L):
    """Return the minimum, maximum, and average of the entries of L
    (in that order).
    """
    return min(L), max(L), sum(L)/len(L)


# Problem 2
def prob2():
    """Determine which Python objects are mutable and which are immutable.
    Test numbers, strings, lists, tuples, and sets. Print your results.
    """
    int_1 = 5
    temp = int_1
    temp += 1
    print("Are ints mutable?",temp == int_1)
    str_1 = "Hello"
    temp = str_1
    temp += " world"
    print("Are strings mutable?",temp == str_1)
    list_1 = [1,2,3]
    temp = list_1
    temp[0] = 5
    print("Are lists mutable?",temp == list_1)
    tuple_1 = ("apple","banana","cherry")
    temp = tuple_1
    temp += (1,)
    print("Are tuples mutable?",temp == tuple_1)
    set_1 = {"apple", "banana", "cherry"}
    temp = set_1
    temp.add("some other fruit")
    print("Are sets mutable?",temp == set_1)
    return
    


# Problem 3
def hypot(a, b):
    """Calculate and return the length of the hypotenuse of a right triangle.
    Do not use any functions other than those that are imported from your
    'calculator' module.

    Parameters:
        a: the length one of the sides of the triangle.
        b: the length the other non-hypotenuse side of the triangle.
    Returns:
        The length of the triangle's hypotenuse.
    """
    return clc.sqrt(clc.add(clc.multiply(a,a),clc.multiply(b,b)))

  
# Problem 4
def power_set(A):
    """Use itertools to compute the power set of A.

    Parameters:
        A (iterable): a str, list, set, tuple, or other iterable collection.

    Returns:
        (list(sets)): The power set of A as a list of sets.
    """
    myList = list()
    for i in range(1,len(A)+1,1):
        myList += combinations(A,i)
    return myList

if __name__ == "__main__":
    print(prob1((3,5,12,0,2)))
    prob2()
    print(hypot(3,4))
    print(power_set(("A","B","C","D")))
