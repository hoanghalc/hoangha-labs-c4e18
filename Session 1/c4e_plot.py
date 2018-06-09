import matplotlib
matplotlib.use("TkAgg")

from matplotlib import pyplot

#1. Prepare Data
labels = ['iOS','Android','Web', 'React Native']
values = [20,15,40,25]
colors = ['red','green','cyan','gold']
explode = [0,0,0,0.2]
shadow = True

#2. Plot
pyplot.pie(values, labels=labels, 
                    colors=colors,
                    explode=explode,
                    shadow=shadow
            )
pyplot.axis("equal")
#3. Show Chart
pyplot.show() 