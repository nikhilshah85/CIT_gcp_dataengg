from pyspark.sql import SparkSession

# create a SparkSession
spark = SparkSession.builder.appName("Read CSV Data").getOrCreate()

# read the CSV file
df = spark.read.csv("C:\\Users\\nikhi\\OneDrive\\Desktop\\test\\1_sales.csv", 
                    header=True, 
                    inferSchema=True)

# show the data
df.show()

# stop the SparkSession
spark.stop()