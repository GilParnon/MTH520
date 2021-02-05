# matplotlib_intro.py
"""Python Essentials: Intro to Matplotlib.
<Gil Parnon>
<MTH 520>
<2/3>
"""
import numpy as np
from matplotlib import pyplot as plt

# Problem 1
def var_of_means(n):
    """Construct a random matrix A with values drawn from the standard normal
    distribution. Calculate the mean value of each row, then calculate the
    variance of these means. Return the variance.

    Parameters:
        n (int): The number of rows and columns in the matrix A.

    Returns:
        (float) The variance of the means of each row.
    """
    A = np.random.normal(size=(n,n))
    m = A.mean(axis=1)
    return np.var(m)
   

def prob1():
    """Create an array of the results of var_of_means() with inputs
    n = 100, 200, ..., 1000. Plot and show the resulting array.
    """
    n = 100*np.linspace(1,10,10)
    x = [0]*len(n)
    for i in range(len(n)):
        x[i] = var_of_means(int(n[i]))
    plt.plot(n,x)
    plt.show()
    return x

# Problem 2
def prob2():
    """Plot the functions sin(x), cos(x), and arctan(x) on the domain
    [-2pi, 2pi]. Make sure the domain is refined enough to produce a figure
    with good resolution.
    """
    pi = np.pi
    x = np.linspace(-2*pi,2*pi,100)
    print("Sin(x)")
    a = np.sin(x)
    b = np.cos(x)
    c = np.arctan(x)
    print("Sin(x)")
    plt.plot(x,a)
    plt.show()
    print("Cos(x)")
    plt.plot(x,b)
    plt.show()
    print("ArcTan(x)")
    plt.plot(x,c)
    plt.show()


# Problem 3
def prob3():
    """Plot the curve f(x) = 1/(x-1) on the domain [-2,6].
        1. Split the domain so that the curve looks discontinuous.
        2. Plot both curves with a thick, dashed magenta line.
        3. Set the range of the x-axis to [-2,6] and the range of the
           y-axis to [-6,6].
    """
    x1 = np.linspace(-2,1,50,endpoint=False)
    x2 = np.flip(np.linspace(6,1,100,endpoint=False))
    f1 = 1/(x1-1)
    f2 = 1/(x2-1)
    plt.plot(x1,f1,'m--', linewidth = 4)
    plt.plot(x2,f2, 'm--', linewidth = 4)
    plt.xlim(-2,6)
    plt.ylim(-6,6)
    plt.show()


# Problem 4
def prob4():
    """Plot the functions sin(x), sin(2x), 2sin(x), and 2sin(2x) on the
    domain [0, 2pi].
        1. Arrange the plots in a square grid of four subplots.
        2. Set the limits of each subplot to [0, 2pi]x[-2, 2].
        3. Give each subplot an appropriate title.
        4. Give the overall figure a title.
        5. Use the following line colors and styles.
              sin(x): green solid line.
             sin(2x): red dashed line.
             2sin(x): blue dashed line.
            2sin(2x): magenta dotted line.
    """
    x = np.linspace(0,2*np.pi)
    fig, axs = plt.subplots(2,2)
    axs[0,0].plot(x,np.sin(x),'g-')
    axs[0,1].plot(x,np.sin(2*x),'r--')
    axs[1,0].plot(x,2*np.sin(x),'b--')
    axs[1,1].plot(x,2*np.sin(2*x),'m:')
    plt.axis([0,2*np.pi,-2,2])
    axs[0,0].set_title('Sin(x)')
    axs[0,1].set_title('Sin(2x)')
    axs[1,0].set_title('2Sin(x)')
    axs[1,1].set_title('2Sin(2x)')
    fig.suptitle('Various Sin functions')
    plt.show()
    

# Problem 6
def prob6():
    """Plot the function f(x,y) = sin(x)sin(y)/xy on the domain
    [-2pi, 2pi]x[-2pi, 2pi].
        1. Create 2 subplots: one with a heat map of f, and one with a contour
            map of f. Choose an appropriate number of level curves, or specify
            the curves yourself.
        2. Set the limits of each subplot to [-2pi, 2pi]x[-2pi, 2pi].
        3. Choose a non-default color scheme.
        4. Add a colorbar to each subplot.
    """
    x = np.linspace(-2*np.pi,2*np.pi) 
    y = x.copy()
    X,Y = np.meshgrid(x,y)
    Z = np.sin(X)*np.sin(Y)/(X*Y)
    plt.subplot(121,aspect = 'equal')
    plt.pcolormesh(X,Y,Z,cmap="magma")
    plt.colorbar()
    plt.xlim(-2*np.pi,2*np.pi)
    plt.ylim(-2*np.pi,2*np.pi)

    plt.subplot(122,aspect = 'equal')
    plt.contour(X,Y,Z,10,cmap = "coolwarm")
    plt.xlim(-2*np.pi,2*np.pi)
    plt.ylim(-2*np.pi,2*np.pi)
    plt.colorbar()
    return

prob1()
prob2()
prob3()
prob4()
prob6()