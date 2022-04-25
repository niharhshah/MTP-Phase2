import csv
import matplotlib.pyplot as pl

x = []
y = []
s = []

with open('Saved_data.csv','r')  as csvfile:
    plots = csv.reader(csvfile, delimiter = ',')
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))
        s.append(int(row[2]))
pl.plot(x,y)
pl.plot(x,s)
# pl.legend()
pl.show()
