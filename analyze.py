import matplotlib.pyplot as plt
import csv
import random
y = []
for i in range(500):
    y.append(i)
plt.figure(0)
col = ["g","b","r","y","purple"]
for i in range(5):

    with open(f'test{i}.csv','r') as file:
        x = file.read()
        random.randint(0,self.numSensorNeurons-1)

    x = x.split(",")
    for j in range(500):
        x[j] = float(x[j])
    plt.plot(y, x, color = col[i], label = "Fitness:" + str(i))
    plt.xlabel('Evolution')
    plt.ylabel('Fitness')
    plt.title('best Fitness at each evolution')
    plt.legend()
plt.show()

'''
plt.figure(1)
with open('test1.csv','r') as file:
    x = file.read()
x = x.split(",")
y = []
for i in range(500):
    x[i] = float(x[i])
    y.append(i)
print(x)

plt.plot(y, x, color = 'b', label = "Fitness")
plt.xlabel('Evolution')
plt.ylabel('Fitness')
plt.title('best Fitness at each evolution 1')
plt.legend()


plt.figure(2)
with open('test2.csv','r') as file:
    x = file.read()
x = x.split(",")
y = []
for i in range(500):
    x[i] = float(x[i])
    y.append(i)
print(x)

plt.plot(y, x, color = 'r', label = "Fitness")
plt.xlabel('Evolution')
plt.ylabel('Fitness')
plt.title('best Fitness at each evolution 2')
plt.legend()




plt.figure(3)
with open('test3.csv','r') as file:
    x = file.read()
x = x.split(",")
y = []
for i in range(500):
    x[i] = float(x[i])
    y.append(i)
print(x)

plt.plot(y, x, color = 'y', label = "Fitness")
plt.xlabel('Evolution')
plt.ylabel('Fitness')
plt.title('best Fitness at each evolution 3')
plt.legend()


plt.figure(4)
with open('test4.csv','r') as file:
    x = file.read()
x = x.split(",")
y = []
for i in range(500):
    x[i] = float(x[i])
    y.append(i)
print(x)

plt.plot(y, x, color = 'purple', label = "Fitness")
plt.xlabel('Evolution')
plt.ylabel('Fitness')
plt.title('best Fitness at each evolution 4')
plt.legend()
plt.show()
'''