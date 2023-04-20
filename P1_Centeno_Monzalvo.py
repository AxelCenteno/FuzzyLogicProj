import numpy as np
import matplotlib.pyplot as plt

def Triangular(universe:list,a:int,b:int,c:int)->list:
    lista = []
    y = []

    for i in universe:
        if i == b:
            y.append(1)
        elif i <= a:
            y.append(0)
        elif i >= a and i <= b:
            y.append(1/(b-a)*(i-a))
        elif i >= b and i <= c:
            y.append(-1/(c-b)*(i-c))
        else:
            y.append(0)
    return y

def Trapezoidal(universe:list,a:int,b:int,c:int,d:int)->list:
    y = []

    for i in universe:
        if i == b:
            y.append(1)
        elif i <= a:
            y.append(0)
        elif i >= a and i <= b:
            y.append(1/(b-a)*(i-a))
        elif i >= b and i <= c:
            y.append(1)
        elif i >= c and i <= d:
            y.append(-1/(d-c)*(i-d))
        else:
            y.append(0)
    return y

def Bell(universe:list,a:int,b:int,c:int)->list:
    lista = []
    y = [(1/(1+np.abs((i-c)/a)**(2*b))) for i in universe]
    return y

def Gaussian(universe:list,c:int,sigma:int)->list:
    lista = []
    y = [(np.exp(-((i-c)**2)/(2*sigma**2))) for i in universe]
    return y

def Sigmoidal(universe,a:float,c:int)->list:
    lista = []
    y = [(1/(1+np.exp(-a*(i-c)))) for i in universe]
    return y

if __name__ == "__main__":
    universe = []
    y1,y2,y3,y4,y5,y6 = [[],[],[],[],[],[]]
    fig1 = plt.figure(1)
    [universe,y1]=Triangular(0,200,50,100,150,0.5)
    [universe,y2]=Trapezoidal(0,200,0,0,45,80,0.5)
    [universe,y3]=Trapezoidal(0,200,120,155,200,200,0.5)
    plt.plot(universe,y1)
    plt.plot(universe,y2)
    plt.plot(universe,y3)   
    plt.title('Trapezoidal, Triangular, Trapezoidal')
    plt.ylabel('Membership')
    plt.xlabel('Universe')

    plt.figure(2)
    [universe,y4]=Bell(0,200,40,10,0,0.5)
    [universe,y5]=Gaussian(0,200,100,25,0.5)
    [universe,y6]=Sigmoidal(0,200,0.1,140,0.5)
    plt.plot(universe,y4)
    plt.plot(universe,y5)
    plt.plot(universe,y6)
    plt.title('Bell, Gaussian, Sigmoidal')
    plt.ylabel('Membership')
    plt.xlabel('Universe')
    plt.show()
    

