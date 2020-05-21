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
#mean_df = df.select('salary').agg(F.mean())
#print(mean_df.show())


# get the average salary for Russia
#df_filtered  = df.filter(df('country') == 'Russia').groupBy()

# filtering on String
print(df.filter(df.country == 'Russia').show())

# filtering on integer
print(df.filter(df.id < 50).show())

# filtering on multiple conditions
print(df.filter((df.id < 50) & (df.id > 30)).show())

# filtering on timestamp

startDate = "2016-02-02 14:09:48"
endDate = "2016-02-02 22:43:17"
print(df.filter(df['registration_dttm'].between(startDate, endDate)).show())



# filtering on date

def transform(row):
    print(row)
    return row
rdd = df.select(df.birthdate).rdd
rdd_clean = rdd.map(lambda x: transform(list(x)[0])).collect()
rdd_DF = rdd.map(lambda x: (x,)).toDF()
print(rdd_DF.show())

# replace empty String literal with something
df = df.withColumn("birthdate",F.when(df.birthdate != '',df.birthdate).otherwise("05/05/2020"))

# Drop empty String literals from birthdate column
df = df.filter(df.birthdate != '')
print(df.show())
df = df.withColumn("birthdate", to_date(df.birthdate,'mm/dd/yyyy'))
print(df.show())
# filter on the birthdate
print(df.filter(df['birthdate'].between("1970-02-01","1975-02-02")).show())

# drop String literal and cast to integer
df = df.withColumn("cc", F.when(df.cc != '', df.cc).otherwise('0'))
df = df.withColumn("cc", df.cc.cast(IntegerType()))
print(df.printSchema())

