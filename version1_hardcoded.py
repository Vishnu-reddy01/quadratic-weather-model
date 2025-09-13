import matplotlib.pyplot as plt
import numpy as np

a = 0.5
b = -3
c = 28

# Specific time
t_val = 5
T_val = a * t_val**2 + b * t_val + c

print(f"Predicted temperature at t={t_val}: {T_val:.2f}°C")

# For graph (smooth curve)
t = np.linspace(0, 10, 100)
T = a * t**2 + b * t + c

# Plot
plt.plot(t, T, label="Temperature Curve")
plt.scatter(t_val, T_val, color="red", s=100, label=f"t={t_val}")
plt.xlabel("t (hours/days)")
plt.ylabel("Temperature (°C)")
plt.title("Version 1")
plt.legend()
plt.grid(True)
plt.show()
