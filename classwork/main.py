import math
import random
import statistics
# import plotly.express as px
import plotly.figure_factory as ff

print("Running main.py")
sums = []
count =[]
for i in range(0,1000):
    r1 = random.randint(1, 6)
    r2 = random.randint(1, 6)
    sum1 = r1+r2
    sums.append(sum1)
    count.append(i)
    # print("{},{} sum:{}".format(r1, r2, sum1))

# print(f"List : {sums}")

def precentagestdev(arr:list,mean,stddev):
    # print("fun called")
    isinrange=lambda a: (a > (mean -stddev)) and ( a < (mean+ stddev) )
    i1=filter(isinrange,arr)
    i1 = list(i1)
    p1 = (len(i1)/len(arr)) *100
    # print(i1)
    # print(f"Percentage :{p1}")
    return p1

mymean = statistics.mean(sums)
mymode = statistics.mode(sums)
mymedian = statistics.median(sums)
mystdev = statistics.stdev(sums)
myper= precentagestdev(sums,mymean,mystdev)
print("Mean : {} \nMode: {} \nMedian : {} \nStandard Deveation : {} \n% of Data between +Standard Deveation and -Standard Deveation : {}".format(mymean,mymode,mymedian,mystdev,myper))
# sumf = pd.array(sums,x="result",y="count")
exit()
# find the % of data that lies between mean+ stdev and mean - stdev 
print("Creating Figure...")
fig = ff.create_distplot([sums],group_labels=["sums"])
print("Displaying Figure...")
fig.show()
print("Done")
exit()