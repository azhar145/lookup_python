from pyspark import SparkContext
from operator import add
sc = SparkContext("local", "Reduce app")
nums = sc.parallelize([1, 2, 3, 4, 105])
adding = nums.reduce(add)
print "Adding all the elements -> %i" % (adding)
