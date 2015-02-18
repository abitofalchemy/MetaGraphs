#!/usr/bin/python 
# -*- coding: utf-8 -*-
# Copyright (c) Sal Aguinaga 2015

import sys, os
import argparse, re
import pandas as pd
import numpy as np
from collections import OrderedDict
from itertools import islice

def imdb_parse_movies():
	
	list_input = "imdb_data/movies.list"

	with open(list_input) as f:
		movies_dict = dict()
		k = 0
		for line in f:
			#lparts = re.split('\t',line.rstrip())
			#pattern = re.compile(r'"(.*?)"\s(\(.*\))\s+(\d*-.*)\n|"(.*?)"\s(\(.*\))\s({.*})\s*(\d*)')
			#pattern = re.compile(r'^"(.*?)"\s(\(.*\))\s+(\d*-.*)\n|"(.*?)"\s(\(.*\))\s({.*})\s*(\d*)')
			pattern = re.compile(r'(^.*)\t(\d{4}.*)')
			lparts = pattern.search(line)
			if lparts is not None:
				#print k, len(lparts.groups()), lparts.group(1).replace('"', '""')
				movies_dict[lparts.group(1).replace('"', '""').replace('\t','')] = lparts.group(2)
			
	print len(movies_dict)

	return movies_dict

def imdb_parse_actors_list():
	in_file = "imdb_data/actors.list"
	print 'imdb_parse_actors_list'	
	with open(in_file) as f:
		local_data = []# key = movie, value = array of actors
		k = l = start_line_reached = 0
		for line in f:
			if ('----\t\t\t------') in line: start_line_reached = True
			line = line.replace('\tFredersdorff','Fredersdorff')
			line = line.replace('\t\t','\t')
			line = line.replace('\t\t','\t')
			line = line.replace('\t]',']')
			line_parts = line.rstrip('\r\n').split('\t')
			for part in line_parts:
				part.replace('\t','')
			if (start_line_reached and len(line_parts)>1):
				#print k, line_parts
				if len(line_parts)>2:
					print line_parts, line
				k += 1
				pattern = re.compile(r'(.*\s\(\d{4}\))')
				mtitle = pattern.search(line_parts[1])
				if mtitle is not None: 
						#print ( [line_parts[0], mtitle.group(1)])
					local_data.append( [line_parts[0], mtitle.group(1)])
								#end of for loop	 
				#if k>10: break
	return local_data

def imdb_parse_actresses_list():
	print "imdb_parse_actresses_list"
	in_file = "imdb_data/actresses.list"
	#
	with open(in_file) as f:
		local_data = []# key = movie, value = array of actors
		k = l = 0
		start_line_reached = False
		for line in f:
			if ('Name\t\t\tTitles') in line: start_line_reached = True
			line = line.replace('\t\t','')
			line = line.replace('\t]',']')
			line_parts = line.rstrip('\r\n').split('\t')
			if (start_line_reached and len(line_parts)>1):
				if len(line_parts)>2: print k, line_parts, line
				pattern = re.compile(r'(.*\s\(\d{4}\))')
				mtitle = pattern.search(line_parts[1])
				if mtitle is not None:
					k += 1
					#print ( [line_parts[0], mtitle.group(1)])
					local_data.append( [line_parts[0],mtitle.group(1)] )
				#if k > 10: break
	#print local_data
	return local_data

"""
			#lparts = re.split('\t',line.rstrip())
			pattern = re.compile(r'\$(.*),(.*)\t(.*)')
			lparts = pattern.search(line)
			if lparts is not None:
				print k, len(lparts.groups()), lparts.groups()
				#local_dict[lparts.group(1).replace('"', '""').replace('\t','')] = lparts.group(2)
				if k>15:	break
				k += 1
"""
"""
	## turn dict to pandas data frame to perform a merge
	paper_title_df = pd.DataFrame.from_dict(p_t_dict.items())
	paper_title_df.columns=['paper','title']

	## merge dataframes
	mdf = pd.DataFrame.merge(paper_title_df, author, on="paper", how="inner")
	print author.shape, paper_title_df.shape, mdf.shape
	print mdf.head()

	## output dataframe to disk
	mdf.to_csv("data/dblp_author_paper_title.csv", sep=',', mode='w', header=True, index=False)
"""
def imdb_parse_by_actresses():
	aDat= imdb_parse_actresses_list()
	df = pd.DataFrame(aDat,columns=['Name','Titles'])
	print 'Saving to disk...' #df.shape, df.head()
	df.to_csv("imdb_data/imdb_actresses_mov_tmp.csv", mode='w', header=True, index=False)
	return

def imdb_parse_by_actors():
	aDat= imdb_parse_actors_list()
	df = pd.DataFrame(aDat,columns=['actor','Titles'])
	print 'Saving to disk...' #df.shape, df.head()
	df.to_csv("imdb_data/imdb_actor_mov_tmp.csv", mode='w', header=True, index=False)
	return

def imdb_parse_by_movies():
	aDict	= imdb_parse_movies()	
	aDict	= OrderedDict(sorted(aDict.items(), key=lambda t: t[1]))
	df = pd.DataFrame.from_dict(aDict.items())
	df.columns=['Titles','year']
	
	print 'Saving to disk...' #df.shape, df.head()
	df.to_csv("imdb_data/imdb_movies.csv", mode='w', header=True, index=False)
	return

if	__name__ =='__main__':
	parser = argparse.ArgumentParser(description='Generate a txt file for a graph')
	parser.add_argument('list_type', help='input file path and list type name', action='store')
	
	args = parser.parse_args()
	print args.list_type
	if (args.list_type == "movies"):#print args.type_movies
		imdb_parse_by_movies()
	elif (args.list_type == "actors"):
		imdb_parse_by_actors()
	elif (args.list_type == "actresses"):
		imdb_parse_by_actresses()
