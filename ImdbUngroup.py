#!/usr/bin/python 
# -*- coding: utf-8 -*-
# Copyright (c) Sal Aguinaga 2015

import sys, os
import argparse, re
import pandas as pd
import numpy as np
import csv, pprint
import math

def ungroup_actors_list(data_file):
	actor_movie_data = []
	name_title_dict	= dict()
	with open(data_file, 'rb') as f:
		#per_line = f.readline().rstrip().split(',')
		#actor_movie_data.append( [per_line[0], per_line[1]] )
		
		reader = csv.reader(f)
		k = 0
		for Name, Title	in reader:
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
	parser = argparse.ArgumentParser(description="IMDB list data prep\'ing")
	parser.add_argument('file_path', help='input file path actor/actress .csv', action='store')
	
	args = parser.parse_args()
	in_file = args.file_path
	#in_file = "imdb_data/imdb_actresses_mov_tmp.csv"
	data = ungroup_actors_list(in_file)
	df = pd.DataFrame(data[1:],columns=data[0])
	print df.head()
	df.to_csv("imdb_data/imdb_actors_movietitle.csv", mode='w', header=True, index=False)
	

if	__name__ =='__main__':
	"""
	ImdbUngroup.py	2nd step in prep'ing the data
	- ungroup the actors/actresses 
	"""

	main()
