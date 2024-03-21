import matplotlib.pyplot as plt
import numpy as np
# Menentukan parameter
t = np.linspace(0, 10, 1000)
f1 = 15 * np.sin(2 * np.pi * 5 * t)
f2 = 12.5 * np.cos(2 * np.pi * 3 * t)
f3 = 10 * np.sin(2 * np.pi * 7 * t)

# Menjumlahkan sinyal
f = f1 + f2 + f3

# Mengatur plot
plt.plot(t, f, label="Sinyal Asli")
plt.xlabel("Waktu (detik)")
plt.ylabel("Amplitudo (volt)")
plt.legend()

# Menambahkan garis bantu
plt.axhline(y=15, color="gray", linestyle="dashed")
plt.axhline(y=-15, color="gray", linestyle="dashed")
plt.axvline(x=0, color="gray", linestyle="dashed")

# Menampilkan plot
plt.show()
