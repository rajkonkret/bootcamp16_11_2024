import matplotlib.pyplot as plt
# pip install matplotlib
import numpy as np

x = np.linspace(0, 10, 100)
y = np.linspace(0, 10, 100)

plt.plot(x, y)

plt.xlabel("Oś X")
plt.ylabel("Oś Y")
plt.title("Wykres")

# plt.show() # pokazanie wykresu
plt.savefig('wykres.png')
# plt.close()

plt.savefig('wykres2.png', dpi=300)

plt.savefig('wykres3.png', dpi=300, bbox_inches='tight')
plt.close()
