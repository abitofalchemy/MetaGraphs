##==============================================================================
## Author: saguinag
## imdbTodotG.R 
##    Description: converts text file to graph (Subude dot G) files
##
## Notes:
##
## - interactive commands 
##   source ( r file )


##==============================================================================
## set the working dir
setwd('/data/saguinag/MetaGraphs/')

## In movies dataset
movie <- read.csv("imdb_data/imdb_movies.csv", sep=",", header=TRUE)#,nrows=1000)
mov_df <- data.frame(movie)
names(mov_df)[names(mov_df)=="movie"]<-"Titles"
mov_df$year <- NULL

## In Actors Name & (Movie) Titles
actor <- read.csv("imdb_data/imdb_actors_movietitle.csv", sep=",", header=TRUE)# nrows=1000)
actor_df <- data.frame(actor)

## Merge the datasets (inner join)
mother <- merge(actor_df,mov_df, by="Titles")
#head(mother)
#write.table(mother, "imdb_data/ttl_nam_yrs.tsv", sep="\t") 

##==============================================================================
## Generate a graph file ".g"
## v.title
## v.Name
## e v.title v.name

#motherdf <- mother[sample(1:nrow(mother), 10,replace=FALSE),] # sample from mother
motherdf <- mother 
rownames(motherdf) <- 1:nrow(motherdf)
motherdf$node <- row.names(motherdf)  # create the node (v) column with its ids 
motherdf$year <- NULL                 # remove year column
motherdf <- melt(motherdf,id="node")    # stack Names & Titles node, variable, value
motherdf$value <- paste('"',motherdf$value,'"',sep='')
motherdf$node <- row.names(motherdf)  # create the node (v) column with its ids 
motherdf$vertex <- "v"
head(motherdf)
motherdf <- motherdf[c(4,1,3,2)]
motherdf$variable <- NULL 

## Write data.frame to disk
write.table(motherdf, "imdb_data/imdb_vertices.g", sep="\t", quote=FALSE, col.names=FALSE, row.names=FALSE)

##==============================================================================
## Create a list of edges
## 

# edgesdf <- mother[sample(1:nrow(mother), 10,replace=FALSE),] # sample from mother
edgesdf <- mother
rownames(edgesdf) <- 1:nrow(edgesdf)    # reindex/reset the dataframe
edgesdf$tnode <- row.names(edgesdf)     
rownames(edgesdf) <- 1:nrow(edgesdf)

edgesdf <- transform(edgesdf, tnode=as.numeric(tnode))
edgesdf$nnode <- edgesdf$tnode + nrow(edgesdf)
edgesdf$year <- NULL # Drop the year column for now
edgesdf$edge <- "e"
edgesdf <- edgesdf[c(5,4,3,2,1)]
edgesdf$Names <- paste('"',edgesdf$Names,' was_in ',sep='')
edgesdf$Titles <- paste(edgesdf$Titles,'"',sep='')
head(edgesdf)
write.table(edgesdf, "imdb_data/imdb_edges.g", sep="\t",quote=FALSE, col.names=FALSE, row.names=FALSE)

## concate files
try(system("cat imdb_vertices.g >> imdb.g; cat imdb_edges.g >> imdb.g", intern = FALSE)) 