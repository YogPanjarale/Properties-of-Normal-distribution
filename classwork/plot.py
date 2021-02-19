import math
import random
import statistics
import pandas as pd
import plotly.figure_factory as ff

print("Running main.py")
datalist = []
count = []
colname="Height(Inches)"#Weight(Pounds) 
f = pd.read_csv("./data.csv")
datalist= f[colname].to_list()
def precentagestdev(arr: list, mean, stddev):

    def isinrange(a): return (a > (mean - stddev)) and (a < (mean + stddev))
    i1 = filter(isinrange, arr)
    i1 = list(i1)
    p1 = (len(i1)/len(arr)) * 100
    return p1

mymean = statistics.mean(datalist)
mymode = statistics.mode(datalist)
mymedian = statistics.median(datalist)
mystdev = statistics.stdev(datalist)
myper = precentagestdev(datalist, mymean, mystdev)
print(f"DataSet : {colname}")
print("Mean : {} \nMode: {} \nMedian : {} \nStandard Deveation : {} \n% of Data between +Standard Deveation and -Standard Deveation : {}".format(mymean, mymode, mymedian, mystdev, myper))

exit()

print("Creating Figure...")
fig = ff.create_distplot([datalist], group_labels=["sums"])
print("Displaying Figure...")
fig.show()
print("Done")
exit()
