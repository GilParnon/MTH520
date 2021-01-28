# numpy_intro.py
"""Python Essentials: Intro to NumPy.
<Name>
<Class>
<Date>
"""
import numpy as np


def prob1():
    """Define the matrices A and B as arrays. Return the matrix product AB."""
    A = np.array([[3, -1,4],[1,5,-9]])
    B = np.array([[2, 6,-5,3],[5, -8,9,7],[9,-3,-2,-3]])
    return np.dot(A,B)

def prob2():
    """Define the matrix A as an array. Return the matrix -A^3 + 9A^2 - 15A."""
    A = np.array([[3,1,4],[1,5,9],[-5,3,1]])
    return -np.dot(A,np.dot(A,A))+9*np.dot(A,A)-15*A


def prob3():
    """Define the matrices A and B as arrays. Calculate the matrix product ABA,
    change its data type to np.int64, and return it.
    """
    A = np.triu(np.ones((7,7), dtype=np.int))
    B = 5*np.ones((7,7), dtype=np.int) - 6*np.tril(np.ones((7,7)))
    C = np.dot(A,np.dot(B,A))
    C = C.astype(np.int64)
    return C


def prob4(A):
    """Make a copy of 'A' and set all negative entries of the copy to 0.
    Return the copy.
    Example:
    """
    B = A.copy()
    B[B<0] = 0
    return B    


def prob5():
    """Define the matrices A, B, and C as arrays. Return the block matrix
                                | 0 A^T I |
                                | A  0  0 |,
                                | B  0  C |
    where I is the 3x3 identity matrix and each 0 is a matrix of all zeros
    of the appropriate size.
    """
    A = np.array([[0,2,4],[1,3,5]])
    B = 3*np.tril(np.ones((3,3)))
    C = np.diag([-2,-2,-2])
    X1 = np.vstack((np.zeros((3,3)),A,B))
    X2 = np.vstack((A.T,np.zeros((2,2)),np.zeros((3,2))))
    X3 = np.vstack((np.eye(3),np.zeros((2,3)),C))
    return np.hstack((X1,X2,X3))

    raise NotImplementedError("Problem 5 Incomplete")


def prob6(A):
    """Divide each row of 'A' by the row sum and return the resulting array.

    Example:
        >>> A = np.array([[1,1,0],[0,1,0],[1,1,1]])
        >>> prob6(A)
        array([[ 0.5       ,  0.5       ,  0.        ],
               [ 0.        ,  1.        ,  0.        ],
               [ 0.33333333,  0.33333333,  0.33333333]])
    """
    raise NotImplementedError("Problem 6 Incomplete")
