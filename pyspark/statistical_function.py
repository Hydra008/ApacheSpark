from pyspark.sql import SparkSession,SQLContext

import os
os.environ['PYSPARK_PYTHON'] = '/Library/Frameworks/Python.framework/Versions/3.6/bin/python3'

from pyspark.sql.functions import to_date
from pyspark.sql.types import IntegerType, FloatType, TimestampType
from pyspark.sql import functions as F

# Created a spark session
spark = SparkSession.builder \
           .master('local[*]') \
           .appName('My App') \
           .getOrCreate()
print(spark)

# Read a parquet file

sparkContext = spark.sparkContext
sc = SQLContext(sparkContext)

df = sc.read.parquet('../data/userdata1.parquet')
print(df.show())

# Mean
mean_df = df.agg({'salary': 'mean'})
print(mean_df.collect()[0][0])

# Using describe
described_df = df.select(['salary']).describe()
print(described_df.collect()[1][1])

# multiple aggregate functions
mean_df = df.select('salary').agg(F.mean())
print(mean_df.show())









