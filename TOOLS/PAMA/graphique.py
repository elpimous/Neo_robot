from pylab import *


y = (5.2,8.33,9.12,12.21,14.44)
plot(y,marker='o',markerfacecolor = 'red')

xlabel('Tests')
ylabel('')
title('Accuracy graph.')
grid(True)
savefig("/home/neo/Images/graph.png")
show()

