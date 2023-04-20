
#pick some random value to start with 
import numpy as np
import matplotlib as plt
theta_0 = np.random.random()
theta_1 = np.random.random()
def hypothesis (theta_0,theta_1,XT):
    return theta_1*X + theta_0
def cost_function (XT,YT,theta_0,theta_1):
     m = len(XT)
     summation = 0.0
     for i in range (m):
        summation += ((theta_1 * XT[i] + theta_0) - YT[i])**2
        return summation /(2*m)
def gradient_descent(X,y,theta_0,theta_1,learning_rate):
    t0_deriv = 0
    t1_deriv = 0
    m = len(XT)
    for i in range (m):
        t0_deriv += (theta_1 * XT[i] + theta_0) - YT[i]
        t1_deriv += ((theta_1 * XT[i] + theta_0) - YT[i])* XT[i]
        theta_0 -= (1/m) * learning_rate * t0_deriv
        theta_1 -= (1/m) * learning_rate * t1_deriv
        return theta_0,theta_1 cost
cost_history = [0]
t0_history = [0]
t1_history = [0]
def training (XT, YT, theta_0, theta_1, learning_rate, iters):
    for i in range(iters):
         theta_0,theta_1 = gradient_descent(XT, YT, theta_0, theta_1, learning_rate)
         t0_history.append(theta_0)
         t1_history.append(theta_1)
         cost = cost_function(XT, YT, theta_0, theta_1)
         cost_history.append(cost)
         return cost_history,t0_history,t1_history,
    iterst0_history, t1_history, cost_history, iters= training (XT, YT, theta_0, theta_1, 0.01, 29)
    print(cost_history)
    cost_history = np.reshape(cost_history,(30,1))
         #Plot the cost function
plt.title('Cost Function')
plt.xlabel('No. of iterations')
plt.ylabel('Cost Function')
plt.plot(cost_history)
plt.ylim(ymin=0)
plt.xlim(xmin=0)
plt.show()

