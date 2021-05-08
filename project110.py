import csv
import random
import pandas as pd
import statistics
import plotly.graph_objects as go
import plotly.figure_factory as ff
df=pd.read_csv("medium_data.csv")
data=df["reading_time"].tolist()
def randomset(counter):
    dataset = [] 
    for i in range(0, counter): 
        random_index= random.randint(0,len(data)-1) 
        value = data[random_index] 
        dataset.append(value) 
        mean = statistics.mean(dataset) 
    return mean
def showfig(meanlist): 
    df = meanlist 
    mean = statistics.mean(df) 
    fig = ff.create_distplot([df], ["reading_time"], show_hist=False) 
    fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 1], mode="lines", name="MEAN")) 
    fig.show()
def main():
    meanlist = [] 
    for i in range(0,1000): 
        set_of_means= randomset(100) 
        meanlist.append(set_of_means) 
    showfig(meanlist) 
    mean = statistics.mean(meanlist) 
    print("Mean of sampling distribution :-",mean )
main()
populationmean=statistics.mean(data)
print(populationmean)

def standarddeviation():
    meanlist = [] 
    for i in range(0,1000): 
        set_of_means= randomset(100) 
        meanlist.append(set_of_means) 
    sd=statistics.stdev(meanlist)
    print(sd)
standarddeviation()
