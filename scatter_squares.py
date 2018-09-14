import matplotlib.pyplot as plt



x_vlaues =list(range(1,1001))
y_values =[x**2 for x in x_vlaues]


plt.scatter(x_vlaues,y_values,c=y_values,cmap=plt.cm.Blues,edgecolor="none",s =40)

# set chart titles and label axes

plt.title("Square Numbers", fontsize=23)
plt.xlabel("Value",fontsize=23)
plt.ylabel("square of value", fontsize=23)

# set size of tick labels.

plt.tick_params(axis='both',labelsize=14)

plt.axis([0,1100,0,1100000])

plt.show()
