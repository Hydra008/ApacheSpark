from pyspark.sql import SparkSession,SQLContext
from pyspark.sql.types import IntegerType, FloatType
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
print(df)

# Handle duplicate values
print(df.drop_duplicates().count())

# Handling missing data
print(df.fillna(0).show())
print(df.dropna().show())

# fill missing values in specefic columns
print(df.fillna({'cc':'6767119071901597' }).show())

# Changing data type in the DF
df1 = df.withColumn("salary",  df["salary"].cast(FloatType()))
print(df1.show())
print(df1.printSchema())

# replace null values with mean salary
print(F.avg(df1.salary))
# df1 = df1.fillna()
