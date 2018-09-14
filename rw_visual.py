import matplotlib.pyplot as plt
from randomwalk import RandomWalk



rw = RandomWalk(50000)

rw.fill_walk()

#plot the points and show the points

point_numbers = list(range(rw.num_points))
plt.scatter(rw.x_values, rw.y_values,c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=1)

# removing the x-axis and y-axis

plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)


# plot the first and the last point

plt.scatter(0,0, c='green',edgecolor='none' , s=100)

plt.scatter(rw.x_values[-1],rw.y_values[-1], c='red',edgecolor='none',s=100)


#setting the size of the window

plt.figure(dpi=128,figsize=(40,30))
plt.show()


