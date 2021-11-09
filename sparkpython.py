from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("appName").getOrCreate()
sc = spark.sparkContext
rdd = sc.parallelize([1,2,3,4,5,6,7])
print(rdd.count())
