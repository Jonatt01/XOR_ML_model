import csv
import matplotlib.pyplot as plt
 
x = []
y = []

with open('Myfile.csv','r') as csvfile:
    lines = csv.reader(csvfile, delimiter=',')
    next(lines)
    for row in lines:
        y.append(float(row[2]))

x = range(len(y))
plt.plot(x, y, color = 'g', linestyle = 'dashed',
         marker = 'o',label = "loss")

plt.xlabel('epoch')
plt.ylabel('loss')
plt.title('LOSS')
plt.grid()
plt.legend()
plt.show()