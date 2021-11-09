import pyspark
sc = pyspark.SparkContext('local[*]')

txt = sc.textFile('/home/az2/Downloads/tr2.txt')

counts = txt.take(1)
print ("Number of elements in RDD -> %i" % (counts))


# print("Txt count is:" + str(txt.count()))
# print(txt.take(1))
# python_lines = txt.filter(lambda line: 'python' in line.lower())
# print("word python count is:" + str(python_lines.count()))
