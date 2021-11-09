from pyspark import SparkContext as sc
RDDread = sc.textFile ("/home/az2/Downloads/tr2.txt")
# print(RDDread.First ())
print "Adding all the elements -> %i" % (RDDread.First ())

