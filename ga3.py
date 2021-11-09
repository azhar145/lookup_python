import random
NUM_SAMPLES = 100000000
def inside(p):
 x, y = random.random(), random.random()
 return x*x + y*y < 1


from pyspark import SparkContext
sc =SparkContext()

count = sc.parallelize(range(0, NUM_SAMPLES)).filter(inside).count()
pi = 4 * count / NUM_SAMPLES
print("Pi is roughl", pi)
