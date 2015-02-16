library(ggplot2);

## interactive commands 
#  source ( r file )
## set the working dir
setwd('/data/saguinag/MetaGraphs/')

## in mov_dfies dataset
mov_df_indata <- read.csv("imdb_data/imdb_movies.csv", sep=",", header=TRUE, 
                          nrows=1000)
mov_df <- data.frame(mov_df_indata)
#mov_df <- mov_df[sample(nrow(mov_df),500),]
head(mov_df)
dim(mov_df)

## in ators/film titles list
actor_indata <- read.csv("imdb_data/imdb_actor_movietitle.csv", sep=",",
                         header=TRUE, nrows=1000)
actor_df <- data.frame(actor_indata)
#actor_df <- actor_df[sample(nrow(actor_df),500),]
head(actor_df)

# merge data frames
#m1 <- merge(actor_df, mov_df, by.x = "Title", by.y = "name"))
