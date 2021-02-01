# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sqlite3

x = []
y = []
conn = sqlite3.connect('chinook.sqlite')
print("Opened database successfully");

cursor = conn.execute("SELECT DISTINCT invoiceid, total FROM invoice")
for row in cursor:
   x.append(row[0])
   y.append(row[1])

'''xa = {
   'Id' : x,
   'Total' : y}
print("Operation done successfully")
myvar = pd.DataFrame(xa)
print(myvar.to_string(index = False))''' # Prints all data

xpts = np.array(x)
ypts = np.array(y)

plt.plot(xpts, ypts) #Shows amount of money per transaction
plt.show()

conn.close()
