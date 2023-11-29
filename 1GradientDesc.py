import numpy as np

def gradient_descent(x,y):
    m_current = b_current = 0
    iterations = 1000

    n = len(x)
    learning_rate = 0.001

    for i in range(iterations):
        y_predicted = m_current * x + b_current   #y=mx+c

        cost = (1/n) * sum([val**2 for val in (y-y_predicted)])

        m_derivative = -(2/n) *sum(x*(y-y_predicted))   #partial derivative wih respect to m
        b_derivative = -(2/n) *sum(y-y_predicted)       #partial derivative with respect to b

        m_current = m_current - learning_rate * m_derivative  
        b_current = b_current - learning_rate * b_derivative
        
        print("m {},b {},cost {},iteration {}".format(m_current,b_current,cost,i))

x = np.array([1,2,3,4,5])
y = np.array([5,7,9,11,13])

gradient_descent(x,y)