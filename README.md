# ApacheSpark

Apache Spark is a lightning fast real-time processing framework. It does in-memory computations to analyze data in 
real-time.Apache Spark supports interactive queries and iterative algorithms also. Apache Spark has its own cluster 
manager, where it can host its application. It leverages Apache Hadoop for both storage and processing. It uses HDFS
 (Hadoop Distributed File system) for storage and it can run Spark applications on YARN as well
 
## Apache Spark Vs Hadoop

<p>the key difference between Hadoop MapReduce and Spark lies in the 
approach to processing: Spark can do it in-memory, while Hadoop 
MapReduce has to read from and write to a disk. As a result, the speed 
of processing differs significantly – Spark may be up to 100 times 
faster</p> 

<b>Task hadoop is good for</b>

<p>Linear processing of huge data sets. Hadoop MapReduce allows parallel
 processing of huge amounts of data. It breaks a large chunk into 
 smaller ones to be processed separately on different data nodes and 
 automatically gathers the results across the multiple nodes to return 
 a single result. In case the resulting dataset is larger than available
 RAM, Hadoop MapReduce may outperform Spark</p>

<b>Task Spark is good for</b>

<ul>
    <li>f the task is to process data again and again – Spark defeats 
    Hadoop MapReduce. Spark’s Resilient Distributed Datasets (RDDs) 
    enable multiple map operations in memory, while Hadoop MapReduce 
    has to write interim results to a disk.</li>
    <li>If a business needs immediate insights, then they should opt 
    for Spark and its in-memory processing.</li>
    <li>Spark’s computational model is good for iterative computations 
    that are typical in graph processing. And Apache Spark has GraphX – 
    an API for graph computation.</li>
    <li>< Spark has MLlib – a built-in machine learning library, while Hadoop needs a third-party to provide 
    it. MLlib has out-of-the-box algorithms that also run in memory.</li>
    <li>Joining datasets. Due to its speed, Spark can create all 
    combinations faster, though Hadoop may be better if joining of very
     large data sets that requires a lot of shuffling and sorting is 
     needed.</li>
</ul>
 
## Apache Spark Components

<b>Core Components</b> <p>Spark Core is the underlying general execution engine for spark platform that all other 
functionality is built upon. It provides In-Memory computing and referencing datasets in external storage systems.</p>

<b>Spark SQL</b> <p>Spark SQL is a component on top of Spark Core that introduces a new data abstraction called 
SchemaRDD, which provides support for structured and semi-structured data.</p>

<b>Spark Streaming</b> <p>Spark Streaming leverages Spark Core's fast scheduling capability to perform streaming 
analytics. It ingests data in mini-batches and performs RDD (Resilient Distributed Datasets) transformations on those 
mini-batches of data.</p>

<b>Mlib</b> <p>MLlib is a distributed machine learning framework above Spark because of the distributed memory-based 
Spark architecture. It is, according to benchmarks, done by the MLlib developers against the Alternating Least Squares
 (ALS) implementations. Spark MLlib is nine times as fast as the Hadoop disk-based version of Apache 
 Mahout (before Mahout gained a Spark interface).</p>

<b>Graphs</b> <p>GraphX is a distributed graph-processing framework on top of Spark. It provides an API for expressing 
graph computation that can model the user-defined graphs by using Pregel abstraction API. It also provides an optimized 
runtime for this abstraction.</p>
 
 
 
## RDD ( Resilient Distributed Datasets )
 
<p>
Resilient Distributed Datasets (RDD) is a fundamental data structure of 
Spark. It is an immutable distributed collection
of objects. Each dataset in RDD is divided into logical partitions, 
which may be computed on different nodes of the 
cluster. This concept of spark makes it have faster and effecient map 
reduce operations. RDD can store single values & Key value pairs. 

With key value type of RDD, we can do SQL like things such as
joins, rightJoins, leftJoins and so on
</p> 

### Creating RDD

RDD can be created in 2 ways as follows
<ol>
    <li>Parallelizing an existing collection in the driver program</li>
    <li>Referencing a dataset in an external storage such as HDFS, 
    Hbase or so</li>
</ol>

### Transformations and actions

<b> Transformations </b> <p>These are the operations, which are applied 
on a RDD to create a new RDD. Filter, groupBy 
and map are the  examples of transformations.</p>

<b>Sample Transformations /b>

<ol>
   <li>map(lambda x:x^x): Map function takes a function as an argument 
   and applies transformation to all values in EDD </li>
   <li>reduceByKey(lambda x,y: x+y): reduces RDD to a single value 
   based on the reducer function provided</li>
   <li>groupByKey(): Group values by key</li>
   <li>sortByKey(): Sort RDD by key values</li>
   <li>flatMap(): takes a lambda function. it flattens the output value
   and runs the map function over it</li>
</ol>

<b>Actions</b> <p>These are the operations that are applied on RDD, 
which instructs Spark to perform computation and 
send the result back to the driver. which is a python object </p>

<b>Sample Actions</b>

<ol>
   <li>countByValue(): gets counts for unique values in dataset </li>
</ol>

```pyspark
 data = sc.textFile('file:///Users/PycharmProjects/ApacheSpark/data-master/retail_db/order_items')
 To get the first element of RDD 
 data.first()

 To get the first 10 element of RDD 
 data.take(10)

 Convert RDD to python collection
 data.collect()

 Convert Collections to RDD
 collection = [1,2,3,4,5]
 rddCollection = sc.parallelize(collection)
```


### Lazy evaluations and Directed Acyclic Graph (DAG)

Transformations are lazy in nature meaning when we call some operation in RDD, it does not execute immediately. 
Spark maintains the record of which operation is being called(Through DAG).

Since transformations are lazy in nature, so we can execute operation any time by calling an action on data. Hence, 
in lazy evaluation data is not loaded until it is necessary.

## SparkSQL 

<p>Spark SQL is a Spark module for structured data processing. One use of Spark SQL is to execute SQL queries. Spark SQL
 can also be used to read data from an existing Hive installatio</p>

### Reading files of different formats

In Spark, you can load data from various formats directly such as 
Parquet (column storage format freely available in Hadoop), ORC (Optimized row columnar) file use by Hive, json, csv and so on


### DataFrame

<p>A DataFrame is a Dataset organized into named columns. It is conceptually equivalent to a table in a relational 
database or a data frame in R/Python, but with richer optimizations under the hood</p>

#### Preview data in DataFrame

```python
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('Df_test').getOrCreate()
ordersDF= spark.read.csv('/Users/186181152/PycharmProjects/ApacheSpark/data-master/retail_db_json/orders/part-r-00000-990f5773-9005-49ba-b670-631286032674',header=True)
print( ordersDF.first())

# Get summary of Data (min, max, count, std dev, mean)
ordersDF.summary()

# Get number of records in Dataframe
ordersDF.count()

# convert to python list
ordersDF.collect()
```

#### Creating data frames from various sources

##### Hive Table

To connect to Hive table, we need to create Spark Session in a way that supports it.

```pyspark

# Option 1  
from pyspark import SparkContext, SparkConf
from pyspark.conf import SparkConf
from pyspark.sql import SparkSession, HiveContext

sparkSession = (SparkSession
                .builder
                .appName('example-pyspark-read-and-write-from-hive')
                .config("hive.metastore.uris", "thrift://localhost:9083", conf=SparkConf())
                .enableHiveSupport()
                .getOrCreate()
                )

# option 2 
# First place hive-site.xml in pyspark's conf/ directory and then in code
from pyspark.sql import HiveContext
sqlContext = HiveContext(sc) 

# use an existing table from db
orders = spark.read.table('dbName.tableName')   

# show schema
orders.printSchema() 
orders.show()

# we cna run an SQL query as well
spark.sql('select * from retail.orders').printSchema()
```
Once we have specified the Hive URL in Spark Session, we can use Hive in our Application as follows

```python

```

##### JSON Data Sources

##### Reading table from mySQL over JDBC

<p>WIth JDBC, tables from remote databases can be loaded as DataFrame 
or Spark SQL temporary view.</p>

<b>config</b> <p>To connect with JDBC, we need to make sure JDBC Jar 
file is registered using --packages or --jars and pass 
--driver-class-path while launching pyspark . In pycharms we can either 
move the relevant jars  to $SPARK_HOME/jars</p>




Once data is created, we can process data using two approaches

1. Native Data Frame API's
2. Register as temp table and run queries using spark sql



#### DataFrame in Python

<p>A Data frame is a two-dimensional data structure, i.e., data is aligned in a tabular fashion in rows and columns.
</p>

<b>Features of Dataframe</b>

<ul>
    <li>Potentially columns are of different types</li>
    <li>Size – Mutable</li>
    <li>Labeled axes (rows and columns)</li>
    <li>Can Perform Arithmetic operations on rows and columns</li>
</ul>

###### Creating Python ND Array

You can create python dataframe from dictionary of NDArrays or Lists

```python
# Creating Dataframe from Arrays
import pandas as pd
data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
df = pd.DataFrame(data)
print df

# Creating Dataframe from List of Dict

import pandas as pd
data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data)
print df
```

this will create a Datafram with standard index 0,1,2,3 

You can pass custom index to Dataframe like this

```python
df1 = pd.DataFrame(data, index=['first', 'second'], columns=['a', 'b'])
```

Creating a Dataframe from Dict of series

```python
import pandas as pd

d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
   'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
```

##### Addition and Deletion of Rows and columns in Dataframe

```python

# Addition of Column
df['three']=pd.Series([10,20,30],index=['a','b','c'])

# Deletion of Column
del df['one']

# selection of Row
df.loc['b']

# Selection by integer location
df.iloc[2]

# Multiple rows can be selected using ‘ : ’ operator.
df[2:4]

# Addition of Rows
df = pd.DataFrame([[1, 2], [3, 4]], columns = ['a','b'])
df2 = pd.DataFrame([[5, 6], [7, 8]], columns = ['a','b'])
df = df.append(df2)

# Drop rows with label 0
df = df.drop(0)
```

You can also do head, tail, & transponse operations on data frames

Also, you can do some basic statistics in Dataframe

```python
import pandas as pd
import numpy as np
 
#Create a Dictionary of series
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack',
   'Lee','David','Gasper','Betina','Andres']),
   'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])
}
 
#Create a DataFrame
df = pd.DataFrame(d)

# Sum
df.sum(1)

# Mean
df.mean()

# Standard Deviations
df.std()

# Summarize the data
df.describe()
```

##### Pandas function applications

<p>To apply your own or another library’s functions to Pandas objects, you should be aware of the three important methods. The methods have been discussed below. The appropriate method to use depends on whether your function expects to operate on an entire DataFrame, row- or column-wise, or element wise.
</p>
<ul>
<li>Table wise Function Application: pipe()</li>
<li>Row or Column Wise Function Application: apply()</li>
<li>Element wise Function Application: applymap()</li>
</ul>

## Performance Tuning

### Caching Data in-memory

<p>Spark SQL can cache tables using an in-memory columnar format by 
calling spark.catalog.cacheTable("tableName") or dataFrame.cache(). 
Then Spark SQL will scan only required columns and will automatically 
tune compression to minimize memory usage. 
You can call spark.catalog.uncacheTable("tableName") to remove the 
table from memory. Configuration of in-memory caching can be done using
the setConf method on SparkSession or by running SET key=value commands 
using SQL.</p>

### Broadcast Variables

<p>
Broadcast variables allow the programmer to keep a read-only variable 
cached on each machine rather than shipping a copy of it with tasks. 
They can be used to give every node a copy of a large input dataset 
in an efficient manner. Spark also attempts to distribute broadcast 
variables using efficient broadcast algorithms to reduce communication 
cost.
</p>

<p>Broadcast variables help in storing a lookup table inside the memory
 which enhances the retrieval efficiency when compared to an RDD 
 lookup().</p>

```python
broadcastDict = sc.broadcast(v)
```

<b>We should avoid making changes ot the variable after broadcasting it
to ensure same copy is available for each worker node</b>


### Minimize data transfers using Broadcast

<p>Using Broadcast Variable- Broadcast variable enhances the efficiency
 of joins between small and large RDDs.</p>

<p>Using Accumulators – Accumulators help update the values of variables
 in parallel while executing.</p>

### Accumulators




 