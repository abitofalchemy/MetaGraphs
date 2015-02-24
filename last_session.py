exec("toDotG.py")
execfile("toDotG.py")
toy = df[10,]
ls()_
ls()
ls
print df.head()
eval("toDotG.py")
toDotG.py
toDotG
pwd
cwd
import sys, os
import argparse, re
import pandas as pd
import numpy as np
import csv, pprint
import math
def ungroup_actors_list(data_file):
  actor_movie_data = []
  name_title_dict = dict()
  with open(data_file, 'rb') as f:
    #per_line = f.readline().rstrip().split(',')
    #actor_movie_data.append( [per_line[0], per_line[1]] )
    reader = csv.reader(f)
    k = 0
    for Name, Title in reader:
      if Name is '':
        actor_movie_data.append([hold_name, Title])
      else:
        hold_name = Name
        actor_movie_data.append([hold_name, Title])
      #print [hold_name, Title]
      k += 1
      #if k>20: break
  return actor_movie_data
def main():
  ## Begin
  inputfile ="imdb_data/imdb_actor_titles.csv"
  df = pd.read_csv(inputfile,header=True)
  print df.head()
  toy = df[10,]
df
 inputfile ="imdb_data/imdb_actor_titles.csv"
inputfile ="imdb_data/imdb_actor_titles.csv"
import pandas as pd
df = pd.read_csv(inputfile, header=True)
toy = df[,10]
toy = df[10,]
toy = df.head()
toy
toy = df.head(10)
toy
df = pd.read_csv(inputfile)
toy = df.head(10)
toy
toy.columns = ['MO']
toy.columns = ['MO','AR
toy.columns = ['MO','AR']
toy
toy.columns = ['AR','MO']
import itertools
itertools.groupby(sorted(toy))
unique = [k for k,g in itertools.groupby(sorted(toy))]
unique
toy
toy.idx
toy.ix
toy.index.values
toy[tnode]=toy.index.values
toy['tnode']=toy.index.values
toy['node']=toy.index.values
toy
itertools.groupby(AR)
itertools.groupby(toy.AR)
unique = [k for k,g in itertools.groupby(toy.AR)]
unique
unique.ix=unique.index.values
df = pd.dataframe(unique)
df = pd.DataFrame(unique)
df
df['k']=df.index.values
df
df.columns=['AR','k']
mg = pd.join(toy, df, on='AR')
mg = pd.merge(toy, df, on='AR')
mg
unique = [k for k,g in itertools.groupby()]
import readline
for i in range(readline.get_current_history_length()):
    print readline.get_history_item(i)
unique = [k for k,g in itertools.groupby(mg)]
unique
itertools.groupby(mg).groups()
itertools.groupby(mg).groups
itertools.groupby(mg)
mg
mg.groupb(AR)
mg.groupby(AR)
mg.groupby(mg.AR)
mg.groupby(mg.AR).values
mg.groupby(mg.AR).groups()
mg.groupby(mg.AR).groups
import pprint
pprint.pprint( mg.groupby(mg.AR).groups )
mg
mg.drop('node')
mg.drop('node',axis=1,inplace=True)
mg
readline.write_history_file("last_session.py")
