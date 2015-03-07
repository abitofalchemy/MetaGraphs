# Input file
setwd("/data/saguinag/MetaGraphs/")

## in mov_dfies dataset
titles_indata <- read.csv("imdb_data/imdb_movies.csv", sep=",", header=TRUE, nrows=1000)

titles_df <- data.frame(titles_indata)
print (dim(titles_df))
titles_df$year <- NULL
titles_df$node <- "v"
titles_df$nbr <- row.names(titles_df)
titles_df <- titles_df[c(2,3,1)]

titles_df$movie <- paste('"',titles_df$movie,'"',sep='')
print ( head(titles_df))

## toy_imdb.g is a SUBDUE formatted graph file that list movie-titles as 
## principal nods
output_file = "imdb_data/toy_imdb.g"
write.table(titles_df, output_file, sep=" ", row.names=FALSE)
print ("Saved data to disk: imdb_data/toy_imdb.g")

## Append the nodes Actors
## in actors dataset
actors <- read.csv("imdb_data/imdb_actors_movietitle.csv", sep=",", header=TRUE, nrows=1000)
df <- data.frame(actors)
print(head(actors))

