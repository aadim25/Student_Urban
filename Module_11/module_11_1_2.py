import matplotlib as plt # Импорт библиотеки
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter, AutoLocator) # Локатор дл нанесения рисок

import numpy as np # Библотека вычислений

x = np.linspace(0,10,10) # Создание последовательности значений

y1 = 4*x # Значения функии
y2 = [i**2 for i in x] # Значения функии
fig, ax = plt.subplots(figsize=(8, 6)) # Задание формата графиков
ax.set_title('Графики зависимостей: y1=4*x, y2=x^2', fontsize=16) # легенды
ax.set_xlabel('x', fontsize=14) # Формат легенд
ax.set_ylabel('y1, y2', fontsize=14)
ax.grid(which='major', linewidth=1.2) # Сетка
ax.grid(which='minor', linestyle='--', color='gray', linewidth=0.5) # Формат сетки
ax.scatter(x, y1, c='red', label='y1 = 4*x') # Формат графика
ax.plot(x, y2, label='y2 = x^2') # Вывод графика
ax.legend()
ax.xaxis.set_minor_locator(AutoMinorLocator()) # Легенды
ax.yaxis.set_minor_locator(AutoMinorLocator())
ax.tick_params(which='major', length=10, width=2) # Параметры тиков
ax.tick_params(which='minor', length=5, width=1)
plt.show()