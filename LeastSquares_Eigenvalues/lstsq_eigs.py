# lstsq_eigs.py
"""Volume 1: Least Squares and Computing Eigenvalues.
<Name>
<Class>
<Date>
"""

# (Optional) Import functions from your QR Decomposition lab.
# import sys
# sys.path.insert(1, "../QR_Decomposition")
#from qr_decomposition import qr_gram_schmidt, qr_householder, hessenberg

import numpy as np
from scipy.linalg import solve_triangular
from scipy import linalg as la
from matplotlib import pyplot as plt


# Problem 1
def least_squares(A, b):
    """Calculate the least squares solutions to Ax = b by using the QR
    decomposition.

    Parameters:
        A ((m,n) ndarray): A matrix of rank n <= m.
        b ((m, ) ndarray): A vector of length m.

    Returns:
        x ((n, ) ndarray): The solution to the normal equations.
    """
    Q,R = np.linalg.qr(A)
    b2 = np.dot(np.transpose(Q),b)
    x = solve_triangular(R,b2)
    
    return x

# Problem 2
def line_fit():
    """Find the least squares line that relates the year to the housing price
    index for the data in housing.npy. Plot both the data points and the least
    squares line.
    """
    data = np.load('housing.npy')
    b = data[:,1]
    A = data.copy()
    A[:,1] = [1]*len(b)
    x = least_squares(A,b)
    plt.scatter(data[:,0],data[:,1])
    plt.plot(data[:,0],x[0]*data[:,0]+[x[1]]*len(data[:,0]))
    plt.show()
    return x
    

# Problem 3
def polynomial_fit():
    """Find the least squares polynomials of degree 3, 6, 9, and 12 that relate
    the year to the housing price index for the data in housing.npy. Plot both
    the data points and the least squares polynomials in individual subplots.
    """
    data = np.load('housing.npy')
    A1 = np.vander(data[:,0],4)
    A2 = np.vander(data[:,0],7)
    A3 = np.vander(data[:,0],10)
    
    x1 = la.lstsq(A1, data[:,1])[0]
    y1 = data[:,0]**3*x1[0]+data[:,0]**2*x1[1]+data[:,0]*x1[2]+x1[3]
    
    x2 = la.lstsq(A2, data[:,1])[0]
    y2 = data[:,0]**6*x2[0]+data[:,0]**5*x2[1]+data[:,0]**4*x2[2]+data[:,0]**3*x2[3]+data[:,0]**2*x2[4]+data[:,0]*x2[5]+x2[6]
    
    x3 = la.lstsq(A3, data[:,1])[0]
    y3 = data[:,0]**9*x3[0]+data[:,0]**8*x3[1]+data[:,0]**7*x3[2]+data[:,0]**6*x3[3]+data[:,0]**5*x3[4]
    y3 = y3+data[:,0]**4*x3[5]+data[:,0]**3*x3[6]+data[:,0]**2*x3[7]+data[:,0]*x3[8]+x3[9]
 
    xp1 = np.polyfit(data[:,0],data[:,1],3)
    xp2 = np.polyfit(data[:,0],data[:,1],6)
    xp3 = np.polyfit(data[:,0],data[:,1],9)
    print("|Vandermonde x^3 - np.polyfit(3rd degree)| = "+str(la.norm(xp1-x1)))
    print("|Vandermonde x^6 - np.polyfit(6th degree)| = "+str(la.norm(xp2-x2)))
    print("|Vandermonde x^6 - np.polyfit(9th degree)| = "+str(la.norm(xp3-x3)))

    """  
    plt.scatter(data[:,0],y1)
    plt.scatter(data[:,0],y2)
    plt.scatter(data[:,0],y3)
    plt.scatter(data[:,0],data[:,1])
    plt.show()
    """
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3)
    fig.suptitle('x^3, x^6, x^9')
    ax1.scatter(data[:,0], y1)
    ax1.scatter(data[:,0],data[:,1])
    ax2.scatter(data[:,0], y2)
    ax2.scatter(data[:,0],data[:,1])
    ax3.scatter(data[:,0], y3)
    ax3.scatter(data[:,0],data[:,1])    
    
    


def plot_ellipse(a, b, c, d, e):
    """Plot an ellipse of the form ax^2 + bx + cxy + dy + ey^2 = 1."""
    theta = np.linspace(0, 2*np.pi, 200)
    cos_t, sin_t = np.cos(theta), np.sin(theta)
    A = a*(cos_t**2) + c*cos_t*sin_t + e*(sin_t**2)
    B = b*cos_t + d*sin_t
    r = (-B + np.sqrt(B**2 + 4*A)) / (2*A)

    plt.plot(r*cos_t, r*sin_t)
    plt.gca().set_aspect("equal", "datalim")

# Problem 4
def ellipse_fit():
    """Calculate the parameters for the ellipse that best fits the data in
    ellipse.npy. Plot the original data points and the ellipse together, using
    plot_ellipse() to plot the ellipse.
    """
    raise NotImplementedError("Problem 4 Incomplete")


# Problem 5
def power_method(A, N=20, tol=1e-12):
    """Compute the dominant eigenvalue of A and a corresponding eigenvector
    via the power method.

    Parameters:
        A ((n,n) ndarray): A square matrix.
        N (int): The maximum number of iterations.
        tol (float): The stopping tolerance.

    Returns:
        (float): The dominant eigenvalue of A.
        ((n,) ndarray): An eigenvector corresponding to the dominant
            eigenvalue of A.
    """
    raise NotImplementedError("Problem 5 Incomplete")


# Problem 6
def qr_algorithm(A, N=50, tol=1e-12):
    """Compute the eigenvalues of A via the QR algorithm.

    Parameters:
        A ((n,n) ndarray): A square matrix.
        N (int): The number of iterations to run the QR algorithm.
        tol (float): The threshold value for determining if a diagonal S_i
            block is 1x1 or 2x2.

    Returns:
        ((n,) ndarray): The eigenvalues of A.
    """
    raise NotImplementedError("Problem 6 Incomplete")
