import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

Nx = 50     # Gitterpunkter langs x-retningen
Nt = 1000   # Gitterpunkter langs t-retningen
h = 0.1
k = 3
Lambda = k / h**2

x = np.linspace(0, 1, Nx)
u = np.sin(x)
u[0] = u[-1] = 0
sol = [u.copy()]

for n in range(Nt):
    u_new = u.copy()
    for i in range(1, Nx-1):
        u_new[i] = (u[i] + Lambda*(u[i-1] + u[i+1])) / (1 + 2*Lambda)   # Omskrivningen som er beskrevet i teksten
    u = u_new.copy()
    sol.append(u.copy())

fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(-1, 1)
ax.set_xlabel("posisjon")
ax.set_ylabel("temperatur")
line, = ax.plot(x, sol[0], label="Temperaturfordeling")
ax.legend()

def update(frame):
    line.set_ydata(sol[frame])
    return line,

ani = animation.FuncAnimation(fig, update, frames=len(sol), interval=20, blit=True)
plt.show()

