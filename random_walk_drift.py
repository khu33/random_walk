import random as rnd
import matplotlib.pyplot as plt
import numpy as np

T =1
n_list = [10, 50, 100, 1000]

fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1, sharex = True)

def beta(t):

    return t

X_list = []
T_list = []
for j in range(4):

    n = n_list[j]

    N = n*T
    t_grid = np.linspace(0, T, N)

    X = [0]*N

    for i in range(1, N):

        X[i] = 1/np.sqrt(n)* rnd.gauss(0, 1) * np.sqrt(beta(i/n)) + np.sqrt((1 - beta(i/n)/n)) * X[i-1] 
    X_list.append(X)
    T_list.append(t_grid)


ax1.plot(T_list[0], X_list[0])
ax1.set_title('T = ' + str(n_list[0]))
ax2.plot(T_list[1], X_list[1])
ax2.set_title('T = ' + str(n_list[1]))
ax3.plot(T_list[2], X_list[2])
ax3.set_title('T = ' + str(n_list[2]))
ax4.plot(T_list[3], X_list[3])
ax4.set_title('T = ' + str(n_list[3]))
plt.show()


    
