from pyspark.sql import SparkSession,SQLContext

# Created a spark session
spark = SparkSession.builder \
           .master('local') \
           .appName('My App') \
           .getOrCreate()
print(spark)

# Read a parquet file

sparkContext = spark.sparkContext
sc = SQLContext(sparkContext)

df = sc.read.parquet('../data/userdata1.parquet')
print(df)

# Peek Data, head and tail
print(df.show())
print(df.head(5))
print(df.take(3))

# print columns
print(df.columns)

# print col, row length
print(len(df.columns))
print(df.count())

# Descriptive Statistics
print(df.describe().show(5))

# Print Schema
print(df.printSchema())
print(df.schema)