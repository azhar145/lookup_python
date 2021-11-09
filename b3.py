from pyspark import SparkContext
sc = SparkContext()
n=sc.textFile('/home/hadoop/g.txt')
n.take(2)
