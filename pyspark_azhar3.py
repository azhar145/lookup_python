from pyspark import SparkContext
sc = SparkContext("local", "count app")
words = sc.parallelize (
   ["scala",
   "java",
   "hhhhh",
   "gggfff",
   "hadoop",
   "spark",
   "akka",
   "spark vs hadoop",
   "pyspark",
   "pyspark and spark"]
)
counts = words.count()
print "Number of elements in RDD -> %i" % (counts)



from pyspark.sql import SparkSession
spark = SparkSession.builder.master("local[*]").getOrCreate()
sc = spark.sparkContext
textRDD1 = sc.textFile("/home/az2/Downloads/tr2.txt")
textRDD2 = spark.read.text('/home/az2/Downloads/tr2.txt').rdd

Print(textRDD1.take(5))
Print(textRDD2.take(5))
