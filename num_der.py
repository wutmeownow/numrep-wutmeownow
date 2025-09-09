import math
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
 

# Use forward-, central-, and extrapolated-difference algorithms to differentiate the functions cos(t) and exp(t) at t = 0.1, 1., and 100.

times = np.array([0.1,1.,100.], dtype=np.float64)
# print(times)

def forward_dif(func, t, h):
    return (func(t+h) - func(t))/h

def central_dif(func, t, h):
    return (func(t+(h/2)) - func(t-(h/2)))/h

def extrap_dif(func, t, h):
    return (8* (func(t+(h/4))-func(t-(h/4))) - (func(t+(h/2)) - func(t-(h/2))))/3/h

def rel_err(exper, actual):
    # return array of relative errors between experimental values (array) and the actual value (float)
    return np.abs((exper-actual*np.ones(exper.size))/actual)


h_vals = np.logspace(-17,1,100, dtype=np.float64)
print(h_vals[0])

# make figure
fig, axs = plt.subplots(3, 2)
fig.set_size_inches(12,10)


for i in range(3):
    print(f"t={times[i]}")
    
    # calculate (d/dt)cos at this t with the three methods as a function of h
    act = -np.sin(times[i])

    fdif = forward_dif(np.cos, times[i], h_vals)
    fdif_err = rel_err(fdif, act)

    cdif = central_dif(np.cos, times[i], h_vals)
    cdif_err = rel_err(cdif, act)

    edif = extrap_dif(np.cos, times[i], h_vals)
    edif_err = rel_err(edif, act)

    # plot all three on the same axis versus h logscale
    axs[i,0].plot(h_vals, act*np.ones(h_vals.size), label="Actual", color='r')
    axs[i,0].plot(h_vals, fdif, label="Forward Dif.")
    axs[i,0].plot(h_vals, cdif, label="Central Dif.")
    axs[i,0].plot(h_vals, edif, label="Extrap. Dif.")
    axs[i,0].legend()
    axs[i,0].set_xscale('log')
    axs[i,0].set_ylabel(f"(d/dt)cos({times[i]})")
    axs[i,0].set_xlabel("h")

    # plot the relative error versus h, both on logscale
    axs[i,1].plot(h_vals, fdif_err, label="Forward Dif.")
    axs[i,1].plot(h_vals, cdif_err, label="Central Dif.")
    axs[i,1].plot(h_vals, edif_err, label="Extrap. Dif.")
    axs[i,1].legend()
    axs[i,1].set_xscale('log')
    axs[i,1].set_yscale('log')
    axs[i,1].set_ylabel(f"Relative Error")
    axs[i,1].set_xlabel("h")

fig.tight_layout()
plt.show()
# plt.savefig("plot.pdf")
# plt.savefig("plot.png")

# make figure
fig, axs = plt.subplots(3, 2)
fig.set_size_inches(12,10)


for i in range(3):
    print(f"t={times[i]}")
    
    # calculate (d/dt)exp(t) at this t with the three methods as a function of h
    act = np.exp(times[i])

    fdif = forward_dif(np.exp, times[i], h_vals)
    fdif_err = rel_err(fdif, act)

    cdif = central_dif(np.exp, times[i], h_vals)
    cdif_err = rel_err(cdif, act)

    edif = extrap_dif(np.exp, times[i], h_vals)
    edif_err = rel_err(edif, act)

    # plot all three on the same axis versus h logscale
    axs[i,0].plot(h_vals, act*np.ones(h_vals.size), label="Actual", color='r')
    axs[i,0].plot(h_vals, fdif, label="Forward Dif.")
    axs[i,0].plot(h_vals, cdif, label="Central Dif.")
    axs[i,0].plot(h_vals, edif, label="Extrap. Dif.")
    axs[i,0].legend()
    axs[i,0].set_xscale('log')
    axs[i,0].set_ylabel(f"(d/dt)exp({times[i]})")
    axs[i,0].set_xlabel("h")

    # plot the relative error versus h, both on logscale
    axs[i,1].plot(h_vals, fdif_err, label="Forward Dif.")
    axs[i,1].plot(h_vals, cdif_err, label="Central Dif.")
    axs[i,1].plot(h_vals, edif_err, label="Extrap. Dif.")
    axs[i,1].legend()
    axs[i,1].set_xscale('log')
    axs[i,1].set_yscale('log')
    axs[i,1].set_ylabel(f"Relative Error")
    axs[i,1].set_xlabel("h")

fig.tight_layout()
plt.show()


