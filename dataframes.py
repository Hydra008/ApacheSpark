import os
os.environ['PYSPARK_PYTHON'] = '/Library/Frameworks/Python.framework/Versions/3.6/bin/python3'
from pyspark.sql.session import SparkSession
from pyspark.sql import functions as f
spark = SparkSession.builder \
    .master("local") \
    .appName("Dataframes - Test") \
    .getOrCreate()

#  Created DF from text - each line representing a string value
movieRatingsDF = spark.read.text("file:///Users/186181152/PycharmProjects/ApacheSpark/ml-100k/u.data")
names = spark.read.text('file:///Users/186181152/PycharmProjects/ApacheSpark/ml-100k/u.item')
print(names.show())
# Giving Structure to DF
structuredRatings = movieRatingsDF.select(f.split(movieRatingsDF.value,"\t")).rdd\
    .flatMap(lambda x: x).toDF(schema=["user_id","item_id","ratings", "timestamp"])
movieNames = names.select(f.split(names.value,"\t")).rdd.flatMap(lambda x: (x[0],x[1])).toDF(schema=['item_id', 'movie_name'])

# converting ratings to integer
structuredRatings = structuredRatings.withColumn("ratings", structuredRatings.ratings.cast("int"))
print(structuredRatings.show())
print(movieNames.show())

# Calculate Avg ratings for all movies
avgRatings = structuredRatings.groupBy().mean('ratings')
print(avgRatings.show())

# calculate avg ratings for each movie
avgRatingsMovie = structuredRatings.groupBy('item_id').agg({'ratings': 'mean'}).sort('avg(ratings)', ascending=False)
print(avgRatingsMovie.show())

