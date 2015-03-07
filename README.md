# MetaGraphs
Find and extract subgraphs in a single massive graph

# Input File Format
- http://gephi.github.io/users/supported-graph-formats/gdf-format/

# Notes
- String mapped to a hash key:  int(hashlib.sha1(s).hexdigest(), 16) % (10 ** 8)
  http://stackoverflow.com/questions/1303021/shortest-hash-in-python-to-name-cache-files
  http://stackoverflow.com/questions/16008670/python-how-to-hash-a-string-into-8-digits

# Software 
- Subgraph mining:
  But there are problems getting R 3 working with this 
  package. http://stackoverflow.com/questions/19830394/error-with-setwd-in-r
  Resources: 
  - https://www.researchgate.net/post/Have_anyone_implemented_gSpan_algorithm_in_c_R_or_Matlab_for_frequent_sub-graph_mining
  * In R, install igraph and then the subgraph mining package
  - http://www.csc.ncsu.edu/faculty/samatova/practical-graph-mining-with-R/PracticalGraphMiningWithR.html#SampleChapters


  
