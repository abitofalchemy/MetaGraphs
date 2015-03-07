#!/usr/bin/python 
# -*- coding: utf-8 -*-
# Copyright (c) Sal Aguinaga 2015

import sys, os
import argparse, re
import pandas as pd
import numpy as np
import csv, pprint
import math
import itertools

## Begin
inputfile ="imdb_data/imdb_actor_titles.csv"
df = pd.read_csv(inputfile,header=True,nrows=10000)

df.columns = ['AR','MO'] 
df['node'] = df.index.values

uars = [k for k,g in df.groupby(['AR'])]
umov = [k for k,g in df.groupby(['MO'])]

tmar = pd.DataFrame(uars)
tmar.columns = ['AR']
tmar['Label'] = "AR"

tmov = pd.DataFrame(umov)
tmov.columns = ['MO']
tmov['Label'] = "MO"


vertices = pd.concat([tmar,tmov])
#print vertices.columns
vertices['type'] = 'v'
vertices = vertices.reset_index()
vertices['node'] = vertices.index.values + 1
## Reorder the columns
vertices = vertices[['type','node','Label']]

## Save vertices to disk
vertices.to_csv("imdb_data/imdb_10000.g",mode='w', header=False, index=False, sep='\t')
print 'Saved Vertices to disk'

## EDGES
print '-'*80

#print tmov.head()
#print tmar.head()
tmar['node'] = tmar.index.values + 1
tmov['node'] = tmov.index.values + len(tmar) + 1

edges = pd.merge(df, tmar, on="AR")
edges.drop('node_x',axis=1, inplace=True)
edges = pd.merge(edges, tmov, on="MO")
edges['type'] = "e"
edges_g = edges[["type", "node_y", "node"]]
edges_g['Link'] = "WasIn"
#print edges_g

## Save edges to disk
edges_g.to_csv("imdb_data/imdb_10000.g",mode='a', header=False, index=False, sep='\t')
print 'Appended edges to .g file.\nDone.'
