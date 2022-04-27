import numpy as np
import matplotlib.pyplot as plt

with open("Abdrazakov/settings.txt", "r") as settings:
    tmp = [float(i) for i in settings.read().split("\n")]

set_array = np.loadtxt("Abdrazakov/settings.txt", dtype = float)
data_array = np.loadtxt("Abdrazakov/data.txt", dtype = int)

fig, ax = plt.subplots(figsize = (16, 11), dpi = 250)


data_array = data_array * set_array[0]
y = data_array
x = [0] * 898

for i in range(898):
    x[i] = i * set_array[1]

t_charge = np.argmax(data_array)
t_charge = t_charge * set_array[1]
t_down = (898 - np.argmax(data_array)) * set_array[1]
plt.title("Зависимость U(t)", position=(0.5, 0.5)) # заголовок
ax.grid(color = 'blue',    #  цвет линий
        linewidth = 0.5,    #  толщина
        linestyle = '--')
ax.minorticks_on()
ax.grid(which='minor',
        color = 'gray',
        linewidth = 0.25,
        linestyle = '-')

plt.plot(x, y, '-r', label='Зависимость', markevery=200)
plt.legend()
ax.set_xlabel('время (с)')
ax.set_ylabel('напряжение (В)')
plt.text(6, 1.5, 'время зарядки %f' % t_charge, fontsize=10)
plt.text(6, 2, 'время разрядки %f' % t_down, fontsize=10)
print(t_charge)
print(t_down)
plt.xlim (0, 10)

plt.text(0, 7, 'время зарядки %f' % t_charge, fontsize=500)

plt.show()

fig.savefig("png.png")
#print(data_array)
