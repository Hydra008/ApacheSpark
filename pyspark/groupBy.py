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

# Group by 1 column
print(df.groupBy('country').avg('salary').show())

# Group by 2 column with aggregation
print(df
      .groupBy(['country', 'gender'])
      .avg('salary')
      .orderBy('country')
      .show()
      )

# use df.agg function
print(df
      .groupBy(['country', 'gender'])
      .agg({'salary': 'avg'})
      .orderBy('country')
      .show()
      )
