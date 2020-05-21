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

