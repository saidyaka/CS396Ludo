import matplotlib.pyplot as plt
import csv

with open('test2.csv','r') as file:
    x = file.read()
x = x.split(",")
y = []
for i in range(40):
    x[i] = float(x[i])
    y.append(i)
print(x)

plt.plot(y, x, color = 'g', label = "Fitness")
plt.xlabel('evolution number')
plt.ylabel('fitness')
plt.title('Fitness of best seed at each evolution')
plt.legend()
plt.show()

plt.line