import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

# Definējam punktus A un B
A = np.array([2, 0, 3])
B = np.array([1, 1, -1])

# Aprēķinām vektoru AB
AB = B - A

# Aprēķinām vektora AB moduli
modulis = np.linalg.norm(AB)

# Aprēķinām virziena kosinusus
virziena_kosinusi = AB / modulis

# Aprēķinām ortu
ortu = AB / modulis

print("Vektors AB:", AB)
print("Modulis:", modulis)
print("Virziena kosinusi:", virziena_kosinusi)
print("Ortu:", ortu)

fig = plt.figure()

# Izveidojam 3D ass
ax = fig.add_subplot(111, projection='3d')

# Uzzīmējam vektoru no A līdz B
ax.quiver(*A, *AB, color='b')

ax.set_xlim([0, 3])
ax.set_ylim([-2, 2])
ax.set_zlim([-2, 4])

# Save the figure as an image
plt.savefig("vector_plot.png")
