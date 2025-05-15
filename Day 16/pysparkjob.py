from pyspark.sql import SparkSession

# create a SparkSession
spark = SparkSession.builder.appName("Sample Superstore").getOrCreate()

# read the CSV file
df = spark.read.csv("C:\\Users\\nikhi\\OneDrive\\Desktop\\test\\Sample - Superstore.csv", 
                    header=True, inferSchema=True)

# select only the first 5 columns
df = df.select(df.columns[:5])

# write the output to a new CSV file
df.write.csv("C:\\Users\\nikhi\\OneDrive\\Desktop\\test\\mysales.csv", header=True)

# stop the SparkSession
spark.stop()