
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

# Select, Add, delete columns in dataframe

# Selecting a column
print(df.select('first_name').show())
# Selecting multiple columns
print(df.select(['first_name',df.id.between(5,10)]).show())