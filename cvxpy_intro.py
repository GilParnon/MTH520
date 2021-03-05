# cvxpy_intro.py
"""Volume 2: Intro to CVXPY.
<Gil Parnon>
<MTH 520>
<3/5/21>
"""
import cvxpy as cp
import numpy as np

def prob1():
    """Solve the following convex optimization problem:

    minimize        2x + y + 3z
    subject to      x  + 2y         <= 3
                         y   - 4z   <= 1
                    2x + 10y + 3z   >= 12
                    x               >= 0
                          y         >= 0
                                z   >= 0

    Returns (in order):
        The optimizer x (ndarray)
        The optimal value (float)
    """
    x = cp.Variable(3, nonneg = True)
    c = np.array([2,1,3])
    objective = cp.Minimize(c.T @ x)
    
    A = np.array([1,2,0])
    B = np.array([0,2,-4])
    D = np.array([2,10,3])
    P = np.eye(3)
    constraints  = [A @ x <= 3, B @ x <= 1, D @ x >= 12, P @ x >= 0]
    
    problem = cp.Problem(objective, constraints)
    return x, problem.solve()
    
[x,ans] = prob1()
print("The optimal x is: ", x.value)
print("The optimal value is " + ans)
    


# Problem 2
def l1Min(A, b):
    """Calculate the solution to the optimization problem

        minimize    ||x||_1
        subject to  Ax = b

    Parameters:
        A ((m,n) ndarray)
        b ((m, ) ndarray)

    Returns:
        The optimizer x (ndarray)
        The optimal value (float)
    """
    x = cp.Variable(len(A[0,:]))
    objective = cp.Minimize(cp.norm(x,1))
    constraints = [A[0,:] @ x == b[0], A[1,:] @ x == b[1]]
    problem = cp.Problem(objective,constraints)
    return x,problem.solve()
A = np.array([[1,2,1,1],[0,3,-2,-1]])
b = np.array([[7],[4]])
[x,mini] = l1Min(A,b)
print(x,mini)

# Problem 3
def prob3():
    """Solve the transportation problem by converting the last equality constraint
    into inequality constraints.

    Returns (in order):
        The optimizer x (ndarray)
        The optimal value (float)
    """
    x = cp.Variable(6,nonneg = True)
    c = np.array([4,7,6,8,8,9])
    objective = cp.Minimize(c.T @ x)
    A = np.array([[1,0,1,0,1,0],[0,1,0,1,0,1],[1,1,1,1,1,1],[1,1,0,0,0,0],[0,0,1,1,0,0],[0,0,0,0,1,1]])
    b = np.array([5,8,13,7,2,4])
    constraints = (A[0,:]@x == b[0],A[1,:]@x == b[1],A[2,:]@x == b[2],A[3,:]@x == b[3],A[4,:]@x == b[4],A[5,:]@x == b[5])
    problem = cp.Problem(objective,constraints)
    return x,problem.solve()
[x,mini] = prob3()
print(x.value,mini)
    
    
# Problem 4
def prob4():
    """Find the minimizer and minimum of

    g(x,y,z) = (3/2)x^2 + 2xy + xz + 2y^2 + 2yz + (3/2)z^2 + 3x + z

    Returns (in order):
        The optimizer x (ndarray)
        The optimal value (float)
    """
    x = cp.Variable(3)
    Q = np.array([[3,2,1],[2,4,2],[1,2,3]])
    r = np.array([3,0,1])
    prob = cp.Problem(cp.Minimize(.5*cp.quad_form(x,Q)+r.T @ x))
    return x,prob.solve()
[x,mini] = prob4()
print(x.value, mini)


# Problem 5
def prob5(A, b):
    """Calculate the solution to the optimization problem
        minimize    ||Ax - b||_2
        subject to  ||x||_1 == 1
                    x >= 0
    Parameters:
        A ((m,n), ndarray)
        b ((m,), ndarray)
        
    Returns (in order):
        The optimizer x (ndarray)
        The optimal value (float)
    """
    x = cp.Variable(4,nonneg = True)
    objective = cp.Minimize(cp.sum_squares(A @ x - b))
    constraints = [x[0]+x[1]+x[2]+x[3] == 1]
    problem = cp.Problem(objective,constraints)
    return x,np.sqrt(problem.solve())
b = np.array([7,4])
[x,mini] = prob5(A,b)
print(x,mini)


# Problem 6
def prob6():
    """Solve the college student food problem. Read the data in the file 
    food.npy to create a convex optimization problem. The first column is 
    the price, second is the number of servings, and the rest contain
    nutritional information. Use cvxpy to find the minimizer and primal 
    objective.
    
    Returns (in order):
        The optimizer x (ndarray)
        The optimal value (float)
    """	 
    raise NotImplementedError("Problem 6 Incomplete")