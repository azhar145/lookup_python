from pyspark.sql.functions import year, month, dayofmonth
from pyspark.sql import SparkSession
from datetime import date, timedelta
from pyspark.sql.types import IntegerType, DateType, StringType, StructType, StructField

appName = "PySpark Partition Example"
master = "local[8]"

# Create Spark session with Hive supported.
spark = SparkSession.builder \
    .appName(appName) \
    .master(master) \
    .getOrCreate()

print(spark.version)
# Populate sample data
start_date = date(2019, 1, 1)
data = []
for i in range(0, 50):
    data.append({"Country": "CN", "Date": start_date +
                 timedelta(days=i), "Amount": 10+i})
    data.append({"Country": "AU", "Date": start_date +
                 timedelta(days=i), "Amount": 10+i})

schema = StructType([StructField('Country', StringType(), nullable=False),
                     StructField('Date', DateType(), nullable=False),
                     StructField('Amount', IntegerType(), nullable=False)])

df = spark.createDataFrame(data, schema=schema)
df.show()
print(df.rdd.getNumPartitions())
df.write.mode("overwrite").csv("/home/az2/Downloads/uu/pyspark_example.csv", header=True)
