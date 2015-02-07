#!/usr/bin/python 
# -*- coding: utf-8 -*-
# Copyright (c) Sal Aguinaga 2015

import sys, os
import argparse, re
import pandas as pd
import numpy as np

#	print mdf.head()


#	#print author.head()
#
#	article = pd.read_csv(article_path, index_col=0, na_filter=True,engine='c',
#                        dtype={"paper": str,"mdate": str,"publtype": str,"reviewid": str,
#                               "rating": str,"type": str,"title": str,"booktitle": str,
#                               "pages": str,"year": str,"address": str,"journal": str,
#                               "volume": str,"number": str,"month": str,"url": str,
#                               "ee": str,"cdrom": str,"publisher": str,"note": str,
#                               "isbn": str,"series": str,"school": str,"chapter": str})
#
#  #article['title'] = article['title'].map(lambda x: x.lstrip('\n').rstrip('<title>'))
#  ## Sampling the dataframe
#	article['title'] = article['title'].map(lambda x: x.lstrip('<title>').rstrip('\n').rstrip('</title>') if isinstance(x, basestring) else	None)

#	print author.columns
#	print article.columns, '\n','-'*80
#
#	print author.head()
#	print article.head()


#	mdf = pd.DataFrame.join(article, author)
#	print 'article, author, merged', article.shape, author.shape, mdf.shape
#
#	print mdf.head()
#	print mdf.tail()
#
#	print
#	article['title'] = article['title'].map(lambda x: x.lstrip('<title>') if	isinstance(x, str) else None)
#rows = np.random.choice(article.index.values,10)
#  sampled_df = article.ix[rows]
#  sampled_df['title'] = sampled_df['title'].map(lambda x: x.lstrip('<title>').rstrip('\n').rstrip('</title>'))


def main():
  parser = argparse.ArgumentParser(description='Generate a txt file for a graph')
  parser.add_argument('file_path', help='input file path and name', action='store')

  args = parser.parse_args()
  
    
  

if  __name__ =='__main__':
  #main()
	author_path  = "/data/bshi/dblp/author.csv"
	article_path = "/data/bshi/dblp/article.csv"
	field_file   = "data/fieldFile.txt"

	author = pd.read_csv(author_path)
	with open(field_file) as f:
		p_t_dict = dict()
		for line in f:
			lparts = re.split(r'\t\d*\ttitle\t+',line.rstrip())
			if (len(lparts)>1):
				p_t_dict[lparts[0]] = lparts[1]

	## turn dict to pandas data frame to perform a merge
	paper_title_df = pd.DataFrame.from_dict(p_t_dict.items())
	paper_title_df.columns=['paper','title']

	## merge dataframes
	mdf = pd.DataFrame.merge(paper_title_df, author, on="paper", how="inner")
	print author.shape, paper_title_df.shape, mdf.shape
	print mdf.head()

	## output dataframe to disk
	mdf.to_csv("data/dblp_author_paper_title.csv", sep=',', mode='w', header=True, index=False)
	print "\n","-"*80,"\nDone"
