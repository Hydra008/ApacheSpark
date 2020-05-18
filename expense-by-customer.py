import os

os.environ['PYSPARK_PYTHON'] = '/Library/Frameworks/Python.framework/Versions/3.6/bin/python3'
from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("WordCount")
sc = SparkContext(conf=conf)


def parseLine(lineData):
    line = lineData.split(',')
    custId = line[0]
    itemId = line[1]
    price = float(line[2])
    return custId, price


input = sc.textFile("file:///Users/186181152/PycharmProjects/ApacheSpark/customer-orders.csv")
print(input.take(15))

customerData = input.map(parseLine)
print(customerData.take(15))

customerExpense = customerData.reduceByKey(lambda x,y: x + y)
print(customerExpense.take(15))

temp = customerExpense.map(lambda x: (x[1], x[0])).sortByKey(False)
print(temp.take(15))
