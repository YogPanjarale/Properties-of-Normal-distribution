import statistics as stats
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import plotly.io as pio
pio.renderers.default = "browser"
f = pd.read_csv("StudentsPerformanceMini.csv")
# reading score
key = "math score"
data = f[key].tolist()
# caluculating mean,median,mode and Standard Deviation
mean = round(sum(data) / len(data), 2)
std_deviation = round(stats.stdev(data), 2)
median = stats.median(data)
mode = stats.mode(data)


def stdpercent(arr: list, mean: float, stddev: float, startend: bool = False):
    def isinrange(a): return (a > (mean - stddev)) and (a < (mean + stddev))
    i1 = list(filter(isinrange, arr))
    p1 = (len(i1)/len(arr)) * 100
    if startend:
        return (round((mean + stddev),2), round((mean - stddev),2))
    return round(p1,2)


std1 = stdpercent(data, mean, std_deviation)
std2 = stdpercent(data, mean, std_deviation*2)
std3 = stdpercent(data, mean, std_deviation*3)
std1s, std1e = stdpercent(data, mean, std_deviation, startend=True)
std2s, std2e = stdpercent(data, mean, std_deviation*2, startend=True)
std3s, std3e = stdpercent(data, mean, std_deviation*3, startend=True)
# Print Result
print(f"""DataSet : {key}
Mean : {mean}
Median : {median}
Mode : {mode}
Standard Deviation : {std_deviation}
{std1}% of data lies within 1 Standard Deviation
{std2}% of data lies within 2 Standard Deviation
{std3}% of data lies within 3 Standard Deviation
{std1s,std1e,std2s,std2e,std3s,std3e,}""")
# Creating Graph
print("Creating Figure...")
fig = ff.create_distplot([data], group_labels=[key], show_hist=False)
print("Adding lines")
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[std1s, std1s], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[std1e, std1e], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[std2s, std2s], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x=[std2e, std2e], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
print("Displaying Figure...")
fig.show()
print("Done.")
exit()
