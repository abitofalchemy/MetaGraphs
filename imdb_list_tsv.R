##==============================================================================
## Author: saguinag
## imdbTodotG.R 
##    Description: converts text file to graph (Subude dot G) files
##
## Notes:
##
## - interactive commands 
##   source ( r file )

library('reshape2')
##==============================================================================
## set the working dir
setwd('/data/saguinag/MetaGraphs/')

## In movies dataset
movie <- read.csv("imdb_data/imdb_titles.csv", sep=",", header=TRUE)#,nrows=1000)
mov_df <- data.frame(movie)
names(mov_df)[names(mov_df)=="movie"]<-"Titles"
mov_df$year <- NULL

## In Actors Name & (Movie) Titles
actor <- read.csv("imdb_data/imdb_actor_titles.csv", sep=",", header=TRUE)# nrows=1000)
actor_df <- data.frame(actor)

## Merge the datasets (inner join)
mother <- merge(actor_df,mov_df, by="Titles")
#head(mother)
write.table(mother, "imdb_data/imdb.tsv", sep="\t") 
dir('imdb_data/imdb.tsv')
