from matplotlib import pyplot 
from matplotlib import style
style.use("ggplot")

pyplot.plot([0.03,0.57,0.10,0.06,0.05],[0.09,1.61,0.30,0.18,0.14])
pyplot.title("V vs R Graph")
pyplot.xlabel("Current")
pyplot.ylabel("Voltage")
pyplot.legend()


pyplot.show()

