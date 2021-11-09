from pyspark import SparkContext
sc = SparkContext("local", "Map app")
words = sc.parallelize (
   ["scala", 
   "java55", 
   "hadoop", 
   "spark",
   "spark", 
   "akka",
   "spark vs hadoop", 
   "pyspark",
   "pyspark and spark"]
)
words_map = words.map(lambda x: (x, 1))
mapping = words_map.collect()
print "Key value pair -> %s" % (mapping)
