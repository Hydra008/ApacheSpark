from pyspark.sql import SparkSession,SQLContext
from pyspark.sql import functions as F

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

# Sort country field in asc and dsc
df = df.orderBy('country', ascending=True)
print(df.show())

# Sort integer field in asc and dsc
df = df.orderBy('id', ascending=False)
print(df.show())
df = df.sort('id')
print(df.show())

# sort data field in asc and dsc
df = df.orderBy('registration_dttm',ascending=True)
print(df.show())
# sort by column names
df = df.select(sorted(df.columns))
print(df.show())

# Sort ascending in 1 column and descending in other
df = df.orderBy(['gender','country'], ascending=[False,True])
print(df.show())