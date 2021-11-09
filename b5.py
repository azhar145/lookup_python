from pyspark import SparkContext
sc = SparkContext()
n=sc.textFile('/home/az2/g.txt')
print(n.take(2))
