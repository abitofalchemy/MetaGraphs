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

## Read imdb.tsv fil
imdb <- read.csv("imdb_data/imdb.tsv", sep="\t", header=TRUE)#,nrows=1000)


##==============================================================================
## Generate a graph file ".g"
## v.title
## v.Name
## e v.title v.name

motherdf <- imdb[1:10,] # sample from mother
#motherdf <- mother[sample(1:nrow(mother), 100,replace=FALSE),] # sample from mother
#motherdf <- mother 
edges <- motherdf # Save a copy 
rownames(motherdf) <- 1:nrow(motherdf)  # reset node names
motherdf$node <- row.names(motherdf)    # create the node (v) column with its ids 
colnames(motherdf) <- c("MO","AR","node")
motherdf <- melt(motherdf,id="node")  # stack Names & Titles node, variable, value
motherdf$node <-NULL
vertices <- unique(motherdf)
#vertices$variable<-NULL
colnames(vertices) <- c("Names")
rownames(vertices) <- 1:nrow(vertices)  # reset node names
head(vertices)
vertices$node <- row.names(vertices) 
vertices$Names <- paste('"',vertices$Names,'"',sep='')
vertices$vertex <- "v"
vertices <- vertices[c(3,2,1)] #reorder columns
head(vertices)
## Write data.frame to disk
write.table(vertices, "imdb_data/imdb_vertices.g", sep="\t", quote=FALSE, col.names=FALSE, row.names=FALSE)

##==============================================================================
## Create a list of edges
## 
edges <- imdb[1:10,] # sample from mother
head(edges)
edges$tnode <- row.names(edges)
edges$nnode <- row.names(edges)


titlerow <- edges$Titles[1]

for (i in (2:nrow(edges))){
  if (edges[i,1] == titlerow)
    edges$tnode[i] <- edges$tnode[i-1]
  else {
    edges$tnode[i] <- edges$tnode[i-1]+1
    titlerow <- edges$Titles[i]
  }
}
head(edges)
#edges$node <- NULL
#colnames(edges) <- c("Names","actor","tnode")
#head(motherdf)
k = 1
for (i in (1:nrow(vertices))){
  if (vertices[i,3] == c("AR")){
    edges[k,3] = vertices[i,2]
    k = k +1
  }
  if (k == nrow(edges)) {break}
}
head(edges)



# rownames(vertices) <- c("")
# edges$edge <- "e"
# for (i in (1:nrow(edges))){
#   edges[i,3] = nrow(edges)+i
# }
# edges <- edges[c(5,4,3,2,1)]
# edges$Names <- paste('"',edges$Names,' was_in ',sep='')
# edges$Titles <- paste(edges$Titles,'"',sep='')
# tail(edges)
# write.table(edges, "imdb_data/imdb_edges.g", sep="\t",quote=FALSE, col.names=FALSE, row.names=FALSE)
# 
# head(edges)
# 
# 
# 
# edgesdf <- mother[1:100000,] # sample from mother
# #edgesdf <- mother[sample(1:nrow(mother), 100,replace=FALSE),] # sample from mother
# #edgesdf <- mother
# rownames(edgesdf) <- 1:nrow(edgesdf)    # reindex/reset the dataframe
# edgesdf$tnode <- row.names(edgesdf)     
# rownames(edgesdf) <- 1:nrow(edgesdf)
# 
# edgesdf <- transform(edgesdf, tnode=as.numeric(tnode))
# edgesdf$nnode <- edgesdf$tnode + nrow(edgesdf)
# edgesdf$year <- NULL # Drop the year column for now
# edgesdf$edge <- "e"
# edgesdf <- edgesdf[c(5,4,3,2,1)]
# edgesdf$Names <- paste('"',edgesdf$Names,' was_in ',sep='')
# edgesdf$Titles <- paste(edgesdf$Titles,'"',sep='')
# tail(edgesdf)
# write.table(edgesdf, "imdb_data/imdb_edges.g", sep="\t",quote=FALSE, col.names=FALSE, row.names=FALSE)
# 
# ## concate files
# #try(system("rm imdb_data/imdb.g"))
# try(system("cat imdb_data/imdb_vertices.g >> imdb_data/imdb_100k.g; cat imdb_data/imdb_edges.g >> imdb_data/imdb_100k.g", intern = FALSE)) 
# 
# ## create an igraph (format) graph file
# edgesdf$edge <- NULL
# write.table(edgesdf, "imdb_data/imdb_100k.ig", sep="\t",quote=FALSE, col.names=FALSE, row.names=FALSE)
# require(igraph)
# # Load the data. The data needs to be loaded as a table first: 
# bsk<-read.table("imdb_data/imdb_100k.ig") 
# bsk.network<-graph.data.frame(edgesdf, directed=F) #the 'directed' attribute specifies whether the edges are directed
# #plot(bsk.network)
# degree(bsk.network)
