##==============================================================================
## Author: saguinag
## imdb_.R 
##    Description: ls
## interactive commands 
##  source ( r file )
##==============================================================================
## set the working dir
setwd('/data/saguinag/MetaGraphs/')

## in mov_dfies dataset
movie <- read.csv("imdb_data/imdb_movies.csv", sep=",", header=TRUE)#,nrows=1000)
mov_df <- data.frame(movie)
names(mov_df)[names(mov_df)=="movie"]<-"Titles"
mov_df$year <- NULL

## Actors Name & (Movie) Titles
actor <- read.csv("imdb_data/imdb_actors_movietitle.csv", sep=",", header=TRUE)# nrows=1000)
actor_df <- data.frame(actor)

head(mov_df)
head(actor_df)

mother <- merge(actor_df,mov_df, by="Titles")
head(mother)
#write.table(mother, "imdb_data/ttl_nam_yrs.tsv", sep="\t") 

##==============================================================================
## Generate a graph file ".g"
## v.title
## v.Name
## e v.title v.name
df <- mother[sample(1:nrow(mother), 1000,replace=FALSE),] # sample from mother
df$node <- row.names(df)    # create the node (v) column with its ids 
df <- melt(df,id="node")    # stack Names & Titles node, variable, value
df$value <- paste('"',df$value,'"',sep='')

##==============================================================================
## Create a list of edges
edf <- mother[sample(1:nrow(mother), 100,replace=FALSE),] # sample from mother
rownames(edf) <- 1:nrow(edf)    # reindex/reset the dataframe
edf$tnode <- row.names(edf)     
rownames(edf) <- 1:nrow(edf)

edf <- transform(edf, tnode=as.numeric(tnode))
edf$nnode <- edf$tnode + nrow(edf)
edf$year <- NULL # Drop the year column for now
edf$edge <- "e"
edf <- edf[c(5,4,3,2,1)]
edf$Names <- paste('"',edf$Names,'"',sep='')
edf$Titles <- paste('"',edf$Titles,'"',sep='')
head(edf)
write.table(edf, "imdb_data/toy_edges.g", sep=" ", row.names=FALSE, quote=FALSE)
