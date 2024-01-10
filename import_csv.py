import csv
from pandas import *
temp_ep=''
temp_show=''
query=input("Please input country of episodes you want to watch:")
query=query.strip()
data=read_csv("Map_data.csv")
show=data["Show"].tolist()
locations=data["Country"].tolist()
descriptions=data["Description"].tolist()
season=data["Season"].tolist()
episode=data["Episode"].tolist()
with open("Map_data.csv", newline='') as f:
    reader=csv.reader(f)
    csv_file=list(reader)
for i in range(len(locations)):
    if(locations[i]==query):
        if(temp_ep==str(episode[i]) and temp_show==show[i]):
            continue
        else:
            print("Anthony Bourdain: "+show[i]+", Season "+str(season[i])+" Episode "+str(episode[i])+": "+ descriptions[i]+"\n")
            temp_ep=str(episode[i])
            temp_show=show[i]
